#!/usr/bin/env python3
"""Generate and independently verify the finite shifted-prime-power certificate.

The accompanying proof derives every bound in this file.  The generator
factors 81*t +/- 40; the verifier instead sieves all primes through the
proved bound and tests the congruences.  It checks strict neighboring cubes
for every case without recomputing a cube root.  Standard library only.
"""

from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json


INDEX_LIMIT = 1 << 192
PRIME_LIMIT = 81 * 224 + 40


def factor_distinct(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.append(n)
    return result


def floor_cube_root(n):
    """Exact integer binary search, used only by the generator."""
    assert n > 0
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid
    return hi if hi ** 3 == n else lo


def generate_cases():
    keys = set()
    for t in range(163, 225):
        prime_factors = set(factor_distinct(81 * t - 40))
        prime_factors.update(factor_distinct(81 * t + 40))
        for p in prime_factors:
            if p < 7:
                continue
            a = 3
            while p ** a + 2 < INDEX_LIMIT:
                keys.add((p, a, t))
                a += 3
    for p, first_a, t_values in [(2, 15, range(21, 29)), (5, 8, range(33, 45))]:
        a = first_a
        while p ** a + 2 < INDEX_LIMIT:
            for t in t_values:
                keys.add((p, a, t))
            a += 3
    cases = []
    for p, a, t in sorted(keys):
        n = p ** a + 2
        assert n * (n - 1) % 6 == 0
        value = t * (n * (n - 1) // 6)
        m = floor_cube_root(value)
        assert m ** 3 < value < (m + 1) ** 3
        cases.append({
            "prime": p,
            "exponent": a,
            "quotient": t,
            "lower_cube_root": str(m),
        })
    return cases


def sieve_primes(limit):
    """Independent complete prime list for the verifier."""
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            for multiple in range(p * p, limit + 1, p):
                flags[multiple] = 0
    return [p for p in range(2, limit + 1) if flags[p]]


def verify_cases(cases):
    # Reconstruct the complete domain without using the generator's
    # factorization function or its list of candidate prime factors.
    primes = sieve_primes(PRIME_LIMIT)
    expected = set()
    for p in primes:
        if p >= 7:
            ts = [t for t in range(163, 225)
                  if (81 * t - 40) % p == 0 or (81 * t + 40) % p == 0]
            for a in range(3, 192, 3):
                if p ** a + 2 >= INDEX_LIMIT:
                    break
                for t in ts:
                    expected.add((p, a, t))
        elif p == 2:
            for a in range(15, 192, 3):
                if p ** a + 2 < INDEX_LIMIT:
                    expected.update((p, a, t) for t in range(21, 29))
        elif p == 5:
            for a in range(8, 192, 3):
                if p ** a + 2 < INDEX_LIMIT:
                    expected.update((p, a, t) for t in range(33, 45))

    actual = [(row["prime"], row["exponent"], row["quotient"]) for row in cases]
    assert len(actual) == len(set(actual)), "duplicate certificate rows"
    assert set(actual) == expected, "certificate domain missing or extraneous cases"

    counts = {"base_2": 0, "base_5": 0, "base_at_least_7": 0}
    for row in cases:
        p, a, t = row["prime"], row["exponent"], row["quotient"]
        m_text = row["lower_cube_root"]
        assert isinstance(m_text, str) and m_text.isdecimal()
        m = int(m_text)
        n = p ** a + 2
        assert n < INDEX_LIMIT and n * (n - 1) % 6 == 0
        value = t * (n * (n - 1) // 6)
        # These are the finite certificates.  No cube-root algorithm is
        # used by the verifier, and equality on either side is rejected.
        assert m ** 3 < value
        assert value < (m + 1) ** 3
        key = "base_2" if p == 2 else "base_5" if p == 5 else "base_at_least_7"
        counts[key] += 1

    assert counts == {"base_2": 472, "base_5": 300, "base_at_least_7": 2131}
    large_pairs = {(p, t) for p, a, t in expected if p >= 7}
    large_prime_exponents = {(p, a) for p, a, t in expected if p >= 7}
    large_primes = {p for p, a, t in expected if p >= 7}
    assert len(large_pairs) == 204
    assert len(large_prime_exponents) == 840
    assert len(large_primes) == 119 and max(large_primes) == 17293
    assert len(expected) == 2903

    # Exact rational constants in the height argument.
    h = Fraction(162) * Fraction(513, 512) ** 3 * (1 + Fraction(1, 1 << 18))
    assert h < 163
    assert Fraction(2000, 9) * Fraction(81, 80) == 225
    assert Fraction(65, 24) + Fraction(1, 100) < Fraction(11, 4)
    assert Fraction(11, 4) ** 2 < 8
    assert 2 ** 128 - 2 > 2 ** 20
    for K, t_low, t_high in [(1, 163, 224), (8, 21, 28), (5, 33, 44)]:
        derived = [t for t in range(1, 226) if Fraction(162, K) < t < Fraction(225, K)]
        assert derived == list(range(t_low, t_high + 1))
        assert not any(Fraction(162, K) < t < Fraction(163, K) for t in range(1, 226))
    assert 2 ** 189 + 2 < INDEX_LIMIT <= 2 ** 192 + 2
    assert 5 ** 80 + 2 < INDEX_LIMIT <= 5 ** 83 + 2

    return {
        "counts": counts,
        "total_cases": len(expected),
        "large_prime_base_count": len(large_primes),
        "large_prime_quotient_pair_count": len(large_pairs),
        "large_prime_exponent_pair_count": len(large_prime_exponents),
        "largest_candidate_prime": max(large_primes),
        "base_2_exponents": sorted({a for p, a, t in expected if p == 2}),
        "base_5_exponents": sorted({a for p, a, t in expected if p == 5}),
        "height_bound_rational_numerator": h.numerator,
        "height_bound_rational_denominator": h.denominator,
        "height_bound_integer_margin": 163 * h.denominator - h.numerator,
        "zero_cubes": True,
        "domain_reconstruction": "independent prime sieve and congruence tests",
        "row_verification": "strict inequalities m^3 < t*(p^a+2)*(p^a+1)/6 < (m+1)^3",
    }


def main():
    source = Path(__file__).resolve()
    certificates_path = source.with_name("v8_shifted_prime_power_completion_certificates.json")
    report_path = source.with_name("v8_shifted_prime_power_completion_verification.json")
    certificate = {
        "format": "shifted-prime-power-neighbor-cubes-v1",
        "original_equation": "choose(choose(i,j),choose(k,ell)) = choose(i^2,j^2)+choose(k^2,ell^2)",
        "index_limit_exclusive": str(INDEX_LIMIT),
        "prime_bound_inclusive": PRIME_LIMIT,
        "value_definition": "quotient * (prime^exponent+2) * (prime^exponent+1) / 6",
        "required_strict_inequalities": "lower_cube_root^3 < value < (lower_cube_root+1)^3",
        "large_integer_encoding": "lower_cube_root and index_limit_exclusive are decimal strings",
        "cases": generate_cases(),
    }
    certificates_path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    # Read the serialized artifact back before independent verification.
    serialized = json.loads(certificates_path.read_text())
    result = verify_cases(serialized["cases"])
    result.update({
        "status": "PASS",
        "theorem_scope": "complete exclusion of ell=1,j=i-3,i=P^a+2 for every prime P and a>=1, together with the separate base-three proof",
        "arbitrary_search_cutoff": False,
        "r_interval_enumeration": False,
        "probabilistic_primality_tests": False,
        "new_python_proof_of_analytic_input": False,
        "new_lean_formalization_by_this_script": False,
        "checker_sha256": sha256(source.read_bytes()).hexdigest(),
        "certificate_sha256": sha256(certificates_path.read_bytes()).hexdigest(),
    })
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "counts": result["counts"],
                      "total_cases": result["total_cases"],
                      "certificate": str(certificates_path), "report": str(report_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
