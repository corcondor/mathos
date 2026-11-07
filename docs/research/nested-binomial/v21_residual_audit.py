#!/usr/bin/env python3
"""v21 complete residual scan: exact integer arithmetic, no external modules.

Assumes the proved v21 inequality a² < 152 rho ln(rho) and the inherited
necessary conditions for actual solutions, NOT all auxiliary sextic points.
"""
from math import comb, gcd, isqrt
from pathlib import Path
import json

DIVISORS_486 = (1, 2, 3, 6, 9, 18, 27, 54, 81, 162, 243, 486)
RHO_LIMIT = 4096
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)


def sextic(a, b, rho):
    a2, b2 = a*a, b*b
    return (4*a2**3 + (24*b2 - 12*rho)*a2*a2
            + (36*b2*b2 + 60*b2*rho + 12*rho*rho)*a2
            - 3*b2*rho*rho - 4*rho**3)


def binomial_lucas(n, k, p):
    if not (0 <= k <= n):
        return 0
    x = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        x = x * comb(ni, ki) % p
        n //= p
        k //= p
    return x


def modular_witness(n, r):
    A = n*(n-1)*(n-2)//6
    m = 6*n-9
    return {
        side: next(p for p in SMALL_PRIMES
                   if (binomial_lucas(A, r, p)
                       - binomial_lucas(n*n, m, p) - (k*k)%p) % p != 0)
        for side, k in (("k=r", r), ("k=A-r", A-r))
    }


def enumerate_residuals(bound=RHO_LIMIT):
    counts = dict(attempts=0, primitive_filtered=0, residual_squares=0,
                  positive_integer_t=0, integer_n=0, branch_points=0)
    result = []
    for rho in range(13, bound+1):
        if rho % 9 not in (1, 4, 6, 7):
            continue
        # ln(rho) < bit_length(rho)*ln(2) < bit_length(rho).
        # Thus this bound rigorously covers all a² < 152 rho ln(rho).
        a_max = isqrt(152*rho*rho.bit_length())
        for b in DIVISORS_486:
            for a in range(b+1, a_max+1):
                counts['attempts'] += 1
                if (27*a < 31*b or gcd(a, b) != 1
                    or gcd(a, rho) != gcd(a, 3)
                    or (a*a-rho) % b != 0
                    or (rho-a-b) % 2 != 0):
                    continue
                a2, b2 = a*a, b*b
                if a2 <= b2+rho or 1377*rho >= 216*a2+760*b2:
                    continue
                counts['primitive_filtered'] += 1
                f = sextic(a, b, rho)
                if f < 0:
                    continue
                y = isqrt(f)
                if y*y != f:
                    continue
                counts['residual_squares'] += 1
                for sign in (-1, +1):
                    numerator = 2*a*(a2+3*b2) - rho*(3*b+2*a) + sign*y
                    denominator = 2*b*rho
                    if numerator % denominator:
                        continue
                    t = numerator // denominator
                    if t <= 0:
                        continue
                    counts['positive_integer_t'] += 1
                    q = t*t+3*t+3
                    nnum = b2*q + a*b*(t+6) - a2 + rho
                    if nnum % (9*a*b):
                        continue
                    n = nnum // (9*a*b)
                    counts['integer_n'] += 1
                    r = 3*n+t
                    if n < 104 or t*t <= 9*n or 3*r >= 10*n:
                        continue
                    counts['branch_points'] += 1
                    M = gcd(n, 3)*gcd(n-1, 6)
                    Q = n*(n-1)//M
                    delta = Q // gcd(Q, r*r)
                    # Check these are genuine integer points of the
                    # reconstruction identities, even though they need not
                    # satisfy the original binomial equation.
                    assert 81*a*n*(n-1) == b*(9*n*q+t*t*t)
                    assert rho == a*a + a*b*(9*n-t-6) - b*b*q
                    result.append(dict(rho=rho, a=a, b=b, t=t, n=n,
                                       delta=delta, witnesses=modular_witness(n, r)))
    return {'bound':bound, 'counts':counts, 'points':result,
            'method':'exact standard library; Lucas mod prime for both k branches'}


if __name__ == '__main__':
    d = enumerate_residuals()
    path = Path(__file__).with_name('v21_residual_certificate.json')
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True)+'\n')
    print(json.dumps(d, ensure_ascii=False, indent=2))
    assert len(d['points']) == 8
    assert all(p['witnesses']['k=r'] and p['witnesses']['k=A-r']
               for p in d['points'])
