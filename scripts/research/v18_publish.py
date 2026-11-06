#!/usr/bin/env python3
"""Commit only generated v18 outputs; retry ordinary merge/push on writer races."""
import argparse
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PREFIX = 'docs/research/nested-binomial/'
ALLOWED_BRANCHES = {'research/nested-binomial-2026-11-05', 'research/v18-next-descent'}


def git(*args, check=True):
    return subprocess.run(['git', *args], cwd=ROOT, check=check, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def publish(branch):
    if branch not in ALLOWED_BRANCHES:
        raise ValueError('Publication is restricted to the two authorized research branches')
    git('config','user.name','github-actions[bot]')
    git('config','user.email','41898282+github-actions[bot]@users.noreply.github.com')
    # NUL-separated porcelain handles spaces safely. No proof or workflow files.
    paths = git('ls-files', '--others', '--modified', '--exclude-standard', '-z',
                '--', PREFIX).stdout.split('\0')
    allowed = re.compile(re.escape(PREFIX)+r'(v18_ranks_a\d+\.(md|json)|'
                         r'v18_fixed_J_search\.(md|json)|v18_modular_levels\.json|'
                         r'v18_actions_(latest\.json|lcm\.md)|v18_actions/[^/]+/.+\.json)$')
    selected = sorted({p for p in paths if p and allowed.fullmatch(p)})
    if not selected:
        print('No generated changes to publish')
        return
    if git('diff','--cached','--name-only').stdout.strip():
        raise RuntimeError('Refusing to include pre-existing staged changes')
    git('add','--',*selected)
    if git('diff','--cached','--quiet',check=False).returncode == 0:
        return
    git('commit','-m','research(v18): save GitHub Actions computation certificates [skip ci]')
    for _ in range(3):
        git('fetch','origin',branch)
        merge = git('merge','--no-edit','FETCH_HEAD',check=False)
        if merge.returncode:
            git('merge','--abort',check=False)
            raise RuntimeError('Concurrent edits conflict; certificates remain in Actions artifacts. '+merge.stderr)
        pushed = git('push','origin','HEAD:refs/heads/'+branch,check=False)
        if pushed.returncode == 0:
            print('Saved results to '+branch)
            return
        if not any(t in pushed.stderr for t in ('non-fast-forward','fetch first')):
            raise RuntimeError('GitHub refused result publication: '+pushed.stderr)
    raise RuntimeError('Branch kept advancing; artifacts retain all results after three push attempts')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--branch', required=True)
    publish(parser.parse_args().branch)
