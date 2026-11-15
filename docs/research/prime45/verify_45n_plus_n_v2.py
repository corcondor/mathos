#!/usr/bin/env python3
"""Finite exact tests supporting the v2 paper proof for 45**n+n.

Uses only Python standard library; this is NOT a primality certificate nor a
formal proof of the paper's general theorems.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import gcd, lcm
import json

A = 45


def small_primes(bound: int) -> list[int]:
    arr = []
    for x in range(2, bound + 1):
        if all(x % p for p in arr if p * p <= x):
            arr.append(x)
    return arr


def prime_factors(x: int) -> list[int]:
    return [p for p in small_primes(x) if x % p == 0]


def order(p: int) -> int:
    assert p >= 2 and gcd(A, p) == 1 and p in small_primes(p)
    d = p-1
    for q in prime_factors(d):
        while d % q == 0 and pow(A, d//q, p) == 1:
            d //= q
    assert pow(A, d, p) == 1
    for q in prime_factors(d):
        assert pow(A, d//q, p) != 1
    return d


def Fmod(n: int, mod: int) -> int:
    return (pow(A, n, mod) + n) % mod


def lift_zero(p: int, r: int, e: int) -> tuple[int, int]:
    """One class n mod d*p**e where F(n)=0 (mod p**e)."""
    d = order(p)
    t = (-pow(A, r, p)-r)*pow(d, -1, p) % p
    n = r + d*t
    period = d*p
    for k in range(1, e):
        step = p**k
        residue = Fmod(n, p**(k+1)) // step
        j = -residue * pow(d, -1, p) % p
        n += j * period
        period *= p
        assert Fmod(n, p**(k+1)) == 0
    return n, period


def test_prime_power_uniformity() -> list[dict]:
    ans=[]
    for p in small_primes(23):
        for e in (1,2,3):
            q=p**e
            if A % p == 0:
                # The transient is harmless; for n >= e, F(n) == n mod q.
                cnt=Counter(Fmod(n,q) for n in range(e,e+q))
                assert len(cnt) == q and set(cnt.values()) == {1}
                expected=1
                length=q
            else:
                d=order(p)
                length=d*q
                cnt=Counter(Fmod(n,q) for n in range(length))
                assert len(cnt) == q and set(cnt.values()) == {d}
                expected=d
                for r in range(d):
                    n0, per=lift_zero(p,r,e)
                    assert per == length and Fmod(n0,q) == 0
            ans.append({'p':p,'power':e,'period_or_tail_length':length,'per_residue':expected})
    return ans


def test_sieve() -> dict:
    # All p <= 13. Their combined period equals 60,060.
    primes=small_primes(13)
    moduli=[p if A%p == 0 else p*order(p) for p in primes]
    L=lcm(*moduli)
    assert L == 60060
    good=bytearray([1])*L
    for p in primes:
        if A%p == 0:
            roots=[0]; per=p
        else:
            d=order(p)
            per=d*p
            roots=[r+d*((-pow(A,r,p)-r)*pow(d,-1,p)%p) for r in range(d)]
        for n0 in roots:
            for n in range(n0,L,per):
                good[n]=0
    density=Fraction(sum(good),L)
    product=Fraction(1,1)
    for p in primes:
        product*=Fraction(p-1,p)
    assert density == product == Fraction(192,1001)
    return {'all_primes_at_most_13':primes,'combined_period':L,
            'survivors':sum(good),'exact_density':str(density)}


def test_2027_lifts() -> list[dict]:
    p=2027
    assert p in small_primes(p)
    d=order(p)
    assert d == 2026
    seq=[]
    for k,n in [(1,2),(2,4106704),(3,1706482522274)]:
        root, period=lift_zero(p,2,k)
        assert n==root and Fmod(n,p**k)==0
        seq.append({'p_power':k,'exponent_n':n,'residue_modulus':period})
    assert Fmod(2, p*p) != 0
    assert Fmod(4106704, p**3) != 0
    return seq


def test_polynomial_and_gcd() -> dict:
    for p in (7,11,13,19,23):
        x=p-1
        for q in (x-1,x,x*x+1):
            n=x+x*(x+1)*q
            assert n>0 and n%(p-1)==0 and n%p==p-1
            assert Fmod(n,p)==0
        for k in (1,2,3,4):
            n=p**k-1
            assert Fmod(n,p)==0
    n=21
    a=Fmod(n,44*n-1)
    g=gcd(a,44*n-1)
    assert g==13
    assert 44*n-1 == 923
    for n in (1,2,3,4,5,15,27,45,3878,9424):
        z=n
        for p in (3,5):
            while z%p==0:z//=p
        smooth=n//z
        assert gcd(Fmod(n,n) if n>1 else 0,n) == smooth if n>1 else True
    return {'P_polynomial_samples':'PASS', 'gcd_F21_F22':g}


def main() -> dict:
    powers=test_prime_power_uniformity()
    sieve=test_sieve()
    lifts=test_2027_lifts()
    pol=test_polynomial_and_gcd()
    return {'status':'PASS finite exact modular tests; NOT an infinite theorem certification',
            'prime_power_uniformity_checks':len(powers),'prime_powers':powers,
            'sieve':sieve,'2027_lifts':lifts,'polynomial_and_gcd':pol}


if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
