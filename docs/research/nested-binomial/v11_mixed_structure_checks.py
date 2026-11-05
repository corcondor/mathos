#!/usr/bin/env python3
"""Exact checks for the new n-3 obstruction in v11.

The uniform statements are proved in v11_mixed_structure.md. These checks
reproduce its finite divisor cases and corroborate its local lemmas on
specified examples. They do not assert that a finite search solves the
original equation. Only the Python standard library is required.
"""

from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, prod
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent


def valuation(n, p):
    assert n > 0 and p >= 2
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def factor(n):
    assert n >= 1
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


def cube_completion(n):
    return prod(p ** ((e + 2) // 3) for p, e in factor(n))


def binomial_mod_prime(N, K, p):
    """Independent digit computation using Lucas's binomial congruence."""
    assert 0 <= K <= N
    result = 1
    while N or K:
        ni, ki = N % p, K % p
        if ki > ni:
            return 0
        result = result * comb(ni, ki) % p
        N //= p
        K //= p
    return result


def largest_power_exponent_at_most(n, p):
    assert n >= 1
    e = 0
    power = 1
    while power * p <= n:
        power *= p
        e += 1
    return e


def check_identities():
    factorization_count = 0
    for n in range(4, 501):
        A = comb(n, 3)
        assert 6 * (A - 1) == (n - 3) * (n * n + 2)
        g, d = gcd(n, 3), gcd(n - 1, 6)
        assert g * d <= 6
        assert gcd(n // g, (n - 1) // d) == 1
        factorization_count += 1

    pair_identity_count = 0
    for A in range(3, 101):
        for r in range(2, A + 1):
            assert r * (r - 1) * comb(A, r) == (
                A * (A - 1) * comb(A - 2, r - 2)
            )
            pair_identity_count += 1

    linear_identity_count = 0
    for w in range(1, 49):
        for q in [7, 11, 49, 121, 343]:
            n = w * q + 3
            for m in range(3 * w + 1, (10 * w) // 3 + 1):
                for delta in [0, 1]:
                    r = m * q + delta
                    assert w * r - m * n == w * delta - 3 * m
                    assert w * r - m * (n - 1) == w * delta - 2 * m
                    assert 0 < 3 * m - w * delta <= 10 * w
                    assert 0 < 3 * (2 * m - w * delta) <= 20 * w
                    linear_identity_count += 1

    assert 6 * (Fraction(10) * Fraction(20, 3)) ** 3 == Fraction(4000, 3) ** 2
    assert Fraction(4000, 3) < 12 ** 3
    small_q_constant_count = 0
    for w in range(1, 1001):
        assert 6 * w * w + 3 < Fraction(4000, 3) * w ** 3 + 1
        small_q_constant_count += 1
    return {
        "factorization_and_gcd_examples": factorization_count,
        "choose_pair_identity_examples": pair_identity_count,
        "linear_identity_examples": linear_identity_count,
        "exact_height_constant": "6*(10*20/3)^3=(4000/3)^2",
        "small_q_constant_examples": small_q_constant_count,
    }


def check_odd_prime_local_and_grid():
    primes = [
        p for p in range(7, 200)
        if p % 4 == 3 and factor(p) == [(p, 1)]
    ]
    tested = 0
    divisible_w = 0
    grid_checks = 0
    largest_n = 0
    for w in range(1, 49):
        for p in primes:
            assert all((z * z + 1) % p != 0 for z in range(p))
            for a in range(1, 6):
                q = p ** a
                n = w * q + 3
                if n < 104 or q <= 6 * w:
                    continue
                length = 6 * w * q + 9
                assert q > 9 and length < q * q
                largest_v = largest_power_exponent_at_most(length, p)
                correction_lower_bound = 2 * a + 2 * valuation(w, p) - largest_v
                assert correction_lower_bound >= 1
                assert binomial_mod_prime(n * n, length, p) == 1
                A = comb(n, 3)
                assert (A - 1) % q == 0

                for delta in [0, 1]:
                    # Exact integer endpoints for 3n < mq+delta < 10n/3.
                    m_min = (3 * n - delta) // q + 1
                    m_max = (10 * n - 3 * delta - 1) // (3 * q)
                    assert m_min >= 3 * w + 1
                    assert m_max <= (10 * w) // 3
                    grid_checks += 1
                if w % p == 0:
                    divisible_w += 1
                tested += 1
                largest_n = max(largest_n, n)

    # Ordinary exact binomials are a second independent check of digit residues.
    direct_parameters = [
        (1, 7, 3), (2, 11, 2), (3, 19, 2),
        (4, 31, 1), (7, 7, 2), (11, 11, 2),
    ]
    exact_records = []
    for w, p, a in direct_parameters:
        q = p ** a
        n = w * q + 3
        assert n >= 104 and q > 6 * w
        X = comb(n * n, 6 * n - 9)
        residue = X % p
        assert residue == 1 == binomial_mod_prime(n * n, 6 * n - 9, p)
        exact_records.append({"w": w, "p": p, "a": a, "n": n, "X_mod_p": residue})

    return {
        "parameter_set": {"w": [1, 48], "primes": primes, "a": [1, 5]},
        "conditions": "n>=104 and p^a>6w",
        "local_congruence_examples": tested,
        "examples_with_p_dividing_w": divisible_w,
        "coefficient_endpoint_examples": grid_checks,
        "largest_sample_n": largest_n,
        "ordinary_exact_binomial_checks": exact_records,
        "scope": "These examples corroborate the uniform proof, not an equation search.",
    }


def check_four_cofactors():
    coefficient_lists = {
        str(w): list(range(3 * w + 1, (10 * w) // 3 + 1))
        for w in range(1, 5)
    }
    assert coefficient_lists == {"1": [], "2": [], "3": [10], "4": [13]}
    assert 6 * 4 ** 2 + 3 < 104

    # w=3, delta=1: every divisor of 729 is odd, whereas q+1 is even.
    assert all((3 ** e) % 2 for e in range(7))
    w3_delta0 = []
    for b in range(4):
        Q1 = 5 ** b
        if Q1 % 3 != 2:
            continue
        q = (Q1 - 2) // 3
        n = 3 * q + 3
        rejection = "n<104" if n < 104 else "q+1 does not divide 1000"
        assert n < 104 or 1000 % (q + 1) != 0
        w3_delta0.append({"b": b, "Q1": Q1, "q": q, "n": n, "rejection": rejection})
    assert [record["q"] for record in w3_delta0] == [1, 41]

    # w=4, delta=0: the 3-free divisors of 39^3 are all 1 modulo 4.
    assert all(pow(13, b, 4) == 1 for b in range(4))

    d2_residues = [(1 + 2 * 11 ** e) % 7 for e in range(4)]
    assert d2_residues == [3, 2, 5, 3]
    d6_exponents = [e for e in range(4) if (1 + 6 * 11 ** e) % 7 == 0]
    assert d6_exponents == [0, 3]
    d6_values = [1 + 6 * 11 ** e for e in d6_exponents]
    assert d6_values == [7, 7987]
    assert d6_values[0] < 104
    assert d6_values[1] % 5 == 2 and d6_values[1] > 7 ** 3

    # Independent exhaustive reproduction of the finite divisor lattice in (24).
    w4_divisor_records = []
    for b in range(4):
        for c in range(4):
            n = 5 ** b * 7 ** c
            if n < 104 or n % 8 != 7 or n % 3 == 0:
                continue
            q = (n - 3) // 4
            r = 13 * q + 1
            Q1 = (n - 1) // gcd(n - 1, 6)
            assert pow(r, 3, Q1) != 0
            assert 22 ** 3 % Q1 != 0
            w4_divisor_records.append({
                "b": b, "c": c, "n": n, "q": q, "r": r,
                "Q1": Q1, "r_cubed_mod_Q1": pow(r, 3, Q1),
                "22_cubed_mod_Q1": 22 ** 3 % Q1,
            })
    assert sorted(record["n"] for record in w4_divisor_records) == [175, 343, 8575]
    return {
        "coefficient_lists": coefficient_lists,
        "w3_delta0_derived_cases": w3_delta0,
        "w4_delta1_d2_residues_mod7": d2_residues,
        "w4_delta1_d6_derived_values": d6_values,
        "w4_independent_divisor_lattice": w4_divisor_records,
        "surviving_cases": 0,
    }


def check_exceptional_bases():
    local_records = []
    for p, exponents, loss in [(2, range(7, 13), 2), (3, range(5, 9), 1)]:
        for a in exponents:
            q = p ** a
            n = q + 3
            A = comb(n, 3)
            modulus = p ** (a - loss)
            X = comb(n * n, 6 * n - 9)
            assert X % modulus == 1
            assert valuation(A - 1, p) == a - 1
            assert A % p != 0
            if p == 3:
                assert all((X + k * k) % 3 != 0 for k in range(3))
                assert 6 * q + 9 < 9 * q
                M, first_m = q // 3, 10
                assert Fraction(10 * q, 3) - Fraction(25 * (q + 3), 8) == Fraction(5 * q - 225, 24)
                if a >= 7:
                    assert n >= 1024 and 5 * q > 225
            else:
                assert all(valuation(X + k * k, 2) <= 1 for k in range(4))
                assert 6 * q + 9 < 8 * q
                M, first_m = q // 4, 13
                assert Fraction(13 * q, 4) - Fraction(25 * (q + 3), 8) == Fraction(q - 75, 8)
                if a >= 10:
                    assert n >= 1024 and q > 75

            # The previous 0/1 residue classes lie below the strict lower gap.
            assert (first_m - 1) * M + 1 <= 3 * n
            assert first_m * M > 3 * n
            local_records.append({
                "p": p, "a": a, "n": n,
                "modulus": modulus, "X_residue": X % modulus,
                "valuation_A_minus_1": valuation(A - 1, p),
                "first_allowed_r": first_m * M,
            })

    n = 246
    Q0 = n // gcd(n, 3)
    assert Q0 == 82 and all(e == 1 for _, e in factor(Q0))
    assert 3 * n == 9 * Q0 and 10 * n == 3 * 10 * Q0
    n = 732
    Q0 = n // gcd(n, 3)
    Q1 = (n - 1) // gcd(n - 1, 6)
    assert (Q0, Q1) == (244, 731)
    required_divisor = cube_completion(Q0 * Q1)
    assert required_divisor == 89182 and 3 * required_divisor > 10 * n

    two_boundary_records = []
    for a in [7, 8, 9]:
        n = 2 ** a + 3
        factors = factor(n)
        assert gcd(n, 3) == 1
        assert all(e == 1 for _, e in factors)
        assert cube_completion(n) == n
        two_boundary_records.append({"a": a, "n": n, "factorization": factors})
    assert [record["n"] for record in two_boundary_records] == [131, 259, 515]

    return {
        "ordinary_exact_binomial_and_local_checks": local_records,
        "base3_boundary": [
            {"a": 5, "n": 246, "Q0": 82, "open_gap": [738, 820]},
            {"a": 6, "n": 732, "Q0": 244, "Q1": 731,
             "required_divisor_of_r": 89182, "strict_upper_r": 2440},
        ],
        "base2_boundary": two_boundary_records,
        "small_exponents": "p=3,a<=4 and p=2,a<=6 are covered by prior j<=100 exclusion",
        "surviving_boundary_cases": 0,
    }


def check_exceptional_cofactor_extensions():
    slope37_records = []
    for c in [1, 2, 3]:
        Q1 = 31 ** c
        assert (Q1 - 1) % 6 == 0
        M = (Q1 - 1) // 6
        Q0 = 4 * M + 1
        assert 3 * Q0 - 2 * Q1 == 1
        assert 33 ** 3 % Q0 != 0
        slope37_records.append({
            "c": c, "M": M, "Q0": Q0, "Q1": Q1,
            "33_cubed_mod_Q0": 33 ** 3 % Q0,
        })
    assert [row["M"] for row in slope37_records] == [5, 160, 4965]
    assert [row["33_cubed_mod_Q0"] for row in slope37_records] == [6, 41, 16076]

    local_records = []
    for p, w, exponents in [
        (3, 2, range(4, 8)),
        (2, 3, range(6, 11)),
        (3, 4, range(3, 8)),
    ]:
        for a in exponents:
            q = p ** a
            n = w * q + 3
            A = comb(n, 3)
            length = 6 * w * q + 9
            X = comb(n * n, length)
            assert valuation(A - 1, p) == a - 1
            if p == 2:
                assert length < 32 * q
                modulus = 2 ** (a - 4)
                assert X % modulus == 1 and modulus >= 4
                assert all(valuation(X + k * k, 2) <= 1 for k in range(4))
                M = q // 4
                if a >= 9:
                    assert n >= 1024 and M >= 128
                    assert n == 12 * M + 3
                    assert Fraction(25 * n, 8) < 38 * M
            else:
                assert length < 27 * q
                modulus = 3 ** (a - 2)
                assert X % modulus == 1
                assert all((X + k * k) % 3 != 0 for k in range(3))
                M = q // 3
                if w == 2:
                    assert 18 * M + 1 <= 3 * n < 19 * M
                    assert Fraction(19 * q, 3) - Fraction(25 * n, 8) == Fraction(2 * q - 225, 24)
                    if a >= 6:
                        assert n >= 1024 and 2 * q > 225
                elif a >= 6:
                    assert n >= 1024 and M >= 243
                    assert n == 12 * M + 3
                    assert Fraction(25 * n, 8) < 38 * M
            local_records.append({
                "p": p, "w": w, "a": a, "n": n,
                "modulus": modulus, "X_residue": X % modulus,
                "valuation_A_minus_1": valuation(A - 1, p), "M": M,
            })

    squarefree_boundary_records = []
    for n in [165, 489, 195, 387, 771, 111, 327]:
        Q0 = n // gcd(n, 3)
        assert n == 3 * Q0
        assert all(e == 1 for _, e in factor(Q0))
        assert cube_completion(Q0) == Q0
        squarefree_boundary_records.append({"n": n, "Q0": Q0, "Q0_factorization": factor(Q0)})
    n = 975
    Q0 = n // gcd(n, 3)
    Q1 = (n - 1) // gcd(n - 1, 6)
    assert (Q0, Q1) == (325, 487)
    assert factor(Q1) == [(487, 1)]
    required = cube_completion(Q0 * Q1)
    assert required == 31655 and 3 * required > 10 * n
    return {
        "coefficient37_delta0": "Coprime Q0,Q1>1 cannot both divide 37^3",
        "coefficient37_delta1_complete_cases": slope37_records,
        "local_congruence_examples": local_records,
        "squarefree_boundary_cases": squarefree_boundary_records,
        "last_boundary": {
            "n": n, "Q0": Q0, "Q1": Q1,
            "required_divisor_of_r": required, "strict_upper_r": 3250,
        },
        "absorbed_into_pure_powers": ["2*2^a=2^(a+1)", "4*2^a=2^(a+2)", "3*3^a=3^(a+1)"],
        "surviving_cases": 0,
    }


def main():
    result = {
        "status": "PASS",
        "scope": "ell=1,j=i-3; both k branches; original squared-index equation",
        "methods": "Exact integer arithmetic, rational constants, direct binomials, and independent digit residues",
        "identities_and_constants": check_identities(),
        "odd_prime_local_and_grid": check_odd_prime_local_and_grid(),
        "complete_four_cofactor_cases": check_four_cofactors(),
        "exceptional_bases": check_exceptional_bases(),
        "exceptional_cofactor_extensions": check_exceptional_cofactor_extensions(),
        "formalization": "No Lean execution is claimed by this checker.",
        "limits": "Samples do not replace the uniform written proofs or solve the remaining equation.",
    }
    result["source_sha256"] = {
        name: sha256((ROOT / name).read_bytes()).hexdigest()
        for name in ["v11_mixed_structure.md", "v11_mixed_structure_checks.py"]
    }
    output = ROOT / "v11_mixed_structure_verification.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "local_congruence_examples": result["odd_prime_local_and_grid"]["local_congruence_examples"],
        "p_dividing_w_examples": result["odd_prime_local_and_grid"]["examples_with_p_dividing_w"],
        "coefficient_endpoint_examples": result["odd_prime_local_and_grid"]["coefficient_endpoint_examples"],
        "finite_divisor_cases_surviving": result["complete_four_cofactor_cases"]["surviving_cases"],
        "exceptional_boundary_cases_surviving": result["exceptional_bases"]["surviving_boundary_cases"],
        "output": output.name,
        "source_sha256": result["source_sha256"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
