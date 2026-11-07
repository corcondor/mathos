#!/usr/bin/env python3
"""Exact corroboration for the uniform v8 cofactor proof.

The unbounded conclusions are proved in the companion note. These
checks verify constants and representative exact valuation identities;
they do not extrapolate an exclusion from a bounded search.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "v8_composite_dominant_prime_powers_verification.json"


def vp(n: int, p: int) -> int:
    assert n > 0
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a


def vbin(n: int, k: int, p: int) -> int:
    assert 0 <= k <= n
    e, h = 0, p
    while h <= n:
        e += n // h - k // h - (n - k) // h
        h *= p
    return e


def prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def main() -> None:
    t = 1083
    polynomial = 247 * t * t - 46628 * t - 62500
    assert polynomial == 239142959 > 0
    assert 494 * t - 46628 > 0
    assert Fraction(25, 8) ** 3 * Fraction((t + 2) ** 2, t * (t + 1)) < 31
    assert 36 * 3 > 62

    # (w,p,a,s), with both possible locations of the unique residue h
    # represented in the 8w<p<9w interval.
    parameters = [
        (1, 7, 3, 3),
        (1, 11, 3, 3),
        (2, 13, 2, 6),
        (2, 13, 5, 6),
        (2, 17, 3, 6),
        (3, 19, 2, 9),
        (3, 23, 4, 9),
        (4, 29, 2, 12),
        (4, 31, 3, 12),
        (5, 31, 5, 15),
        (5, 43, 2, 15),
        (5, 43, 2, 16),
        (6, 37, 2, 18),
        (6, 41, 4, 19),
        (7, 47, 2, 21),
        (7, 59, 2, 21),
        (7, 59, 2, 22),
        (9, 59, 2, 27),
        (12, 73, 4, 36),
    ]
    valuation_records = []
    for w, p, a, s in parameters:
        assert prime(p) and p > 6 * w and a >= 2
        q, n = p**a, w * p**a + 2
        A = n * (n - 1) * (n - 2) // 6
        T = A // q
        e = max(1, a // 2)
        r = s * q + p**e
        assert 3 * n < r and 3 * r < 10 * n
        assert s == r // q and 3 * w <= s < p
        assert vp(A, p) == a and vp(r, p) == e < a
        assert vbin(n * n, 6 * n - 9, p) == a
        actual_delta = vbin(T - 1, s, p)
        if w % 3 == 0:
            c = w // 3
            assert vp(T - c, p) == a
            expected_delta = a
            eta = 1 if w % 2 == 0 else 2
            Q = n * (n - 1) // eta
            assert Q == (n // gcd(n, 3)) * ((n - 1) // gcd(n - 1, 6))
            assert gcd(Q, p) == 1
            assert Fraction(25, 8) ** 3 * Fraction(n * n, q * (n - 1)) < 31 * w
            assert p**(a + 1) > 6 * (n - 2)
        else:
            h = (w * pow(3, -1, p)) % p
            tau = (3 * h - w) // p
            assert tau in (1, 2) and 3 * h == w + tau * p
            assert vp(T - h, p) == 1
            expected_delta = int(h <= s)
            if expected_delta:
                assert 6 * w < p < 9 * w and (p + w) % 3 == 0
            if 6 * w < p < 8 * w and (p + w) % 3 == 0:
                assert expected_delta == 1
        assert actual_delta == expected_delta
        assert vbin(A - 1, r - 1, p) == actual_delta
        assert vbin(A, r, p) == a - e + expected_delta
        assert vp((A - r) ** 2, p) == vp(r * r, p) == 2 * e
        valuation_records.append({"w": w, "p": p, "a": a, "s": s, "delta": actual_delta})

    # If q divides r in the nonmultiple-of-three cofactor case, the
    # outer valuation is at most one, regardless of the branch of k.
    divisible_records = []
    for w, p, a, s in [(4, 29, 2, 13), (5, 43, 2, 16), (7, 59, 2, 22), (7, 59, 3, 23)]:
        q, n = p**a, w * p**a + 2
        A = n * (n - 1) * (n - 2) // 6
        r = q * s
        assert 3 * n < r and 3 * r < 10 * n
        value = vbin(A, r, p)
        assert value == vbin(A // q, s, p) <= 1 < a
        assert vp(r * r, p) >= 2 * a and vp((A - r) ** 2, p) >= 2 * a
        divisible_records.append({"w": w, "p": p, "a": a, "s": s, "v_p_L": value})

    # Compute full integer binomials for modest representative inputs
    # and check the normalized residue, independently of its proof.
    unit_records = []
    for w, p, a in [(1, 7, 2), (1, 7, 3), (2, 13, 2), (3, 19, 2), (6, 37, 1), (9, 59, 1)]:
        q, n = p**a, w * p**a + 2
        X = comb(n * n, 6 * n - 9)
        B = comb(6 * w, 2 * w)
        assert vp(X, p) == a
        actual = (X // q) % p
        expected = (-2 * w * pow(B, -1, p)) % p
        assert actual == expected
        unit_records.append({"w": w, "p": p, "a": a, "normalized_X_mod_p": actual})

    report = {
        "status": "PASS",
        "scope": "Uniform written proof for ell=1,j=i-3,n=w*p^a+2,p>6w; finite checks corroborate identities only.",
        "constant_polynomial_at_1083": polynomial,
        "valuation_examples": valuation_records,
        "q_divides_r_examples": divisible_records,
        "normalized_residue_examples": unit_records,
        "total_identity_examples": len(valuation_records) + len(divisible_records) + len(unit_records),
        "not_a_finite_exclusion_scan": True,
        "not_lean_formalized": True,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "identity_examples": report["total_identity_examples"], "constant_polynomial_at_1083": polynomial}, indent=2))


if __name__ == "__main__":
    main()
