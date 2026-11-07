#!/usr/bin/env python3
"""Exact exclusion of the proved k<=20 remainder for prime i, e>=3.

Prerequisites: lower branch, j>l, i=p prime, M=j>=21, B<3j.
Then k<j<p, p does not divide B, and Lucas forces p|Y, hence p<=k^2.
If e=min(l,k-l)>=3, C(k,3)<=B<3j<3p<=3k^2, so k<=20 and p<=400.
This program checks exactly that finite remainder; all arithmetic is exact.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from functools import lru_cache
from math import comb
from pathlib import Path
import time

from finite_prime_outer_exclusion import (
    lucas_direct, lucas_table, prime_trial, sieve, tables,
)

CERT = Path(__file__).with_name("finite_prime_effective_index_certificates.json")
REPORT = Path(__file__).with_name("finite_prime_effective_index_verification.json")


@lru_cache(None)
def A_value(p, j):
    return comb(p, j)


def generate():
    started = time.monotonic()
    moduli = sieve(997)
    tabs = {q: tables(q) for q in moduli}
    primes = sieve(400)
    rows = []
    unresolved = []
    counts = collections.Counter()
    total = 0
    for k in range(6, 21):
        for l in range(3, k - 2):
            B = comb(k, l)
            low_j = max(21, B // 3 + 1)
            for p in primes:
                if p < low_j + 2 or p > k * k:
                    continue
                for j in range(low_j, min(p - 2, B - 2) + 1):
                    assert l < j
                    A = A_value(p, j)
                    if 2 * B > A:
                        continue
                    total += 1
                    witness = None
                    for q in moduli:
                        tab = tabs[q]
                        lhs = lucas_table(A, B, q, tab)
                        rhs = (lucas_table(p * p, j * j, q, tab)
                               + lucas_table(k * k, l * l, q, tab)) % q
                        if lhs != rhs:
                            witness = q
                            break
                    counts[min(l, k - l)] += 1
                    if witness is None:
                        unresolved.append([p, j, k, l])
                    else:
                        rows.append([p, j, k, l, witness])
    data = {
        "scope": {
            "p_prime_at_most": 400,
            "k_at_most": 20,
            "j_min": 21,
            "j_max": "p-2",
            "effective_second_lower_index_min": 3,
            "conditions": "j+2 <= B < 3*j; 2*B <= A; p <= k^2",
            "height_prerequisites": "C(k,3)<=B<3j<3p<=3k^2",
        },
        "candidate_count": total,
        "certified_count": len(rows),
        "by_effective_second_lower_index": dict(counts),
        "unresolved": unresolved,
        "certificate_rows_p_j_k_l_q": rows,
        "generation_seconds": time.monotonic() - started,
    }
    CERT.write_text(json.dumps(data, separators=(",", ":")))
    print(json.dumps({k: v for k, v in data.items()
                      if k != "certificate_rows_p_j_k_l_q"}, indent=2))


def verify():
    started = time.monotonic()
    source = CERT.read_bytes()
    data = json.loads(source)
    assert data["scope"]["p_prime_at_most"] == 400
    assert data["scope"]["k_at_most"] == 20
    assert data["scope"]["j_min"] == 21
    assert data["scope"]["effective_second_lower_index_min"] == 3
    cert = {}
    for row in data["certificate_rows_p_j_k_l_q"]:
        assert len(row) == 5 and all(isinstance(x, int) for x in row)
        key = tuple(row[:4])
        assert key not in cert
        cert[key] = row[-1]
    pending = set(map(tuple, data["unresolved"]))
    assert len(pending) == len(data["unresolved"])
    assert not pending.intersection(cert)
    checked_moduli = set()
    count = 0
    counts = collections.Counter()
    missing = []
    for p in range(23, 401):
        if not prime_trial(p):
            continue
        for j in range(21, p - 1):
            A = comb(p, p - j)
            for e in range(3, 11):
                for k in range(2 * e, 21):
                    if k * k < p:
                        continue
                    B = comb(k, e)
                    if not (j + 2 <= B < 3 * j and 2 * B <= A):
                        continue
                    for l in sorted({e, k - e}):
                        assert 3 <= l <= k - 3 and l < j
                        key = (p, j, k, l)
                        count += 1
                        counts[e] += 1
                        if key in pending:
                            pending.remove(key)
                            missing.append(key)
                            continue
                        assert key in cert, ("missing certificate", key)
                        q = cert.pop(key)
                        if q not in checked_moduli:
                            assert prime_trial(q)
                            checked_moduli.add(q)
                        lhs = lucas_direct(A, B, q)
                        rhs = (lucas_direct(p * p, j * j, q)
                               + lucas_direct(k * k, l * l, q)) % q
                        assert lhs != rhs, ("failed witness", key, q)
    assert not cert and not pending
    assert count == data["candidate_count"]
    assert count - len(missing) == data["certified_count"]
    assert dict(counts) == {int(k): v for k, v in data["by_effective_second_lower_index"].items()}
    report = {
        "verification_passed": not missing,
        "scope": data["scope"],
        "candidate_count": count,
        "certified_count": count - len(missing),
        "unresolved_count": len(missing),
        "unresolved": missing,
        "by_effective_second_lower_index": dict(counts),
        "distinct_witness_primes": len(checked_moduli),
        "largest_witness_prime": max(checked_moduli, default=None),
        "coverage": "Independent p,j,e,k enumeration with exact symmetry handling.",
        "arithmetic": "Exact integers; independent direct-digit Lucas congruences.",
        "certificate_sha256": hashlib.sha256(source).hexdigest(),
        "verification_seconds": time.monotonic() - started,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
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
