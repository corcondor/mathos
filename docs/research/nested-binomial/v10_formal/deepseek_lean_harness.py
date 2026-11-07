"""Lean feedback, bounded resource retries, and durable failed-attempt memory.

This module never writes a mathematical proof or changes a theorem statement.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
DEFAULTS = {'initial_heartbeats': 400000, 'max_heartbeats': 3200000,
            'initial_rec_depth': 1024, 'max_rec_depth': 4096, 'critic_repeat_threshold': 2}


def policy(root):
    path = Path(root) / 'deepseek_harness.json'
    result = dict(DEFAULTS)
    if path.exists():
        supplied = json.loads(path.read_text())
        if set(supplied) - set(result): raise ValueError('Unknown Lean harness policy')
        result.update(supplied)
    for key in result:
        if type(result[key]) is not int or result[key] <= 0: raise ValueError('Invalid Lean harness policy')
    if not 100000 <= result['initial_heartbeats'] <= result['max_heartbeats'] <= 5000000:
        raise ValueError('Use bounded Lean heartbeats between 100000 and 5000000')
    if not 128 <= result['initial_rec_depth'] <= result['max_rec_depth'] <= 8192 or result['critic_repeat_threshold'] > 10:
        raise ValueError('Lean harness policy is out of bounds')
    return result


def analyze(output, exit_code=1):
    categories = []
    patterns = {
        'no_goals': r'No goals to be solved',
        'simp_no_progress': r'`simp` made no progress',
        'heartbeat': r'maximum number of heartbeats|deterministic\) timeout',
        'recursion_depth': r'maximum recursion depth|maximum recursion',
        'library_api': r'Unknown (?:constant|identifier)|Invalid field|Application type mismatch|unknown namespace',
        'syntax': r'unexpected token|unexpected identifier|invalid syntax',
        'missing_cache': r'object file .* does not exist|unknown module prefix',
        'proof_gap': r'unsolved goals|linarith failed|omega could not|tactic .* failed',
        'unused_binding': r'warning: (?:Variable name|unused variable)|not explicitly referenced',
        'wall_timeout': r'HARNESS_WALL_TIMEOUT',
    }
    for name, pattern in patterns.items():
        if re.search(pattern, output, re.I): categories.append(name)
    errors = re.findall(r'(?m)^.*?\berror(?:\([^)]*\))?: (.*)$', output)
    resource_patterns = patterns['heartbeat'] + '|' + patterns['recursion_depth']
    if any(not re.search(resource_patterns, error, re.I) for error in errors) and not (
            set(categories) - {'heartbeat', 'recursion_depth', 'unused_binding'}):
        categories.append('other_error')
    axioms = set()
    for text in re.findall(r'depends on axioms:\s*\[([^\]]*)\]', output):
        axioms.update(re.findall(r'[A-Za-z_][\w.]*', text))
    untrusted = axioms - ALLOWED_AXIOMS
    if exit_code == 0 and ('sorryAx' in output or untrusted): categories.append('trust_failure')
    locations = [{'line': int(m[1]), 'column': int(m[2]), 'kind': m[3], 'message': m[4]}
                 for m in re.findall(r'(?m)^(.+?\.lean):(\d+):(\d+): (error|warning)(?:\([^)]*\))?: (.*)$', output)]
    warnings = [line for line in output.splitlines() if 'warning:' in line]
    error_lines = [line for line in output.splitlines() if re.search(r'error(?:\([^)]*\))?:|warning:', line)]
    normalized = re.sub(r'[^\s]+\.lean:\d+:\d+:', '<source>:', '\n'.join(error_lines))
    fingerprint = hashlib.sha256((str(sorted(categories)) + '\n' + normalized).encode()).hexdigest()
    hints = {
        'no_goals': 'A prior tactic already closed this goal. Inspect the reported source lines; do not redo the mathematics.',
        'simp_no_progress': 'The requested simp rewrite had no effect. Inspect the exact expression and avoid redundant simplification.',
        'heartbeat': 'The executor can retry the unchanged source with a larger bounded heartbeat budget. Do not inject set_option into proofs.',
        'recursion_depth': 'The executor controls a bounded recursion budget; inspect expression size if the ceiling is reached.',
        'library_api': 'Retrieve the real pinned declaration and its argument order; do not guess lemma names.',
        'unused_binding': 'Unused-variable warnings are retained as lint. They do not invalidate a kernel-checked fixed theorem.',
        'wall_timeout': 'Compilation exceeded the wall-clock limit. Use a more focused argument or split genuinely necessary sublemmas.',
    }
    return {'categories': categories, 'fingerprint': fingerprint, 'locations': locations[:10],
            'warnings': warnings[:12], 'untrusted_axioms': sorted(untrusted),
            'resource_only': bool(categories) and set(categories) <= {'heartbeat', 'recursion_depth', 'unused_binding'},
            'hints': [hints[c] for c in categories if c in hints],
            'reported_goal_states': '\n'.join(output.splitlines()[max(0, next((i for i,l in enumerate(output.splitlines()) if '⊢' in l), len(output.splitlines()))-12):])[:8000] if '⊢' in output else ''}


def accepted(exit_code, output):
    info = analyze(output, exit_code)
    return exit_code == 0 and 'sorryAx' not in output and not info['untrusted_axioms']


def source_context(source, info):
    lines = source.splitlines(); parts = []
    for location in info['locations'][:6]:
        index = location['line'] - 1
        parts.append('\n'.join(f'{i+1}: {lines[i]}' for i in range(max(0,index-3), min(len(lines),index+4))))
    return '\n\n'.join(parts)[:10000]


def compile_lean(command, env, timeout, settings):
    env = {key: value for key, value in env.items()
           if key not in {'MISTRAL_API_KEY', 'GITHUB_TOKEN', 'GH_TOKEN', 'GH_ENTERPRISE_TOKEN'}}
    if sysroot := env.get('LEAN_SYSROOT'):
        paths = env.get('LEAN_PATH', '').split(os.pathsep)
        standard_library = str(Path(sysroot) / 'lib' / 'lean')
        if standard_library not in paths:
            env['LEAN_PATH'] = os.pathsep.join(filter(None, [*paths, standard_library]))
    started = time.monotonic(); heartbeats = settings['initial_heartbeats']; retries = []
    depth = settings['initial_rec_depth']
    while True:
        actual = [command[0], f'-DmaxHeartbeats={heartbeats}', f'-DmaxRecDepth={depth}', *command[1:]]
        remaining = max(1, timeout - (time.monotonic()-started))
        try:
            result = subprocess.run(actual, env=env, capture_output=True, text=True, timeout=remaining)
            output, code = result.stdout + result.stderr, result.returncode
        except subprocess.TimeoutExpired as error:
            def text(value): return value.decode(errors='replace') if isinstance(value, bytes) else (value or '')
            output = text(error.stdout) + text(error.stderr) + '\nHARNESS_WALL_TIMEOUT\n'
            code = 124
        info = analyze(output, code)
        retries.append({'heartbeats': heartbeats, 'max_rec_depth': depth, 'exit_code': code, 'categories': info['categories'],
                        'elapsed_seconds': round(time.monotonic()-started, 3)})
        more_heartbeats = 'heartbeat' in info['categories'] and heartbeats < settings['max_heartbeats']
        more_depth = 'recursion_depth' in info['categories'] and depth < settings['max_rec_depth']
        if (code != 0 and info['resource_only'] and (more_heartbeats or more_depth)
                and time.monotonic()-started < timeout-1):
            if more_heartbeats: heartbeats = min(settings['max_heartbeats'], heartbeats*2)
            if more_depth: depth = min(settings['max_rec_depth'], depth*2)
            continue
        return {'exit_code': code, 'output': output, 'analysis': info, 'resource_attempts': retries,
                'command': actual, 'elapsed_seconds': round(time.monotonic()-started, 3)}


class FailureMemory:
    def __init__(self, path):
        self.path = Path(path)
        self.data = json.loads(self.path.read_text()) if self.path.exists() else {'goals': {}}

    def record(self, name, candidate_hash, info, was_accepted, resources):
        entries = self.data['goals'].setdefault(name, [])
        entries.append({'source_sha256': candidate_hash, 'accepted': was_accepted,
                        'categories': info['categories'], 'fingerprint': info['fingerprint'],
                        'warnings': info['warnings'], 'resource_attempts': resources})
        self.data['goals'][name] = entries[-30:]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix('.tmp')
        temporary.write_text(json.dumps(self.data, ensure_ascii=False, indent=2)+'\n')
        temporary.chmod(0o600); temporary.replace(self.path)

    def summary(self, name):
        entries = self.data['goals'].get(name, [])
        failed = [e for e in entries if not e['accepted']]
        streak = 0
        if failed:
            for item in reversed(entries):
                if item['accepted'] or item['fingerprint'] != failed[-1]['fingerprint']: break
                streak += 1
        return {'previous_attempts': len(entries), 'failures': failed[-5:], 'same_failure_streak': streak}

    def repeated_nonresource_candidate(self, name, candidate_hash):
        for entry in self.data['goals'].get(name, []):
            if (entry['source_sha256'] == candidate_hash and not entry['accepted']
                    and not set(entry['categories']) <= {'heartbeat', 'recursion_depth', 'wall_timeout'}):
                return True
        return False
