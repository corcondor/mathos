#!/usr/bin/env python3
"""v102: exact-arithmetic sanity checks for the uniform mod-p^2 theorems.

This DOES NOT brute-force all values of i or claim a full proof.
The mathematical proof is in V102_PRIME_POWER_COPRIME_P_ADIC_ARCHIMEDEAN_ja.md.

For p>=5 prime and 0<=r<p, all integer q:
  C(p*q+r,p) == q*(1+p*H_r) (mod p^2).
For the nested-binomial equation, R_p=C(p^2,2p-1) is a p^2-multiple.
  q == r^2*(1+p*(2r-H_r)) (mod p^2).
That residue gives the UNIQUE q in [0,p^2), without searching i.

The script checks example primes/residues and P-adic local lifting.
Proof for all primes uses Vandermonde, Hensel and rigorous inequalities.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p) + 1))


def harmonic_mod(r: int, p: int) -> int:
    assert r < p and prime(p)
    return sum(pow(d, -1, p) for d in range(1, r + 1)) % p


def predicted_q(p: int, r: int) -> int:
    h = harmonic_mod(r, p)
    return (r * r * (1 + p * (2 * r - h))) % (p * p)


def verify(pmax: int) -> dict:
    checked_binomial_congruences = 0
    checked_padic_equation_lifts = 0
    local_lifts = []
    example_primes = []
    for p in range(5, pmax + 1):
        if not prime(p):
            continue
        R = math.comb(p * p, 2 * p - 1)
        assert R % (p * p) == 0
        for r in range(p):
            hr = harmonic_mod(r, p)
            # A few independent integer q values; check the exact identity.
            for q in {0, 1, 2, p, p + 1, p * p - 1}:
                lhs = math.comb(p * q + r, p) % (p * p)
                rhs = (q * (1 + p * hr)) % (p * p)
                assert lhs == rhs, (p, r, q, lhs, rhs)
                checked_binomial_congruences += 1
            q = predicted_q(p, r)
            i = p * q + r
            residual = math.comb(i, p) - i * i - R
            assert residual % (p * p) == 0
            checked_padic_equation_lifts += 1
            if r in [0, 1, p - 1]:
                local_lifts.append(dict(p=p, r=r, q=q, i=i))
        assert predicted_q(p, 1) == p + 1
        assert predicted_q(p, p - 1) == p * p - 4 * p + 1
        example_primes.append(p)

    assert math.comb(34, 5) < math.comb(25, 9)
    assert math.comb(160, 7) > math.comb(49, 13) + 160 ** 2

    return {
        "status": "PASS_EXACT_MODULAR_SANITY",
        "scope": "exact modular checks, not universal proof nor general-solution search",
        "pmax": pmax,
        "primes": example_primes,
        "tested_formula_cases": checked_binomial_congruences,
        "tested_local_congruence_lifts": checked_padic_equation_lifts,
        "endpoints": local_lifts,
        "explicit_p5_p7_comparisons": "PASS",
        "unbounded_proof": "V102_PRIME_POWER_COPRIME_P_ADIC_ARCHIMEDEAN_ja.md"
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--max-prime", type=int, default=31)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    assert 5 <= a.max_prime <= 97
    result = verify(a.max_prime)
    print("V102_RESULT", json.dumps(result, ensure_ascii=False), flush=True)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
