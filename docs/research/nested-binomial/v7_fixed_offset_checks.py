#!/usr/bin/env python3
"""Exact consistency checks for the uniform proof in the companion note."""
from math import comb, factorial, gcd, lcm, prod
from fractions import Fraction
from pathlib import Path
import json


def check(n, d, h):
    assert d >= 2*h-1 and n-d >= h
    P = prod(n-s for s in range(h))
    L = lcm(*(n-s for s in range(h)))
    assert factorial(h-1)*L % P == 0
    Ms = [prod((d-s)**2-b for b in range(s*s+1)) for s in range(h)]
    M = prod(Ms)
    K = factorial(h-1)*M
    D = P // gcd(P, K)
    falling_d = prod(d-s for s in range(h))
    assert M % falling_d == 0
    A = comb(n, d)
    X = comb(n*n, (n-d)**2)
    assert K*A % P == 0
    assert all(Ms[s]*X % (n-s) == 0 for s in range(h))
    assert K*X % P == 0
    assert A % D == 0 and X % D == 0
    E = 2*sum(s*s+1 for s in range(h))
    assert K < factorial(h-1)*d**E
    return {
        "n": n, "d": d, "h": h, "degree_E": E,
        "P": P, "K": K, "common_divisor_D": D,
        "A_mod_D": A % D, "X_mod_D": X % D,
    }


def main():
    cases = [
        (14,7,4), (21,7,4), (101,7,4), (108,7,4),
        (128,7,4), (197,7,4), (509,7,4),
        (109,8,4), (211,8,4),
        (18,9,5), (110,9,5), (127,9,5), (257,9,5),
        (112,11,5), (211,11,5), (131,30,5),
        (113,12,6), (201,100,6),
    ]
    rows = [check(*c) for c in cases]
    assert any(row["common_divisor_D"] > 1 for row in rows)
    assert Fraction(2916,17) < 172
    assert Fraction(3564,5) < 27**2
    assert Fraction(1)-Fraction(6,108)==Fraction(17,18)
    assert Fraction(1)-Fraction(10,110)==Fraction(10,11)
    report = {
        "status": "pass",
        "scope": "Exact checks of divisibility formulas and constants; no search for all solutions.",
        "original_equation_globally_solved": False,
        "finite_remainders_fully_excluded": False,
        "new_theorems_formalized_in_Lean": False,
        "sample_count": len(rows),
        "samples_with_nontrivial_D": sum(row["common_divisor_D"]>1 for row in rows),
        "samples": rows,
        "height_bound_constants": {
            "four_factors": str(Fraction(2916,17)),
            "five_factors_squared": str(Fraction(3564,5)),
        },
    }
    dest = Path(__file__).with_name("v7_fixed_offset_verification.json")
    dest.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="samples"},indent=2))


if __name__ == "__main__":
    main()
