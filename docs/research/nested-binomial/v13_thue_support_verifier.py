#!/usr/bin/env python3
"""Independent encodings of the fixed prime-support Thue reduction.

This uses PARI/GP twice, so it is not an independent CAS implementation.
No upper bound for n, a, or b is used.  thueinit flag=1 removes GRH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess


def core_pairs(primes):
    # Prime-wise assignment instead of enumerating a square core table.
    choices = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2))
    pairs = set()
    for exponents in itertools.product(choices, repeat=len(primes)):
        left = math.prod(p**e[0] for p, e in zip(primes, exponents))
        right = math.prod(p**e[1] for p, e in zip(primes, exponents))
        assert math.gcd(left, right) == 1
        pairs.add((left, right))
    assert len(pairs) == 5 ** len(primes)
    return sorted(pairs)


def run(gp, primes, destination):
    pairs = core_pairs(primes)
    lines = ['print(version());']
    for a, b in pairs:
        lines.append(
            f'print([{a},{b},'
            f'thue(thueinit({a}*x^3-{b},1),1),'
            f'thue(thueinit(x^3-{a*a*b},1),{a*a})]);'
        )
    lines.append('quit;')
    program = '\n'.join(lines) + '\n'
    process = subprocess.run(
        [str(gp), '-f', '-q'], input=program, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
        timeout=180,
    )
    if process.stderr.strip():
        raise RuntimeError(f'Unexpected PARI stderr: {process.stderr}')
    output = process.stdout.splitlines()
    version = ast.literal_eval(output[0])
    records = [ast.literal_eval(line) for line in output[1:]]
    assert [(row[0], row[1]) for row in records] == pairs
    results = []
    positive_ns = set()
    for a, b, direct, transformed in records:
        direct = sorted(tuple(row) for row in direct)
        for x, y in direct:
            assert a*x**3-b*y**3 == 1
        for u, y in transformed:
            assert u**3-a*a*b*y**3 == a*a
        recovered = sorted((u//a, y) for u, y in transformed if u % a == 0)
        assert direct == recovered
        positive = [(x, y) for x, y in direct if x > 0 and y > 0]
        ns = sorted(a*x**3 for x, y in positive)
        positive_ns.update(ns)
        results.append({'A':a, 'B':b, 'all_integer_solutions':direct,
                        'transformed_all_integer_solutions':transformed,
                        'positive_solutions':positive, 'positive_n':ns})
    report = {
        'status':'PASS',
        'pari_version':version,
        'support_primes':primes,
        'pair_count':len(pairs),
        'pari_calls':2*len(pairs),
        'thueinit_flag':1,
        'unbounded_variables':['n','a','b'],
        'same_backend_twice':True,
        'positive_n':sorted(positive_ns),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'gp_input_sha256':hashlib.sha256(program.encode()).hexdigest(),
        'gp_stdout_sha256':hashlib.sha256(process.stdout.encode()).hexdigest(),
        'records':results,
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2)+'\n')
    destination.with_suffix('.gp').write_text(program)
    destination.with_suffix('.stdout').write_text(process.stdout)
    print(json.dumps({k:v for k,v in report.items() if k != 'records'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gp', type=Path, required=True)
    parser.add_argument('--primes', type=int, nargs='+', default=[2,3])
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    run(arguments.gp, arguments.primes, arguments.output)
