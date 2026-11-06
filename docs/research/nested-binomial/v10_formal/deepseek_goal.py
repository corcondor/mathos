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

from deepseek_goal_budget import GoalBudgetExceeded
from deepseek_proof_loop import ROOT, MODEL, api, completion_text, digest, load_api_settings

REPO = ROOT.parents[3]
NOTES = ROOT.parent
MATHLIB = Path('/workspace/.cloud-setup/lean/mathlib')
SKILL = REPO / '.agents/skills/deepseek-goal/SKILL.md'
GOAL = SKILL.with_name('goal.json')
DEFAULT_RUN = Path('/workspace/.cloud-setup/deepseek-goal/nested-binomial-cf')
PROGRESS = NOTES / 'DEEPSEEK_GOAL_PROGRESS.md'
REGISTRY = ROOT / 'goal_verified_modules.json'
FORBIDDEN = (r'\b(sorry|admit|axiom|native_decide|unsafe|initialize|run_cmd|run_tac|run_elab|'
             r'run_io|liftIO|elab|macro|macro_rules|syntax|notation|attribute|set_option)\b|#|\b(IO|Lean|System)\.')


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(path)


def rooted(base, name):
    if not isinstance(name, str) or Path(name).is_absolute():
        raise ValueError('Expected a relative research/library path')
    path = (base / name).resolve()
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError('File is outside the allowed research/library root or missing')
    if path.suffix not in {'.lean', '.md', '.py', '.json', '.txt', '.toml'}:
        raise ValueError('Unsupported research/library file type')
    return path


