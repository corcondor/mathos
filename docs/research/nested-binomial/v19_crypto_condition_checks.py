#!/usr/bin/env python3
"""Exact supporting checks for the written Coppersmith applicability analysis.

The universal exclusions in the note are proved algebraically. These checks
inspect their use on the 93 fully generated auxiliary candidates and construct
two independent short evaluation vectors on one fixed conic. No lattice solver
or probabilistic recovery procedure is used.
"""

from collections import Counter
import gzip
import hashlib
import json
from math import gcd
from pathlib import Path


BASE = Path(__file__).resolve().parent
CERTIFICATE = BASE / "v19_defect_13_24_certificate.json.gz"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    with gzip.open(CERTIFICATE, "rt") as handle:
        data = json.load(handle)
    counts = Counter()
    for rec in data["candidates"]:
        n, r, delta, M, K = (rec[x] for x in ("n", "r", "delta", "M", "K"))
        Q, C = n * (n - 1) // M, M * delta
        assert delta ** 3 <= Q and Q % (delta ** 3) == 0
        assert C ** 3 <= M * M * n * (n - 1) < n ** 6
        assert delta < Q and K * Q == delta * r * r
        assert C < n * n and K < r * r
        primitive_content = gcd(C, K)
        W = max(K * n * n, C * r * r) // primitive_content
        assert n * n * r * r > W
        assert r ** 3 > Q
        counts["raw_bivariate_bound_excluded"] += 1
        counts["raw_univariate_cubic_bound_excluded"] += 1
        for c in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15):
            if ((c + 2) * n - 3 * c) % 6 == 0:
                assert 0 < n * n - c < n * n
                counts["negative_neighbor_degree_two_bound_excluded"] += 1

    # Two auxiliary candidates, already excluded from the original binomial
    # equation by their recorded modular witnesses, on the same exact conic.
    selected = sorted((rec for rec in data["candidates"]
                       if (rec["delta"], rec["M"], rec["K"]) == (13, 6, 703)),
                      key=lambda rec: rec["n"])[:2]
    assert len(selected) == 2
    C, K = 78, 703
    H = max(max(rec["n"], rec["r"]) for rec in selected) + 1
    S = H * H
    vectors = []
    for rec in selected:
        n, r = rec["n"], rec["r"]
        assert C * r * r - K * n * (n - 1) == 0
        vec = [S, H * n, H * r, n * n, n * r, r * r]
        assert sum(z * z for z in vec) < 6 * S * S
        weighted_coefficients = [0, K * H, 0, -K * S, 0, C * S]
        assert sum(a * b for a, b in zip(vec, weighted_coefficients)) == 0
        vectors.append(vec)
    minor = vectors[0][0] * vectors[1][1] - vectors[1][0] * vectors[0][1]
    assert minor != 0

    # Exact finite-field enumeration illustrates that the raw conic itself is
    # not an empty modular variety. It is a complete calculation for each p.
    finite_fields = []
    for p in (5, 7, 11, 17, 19, 23, 29, 31):
        assert all(p % d for d in range(2, p))
        points = [(n, r) for n in range(p) for r in range(p)
                  if (C * r * r - K * n * (n - 1)) % p == 0]
        assert (0, 0) in points and (1, 0) in points
        row = {"prime": p, "affine_point_count": len(points)}
        if 2 * C * K % p:
            legendre = pow(C * K % p, (p - 1) // 2, p)
            legendre = -1 if legendre == p - 1 else legendre
            assert len(points) == p - legendre
            row["nonsingular_count_formula"] = "p-Legendre(C*K,p)"
        finite_fields.append(row)

    out = {
        "status": "PASS", "certificate_sha256": sha(CERTIFICATE),
        "script_sha256": sha(Path(__file__)), "supporting_counts": dict(counts),
        "universal_vs_finite": "The inequalities for arbitrary roots and boxes are proved in the note; these counts are supporting checks on the complete fixed-defect candidate set",
        "dual_nonisolation": {
            "delta": 13, "M": 6, "C": C, "K": K,
            "points": [{key: rec[key] for key in ("family_index", "power", "n", "r", "witnesses")} for rec in selected],
            "common_box": {"n_upper_exclusive": H, "r_upper_exclusive": H},
            "monomials": ["1", "n", "r", "n^2", "n*r", "r^2"],
            "scale_S": S,
            "vectors": vectors,
            "nonzero_independence_minor": minor,
            "both_squared_norms_less_than_6S2": True,
            "deduction": "For the modular orthogonal lattice containing both evaluation vectors, lambda_2 < S*sqrt(6), contradicting the sufficient gap lambda_2 > eta^(2*(6-1))*S*sqrt(6) for every eta>=1. The note proves the analogous argument for every total degree t>=2.",
            "not_original_solutions": "Both points have explicit modular witnesses excluding both original k branches in the full certificate"
        },
        "finite_field_complete_checks": finite_fields,
        "lattice_solver_run": False,
        "Lean_run": False,
        "DeepSeek_call": False
    }
    target = BASE / "v19_crypto_condition_checks.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": out["status"], "supporting_counts": dict(counts),
                      "dual_conic": {"C": C, "K": K, "distinct_points": 2},
                      "finite_fields": finite_fields}, indent=2))


if __name__ == "__main__":
    main()
