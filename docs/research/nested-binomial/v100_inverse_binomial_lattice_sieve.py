#!/usr/bin/env python3
"""v100: exact inverse-binomial gap and shifted-divisor sieve.

Restricted ORIGINAL squared-index equation:
  j=1, ell=k-1, k>=2, i>=k:
     choose(i,k) = i*i + choose(k*k,2*k-1).

No floating point arithmetic is used for correctness. For every k>=3,
R=choose(k*k,2*k-1) > choose(2*k,k), so all i<=2*k fail.
For i>=2*k the difference F(i)=choose(i,k)-i*i-R strictly increases:
  F(i+1)-F(i)=choose(i,k-1)-(2*i+1)>0.
Hence exactly one crossing integer I(k)=min{i:F(i)>=0} exists.
An integer solution can only be i=I(k).

The following NECESSARY arithmetic restrictions are derived from the
falling-factorial identities, without assuming an asymptotic:
  I(k) | k*R,
  I(k)-1 | k*(k-1)*(R+1).
All operations and comparisons are exact Python integers.
Finite range verification is not a proof for unbounded k.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import time


def equation_defect(k: int, i: int, R: int) -> int:
    return math.comb(i, k) - i * i - R


def crossing(k: int, R: int) -> tuple[int, int, int]:
    """Unique sign-crossing with exact arithmetic; all i<crossing have F<0."""
    assert k >= 3
    assert math.comb(2 * k, k) < R
    lo, hi = 2 * k, 4 * k
    assert equation_defect(k, lo, R) < 0
    while equation_defect(k, hi, R) < 0:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if equation_defect(k, mid, R) < 0:
            lo = mid
        else:
            hi = mid
    f_lo = equation_defect(k, lo, R)
    f_hi = equation_defect(k, hi, R)
    assert f_lo < 0 <= f_hi and hi == lo + 1
    return hi, f_lo, f_hi


def run(max_k: int) -> dict:
    assert 3 <= max_k <= 10000
    begin = time.perf_counter()
    records = []
    first_pass = []
    joint_pass = []
    exact_solutions = []
    for k in range(3, max_k + 1):
        R = math.comb(k * k, 2 * k - 1)
        i, fprev, fnow = crossing(k, R)
        h0 = (k * R) % i == 0
        h1 = (k * (k - 1) * (R + 1)) % (i - 1) == 0
        is_solution = (fnow == 0)
        # If a point is a genuine solution, its two shifted-divisor
        # conditions MUST hold. This assertion also checks coding logic.
        assert not is_solution or (h0 and h1)
        rec = {"k": k, "only_possible_i": i,
               "i_divides_kR": h0, "i_minus_1_divides_k_kminus1_Rplus1": h1,
               "is_exact_solution": is_solution}
        records.append(rec)
        if h0:
            first_pass.append({"k": k, "i": i})
        if h0 and h1:
            joint_pass.append({"k": k, "i": i})
        if is_solution:
            exact_solutions.append({"k": k, "i": i})
    report = {
        "statement": "j=1, ell=k-1 original squared-index binomial equation",
        "rigor": "integer-only bisection + proved one-crossing lemma + necessary shifted divisibility",
        "small_k_2": "no solution: choose(i,2)<i^2+4 for every i>=2",
        "range": [3, max_k],
        "count": len(records),
        "first_divisibility_pass": len(first_pass),
        "both_divisibility_pass": len(joint_pass),
        "full_equation_solutions": len(exact_solutions),
        "first_pass_list": first_pass,
        "both_pass_list": joint_pass,
        "solutions": exact_solutions,
        "sample_crossings": [rec for rec in records
                             if rec["k"] in [3, 4, 5, 8, 10, 20, 50, 100, 200, 500, 1000]],
        "records": records,
        "elapsed_seconds": round(time.perf_counter() - begin, 3),
        "source_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    }
    if max_k == 1000:
        assert report["count"] == 998
        assert report["first_divisibility_pass"] == 35
        assert report["both_divisibility_pass"] == 0
        assert report["full_equation_solutions"] == 0
        assert {p["k"]: p["only_possible_i"] for p in report["sample_crossings"]}[1000] == 673779016
    return report


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--max-k", type=int, default=1000)
    p.add_argument("--output", type=pathlib.Path)
    a = p.parse_args()
    report = run(a.max_k)
    summary = {key: val for key, val in report.items() if key != "records"}
    print("V100_RESULT", json.dumps(summary, ensure_ascii=False), flush=True)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
