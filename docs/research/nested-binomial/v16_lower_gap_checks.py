#!/usr/bin/env python3
"""Exact algebra and finite consistency checks for the v16 lower-gap proof."""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


# A Laurent polynomial in (M,h,t,n), with exact rational coefficients.
# Negative powers occur only for M, whose mathematical domain is positive.
class Poly:
    def __init__(self, terms):
        if isinstance(terms, (int, F)):
            terms = {(0, 0, 0, 0): F(terms)}
        self.terms = {e: F(c) for e, c in terms.items() if c}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly(value)

    def __add__(self, other):
        result = self.terms.copy()
        for e, c in self.coerce(other).terms.items():
            result[e] = result.get(e, F(0)) + c
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        result = {}
        for e, c in self.terms.items():
            for f, d in self.coerce(other).terms.items():
                powers = tuple(a + b for a, b in zip(e, f))
                result[powers] = result.get(powers, F(0)) + c * d
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, power):
        require(power >= 0, 'nonnegative polynomial power')
        result = Poly(1)
        for _ in range(power):
            result = result * self
        return result


def polynomial_identities():
    M = Poly({(1, 0, 0, 0): 1})
    inv_M = Poly({(-1, 0, 0, 0): 1})
    h = Poly({(0, 1, 0, 0): 1})
    t = Poly({(0, 0, 1, 0): 1})
    n = Poly({(0, 0, 0, 1): 1})
    D = 9 * t ** 2 + 27 * t + 27
    P = M * D + h
    q = P + F(2, 9) * h * (t - 3) - F(2, 729) * h ** 2 * inv_M
    R = (24 * M * h * t + 36 * M * h + F(28, 27) * h ** 2
         + F(8, 6561) * h ** 3 * t * inv_M
         + F(4, 2187) * h ** 3 * inv_M
         - F(4, 531441) * h ** 4 * inv_M ** 2)
    lower_q = M * ((9 - F(32, 729)) * t ** 2 + 27 * t + 27)
    x = 2 * h * n - P
    expressions = {
        'cubic_division': (3 * n + t) ** 3 - ((27 * n + 27 * t + 27) * n * (n - 1) + D * n + t ** 3),
        'square_root_residual': P ** 2 + 4 * h * M * t ** 3 - q ** 2 - R,
        'lower_q_positive_polynomial': lower_q - F(17, 3) * M * (t + 3) ** 2
            - F(1, 729) * M * (2398 * (t - 4) ** 2 + 14081 * (t - 4) + 460),
        'fixed_denominator_parity': x - q - F(2, 729) * inv_M
            * (729 * M * (h * n - P) - 81 * M * h * (t - 3) + h ** 2),
        'residual_positive_grouping': R - (24 * M * h * t + 36 * M * h + F(28, 27) * h ** 2
            + F(4, 2187) * h ** 3 * inv_M
            + F(4, 531441) * h ** 3 * inv_M ** 2 * (162 * M * t - h)),
    }
    for name, expression in expressions.items():
        require(expression.terms == {}, name)
    return {name: 'all coefficients zero' for name in expressions}


def smallest_prime_factors(limit):
    factors = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if factors[p] == p:
            for m in range(p * p, limit + 1, p):
                if factors[m] == m:
                    factors[m] = p
    return factors


def cube_root_divisor(m, smallest):
    result = 1
    while m > 1:
        p = smallest[m]
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        result *= p ** ((e + 2) // 3)
    return result


def run(limit, output):
    require(limit >= 104, 'limit at least 104')
    algebra = polynomial_identities()
    C = 864 + F(8, 9) + F(8, 6561)
    K = F(2187, 68) * C
    B = K * F(28, 3) ** 3 * 36
    require(C == F(5674544, 6561), 'upper residual constant')
    require(K == F(1418636, 51), 'integer gap constant')
    require(B == F(124567589888, 153) < 2 ** 30, 'final constant')
    require(2 ** 30 - B == F(39714909184, 153), 'positive constant margin')

    smallest = smallest_prime_factors(limit)
    indices = []
    examples = []
    pair_count = 0
    min_t = None
    for n in range(104, limit + 1):
        g, d = gcd(n, 3), gcd(n - 1, 6)
        M = g * d
        Q = n * (n - 1) // M
        c3 = cube_root_divisor(n // g, smallest) * cube_root_divisor((n - 1) // d, smallest)
        first_r = (3 * n // c3 + 1) * c3
        if 3 * first_r >= 10 * n:
            continue
        indices.append(n)
        for r in range(first_r, (10 * n - 1) // 3 + 1, c3):
            require(r ** 3 % Q == 0 and 3 * n < r and 3 * r < 10 * n, 'input conditions')
            t = r - 3 * n
            u = t + 3
            D = 9 * t * t + 27 * t + 27
            numerator = M * (D * n + t ** 3)
            require(numerator % (n * (n - 1)) == 0, 'h integrality')
            h = numerator // (n * (n - 1))
            require(t >= 4 and 0 < h < 4 * M * t, 'h coarse bound')
            require(3 * n * h < 28 * M * u * u, 'h refined bound')
            P = M * D + h
            x = 2 * h * n - P
            q = P + F(2 * h * (t - 3), 9) - F(2 * h * h, 729 * M)
            R = x * x - q * q
            require(x > q > F(17 * M * u * u, 3), 'positive square-root comparison')
            require(x * x == P * P + 4 * h * M * t ** 3, 'integer discriminant')
            require((x - q) * F(729 * M, 2) >= 1 and ((x - q) * F(729 * M, 2)).denominator == 1,
                    'positive lattice spacing')
            require(F(68 * u * u, 2187) < R < C * F(h ** 3 * u, M), 'residual bounds')
            require(u < K * F(h ** 3, M), 'u versus h cubed')
            require(n ** 3 < B * u ** 5 < 2 ** 30 * u ** 5, 'three-fifths bound')
            pair_count += 1
            min_t = t if min_t is None else min(min_t, t)
            if len(examples) < 12:
                examples.append({'n': n, 'r': r, 't': t, 'M': M, 'h': h})

    here = Path(__file__).resolve().parent
    report = {
        'status': 'PASS',
        'scope': 'Exact polynomial coefficient and rational checks, plus finite consistency examples; universal completeness rests on the written proof.',
        'theorem': 'n^3 < 2^30*(r-3*n+3)^5',
        'inputs': 'n>=104, 3*n<r<10*n/3, M=gcd(n,3)*gcd(n-1,6), Q=n*(n-1)/M, Q divides r^3',
        'polynomial_identities': algebra,
        'exact_constants': {'residual_upper': str(C), 'u_bound': str(K), 'n_cubed_bound': str(B), 'margin_below_2_30': str(2 ** 30 - B)},
        'finite_limit': limit,
        'necessary_condition_first_indices': len(indices),
        'necessary_condition_pairs': pair_count,
        'smallest_observed_t': min_t,
        'example_pairs': examples,
        'examples_are_original_equation_solutions': False,
        'proof_by_finite_extrapolation': False,
        'new_lean_execution': False,
        'new_deepseek_api_calls': 0,
        'new_complete_cas_calls': 0,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256': hashlib.sha256((here / 'v16_lower_gap.md').read_bytes()).hexdigest(),
    }
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ['status', 'finite_limit', 'necessary_condition_first_indices',
                                                'necessary_condition_pairs', 'smallest_observed_t', 'exact_constants']}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=100000)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    run(args.limit, args.output)
