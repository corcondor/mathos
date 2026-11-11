#!/usr/bin/env python3
"""v103: Verify the exact p-adic unit finite-difference identity and digit lift.

For ALL primes p, a>=1, k=p**a, 0<=r<k, q>=0, t>=0,
G_r(q+p**t)-G_r(q) == p**t (mod p**(t+1)).
Proved for all parameters by Vandermonde + prime-power valuation.
The script checks some exact integer instances, not all integers.

For n>=1, q_n is THE UNIQUE root of G_r(q)=0 mod p**n.
This computes q_(2a) with 2a digit lifts, never scanning every q/i.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def residual(k: int, r: int, q: int, R: int) -> int:
    i = k*q + r
    return math.comb(i, k) - i*i - R


def unique_lift(p: int, a: int, r: int) -> dict:
    assert a >= 1 and 0 <= r < p**a
    k = p**a
    R = math.comb(k*k, 2*k-1)
    assert R % (k*k) == 0
    q = r*r % p
    digits = [q]
    assert residual(k, r, q, R) % p == 0
    for n in range(1, 2*a):
        pn = p**n
        G = residual(k, r, q, R)
        assert G % pn == 0
        d = (-G // pn) % p
        q += d * pn
        digits.append(d)
        assert 0 <= q < p**(n+1)
        assert residual(k, r, q, R) % p**(n+1) == 0
    assert 0 <= q < k*k
    return {"p":p,"a":a,"k":k,"r":r,"q_unique":q,"i_unique":k*q+r,
            "digits_low_to_high":digits,"modulus":k*k}


def verify() -> dict:
    prime_powers = [(2,1),(2,2),(2,3),(3,1),(3,2),
                    (5,1),(5,2),(7,1),(11,1),(13,1)]
    checked_differences = 0
    checked_lifts = 0
    roots = []
    for p,a in prime_powers:
        k=p**a
        R=math.comb(k*k,2*k-1)
        for r in sorted({0,1,min(2,k-1),k//2,max(0,k-2),k-1}):
            for q in (0,1,2,5):
                for t in range(0,2*a+2):
                    M=p**(t+1)
                    jump=residual(k,r,q+p**t,R)-residual(k,r,q,R)
                    assert jump%M==p**t
                    checked_differences+=1
            z=unique_lift(p,a,r)
            checked_lifts+=1
            roots.append(z)
            if a==1 and p>=5:
                if r==1:
                    assert z["q_unique"]==p+1
                if r==p-1:
                    assert z["q_unique"]==p*p-4*p+1
    assert checked_differences>500
    assert checked_lifts>30
    return {"status":"PASS_MODULAR_IDENTITY_SANITY",
            "scope":"selected exact finite checks; proof for ALL p,a,q,r,t in v103 written theorem",
            "sample_prime_powers":prime_powers,
            "verified_exact_jumps":checked_differences,
            "verified_exact_lifts":checked_lifts,
            "sample_roots":roots,
            "not_verified":"all-prime-powers Lean kernel theorem or unrestricted original equation"}

if __name__=="__main__":
    pa=argparse.ArgumentParser()
    pa.add_argument("--output",type=Path)
    x=pa.parse_args()
    report=verify()
    print("V103_RESULT",json.dumps({k:v for k,v in report.items() if k!="sample_roots"},ensure_ascii=False),flush=True)
    if x.output:
        x.output.parent.mkdir(parents=True,exist_ok=True)
        x.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
