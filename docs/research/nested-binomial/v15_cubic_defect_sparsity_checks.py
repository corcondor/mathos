#!/usr/bin/env python3
"""Exact finite consistency checks for the uniform cubic-defect counting proof.

These checks neither search for solutions of the original equation nor
prove the uniform bound by finite extrapolation. They use no Thue solver.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def factor_table(limit):
    smallest = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if smallest[p] == p:
            for k in range(p * p, limit + 1, p):
                if smallest[k] == k:
                    smallest[k] = p
    return smallest


def prime_exponents(n, smallest):
    factors = []
    while n > 1:
        p = smallest[n]
        exponent = 0
        while n % p == 0:
            exponent += 1
            n //= p
        factors.append((p, exponent))
    return factors


def cube_ceiling(n, smallest):
    result = 1
    for p, exponent in prime_exponents(n, smallest):
        result *= p ** ((exponent + 2) // 3)
    return result


def canonical(n, smallest):
    a = b = c = 1
    for p, exponent in prime_exponents(n, smallest):
        h, e = divmod(exponent, 3)
        c *= p ** h
        if e == 1:
            a *= p
        elif e == 2:
            b *= p
    return a, b, c


def integer_cuberoot(n):
    lo, hi = 0, 1
    while hi ** 3 <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def triple_upper_bound(limit, constant):
    return sum(
        math.isqrt(limit // (a * c ** 3))
        for c in range(1, integer_cuberoot(limit) + 1)
        for a in range(1, constant * c + 1)
    )


def run(limit, output):
    require(limit >= 104, 'limit must be at least 104')
    smallest = factor_table(limit)
    data = [None] * (limit + 1)
    for m in range(1, limit + 1):
        a, b, c = canonical(m, smallest)
        ceiling = cube_ceiling(m, smallest)
        defect = m // ceiling
        require(m == a * b * b * c ** 3, f'canonical identity at {m}')
        require(ceiling == a * b * c, f'c3 identity at {m}')
        require(defect == b * c * c, f'defect identity at {m}')
        require(math.gcd(a, b) == 1, f'core coprimality at {m}')
        require(all(e == 1 for _, e in prime_exponents(a, smallest)), f'a squarefree at {m}')
        require(all(e == 1 for _, e in prime_exponents(b, smallest)), f'b squarefree at {m}')
        require(m < 21 * defect * defect if a < 21 * c else m >= 21 * defect * defect,
                f'ratio identity at {m}')
        data[m] = (a, b, c, ceiling, defect)

    candidates = []
    logarithmic_candidates = []
    witness_both_count = 0
    for n in range(104, limit + 1):
        g = math.gcd(n, 3)
        d = math.gcd(n - 1, 6)
        require(6 % (g * d) == 0, f'gd divides 6 at {n}')
        c1 = cube_ceiling(n // g, smallest)
        c2 = cube_ceiling((n - 1) // d, smallest)
        require(math.gcd(c1, c2) == 1, f'coprime roots at {n}')
        modulus = c1 * c2
        r = modulus * ((3 * n) // modulus + 1)
        if 3 * r >= 10 * n:
            continue
        require(r ** 3 % ((n // g) * ((n - 1) // d)) == 0,
                f'original common divisibility at {n}')
        require(data[n][3] * data[n - 1][3] <= 6 * r < 20 * n,
                f'root product bound at {n}')
        require(n - 1 < 20 * data[n][4] * data[n - 1][4],
                f'defect product bound at {n}')
        flags = [data[m][0] < 21 * data[m][2] for m in [n, n - 1]]
        require(any(flags), f'canonical witness at {n}')
        witness_both_count += int(all(flags))
        candidates.append(n)

        # A rational upper bound weaker than the actual logarithmic one:
        # 3^L<n implies log(n)>L because e<3.
        if n >= 1024:
            L = 0
            while 3 ** (L + 1) < n:
                L += 1
            require(L >= 6, f'positive logarithm lower bound at {n}')
            if 4 * L * r < 12 * L * n + 3 * n:
                require(data[n][3] * data[n - 1][3] * 4 < 75 * n,
                        f'stronger product bound at {n}')
                require(any(data[m][0] < 19 * data[m][2] for m in [n, n - 1]),
                        f'constant19 witness at {n}')
                logarithmic_candidates.append(n)

    checkpoints = sorted({v for v in [104, 1000, 10000, 100000, limit] if v <= limit})
    counts = []
    for bound in checkpoints:
        witness21 = sum(data[m][0] <= 21 * data[m][2] for m in range(1, bound + 1))
        witness19 = sum(data[m][0] <= 19 * data[m][2] for m in range(1, bound + 1))
        triples21 = triple_upper_bound(bound, 21)
        triples19 = triple_upper_bound(bound, 19)
        require(witness21 <= triples21, f'triple counting at {bound}, constant21')
        require(witness19 <= triples19, f'triple counting at {bound}, constant19')
        candidate_count = sum(n <= bound for n in candidates)
        require(candidate_count <= 2 * witness21, f'index-to-witness count at {bound}')
        counts.append({
            'X': bound,
            'canonical_witnesses_C21': witness21,
            'all_integer_triples_C21': triples21,
            'canonical_witnesses_C19': witness19,
            'all_integer_triples_C19': triples19,
            'necessary_divisibility_interval_indices': candidate_count,
            'weaker_rational_log_interval_indices_n_ge_1024': sum(n <= bound for n in logarithmic_candidates),
        })

    result = {
        'status': 'PASS',
        'scope': 'Finite consistency checks of a written uniform counting proof; not original-equation solutions',
        'limit': limit,
        'canonical_identity_checks': limit,
        'necessary_divisibility_interval_indices': len(candidates),
        'witness_both_count': witness_both_count,
        'weaker_rational_log_interval_indices_n_ge_1024': len(logarithmic_candidates),
        'candidate_sample': candidates[:25],
        'checkpoints': counts,
        'uniform_theorem': 'T(X) <= 4 sqrt(21X) H_floor(cuberoot(X)) <= 4 sqrt(21X) (1+log(X)/3)',
        'proof_not_extrapolation': True,
        'new_lean_execution': False,
        'new_cas_calls': 0,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=100000)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    run(arguments.limit, arguments.output)
