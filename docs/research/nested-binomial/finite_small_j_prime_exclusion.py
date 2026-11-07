#!/usr/bin/env python3
"""Exact certificate for 21 <= j <= 99, lower branch, j>l, B>=3j.

The prime first upper index p is bounded by the proved A < B^3 < 1000*j^3.
All offsets p-j >= 2 are included, and l=1 is included.
This closes the small-j remainder left by the offset-2/3 theorem.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import time

from finite_prime_outer_exclusion import (
    lucas_direct,
    lucas_table,
    prime_trial,
    sieve,
    tables,
)

CERT = Path(__file__).with_name("finite_small_j_prime_certificates.json")
REPORT = Path(__file__).with_name("finite_small_j_prime_verification.json")


def candidates_generate(j: int, p: int):
    A = comb(p, j)
    d = p - j
    lower = 3 * j
    upper = min(10 * j - 1, A // 2)
    if d == 2:
        lower = 4 * j + 5
    if d == 3:
        lower = 3 * j + 1
    if d >= 3 and j >= 30:
        upper = min(upper, 4 * j - 1)
    for B in range(lower, upper + 1):
        yield B, 1, B, A
    kmax = (1 + isqrt(1 + 8 * upper)) // 2
    for k in range(4, kmax + 1):
        for l in range(2, min(k - 1, j)):
            B = comb(k, l)
            if lower <= B <= upper:
                yield k, l, B, A


def candidates_verify(j: int, p: int):
    A = comb(p, p - j)
    d = p - j
    low = 4 * j + 5 if d == 2 else (3 * j + 1 if d == 3 else 3 * j)
    high = min(A // 2, (4 if d >= 3 and j >= 30 else 10) * j - 1)
    for k in range(low, high + 1):
        yield k, 1, k, A
    e = 2
    while comb(2 * e, e) <= high:
        k = 2 * e
        while comb(k, e) <= high:
            B = comb(k, e)
            if B >= low:
                for l in sorted({e, k - e}):
                    if l < j and k >= l + 2:
                        yield k, l, B, A
            k += 1
        e += 1


def generate():
    started = time.monotonic()
    primes = sieve(997)
    prime_set = set(primes)
    tabs = {q: tables(q) for q in primes}
    rows = []
    unresolved = []
    by_offset = collections.Counter()
    by_l1 = collections.Counter()
    pairs = []
    max_p = 0
    for j in range(21, 100):
        p = j + 2
        limit = 1000 * j**3
        while comb(p, j) < limit:
            # This is monotone in p. The first failed p excludes all larger p.
            if prime_trial(p):
                max_p = max(max_p, p)
                pairs.append([j, p])
                for k, l, B, A in candidates_generate(j, p):
                    witness = None
                    for q in primes:
                        tab = tabs[q]
                        left = lucas_table(A, B, q, tab)
                        right = (lucas_table(p * p, j * j, q, tab)
                                 + lucas_table(k * k, l * l, q, tab)) % q
                        if left != right:
                            witness = q
                            break
                    by_offset[p - j] += 1
                    by_l1["l1" if l == 1 else "l_ge_2"] += 1
                    if witness is None:
                        unresolved.append([j, p, k, l])
                    else:
                        assert witness in prime_set
                        rows.append([j, p, k, l, witness])
            p += 1
    data = {
        "scope": {
            "j_min": 21,
            "j_max": 99,
            "prime_upper_index": True,
            "all_offsets_at_least": 2,
            "branch": "B <= A-B and j>l and B>=3*j",
            "height_prerequisite": "A < B^3 < 1000*j^3",
            "l1_included": True,
        },
        "candidate_count": sum(by_offset.values()),
        "certified_count": len(rows),
        "by_offset": dict(by_offset),
        "by_second_lower_index": dict(by_l1),
        "prime_index_pairs_j_p": pairs,
        "largest_p": max_p,
        "unresolved": unresolved,
        "certificate_rows_j_p_k_l_q": rows,
        "generation_seconds": time.monotonic() - started,
    }
    CERT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(json.dumps({k: v for k, v in data.items()
                      if k not in ("certificate_rows_j_p_k_l_q", "prime_index_pairs_j_p")},
                     ensure_ascii=False, indent=2))


def verify():
    started = time.monotonic()
    source = CERT.read_bytes()
    data = json.loads(source)
    assert data["scope"]["j_min"] == 21 and data["scope"]["j_max"] == 99
    assert data["scope"]["l1_included"] is True
    cert = {}
    for row in data["certificate_rows_j_p_k_l_q"]:
        assert len(row) == 5 and all(isinstance(x, int) for x in row)
        key = tuple(row[:4])
        assert key not in cert
        cert[key] = row[-1]
    pending = set(map(tuple, data["unresolved"]))
    assert len(pending) == len(data["unresolved"])
    assert not pending.intersection(cert)
    pairs = []
    counts = collections.Counter()
    by_l1 = collections.Counter()
    checked_moduli = set()
    missing = []
    for j in range(21, 100):
        # A separate, finite exact bound check provides the verifier's p range.
        assert comb(2 * j, j) > 1000 * j**3
        for p in range(j + 2, 2 * j):
            if not prime_trial(p) or comb(p, j) >= 1000 * j**3:
                continue
            pairs.append([j, p])
            for k, l, B, A in candidates_verify(j, p):
                key = (j, p, k, l)
                counts[p - j] += 1
                by_l1["l1" if l == 1 else "l_ge_2"] += 1
                if key in pending:
                    pending.remove(key)
                    missing.append(key)
                    continue
                assert key in cert, ("missing", key)
                q = cert.pop(key)
                if q not in checked_moduli:
                    assert prime_trial(q)
                    checked_moduli.add(q)
                left = lucas_direct(A, B, q)
                right = (lucas_direct(p * p, j * j, q)
                         + lucas_direct(k * k, l * l, q)) % q
                assert left != right, ("failed witness", key, q)
    assert not cert and not pending
    assert pairs == data["prime_index_pairs_j_p"]
    assert max(p for _, p in pairs) == data["largest_p"]
    assert dict(counts) == {int(k): v for k, v in data["by_offset"].items()}
    assert dict(by_l1) == data["by_second_lower_index"]
    count = sum(counts.values())
    assert count == data["candidate_count"]
    assert count - len(missing) == data["certified_count"]
    result = {
        "verification_passed": not missing,
        "scope": data["scope"],
        "candidate_count": count,
        "certified_count": count - len(missing),
        "unresolved_count": len(missing),
        "unresolved": missing,
        "by_offset": dict(counts),
        "by_second_lower_index": dict(by_l1),
        "prime_index_pair_count": len(pairs),
        "largest_p": max(p for _, p in pairs),
        "distinct_witness_primes": len(checked_moduli),
        "largest_witness_prime": max(checked_moduli, default=None),
        "coverage": "Independent central-binomial p bound; effective-index-first enumeration.",
        "arithmetic": "Exact integers; independent direct-digit Lucas checks.",
        "certificate_sha256": hashlib.sha256(source).hexdigest(),
        "verification_seconds": time.monotonic() - started,
    }
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if missing:
        raise SystemExit(2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("generate", "verify"))
    args = parser.parse_args()
    if args.mode == "generate":
        generate()
    else:
        verify()


if __name__ == "__main__":
    main()
