#!/usr/bin/env python3
"""Exact supporting checks for the written v15 neighbor-prime argument.

This is not an original-equation search and does not prove the universal
claims by finite sampling. Their proofs are in neighbor_prime_obstruction.md.
"""
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prime_divisors(value):
    result = []
    p = 2
    while p * p <= value:
        if value % p == 0:
            result.append(p)
            while value % p == 0:
                value //= p
        p = 3 if p == 2 else p + 2
    if value > 1:
        result.append(value)
    return result


def main():
    here = Path(__file__).resolve().parent
    constants = {
        "complementary_height": (6 * Fraction(10829, 27)**3, 20000**2),
        "small_height": (36 * Fraction(12032, 27)**3, 240**4),
        "uniform_prime_bound": (
            20000 * Fraction(101, 100)**3 * Fraction(100, 99), 28**3),
        "small_branch_prime_bound": (
            57600 * Fraction(101, 100)**3 * Fraction(100, 99)**2, 40**3),
    }
    for name, (left, right) in constants.items():
        require(left < right, name)

    squares_mod9 = {a*a % 9 for a in range(9)}
    z_mod9 = {5*(a-1) % 9 for a in squares_mod9}
    require(squares_mod9 == {0, 1, 4, 7}, "square residues mod 9")
    require(z_mod9 == {0, 3, 4, 6}, "coefficient residues mod 9")
    require([z for z in (9, 10, 11) if z % 9 in z_mod9] == [9],
            "prime-neighbor coefficient exclusion")

    binomial_checks = []
    for n in range(104, 321):
        m = 6*n-9
        large = [p for p in prime_divisors(n*n+2) if p > m]
        if large:
            value = comb(n*n, m)
            for p in large:
                require(value % p == (8-6*n) % p,
                        f"exact binomial congruence n={n}, p={p}")
                require(comb(n, 3) % p == 1,
                        f"neighbor factorization n={n}, p={p}")
                require((6*n-8) % p != 0, "nonzero residue")
                binomial_checks.append({"n": n, "p": p})

    valuation_checks = 0
    for q in range(1, 161):
        for r in range(1, 241):
            if r**3 % q:
                continue
            for w in (1, 2, 5):
                for epsilon in (0, 1):
                    for u in (0, 1, 3):
                        c = w*r*(r-2*epsilon)+q*u
                        require(c**3 % q == 0, "ordinary cube transfer")
                        if epsilon == 0:
                            require(c**3 % (q*q) == 0,
                                    "doubled valuation transfer")
                        valuation_checks += 1

    identity_checks = 0
    for n in (104, 127, 245, 1024, 13720):
        for w in (1, 2, 17, 101):
            for z in (9*w, 10*w, 11*w):
                for r in (3*n+1, 3*n+7):
                    for epsilon in (0, 1):
                        residual = w*(r-epsilon)**2-z*(n*n+2)-6*w*n+8*w
                        c0 = 2*z-(8+epsilon*epsilon)*w
                        c1 = 3*z-(2+epsilon*epsilon)*w
                        lhs0 = w*r*(r-2*epsilon)-c0-residual
                        lhs1 = w*r*(r-2*epsilon)-c1-residual
                        require(lhs0 == n*(z*n+6*w), "Q0 identity")
                        require(lhs1 == (n-1)*(z*(n+1)+6*w), "Q1 identity")
                        identity_checks += 1

    report = {
        "status": "PASS",
        "scope": "Exact supporting checks; universal conclusions use written proofs.",
        "original_equation_search": False,
        "new_lean_execution": False,
        "constants": {name: {"left": str(left), "strict_upper": str(right)}
                      for name, (left, right) in constants.items()},
        "mod9_square_residues": sorted(squares_mod9),
        "mod9_z_residues": sorted(z_mod9),
        "allowed_z_when_neighbor_prime": [9],
        "actual_binomial_sample_n_range": [104, 320],
        "actual_binomial_congruence_checks": len(binomial_checks),
        "actual_binomial_samples": binomial_checks,
        "generic_local_cube_transfer_checks": valuation_checks,
        "polynomial_identity_checks": identity_checks,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_note_sha256": hashlib.sha256(
            (here / 'v15_neighbor_prime_obstruction.md').read_bytes()).hexdigest(),
    }
    output = here / 'v15_neighbor_prime_checks.json'
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in (
        'status', 'actual_binomial_congruence_checks',
        'generic_local_cube_transfer_checks', 'polynomial_identity_checks')}))


if __name__ == '__main__':
    main()
