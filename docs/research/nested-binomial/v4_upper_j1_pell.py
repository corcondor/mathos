#!/usr/bin/env python3
"""Certificate generation for j=1 in the upper branch via Pell equations.

All arithmetic is exact. Completeness uses v4_upper_j1_smooth_pell.md and
the earlier exact height theorem. No claim of a bound on ell is made.
"""

import argparse
import hashlib
import json
import math
import pathlib
import time


def primes_upto(n):
    flags = bytearray(b"\1") * (n + 1)
    flags[:2] = b"\0\0"
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            flags[p * p:n + 1:p] = b"\0" * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if flags[p]]


def smooth(n, primes):
    assert n > 0
    for p in primes:
        while n % p == 0:
            n //= p
    return n == 1


def exact_height(ell):
    numerator = math.factorial(ell * ell)
    denominator = math.factorial(ell) ** (2 * ell)
    lo, hi = ell, 2 * ell
    while math.comb(hi, ell) * denominator < numerator:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if math.comb(mid, ell) * denominator < numerator:
            lo = mid
        else:
            hi = mid
    assert math.comb(lo, ell) * denominator < numerator
    assert math.comb(lo + 1, ell) * denominator >= numerator
    return lo, numerator, denominator


def squarefree_products(primes):
    products = [1]
    for p in primes:
        products += [p * d for d in products]
    return products[1:]


def fundamental_bounded(d, bound):
    """First +1 Pell convergent, or None once increasing x exceeds bound."""
    a0 = math.isqrt(d)
    assert a0 * a0 != d
    m, denominator, a = 0, 1, a0
    x_previous, x_before = 1, 0
    y_previous, y_before = 0, 1
    while True:
        x = a * x_previous + x_before
        y = a * y_previous + y_before
        if x > bound:
            return None
        if x * x - d * y * y == 1:
            assert x > 1 and y > 0
            return x, y
        x_before, x_previous = x_previous, x
        y_before, y_previous = y_previous, y
        m = denominator * a - m
        numerator = d - m * m
        assert numerator % denominator == 0
        denominator = numerator // denominator
        a = (a0 + m) // denominator


def pell_candidates(primes, bound):
    candidates = {}
    counters = {
        "squarefree_d": 0,
        "fundamental_below_height": 0,
        "smooth_fundamental_y": 0,
        "pell_powers_below_height": 0,
        "smooth_triples": 0,
        "largest_pell_exponent_considered": 0,
    }
    for d in squarefree_products(primes):
        counters["squarefree_d"] += 1
        fundamental = fundamental_bounded(d, bound)
        if fundamental is None:
            continue
        counters["fundamental_below_height"] += 1
        x1, y1 = fundamental
        # Every y_n is divisible by y_1.
        if not smooth(y1, primes):
            continue
        counters["smooth_fundamental_y"] += 1
        x, y, exponent = x1, y1, 1
        while x <= bound:
            assert x * x - d * y * y == 1
            counters["pell_powers_below_height"] += 1
            counters["largest_pell_exponent_considered"] = max(
                counters["largest_pell_exponent_considered"], exponent)
            if smooth(y, primes) and smooth(x, primes):
                assert smooth(x - 1, primes) and smooth(x + 1, primes)
                assert x not in candidates
                candidates[x] = {"d": str(d), "y": str(y), "exponent": exponent}
            x, y = x1 * x + d * y1 * y, x1 * y + y1 * x
            exponent += 1
    counters["smooth_triples"] = len(candidates)
    return candidates, counters


def lucas(n, k, p):
    if k < 0 or k > n:
        return 0
    answer = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        answer = answer * math.comb(ni, ki) % p
        n //= p
        k //= p
    return answer


def equation_candidates(ell, ks, height):
    bound, numerator, denominator = height
    for k in sorted(ks):
        if k < ell + 2 or k > bound:
            continue
        B = math.comb(k, ell)
        t_stop = 2 * ell if k >= 2 * ell else 10 * ell
        for t in range(ell + 2, min(t_stop, B + 1)):
            # Exact form of t > phi * ell.
            if (2 * t - ell) ** 2 <= 5 * ell * ell:
                continue
            A = B + t
            if A * denominator >= numerator:
                continue
            yield k, t, A


def generate(ell_min, ell_max, output):
    started = time.monotonic()
    heights = {ell: exact_height(ell) for ell in range(ell_min, ell_max + 1)}
    groups = {}
    for ell in heights:
        group = tuple(primes_upto(2 * ell))
        groups.setdefault(group, []).append(ell)
    witnesses = []
    survivors = []
    group_reports = []
    counts = {ell: 0 for ell in heights}
    witness_primes = primes_upto(251)
    for primes, ells in groups.items():
        bound = max(heights[ell][0] for ell in ells)
        ks, counters = pell_candidates(primes, bound)
        report = {"ells": ells, "prime_count": len(primes),
                  "largest_smooth_prime": primes[-1], "k_bound": str(bound),
                  **counters}
        group_reports.append(report)
        print(json.dumps(report), flush=True)
        for ell in ells:
            for k, t, A in equation_candidates(ell, ks, heights[ell]):
                counts[ell] += 1
                for p in witness_primes:
                    left = lucas(A, t, p)
                    right = (A * A + lucas(k * k, ell * ell, p)) % p
                    if left != right:
                        witnesses.append({"ell": ell, "k": str(k), "t": t,
                                          "p": p, "left": left, "right": right})
                        break
                else:
                    survivors.append({"ell": ell, "k": str(k), "t": t})
    result = {
        "equation": "C(C(i,j),C(k,l))=C(i^2,j^2)+C(k^2,l^2)",
        "scope": {"j": 1, "branch": "A/2 <= B < A", "ell_min": ell_min,
                  "ell_max": ell_max, "i_and_k": "unbounded before proved reductions"},
        "method": "three-consecutive smoothness, bounded Pell generation, exact Lucas witnesses",
        "dependencies": ["v4_upper_j1_smooth_pell.md", "global_height_bound.md",
                         "sharp_q_bounds.md", "entropy_phi_reduction.md"],
        "groups": group_reports,
        "height_bounds": {str(ell): str(heights[ell][0]) for ell in heights},
        "candidate_counts": counts,
        "total_equation_candidates": sum(counts.values()),
        "witness_count": len(witnesses),
        "largest_witness_prime": max((w["p"] for w in witnesses), default=0),
        "survivors": survivors,
        "witnesses": witnesses,
        "seconds": time.monotonic() - started,
    }
    path = pathlib.Path(output)
    path.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True,
                               separators=(",", ":")) + "\n")
    print(json.dumps({"written": str(path), "bytes": path.stat().st_size,
                      "candidates": result["total_equation_candidates"],
                      "survivors": len(survivors), "seconds": result["seconds"],
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ell-min", type=int, default=21)
    parser.add_argument("--ell-max", type=int, default=30)
    parser.add_argument("--output", default="v4_upper_j1_pell_certificates.json")
    args = parser.parse_args()
    assert 21 <= args.ell_min <= args.ell_max
    generate(args.ell_min, args.ell_max, args.output)
