#!/usr/bin/env python3
"""Proof-derived finite certificates for i=2*P^a+2, ell=1, j=i-3.

The generator factors 6561*t +/- 728.  The verifier independently sieves
all primes through the proved bound.  All row checks use neighboring
integer cubes, without floating point or a cube-root routine in the verifier.
The uniform reductions are proved in v9_cofactor_two.md.
"""

from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, isqrt, prod
from pathlib import Path
import json


INDEX_LIMIT = 1 << 192
PRIME_LIMIT = 6561 * 224 + 728


def factor_distinct(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append(n)
    return out


def is_prime_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def floor_cube_root(n):
    """Generator only: binary search with exact integer arithmetic."""
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid
    return hi if hi ** 3 == n else lo


def value(p, a, t):
    n = 2 * p ** a + 2
    assert n * (n - 1) % 3 == 0
    return t * (n * (n - 1) // 3)


def generate_cases():
    keys = set()
    for t in range(163, 225):
        factors = set(factor_distinct(6561 * t - 728))
        factors.update(factor_distinct(6561 * t + 728))
        for p in factors:
            if p < 5 or p in (7, 13):
                continue
            a = 6 if p in (5, 11) else 3
            while 2 * p ** a + 2 < INDEX_LIMIT:
                keys.add((p, a, t))
                a += 3
    for p, first_a, ts in [(7, 5, range(24, 33)), (13, 2, range(13, 18))]:
        a = first_a
        while 2 * p ** a + 2 < INDEX_LIMIT:
            keys.update((p, a, t) for t in ts)
            a += 3
    rows = []
    for p, a, t in sorted(keys):
        V = value(p, a, t)
        m = floor_cube_root(V)
        assert m ** 3 < V < (m + 1) ** 3
        rows.append({"prime": p, "exponent": a, "quotient": t,
                     "lower_cube_root": str(m)})
    return rows


def sieve_primes(limit):
    """Independent complete prime list used only by the verifier."""
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start::p] = b"\x00" * ((limit - start) // p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def verify_cases(rows):
    expected = set()
    pairs = set()
    for p in sieve_primes(PRIME_LIMIT):
        if p < 5 or p in (7, 13):
            continue
        ts = [t for t in range(163, 225)
              if (6561 * t - 728) % p == 0 or (6561 * t + 728) % p == 0]
        pairs.update((p, t) for t in ts)
        if not ts:
            continue
        first_a = 6 if p in (5, 11) else 3
        for a in range(first_a, 192, 3):
            if 2 * p ** a + 2 >= INDEX_LIMIT:
                break
            expected.update((p, a, t) for t in ts)
    for p, first_a, ts in [(7, 5, range(24, 33)), (13, 2, range(13, 18))]:
        for a in range(first_a, 192, 3):
            if 2 * p ** a + 2 >= INDEX_LIMIT:
                break
            expected.update((p, a, t) for t in ts)

    actual = [(r["prime"], r["exponent"], r["quotient"]) for r in rows]
    assert len(actual) == len(set(actual)), "duplicate certificate rows"
    assert set(actual) == expected, "missing or extraneous certificate rows"
    counts = {"ordinary_bases": 0, "base_7": 0, "base_13": 0}
    for row in rows:
        p, a, t = row["prime"], row["exponent"], row["quotient"]
        m_text = row["lower_cube_root"]
        assert isinstance(m_text, str) and m_text.isdecimal()
        m = int(m_text)
        V = value(p, a, t)
        # No cube-root algorithm or floating point is used by this verifier.
        assert m ** 3 < V < (m + 1) ** 3
        counts["base_7" if p == 7 else "base_13" if p == 13 else "ordinary_bases"] += 1

    ordinary_primes = {p for p, t in pairs}
    all_prime_exponents = {(p, a) for p, a, t in expected}
    assert counts == {"ordinary_bases": 2309, "base_7": 198, "base_13": 85}
    assert len(rows) == 2592 and len(all_prime_exponents) == 1018
    assert len(pairs) == 241 and len(ordinary_primes) == 163
    assert max(ordinary_primes) == 1436131
    return {
        "counts": counts, "total_cases": len(rows),
        "prime_exponent_pairs": len(all_prime_exponents),
        "ordinary_prime_quotient_pairs": len(pairs),
        "ordinary_prime_bases": len(ordinary_primes),
        "largest_candidate_prime": max(ordinary_primes),
        "special_exponents": {str(p): sorted({a for P, a, t in expected if P == p})
                              for p in (5, 7, 11, 13)},
        "zero_cubes": True,
        "domain_reconstruction": "independent complete prime sieve and direct congruence tests",
        "row_verification": "strict inequalities m^3 < t*(2*p^a+2)*(2*p^a+1)/3 < (m+1)^3",
    }


def vp_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_binomial(n, k, p):
    return vp_factorial(n, p) - vp_factorial(k, p) - vp_factorial(n - k, p)


def unit_factorial_mod_p(n, p):
    """Wilson-block recursion for n! after removing its entire p-power."""
    partial = [1] * p
    for t in range(1, p):
        partial[t] = partial[t - 1] * t % p
    out = 1
    while n:
        if (n // p) % 2:
            out = -out
        out = out * partial[n % p] % p
        n //= p
    return out


def unit_binomial_mod_p(n, k, p):
    den = unit_factorial_mod_p(k, p) * unit_factorial_mod_p(n - k, p) % p
    return unit_factorial_mod_p(n, p) * pow(den, -1, p) % p


def structural_checks():
    # All exceptional small-index factorizations in the written proof.
    squarefree = [
        (3, 4, [163]), (3, 5, [487]), (3, 6, [1459]),
        (3, 8, [11, 1193]), (3, 10, [17, 6947]),
        (3, 12, [353, 3011]), (5, 3, [251]), (11, 3, [2663]),
    ]
    small_rows = []
    for p, a, factors in squarefree:
        n = 2 * p ** a + 2
        assert n - 1 == prod(factors)
        assert len(factors) == len(set(factors))
        assert all(is_prime_trial(q) for q in factors)
        small_rows.append({"prime": p, "exponent": a, "index": n,
                           "index_minus_one_prime_factors": factors})
    n = 2 * 11 ** 2 + 2
    Q = n * (n - 1) // 3
    assert n == 244 and Q == 2 ** 2 * 3 ** 4 * 61
    c = 2 * 3 ** 2 * 61
    assert c == 1098 and 3 * c > 10 * n and is_prime_trial(61)
    assert all(2 * 3 ** a + 2 <= 103 for a in (1, 2, 3))
    assert 2 * 5 ** 2 + 2 <= 103 and 2 * 7 ** 2 + 2 <= 103

    # Exact constants, quotient intervals, and base-three exponent endpoint.
    h = Fraction(162) * Fraction(513, 512) ** 3 * (1 + Fraction(1, 1 << 18))
    assert h < 163
    assert Fraction(2000, 9) * Fraction(81, 80) == 225
    assert Fraction(2000, 27) * Fraction(81, 80) == 75 < 3 ** 4
    assert Fraction(75, 4) * (1 + Fraction(1, 3 ** 6)) < 19
    assert Fraction(65, 24) + Fraction(1, 100) < Fraction(11, 4)
    assert Fraction(11, 4) ** 2 < 8 and 2 ** 128 - 2 > 2 ** 20
    for K, first, last in [(1, 163, 224), (7, 24, 32), (13, 13, 17)]:
        assert [t for t in range(1, 226) if 162 < K * t < 225] == list(range(first, last + 1))
    B = prod(Fraction(2, 3) - m for m in range(1, 7)) / 720
    assert B == Fraction(728, 6561)
    assert Fraction(2, 3) * B == Fraction(1456, 27 ** 3)

    # Exact Legendre and factorial-unit checks corroborate the uniform proofs.
    valuations = []
    for p, a in [(5, 3), (5, 6), (5, 9), (7, 3), (7, 5),
                 (7, 8), (11, 2), (11, 3), (11, 6),
                 (13, 2), (13, 5), (17, 3), (19, 3), (23, 3)]:
        q = p ** a
        n = 2 * q + 2
        A = n * (n - 1) * (n - 2) // 6
        T = A // q
        beta = a - 1 if p in (5, 11) else a
        delta = 1 if p in (7, 13) else 0
        assert vp_binomial(n ** 2, 6 * n - 9, p) == beta
        assert vp_binomial(T - 1, 6, p) == delta
        for d in sorted({1, a - 1}):
            u = p ** d
            if u <= 6:
                u *= 2
            r = 6 * q + u
            assert r // q == 6 and gcd(r // p ** d, p) == 1
            assert vp_binomial(A, r, p) == a - d + delta
            if delta == 0:
                v = r // p ** d
                sign = -1 if (r - 7) % 2 else 1
                expected = sign * T * pow(v, -1, p) * 728 * pow(6561, -1, p) % p
                assert unit_binomial_mod_p(A, r, p) == expected
            valuations.append({"prime": p, "exponent": a, "r_valuation": d,
                               "outer_valuation": a - d + delta,
                               "squared_index_valuation": beta})
    base_three = []
    for a in (6, 7, 8, 9, 10, 12, 14):
        q = 3 ** a
        n = 2 * q + 2
        rho = q // 3
        A = n * (n - 1) * (n - 2) // 6
        T = A // rho
        assert vp_binomial(T - 1, 18, 3) == a - 1
        assert vp_binomial(n ** 2, 6 * n - 9, 3) == a - 2
        for d in sorted({2, a - 2}):
            r = 18 * rho + 3 ** d
            assert r // rho == 18
            assert vp_binomial(A, r, 3) == 2 * (a - 1) - d
            base_three.append({"exponent": a, "r_valuation": d,
                               "outer_valuation": 2 * (a - 1) - d})
    return {
        "small_squarefree_exclusions": small_rows,
        "exceptional_index_244_forced_divisor": c,
        "large_prime_identity_examples": valuations,
        "base_three_identity_examples": base_three,
        "height_bound_rational_numerator": h.numerator,
        "height_bound_rational_denominator": h.denominator,
        "height_bound_integer_margin": 163 * h.denominator - h.numerator,
    }


def main():
    source = Path(__file__).resolve()
    certificates_path = source.with_name("v9_cofactor_two_certificates.json")
    report_path = source.with_name("v9_cofactor_two_verification.json")
    certificate = {
        "format": "cofactor-two-neighbor-cubes-v1",
        "original_equation": "choose(choose(i,j),choose(k,ell)) = choose(i^2,j^2)+choose(k^2,ell^2)",
        "index_limit_exclusive": str(INDEX_LIMIT),
        "prime_bound_inclusive": PRIME_LIMIT,
        "value_definition": "quotient * (2*prime^exponent+2) * (2*prime^exponent+1) / 3",
        "required_strict_inequalities": "lower_cube_root^3 < value < (lower_cube_root+1)^3",
        "large_integer_encoding": "lower_cube_root and index_limit_exclusive are decimal strings",
        "cases": generate_cases(),
    }
    certificates_path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    serialized = json.loads(certificates_path.read_text())
    result = verify_cases(serialized["cases"])
    result.update(structural_checks())
    result.update({
        "status": "PASS",
        "theorem_scope": "complete exclusion of ell=1,j=i-3,i=2*P^a+2 for every prime P and a>=1, both outer branches",
        "arbitrary_search_cutoff": False,
        "r_interval_enumeration": False,
        "probabilistic_primality_tests": False,
        "new_python_proof_of_analytic_input": False,
        "new_lean_formalization_by_this_script": False,
        "whole_original_equation_solved": False,
        "checker_sha256": sha256(source.read_bytes()).hexdigest(),
        "certificate_sha256": sha256(certificates_path.read_bytes()).hexdigest(),
    })
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "counts": result["counts"],
                      "total_cases": result["total_cases"],
                      "certificate": str(certificates_path), "report": str(report_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
