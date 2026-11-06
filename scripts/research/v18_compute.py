#!/usr/bin/env python3
"""Checkpointed v18 GitHub Actions computations. No API keys or Lean edits."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from math import comb, gcd, isqrt
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

from v18_arithmetic import (pairs, residual_points, forced_r_divisor, spf_sieve,
                           modular_witness, n_height_exclusive)

ROOT = Path(__file__).resolve().parents[2]
NOTES = ROOT/'docs/research/nested-binomial'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    os.replace(tmp, path)


def provenance():
    sources = [*Path(__file__).parent.glob('v18_*.py'),
               NOTES/'v17_square_root_gap.md', NOTES/'v18_neighbor_cofactor_height.md',
               NOTES/'v18_residual_gap.md',
               NOTES/'v18_short_lcm.md', NOTES/'v18_defect_resultants.md']
    return {"utc": datetime.now(timezone.utc).isoformat(),
            "source_commit": os.environ.get('GITHUB_SHA', 'local-unpublished'),
            "run_id": os.environ.get('GITHUB_RUN_ID'),
            "run_attempt": os.environ.get('GITHUB_RUN_ATTEMPT'),
            "sources_sha256": {str(p.relative_to(ROOT)): sha(p) for p in sources},
            "new_lean_verification": False}


def ranks(args):
    all_pairs = pairs(args.a_max)
    selected = [ab for i, ab in enumerate(all_pairs) if i % args.shards == args.shard]
    out = args.out
    report = {"provenance": provenance(), "a_max": args.a_max,
              "shard": args.shard, "shards": args.shards,
              "expected_pairs": [list(x) for x in selected], "curves": [],
              "status": "running"}
    started = time.monotonic()
    target = out/f'ranks-{args.shard}.json'
    write(target, report)
    for a, b in selected:
        if time.monotonic()-started > args.seconds:
            break
        # Save the COMPLETE finite strip before any expensive CAS stage.
        record = {"a": a, "b": b, "residual": residual_points(a, b),
                  "sage": {"status": "not_started"}}
        report['curves'].append(record)
        write(target, report)
        if 3*a == b:
            record['sage'] = {"status": "singular", "reason": "discriminant zero; not an elliptic curve"}
            write(target, report)
            continue
        checkpoint = out/f'curves/a{a}-b{b}.json'
        checkpoint.parent.mkdir(parents=True, exist_ok=True)
        command = [sys.executable, str(Path(__file__).with_name('v18_sage_curve.py')),
                   '--a', str(a), '--b', str(b), '--output', str(checkpoint),
                   '--stage-seconds', str(max(1, (args.curve_seconds-10)//3))]
        hard_timeout = False
        with checkpoint.with_suffix('.log').open('w') as log:
            proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                    start_new_session=True)
            try:
                proc.wait(timeout=args.curve_seconds)
            except subprocess.TimeoutExpired:
                hard_timeout = True
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()
        if checkpoint.exists():
            record['sage'] = json.loads(checkpoint.read_text())
        record['sage']['exit_code'] = proc.returncode
        record['sage']['hard_timeout'] = hard_timeout
        if proc.returncode:
            record['sage']['status'] = 'partial' if checkpoint.exists() else 'error'
        write(target, report)
        print(f'a={a} b={b}: {record["sage"]["status"]}', flush=True)
    report['status'] = 'enumerated' if len(report['curves']) == len(selected) else 'partial'
    write(target, report)


def conditional_height_checks(n, delta, epsilon, spf):
    """Only apply delta^4 when the published repeated-prime hypothesis holds."""
    checks = []
    neighbors = [(c, n*n-c) for c in (2,3,5,6,7,8,10,11,12,13,14,15)
                 if ((c+2)*n-3*c) % 6 == 0]
    if n % 6 == 3:
        neighbors.append((-2, n*n+2))
    for c, number in neighbors:
        for p in range(2, isqrt(number)+1):
            if spf[p] != p or p*p <= 6*n-9 or number % (p*p):
                continue
            if c > 0:
                bound = (1 << (18 if c == 10 else 38))*delta**4
                branch_ok = epsilon == 1
            else:
                bound = (1 << (24 if epsilon == 0 else 42))*delta**4
                branch_ok = True
            checks.append({"c": c, "p": p, "n_upper_exclusive": bound,
                           "height_pass": n < bound, "branch_pass": branch_ok})
    return checks


def fixed_j(args):
    if not 104 <= args.n_max <= 10_000_000:
        raise ValueError('n-max must be in [104,10000000] (explicit memory/runtime limit)')
    report = {"provenance": provenance(), "requested_n_max": args.n_max,
              "j_max": {"small": args.j_small_max, "complement": args.j_complement_max},
              "n_scanned_through": 103, "status": "running", "counts": {},
              "candidates": [], "survivors": [],
              "meaning": "necessary-condition search; modular survivors are not solutions"}
    target = args.out/'fixed-j.json'
    write(target, report)
    start = time.monotonic()
    spf = spf_sieve(max(args.n_max+1, 6))
    counts = Counter()
    for n in range(104, args.n_max+1):
        if n % 1000 == 0:
            report['counts'] = dict(counts)
            write(target, report)
            if time.monotonic()-start > args.seconds:
                break
        f = forced_r_divisor(n, spf)
        # Exactly the multiples of F in 3n<r<10n/3, t>=4, 3t<n.
        lower, upper = 3*n+4, (10*n-1)//3
        for r in range(((lower+f-1)//f)*f, upper+1, f):
            counts['Q_divides_r_cubed'] += 1
            t = r-3*n
            if t*t < 9*n or (96*(t+3))**11 <= n**7:
                continue
            m = gcd(n, 3)*gcd(n-1, 6)
            q = n*(n-1)//m
            delta = q//gcd(q, r*r)
            for epsilon, name, limit in [(0,'small',args.j_small_max),
                                         (1,'complement',args.j_complement_max)]:
                numer = (r-epsilon)**2-6*n+8-9*(n*n+2)
                common = gcd(n*n+2, numer)
                j = numer//common
                if not 1 <= j <= limit or n >= n_height_exclusive(j, epsilon):
                    continue
                w = (n*n+2)//common
                counts['within_requested_J_and_height'] += 1
                item = {"n": n, "r": r, "branch": name, "J": j, "w": w,
                        "delta": delta}
                assert gcd(w, j) == 1
                divisor = 72 if epsilon else 25
                if delta < 13 or divisor % gcd(delta, j):
                    item['rejection'] = 'delta>=13 or gcd(delta,J) constraint'
                else:
                    conditions = conditional_height_checks(n, delta, epsilon, spf)
                    item['conditional_delta4'] = conditions
                    if any(not x['height_pass'] or not x['branch_pass'] for x in conditions):
                        item['rejection'] = 'conditional repeated-prime height/branch'
                    else:
                        item['modular_witness'] = modular_witness(n, r, epsilon)
                        if item['modular_witness'] is None:
                            report['survivors'].append(item.copy())
                report['candidates'].append(item)
        report['n_scanned_through'] = n
    report['counts'] = dict(counts)
    report['status'] = 'bounded_scan_complete' if report['n_scanned_through'] == args.n_max else 'partial'
    report['coverage'] = {}
    for epsilon, name, limit in [(0,'small',args.j_small_max), (1,'complement',args.j_complement_max)]:
        report['coverage'][name] = [
            {"J": j, "n_upper_exclusive": n_height_exclusive(j, epsilon),
             "height_fully_covered": report['n_scanned_through'] >= n_height_exclusive(j, epsilon)-1}
            for j in range(1, limit+1)]
    write(target, report)
    print(json.dumps({k: report[k] for k in ['status','n_scanned_through','counts']}), flush=True)


def lcm(args):
    args.out.mkdir(parents=True, exist_ok=True)
    auditor = NOTES/'v18_short_lcm_independent_audit.py'
    audit_path = args.out/'lcm-audit.json'
    subprocess.run([sys.executable, str(auditor), '--output', str(audit_path)], check=True)
    # Store independently reconstructed records, not just a PASS string.
    primes = [p for p in range(11, 75) if all(p % d for d in range(2, isqrt(p)+1))]
    cs = [c for c in range(2,16) if isqrt(c)**2 != c]
    records = []
    for c in cs:
        for p in primes:
            for w in range(1, 9):
                if 9*w < p:
                    number = p**3*w+c
                    records.append([p,w,c,number,isqrt(number)])
    for p,c in [(11,12),(13,14)]:
        number = p**7+c
        records.append([p,1,c,number,isqrt(number)])
    assert len(records) == 830
    stored = json.loads((NOTES/'v18_short_lcm_checks.json').read_text())['complete_exception_domain']
    assert sorted(records) == sorted(stored['cubic_square_records']+stored['seventh_square_records'])
    write(args.out/'lcm-certificate.json', {"provenance": provenance(),
          "status": "PASS", "records": records,
          "auditor_sha256": sha(auditor), "audit_sha256": sha(audit_path),
          "producer_report_sha256": sha(NOTES/'v18_short_lcm_checks.json')})


def auxiliary(args):
    data = {"provenance": provenance(), "delta_min": 13, "delta_max": args.delta_max,
            "status": "finite necessary gcd constraint only; not realizability"}
    for name, limit, constant in [('small',args.j_small_max,25),
                                  ('complement',args.j_complement_max,72)]:
        data[name] = [[d,j] for d in range(13,args.delta_max+1)
                      for j in range(1,limit+1) if constant % gcd(d,j) == 0]
    write(args.out/'delta-j.json', data)


def positive(value):
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError('must be positive')
    return n


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='task', required=True)
    for task in ['ranks', 'fixed-j', 'lcm', 'auxiliary']:
        p = commands.add_parser(task)
        p.add_argument('--out', type=Path, required=True)
        p.add_argument('--seconds', type=positive, default=900)
        if task == 'ranks':
            p.add_argument('--a-max', type=positive, default=20)
            p.add_argument('--shard', type=int, default=0)
            p.add_argument('--shards', type=positive, default=1)
            p.add_argument('--curve-seconds', type=positive, default=120)
        if task in ('fixed-j', 'auxiliary'):
            p.add_argument('--j-small-max', type=positive, default=100)
            p.add_argument('--j-complement-max', type=positive, default=30)
        if task == 'fixed-j':
            p.add_argument('--n-max', type=positive, default=1_000_000)
        if task == 'auxiliary':
            p.add_argument('--delta-max', type=positive, default=200)
    args = parser.parse_args()
    if args.task in ('fixed-j', 'auxiliary') and max(args.j_small_max, args.j_complement_max) > 1000:
        parser.error('J limits must be <=1000 for this runner configuration')
    if args.task == 'ranks' and not 10 <= args.curve_seconds <= 300:
        parser.error('curve-seconds must be in [10,300] so artifact upload has reserved time')
    args.out.mkdir(parents=True, exist_ok=True)
    if args.task == 'ranks' and not 0 <= args.shard < args.shards:
        parser.error('shard must be in [0, shards)')
    {'ranks': ranks, 'fixed-j': fixed_j, 'lcm': lcm, 'auxiliary': auxiliary}[args.task](args)


if __name__ == '__main__':
    main()
