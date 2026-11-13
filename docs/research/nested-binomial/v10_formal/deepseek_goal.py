#!/usr/bin/env python3
"""Persistent research goal whose action decisions are made by DeepSeek.

The executor provides only bounded research, library, Lean and publication tools.
It never selects a mathematical subgoal or authors/edits a proof body.
"""
from __future__ import annotations

import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
import uuid
import gzip

from deepseek_goal_budget import GoalBudgetExceeded
from deepseek_proof_loop import ROOT, MODEL, api, completion_text, digest, load_api_settings
from deepseek_lean_harness import analyze, accepted as lean_accepted, source_context
from deepseek_publication import PublicationBlocked, authorize, synchronize, push_verified
from deepseek_method_research import MethodResearch

REPO = ROOT.parents[3]
NOTES = ROOT.parent
MATHLIB = Path(os.environ.get('DEEPSEEK_MATHLIB', '/workspace/.cloud-setup/lean/mathlib'))
ELAN_HOME = os.environ.get('ELAN_HOME', '/workspace/.cloud-setup/lean/elan')
SKILL = REPO / '.agents/skills/deepseek-goal/SKILL.md'
GOAL = SKILL.with_name('goal.json')
DEFAULT_RUN = Path('/workspace/.cloud-setup/deepseek-goal/nested-binomial-cf')
PROGRESS = NOTES / 'DEEPSEEK_GOAL_PROGRESS.md'
REGISTRY = ROOT / 'goal_verified_modules.json'
FORBIDDEN = (r'\b(sorry|admit|axiom|native_decide|unsafe|initialize|run_cmd|run_tac|run_elab|'
             r'run_io|liftIO|elab|macro|macro_rules|syntax|notation|attribute|set_option)\b|#|\b(IO|Lean|System)\.')


def lean_environment():
    env = os.environ.copy()
    env['ELAN_HOME'] = ELAN_HOME
    env['PATH'] = str(Path(ELAN_HOME) / 'bin') + os.pathsep + env['PATH']
    env.pop('MISTRAL_API_KEY', None)
    return env


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(path)


MAX_COMPRESSED_CONTENT = 8 * 1024 * 1024


def rooted(base, name, allow_compressed=False):
    if not isinstance(name, str) or Path(name).is_absolute():
        raise ValueError('Expected a relative research/library path')
    path = (base / name).resolve()
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError('File is outside the allowed research/library root or missing')
    if path.suffix not in {'.lean', '.md', '.py', '.json', '.txt', '.toml'} and not (
            allow_compressed and path.name.endswith('.json.gz')):
        raise ValueError('Unsupported research/library file type')
    return path


def excerpt(path, start=1, count=160):
    if type(start) is not int or type(count) is not int or start < 1 or not 1 <= count <= 250:
        raise ValueError('Use a positive start and 1..250 lines')
    if path.name.endswith('.json.gz'):
        with gzip.open(path,'rb') as source: data=source.read(MAX_COMPRESSED_CONTENT+1)
        if len(data)>MAX_COMPRESSED_CONTENT:raise ValueError('Compressed research exceeds the bounded 8 MiB inspection limit')
        return '\n'.join(f'{i}: {line}' for i,line in enumerate(data.decode('utf-8').splitlines(),1)
                         if start<=i<start+count)[:32000]
    lines = []
    with path.open() as source:
        for index, line in enumerate(source, 1):
            if index >= start:
                lines.append(f'{index}: {line.rstrip()}')
            if index >= start + count - 1:
                break
    return '\n'.join(lines)[:32000]


def local_dependencies(imports, base=None):
    base = ROOT if base is None else base
    ordered, active, done = [], set(), set()
    def visit(name):
        if name in active:
            raise ValueError('Cyclic local Lean imports')
        if name in done:
            return
        path = rooted(base, name + '.lean')
        active.add(name)
        for dependency in re.findall(r'^import ([A-Za-z][A-Za-z0-9_.]*)\s*$', path.read_text(), re.M):
            if '.' not in dependency and (base / (dependency + '.lean')).is_file():
                visit(dependency)
        active.remove(name); done.add(name); ordered.append(path.name)
    for name in re.findall(r'^import ([A-Za-z][A-Za-z0-9_.]*)\s*$', imports, re.M):
        if not name.startswith('Mathlib.'):
            visit(name)
    return ordered


