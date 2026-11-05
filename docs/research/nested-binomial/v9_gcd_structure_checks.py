#!/usr/bin/env python3
"""Exact identity checks for v9_gcd_structure.md; no original-equation scan."""

from __future__ import annotations

from collections import Counter
from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import json


def is_prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def vp(n: int, p: int) -> int:
    assert n > 0
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def factorial_vp(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def binomial_vp(n: int, k: int, p: int) -> int:
    return factorial_vp(n, p) - factorial_vp(k, p) - factorial_vp(n-k, p)


def carry_vp(n: int, k: int, p: int) -> int:
    """Kummer count, independently of factorial valuations."""
    assert 0 <= k <= n
    left, right = k, n-k
    carry = total = 0
    while left or right or carry:
        digit_sum = left % p + right % p + carry
        carry = digit_sum // p
        total += carry
        left //= p
        right //= p
    return total


def run_checks() -> dict:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert all(is_prime(p) for p in primes)
    valuation_cases = 0
    gcd_cases = 0
    by_prime = Counter()
    large_b_cases = 0
    boundary_cases = 0
    sample_gcd_records = []

    for w in range(1, 31):
        B = comb(6*w, 2*w)
        D = B // gcd(B, 6)
        c_w = w // gcd(w, 6)
        for p in primes:
            if w % p == 0:
                continue
            b = vp(B, p)
            beta = vp(D, p)
            assert b == binomial_vp(6*w, 2*w, p)
            assert b == carry_vp(6*w, 2*w, p)
            assert beta == max(b - int(p in (2, 3)), 0)
            assert p**b <= 6*w

            power = p
            floor_log = 0
            floor_sum = 0
            while power <= 6*w:
                digit = (6*w)//power - (2*w)//power - (4*w)//power
                assert digit in (0, 1)
                floor_log += 1
                floor_sum += digit
                power *= p
            assert floor_sum == b <= floor_log

            for a in range(1, 10):
                q = p**a
                if q <= 4*w:
                    continue
                n = w*q+2
                U, V = q*w*w+4*w, 6*w
                assert n*n == q*U+4
                assert 6*n-9 == q*V+3
                assert n*n-(6*n-9) == q*(U-V)+1
                expected_x = a + int(p == 2) - b
                actual_x = carry_vp(n*n, 6*n-9, p)
                actual_a = carry_vp(n, 3, p)
                assert actual_x == expected_x
                assert actual_a == a - int(p == 3)
                assert actual_x == vp(4, p) + carry_vp(U, V, p)
                assert max(actual_a-actual_x, 0) == beta
                assert c_w*p**beta <= 6*w*c_w
                if p > 6*w:
                    assert beta == 0
                valuation_cases += 1
                by_prime[p] += 1
                large_b_cases += b > 1
                boundary_cases += q//p <= 4*w

                if n <= 2500:
                    A = comb(n, 3)
                    X = comb(n*n, 6*n-9)
                    S = A // gcd(A, X)
                    assert vp(X, p) == expected_x
                    assert vp(A, p) == actual_a
                    assert vp(S, p) == beta
                    assert ((n-2)//gcd(n-2, 6)) % S == 0
                    assert (c_w*p**beta) % S == 0
                    gcd_cases += 1
                    if len(sample_gcd_records) < 12:
                        sample_gcd_records.append({
                            "w": w, "p": p, "a": a, "n": n,
                            "S": S, "divisor_bound": c_w*p**beta,
                        })

    normalization_cases = 0
    for w in range(1, 51):
        for p in [2, 3, 5, 7, 11]:
            h = vp(w, p)
            reduced_w = w // p**h
            assert reduced_w % p
            for a in [1, 2, 5, 11]:
                assert w*p**a+2 == reduced_w*p**(a+h)+2
                assert reduced_w <= w
                assert reduced_w**2*gcd(w, 6) <= w**2*gcd(reduced_w, 6)
                normalization_cases += 1

    # Complete residue table giving the stronger divisor S|(n-2)/gcd(n-2,6).
    for n in range(6, 12):
        assert gcd(n, 3)*gcd(n-1, 6)*gcd(n-2, 6) == 6

    # Exact elementary inequality covering the small-power case.
    for m in range(1, 101):
        assert 8**m >= 1+7*m > 6*m

    return {
        "status": "PASS",
        "scope": "Exact structural tests of uniform written proofs; no search of the original equation",
        "valuation_formula_cases": valuation_cases,
        "independent_method": "Base-p carries, separate from the factorial-valuation proof",
        "full_binomial_gcd_cases": gcd_cases,
        "cases_with_vp_B_greater_than_one": large_b_cases,
        "first_power_above_4w_cases": boundary_cases,
        "valuation_cases_by_prime": dict(sorted(by_prime.items())),
        "normalization_cases": normalization_cases,
        "sample_full_gcd_records": sample_gcd_records,
        "full_gcd_test_max_n": 2500,
        "test_parameter_range": {"w": [1, 30], "a": [1, 9], "primes": primes},
        "uniform_defect_formula": "v_p(S)=v_p(C(6w,2w)/gcd(C(6w,2w),6)), if p does not divide w and p^a>4w",
        "uniform_fixed_cofactor_bound": "log(i)<768w^2/gcd(w,6) and i<2^(1152w^2/gcd(w,6)) for any solution with i=wp^a+2, ell=1, j=i-3",
        "stronger_divisor": "S divides (n-2)/gcd(n-2,6), and S divides (w/gcd(w,6))*p^v_p(D_w) in the exact-defect range",
        "all_fixed_cofactor_remainders_checked": False,
        "new_Lean_formalization": False,
        "original_equation_solved": False,
    }


if __name__ == "__main__":
    report = run_checks()
    report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = Path(__file__).with_name("v9_gcd_structure_verification.json")
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: report[k] for k in [
        "status", "valuation_formula_cases", "full_binomial_gcd_cases",
        "cases_with_vp_B_greater_than_one", "first_power_above_4w_cases",
        "normalization_cases",
    ]}))
