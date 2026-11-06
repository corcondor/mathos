#!/usr/bin/env python3
"""Exact certificates and supporting checks for repeated primes in n^2-10."""

from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def prime_factors(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        answer.append(n)
    return answer


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def valuation(n, p):
    require(n != 0, "nonzero valuation argument")
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def factorial_valuation(n, p):
    result = 0
    while n:
        n //= p
        result += n
    return result


def binomial_valuation(upper, lower, p):
    return (factorial_valuation(upper, p) - factorial_valuation(lower, p)
            - factorial_valuation(upper - lower, p))


def hensel_roots(p):
    base = [x for x in range(p) if (x * x - 10) % p == 0]
    lifts = []
    for x in base:
        t = -((x * x - 10) // p) * pow(2 * x, -1, p) % p
        lifts.append(x + p * t)
    return base, sorted(lifts)


def main():
    constants = []
    exceptional = set()
    for t in range(11):
        D = (9 + t) ** 2 - 360
        require(D != 0, "nonzero short-product constant")
        factors = prime_factors(abs(D))
        exceptional.update(p for p in factors if p >= 29)
        constants.append({"t": t, "D": D, "prime_factors": factors})
    require(exceptional == {31, 41, 71, 191, 239}, "all eleven constants retained")

    expected = {29: [], 31: [76, 885], 37: [566, 803], 41: [517, 1164],
                71: [275, 4766], 191: [5382, 31099], 239: [25535, 31586]}
    root_table = []
    residual = []
    for p, roots in expected.items():
        require(is_prime(p), "exception modulus is prime")
        base, lifts = hensel_roots(p)
        direct = [n for n in range(p * p) if (n * n - 10) % (p * p) == 0]
        require(lifts == roots == direct, "complete Hensel/direct residue set")
        upper = (p * p + 8) // 6
        remaining = [n for n in roots if 104 <= n <= upper]
        residual.extend((p, n) for n in remaining)
        root_table.append({"prime": p, "roots_mod_p": base, "roots_mod_p_squared": roots,
                           "upper_n": upper, "remaining_n": remaining,
                           "all_p_squared_residues_independently_checked": p * p})
    require(residual == [(71, 275), (191, 5382)], "all exceptional indices")

    Q275 = 275 * 274 // (gcd(275, 3) * gcd(274, 6))
    require(Q275 == 5 ** 2 * 11 * 137 == 37675, "n275 Q factorization")
    require(all(is_prime(p) for p in [5, 11, 137]), "n275 prime factors")
    require(3 * 7535 > 10 * 275, "n275 impossible interval")
    require(5382 // gcd(5382, 3) == 1794 == 2 * 3 * 13 * 23, "n5382 squarefree divisor")
    require(all(is_prime(p) for p in [2, 3, 13, 23]), "n5382 prime factors")
    require(5382 == 3 * 1794 and 10 * 1794 * 3 == 10 * 5382, "n5382 strict endpoint")
    require(Fraction(208000, 927) < 225 and 225 - Fraction(208000, 927) == Fraction(575, 927),
            "small-branch constant")
    require(21 * 104 - 369 > 0, "small-branch opposite constant")

    synthetic = 0
    loss_values = set()
    for p in [41, 43, 281]:
        for e in [2, 3, 4]:
            for b in [0, 1, 10, p - 1, p, p + 10]:
                for s in sorted({b + 1, b + 2, b + p, 2 * p + 1, p * p - 1}):
                    if not b < s < p * p:
                        continue
                    for unit in [1, 2]:
                        upper = b + unit * p ** e
                        loss = (factorial_valuation(s, p) - factorial_valuation(b, p)
                                - factorial_valuation(s - b - 1, p))
                        require(loss in [0, 1], "one-level factorial loss")
                        require(binomial_valuation(upper, s, p) == e - loss,
                                "general exact valuation transfer")
                        synthetic += 1
                        loss_values.add(loss)
    require(loss_values == {0, 1}, "both loss regimes tested")

    actual_inputs = []
    actual_cases = []
    for p in range(281, 1500):
        if not is_prime(p):
            continue
        _, roots = hensel_roots(p)
        for n in roots:
            m = 6 * n - 9
            if not (n >= 104 and p * p > m):
                continue
            e = valuation(n * n - 10, p)
            a, A = 2 * n - 5, comb(n, 3)
            require(e >= 2 and valuation(A - a, p) == e, "actual repeated-root index")
            F = (factorial_valuation(m, p) - factorial_valuation(10, p)
                 - factorial_valuation(m - 11, p))
            require(F == 0 and binomial_valuation(n * n, m, p) == e, "actual inner valuation")
            actual_inputs.append({"p": p, "n": n, "e": e, "F": F})
            low, high = 3 * n + 1, (10 * n - 1) // 3
            sample_r = {low, high, ((low + p - 1) // p) * p,
                        a + ((low - a + p - 1) // p) * p}
            for r in sorted(sample_r):
                if not low <= r <= high:
                    continue
                G = (factorial_valuation(r, p) - factorial_valuation(a, p)
                     - factorial_valuation(r - a - 1, p))
                outer_v = binomial_valuation(A, r, p)
                require(G in [0, 1] and outer_v == e - G, "actual outer valuation")
                exponents = []
                for k in [r, A - r]:
                    v = valuation(k, p)
                    require(v <= 1, "actual square valuation upper bound")
                    if G == 0:
                        require(v == 0, "G0 cannot have p dividing k")
                    if v:
                        require(G == 1, "p divides k forces factorial loss")
                    exponents.append(v)
                require(valuation(A - r, p) == valuation(r - a, p), "complement exact valuation")
                actual_cases.append({"n": n, "p": p, "r": r, "e": e, "G": G,
                                     "outer_valuation": outer_v, "inner_valuation": e,
                                     "k_valuations": exponents})
    require(actual_inputs and actual_cases, "nonempty actual-input samples")

    here = Path(__file__).resolve().parent
    report = {
        "status": "PASS",
        "theorem": "If p is prime, e=v_p(n^2-10)>=2 and p^2>6*n-9, an original solution must have k=A-r, e=3, and v_p(r-2*n+5)=1.",
        "fixed_prime_cutoff_in_final_theorem": None,
        "scope": "Complete finite exceptional-prime certificates plus supporting checks of the written uniform valuation proof.",
        "new_lean_execution": False,
        "new_deepseek_api_calls": 0,
        "new_complete_cas_calls": 0,
        "all_eleven_constants": constants,
        "factorial_loss_exceptional_primes_ge_29": sorted(exceptional),
        "complete_small_prime_root_table": root_table,
        "residual_exceptional_pairs": residual,
        "residual_exclusions": [{"n": 275, "forced_r_divisor": 7535, "reason": "exceeds strict upper interval"},
                                {"n": 5382, "forced_r_divisor": 1794, "least_multiple_above_3n": 17940,
                                 "reason": "equals excluded upper endpoint"}],
        "synthetic_valuation_identity_checks": synthetic,
        "synthetic_loss_values": sorted(loss_values),
        "actual_input_sample_prime_interval": [281, 1499],
        "actual_repeated_root_inputs_count": len(actual_inputs),
        "actual_valuation_cases_count": len(actual_cases),
        "actual_repeated_root_inputs": actual_inputs,
        "actual_valuation_case_sample": actual_cases[:32],
        "samples_are_original_solutions": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_note_sha256": hashlib.sha256((here / "v16_repeated_neighbor_primes.md").read_bytes()).hexdigest(),
    }
    (here / "v16_repeated_neighbor_primes_checks.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "constants": len(constants), "small_prime_moduli": len(root_table),
                      "exceptional_pairs_excluded": len(residual), "synthetic_valuation_checks": synthetic,
                      "actual_repeated_root_inputs": len(actual_inputs), "actual_valuation_cases": len(actual_cases)}, indent=2))


if __name__ == "__main__":
    main()
