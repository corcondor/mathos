"""Exact finite remainder for equal effective inner lower indices.

Equation: C(C(i,j),C(k,l)) = C(i*i,j*j) + C(k*k,l*l).
This checks only the two crossed orientations with effective index two.
The proved finite bounds are documented in equal_effective_upper.md.
No floating point arithmetic or third-party package is used.
"""

from math import comb
import json
from pathlib import Path


def run():
    # Exact constants used in the analytic part.
    assert 2**88 * 23**10 < 3**88
    assert 16 * 24**10 < 81 * 23**10
    assert 2**59 > 3**26

    result = {
        "equation": "C(C(i,j),C(k,l)) = C(i^2,j^2) + C(k^2,l^2)",
        "arithmetic": "Python exact integers and math.comb",
        "scope": "Upper branch; equal effective indices 2; crossed orientations; M >= 21",
        "cases": {},
    }
    for orientation in ("high_first", "high_second"):
        counts = {"checked": 0, "left_smaller": 0, "left_larger": 0, "equalities": []}
        if orientation == "high_first":
            candidates = ((n, n-2, k, 2) for n in range(23, 256) for k in range(4, n))
        else:
            candidates = ((n+s, 2, n, n-2) for n in range(23, 160) for s in range(1, 10))
        for i, j, k, l in candidates:
            A, B = comb(i, j), comb(k, l)
            M, t = max(j, l), A-B
            if not (M >= 21 and M+2 <= t < 10*M and t <= B):
                continue
            counts["checked"] += 1
            lhs = comb(A, t)
            rhs = comb(i*i, j*j) + comb(k*k, l*l)
            if lhs < rhs:
                counts["left_smaller"] += 1
            elif lhs > rhs:
                counts["left_larger"] += 1
            else:
                counts["equalities"].append([i,j,k,l])
        assert not counts["equalities"], counts
        result["cases"][orientation] = counts
    result["verified"] = True
    return result


if __name__ == "__main__":
    result = run()
    Path(__file__).with_name("verification_equal_effective_upper.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
