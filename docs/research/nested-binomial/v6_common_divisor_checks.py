"""Exact checks of the written common-divisor proof.

The uniform theorem is proved in v6_common_divisor.md. This script checks
the derived exponent cases and the sole residual integer n=250 exactly.
"""
from math import comb, gcd, isqrt
from pathlib import Path
import json


def squarefree(n):
    return all(n % (d*d) for d in range(2, isqrt(n)+1))


def main():
    samples = []
    for n in (104, 106, 109, 250, 512):
        t, N, m = n-1, n*n, (n-3)**2
        assert (t**3-8*t*t+23*t-28) % 2 == 0
        assert comb(m, 2)-6 == t*((t**3-8*t*t+23*t-28)//2)
        assert comb(N, 2) % t == 0
        A, X = comb(n, 3), comb(N, m)
        q0, q1 = n//gcd(n, 3), (n-1)//gcd(n-1, 6)
        Q = q0*q1
        assert gcd(q0, q1) == 1
        assert A % Q == 0 and X % Q == 0
        samples.append({"n": n, "q0": q0, "q1": q1, "Q": Q,
                        "A_mod_Q": A % Q, "X_mod_Q": X % Q})

    d3_values = sorted({2**a*5**b for a in range(1, 4)
                        for b in range(4)
                        if a+b == 2*((a+b)//2) and 2**a*5**b >= 104})
    assert d3_values == [250, 1000]
    assert squarefree(249) and not squarefree(999)
    for a in range(1, 4):
        assert (19**a-1) % 9 == 0
        assert (5**a-1) % 4 == 0

    n, p = 250, 83
    A, r = comb(n, 3), 830
    X, L = comb(n*n, (n-3)**2), comb(A, r)
    assert A == 2573000 and A//p % p == 41
    left = L % p
    via_lucas = comb(41, 10) % p
    assert left == via_lucas and left != 0
    rows = []
    for k in (r, A-r):
        right = (X+k*k) % p
        assert right == 0 and left != right
        rows.append({"k": k, "left_mod_83": left, "right_mod_83": right})
    result = {
        "status": "pass",
        "scope": "Formula checks and complete small exponent remainder; the infinite theorem is the written proof.",
        "common_divisor_samples": samples,
        "d3_exponent_cases_above_103": d3_values,
        "d3_squarefree_successor_cases": [250],
        "d6_t19_exclusion": "9 divides 19^a-1 for all a=1,2,3",
        "d6_t20_exclusion": "4 divides 5^a-1 for all a=1,2,3",
        "n250": {"A": A, "r": r, "prime": p,
                 "lucas_small_binomial_residue": via_lucas,
                 "direct_binomial_branches": rows},
        "whole_equation_solved": False,
        "new_squarefree_successor_theorem_formalized_in_Lean": False,
    }
    dest = Path(__file__).with_name("v6_common_divisor_verification.json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
