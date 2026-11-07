#!/usr/bin/env python3
"""Finite exact certificate for the uniform proof in v8_shifted_base_three.md."""

from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path
from hashlib import sha256
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factorization(n, factors):
    assert all(prime(p) and e >= 1 for p, e in factors.items())
    assert prod(p ** e for p, e in factors.items()) == n
    return {"n": n, "prime_factors": {str(p): e for p, e in factors.items()}}


small = []
for a in range(1, 5):
    n = 3 ** a + 2
    assert n - 3 <= 100
    small.append({"a": a, "n": n, "exclusion": "previous complete j<=100 theorem"})

n = 3 ** 5 + 2
assert n == 245
assert gcd(n, 3) == 1 and (n - 1) // gcd(n - 1, 6) == 122
factorization(n, {5: 1, 7: 2})
factorization(122, {2: 1, 61: 1})
assert prod([5, 7, 2, 61]) == 4270
assert 3 * 4270 > 10 * n
small.append({"a": 5, "n": n, "exclusion": "forced r divisor 4270 exceeds 10n/3"})

for a, fac in [(6, {17: 1, 43: 1}), (7, {11: 1, 199: 1})]:
    n = 3 ** a + 2
    entry = factorization(n, fac)
    assert gcd(n, 3) == 1 and all(e == 1 for e in fac.values())
    entry.update(a=a, exclusion="squarefree first index")
    small.append(entry)

# a=8, and every larger even a, are uniformly excluded by 2d=a-1.
assert (8 - 1) % 2 == 1

z = 3 ** 9
n = z + 2
Q = n * (n - 1) // 2
assert z > 320 and gcd(Q, 3) == 1
ratio = Fraction((z + 2) ** 2, z * (z + 1))
assert ratio == 1 + Fraction(3 * z + 4, z * (z + 1))
assert ratio < 1 + Fraction(4, z) < Fraction(81, 80)
assert Fraction(2000, 27) * Fraction(81, 80) == 75
assert Fraction(2000, 27) * ratio < 75 < 81
assert 3 ** ((11 - 3) // 2) == 81

last = factorization(n, {5: 1, 31: 1, 127: 1})
assert n == 19685 and gcd(n, 3) == 1
assert Fraction(10, 3) < 4
last.update(a=9, exclusion="squarefree n forces r multiple of n; interval 3n<r<10n/3 has none")

report = {
    "status": "PASS",
    "scope": "exact certificates for the uniform exponent bound and its one residual exponent",
    "original_equation": "choose(choose(i,j),choose(k,ell)) = choose(i^2,j^2)+choose(k^2,ell^2)",
    "complete_exclusion": "ell=1, j=i-3, i=3^a+2, a>=1",
    "combined_v7_v8_exclusion": "ell=1, j=i-3, i=3*p^a+2 for every prime p and a>=1",
    "small_exponent_coverage": small,
    "all_even_a_at_least_8": "excluded by the proved identity 2d=a-1",
    "exponent_bound": {
        "input": "a>=9 odd, d=(a-1)/2",
        "proved_inequality": "3^((a-3)/2) < 75 < 81",
        "remaining_exponents": [9],
        "rational_bound_numerator_at_a9": (Fraction(2000, 27) * ratio).numerator,
        "rational_bound_denominator_at_a9": (Fraction(2000, 27) * ratio).denominator,
    },
    "single_remaining_case": last,
    "unbounded_scan": False,
    "wieferich_distribution_assumption": False,
    "new_lean_formalization": False,
}
source = Path(__file__).resolve()
report["checker_sha256"] = sha256(source.read_bytes()).hexdigest()
output = source.with_name("v8_shifted_base_three_verification.json")
output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": report["status"], "remaining_cases_verified": 1, "output": str(output)}))
