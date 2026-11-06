#!/usr/bin/env python3
"""Exact finite Pell certificate for the reduced denominator of r^2/Q.

Completeness requires the written height reduction, Legendre's convergent
criterion for actual Pell solutions, and the minimal-unit descent lemma.
No floating point, CAS complete solver, API request or Lean execution.
"""

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
from math import comb, gcd, isqrt
from pathlib import Path


STAGES = {
    "i": "n or r is not an integer under reconstruction",
    "n": "n is below 104",
    "m": "actual gcd(n,3)*gcd(n-1,6) differs from M",
    "d": "actual reduced denominator of r^2/Q differs from delta",
    "q": "Q does not divide r^3",
    "c": "strict coarse interval fails",
    "l": "strict rational logarithmic interval fails",
    "w": "both original k branches have recorded modular witnesses",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def squarefree_decomposition(z):
    original = z
    s = d = 1
    p = 2
    while p * p <= z:
        e = 0
        while z % p == 0:
            e += 1
            z //= p
        s *= p ** (e // 2)
        if e % 2:
            d *= p
        p += 1
    if z > 1:
        d *= z
    require(s * s * d == original, "squarefree decomposition")
    return s, d


@lru_cache(None)
def fundamental_unit(d):
    a0 = isqrt(d)
    require(a0 * a0 < d < (a0 + 1) ** 2, "nonsquare radicand")
    m, den, a = 0, 1, a0
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    partials, norms = [], []
    while True:
        require(den > 0 and a == (a0 + m) // den, "exact complete quotient")
        lower = a * den - m
        upper = (a + 1) * den - m
        require((lower <= 0 or lower * lower <= d)
                and upper > 0 and d < upper * upper, "floor of quadratic surd")
        x, y = a * pm1 + pm2, a * qm1 + qm2
        norm = x * x - d * y * y
        partials.append(a)
        norms.append(norm)
        if norm == 1:
            require(all(z != 1 for z in norms[:-1]), "first norm-one convergent")
            return {"d": d, "a0": a0, "x": x, "y": y,
                    "partial_quotients": partials, "convergent_norms": norms}
        pm2, pm1, qm2, qm1 = pm1, x, qm1, y
        m = den * a - m
        numerator = d - m * m
        require(numerator > 0 and numerator % den == 0, "surd step exact division")
        den = numerator // den
        a = (a0 + m) // den


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


PRIMES = [p for p in range(2, 1000) if is_prime(p)]


def lucas(n, k, p):
    value = 1
    zero = None
    digit = 0
    while n or k:
        top, bottom = n % p, k % p
        if bottom > top:
            value = 0
            if zero is None:
                zero = {"position": digit, "upper_digit": top, "lower_digit": bottom}
        else:
            value = value * comb(top, bottom) % p
        n //= p
        k //= p
        digit += 1
    return value, zero


def logarithm_lower(n):
    j, power = 0, 1
    while power * 3 < n:
        j += 1
        power *= 3
    require(power < n and power * 3 >= n, "strict base-three logarithm bracket")
    return j


def original_witness(n, r, branch):
    A = n * (n - 1) * (n - 2) // 6
    k = r if branch == "k=r" else A - r
    for p in PRIMES:
        left, left_zero = lucas(A, r, p)
        B, B_zero = lucas(n * n, 6 * n - 9, p)
        square = k * k % p
        right = (B + square) % p
        if left != right:
            return {"branch": branch, "prime": p, "left_residue": left,
                    "B_residue": B, "k_squared_residue": square, "right_residue": right,
                    "left_zero_digit": left_zero, "B_zero_digit": B_zero}
    raise AssertionError(f"No modular witness among the stated primes: n={n}, r={r}, branch={branch}")


def classify_point(numerator_n, numerator_r, denominator_r, delta, M, K,
                   family_index, power_index, counts, candidates):
    if numerator_n % 2 or numerator_r % denominator_r:
        return "i"
    n, r = numerator_n // 2, numerator_r // denominator_r
    counts["integral_n_r"] += 1
    if n < 104:
        return "n"
    counts["n_ge_104"] += 1
    if gcd(n, 3) * gcd(n - 1, 6) != M:
        return "m"
    counts["actual_M"] += 1
    Q = n * (n - 1) // M
    require(M * delta * r * r == K * n * (n - 1), "reconstructed quadratic identity")
    if Q // gcd(Q, r * r) != delta:
        return "d"
    counts["actual_delta"] += 1
    if r ** 3 % Q:
        return "q"
    counts["cube_divisibility"] += 1
    require(r % delta == 0 and Q % (delta ** 3) == 0, "defect cube and r divisibility")
    if not 3 * n < r or not 3 * r < 10 * n:
        return "c"
    counts["strict_coarse_interval"] += 1
    J = logarithm_lower(n) if n >= 1024 else None
    if J is not None and not 4 * J * r < 12 * J * n + 3 * n:
        return "l"
    counts["strict_log_interval"] += 1
    witnesses = [original_witness(n, r, branch) for branch in ["k=r", "k=A-r"]]
    counts["original_branches"] += 2
    counts["modular_branch_exclusions"] += 2
    candidates.append({"family_index": family_index, "power_index": power_index,
                       "delta": delta, "M": M, "K": K, "n": n, "r": r,
                       "log_lower_J": J, "witnesses": witnesses})
    return "w"


def run(limit, output, v15_certificate):
    require(1 <= limit, "positive defect cutoff")
    totals = Counter()
    families, candidates, per_delta = [], [], []
    used_d = set()
    for delta in range(1, limit + 1):
        counts = Counter()
        for M in [1, 2, 3, 6]:
            C = M * delta
            last_K = (10400 * C - 1) // 927
            for K in range(9 * C + 1, last_K + 1):
                if gcd(K, delta) != 1:
                    continue
                counts["coefficient_triples"] += 1
                s, d = squarefree_decomposition(C * K)
                family_index = len(families)
                family = {"delta": delta, "M": M, "K": K, "s": s, "d": d}
                if d == 1:
                    counts["square_discriminants"] += 1
                    family.update({"pell_points": 0, "dispositions": "", "first_omitted_point": None,
                                   "reason": "(x-y)(x+y)=1 has no positive-y solution"})
                    families.append(family)
                    continue
                used_d.add(d)
                unit = fundamental_unit(d)
                u, v = unit["x"], unit["y"]
                x, y, power_index = u, v, 1
                boundary = (1 << (42 * delta + 1)) - 1
                dispositions = []
                while x < boundary:
                    require(x * x - d * y * y == 1, "Pell norm")
                    counts["pell_points_below_height"] += 1
                    code = classify_point(x + 1, s * d * y, 2 * C, delta, M, K,
                                          family_index, power_index, counts, candidates)
                    dispositions.append(code)
                    x, y = u * x + d * v * y, v * x + u * y
                    power_index += 1
                require(x >= boundary and x * x - d * y * y == 1, "first omitted point")
                require(len(dispositions) <= 28 * delta + 1, "universal recurrence length bound")
                family.update({"pell_points": len(dispositions), "dispositions": "".join(dispositions),
                               "first_omitted_point": {"power": power_index, "x": x, "y": y}})
                families.append(family)
        require(counts["coefficient_triples"] < 27 * delta, "uniform coefficient count")
        totals.update(counts)
        per_delta.append({"delta": delta, "statistics": dict(counts)})

    require(totals["original_branches"] == totals["modular_branch_exclusions"], "all original branches excluded")
    delta1 = sorted([[c["n"], c["r"]] for c in candidates if c["delta"] == 1])
    require([169, 546] in delta1, "known nontrivial v15 control retained")
    baseline = json.loads(v15_certificate.read_text())
    old_pairs = sorted({(x["n"], x["r"]) for x in baseline["original_equation_modular_records"]})
    require(delta1 == [list(x) for x in old_pairs], "v15 final delta=1 candidate set")
    witnesses = [w for c in candidates for w in c["witnesses"]]
    vanish = sum(w["left_residue"] == w["B_residue"] == 0
                 and w["k_squared_residue"] != 0 for w in witnesses)
    report = {
        "status": "PASS",
        "scope": "ell=1, j=i-3, n>=104, both k branches; original squared-index equation",
        "definition": "delta=Q/gcd(Q,r^2), Q=n(n-1)/(gcd(n,3)gcd(n-1,6))",
        "excluded_defects": [1, limit],
        "necessary_lower_bound": limit + 1,
        "height": "n<exp(28*delta)<2^(42*delta)",
        "coefficient_conditions": "M in {1,2,3,6}, C=M*delta, gcd(K,delta)=1, 9*C<K<10400*C/927",
        "reconstruction": "C*K=s^2*d; x^2-d*y^2=1; n=(x+1)/2; r=s*d*y/(2*C)",
        "continued_fraction_completeness": "Actual Pell solutions satisfy |x/y-sqrt(d)|<1/(2*y^2), so Legendre's convergent criterion applies. All earlier convergents are encoded and checked. This does not replace the separate old 3/2 approximation constant.",
        "unit_power_completeness": "Minimal positive-y unit generates all positive Pell solutions by the written norm-one descent.",
        "disposition_codes": STAGES,
        "statistics": dict(totals),
        "by_delta": per_delta,
        "fundamental_units": [fundamental_unit(d) for d in sorted(used_d)],
        "families": families,
        "candidates": candidates,
        "largest_witness_prime": max(w["prime"] for w in witnesses),
        "both_binomials_zero_witnesses": vanish,
        "largest_candidate_decimal_digits": max(len(str(c["n"])) for c in candidates),
        "survivors": [],
        "v15_control": {"input_file": v15_certificate.name, "input_sha256": digest(v15_certificate),
                        "same_final_delta1_pairs": True, "pairs": delta1},
        "source_sha256": digest(Path(__file__)),
        "verification_boundary": "Written elementary reductions plus exact Python certificate; not Lean verification, external peer review, or a new complete CAS solver execution.",
    }
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ["status", "excluded_defects", "statistics",
                      "largest_witness_prime", "both_binomials_zero_witnesses",
                      "largest_candidate_decimal_digits", "survivors"]}, indent=2))
    print(json.dumps({"distinct_radicands": len(used_d), "output_bytes": output.stat().st_size}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--v15-certificate", type=Path, required=True)
    args = parser.parse_args()
    run(args.limit, args.output, args.v15_certificate)
