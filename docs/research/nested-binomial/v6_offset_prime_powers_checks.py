#!/usr/bin/env python3
"""Compact exact checks for v6_offset_prime_powers_wieferich.md.

The universal assertions are proved in the companion note. This checks
four explicit divisor exclusions, sample lifting identities, and the
four explicit Wieferich primes used in the strengthened necessary
condition. It does not search for all Wieferich primes or all solutions.
Only the Python standard library is used.
"""

from fractions import Fraction as Q
from math import gcd, isqrt, prod
from pathlib import Path
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factor(n):
    out = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            out[divisor] = out.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def valuation(n, p):
    assert n > 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def order(base, p):
    assert prime(p) and base % p
    answer = p - 1
    for divisor in factor(p - 1):
        while answer % divisor == 0 and pow(base, answer // divisor, p) == 1:
            answer //= divisor
    assert pow(base, answer, p) == 1
    for divisor in factor(answer):
        assert pow(base, answer // divisor, p) != 1
    return answer


def primitive_multiplicity(base, p, f):
    assert pow(base, f, p) == 1
    e = 1
    while pow(base, f, p ** (e + 1)) == 1:
        e += 1
    return e


def cube_divisor(n):
    return prod(p ** ((e + 2) // 3) for p, e in factor(n).items())


def divisor_exclusions():
    expected = {
        (2, 9): (511, 511, 8176),
        (2, 12): (1365, 1365, 43680),
        (5, 5): (1562, 1562, 39050),
        (5, 8): (65104, 16276, 2034500),
    }
    rows = []
    for (base, a), (expected_D, expected_c, expected_divisor) in expected.items():
        n = base ** a
        D = (n - 1) // gcd(n - 1, 6)
        fD = factor(D)
        assert prod(p ** e for p, e in fD.items()) == D
        assert all(prime(p) for p in fD)
        c = cube_divisor(D)
        d = a // 3 + 1 if base == 2 else (a + 1) // 3
        assert gcd(base, c) == 1
        necessary_divisor = base ** d * c
        assert (D, c, necessary_divisor) == (expected_D, expected_c, expected_divisor)
        margin = 3 * necessary_divisor - 10 * n
        assert margin > 0
        rows.append({
            "base": base, "a": a, "n": n,
            "D": D, "factorization_D": fD,
            "c3_D": c, "forced_valuation_r": d,
            "necessary_divisor_r": necessary_divisor,
            "three_times_divisor_minus_ten_n": margin,
        })
    return rows


def lifting_example(base, a):
    n = base ** a
    factors = factor(n - 1)
    assert prod(p ** e for p, e in factors.items()) == n - 1
    assert all(prime(p) for p in factors)
    radical = prod(factors)
    W = 1
    rows = []
    for q, actual in factors.items():
        if q == 2:
            continue
        f = order(base, q)
        assert a % f == 0 and (q - 1) % f == 0
        e = primitive_multiplicity(base, q, f)
        assert actual == e + valuation(a, q)
        assert pow(base, q - 1, q ** e) == 1
        assert pow(base, q - 1, q ** (e + 1)) != 1
        W *= q ** (e - 1)
        rows.append({
            "q": q, "order": f, "primitive_multiplicity_e": e,
            "actual_vq_n_minus_one": actual,
            "predicted_vq_n_minus_one": e + valuation(a, q),
        })
    excess = (n - 1) // radical
    if base == 2:
        multiple = a * W
    elif base == 5:
        assert factors[2] == 2 + valuation(a, 2)
        multiple = 2 * a * W
    else:
        C = 2 ** (valuation(base * base - 1, 2) - 2)
        multiple = C * a * W
    assert multiple % excess == 0
    return {
        "base": base, "a": a, "n_minus_one_factorization": factors,
        "repetition_excess": excess, "W": W,
        "proved_multiple_of_excess": multiple,
        "divisibility_verified": True,
        "odd_prime_lifting_checks": rows,
    }


def wieferich_examples():
    expected = [
        (2, 1093, 364),
        (2, 3511, 1755),
        (5, 20771, 10385),
        (5, 40487, 40486),
    ]
    rows = []
    for base, q, f in expected:
        assert prime(q) and order(base, q) == f
        order_tests = {
            divisor: pow(base, f // divisor, q)
            for divisor in factor(f)
        }
        assert all(residue != 1 for residue in order_tests.values())
        q2_residue = pow(base, f, q * q)
        q3_residue = pow(base, f, q ** 3)
        assert q2_residue == 1 and q3_residue != 1
        assert pow(base, q - 1, q * q) == 1
        rows.append({
            "base": base, "q": q, "prime_verified": True,
            "order": f, "order_factorization": factor(f),
            "proper_order_test_residues": order_tests,
            "b_to_order_mod_q2": q2_residue,
            "b_to_order_mod_q3": q3_residue,
            "primitive_multiplicity": 2,
        })
    return rows


def constants():
    base2_start = Q(2 ** 6, 50) * (1 - Q(1, 2 ** 15))
    base5_start = Q(5 ** 4, 20 * 11) * (1 - Q(1, 5 ** 11))
    base2_set_product = 1093 * 3511
    base5_set_product = 20771 * 40487
    margin2 = 2 ** 33 - 640 * base2_set_product
    margin5 = 5 ** 20 - 40 * 59 * base5_set_product
    assert base2_start > 1 and base5_start > 1
    assert margin2 > 0 and margin5 > 0
    assert 364 // gcd(364, 3) == 364
    assert 1755 // gcd(1755, 3) == 585
    return {
        "base2_lower_bound_at_h5": str(base2_start),
        "base5_weaker_lower_bound_at_a11": str(base5_start),
        "base2_explicit_set_product": base2_set_product,
        "base5_explicit_set_product": base5_set_product,
        "base2_set_exclusion_integer_margin": margin2,
        "base5_set_exclusion_integer_margin": margin5,
    }


def main():
    report = {
        "status": "pass",
        "scope": "Exact checks of proved formulas and four explicitly required small exponents; no unbounded search is claimed.",
        "original_equation_globally_solved": False,
        "new_results_formalized_in_Lean": False,
        "abc_conjecture_used": False,
        "explicit_divisor_exclusions": divisor_exclusions(),
        "exact_lifting_examples": [
            lifting_example(base, a)
            for base, a in (
                (2, 6), (2, 9), (2, 12), (2, 15), (2, 18),
                (5, 5), (5, 8), (5, 11),
                (7, 3), (7, 6), (11, 3), (11, 6),
            )
        ],
        "explicit_wieferich_prime_checks": wieferich_examples(),
        "constant_checks": constants(),
    }
    destination = Path(__file__).with_name("v6_offset_prime_powers_verification.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"],
        "divisor_exclusions": len(report["explicit_divisor_exclusions"]),
        "lifting_examples": len(report["exact_lifting_examples"]),
        "wieferich_prime_checks": len(report["explicit_wieferich_prime_checks"]),
        "constant_checks": report["constant_checks"],
        "report": str(destination),
    }, indent=2))


if __name__ == "__main__":
    main()
