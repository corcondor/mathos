#!/usr/bin/env python3
"""Exact supporting checks for the uniform v16 quadratic-neighbor proof."""

from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def prime_divisors(value):
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append(value)
    return result


def lucas(upper, lower, prime):
    result = 1
    while upper or lower:
        a, b = upper % prime, lower % prime
        if b > a:
            return 0
        result = result * comb(a, b) % prime
        upper //= prime
        lower //= prime
    return result


def main():
    expected = {
        0: list(range(0, 17, 2)),
        1: [1, 4, 7, 10, 13, 16],
        2: [4, 10, 16],
        3: list(range(17)),
        4: [4, 10, 16],
        5: [1, 4, 7, 10, 13, 16],
    }
    residues = {n: [c for c in range(17) if ((c + 2) * n - 3 * c) % 6 == 0]
                for n in range(6)}
    require(residues == expected, "full residue classification")
    nonsquares = {n: [c for c in cs if isqrt(c) ** 2 != c]
                  for n, cs in residues.items()}

    endpoint_constants = []
    for c in range(17):
        for t in range(0, c + 1, 2):
            D = (9 + t) ** 2 - 36 * c
            require(D % 4 == 1 and D != 0, "endpoint constant is nonzero")
            require(-495 <= D <= 81, "endpoint constant exact range")
            require(abs(D) < 6 * 104 - 25, "endpoint constant smaller than prime")
            endpoint_constants.append({"c": c, "t": t, "D": D})
    require(len(endpoint_constants) == 81, "endpoint count")

    records = []
    actual_checks = []
    identity_checks = 0
    endpoint_r_prime_controls = []
    for n in range(104, 501):
        A, m = comb(n, 3), 6 * n - 9
        for c in residues[n % 6]:
            a = ((c + 2) * n - 3 * c) // 6
            require(6 * (A - a) == (n - 3) * (n * n - c), "polynomial identity")
            require(0 < a <= 3 * n - 8, "small integer top residue")
            identity_checks += 1
            for p in prime_divisors(n * n - c):
                if 3 * n < p and 3 * p < 10 * n:
                    Q = n * (n - 1) // (gcd(n, 3) * gcd(n - 1, 6))
                    require(pow(p, 3, Q) != 0, "prime r endpoint rejected by Q")
                    endpoint_r_prime_controls.append({"n": n, "c": c, "r": p, "Q": Q})
                for r in sorted({3 * n + 1, (10 * n - 1) // 3}):
                    require(3 * n < r and 3 * r < 10 * n, "strict r sample interval")
                    if p <= r:
                        continue
                    left = lucas(A, r, p)
                    inner = lucas(n * n, m, p)
                    require(left == inner == 0, "both binomials vanish")
                    for branch, k in [("k=r", r), ("k=A-r", A - r)]:
                        square = pow(k, 2, p)
                        require(square != 0, "square remains nonzero")
                        require(left != (inner + square) % p, "original equation excluded")
                    rec = {"n": n, "c": c, "r": r, "p": p,
                           "A_mod_p": A % p, "a": a, "inner_low_digit": m % p,
                           "binomial_residues": [left, inner],
                           "square_residues": [pow(r, 2, p), pow(A - r, 2, p)]}
                    records.append(rec)
                    if len(actual_checks) < 64:
                        require(comb(A, r) % p == left, "actual outer binomial")
                        require(comb(n * n, m) % p == inner, "actual inner binomial")
                        actual_checks.append(rec)

    positive_neighbor = []
    positive_actual = []
    for n in range(105, 501, 6):
        A, m, a = comb(n, 3), 6 * n - 9, (n + 3) // 6
        require(6 * (A - a) == (n - 3) * (n * n + 1), "positive neighbor identity")
        for p in prime_divisors(n * n + 1):
            if p <= m:
                continue
            for r in sorted({3 * n + 1, (10 * n - 1) // 3}):
                left, inner = lucas(A, r, p), lucas(n * n, m, p)
                require(left == 0 and inner == p - 1, "positive neighbor binomial residues")
                require(1 < r < p - 1 and 1 < r - a < p - 1, "nontrivial square roots interval")
                for k in [r, A - r]:
                    require(pow(k, 2, p) != 1, "positive neighbor square not one")
                    require(left != (inner + pow(k, 2, p)) % p, "positive original equation exclusion")
                rec = {"n": n, "r": r, "p": p, "a": a,
                       "binomial_residues": [left, inner],
                       "square_residues": [pow(r, 2, p), pow(A - r, 2, p)]}
                positive_neighbor.append(rec)
                if len(positive_actual) < 24:
                    require(comb(A, r) % p == left and comb(n * n, m) % p == inner,
                            "positive neighbor actual binomials")
                    positive_actual.append(rec)

    require(records and positive_neighbor and endpoint_r_prime_controls, "nonempty controls")
    here = Path(__file__).resolve().parent
    report = {
        "status": "PASS",
        "scope": "Finite exact supporting checks of a written uniform proof; not a search for original-equation solutions.",
        "main_theorem": "For 0<=c<=16 with 6|((c+2)n-3c), P+(n^2-c)<r; c=10 applies to every n.",
        "positive_neighbor_theorem": "If n=3 mod 6, P+(n^2+1)<=6*n-9.",
        "new_lean_execution": False,
        "new_deepseek_api_calls": 0,
        "exact_prime_power_bound_claimed": False,
        "sample_n_range": [104, 500],
        "residue_classes": residues,
        "nonsquare_residue_classes": nonsquares,
        "endpoint_constants_count": len(endpoint_constants),
        "endpoint_constants": endpoint_constants,
        "polynomial_identity_checks": identity_checks,
        "neighbor_modular_records_count": len(records),
        "neighbor_modular_branch_exclusions_count": 2 * len(records),
        "actual_binomial_pair_checks": len(actual_checks),
        "neighbor_record_sample": records[:64],
        "positive_neighbor_records_count": len(positive_neighbor),
        "positive_neighbor_actual_binomial_pair_checks": len(positive_actual),
        "positive_neighbor_record_sample": positive_neighbor[:24],
        "prime_r_endpoint_controls_count": len(endpoint_r_prime_controls),
        "prime_r_endpoint_control_sample": endpoint_r_prime_controls[:20],
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_note_sha256": hashlib.sha256((here / "v16_quadratic_neighbors.md").read_bytes()).hexdigest(),
    }
    output = here / "v16_quadratic_neighbors_checks.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["status", "endpoint_constants_count",
        "polynomial_identity_checks", "neighbor_modular_records_count", "actual_binomial_pair_checks",
        "positive_neighbor_records_count", "positive_neighbor_actual_binomial_pair_checks",
        "prime_r_endpoint_controls_count"]}, indent=2))


if __name__ == "__main__":
    main()