def validate_job(config, targets, base=None):
    base = ROOT if base is None else base
    if not isinstance(config, dict) or set(config) - {'module', 'imports', 'definitions', 'goals', 'local_dependencies'}:
        raise ValueError('Invalid fixed-job schema')
    module = config.get('module', '')
    if not isinstance(module, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', module):
        raise ValueError('Invalid module name')
    if (base / (module + '.lean')).exists():
        raise ValueError('Existing Lean modules are immutable; choose a new module')
    imports = config.get('imports', '')
    if not isinstance(imports, str) or not imports.strip():
        raise ValueError('imports must be a Lean import string')
    for line in imports.splitlines():
        if line.strip() and not re.fullmatch(r'import (Mathlib\.[A-Za-z0-9_.]+|[A-Za-z][A-Za-z0-9_]*)', line):
            raise ValueError('Only specific Mathlib imports and existing local modules are allowed')
    definitions = config.get('definitions', '')
    if not isinstance(definitions, str) or re.search(FORBIDDEN, definitions):
        raise ValueError('Unsupported fixed definitions')
    if re.search(r'(?m)^\s*(import|namespace|end|instance|opaque|constant|theorem|lemma|example)\b', definitions):
        raise ValueError('Definitions must remain root-level and cannot introduce commands or instances')
    goals = config.get('goals')
    if not isinstance(goals, list) or not 1 <= len(goals) <= 4:
        raise ValueError('A focused module needs 1..4 fixed theorem declarations')
    names = set()
    for goal in goals:
        if not isinstance(goal, list) or len(goal) != 2:
            raise ValueError('Each goal must be [name, theorem declaration]')
        name, statement = goal
        if (not isinstance(name, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', name)
                or name in names or not isinstance(statement, str)
                or not statement.startswith('theorem ' + name + ' ')
                or ':=' in statement or re.search(FORBIDDEN, statement)
                or re.search(r'\n\s*(import|namespace|end|def|theorem|lemma|instance)\b', statement)):
            raise ValueError('Invalid or executable theorem declaration; types only, no proof bodies')
        names.add(name)
    for target in targets:
        if module == target['module']:
            if definitions.strip() or goals != [[target['name'], target['statement']]]:
                raise ValueError('Final target declaration/definitions do not match the immutable goal')
            if digest(target['statement']) != target['statement_sha256']:
                raise ValueError('Frozen target hash mismatch')
    return {**config, 'definitions': definitions,
            'local_dependencies': local_dependencies(imports, base)}


TOOLS = '''Choose ONE action and return JSON {"action":NAME,"arguments":OBJECT,"reason":SHORT_SUMMARY}.
list_research: {} -> authorized filenames.
read_research: {path,start?,count?}; paths relative to docs/research/nested-binomial.
  start is 1-based and count is at most 250. Reuse working_memory before rereading.
search_research: {query,glob?}; literal search of research only.
read_mathlib: {path,start?,count?}; paths relative to pinned mathlib/Mathlib.
list_mathlib: {glob?}; actual pinned Mathlib filenames, to avoid guessing paths.
search_mathlib: {query,glob?}; literal search of actual pinned Mathlib declarations.
cache_mathlib: {path}; fetch the compiled cache for one actual Mathlib/*.lean file.
propose_job: {config:{module,imports,definitions,goals:[[name,theorem]],local_dependencies?},
              why_needed,extra_context:[research_paths],library_reference:[Mathlib_relative_paths]}.
  You author the job. Executor validates syntax/boundaries, asks a separate DeepSeek scope review,
  freezes the types, and returns job_id. No proof bodies here. Never weaken the final target.
inspect_job: {job_id}; see the frozen config and actual last result.
diagnose_job: {job_id}; classified failures, exact source locations, partial successes and reusable candidates.
update_job_context: {job_id,extra_context?,library_reference?}; add actual sources without changing frozen theorem types.
review_failure: {job_id}; ask a separate DeepSeek repair critic for a different strategy and pass its notes to the worker.
set_plan: {milestones:[{id,objective,depends_on:[],modules:[]}]}; persist a dependency plan; evidence status is machine-derived.
prove_job: {job_id,attempts?}; choose 1..20 proof attempts (default 5), then reconsider using real feedback.
publish: {}; verify all accepted modules and commit/push ONLY their artifacts to authorized PR branch.
sync_research: {}; fetch/merge the authorized branch, preserving verified sources; conflicts stop with actual diagnostics.
github_status: {}; inspect the authorized research PR and head check-runs. GitHub checks are observations, not Lean proof evidence.
inspect_methods: {}; real attempt metrics and recorded method hypotheses/evaluations.
propose_method: {id,title,kind,hypothesis,procedure:[],success_criterion,failure_criterion,references:[]}.
  kind is mathematical_strategy, formalization or certificate_design. References are existing research paths.
use_method: {method_id,job_id?}; apply a hypothesis to planning and optionally a ready/failed/interrupted job, preserving its fixed type.
evaluate_method: {method_id,job_id,conclusion,decision}; compare real trial evidence; decision is keep/revise/drop, not a proof or causal finding.
checkpoint: {summary}; retain a brief research note, then CONTINUE; it does not end the goal.
request_completion: {}; succeeds ONLY when both exact final targets are Lean-verified and published.
There is no done action, arbitrary shell, arbitrary file write, or permission to edit existing proofs.
Read/search tools give you source. You choose every mathematical task. Never ask Codex to choose it.
Return compact actionable JSON, not a long essay. A result on one lemma is progress, not completion.
'''


class GoalAgent:
    run_lock_fd = None

    def __init__(self, run_dir=DEFAULT_RUN, goal_path=GOAL):
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.run_dir.chmod(0o700)
        self.goal = json.loads(Path(goal_path).read_text())
        self.goal_hash = digest(json.dumps(self.goal, sort_keys=True))
        self.state_path = self.run_dir / 'state.json'
        self.history = []
        self.load_state()

    def load_state(self):
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text())
            if self.state['goal_hash'] != self.goal_hash:
                raise ValueError('Goal changed: start a separate goal; do not weaken an active contract')
        else:
            self.state = {'goal_hash': self.goal_hash, 'status': 'not_started', 'steps': 0,
                          'jobs': {}, 'notes': [], 'last_observation': None, 'publication': None}
        if 'working_memory' not in self.state:
            self.state['working_memory'] = []
            for path in sorted(self.run_dir.glob('*.action.json')):
                entry = json.loads(path.read_text())
                self.remember(entry['action'], entry['observation'])
        for job in self.state['jobs'].values():
            if job['status'] in {'failed', 'interrupted'}:
                job['harness_recovery'] = {'reusable_seed_theorems': list(self.recover_seeds(job)),
                                           'recompilation_required': True}
        self.methods = MethodResearch(self.state,self.run_dir,NOTES,ROOT,lambda path:rooted(NOTES,path))

    def remember(self, action, observation):
        name, args = action.get('action'), action.get('arguments', {})
        if name not in {'read_research', 'read_mathlib', 'search_research', 'search_mathlib', 'list_research', 'list_mathlib'} or 'tool_error' in observation:
            return
        identity = dict(args)
        if name.startswith('read_'): identity.pop('count', None)
        key = name + ':' + json.dumps(identity, sort_keys=True)
        memory = [m for m in self.state.get('working_memory', []) if m['key'] != key]
        text = json.dumps(observation, ensure_ascii=False)[:20000]
        memory.append({'key': key, 'action': name, 'arguments': args,
                       'observed_tool_result': text, 'not_a_verification': True})
        while len(memory) > 16 or sum(len(m['observed_tool_result']) for m in memory) > 160000:
            memory.pop(0)
        self.state['working_memory'] = memory

    def save(self):
        self.state['updated_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        write_json(self.state_path, self.state)
        rows = ['# DeepSeek goal progress', '', self.goal['objective'], '',
                '- Decision maker: ' + MODEL, '- Status: ' + self.state['status'],
                '- Actions: ' + str(self.state['steps']),
                '- Final success requires both frozen targets and verified GitHub publication.', '',
                '| Module | Actual status |', '| --- | --- |']
        if self.state.get('run_origin') == 'codespaces':
            rows[4:4] = ['- New Codespaces run based on checked-in Lean modules. The earlier '
                         '179-action state was not imported.']
        rows += [f"| {j['config']['module']} | {j['status']} |" for j in self.state['jobs'].values()]
        PROGRESS.write_text('\n'.join(rows) + '\n')
        self.methods.save_public()

    def recent_version_notes(self):
        """Names only: let DeepSeek choose which new research to read and verify."""
        entries = []
        for path in NOTES.glob('*.md'):
            match = re.fullmatch(r'(?:V|v|PROGRESS_v)([0-9]+)[A-Za-z0-9_.-]*\.md', path.name)
            if match and path.is_file():
                entries.append((int(match.group(1)), path.name))
        return [name for _, name in sorted(entries, key=lambda pair: (pair[0], pair[1]), reverse=True)[:12]]

    def snapshot(self):
        budget = self.run_dir / 'budget.json'
        generated = ROOT / 'deepseek_generation_checks.json'
        verified = json.loads(generated.read_text())
        return {'goal': self.goal, 'status': self.state['status'], 'steps': self.state['steps'],
                'recent_version_notes': self.recent_version_notes(),
                'jobs': {key: {'module': j['config']['module'], 'status': j['status'],
                              'goals': [g[0] for g in j['config']['goals']], 'why_needed': j['why_needed']}
                         for key, j in self.state['jobs'].items()},
                'job_recovery': {key:j.get('harness_recovery') for key,j in self.state['jobs'].items()
                                 if j.get('harness_recovery')},
                'notes': self.state['notes'][-8:], 'last_observation': self.state['last_observation'],
                'working_memory': self.state.get('working_memory', []),
                'milestone_plan': self.plan_snapshot(),
                'research_methods': self.methods.planning_context(),
                'budget': json.loads(budget.read_text()) if budget.exists() else None,
                'verified_theorem_count': verified['accepted_theorem_count'],
                'verified_module_catalog': [{'module': m['module'], 'theorems': m['theorems']}
                                            for m in verified.get('modules', [])]}

    def decision(self):
        initial = ''
        if not self.history:
            initial = '\nINITIAL RESEARCH:\n' + '\n\n'.join(
                name + '\n' + excerpt(rooted(NOTES, name), 1, 180)
                for name in self.goal['initial_research_files'])
        prompt = SKILL.read_text() + '\n' + TOOLS + '\nCURRENT MACHINE STATE:\n' + json.dumps(self.snapshot(), ensure_ascii=False) + initial
        instruction = ('Resume the saved goal and use working_memory; do not restart already completed inspection.'
                       if self.state['steps'] else 'Start the persistent goal.')
        history = self.history or [{'role': 'user', 'content': instruction + ' You choose the next research action.'}]
        response = api([{'role': 'system', 'content': prompt}, *history])
        step = self.state['steps'] + 1
        write_json(self.run_dir / f'{step:04d}.response.json', response)
        self.history.append({'role': 'assistant', 'content': response['choices'][0]['message']['content']})
        if response['choices'][0].get('finish_reason') != 'stop':
            raise ValueError('No complete action; preserve state and return an actionable final JSON')
        action = json.loads(completion_text(response))
        if not isinstance(action, dict) or not isinstance(action.get('arguments', {}), dict):
            raise ValueError('Expected one action and arguments object')
        return action

    def search(self, base, args):
        query = args.get('query')
        if not isinstance(query, str) or not 1 <= len(query) <= 500:
            raise ValueError('Use a literal search query of 1..500 characters')
        pattern = args.get('glob', '*.lean' if base == MATHLIB / 'Mathlib' else '*')
        result = subprocess.run(['rg', '-n', '-F', '--max-count', '30', '--glob', pattern,
                                 '--', query, '.'], cwd=base, capture_output=True, text=True, timeout=15)
        return {'exit_code': result.returncode, 'output': (result.stdout + result.stderr)[:24000]}

    def check_codespaces_imports(self, config):
        if self.state.get('run_origin') != 'codespaces':
            return
        sources = [(config['module'], config['imports'])]
        sources.extend((name, (ROOT / name).read_text()) for name in config['local_dependencies'])
        for source, text in sources:
            for name in re.findall(r'^import (Mathlib\.[A-Za-z0-9_.]+)\s*$', text, re.M):
                if name == 'Mathlib.Tactic':
                    raise ValueError(f'{source} uses the broad Mathlib.Tactic import, which times out in Codespaces. '
                                     'Use focused imports and keep any slow local module as source context.')
                if not (MATHLIB / (name.replace('.', '/') + '.lean')).is_file():
                    raise ValueError(f'{name} in {source} is absent from pinned mathlib. '
                                     'Check list_mathlib before freezing or retrying the job.')

    def propose(self, args):
        if any(j['status'] == 'verified' for j in self.state['jobs'].values()):
            raise ValueError('Publish verified progress before proposing another module')
        config = validate_job(args.get('config'), self.goal['targets'])
        self.check_codespaces_imports(config)
        if any(j['config']['module'] == config['module'] for j in self.state['jobs'].values()):
            raise ValueError('This module already has a frozen job; inspect/retry it or choose a new module')
        why = args.get('why_needed', '')
        if not isinstance(why, str) or not 10 <= len(why) <= 6000:
            raise ValueError('Explain the concrete dependency on a frozen final target')
        contexts = [rooted(NOTES, p) for p in args.get('extra_context', [])]
        library = [rooted(MATHLIB / 'Mathlib', p) for p in args.get('library_reference', [])]
        if len(contexts) > 8 or len(library) > 4 or any(p.stat().st_size > 300000 for p in contexts + library):
            raise ValueError('Use focused context files; inspect large certificates in slices')
        review = api([{'role': 'user', 'content':
            'Review the following DeepSeek-proposed fixed Lean job against the actual immutable research goal. '
            'Return JSON {verdict:PASS or ISSUES,feedback:...}. This is scope review, not a proof. Reject '
            'tautologies, assumed desired conclusions, disconnected identities or weakened final targets. '
            'Reject restating already-verified generic lemmas without a necessary new data/goal connection. '
            'Allow necessary intermediate lemmas with honest explicit hypotheses. Do not invent mathlib API facts.\n'
            + json.dumps({'goal': self.goal, 'why_needed': why, 'config': config,
                          'existing_verified': self.snapshot()['verified_module_catalog']}, ensure_ascii=False)
            + '\nRESEARCH CONTEXT:\n' + '\n\n'.join(p.read_text() for p in contexts)}])
        verdict = json.loads(completion_text(review))
        job_id = config['module'] + '-' + uuid.uuid4().hex[:8]
        directory = self.run_dir / 'jobs' / job_id
        write_json(directory / 'scope_review.json', review)
        if verdict.get('verdict') != 'PASS':
            return {'accepted': False, 'review': verdict}
        write_json(directory / 'fixed_job.json', config)
        self.state['jobs'][job_id] = {'config': config, 'config_sha256': digest(json.dumps(config, sort_keys=True)),
            'why_needed': why, 'extra_context': [str(p) for p in contexts],
            'library_reference': [str(p) for p in library], 'status': 'ready', 'runs': [], 'review': verdict}
        if self.state.get('active_method_id'):
            self.methods.use({'method_id':self.state['active_method_id'],'job_id':job_id})
        self.save()
        return {'accepted': True, 'job_id': job_id, 'frozen_config': config, 'review': verdict}

    def worker(self, job_id, attempts=5):
        if type(attempts) is not int or not 1 <= attempts <= load_api_settings()['max_attempts']:
            raise ValueError('Choose 1..configured-max proof attempts')
        job = self.state['jobs'][job_id]
        if job['status'] in {'verified', 'published'}:
            return {'status': job['status'], 'result': job.get('result')}
        directory = self.run_dir / 'jobs' / job_id
        config_path = directory / 'fixed_job.json'
        frozen = json.loads(config_path.read_text())
        if digest(json.dumps(frozen, sort_keys=True)) != job['config_sha256'] or frozen != job['config']:
            raise ValueError('Frozen theorem contract changed')
        self.check_codespaces_imports(frozen)
        run = directory / ('run-' + str(len(job['runs']) + 1))
        command = ['lake', 'env', 'env', '-u', 'LD_LIBRARY_PATH', sys.executable,
                   str(ROOT / 'deepseek_goal_worker.py'), job_id,
                   '--job-config', str(config_path), '--run-dir', str(run), '--attempts', str(attempts),
                   '--harness-memory', str(directory / 'failure_memory.json')]
        seeds = self.recover_seeds(job)
        if seeds:
            seed = directory / 'recovered_seed_proofs.json'; write_json(seed, seeds)
            command += ['--seed-proofs', str(seed)]
        for path in job['extra_context']: command += ['--extra-context', path]
        for path in job.get('harness_context', []): command += ['--extra-context', path]
        for path in job.get('method_context', []): command += ['--extra-context', path]
        for path in job['library_reference']: command += ['--library-reference', path]
        job['runs'].append(str(run)); job['status'] = 'running'; self.save()
        env = lean_environment()
        if 'MISTRAL_API_KEY' in os.environ:
            env['MISTRAL_API_KEY'] = os.environ['MISTRAL_API_KEY']
        lock_fds = () if self.run_lock_fd is None else (self.run_lock_fd,)
        with (directory / 'worker.log').open('a') as log:
            interrupted = False
            process = subprocess.Popen(command, cwd=MATHLIB, env=env, stdout=log,
                                       stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                       start_new_session=True, pass_fds=lock_fds)
            try:
                while process.poll() is None:
                    budget = json.loads((self.run_dir / 'budget.json').read_text())
                    if (self.run_dir / 'PAUSE').exists() or time.time() >= budget['deadline']:
                        interrupted = True
                        break
                    time.sleep(.5)
            finally:
                if process.poll() is None:
                    try:
                        os.killpg(process.pid, signal.SIGTERM)
                        process.wait(timeout=15)
                    except ProcessLookupError:
                        process.wait()
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait()
        report_path = run / 'result.json'
        report = json.loads(report_path.read_text()) if report_path.exists() else {}
        job['result'] = report
        job['status'] = 'interrupted' if interrupted else 'failed'
        if process.returncode == 0 and report.get('status') == 'PASS':
            self.accept_worker_result(job, report)
        self.save()
        return {'status': job['status'], 'result': report,
                'actual_worker_log': (directory / 'worker.log').read_text()[-18000:]}

    def accept_worker_result(self, job, report):
        source = ROOT / (job['config']['module'] + '.lean')
        if digest(source.read_bytes()) != report['source_sha256']:
            raise ValueError('Verified source hash mismatch')
        job['result'] = report
        self.register(job)
        job['status'] = 'verified'

    def recover_interrupted_worker(self, job):
        job['status'] = 'interrupted'
        if not job['runs']:
            return
        report_path = Path(job['runs'][-1]) / 'result.json'
        source = ROOT / (job['config']['module'] + '.lean')
        if report_path.is_file() and source.is_file():
            report = json.loads(report_path.read_text())
            if report.get('status') == 'PASS':
                self.accept_worker_result(job, report)

    def recover_seeds(self, job):
        seeds = {}
        names = [g[0] for g in job['config']['goals']]
        for directory in map(Path, job['runs']):
            accepted = directory / 'accepted_proofs.json'
            if accepted.exists():
                for name, proof in json.loads(accepted.read_text()).items():
                    if name in seeds and seeds[name] != proof:
                        raise ValueError('Accepted proof prefix changed across runs')
                    seeds.setdefault(name, proof)
        # Accepted bodies take priority over all older, previously rejected candidates.
        for directory in map(Path, job['runs']):
            report = directory / 'result.json'
            if not report.exists(): continue
            for record in json.loads(report.read_text()).get('records', []):
                name = record.get('theorem')
                if record.get('exit_code') != 0 or name not in names or name in seeds: continue
                prefix = str(names.index(name)+1) + '-' + str(record['attempt'])
                source, log, response = (directory / (prefix + suffix) for suffix in ['.lean', '.compiler.txt', '.response.json'])
                if not (source.exists() and log.exists() and response.exists()): continue
                if digest(source.read_bytes()) != record['source_sha256'] or not lean_accepted(0, log.read_text()): continue
                body = json.loads(completion_text(json.loads(response.read_text())))['proof']
                seeds[name] = body  # Exact DeepSeek output, recompiled against the unchanged contract.
        return {name: proof for name, proof in seeds.items() if name in names}

    def diagnose(self, job_id):
        job = self.state['jobs'][job_id]; failures = []
        for run in map(Path, job['runs'][-3:]):
            paths = sorted(run.glob('*-*.compiler.txt'), key=lambda p: tuple(map(int, p.name.split('.compiler')[0].split('-'))))
            for path in paths[-6:]:
                source = path.with_name(path.name.replace('.compiler.txt', '.lean'))
                output = path.read_text()
                inferred_code = 1 if re.search(r'\berror(?:\([^)]*\))?:|HARNESS_WALL_TIMEOUT', output) else 0
                info = analyze(output, inferred_code)
                failures.append({'attempt': path.stem, 'kernel_pass_if_recompiled': lean_accepted(inferred_code, output),
                    'analysis': info, 'actual_source_context': source_context(source.read_text(), info) if source.exists() else '',
                    'compiler_output': output[-7000:]})
        result = {'frozen_config_sha256': job['config_sha256'], 'actual_attempts': failures[-8:],
                  'reusable_seed_theorems': list(self.recover_seeds(job)), 'recompilation_required': True,
                  'note': 'Diagnostics and lint are not substitutes for actual fixed-type Lean verification.'}
        job['last_diagnosis'] = result; self.save()
        return result

    def update_context(self, args):
        job = self.state['jobs'][args['job_id']]
        if job['status'] in {'verified', 'published', 'running'}:
            raise ValueError('Update context only for a ready, failed or interrupted fixed job')
        extra = [rooted(NOTES, p) for p in args.get('extra_context', [])]
        library = [rooted(MATHLIB / 'Mathlib', p) for p in args.get('library_reference', [])]
        contexts = list(dict.fromkeys(job['extra_context'] + [str(p) for p in extra]))
        references = list(dict.fromkeys(job['library_reference'] + [str(p) for p in library]))
        if len(contexts)>8 or len(references)>4 or any(Path(p).stat().st_size>300000 for p in contexts+references):
            raise ValueError('Use focused source context within the existing file limits')
        job['extra_context'], job['library_reference'] = contexts, references
        self.save(); return {'context_updated': True, 'unchanged_contract_sha256': job['config_sha256']}

    def review_failure(self, job_id):
        job = self.state['jobs'][job_id]
        diagnostic = self.diagnose(job_id)
        response = api([{'role':'user','content':
            'You are a separate DeepSeek repair critic, not an independent external reviewer. '
            'Use the actual compiler failures and unchanged theorem contract to propose a different repair '
            'strategy. For resource or syntax failures, do not invent a new mathematical obstruction. '
            'Return compact JSON {failure_classification,alternative_strategy,needed_facts,avoid}. '
            'Do not alter any theorem or successful proof.\n'+json.dumps({'config':job['config'], 'diagnosis':diagnostic},ensure_ascii=False)}])
        advice = json.loads(completion_text(response))
        directory = self.run_dir/'jobs'/job_id
        write_json(directory/'repair_critic.response.json',response)
        note = directory/'repair_advice.md'
        note.write_text('DeepSeek repair-critic advice (unverified guidance, not proof):\n'+json.dumps(advice,ensure_ascii=False,indent=2))
        job['harness_context'] = [str(note)]; self.save()
        return {'critic_advice':advice,'passed_to_next_worker':True,'unchanged_contract_sha256':job['config_sha256']}

    def set_plan(self, args):
        nodes = args.get('milestones')
        if not isinstance(nodes,list) or not 1<=len(nodes)<=24: raise ValueError('Use 1..24 focused milestones')
        found = {}
        for node in nodes:
            if (not isinstance(node,dict) or set(node)-{'id','objective','depends_on','modules'}
                    or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*',node.get('id',''))
                    or not isinstance(node.get('objective'),str) or not 1<=len(node['objective'])<=2000
                    or not isinstance(node.get('depends_on',[]),list) or not isinstance(node.get('modules',[]),list)
                    or any(not isinstance(dep,str) for dep in node.get('depends_on',[]))
                    or any(not isinstance(m,str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*',m) for m in node.get('modules',[]))
                    or node['id'] in found): raise ValueError('Invalid milestone schema')
            found[node['id']] = node
        visited, active = set(),set()
        def visit(key):
            if key not in found or key in active: raise ValueError('Missing or cyclic milestone dependency')
            if key in visited:return
            active.add(key)
            for dep in found[key].get('depends_on',[]):visit(dep)
            active.remove(key);visited.add(key)
        for key in found:visit(key)
        self.state['milestones']=nodes;self.save()
        return {'plan_saved':True,'plan':self.plan_snapshot(),'final_targets_unchanged':True}

    def plan_snapshot(self):
        data=json.loads((ROOT/'deepseek_generation_checks.json').read_text())
        verified={m['module'] for m in data.get('modules',[]) if m['status']=='PASS'}
        return [{**node,'module_evidence_present':[m for m in node.get('modules',[]) if m in verified],
                 'semantic_goal_completion':False} for node in self.state.get('milestones',[])]

    def register(self, job):
        config, report = job['config'], job['result']
        name = config['module']
        write_json(ROOT / (name + '.goal_job.json'), config)
        write_json(ROOT / (name + '.goal_check.json'), report)
        path = ROOT / 'deepseek_generation_checks.json'
        data = json.loads(path.read_text())
        data['modules'] = [m for m in data['modules'] if m['module'] != name] + [report]
        data['accepted_theorem_count'] = sum(len(m['theorems']) for m in data['modules'])
        write_json(path, data)
        registry = json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {'modules': []}
        if name not in registry['modules']: registry['modules'].append(name)
        write_json(REGISTRY, registry)

    def publish(self):
        pending = [j for j in self.state['jobs'].values() if j['status'] == 'verified']
        if not pending: return {'published': [], 'message': 'No new verified module'}
        synchronization = self.sync_research()
        env = lean_environment()
        command = ['lake', 'env', 'env', '-u', 'LD_LIBRARY_PATH', sys.executable,
                   str(ROOT / 'check_additional_formalization.py')]
        if self.state.get('run_origin') == 'codespaces':
            for job in pending:
                command.extend(['--recheck', job['config']['module']])
        check = subprocess.run(command,
                               cwd=MATHLIB, env=env, capture_output=True, text=True, timeout=1800)
        if check.returncode:
            raise ValueError('Actual full Lean verification failed:\n' + (check.stdout + check.stderr)[-20000:])
        report = json.loads((ROOT / 'additional_kernel_check.json').read_text())
        checked = {r['source']: r for r in report['records']}
        allowed = {ROOT / 'additional_kernel_check.json', ROOT / 'deepseek_generation_checks.json', REGISTRY, PROGRESS}
        if 'reused_verification' in report:
            allowed.update(ROOT / record['log'] for record in report['records'])
        allowed.update(NOTES/name for name in ['DEEPSEEK_METHOD_RESEARCH.json','DEEPSEEK_METHOD_RESEARCH.md'] if (NOTES/name).is_file())
        for job in pending:
            name = job['config']['module']; record = checked.get(name + '.lean')
            if (not record or record['exit_code'] or record['proof_hole_or_custom_axiom_detected']
                    or record['source_sha256'] != job['result']['source_sha256']):
                raise ValueError('Module is not in the actual verification evidence')
            allowed.update(ROOT / (name + suffix) for suffix in ['.lean', '.additional_check.txt', '.goal_job.json', '.goal_check.json'])
        relative = {str(p.relative_to(REPO)) for p in allowed}
        staged = subprocess.check_output(['git', 'diff', '--cached', '--name-only'], cwd=REPO, text=True).splitlines()
        if set(staged) - relative:
            raise ValueError('Unrelated staged changes exist; refusing to include them')
        subprocess.run(['git', 'add', '--', *sorted(relative)], cwd=REPO, check=True)
        subprocess.run(['git', 'diff', '--cached', '--check'], cwd=REPO, check=True)
        changes = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=REPO).returncode
        if changes:
            subprocess.run(['git', 'commit', '-m', 'DeepSeek goal: verify ' + ', '.join(j['config']['module'] for j in pending)], cwd=REPO, check=True)
        publication = push_verified(REPO, self.goal['branch'], self.publication_origins(),
                                    self.protected_sources(), self.compiler_inputs)
        head = publication['commit']
        for job in pending: job['status'] = 'published'; job['published_commit'] = head
        self.state['publication'] = {'commit': head, 'modules': [j['config']['module'] for j in pending]}
        self.save()
        result = {'published': self.state['publication'], 'kernel_check': 'PASS',
                  'synchronization': synchronization, 'publication_receipt': publication}
        try:
            self.update_pr(head, report)
            result['pr_summary_updated'] = True
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            # The verified git publication is still real if only a summary edit fails.
            result['pr_summary_error'] = str(error)[:1000]
        return result

    def publication_origins(self):
        repository = self.goal['repository']
        return {'https://github.com/' + repository, 'https://github.com/' + repository + '.git',
                'git@github.com:' + repository + '.git'}

    def protected_sources(self):
        paths = [*ROOT.glob('*.lean'), *ROOT.glob('*.goal_job.json'), GOAL]
        return {str(p.relative_to(REPO)):digest(p.read_bytes()) for p in paths if p.is_file()}

    def compiler_inputs(self):
        paths = [*ROOT.glob('*.lean'), *ROOT.glob('*.goal_job.json'), REGISTRY, GOAL,
                 ROOT/'check_additional_formalization.py', ROOT/'deepseek_lean_harness.py',
                 ROOT/'deepseek_harness.json']
        return {str(p.relative_to(REPO)):digest(p.read_bytes()) for p in paths if p.is_file()}

    def sync_research(self):
        return synchronize(REPO, self.goal['branch'], self.publication_origins(), self.protected_sources())

    def github_status(self):
        def read(endpoint):
            result=subprocess.run(['gh','api',endpoint],cwd=REPO,capture_output=True,text=True,timeout=60)
            if result.returncode:raise ValueError('GitHub observation failed: '+(result.stdout+result.stderr)[-4000:])
            return json.loads(result.stdout)
        base='repos/'+self.goal['repository']
        pr=read(base+'/pulls/'+str(self.goal['pr']))
        head=pr['head']['sha'];checks=read(base+'/commits/'+head+'/check-runs')
        return {'repository':self.goal['repository'],'pull_request':self.goal['pr'],
                'url':pr['html_url'],'title':pr['title'],'draft':pr['draft'],
                'research_branch':self.goal['branch'],'observed_head_branch':pr['head']['ref'],'observed_head_commit':head,
                'checks':[{'name':c['name'],'status':c['status'],'conclusion':c.get('conclusion'),'url':c.get('html_url')}
                          for c in checks.get('check_runs',[])[:30]],
                'not_Lean_proof_evidence':True}

    def update_pr(self, head, report):
        endpoint = 'repos/' + self.goal['repository'] + '/pulls/' + str(self.goal['pr'])
        current = json.loads(subprocess.check_output(['gh', 'api', endpoint], cwd=REPO, text=True))
        marker = '<!-- deepseek-autonomous-goal -->'
        body = (current.get('body') or '').split(marker)[0].rstrip()
        generated = json.loads((ROOT / 'deepseek_generation_checks.json').read_text())
        addition = ('\n\n' + marker + '\n\n## DeepSeek自身が進める継続目標\n\n'
                    '- 課題選択・定理設計・証明・修正はDeepSeek max、ホストは実行・実検証・保存を担当。\n'
                    '- 最新のDeepSeek作成証明: ' + str(generated['accepted_theorem_count']) + '定理。'
                    '実Lean検査: ' + str(len(report['records'])) + 'モジュール、PASS。\n'
                    '- 保存コミット: `' + head + '`。補題数だけで最終目標を完了扱いにしない。\n'
                    '- 固定した最終2定理と自動進捗: `.agents/skills/deepseek-goal/goal.json`、'
                    '`docs/research/nested-binomial/DEEPSEEK_GOAL_PROGRESS.md`。\n'
                    '- 実行上限での停止は未完了のチェックポイント。全四変数問題の解決を意味しない。\n')
        payload = self.run_dir / 'pr-update.json'
        write_json(payload, {'body': body + addition})
        subprocess.run(['gh', 'api', '--method', 'PATCH', endpoint, '--input', str(payload), '--silent'],
                       cwd=REPO, check=True)

    def completion(self):
        missing = []
        for target in self.goal['targets']:
            found = [j for j in self.state['jobs'].values()
                     if j['status'] == 'published' and j['config']['module'] == target['module']
                     and not j['config']['definitions'].strip()
                     and j['config']['goals'] == [[target['name'], target['statement']]]]
            if not found or digest((ROOT / (target['module'] + '.lean')).read_bytes()) != found[0]['result']['source_sha256']:
                missing.append(target['name'])
        if missing: return {'complete': False, 'missing_verified_published_targets': missing}
        self.state['status'] = 'complete'; self.save()
        return {'complete': True, 'publication': self.state['publication']}

    def execute(self, action):
        name, args = action.get('action'), action.get('arguments', {})
        if name == 'list_research':
            return {'files': sorted(str(p.relative_to(NOTES)) for p in NOTES.rglob('*') if p.is_file() and (p.suffix in {'.lean', '.md', '.py', '.json', '.txt', '.toml'} or p.name.endswith('.json.gz')))}
        if name in {'read_research', 'read_mathlib'}:
            base = NOTES if name == 'read_research' else MATHLIB / 'Mathlib'
            return {'content': excerpt(rooted(base, args['path'],allow_compressed=name=='read_research'), args.get('start', 1), args.get('count', 160))}
        if name in {'search_research', 'search_mathlib'}:
            return self.search(NOTES if name == 'search_research' else MATHLIB / 'Mathlib', args)
        if name == 'list_mathlib':
            result = subprocess.run(['rg', '--files', '--glob', args.get('glob', '*.lean')],
                                    cwd=MATHLIB / 'Mathlib', capture_output=True, text=True, timeout=15)
            return {'files': result.stdout.splitlines()[:400]}
        if name == 'cache_mathlib':
            path = rooted(MATHLIB / 'Mathlib', args['path'])
            if path.suffix != '.lean': raise ValueError('Cache only Lean library files')
            env = lean_environment()
            cache_command = env.get('DEEPSEEK_CACHE_COMMAND')
            command = [cache_command] if cache_command else ['lake', 'exe', 'cache', 'get']
            result = subprocess.run([*command, str(path.relative_to(MATHLIB))],
                                    cwd=MATHLIB, env=env, capture_output=True, text=True, timeout=600)
            return {'exit_code': result.returncode, 'output': (result.stdout + result.stderr)[-12000:]}
        if name == 'propose_job': return self.propose(args)
        if name == 'inspect_job': return self.state['jobs'][args['job_id']]
        if name == 'diagnose_job': return self.diagnose(args['job_id'])
        if name == 'update_job_context': return self.update_context(args)
        if name == 'review_failure': return self.review_failure(args['job_id'])
        if name == 'set_plan': return self.set_plan(args)
        if name == 'prove_job': return self.worker(args['job_id'], args.get('attempts', 5))
        if name == 'publish': return self.publish()
        if name == 'sync_research': return self.sync_research()
        if name == 'github_status':
            if args:raise ValueError('github_status uses only the authorized repository and PR; no overrides')
            return self.github_status()
        if name == 'inspect_methods': return self.methods.overview()
        if name in {'propose_method','use_method','evaluate_method'}:
            result=getattr(self.methods,{'propose_method':'propose','use_method':'use','evaluate_method':'evaluate'}[name])(args)
            self.save();return result
        if name == 'checkpoint':
            summary = args.get('summary', '')
            if not isinstance(summary, str) or not 1 <= len(summary) <= 2000: raise ValueError('Use a brief progress summary')
            self.state['notes'].append({'summary': summary, 'source': MODEL, 'status': 'model_note_not_verification'})
            self.save(); return {'checkpoint_saved': True, 'goal_complete': False, 'next': 'Continue choosing the next action'}
        if name == 'request_completion': return self.completion()
        raise ValueError('Unknown action; there is no self-reported done action')

    def run(self, max_actions=48, max_hours=6, max_completion_tokens=2000000,
            max_api_calls=None, run_origin=None):
        if max_actions < 1 or max_hours <= 0 or max_completion_tokens < 1024:
            raise ValueError('Execution limits must be positive')
        with (self.run_dir / 'running.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            # Reload under the lock in case another process saved state after we opened it.
            if self.state_path.exists():
                self.load_state()
            if self.state['status'] == 'complete': return self.state
            if run_origin is not None:
                self.state.setdefault('run_origin', run_origin)
            (self.run_dir / 'PAUSE').unlink(missing_ok=True)
            budget_path = self.run_dir / 'budget.json'
            if budget_path.exists():
                epochs = self.state.setdefault('previous_budget_epochs', [])
                epochs.append(json.loads(budget_path.read_text()))
            budget = {'max_completion_tokens': max_completion_tokens, 'used_completion_tokens': 0,
                      'deadline': time.time() + max_hours * 3600, 'api_calls': 0}
            if max_api_calls is not None:
                budget['max_api_calls'] = max_api_calls
            write_json(budget_path, budget)
            previous = os.environ.get('DEEPSEEK_GOAL_BUDGET_FILE')
            os.environ['DEEPSEEK_GOAL_BUDGET_FILE'] = str(budget_path)
            self.state['status'] = 'running'; self.state['pid'] = os.getpid()
            self.state['last_error'] = None
            self.run_lock_fd = lock.fileno()
            try:
                for job in self.state['jobs'].values():
                    if job['status'] == 'running':
                        self.recover_interrupted_worker(job)
                self.save()
                for _ in range(max_actions):
                    if (self.run_dir / 'PAUSE').exists():
                        self.state['status'] = 'paused'; break
                    if self.state['status'] == 'complete': break
                    try:
                        action = self.decision()
                    except ValueError as error:
                        action = {'action': 'invalid', 'arguments': {}, 'reason': str(error)}
                    if (self.run_dir / 'PAUSE').exists():
                        self.state['status'] = 'paused'; break
                    self.state['steps'] += 1
                    print(json.dumps({'step': self.state['steps'], 'model': MODEL, 'action': action.get('action'), 'reason': action.get('reason', '')}, ensure_ascii=False), flush=True)
                    try:
                        observation = self.execute(action)
                    except PublicationBlocked as error:
                        observation = {'tool_error': str(error), 'publication_blocked': True,
                                       'goal_complete': False, 'retry_in_this_round': False}
                        self.state['status'] = 'blocked'; self.state['last_error'] = str(error)
                    except (ValueError, KeyError, TypeError, subprocess.SubprocessError, OSError) as error:
                        observation = {'tool_error': str(error)[-18000:], 'goal_complete': False}
                        if action.get('action') in {'publish', 'sync_research'}:
                            detail = getattr(error, 'stderr', '') or ''
                            if isinstance(detail, bytes): detail = detail.decode(errors='replace')
                            observation.update(publication_blocked=True, retry_in_this_round=False)
                            observation['tool_error'] += '\n' + detail[-12000:]
                            self.state['status'] = 'blocked'
                            self.state['last_error'] = observation['tool_error']
                    write_json(self.run_dir / f"{self.state['steps']:04d}.action.json", {'action': action, 'observation': observation})
                    self.state['last_observation'] = observation
                    self.remember(action, observation)
                    self.history.append({'role': 'user', 'content': 'Actual tool result:\n' + json.dumps(observation, ensure_ascii=False)[:40000] + '\nContinue the goal; choose the next action.'})
                    self.history = self.history[-6:]
                    self.save()
                    if observation.get('publication_blocked'): break
                else:
                    if self.state['status'] != 'complete': self.state['status'] = 'action_limit'
            except GoalBudgetExceeded as error:
                self.state['status'] = 'budget_limit'; self.state['last_error'] = str(error)
            except KeyboardInterrupt:
                self.state['status'] = 'paused'
            except Exception as error:
                self.state['status'] = 'blocked'; self.state['last_error'] = str(error)[:2000]
            finally:
                self.run_lock_fd = None
                if (self.run_dir / 'PAUSE').exists() and self.state['status'] != 'complete':
                    self.state['status'] = 'paused'
                self.save()
                if previous is None: os.environ.pop('DEEPSEEK_GOAL_BUDGET_FILE', None)
                else: os.environ['DEEPSEEK_GOAL_BUDGET_FILE'] = previous
            return self.state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['run', 'status', 'pause'])
    parser.add_argument('--run-dir', type=Path, default=DEFAULT_RUN)
    parser.add_argument('--max-actions', type=int, default=48)
    parser.add_argument('--max-hours', type=float, default=6)
    parser.add_argument('--max-completion-tokens', type=int, default=2000000)
    parser.add_argument('--max-api-calls', type=int)
    parser.add_argument('--run-origin', choices=['codespaces'])
    parser.add_argument('--summary', action='store_true', help='Show a compact status')
    args = parser.parse_args()
    if args.max_api_calls is not None and args.max_api_calls < 1:
        parser.error('--max-api-calls must be positive')
    agent = GoalAgent(args.run_dir)
    if args.command == 'pause':
        (args.run_dir / 'PAUSE').write_text('User requested pause\n')
        print('Pause requested; the goal is not marked complete.')
    elif args.command == 'status':
        snapshot = agent.snapshot()
        if args.summary:
            snapshot = {key: snapshot[key] for key in ('status', 'steps', 'budget', 'jobs',
                                                       'verified_theorem_count')}
            snapshot['last_error'] = agent.state.get('last_error')
            snapshot['publication'] = agent.state['publication']
        print(json.dumps(snapshot, ensure_ascii=False, indent=2))
    else:
        try:
            if args.run_origin == 'codespaces':
                authorize(REPO, agent.goal['branch'], agent.publication_origins())
            state = agent.run(args.max_actions, args.max_hours, args.max_completion_tokens,
                              args.max_api_calls, args.run_origin)
        except PublicationBlocked as error:
            parser.exit(1, str(error) + '\n')
        except BlockingIOError:
            parser.exit(1, 'A research runner or its proof worker is still active.\n')
        print(json.dumps({'status': state['status'], 'steps': state['steps'], 'publication': state['publication']}, ensure_ascii=False))
        return 1 if args.run_origin == 'codespaces' and state['status'] == 'blocked' else 0


if __name__ == '__main__':
    sys.exit(main())
