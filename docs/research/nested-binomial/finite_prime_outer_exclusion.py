#!/usr/bin/env python3
"""Exact finite certificate for the prime upper index, lower-branch case.

Only the proved finite remainder is checked:
  i = p prime, 103 <= p < 16384;
  j = p - d >= 100, d in {2, 3};
  l >= 2, l < j, k >= l+2;
  B = C(k,l), 3*j <= B <= A/2, A = C(p,d);
  B < 10*j, strengthened to B < 5*j if j >= 800;
  d=2: B >= 4*j+5; d=3: 3*j < B < 4*j.

The l=1 family is excluded by a separate uniform proof modulo p.
The p >= 16384 family is excluded by a separate analytic proof.
This script does NOT assert either prerequisite merely from this scan.

The generator and verifier use different candidate enumerations and
different modular-binomial implementations. All arithmetic is exact.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import time


LIMIT = 16384
CERTIFICATE = Path(__file__).with_name("finite_prime_outer_certificates.json")
REPORT = Path(__file__).with_name("finite_prime_outer_verification.json")


def sieve(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p * p : limit + 1 : p] = b"\x00" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def band(p: int, d: int) -> tuple[int, int, int, int]:
    j = p - d
    A = comb(p, d)
    lower = 4 * j + 5 if d == 2 else 3 * j + 1
    upper = min(A // 2, (5 if j >= 800 else 10) * j - 1)
    if d == 3:
        upper = min(upper, 4 * j - 1)
    return j, A, lower, upper


def candidates_generator(p: int, d: int):
    """Enumerate k first; obtain C(k,e) by its exact recurrence."""
    j, A, lower, upper = band(p, d)
    if j < 100 or upper < lower:
        return
    kmax = (1 + isqrt(1 + 8 * upper)) // 2
    for k in range(4, kmax + 1):
        B = k * (k - 1) // 2
        for e in range(2, k // 2 + 1):
            if B > upper:
                break
            if B >= lower:
                for l in ((e,) if k == 2 * e else (e, k - e)):
                    if l < j:
                        yield k, l, B, A
            B = B * (k - e) // (e + 1)


def candidates_verifier(p: int, d: int):
    """Enumerate the effective lower index first, then binary-search k.

    This deliberately does not call band() or candidates_generator().
    """
    j = p - d
    if j < 100:
        return
    A = comb(p, d)
    lo_B = 4 * j + 5 if d == 2 else 3 * j + 1
    hi_B = min(A // 2, (5 if j >= 800 else 10) * j - 1)
    if d == 3:
        hi_B = min(hi_B, 4 * j - 1)
    kmax = isqrt(2 * hi_B) + 2
    e = 2
    while comb(2 * e, e) <= hi_B:
        left, right = 2 * e, kmax + 1
        while left < right:
            mid = (left + right) // 2
            if comb(mid, e) < lo_B:
                left = mid + 1
            else:
                right = mid
        first = left
        left, right = 2 * e, kmax + 1
        while left < right:
            mid = (left + right) // 2
            if comb(mid, e) <= hi_B:
                left = mid + 1
            else:
                right = mid
        stop = left
        for k in range(first, stop):
            B = comb(k, e)
            for l in sorted({e, k - e}):
                if 2 <= l < j and k >= l + 2:
                    assert lo_B <= B <= hi_B
                    assert B == comb(k, l)
                    yield k, l, B, A
        e += 1


def tables(q: int) -> tuple[list[int], list[int]]:
    fact = [1] * q
    for n in range(2, q):
        fact[n] = fact[n - 1] * n % q
    inv = [1] * q
    inv[-1] = pow(fact[-1], q - 2, q)
    for n in range(q - 1, 0, -1):
        inv[n - 1] = inv[n] * n % q
    return fact, inv


def lucas_table(n: int, k: int, q: int, tab) -> int:
    fact, inv = tab
    out = 1
    while k:
        n, ni = divmod(n, q)
        k, ki = divmod(k, q)
        if ki > ni:
            return 0
        out = out * fact[ni] * inv[ki] * inv[ni - ki] % q
    return out


def lucas_direct(n: int, k: int, q: int) -> int:
    """Independent digit arithmetic, with exact math.comb per digit."""
    result = 1
    while n or k:
        ni, ki = n % q, k % q
        if ki > ni:
            return 0
        result = result * comb(ni, ki) % q
        n //= q
        k //= q
    return result


def generate():
    started = time.monotonic()
    small_primes = sieve(997)
    tabs = {q: tables(q) for q in small_primes}
    rows = []
    unresolved = []
    counts = collections.Counter()
    witness_counts = collections.Counter()
    primes_used = 0
    for p in sieve(LIMIT - 1):
        if p < 103:
            continue
        primes_used += 1
        ptab = None
        for d in (2, 3):
            j = p - d
            for k, l, B, A in candidates_generator(p, d):
                counts[d] += 1
                witness = None
                # First try small moduli. Larger p is only constructed if needed.
                for q in small_primes:
                    tab = tabs[q]
                    lhs = lucas_table(A, B, q, tab)
                    rhs = (lucas_table(p * p, 2 * p * d - d * d, q, tab)
                           + lucas_table(k * k, l * l, q, tab)) % q
                    if lhs != rhs:
                        witness = q
                        break
                if witness is None:
                    if ptab is None:
                        ptab = tables(p)
                    lhs = lucas_table(A, B, p, ptab)
                    rhs = (lucas_table(p * p, j * j, p, ptab)
                           + lucas_table(k * k, l * l, p, ptab)) % p
                    if lhs != rhs:
                        witness = p
                if witness is None:
                    unresolved.append([p, d, k, l])
                else:
                    rows.append([p, d, k, l, witness])
                    witness_counts[witness] += 1
        if primes_used % 200 == 0:
            print(json.dumps({"primes_processed": primes_used,
                              "last_p": p, "candidates": sum(counts.values()),
                              "unresolved": len(unresolved)}), flush=True)
    out = {
        "scope": {
            "prime_upper_index_less_than": LIMIT,
            "minimum_j": 100,
            "offsets": [2, 3],
            "minimum_l": 2,
            "branch": "B <= A-B",
            "lower_gap_condition": "B >= 3*j",
            "necessary_bands": {
                "d2": "4*j+5 <= B < (5 if j>=800 else 10)*j",
                "d3": "3*j+1 <= B < 4*j",
                "both": "2*B <= A",
            },
        },
        "candidate_count": sum(counts.values()),
        "by_offset": dict(counts),
        "certified_count": len(rows),
        "unresolved": unresolved,
        "witness_prime_counts": dict(witness_counts),
        "certificate_rows_p_d_k_l_q": rows,
        "generation_seconds": time.monotonic() - started,
    }
    CERTIFICATE.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("certificate_rows_p_d_k_l_q", "witness_prime_counts")},
                     ensure_ascii=False, indent=2))


def verify():
    started = time.monotonic()
    source = CERTIFICATE.read_bytes()
    data = json.loads(source)
    assert data["scope"]["prime_upper_index_less_than"] == LIMIT
    assert data["scope"]["minimum_j"] == 100
    assert data["scope"]["offsets"] == [2, 3]
    assert data["scope"]["minimum_l"] == 2
    rows = data["certificate_rows_p_d_k_l_q"]
    cert = {}
    for row in rows:
        assert len(row) == 5 and all(isinstance(x, int) for x in row)
        p, d, k, l, q = row
        key = (p, d, k, l)
        assert key not in cert, ("duplicate", key)
        cert[key] = q
    unresolved = set(map(tuple, data["unresolved"]))
    assert len(unresolved) == len(data["unresolved"])
    assert not unresolved.intersection(cert)
    checked_primes = set()
    count = 0
    by_offset = collections.Counter()
    witnesses = collections.Counter()
    missing = []
    for p in range(103, LIMIT, 2):
        if not prime_trial(p):
            continue
        for d in (2, 3):
            j = p - d
            for k, l, B, A in candidates_verifier(p, d):
                key = (p, d, k, l)
                count += 1
                by_offset[d] += 1
                if key in unresolved:
                    unresolved.remove(key)
                    missing.append(key)
                    continue
                assert key in cert, ("missing certificate", key)
                q = cert.pop(key)
                if q not in checked_primes:
                    assert prime_trial(q), ("nonprime modulus", q)
                    checked_primes.add(q)
                lhs = lucas_direct(A, B, q)
                rhs = (lucas_direct(p * p, j * j, q)
                       + lucas_direct(k * k, l * l, q)) % q
                assert lhs != rhs, ("invalid witness", key, q, lhs, rhs)
                witnesses[q] += 1
    assert not cert, ("extra certificates", len(cert))
    assert not unresolved, ("extra unresolved keys", len(unresolved))
    assert count == data["candidate_count"]
    assert count - len(missing) == data["certified_count"]
    assert dict(by_offset) == {int(k): v for k, v in data["by_offset"].items()}
    assert dict(witnesses) == {int(k): v for k, v in data["witness_prime_counts"].items()}
    report = {
        "verification_passed": not missing,
        "arithmetic": "Exact integers and Lucas congruences; no floating point.",
        "coverage": "Independent e-first enumeration with exact binomial binary searches.",
        "modular_arithmetic": "Independent math.comb evaluation of base-prime digits.",
        "candidate_count": count,
        "by_offset": dict(by_offset),
        "certified_count": count - len(missing),
        "unresolved_count": len(missing),
        "unresolved": missing,
        "distinct_witness_primes": len(checked_primes),
        "largest_witness_prime": max(checked_primes, default=None),
        "certificate_sha256": hashlib.sha256(source).hexdigest(),
        "verification_seconds": time.monotonic() - started,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
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
