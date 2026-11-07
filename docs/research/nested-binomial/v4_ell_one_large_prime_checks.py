#!/usr/bin/env python3
"""Direct-binomial consistency checks of the new p-adic identities.

This checks finite examples of universal proved identities; it is not a
certificate that excludes all lower-branch harmonic candidates.
"""
import json
from math import comb, isqrt
from pathlib import Path


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def main():
    cases = 0
    lower_harmonic_survivors = []
    for p in range(5, 62):
        if not prime(p):
            continue
        for j in range(p // 2 + 1, p - 1):
            if j % 2 == 0:
                continue
            i = j * p**3
            A = comb(i, j)
            X = comb(i * i, j * j)
            L = comb(A, p)
            assert A % p**3 == 0
            assert (A // p**3) % p**3 == 1
            assert L % p**2 == 0
            assert (L // p**2) % p**3 == 1
            assert X % p**6 == 0 and (X // p**6) % p == 1
            upper_residual = L - X - (A - p)**2
            assert upper_residual % p**4 == 0
            assert (upper_residual // p**4) % p == 2
            harmonic = sum(pow(h, -1, p*p) for h in range(1, j)) % (p*p)
            lower_residual = L - X - p*p
            assert lower_residual % p**5 == 0
            assert (lower_residual // p**5) % (p*p) == (-j*harmonic-p) % (p*p)
            if (j*harmonic+p) % (p*p) == 0:
                lower_harmonic_survivors.append([p, j])
            cases += 1
    report = {
        'status': 'all_exact_binomial_consistency_checks_passed',
        'prime_inclusive_bound': 61,
        'pairs_checked': cases,
        'range': 'p/2<j<=p-2, j odd; i=j*p^3',
        'upper_residual_checked': '(L-X-(A-p)^2)/p^4 == 2 (mod p)',
        'lower_residual_checked': '(L-X-p^2)/p^5 == -j*H_(j-1)-p (mod p^2)',
        'lower_harmonic_survivors_in_this_finite_check': lower_harmonic_survivors,
        'global_lower_exclusion_claimed': False,
        'Lean_executed': False,
    }
    Path('v4_ell_one_large_prime_checks.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