def excerpt(path, start=1, count=160):
    if type(start) is not int or type(count) is not int or start < 1 or not 1 <= count <= 250:
        raise ValueError('Use a positive start and 1..250 lines')
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
search_research: {query,glob?}; literal search of research only.
read_mathlib: {path,start?,count?}; paths relative to pinned mathlib/Mathlib.
search_mathlib: {query,glob?}; literal search of actual pinned Mathlib declarations.
cache_mathlib: {path}; fetch the compiled cache for one actual Mathlib/*.lean file.
propose_job: {config:{module,imports,definitions,goals:[[name,theorem]],local_dependencies?},
              why_needed,extra_context:[research_paths],library_reference:[Mathlib_relative_paths]}.
  You author the job. Executor validates syntax/boundaries, asks a separate DeepSeek scope review,
  freezes the types, and returns job_id. No proof bodies here. Never weaken the final target.
inspect_job: {job_id}; see the frozen config and actual last result.
prove_job: {job_id,attempts?}; choose 1..20 proof attempts (default 5), then reconsider using real feedback.
publish: {}; verify all accepted modules and commit/push ONLY their artifacts to authorized PR branch.
checkpoint: {summary}; retain a brief research note, then CONTINUE; it does not end the goal.
request_completion: {}; succeeds ONLY when both exact final targets are Lean-verified and published.
There is no done action, arbitrary shell, arbitrary file write, or permission to edit existing proofs.
Read/search tools give you source. You choose every mathematical task. Never ask Codex to choose it.
Return compact actionable JSON, not a long essay. A result on one lemma is progress, not completion.
'''


class GoalAgent:
    def __init__(self, run_dir=DEFAULT_RUN, goal_path=GOAL):
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.run_dir.chmod(0o700)
        self.goal = json.loads(Path(goal_path).read_text())
        self.goal_hash = digest(json.dumps(self.goal, sort_keys=True))
        self.state_path = self.run_dir / 'state.json'
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text())
            if self.state['goal_hash'] != self.goal_hash:
                raise ValueError('Goal changed: start a separate goal; do not weaken an active contract')
        else:
            self.state = {'goal_hash': self.goal_hash, 'status': 'not_started', 'steps': 0,
                          'jobs': {}, 'notes': [], 'last_observation': None, 'publication': None}
        self.history = []

    def save(self):
        self.state['updated_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        write_json(self.state_path, self.state)
        rows = ['# DeepSeek goal progress', '', self.goal['objective'], '',
                '- Decision maker: ' + MODEL, '- Status: ' + self.state['status'],
                '- Actions: ' + str(self.state['steps']),
                '- Final success requires both frozen targets and verified GitHub publication.', '',
                '| Module | Actual status |', '| --- | --- |']
        rows += [f"| {j['config']['module']} | {j['status']} |" for j in self.state['jobs'].values()]
        PROGRESS.write_text('\n'.join(rows) + '\n')

    def snapshot(self):
        budget = self.run_dir / 'budget.json'
        generated = ROOT / 'deepseek_generation_checks.json'
        verified = json.loads(generated.read_text())
        return {'goal': self.goal, 'status': self.state['status'], 'steps': self.state['steps'],
                'jobs': {key: {'module': j['config']['module'], 'status': j['status'],
                              'goals': [g[0] for g in j['config']['goals']], 'why_needed': j['why_needed']}
                         for key, j in self.state['jobs'].items()},
                'notes': self.state['notes'][-8:], 'last_observation': self.state['last_observation'],
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
        history = self.history or [{'role': 'user', 'content': 'Start the persistent goal. You choose the next research action.'}]
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
                                 '--', query, str(base)], capture_output=True, text=True, timeout=15)
        return {'exit_code': result.returncode, 'output': (result.stdout + result.stderr)[:24000]}

    def propose(self, args):
        if any(j['status'] == 'verified' for j in self.state['jobs'].values()):
            raise ValueError('Publish verified progress before proposing another module')
        config = validate_job(args.get('config'), self.goal['targets'])
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
        run = directory / ('run-' + str(len(job['runs']) + 1))
        command = ['lake', 'env', sys.executable, str(ROOT / 'deepseek_goal_worker.py'), job_id,
                   '--job-config', str(config_path), '--run-dir', str(run), '--attempts', str(attempts)]
        if job['runs']:
            seed = Path(job['runs'][-1]) / 'accepted_proofs.json'
            if seed.exists(): command += ['--seed-proofs', str(seed)]
        for path in job['extra_context']: command += ['--extra-context', path]
        for path in job['library_reference']: command += ['--library-reference', path]
        job['runs'].append(str(run)); job['status'] = 'running'; self.save()
        env = os.environ.copy()
        env['ELAN_HOME'] = '/workspace/.cloud-setup/lean/elan'
        env['PATH'] = env['ELAN_HOME'] + '/bin:' + env['PATH']
        with (directory / 'worker.log').open('a') as log:
            process = subprocess.Popen(command, cwd=MATHLIB, env=env, stdout=log,
                                       stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, start_new_session=True)
            while process.poll() is None:
                budget = json.loads((self.run_dir / 'budget.json').read_text())
                if (self.run_dir / 'PAUSE').exists() or time.time() >= budget['deadline']:
                    os.killpg(process.pid, signal.SIGTERM); process.wait(timeout=15)
                    break
                time.sleep(.5)
        report_path = run / 'result.json'
        report = json.loads(report_path.read_text()) if report_path.exists() else {}
        job['result'] = report
        job['status'] = 'failed'
        if process.returncode == 0 and report.get('status') == 'PASS':
            source = ROOT / (frozen['module'] + '.lean')
            if digest(source.read_bytes()) != report['source_sha256']:
                raise ValueError('Verified source hash mismatch')
            job['status'] = 'verified'
            self.register(job)
        self.save()
        return {'status': job['status'], 'result': report,
                'actual_worker_log': (directory / 'worker.log').read_text()[-18000:]}

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
        origin = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], cwd=REPO, text=True).strip()
        if origin not in {'https://github.com/' + self.goal['repository'] + '.git',
                          'git@github.com:' + self.goal['repository'] + '.git'}:
            raise ValueError('Origin does not match the authorized repository')
        env = os.environ.copy(); env['ELAN_HOME'] = '/workspace/.cloud-setup/lean/elan'
        env['PATH'] = env['ELAN_HOME'] + '/bin:' + env['PATH']
        check = subprocess.run(['lake', 'env', sys.executable, str(ROOT / 'check_additional_formalization.py')],
                               cwd=MATHLIB, env=env, capture_output=True, text=True, timeout=1800)
        if check.returncode:
            raise ValueError('Actual full Lean verification failed:\n' + (check.stdout + check.stderr)[-20000:])
        report = json.loads((ROOT / 'additional_kernel_check.json').read_text())
        checked = {r['source']: r for r in report['records']}
        allowed = {ROOT / 'additional_kernel_check.json', ROOT / 'deepseek_generation_checks.json', REGISTRY, PROGRESS}
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
        subprocess.run(['git', 'push', 'origin', 'HEAD:' + self.goal['branch']], cwd=REPO, check=True)
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
        remote = subprocess.check_output(['git', 'ls-remote', 'origin', 'refs/heads/' + self.goal['branch']], cwd=REPO, text=True).split()[0]
        if remote != head: raise ValueError('Remote head does not match published commit')
        for job in pending: job['status'] = 'published'; job['published_commit'] = head
        self.state['publication'] = {'commit': head, 'modules': [j['config']['module'] for j in pending]}
        self.save()
        result = {'published': self.state['publication'], 'kernel_check': 'PASS'}
        try:
            self.update_pr(head, report)
            result['pr_summary_updated'] = True
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            # The verified git publication is still real if only a summary edit fails.
            result['pr_summary_error'] = str(error)[:1000]
        return result

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
            return {'files': sorted(str(p.relative_to(NOTES)) for p in NOTES.rglob('*') if p.is_file() and p.suffix in {'.lean', '.md', '.py', '.json', '.txt', '.toml'})}
        if name in {'read_research', 'read_mathlib'}:
            base = NOTES if name == 'read_research' else MATHLIB / 'Mathlib'
            return {'content': excerpt(rooted(base, args['path']), args.get('start', 1), args.get('count', 160))}
        if name in {'search_research', 'search_mathlib'}:
            return self.search(NOTES if name == 'search_research' else MATHLIB / 'Mathlib', args)
        if name == 'cache_mathlib':
            path = rooted(MATHLIB / 'Mathlib', args['path'])
            if path.suffix != '.lean': raise ValueError('Cache only Lean library files')
            env = os.environ.copy(); env['ELAN_HOME'] = '/workspace/.cloud-setup/lean/elan'; env['PATH'] = env['ELAN_HOME'] + '/bin:' + env['PATH']
            result = subprocess.run(['lake', 'exe', 'cache', 'get', str(path.relative_to(MATHLIB))],
                                    cwd=MATHLIB, env=env, capture_output=True, text=True, timeout=600)
            return {'exit_code': result.returncode, 'output': (result.stdout + result.stderr)[-12000:]}
        if name == 'propose_job': return self.propose(args)
        if name == 'inspect_job': return self.state['jobs'][args['job_id']]
        if name == 'prove_job': return self.worker(args['job_id'], args.get('attempts', 5))
        if name == 'publish': return self.publish()
        if name == 'checkpoint':
            summary = args.get('summary', '')
            if not isinstance(summary, str) or not 1 <= len(summary) <= 2000: raise ValueError('Use a brief progress summary')
            self.state['notes'].append({'summary': summary, 'source': MODEL, 'status': 'model_note_not_verification'})
            self.save(); return {'checkpoint_saved': True, 'goal_complete': False, 'next': 'Continue choosing the next action'}
        if name == 'request_completion': return self.completion()
        raise ValueError('Unknown action; there is no self-reported done action')

    def run(self, max_actions=48, max_hours=6, max_completion_tokens=2000000):
        if max_actions < 1 or max_hours <= 0 or max_completion_tokens < 1024:
            raise ValueError('Execution limits must be positive')
        with (self.run_dir / 'running.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            if self.state['status'] == 'complete': return self.state
            for job in self.state['jobs'].values():
                if job['status'] == 'running': job['status'] = 'interrupted'
            (self.run_dir / 'PAUSE').unlink(missing_ok=True)
            budget_path = self.run_dir / 'budget.json'
            write_json(budget_path, {'max_completion_tokens': max_completion_tokens, 'used_completion_tokens': 0,
                                     'deadline': time.time() + max_hours * 3600, 'api_calls': 0})
            previous = os.environ.get('DEEPSEEK_GOAL_BUDGET_FILE')
            os.environ['DEEPSEEK_GOAL_BUDGET_FILE'] = str(budget_path)
            self.state['status'] = 'running'; self.state['pid'] = os.getpid(); self.save()
            try:
                for _ in range(max_actions):
                    if (self.run_dir / 'PAUSE').exists():
                        self.state['status'] = 'paused'; break
                    if self.state['status'] == 'complete': break
                    try:
                        action = self.decision()
                    except ValueError as error:
                        action = {'action': 'invalid', 'arguments': {}, 'reason': str(error)}
                    self.state['steps'] += 1
                    print(json.dumps({'step': self.state['steps'], 'model': MODEL, 'action': action.get('action'), 'reason': action.get('reason', '')}, ensure_ascii=False), flush=True)
                    try:
                        observation = self.execute(action)
                    except (ValueError, KeyError, TypeError, subprocess.SubprocessError, OSError) as error:
                        observation = {'tool_error': str(error)[-18000:], 'goal_complete': False}
                    write_json(self.run_dir / f"{self.state['steps']:04d}.action.json", {'action': action, 'observation': observation})
                    self.state['last_observation'] = observation
                    self.history.append({'role': 'user', 'content': 'Actual tool result:\n' + json.dumps(observation, ensure_ascii=False)[:40000] + '\nContinue the goal; choose the next action.'})
                    self.history = self.history[-4:]
                    self.save()
                else:
                    if self.state['status'] != 'complete': self.state['status'] = 'action_limit'
            except GoalBudgetExceeded as error:
                self.state['status'] = 'budget_limit'; self.state['last_error'] = str(error)
            except Exception as error:
                self.state['status'] = 'blocked'; self.state['last_error'] = str(error)[:2000]
            finally:
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
    args = parser.parse_args()
    agent = GoalAgent(args.run_dir)
    if args.command == 'pause':
        (args.run_dir / 'PAUSE').write_text('User requested pause\n')
        print('Pause requested; the goal is not marked complete.')
    elif args.command == 'status': print(json.dumps(agent.snapshot(), ensure_ascii=False, indent=2))
    else:
        state = agent.run(args.max_actions, args.max_hours, args.max_completion_tokens)
        print(json.dumps({'status': state['status'], 'steps': state['steps'], 'publication': state['publication']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
