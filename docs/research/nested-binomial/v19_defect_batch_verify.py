#!/usr/bin/env python3
"""Independent arithmetic verifier of the v19 fixed-defect certificate.

Does not import or run either producer. Fundamental units are recomputed from
the parity of the full continued-fraction period; Lucas digits use factorial
inverses. No floating point, CAS complete solver, Lean, or API calls.
"""

import argparse
from collections import Counter
import gzip
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path
import time


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primality(p):
    if p < 2:
        return False
    return all(p % q != 0 for q in range(2, isqrt(p) + 1))


def decompose(value):
    # Reconstruct from prime factors, independently of producer routines.
    n = value
    square, radical = 1, 1
    for p in range(2, isqrt(value) + 1):
        if p * p > n:
            break
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        square *= p ** (exponent // 2)
        radical *= p ** (exponent % 2)
    if n > 1:
        radical *= n
    assert square * square * radical == value
    return square, radical


def unit_by_period(D):
    a0 = isqrt(D)
    assert a0 * a0 < D
    m, q, a = 0, 1, a0
    period = []
    while True:
        m = q * a - m
        assert (D - m * m) % q == 0
        q = (D - m * m) // q
        a = (a0 + m) // q
        lo, hi = a * q - m, (a + 1) * q - m
        assert (lo <= 0 or lo * lo <= D) and hi > 0 and hi * hi > D
        period.append(a)
        if m == a0 and q == 1:
            assert a == 2 * a0
            break
    terms = [a0] + (period * (1 if len(period) % 2 == 0 else 2))[:-1]
    p0, p1, q0, q1 = 0, 1, 1, 0
    norms = []
    for term in terms:
        p0, p1 = p1, term * p1 + p0
        q0, q1 = q1, term * q1 + q0
        norms.append(p1 * p1 - D * q1 * q1)
    assert norms[-1] == 1 and 1 not in norms[:-1]
    return p1, q1, terms, norms


def digit_tables(p):
    assert primality(p)
    fact = [1]
    for j in range(1, p):
        fact.append(fact[-1] * j % p)
    table = []
    for top in range(p):
        row = []
        for bottom in range(p):
            row.append(0 if bottom > top else fact[top] * pow(fact[bottom] * fact[top - bottom] % p, p - 2, p) % p)
        table.append(row)
    return table


def lucas_from_table(N, R, p, table):
    out = 1
    while R > 0:
        N, top = divmod(N, p)
        R, bottom = divmod(R, p)
        out = out * table[top][bottom] % p
        if out == 0:
            return 0
    return out


def lower_log3(n):
    lo, hi = 0, n.bit_length() + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if pow(3, mid) < n:
            lo = mid
        else:
            hi = mid
    assert pow(3, lo) < n <= pow(3, lo + 1)
    return lo


def verify(path, output):
    start = time.monotonic()
    with gzip.open(path, "rt") as file:
        doc = json.load(file)
    low, high = doc["defects_processed"]
    assert 1 <= low <= high
    expected_keys = [(delta, M, K)
                     for delta in range(low, high + 1)
                     for M in (1, 2, 3, 6)
                     for K in range(9 * M * delta + 1, (10400 * M * delta - 1) // 927 + 1)
                     if gcd(K, delta) == 1]
    assert expected_keys == [(f["delta"], f["M"], f["K"]) for f in doc["families"]]
    checked_units = {}
    for u in doc["units"]:
        assert u["d"] not in checked_units
        actual = unit_by_period(u["d"])
        assert actual == (u["x"], u["y"], u["partial_quotients"], u["convergent_norms"])
        checked_units[u["d"]] = actual[:2]
    tables = {p: digit_tables(p) for p in doc["primes_permitted"]}
    candidate_lookup = {(c["family_index"], c["power"]): c for c in doc["candidates"]}
    assert len(candidate_lookup) == len(doc["candidates"])
    consumed = set()
    total = Counter()
    per_defect = {d: Counter() for d in range(low, high + 1)}
    histogram = Counter()
    used_D = set()
    largest_n = 0

    for index, family in enumerate(doc["families"]):
        delta, M, K = family["delta"], family["M"], family["K"]
        C = delta * M
        counts = per_defect[delta]
        counts["coefficient_families"] += 1
        s, D = decompose(C * K)
        assert (s, D) == (family["s"], family["d"])
        if D == 1:
            counts["square_discriminants"] += 1
            assert family["codes"] == "" and family["first_omitted"] is None
            continue
        used_D.add(D)
        u, v = checked_units[D]
        x, y = 1, 0
        bound = (1 << (42 * delta + 1)) - 1
        for power, stored_code in enumerate(family["codes"], start=1):
            x, y = x * u + D * y * v, y * u + x * v
            assert x < bound and x * x - D * y * y == 1
            counts["pell_points"] += 1
            numerator = s * D * y
            if x % 2 == 0 or numerator % (2 * C):
                code = "i"
            else:
                n, r = (x + 1) // 2, numerator // (2 * C)
                counts["integral"] += 1
                if n <= 103:
                    code = "n"
                else:
                    counts["n_ge_104"] += 1
                    if M != gcd(n, 3) * gcd(n - 1, 6):
                        code = "m"
                    else:
                        counts["actual_M"] += 1
                        Q = (n // gcd(n, 3)) * ((n - 1) // gcd(n - 1, 6))
                        assert Q * M == n * (n - 1)
                        assert delta * r * r == K * Q
                        if delta != Q // gcd(Q, r * r):
                            code = "d"
                        else:
                            counts["actual_delta"] += 1
                            if (r * r % Q) * r % Q != 0:
                                code = "q"
                            else:
                                counts["cube_divisibility"] += 1
                                assert r % delta == 0 and Q % (delta ** 3) == 0
                                if r <= 3 * n or 3 * r >= 10 * n:
                                    code = "c"
                                else:
                                    counts["coarse_interval"] += 1
                                    j = lower_log3(n) if n >= 1024 else None
                                    if j is not None and 4 * j * (r - 3 * n) >= 3 * n:
                                        code = "l"
                                    else:
                                        counts["post_log_candidates"] += 1
                                        loc = (index, power)
                                        c = candidate_lookup[loc]
                                        consumed.add(loc)
                                        assert (c["delta"], c["M"], c["K"], c["n"], c["r"], c["log_lower_j"]) == (delta, M, K, n, r, j)
                                        largest_n = max(largest_n, n)
                                        A = (n * (n - 1) // 2) * (n - 2) // 3
                                        assert 0 < r < A - r
                                        branches = set()
                                        for witness in c["witnesses"]:
                                            branch, p = witness["branch"], witness["prime"]
                                            assert branch in ("small", "complement") and branch not in branches
                                            branches.add(branch)
                                            k = r if branch == "small" else A - r
                                            lhs = lucas_from_table(A, r, p, tables[p])
                                            inner = lucas_from_table(n * n, 6 * n - 9, p, tables[p])
                                            square = pow(k, 2, p)
                                            rhs = (inner + square) % p
                                            assert (witness["left"], witness["inner"], witness["k_squared"], witness["right"]) == (lhs, inner, square, rhs)
                                            assert lhs != rhs
                                            histogram[p] += 1
                                        missing = {"small", "complement"} - branches
                                        assert missing == set(c["unexcluded_branches"])
                                        counts["modular_branches_excluded"] += len(branches)
                                        counts["modular_branches_remaining"] += len(missing)
                                        code = "s" if missing else "w"
            assert code == stored_code, (index, power, stored_code, code)
        x, y = x * u + D * y * v, y * u + x * v
        assert x >= bound and x * x - D * y * y == 1
        assert family["first_omitted"] == {"power": len(family["codes"]) + 1, "x": x, "y": y}
        assert len(family["codes"]) <= 28 * delta + 1

    assert consumed == set(candidate_lookup)
    assert used_D == set(checked_units)
    for d, counts in per_defect.items():
        assert counts["coefficient_families"] < 27 * d
        total.update(counts)
    assert [dict(delta=d, counts=dict(per_defect[d])) for d in range(low, high + 1)] == doc["per_defect"]
    assert dict(total) == doc["counts"]
    assert dict(sorted((str(k), v) for k, v in histogram.items())) == doc["witness_prime_histogram"]
    assert largest_n == doc["max_candidate_n"]
    assert total["modular_branches_remaining"] == 0 and doc["survivors"] == []
    assert doc["status"] == "PASS_COMPLETE_EXCLUSION"
    report = {
        "status": "PASS", "defects_completely_excluded": [low, high],
        "scope": doc["scope"], "counts": dict(total),
        "fundamental_units_independently_recomputed": len(checked_units),
        "all_cf_terms_and_norms_checked": True,
        "all_coefficient_families_and_pell_powers_checked": True,
        "all_first_omitted_points_cross_height": True,
        "all_recorded_modular_witnesses_recomputed": True,
        "producer_imported_or_executed": False,
        "v16_module_imported_or_executed": False,
        "independence": "Full CF period parity instead of first norm-one stopping; factorial-inverse digit coefficients instead of math.comb; binary exponent search for the logarithm bracket",
        "certificate_sha256": digest(path), "verifier_sha256": digest(Path(__file__)),
        "producer_sha256_from_certificate": doc["producer_sha256"],
        "written_theory_dependency": doc["inherited_proof"],
        "wall_seconds": round(time.monotonic() - start, 6),
        "limitations": "Arithmetic certificate verification, not Lean formalization; global completeness depends on the recorded written v16 height and Pell proofs; unbounded delta is not covered"
    }
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=Path(__file__).with_name("v19_defect_13_24_certificate.json.gz"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("v19_defect_13_24_independent_audit.json"))
    args = parser.parse_args()
    verify(args.certificate, args.output)
