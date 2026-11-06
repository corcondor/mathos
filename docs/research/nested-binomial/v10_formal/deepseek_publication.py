"""Synchronize one authorized research branch without rewriting verified proofs."""
import hashlib
from pathlib import Path
import subprocess


class PublicationBlocked(RuntimeError):
    """A real publication failure; stop the planner instead of spending actions on it."""


def git(repo, arguments, *, check=True, binary=False):
    try:
        result = subprocess.run(['git', *arguments], cwd=repo, capture_output=True,
                                text=not binary, timeout=120)
    except (OSError, subprocess.SubprocessError) as error:
        raise PublicationBlocked('git ' + ' '.join(arguments) + ': ' + str(error)) from None
    if check and result.returncode:
        raise PublicationBlocked('git ' + ' '.join(arguments) + '\n' +
                                 (result.stdout + result.stderr)[-12000:])
    return result


def authorize(repo, branch, origins):
    origin = git(repo, ['remote', 'get-url', 'origin']).stdout.strip()
    if origin not in origins:
        raise PublicationBlocked('Origin does not match the authorized repository')
    git(repo, ['check-ref-format', 'refs/heads/' + branch])


def synchronize(repo, branch, origins, protected):
    """Fetch and merge both histories, refusing any incoming edit to a protected file."""
    authorize(repo, branch, origins)
    git(repo, ['fetch', 'origin', branch])
    remote = git(repo, ['rev-parse', 'FETCH_HEAD']).stdout.strip()
    contained = git(repo, ['merge-base', '--is-ancestor', remote, 'HEAD'], check=False)
    if contained.returncode == 0:
        return {'status': 'already_contains_remote', 'remote_commit': remote}
    if contained.returncode != 1:
        raise PublicationBlocked('Cannot determine remote ancestry: ' + contained.stderr)
    if git(repo, ['diff', '--cached', '--name-only']).stdout.strip():
        raise PublicationBlocked('Unrelated staged changes exist; synchronize requires a clean index')
    base = git(repo, ['merge-base', 'HEAD', remote]).stdout.strip()
    incoming = set(git(repo, ['diff', '--name-only', base, remote]).stdout.splitlines())
    for name in incoming & set(protected):
        blob = git(repo, ['show', remote + ':' + name], check=False, binary=True)
        if blob.returncode or hashlib.sha256(blob.stdout).hexdigest() != protected[name]:
            raise PublicationBlocked('Remote changes a verified source or frozen contract: ' + name +
                                     '. Preserve both versions and resolve explicitly; no proof was overwritten.')
    result = git(repo, ['merge', '--no-edit', remote], check=False)
    if result.returncode:
        conflicts = git(repo, ['diff', '--name-only', '--diff-filter=U']).stdout.splitlines()
        if git(repo, ['rev-parse', '--verify', 'MERGE_HEAD'], check=False).returncode == 0:
            git(repo, ['merge', '--abort'])
        raise PublicationBlocked('Research branch merge blocked; conflicts=' + str(conflicts) + '\n' +
                                 (result.stdout + result.stderr)[-12000:])
    for name, expected in protected.items():
        path = Path(repo) / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise PublicationBlocked('Protected source changed during merge: ' + name)
    return {'status': 'merged', 'remote_commit': remote,
            'local_commit': git(repo, ['rev-parse', 'HEAD']).stdout.strip()}


def push_verified(repo, branch, origins, protected, evidence_snapshot, max_attempts=3):
    """Retry concurrent-writer push races only; preserve the checked source snapshot."""
    authorize(repo, branch, origins)
    evidence = evidence_snapshot()
    for attempt in range(1, max_attempts + 1):
        pushed = git(repo, ['push', 'origin', 'HEAD:' + branch], check=False)
        if pushed.returncode == 0:
            head = git(repo, ['rev-parse', 'HEAD']).stdout.strip()
            remote = git(repo, ['ls-remote', 'origin', 'refs/heads/' + branch]).stdout.split()[0]
            if remote != head:
                # Another writer may already have appended a commit after this successful push.
                git(repo, ['fetch', 'origin', branch])
                observed = git(repo, ['rev-parse', 'FETCH_HEAD']).stdout.strip()
                if git(repo, ['merge-base', '--is-ancestor', head, observed], check=False).returncode:
                    raise PublicationBlocked('Remote no longer contains the published commit')
                remote = observed
            return {'commit': head, 'observed_remote_commit': remote, 'push_attempts': attempt}
        detail = (pushed.stdout + pushed.stderr)[-12000:]
        race = any(marker in detail.lower() for marker in ['fetch first', 'non-fast-forward', 'stale info'])
        if not race or attempt == max_attempts:
            raise PublicationBlocked('git push failed after ' + str(attempt) + ' attempt(s):\n' + detail)
        synchronize(repo, branch, origins, protected)
        if evidence_snapshot() != evidence:
            raise PublicationBlocked('Compiler inputs changed during synchronization; rerun Lean verification before publishing')
    raise PublicationBlocked('Publication retry limit reached')
