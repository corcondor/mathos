"""Exact finite certificate for the equal-complement upper branch.

Analytic prerequisites, proved in continuation_arithmetic.md:
* M <= 20 has already been excluded by the earlier complete certificate.
* In the upper branch with equal complements, the complement must be 2.
* For complement 2, all n = i >= 256 are excluded analytically.

This program checks every remaining n = 23, ..., 255 and k = 3, ..., n-1
satisfying the necessary gap and upper-branch conditions, by exact integer
arithmetic. It requires only the Python standard library.
"""

import json
from math import comb
from pathlib import Path


def verify():
    squared_binomial = {n: comb(n * n, 4 * n - 4) for n in range(3, 256)}
    checked = 0
    left_less = 0
    left_greater = 0
    equalities = []

    for n in range(23, 256):
        j = n - 2
        A = n * (n - 1) // 2
        M = j
        for k in range(3, n):
            ell = k - 2
            B = k * (k - 1) // 2
            t = A - B
            if not (M + 2 <= t < 12 * M and t <= B):
                continue
            lhs = comb(A, t)
            rhs = squared_binomial[n] + squared_binomial[k]
            checked += 1
            if lhs < rhs:
                left_less += 1
            elif lhs > rhs:
                left_greater += 1
            else:
                equalities.append([n, j, k, ell])

    report = {
        "verification_passed": not equalities,
        "scope": "Equal complements d=2, upper branch, M>=21, 23<=i<256.",
        "analytic_prerequisites": "continuation_arithmetic.md, Sections 1-3",
        "gap_constant_used": 12,
        "checked_pairs": checked,
        "left_less_than_right": left_less,
        "left_greater_than_right": left_greater,
        "equalities": equalities,
        "arithmetic": "Exact Python integers and math.comb; no floating point.",
    }
    target = Path(__file__).with_name("verification_equal_complement_upper.json")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))
    if equalities:
        raise RuntimeError("A candidate equality survived the finite check.")
    return report


if __name__ == "__main__":
    verify()
