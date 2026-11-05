#!/usr/bin/env python3
"""Exact certificates for the L1, b >= 3j, single-outer-top reduction.

This is a finite application of the uniform theorem in
v4_lower_l1_single_top.md.  It does not prove the full original problem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import time


def sieve(limit):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p:limit+1:p] = [False] * (((limit-p*p)//p)+1)
    return [p for p in range(2, limit + 1) if flags[p]]


PRIMES = sieve(101)
FACT = {}
for _p in PRIMES:
    _f = [1]
    for _a in range(1, _p):
        _f.append(_f[-1] * _a % _p)
    FACT[_p] = _f


def lucas_fast(n, k, p):
    """Generator: factorial tables and modular inverses per base-p digit."""
    if k < 0 or k > n:
        return 0
    f = FACT[p]
    answer = 1
    while k:
        a, b = n % p, k % p
        if b > a:
            return 0
        answer = answer * f[a] * pow(f[b] * f[a-b] % p, -1, p) % p
        n //= p
        k //= p
    return answer


def lucas_check(n, k, p):
    """Verifier: exact math.comb on digits, without factorial tables."""
    if k > n or k < 0:
        return 0
    product = 1
    while n or k:
        n, a = divmod(n, p)
        k, b = divmod(k, p)
        if b > a:
            return 0
        product = (product * comb(a, b)) % p
    return product


def nth_root_floor(n, k):
    """Exact integer root, with verified inequalities."""
    if k == 1:
        return n
    lo, hi = 0, 1 << ((n.bit_length() + k - 1) // k)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid
    assert lo ** k <= n < (lo + 1) ** k
    return lo


def smallest_outer_top(b):
    y = comb(b*b, 2*b-1)
    lo, hi = b*b*b // 4, b*b*b
    assert comb(lo, b) <= y < comb(hi, b)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if comb(mid, b) <= y:
            lo = mid
        else:
            hi = mid
    return hi


def representations_generate(a, b):
    """Enumerate effective indices until the central coefficient is too big."""
    result = set()
    m = 1
    while comb(2*m, m) <= a:
        lo, hi = 2*m, 2*m
        while comb(hi, m) < a:
            hi *= 2
        while lo < hi:
            mid = (lo + hi) // 2
            if comb(mid, m) < a:
                lo = mid + 1
            else:
                hi = mid
        if comb(lo, m) == a:
            for j in {m, lo-m}:
                if 1 <= j <= b//3 and lo-j >= 4:
                    result.add((lo, j))
        m += 1
    return sorted(result)


def representations_verify(a, b):
    """Independent effective-index and upper-index bounds for completeness."""
    result = set()
    for m in range(1, a.bit_length()):
        # C(2m,m) >= 2^m. Thus this range includes every possible m.
        if comb(2*m, m) > a:
            continue
        # A=C(i,m) >= (i-m+1)^m/m!, hence i <= m-1+floor((m!A)^(1/m)).
        left = 2*m
        right = m - 1 + nth_root_floor(factorial(m)*a, m)
        while left <= right:
            i = (left + right) // 2
            c = comb(i, m)
            if c < a:
                left = i + 1
            elif c > a:
                right = i - 1
            else:
                for j in (m, i-m):
                    if j >= 1 and 3*j <= b and i-j >= 4:
                        result.add((i, j))
                break
    return sorted(result)


def obstruction(a, b, i, j):
    for p in PRIMES:
        lhs = lucas_fast(a, b, p)
        rhs = (lucas_fast(i*i, j*j, p)
               + lucas_fast(b*b, 2*b-1, p)) % p
        if lhs != rhs:
            return p
    return None


def generate(start, stop, path):
    begin = time.monotonic()
    records = []
    unresolved = []
    nontrivial = []
    count = 0
    for b in range(start, stop+1):
        a = smallest_outer_top(b)
        representations = representations_generate(a, b)
        entries = []
        for i, j in representations:
            count += 1
            p = obstruction(a, b, i, j)
            if p is None:
                # An unresolved modular test is never silently excluded.
                equal = comb(a, b) == comb(i*i, j*j)+comb(b*b, 2*b-1)
                unresolved.append({"b": b, "i": i, "j": j,
                                   "exact_equality": equal})
            entries.append({"i": i, "j": j, "prime": p})
            if j != 1:
                nontrivial.append({"b": b, "A": a, "i": i, "j": j})
        records.append({"b": b, "A": a, "representations": entries})
        if b % 100 == 0:
            print(json.dumps({"progress_b": b, "representations": count,
                              "elapsed_seconds": round(time.monotonic()-begin, 3)}), flush=True)
    data = {"equation": "C(C(i,j),C(k,l)) = C(i^2,j^2)+C(k^2,l^2)",
            "scope": "L1: k=b, l=b-1, 1<=j<=floor(b/3), i-j>=4, b<=A/2",
            "range_b": [start, stop],
            "uniform_theorem": "v4_lower_l1_single_top.md",
            "families": len(records), "representations": count,
            "nontrivial_representations": nontrivial,
            "unresolved": unresolved, "records": records}
    path.write_text(json.dumps(data, indent=2)+"\n")
    print(json.dumps({"certificate": str(path), "families": len(records),
                      "representations": count,
                      "nontrivial_representations": nontrivial,
                      "unresolved": unresolved,
                      "elapsed_seconds": round(time.monotonic()-begin, 3)}), flush=True)


def verify(path, report_path):
    begin = time.monotonic()
    raw = path.read_bytes()
    data = json.loads(raw)
    start, stop = data["range_b"]
    assert 22 <= start <= stop
    for b in (22, 23, 24):
        e = b-1-2*(b//3)
        assert 32*factorial(b-1)*4**e < b**(3*e)
    assert 32*factorial(23)*4**7 < 22**21
    assert len(data["records"]) == stop-start+1
    assert not data["unresolved"], "Generator reported unresolved cases"
    count = 0
    max_prime = 0
    nontrivial = []
    for b, record in zip(range(start, stop+1), data["records"]):
        assert record["b"] == b
        a = record["A"]
        assert a >= b
        y = comb(b*b, 2*b-1)
        assert comb(a-1, b) <= y < comb(a, b)
        expected = representations_verify(a, b)
        supplied = [(v["i"],v["j"]) for v in record["representations"]]
        assert supplied == expected, (b, supplied, expected)
        assert len(supplied) == len(set(supplied))
        for entry in record["representations"]:
            i,j,p = entry["i"],entry["j"],entry["prime"]
            assert comb(i,j) == a
            assert isinstance(p,int) and p >= 2
            assert all(p % q for q in range(2,isqrt(p)+1))
            left = lucas_check(a,b,p)
            right = (lucas_check(i*i,j*j,p)+lucas_check(b*b,2*b-1,p)) % p
            assert left != right, (b,i,j,p)
            count += 1
            max_prime = max(max_prime,p)
            if j != 1:
                nontrivial.append({"b": b, "A": a, "i": i, "j": j})
    assert count == data["representations"]
    assert len(data["records"]) == data["families"]
    assert nontrivial == data["nontrivial_representations"]
    report = {"verified": True, "range_b": [start,stop],
              "families": stop-start+1, "representations": count,
              "nontrivial_representations": nontrivial,
              "max_obstruction_prime": max_prime,
              "unresolved": 0,
              "certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "elapsed_seconds": round(time.monotonic()-begin,3),
              "formal_proof_assistant_executed": False,
              "limitation": "Finite b range; uniform single-A theorem is a written proof, not a global exclusion."}
    report_path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report),flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["generate","verify"])
    parser.add_argument("--start",type=int,default=22)
    parser.add_argument("--stop",type=int,default=1000)
    parser.add_argument("--certificate",type=Path,default=Path("v4_lower_l1_single_top_certificates.json"))
    parser.add_argument("--report",type=Path,default=Path("v4_lower_l1_single_top_verification.json"))
    args = parser.parse_args()
    if args.action == "generate":
        assert 22 <= args.start <= args.stop
        generate(args.start,args.stop,args.certificate)
    else:
        verify(args.certificate,args.report)


if __name__ == "__main__":
    main()
