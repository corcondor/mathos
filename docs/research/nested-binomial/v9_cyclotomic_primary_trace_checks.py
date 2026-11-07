#!/usr/bin/env python3
"""Exact finite-field certificates and generic identity checks for v9.

This does not search the original equation in a box. Every exponent test
uses a complete, proved multiplicative period. Uniform algebraic and
q-adic statements are proved separately in the companion note.
"""

from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, isqrt, lcm
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent


def prime_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_sieve(limit):
    ok = bytearray(b"\1") * (limit + 1)
    ok[0:2] = b"\0\0"
    for p in range(2, isqrt(limit) + 1):
        if ok[p]:
            for n in range(p * p, limit + 1, p):
                ok[n] = 0
    return [p for p in range(2, limit + 1) if ok[p]]


def prime_factors(n):
    result = []
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        result.append(n)
    return result


def primary_trace(q):
    """Generate by the positive m coordinate of 4q=B^2+27m^2."""
    found = []
    for m in range(1, isqrt(4 * q // 27) + 1):
        v = 4 * q - 27 * m * m
        b = isqrt(v)
        if b * b == v:
            if b % 3 != 2:
                b = -b
            found.append((b, m))
    assert len(found) == 1, (q, found)
    return found[0]


def verify_primary_trace(q, b, m):
    """Independently scan the signed trace coordinate, not m."""
    found = []
    bound = isqrt(4 * q)
    for candidate in range(-bound, bound + 1):
        if candidate % 3 != 2:
            continue
        v = 4 * q - candidate * candidate
        if v <= 0 or v % 27:
            continue
        mm = isqrt(v // 27)
        if 27 * mm * mm == v:
            found.append((candidate, mm))
    assert found == [(b, m)], (q, found, b, m)


def power_cycle(b, q):
    values = []
    seen = set()
    x = 1
    while x not in seen:
        seen.add(x)
        values.append(x)
        x = x * b % q
    assert x == 1
    assert (q - 1) % len(values) == 0
    return values


def exponent_allowed(a, q, branch):
    # Keep residue 1: although the actual exponent a=1 was excluded,
    # larger exponents in that same residue class cannot be discarded.
    if a % 3 == 0 or a % 4 == 0:
        return False
    if a % 2 == 0 and (q % 12 != 7 or branch != 2):
        return False
    return True


def make_row(q):
    b, m = primary_trace(q)
    cycle = power_cycle(b, q)
    d = len(cycle)
    period = lcm(d, 12)
    squares = {x * x % q for x in range(1, q)}
    roots = [r for r in range(q) if (r * r + r + 1) % q == 0]
    assert len(roots) == 2
    entries = []
    for r in roots:
        square_value = (1 - r) * pow(42, -1, q) % q
        square_ok = square_value in squares
        t1 = (2 * r + 1) * pow(r + 3, -1, q) % q
        t2 = (r + 2) * pow(r - 2, -1, q) % q
        branches = []
        for branch, target in [(2, t1), (4, t2)]:
            survivors = [a for a in range(period)
                         if square_ok and exponent_allowed(a, q, branch)
                         and cycle[a % d] == target]
            branches.append({
                "p_mod_7": branch,
                "target": target,
                "cube_character": pow(target, (q - 1) // 3, q),
                "power_log_mod_order": cycle.index(target) if target in cycle else None,
                "surviving_exponent_residues_mod_period": survivors,
            })
        entries.append({
            "p_mod_q": r,
            "j_squared_residue": square_value,
            "quadratic_character": 1 if square_ok else q - 1,
            "branches": branches,
        })
    return {
        "q": q, "primary_trace": b, "norm_m": m,
        "multiplicative_order": d, "full_exponent_period": period,
        "roots": entries,
        "all_exponents_excluded": not any(
            b["surviving_exponent_residues_mod_period"]
            for r in entries for b in r["branches"]),
    }


def verify_row(row):
    q = row["q"]
    b = row["primary_trace"]
    d = row["multiplicative_order"]
    period = row["full_exponent_period"]
    assert prime_trial(q) and q % 3 == 1
    verify_primary_trace(q, b, row["norm_m"])
    assert pow(b, d, q) == 1
    assert all(pow(b, d // t, q) != 1 for t in prime_factors(d))
    assert period % d == 0 and period % 12 == 0
    assert period == d * 12 // gcd(d, 12)
    roots = [r for r in range(q) if pow(r, 3, q) == 1 and r != 1]
    assert roots == [r["p_mod_q"] for r in row["roots"]]
    any_allowed = False
    for data in row["roots"]:
        r = data["p_mod_q"]
        square = (1 - r) * pow(42, q - 2, q) % q
        char = pow(square, (q - 1) // 2, q)
        assert square == data["j_squared_residue"]
        assert char == data["quadratic_character"]
        for branch_data in data["branches"]:
            branch = branch_data["p_mod_7"]
            if branch == 2:
                target = (2 * r + 1) * pow(r + 3, q - 2, q) % q
            else:
                assert branch == 4
                target = (r + 2) * pow(r - 2, q - 2, q) % q
            assert target == branch_data["target"]
            full_logs = [a for a in range(d) if pow(b, a, q) == target]
            assert len(full_logs) <= 1
            assert (full_logs[0] if full_logs else None) == branch_data["power_log_mod_order"]
            expected = []
            for a in range(period):
                if char != 1 or a % 3 == 0 or a % 4 == 0:
                    continue
                if a % 2 == 0 and not (q % 12 == 7 and branch == 2):
                    continue
                if pow(b, a, q) == target:
                    expected.append(a)
            assert expected == branch_data["surviving_exponent_residues_mod_period"]
            assert pow(target, (q - 1) // 3, q) == branch_data["cube_character"]
            any_allowed |= bool(expected)
    assert row["all_exponents_excluded"] == (not any_allowed)


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction())


def fraction_mod(x, modulus):
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def valuation(n, q):
    assert n != 0
    e = 0
    while n % q == 0:
        n //= q
        e += 1
    return e


def structural_checks():
    # Generic centered products. Their parameters are not asserted to
    # solve the cyclotomic equation or the original binomial equation.
    centered = []
    for q, jblock in [(13, 4), (19, 5)]:
        for s in [0, 1, 2]:
            u = q ** s
            j = jblock * u + 1
            assert j < q ** (s + 1) and j % q
            for c in [1, 2]:
                a = 2 * s + 1
                top = j * (1 + c * q ** a)
                aa = comb(top, j)
                J = j // u
                modulus = q ** (s + 2)
                predicted = 1 + c * j * q ** (s + 1) * fraction_mod(harmonic(J), modulus)
                assert aa % modulus == predicted % modulus
                assert valuation(aa - 1, q) >= s + 1
                centered.append({"q": q, "s": s, "j": j, "c": c, "J": J})

    # Direct integer binomials for the outer digit block, including
    # H divisible by q and hence a strict excess in the valuation.
    outer = []
    for q in [13, 19]:
        for s in [0, 1]:
            u = q ** (s + 1)
            for H in [1, 2, q, q + 1, q * q]:
                aa = 1 + u * H
                for p in [3, 5, q + 2, 2 * q - 1]:
                    if not (p < u and p % q and (p - 1) % q):
                        continue
                    ll = comb(aa, p)
                    assert valuation(ll, q) == valuation(aa - 1, q)
                    assert ll % u == 0
                    assert (ll // u) % q == -H * pow(p * (p - 1), -1, q) % q
                    outer.append({"q": q, "s": s, "H": H, "bottom": p,
                                  "valuation": valuation(ll, q)})

    # Generic X product compression, with direct exact binomials on both
    # sides. n is a square, q^a<n<2q^a, and q does not divide n.
    compressed = []
    for q in [13, 19]:
        for s in [0, 1]:
            a = 2 * s + 1
            D = q ** a
            js = [isqrt(D) + 1, isqrt(2 * D - 1)]
            for j in js:
                assert j % q and D < j * j < 2 * D
                n = j * j
                for c in [1, 2]:
                    divisor = q ** (s + 1)
                    M = n * c * D // divisor
                    K = n // divisor
                    xx = comb(n * (1 + c * D), n)
                    reduced = comb(M + K, K)
                    assert xx % divisor == reduced % divisor
                    assert q ** s <= K < 2 * q ** s
                    compressed.append({"q": q, "s": s, "j": j, "c": c,
                                       "original_bottom": n, "reduced_bottom": K})
    return {"centered_product_cases": centered,
            "outer_digit_cases": outer,
            "product_compression_cases": compressed}


def main():
    prefix = [q for q in range(13, 212) if q % 3 == 1 and prime_trial(q)]
    prefix_independent = [q for q in prime_sieve(211) if q >= 13 and q % 3 == 1]
    assert prefix == prefix_independent and len(prefix) == 21
    rows = [make_row(q) for q in prefix]
    for row in rows:
        verify_row(row)
    survivors = [r["q"] for r in rows if not r["all_exponents_excluded"]]
    assert survivors == [19, 31, 67]
    excluded = [r["q"] for r in rows if r["all_exponents_excluded"]]
    assert len(excluded) == 18
    old_quadratic = [r["q"] for r in rows
                     if all(x["quadratic_character"] != 1 for x in r["roots"])]
    assert old_quadratic == [13, 37, 181]
    new_excluded = sorted(set(excluded) - set(old_quadratic))
    assert len(new_excluded) == 15

    expected_survivors = {
        19: (11, 4, 12, [1, 7]),
        31: (5, 4, 60, [19, 29, 49, 59]),
        67: (37, 2, 132, [43, 65, 109, 131]),
    }
    for row in rows:
        if row["q"] not in expected_survivors:
            continue
        actual = [(r["p_mod_q"], b["p_mod_7"], row["full_exponent_period"],
                   b["surviving_exponent_residues_mod_period"])
                  for r in row["roots"] for b in r["branches"]
                  if b["surviving_exponent_residues_mod_period"]]
        assert actual == [expected_survivors[row["q"]]]

    even_bases = [q for q in range(13, 367) if q % 12 == 7 and prime_trial(q)]
    assert even_bases == [q for q in prime_sieve(366) if q >= 13 and q % 12 == 7]
    assert len(even_bases) == 17
    even_rows = [make_row(q) for q in even_bases]
    for row in even_rows:
        verify_row(row)
        assert not any(a % 2 == 0 for r in row["roots"] for b in r["branches"]
                       for a in b["surviving_exponent_residues_mod_period"])
    first_even = make_row(367)
    verify_row(first_even)
    even_survivors = [(r["p_mod_q"], b["p_mod_7"],
                       [a for a in b["surviving_exponent_residues_mod_period"] if a % 2 == 0])
                      for r in first_even["roots"] for b in r["branches"]
                      if any(a % 2 == 0 for a in b["surviving_exponent_residues_mod_period"])]
    assert even_survivors == [(83, 2, [418, 662])]

    minus_one_examples = []
    for m in [3, 7, 9]:
        q = (1 + 27 * m * m) // 4
        assert 4 * q == 1 + 27 * m * m and prime_trial(q)
        assert primary_trace(q) == (-1, m)
        row = make_row(q)
        verify_row(row)
        # This stronger assertion uses no restrictions on the exponent.
        assert all(b["target"] not in {1, q - 1}
                   for r in row["roots"] for b in r["branches"])
        minus_one_examples.append({"q": q, "m": m})

    harmonic_rows = []
    for q in [19, 31, 67]:
        for J in range(isqrt(q), isqrt(2 * q) + 1):
            h = harmonic(J)
            residue = fraction_mod(h, q)
            assert residue != 0
            harmonic_rows.append({"q": q, "J": J,
                                  "numerator": h.numerator,
                                  "denominator": h.denominator,
                                  "residue": residue})

    structural = structural_checks()
    report = {
        "status": "PASS",
        "scope": "Exact complete finite-field exponent periods and generic identity checks; no box search of the original equation",
        "primary_trace_condition": "T1 or T2 = B^a modulo q, with the branch fixed by p modulo 7",
        "all_exponent_prime_bases_checked": 21,
        "all_exponent_bases_excluded": excluded,
        "old_quadratic_exclusions_in_this_prefix": old_quadratic,
        "additional_excluded_bases_in_this_prefix": new_excluded,
        "surviving_bases_in_this_prefix": survivors,
        "all_exponent_tables": rows,
        "even_exponent_lower_bound": 367,
        "even_prime_bases_checked": 17,
        "even_exponent_tables": even_rows,
        "first_unexcluded_even_base_table": first_even,
        "trace_minus_one_unbounded_family": "4q=1+27m^2, q prime different from 7; all positive exponents excluded for prime p>3",
        "trace_minus_one_examples": minus_one_examples,
        "odd_exact_valuation_harmonic_checks": harmonic_rows,
        "structural_identity_counts": {k: len(v) for k, v in structural.items()},
        "structural_identity_examples": structural,
        "independent_domain_and_period_reconstruction": "PASS",
        "arbitrary_exponent_cutoff": False,
        "external_reciprocity_needed_for_finite_tables": False,
        "external_reciprocity_used_for_universal_cube_filter": "Milne, Class Field Theory, VIII Example 5.13, printed p249 / PDF index257",
        "prior_Thue_dependency_in_combined_exponent_tables": True,
        "new_Lean_formalization": False,
        "whole_large_prime_branch_solved": False,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_note_sha256": sha256((HERE / "v9_cyclotomic_primary_trace.md").read_bytes()).hexdigest(),
    }
    out = HERE / "v9_cyclotomic_primary_trace_verification.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["status", "all_exponent_prime_bases_checked",
        "additional_excluded_bases_in_this_prefix", "surviving_bases_in_this_prefix",
        "even_exponent_lower_bound", "even_prime_bases_checked", "structural_identity_counts"]}))


if __name__ == "__main__":
    main()
