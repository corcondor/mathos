#!/usr/bin/env python3
"""Exact algebra and supporting checks for v18_neighbor_cofactor_height.md.

No finite sample is used to prove a universal statement. The universal
proof is in the note. This script uses only Python's standard library.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(*polys):
    out = {}
    for poly in polys:
        for key, val in poly.items():
            out[key] = out.get(key, 0) + val
    return {key: val for key, val in out.items() if val}


def scale(poly, c):
    return {key: val * c for key, val in poly.items() if val * c}


def mul(a, b):
    out = {}
    for x, c in a.items():
        for y, d in b.items():
            key = tuple(i + j for i, j in zip(x, y))
            out[key] = out.get(key, 0) + c * d
    return {key: val for key, val in out.items() if val}


def power(a, n):
    out = {(0, 0, 0): 1}
    for _ in range(n):
        out = mul(out, a)
    return out


def integer(x):
    return {(0, 0, 0): x}


def factor(x):
    out = []
    p = 2
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e:
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append((x, 1))
    return out


def divisors(x):
    vals = [1]
    for p, e in factor(x):
        base = vals[:]
        mult = 1
        for _ in range(e):
            mult *= p
            vals.extend(v * mult for v in base)
    return sorted(vals)


def log_floor(p, m):
    a, power = 0, p
    while power <= m:
        a += 1
        power *= p
    return a


def algebra():
    n = {(1, 0, 0): 1}
    w = {(0, 1, 0): 1}
    J = {(0, 0, 1): 1}
    identities = {}
    c00, c10 = add(scale(w, 10), scale(J, 2)), add(scale(w, 25), scale(J, 3))
    c01, c11 = add(scale(w, 9), scale(J, 2)), add(scale(w, 24), scale(J, 3))
    f0 = mul(J, add(scale(power(w, 2), 30000), scale(mul(w, J), 9600),
                   scale(power(J, 2), 784)))
    f1 = scale(mul(J, add(scale(power(w, 2), 15552),
                         scale(mul(w, J), 5400), scale(power(J, 2), 481))), 7)
    assert not add(scale(power(c00, 3), 125), scale(power(c10, 3), -8), scale(f0, -1))
    identities["small_leading_cube_cancellation"] = "all coefficients zero"
    assert not add(scale(power(c01, 3), 512), scale(power(c11, 3), -27), scale(f1, -1))
    identities["complementary_leading_cube_cancellation"] = "all coefficients zero"
    # In the following identity the second variable is v, not w.
    v = w
    numerator = add(mul(power(n, 2), add(scale(v, 30000), scale(power(v, 2), 9600),
                                       scale(power(v, 3), 784))),
                    scale(mul(add(scale(n, 2), integer(-1)),
                              power(add(integer(10), scale(v, 2)), 3)), -125))
    displayed = add(
        mul(add(scale(power(n, 2), 784), scale(n, -2000), integer(1000)), power(v, 3)),
        mul(add(scale(power(n, 2), 9600), scale(n, -30000), integer(15000)), power(v, 2)),
        mul(add(scale(power(n, 2), 30000), scale(n, -150000), integer(75000)), v),
        scale(n, -250000), integer(125000))
    assert numerator == displayed
    identities["small_positive_numerator"] = "all coefficients zero"
    assert not add(scale(c00, 5), scale(c10, -2), scale(J, -4))
    assert not add(scale(c00, 3), scale(c10, -2), scale(w, 20))
    assert not add(scale(c01, 8), scale(c11, -3), scale(J, -7))
    assert not add(scale(c01, 3), scale(c11, -2), scale(w, 21))
    identities["four_gcd_linear_combinations"] = "all coefficients zero"

    C0, C1 = F(17418496, 9), F(32994542, 27)
    Cs = C0 * F(104, 103) ** 2 * F(112, 3) ** 2
    Cc = C1 * F(104, 103) * F(288, 5) ** 2
    Os = C0 * F(104, 103) ** 2 * F(224, 9) ** 2
    Oc = C1 * F(104, 103) * F(192, 5) ** 2
    assert C0 == 36 * (30000 + 9600 * F(19, 9) + 784 * F(19, 9) ** 2)
    assert C1 == 42 * (15552 + 5400 * F(19, 9) + 481 * F(19, 9) ** 2)
    margins = {
        "complementary_positive_integer": 108864 * 11 - 512 * F(119, 9) ** 3,
        "small_new_height": 2 ** 32 - Cs,
        "complementary_new_height": 2 ** 32 - Cc,
        "small_old_height": 2 ** 31 - Os,
        "complementary_old_height": 2 ** 31 - Oc,
        "small_new_w_height": 2 ** 37 - F(112, 3) ** 7,
        "complementary_new_w_height": 2 ** 18 - F(288, 5) ** 3,
        "small_old_w_height": 2 ** 14 - F(224, 9) ** 3,
        "square_root_coefficient": F(19, 25) - F(2267, 3000),
        "square_root_height": F(4) - 9 * F(19, 25) ** 3,
        "N_upper_at_104": F(5001, 5000) - F(104 ** 2 + 2, 104 ** 2),
    }
    assert all(v > 0 for v in margins.values())
    return identities, {k: str(v) for k, v in margins.items()}


def supporting_common_divisors(records):
    rows = []
    canonical = []
    for rec in records:
        n, r = rec["n"], rec["r"]
        g, d = gcd(n, 3), gcd(n - 1, 6)
        M, N, t = g * d, n * n + 2, r - 3 * n
        Q0, Q1 = n // g, (n - 1) // d
        Q = Q0 * Q1
        assert n >= 104 and Q and r ** 3 % Q == 0 and t >= 4
        assert t * t >= 9 * n
        delta = Q // gcd(Q, r * r)
        for eps in (0, 1):
            S = (r - eps) ** 2 - 6 * n + 8
            T = S - 9 * N
            G = gcd(N, S)
            for q in divisors(G):
                w, z = N // q, S // q
                J = z - 9 * w
                assert J >= 1 and 9 * J < 19 * w
                c0 = (10 - eps) * w + 2 * J
                c1 = (25 - eps) * w + 3 * J
                assert (c0 - w * r * (r - 2 * eps)) % Q0 == 0
                assert (c1 - w * r * (r - 2 * eps)) % Q1 == 0
                assert c0 ** 3 % Q0 == c1 ** 3 % Q1 == 0
                if eps == 0:
                    assert c0 ** 3 % (Q0 * Q0) == c1 ** 3 % (Q1 * Q1) == 0
                    b0, b1 = c0 ** 3 // Q0 ** 2, c1 ** 3 // Q1 ** 2
                    E = 125 * d * d * b0 - 8 * g * g * b1
                    F0 = J * (30000 * w * w + 9600 * w * J + 784 * J * J)
                    assert E > 0 and (n - 1) ** 2 < 36 * F0
                    assert E * n ** 2 * (n - 1) ** 2 == M ** 2 * (
                        n ** 2 * F0 - 125 * c0 ** 3 * (2 * n - 1))
                    assert n < 16 * J ** 6 and J >= 2
                    assert n ** 14 < 2 ** 352 * J ** 33
                    assert w ** 7 < 2 ** 101 * J ** 13
                else:
                    a0, a1 = c0 ** 3 // Q0, c1 ** 3 // Q1
                    E = 512 * d * a0 - 27 * g * a1
                    F1 = 7 * J * (15552 * w * w + 5400 * w * J + 481 * J * J)
                    assert E > 0 and n - 1 < 6 * F1
                    assert E * n * (n - 1) == M * (n * F1 - 512 * c0 ** 3)
                    assert n ** 3 < 2 ** 352 * J ** 33
                    assert w < 2 ** 49 * J ** 5
                rows.append([n, r, eps, q, w, J, E])
                if q == G:
                    assert gcd(w, J) == 1
                    assert (20 if eps == 0 else 21) % gcd(c0, c1) == 0
                    assert (25 if eps == 0 else 72) % gcd(delta, J) == 0
                    canonical.append([n, r, eps, delta, J, gcd(delta, J)])
    return rows, canonical


def binomial_support():
    # Nontrivial small-prime excess cases, including the 3-adic denominator.
    inputs = [218, 450, 816, 989, 1257, 1485, 1917, 2158, 2695, 3433, 3492, 3691]
    rows = []
    for n in inputs:
        N, m = n * n + 2, 6 * n - 9
        A = n * (n - 1) * (n - 2) // 6
        f = factor(N)
        W, R = 1, 1
        for p, e in f:
            a = log_floor(p, m)
            loss = a + int(p == 3)
            W *= p ** min(e, loss)
            R *= p ** max(e - loss, 0)
        assert W * R == N and R > 1
        assert len(factor(R)) == 1
        assert (A - 1) % R == 0
        B = comb(n * n, m)
        assert (B - (8 - 6 * n)) % R == 0
        for r in [3 * n + 1, 3 * n + 4]:
            left = comb(A, r)
            assert left % R == 0
            for eps in (0, 1):
                k = r if eps == 0 else A - r
                S = (r - eps) ** 2 - 6 * n + 8
                assert (left - B - k * k + S) % R == 0
            rows.append({"n": n, "r": r, "R": R, "W": W,
                         "N_factorization": f})
    lemma_count = 0
    for p in (2, 3, 5, 7, 11):
        for e in range(1, 6):
            U = p ** e
            for m in range(1, min(100, U) + 1):
                a = log_floor(p, m)
                modulus = p ** max(e - a, 0)
                lhs = comb(U - 2, m)
                assert (lhs - (-1) ** m * (m + 1)) % modulus == 0
                lemma_count += 1
    return rows, lemma_count


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--residual-report", type=Path, default=here / "v18_residual_gap_checks.json")
    parser.add_argument("--prior-dir", type=Path, default=here)
    args = parser.parse_args()
    residual = json.loads(args.residual_report.read_text())
    identities, margins = algebra()
    rows, canonical = supporting_common_divisors(residual["supporting_sample"]["records"])
    binomial_rows, lemma_count = binomial_support()
    prior_summary_path = args.prior_dir / "v17_neighbor_defect_checks.json"
    prior_summary = json.loads(prior_summary_path.read_text())
    cert_meta = prior_summary["certificate"]
    packed = (args.prior_dir / cert_meta["file"]).read_bytes()
    raw = gzip.decompress(packed)
    assert len(packed) == cert_meta["compressed_bytes"]
    assert len(raw) == cert_meta["uncompressed_bytes"]
    assert hashlib.sha256(packed).hexdigest() == cert_meta["compressed_sha256"]
    assert hashlib.sha256(raw).hexdigest() == cert_meta["uncompressed_sha256"]
    prior = json.loads(raw)
    assert prior["status"] == "PASS" and prior["max_cofactor"] == 64
    assert prior["primality_of_reconstructed_p_required"] is False
    assert len(prior["families"]) == 8712
    assert len(prior["second_divisor_candidates"]) == 1260
    assert len(prior["square_witnesses"]) == 11
    assert not prior["large_case_survivors"]
    assert prior["small_case_derived_index_interval"] == [104, 383]
    assert len(prior["small_case_pairs"]) == 4
    prior_reuse = {
        "summary_sha256": sha(prior_summary_path),
        "compressed_sha256": cert_meta["compressed_sha256"],
        "uncompressed_sha256": cert_meta["uncompressed_sha256"],
        "full_enumeration_reexecuted": False,
        "primality_required": False,
        "counts": prior["statistics"],
        "logical_scope": "All q dividing N and S; q>m falls in saved non-primality-filtered domain, q<=m in saved bounded n domain",
    }
    out = {
        "status": "PASS",
        "scope": "ell=1,j=i-3, both k branches, squared-index equation",
        "exact_polynomial_identities": identities,
        "exact_positive_rational_margins": margins,
        "supporting_common_divisors": {
            "input_necessary_pairs": len(residual["supporting_sample"]["records"]),
            "all_q_cases": len(rows), "canonical_cases": len(canonical),
            "records": rows, "canonical_delta_gcd_records": canonical,
            "finite_samples_prove_universal_theorems": False,
        },
        "actual_binomial_congruences": binomial_rows,
        "general_alternating_pascal_cases": lemma_count,
        "prior_complete_certificate_reuse": prior_reuse,
        "source_sha256": sha(Path(__file__)),
        "proof_note_sha256": sha(here / "v18_neighbor_cofactor_height.md"),
        "supporting_residual_report_sha256": sha(args.residual_report),
        "new_lean_execution": False,
        "new_deepseek_api_calls": 0,
        "original_solution_found": False,
        "verification_boundary": "Written universal proof plus exact coefficient/constant identities; finite necessary-condition and binomial samples are supporting only",
    }
    (here / "v18_neighbor_cofactor_checks.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS", "polynomial_groups": len(identities),
        "positive_constants": len(margins), "all_q_cases": len(rows),
        "canonical_cases": len(canonical), "actual_binomial_cases": len(binomial_rows),
        "general_lemma_cases": lemma_count,
        "proof_note_sha256": out["proof_note_sha256"]}, indent=2))


if __name__ == "__main__":
    main()

