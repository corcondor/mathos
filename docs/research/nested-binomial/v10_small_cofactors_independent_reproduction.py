#!/usr/bin/env python3
"""Reproduce the thirty-cofactor exclusion without reading saved certificates.

This uses the proved quartic bound n < 9*w^4+2 and p<=6*w rather
than the short exponent progression used by the primary certificate.
Squared-index valuations are calculated from base-p digit sums.
"""

from collections import Counter
from hashlib import sha256
from math import gcd, isqrt, prod
from pathlib import Path
import json
import time

BASE = Path(__file__).resolve().parent


def primes_through(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p:limit+1:p] = b'\x00' * ((limit-p*p)//p + 1)
    return [p for p in range(2, limit+1) if flags[p]]


def factor(n, primes):
    out = {}
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    if n > 1:
        out[n] = 1
    return out


def digit_sum(n, p):
    total = 0
    while n:
        n, rem = divmod(n, p)
        total += rem
    return total


def choose_valuation_by_digits(n, k, p):
    numerator = digit_sum(k, p) + digit_sum(n-k, p) - digit_sum(n, p)
    assert numerator >= 0 and numerator % (p-1) == 0
    return numerator // (p-1)


def run():
    start = time.monotonic()
    # Reconstruct w=c*g with g=gcd(w,6), so w/g<=12.
    W = sorted({c*g for g in (1,2,3,6) for c in range(1,13)
                if gcd(c*g, 6) == g})
    assert len(W) == 30
    small_primes = primes_through(6*max(W))
    domain = []
    for w in W:
        for p in small_primes:
            if p > 6*w:
                break
            if w % p == 0:
                continue
            a, q = 1, p
            # The domain includes all powers under the proved polynomial
            # bound; it does not use D_w or the local exponent progression.
            while q < 9*w**3:
                n = w*q + 2
                if n >= 104:
                    domain.append((w,p,a,n))
                a, q = a+1, q*p
    indices = sorted({row[3] for row in domain})
    primes = primes_through(isqrt(max(indices)))
    results = {}
    prime_rows = 0
    for n in indices:
        fac = {}
        for v in (n,n-1,n-2):
            for p,a in factor(v,primes).items():
                fac[p] = fac.get(p,0)+a
        fac[2] -= 1
        fac[3] -= 1
        fac = {p:a for p,a in fac.items() if a}
        A = n*(n-1)*(n-2)//6
        assert prod(p**a for p,a in fac.items()) == A
        F = 1
        for p,a in fac.items():
            x = choose_valuation_by_digits(n*n, 6*n-9, p)
            e = next(t for t in range(a+1) if 3*t >= a or 2*t == x)
            F *= p**e
            prime_rows += 1
        E = A//gcd(A,F**3)
        assert ((n-2)//gcd(n-2,6)) % E == 0
        first = F*(3*n//F+1)
        if E <= 12:
            outcome = 'recovered_defect_at_most_12'
        elif 3*first >= 10*n:
            outcome = 'no_multiple_in_broad_gap'
        elif n >= 1024 and n > 3**8 and 32*first >= 99*n:
            # e<3 and n>3^8 give log(n)>8; use the strict v6 gap.
            outcome = 'logarithmic_gap_with_log_n_greater_than_8'
        else:
            raise AssertionError(('survivor',n,F,E,first))
        results[n] = (outcome,F,E,first)
    out = {
        'status': 'PASS',
        'scope': 'ell=1, j=i-3, i=w*p^a+2, w/gcd(w,6)<=12',
        'method': 'Independent enlarged domain p<=6w, p^a<9w^3; no certificate input or D_w exponent progression',
        'cofactors': W,
        'parameter_records': len(domain),
        'distinct_indices': len(indices),
        'maximum_index': max(indices),
        'parameter_exclusion_counts': dict(Counter(results[n][0] for w,p,a,n in domain)),
        'distinct_index_exclusion_counts': dict(Counter(v[0] for v in results.values())),
        'digit_sum_valuations_checked': prime_rows,
        'logarithmic_gap_records': [dict(n=n,F=v[1],E=v[2],first=v[3])
                                    for n,v in results.items() if v[0].startswith('logarithmic')],
        'survivors': 0,
        'reads_primary_certificate': False,
        'all_integer_arithmetic_exact': True,
        'arbitrary_search_cutoff': False,
        'original_i_interval_scanned': False,
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds': time.monotonic()-start,
    }
    (BASE/'v10_small_cofactors_independent_reproduction_verification.json').write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    run()
