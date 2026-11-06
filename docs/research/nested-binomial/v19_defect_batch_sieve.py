#!/usr/bin/env python3
"""Complete fixed-defect Pell coverage followed by exact finite-field tests.

This is an extension of the v16 certificate method, not a Coppersmith run.
No probabilistic prime tests, numerical logarithms, Lean, or API calls.
Completeness uses the written v16 height and Pell generation proofs.
"""

import argparse
from collections import Counter
import gzip
import hashlib
import importlib.util
import json
from math import gcd
from pathlib import Path
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def produce(low, high, source, output):
    spec = importlib.util.spec_from_file_location("v16_baseline_readonly", source)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    start = time.monotonic()
    all_counts = Counter()
    per_defect, families, candidates, remaining = [], [], [], []
    radicands = set()
    # Every used prime is checked by trial division in the v16 module.
    primes = [p for p in old.PRIMES if p <= 97]

    def witnesses(n, r):
        A = n * (n - 1) * (n - 2) // 6
        todo = {"small": r, "complement": A - r}
        result = []
        for p in primes:
            left, left_zero = old.lucas(A, r, p)
            inner, inner_zero = old.lucas(n * n, 6 * n - 9, p)
            for branch, k in list(todo.items()):
                square = k * k % p
                right = (inner + square) % p
                if left != right:
                    result.append({"branch": branch, "prime": p,
                                   "left": left, "inner": inner,
                                   "k_squared": square, "right": right,
                                   "left_zero_digit": left_zero,
                                   "inner_zero_digit": inner_zero})
                    del todo[branch]
            if not todo:
                break
        return result, sorted(todo)

    for delta in range(low, high + 1):
        counts = Counter()
        for M in (1, 2, 3, 6):
            C = M * delta
            for K in range(9 * C + 1, (10400 * C - 1) // 927 + 1):
                if gcd(K, delta) != 1:
                    continue
                counts["coefficient_families"] += 1
                s, d = old.squarefree_decomposition(C * K)
                family_index = len(families)
                family = {"delta": delta, "M": M, "K": K, "s": s, "d": d}
                if d == 1:
                    counts["square_discriminants"] += 1
                    family.update({"codes": "", "first_omitted": None})
                    families.append(family)
                    continue
                radicands.add(d)
                unit = old.fundamental_unit(d)
                u, v = unit["x"], unit["y"]
                x, y, power = u, v, 1
                boundary = (1 << (42 * delta + 1)) - 1
                codes = []
                while x < boundary:
                    assert x * x - d * y * y == 1
                    counts["pell_points"] += 1
                    if (x + 1) % 2 or s * d * y % (2 * C):
                        code = "i"
                    else:
                        n, r = (x + 1) // 2, s * d * y // (2 * C)
                        counts["integral"] += 1
                        if n < 104:
                            code = "n"
                        else:
                            counts["n_ge_104"] += 1
                            if gcd(n, 3) * gcd(n - 1, 6) != M:
                                code = "m"
                            else:
                                counts["actual_M"] += 1
                                Q = n * (n - 1) // M
                                assert C * r * r == K * n * (n - 1)
                                if Q // gcd(Q, r * r) != delta:
                                    code = "d"
                                else:
                                    counts["actual_delta"] += 1
                                    if pow(r, 3, Q):
                                        code = "q"
                                    else:
                                        counts["cube_divisibility"] += 1
                                        assert r % delta == 0 and Q % (delta ** 3) == 0
                                        if not (3 * n < r and 3 * r < 10 * n):
                                            code = "c"
                                        else:
                                            counts["coarse_interval"] += 1
                                            j = old.logarithm_lower(n) if n >= 1024 else None
                                            if j is not None and not 4 * j * r < (12 * j + 3) * n:
                                                code = "l"
                                            else:
                                                counts["post_log_candidates"] += 1
                                                ww, missing = witnesses(n, r)
                                                counts["modular_branches_excluded"] += len(ww)
                                                counts["modular_branches_remaining"] += len(missing)
                                                record = {"family_index": family_index, "power": power,
                                                          "delta": delta, "M": M, "K": K,
                                                          "n": n, "r": r, "log_lower_j": j,
                                                          "witnesses": ww, "unexcluded_branches": missing}
                                                candidates.append(record)
                                                if missing:
                                                    remaining.append(record)
                                                    code = "s"
                                                else:
                                                    code = "w"
                    codes.append(code)
                    x, y = u * x + d * v * y, v * x + u * y
                    power += 1
                assert x >= boundary and x * x - d * y * y == 1
                assert len(codes) <= 28 * delta + 1
                family.update({"codes": "".join(codes),
                               "first_omitted": {"power": power, "x": x, "y": y}})
                families.append(family)
        assert counts["coefficient_families"] < 27 * delta
        per_defect.append({"delta": delta, "counts": dict(counts)})
        all_counts.update(counts)

    flat = [w for c in candidates for w in c["witnesses"]]
    report = {
        "status": "PASS_COMPLETE_EXCLUSION" if not remaining else "COMPLETE_COVERAGE_WITH_SURVIVORS",
        "scope": "Original squared-index equation; ell=1, j=i-3, n>=104; both k=r and k=C(n,3)-r",
        "defects_processed": [low, high],
        "height": "n < 2^(42*delta), inherited v16 theorem; not an experimental n cutoff",
        "coefficient_interval": "9*M*delta < K < (10400/927)*M*delta; gcd(K,delta)=1",
        "baseline": {"file": source.name, "sha256": sha(source),
                     "reused_functions": ["squarefree_decomposition", "fundamental_unit", "lucas", "logarithm_lower"]},
        "inherited_proof": {"file": source.with_suffix(".md").name,
                            "sha256": sha(source.with_suffix(".md")),
                            "sections": ["4: height", "5: complete Pell reduction", "6: candidate bound"]},
        "producer_sha256": sha(Path(__file__)),
        "counts": dict(all_counts), "per_defect": per_defect,
        "primes_permitted": primes,
        "witness_prime_histogram": dict(sorted(Counter(w["prime"] for w in flat).items())),
        "max_candidate_n": max((c["n"] for c in candidates), default=None),
        "codes": {"i": "nonintegral reconstruction", "n": "n<104", "m": "wrong actual M",
                  "d": "wrong actual delta", "q": "Q does not divide r^3", "c": "coarse interval fails",
                  "l": "necessary rational log interval fails", "w": "both branches excluded by exact residues",
                  "s": "one or both branches survive the listed moduli"},
        "units": [old.fundamental_unit(d) for d in sorted(radicands)],
        "families": families, "candidates": candidates, "survivors": remaining,
        "claims_not_made": ["unbounded delta excluded", "new Coppersmith implementation",
                            "Lean proof", "DeepSeek call", "cryptographic security result"]
    }
    encoded = (json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("wb") as f:
        with gzip.GzipFile(filename="", mode="wb", fileobj=f, mtime=0) as z:
            z.write(encoded)
    summary = {k: v for k, v in report.items() if k not in ("units", "families", "candidates")}
    summary["wall_seconds"] = round(time.monotonic() - start, 6)
    summary["certificate_file"] = output.name
    summary["certificate_sha256"] = sha(output)
    output.with_suffix("").with_suffix(".summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: summary[k] for k in ("status", "defects_processed", "counts", "witness_prime_histogram", "max_candidate_n", "wall_seconds", "certificate_sha256")}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--low", type=int, default=13)
    parser.add_argument("--high", type=int, default=24)
    parser.add_argument("--baseline", type=Path, default=Path(__file__).with_name("v16_square_defect_pell.py"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("v19_defect_13_24_certificate.json.gz"))
    args = parser.parse_args()
    assert 1 <= args.low <= args.high
    produce(args.low, args.high, args.baseline, args.output)
