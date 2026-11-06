#!/usr/bin/env python3
"""Check the finite remainder of the uniform cube-support reduction.

This script does not prove completeness of PARI's Thue solver.  It checks all
coefficient pairs and all returned points, and independently reconstructs the
five final divisibility/interval contradictions using exact integer arithmetic.
The unbounded input reduction is proved in v13_uniform_cube_support.md.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from math import gcd, prod
from pathlib import Path


def factors(value):
    result = []
    p = 2
    while p * p <= value:
        if value % p == 0:
            exponent = 0
            while value % p == 0:
                exponent += 1
                value //= p
            result.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if value > 1:
        result.append((value, 1))
    return result


def check(source):
    data = json.loads(source.read_text())
    assert data['status'] == 'PASS'
    assert data['support_primes'] == [2, 3, 5, 7]
    assert data['thueinit_flag'] == 1
    primes = data['support_primes']
    # Independent enumeration: form every core, then take coprime pairs.
    cores = sorted(prod(p**e for p, e in zip(primes, exponents))
                   for exponents in itertools.product(range(3), repeat=4))
    pairs = {(a, b) for a in cores for b in cores if gcd(a, b) == 1}
    observed = [(row['A'], row['B']) for row in data['records']]
    assert len(observed) == len(set(observed)) == 625
    assert set(observed) == pairs
    possible_n = set()
    for row in data['records']:
        a, b = row['A'], row['B']
        positive = []
        for x, y in row['all_integer_solutions']:
            assert a*x**3-b*y**3 == 1
            if x > 0 and y > 0:
                positive.append(a*x**3)
                possible_n.add(a*x**3)
        assert sorted(positive) == row['positive_n']
    assert sorted(possible_n) == data['positive_n']
    assert sorted(n for n in possible_n if n >= 104) == [126, 225, 2401, 4375, 6860]

    rejections = []
    for n in sorted(possible_n):
        if n < 104:
            continue
        a = n*(n-1)*(n-2)//6
        d = a // gcd(a, n-2)
        fd = factors(d)
        assert prod(p**e for p, e in fd) == d
        f = prod(p**((e+2)//3) for p, e in fd)
        first_r = f * (3*n//f + 1)
        assert first_r > 3*n and first_r-f <= 3*n
        upper = Fraction(10*n, 3)
        log_lower = None
        if n >= 1024:
            # e < 3 implies log(n) > L whenever 3**L < n.
            power, exponent = 1, 0
            while power*3 < n:
                power *= 3
                exponent += 1
            assert exponent > 0 and power == 3**exponent < n
            logarithmic_upper = Fraction(3*n) + Fraction(3*n, 4*exponent)
            if logarithmic_upper < upper:
                upper = logarithmic_upper
                log_lower = exponent
        assert first_r * upper.denominator >= upper.numerator
        rejections.append({
            'n': n, 'binomial_n_3': a,
            'D': d, 'D_factorization': fd, 'forced_divisor_F': f,
            'r_strict_lower_bound': 3*n,
            'first_F_multiple_above_lower_bound': first_r,
            'r_strict_upper_bound': [upper.numerator, upper.denominator],
            'natural_log_strict_lower_bound': log_lower,
            'excluded': True,
        })

    return {
        'status': 'PASS',
        'support_primes': primes,
        'complete_coefficient_pairs': len(pairs),
        'positive_first_indices': sorted(possible_n),
        'indices_below_prior_cutoff_104': sum(n < 104 for n in possible_n),
        'remaining_index_count': len(rejections),
        'remaining_after_divisibility_interval_checks': 0,
        'rejections': rejections,
        'proof_scope': 'Exact finite check after the written uniform reduction and PARI complete Thue solving; not Lean verification.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'thue_results_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=Path(__file__).with_name('v13_thue_support_results.json'))
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('v13_branch_filter_results.json'))
    arguments = parser.parse_args()
    report = check(arguments.input)
    arguments.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
