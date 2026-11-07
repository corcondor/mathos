#!/usr/bin/env python3
"""Exact certificates for v7_offset_cofactor_three.md.

The finite domains follow from the proved bound p^(3d-a) < 223.
No original binomial equation is searched. Generation uses a sieve and
factorization; verification uses independent trial-division primality
and reconstructs the domains from the exponent inequalities.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT / "v7_offset_cofactor_three_certificates.json"
REPORT = ROOT / "v7_offset_cofactor_three_verification.json"


def factor(n: int) -> dict[int, int]:
    assert n >= 1
    factors: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def prime_trial(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_sieve(limit: int) -> list[int]:
    flags = bytearray(b"\1") * (limit + 1)
    flags[:2] = b"\0\0"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p * p : limit + 1 : p] = b"\0" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def valuation(n: int, p: int) -> int:
    assert n > 0
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def binomial_valuation(n: int, k: int, p: int) -> int:
    assert 0 <= k <= n
    result = 0
    power = p
    while power <= n:
        result += n // power - k // power - (n - k) // power
        power *= p
    return result


def make_row(p: int, a: int, large: bool) -> dict:
    n = 3 * p**a + 2
    H = n * (n - 1) // 2
    d = a // 2 if p in (5, 11) or p >= 19 else (a - 1) // 2
    if large and p == 71:
        factors = factor((n - 1) // 2)
    else:
        factors = factor(n)
        if p == 2:
            factors.pop(2, None)
    primes = sorted(factors)
    D = prod(primes)
    return {
        "p": p,
        "a": a,
        "n": n,
        "d": d,
        "H": H,
        "D": D,
        "distinct_prime_factors_of_D": primes,
        "contradiction": "D > 10p" if large else "3*p^d*D >= 10n",
        "integer_margin": D - 10 * p if large else 3 * p**d * D - 10 * n,
    }


def generate() -> dict:
    large_rows = [make_row(p, 2, True) for p in prime_sieve(222) if p >= 19]
    small_powers = {
        2: [9, 11, 13, 15, 17],
        5: [4, 6],
        7: [3, 5, 7],
        11: [4],
        13: [3, 5, 7],
        17: [3, 5],
    }
    small_rows = [make_row(p, a, False) for p, aa in small_powers.items() for a in aa]
    low_rows = []
    for p in small_powers:
        a = 1
        while 3 * p**a + 2 < 1024:
            n = 3 * p**a + 2
            if n >= 104:
                low_rows.append({"p": p, "a": a, "n": n, "prime_factors": sorted(factor(n))})
            a += 1
    return {
        "scope": "ell=1, j=i-3, i=3*p^a+2, p prime other than 3",
        "large_prime_remainder": large_rows,
        "small_prime_remainder": small_rows,
        "small_first_indices": low_rows,
    }


def verify(data: dict) -> dict:
    # Reconstruct the domain from the proved inequalities, independently of
    # the generator's hard-coded small-base exponent lists.
    expected_large = {(p, 2) for p in range(19, 223) if prime_trial(p)}
    expected_small: set[tuple[int, int]] = set()
    for p in (2, 5, 7, 11, 13, 17):
        if p in (5, 11):
            d = 1
            while p**d < 223:
                a = 2 * d
                if 3 * p**a + 2 >= 1024:
                    expected_small.add((p, a))
                d += 1
        else:
            d = 0
            while p**d < 223 * p:
                a = 2 * d + 1
                if 3 * p**a + 2 >= 1024:
                    expected_small.add((p, a))
                d += 1
    assert len(expected_large) == 40
    assert len(expected_small) == 16
    smallest_margin = {}
    for key, expected in (("large_prime_remainder", expected_large), ("small_prime_remainder", expected_small)):
        rows = data[key]
        assert len(rows) == len(expected)
        assert {(row["p"], row["a"]) for row in rows} == expected
        margins = []
        for row in rows:
            p, a, d, D = (row[t] for t in ("p", "a", "d", "D"))
            assert prime_trial(p) and p != 3
            n = 3 * p**a + 2
            H = n * (n - 1) // 2
            assert row["n"] == n >= 1024 and row["H"] == H
            assert gcd(H, p) == 1
            assert 2 * d == (a if p in (5, 11) or p >= 19 else a - 1)
            assert p ** (3 * d) < 223 * p**a
            primes = row["distinct_prime_factors_of_D"]
            assert primes == sorted(set(primes))
            assert all(prime_trial(t) for t in primes)
            assert prod(primes) == D and H % D == 0
            margin = D - 10 * p if key == "large_prime_remainder" else 3 * p**d * D - 10 * n
            assert margin == row["integer_margin"] and margin > 0
            margins.append(margin)
        smallest_margin[key] = min(margins)

    # Check completeness and the deterministic squarefree witnesses for
    # the eight earlier small-index cases.
    expected_low = set()
    for p in (2, 5, 7, 11, 13, 17):
        q, a = p, 1
        while 3 * q + 2 < 1024:
            if 3 * q + 2 >= 104:
                expected_low.add((p, a))
            q *= p
            a += 1
    low_rows = data["small_first_indices"]
    assert len(low_rows) == len(expected_low) == 8
    assert {(row["p"], row["a"]) for row in low_rows} == expected_low
    for row in low_rows:
        n = 3 * row["p"] ** row["a"] + 2
        factors = row["prime_factors"]
        assert row["n"] == n and gcd(n, 3) == 1
        assert factors == sorted(set(factors))
        assert all(prime_trial(t) for t in factors)
        assert prod(factors) == n

    # Exact constants and residual coverage in the dominant-prime note.
    assert Fraction(6 * 37**3, 37**2 - 37 + 12) == Fraction(50653, 224)
    assert Fraction(50653, 224) > Fraction(208000, 927)
    residual = []
    for p in range(7, 37):
        if prime_trial(p):
            for w in range(1, (p - 1) // 6 + 1):
                n = w * p + 2
                if n >= 104:
                    residual.append((p, w, n))
                    q0 = n // gcd(n, 3)
                    assert all(e == 1 for e in factor(q0).values())
    assert residual == [(29, 4, 118), (31, 4, 126), (31, 5, 157)]
    assert 63 * 341**2 - 17979 * 341 - 8000 == 1186864 > 0
    assert 126 * 341 - 17979 > 0
    assert 19**2 > 223
    assert 2**3 * 3**2 * 7 * 13 * 17 == 111384

    # Independent Legendre sums corroborate the uniform valuation proofs.
    samples = sorted(expected_small | {(19, 2), (19, 3), (23, 2), (37, 4)})
    for p, a in samples:
        q, n = p**a, 3 * p**a + 2
        A = n * (n - 1) * (n - 2) // 6
        T = A // q
        d = max(1, a // 2)
        u = p**d
        assert 6 < u < q
        r = 9 * q + u
        assert valuation(A, p) == a and valuation(r, p) == d
        expected_x = a if p in (5, 11) or p >= 19 else a - 1
        expected_l = 2 * a - d - (p == 2)
        assert binomial_valuation(n * n, 6 * n - 9, p) == expected_x
        assert binomial_valuation(A, r, p) == expected_l
        assert binomial_valuation(A - 1, r - 1, p) == binomial_valuation(T - 1, 9, p)

    return {
        "status": "PASS",
        "large_prime_pairs": len(expected_large),
        "small_prime_pairs": len(expected_small),
        "earlier_small_index_exclusions": len(expected_low),
        "dominant_prime_residual_integers": [n for _, _, n in residual],
        "exact_valuation_samples": len(samples),
        "smallest_positive_certificate_margins": smallest_margin,
        "largest_first_index_in_derived_remainder": max(row["n"] for key in ("large_prime_remainder", "small_prime_remainder") for row in data[key]),
        "unresolved_cases": 0,
        "proof_scope": "Complete exclusion only of ell=1, j=i-3, i=3*p^a+2 for prime p != 3; dominant-prime theorem also verified as documented.",
        "not_lean_formalized": True,
    }


def main() -> None:
    data = generate()
    CERT.write_text(json.dumps(data, indent=2) + "\n")
    report = verify(json.loads(CERT.read_text()))
    report["certificate_sha256"] = hashlib.sha256(CERT.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
