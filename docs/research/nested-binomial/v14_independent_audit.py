#!/usr/bin/env python3
"""Audit the v14 finite reduction with exact arithmetic only.

Input completeness still depends on PARI/GP's complete Thue solver. This
program audits coefficient coverage, raw gap-2 output, substitutions, the
pair-to-index reduction, and each divisibility/interval contradiction. It
does not run Lean, evaluate the original giant binomial, or search over H.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
from fractions import Fraction
from math import gcd, prod
from pathlib import Path


def require(test, message):
    if not test:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factor(m):
    original = m
    out = []
    p = 2
    while p*p <= m:
        power = 0
        while m % p == 0:
            m //= p
            power += 1
        if power:
            out.append((p, power))
        p = 3 if p == 2 else p+2
    if m > 1:
        out.append((m, 1))
    require(prod(p**e for p, e in out) == original, "factorization product")
    return out


def audit_thue(path, primes, rhs, odd_only):
    data = json.loads(path.read_text())
    require(data['status'] == 'PASS', 'input status')
    require(data['support_primes'] == primes, 'support primes')
    require(data['thueinit_flag'] == 1, 'unconditional thueinit flag')
    cores = [prod(p**e for p, e in zip(primes, powers))
             for powers in itertools.product(range(3), repeat=len(primes))]
    expected = {(a, b) for a in cores for b in cores if gcd(a, b) == 1}
    rows = data['records']
    observed = [(row['A'], row['B']) for row in rows]
    require(len(rows) == len(expected) == 5**len(primes), 'pair count')
    require(set(observed) == expected, 'coefficient coverage')
    ns = set()
    signed_count = 0
    for row in rows:
        a, b = row['A'], row['B']
        direct = sorted(tuple(point) for point in row['all_integer_solutions'])
        require(len(direct) == len(set(direct)), 'duplicate direct point')
        require(all(type(x) is int and type(y) is int and a*x**3-b*y**3 == rhs
                    for x, y in direct), 'direct substitution')
        key = ('monic_all_integer_solutions' if rhs == 2
               else 'transformed_all_integer_solutions')
        transformed = sorted(tuple(point) for point in row[key])
        require(all(u**3-a*a*b*y**3 == rhs*a*a for u, y in transformed),
                'transformed substitution')
        require(direct == sorted((u//a, y) for u, y in transformed if u % a == 0),
                'encoding agreement')
        ns.update(a*x**3 for x, y in direct
                  if x > 0 and y > 0 and (not odd_only or (x % 2 and y % 2)))
        signed_count += len(direct)
    require(sorted(ns) == data['selected_n' if rhs == 2 else 'positive_n'],
            'positive index aggregate')
    if rhs == 2:
        require(data['rhs'] == 2 and data['odd_bases_required'], 'gap-2 parameters')
        require(data['process_exit_code'] == 0, 'PARI exit code')
        for suffix, key in [('.gp', 'gp_input_sha256'),
                            ('.stdout', 'gp_stdout_sha256'),
                            ('.stderr', 'gp_stderr_sha256')]:
            require(digest(path.with_suffix(suffix)) == data[key], 'raw file hash')
        require(not path.with_suffix('.stderr').read_text().strip(), 'PARI stderr')
        program = ['print(version());']
        for a, b in sorted(expected):
            program.append(f'print([{a},{b},thue(thueinit({a}*x^3-{b},1),{rhs}),'
                           f'thue(thueinit(x^3-{a*a*b},1),{rhs*a*a})]);')
        program.append('quit;')
        require(path.with_suffix('.gp').read_text() == '\n'.join(program)+'\n',
                'all 250 actual calls have flag 1 and correct parameters')
        raw = [ast.literal_eval(line) for line in path.with_suffix('.stdout').read_text().splitlines()]
        require(len(raw) == len(rows)+1 and raw[0] == data['pari_version'],
                'raw stdout record count and version')
        expected_raw = [[row['A'], row['B'], row['all_integer_solutions'],
                         row['monic_all_integer_solutions']] for row in rows]
        require(raw[1:] == expected_raw, 'JSON faithfully records raw stdout')
    return ns, {'file': path.name, 'sha256': digest(path),
                'coefficient_pairs': len(expected), 'signed_solution_count': signed_count,
                'positive_indices': sorted(ns), 'flag': 1}


def interval_check(n):
    a = n*(n-1)*(n-2)//6
    d = a//gcd(a, n-2)
    fs = factor(d)
    f = prod(p**((exponent+2)//3) for p, exponent in fs)
    first = f*(3*n//f+1)
    require(first > 3*n and first-f <= 3*n, 'least strict multiple')
    upper = Fraction(10*n, 3)
    log_lower = None
    if n >= 1024:
        ell = 0
        while 3**(ell+1) < n:
            ell += 1
        require(ell > 0 and 3**ell < n <= 3**(ell+1), 'exact log bound')
        log_upper = Fraction(3*n)+Fraction(3*n, 4*ell)
        if log_upper < upper:
            upper = log_upper
            log_lower = ell
    rejected = first*upper.denominator >= upper.numerator
    return {'n': n, 'A': a, 'D': d, 'D_factorization': fs, 'F': f,
            'first_F_multiple_strictly_above_3n': first,
            'strict_upper_bound': [upper.numerator, upper.denominator],
            'log_n_strict_lower_bound_from_e_lt_3': log_lower,
            'exact_nonnegative_margin': first*upper.denominator-upper.numerator,
            'excluded': rejected}


def run(gap1, gap2, destination):
    adjacent, first_audit = audit_thue(gap1, [2, 3, 5, 7], 1, False)
    odd_ends, second_audit = audit_thue(gap2, [3, 5, 7], 2, True)
    candidates = adjacent | {n+1 for n in adjacent} | {2*n for n in adjacent} | odd_ends
    valid = sorted(n for n in candidates if n >= 3)
    remaining = sorted(n for n in valid if n >= 104)
    rows = [interval_check(n) for n in remaining]
    report = {
        'status': 'PASS' if all(row['excluded'] for row in rows) else 'SURVIVORS',
        'scope': 'ell=1, j=i-3; prior n>=104, H|n-2, 3n<r<10n/3 and logarithmic upper bound',
        'complete_solver_dependency': 'PARI/GP 2.17.4 thueinit flag 1; not independently proved by this auditor',
        'audit_scope': 'Independent exact arithmetic, coverage, encoding, raw gap-2 transcript, and interval verification; no Lean run',
        'inputs': [first_audit, second_audit],
        'raw_union_including_n_2': sorted(candidates),
        'valid_n_ge_3': valid,
        'n_below_104_count': sum(n < 104 for n in valid),
        'n_ge_104': remaining,
        'rejections': rows,
        'survivors': [row['n'] for row in rows if not row['excluded']],
        'source_sha256': digest(Path(__file__)),
    }
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'valid_n_count': len(valid),
                      'n_ge_104_count': len(remaining), 'survivors': report['survivors'],
                      'output': str(destination)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gap1', required=True, type=Path)
    parser.add_argument('--gap2', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    arguments = parser.parse_args()
    run(arguments.gap1, arguments.gap2, arguments.output)
