#!/usr/bin/env python3
"""v106: exact modular audit of close-prime-free certificates and 2-prime CRT.

This script NEVER searches the original integer i. For small k=7,41,
it detects NO-NONZERO-ROOT property of Fq polynomial via polynomial
Euclidean gcd, not testing every i or even enumerating x in Fq.

For k=99,819,821 it tests the universal q-unit self-similarity
    R_k/q == 2*d/R_(d+1) modulo q
and the two-prime CRT residues that contradict 1<=m<k.

The complete *unbounded* proofs are in
V106_ARBITRARY_FACTOR_CERTIFICATE_AND_TWO_PRIME_CRT_ja.md.
No amount of finite CI testing implies the universal proof or solves
the original unrestricted four-variable equation.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
import argparse


def isprime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_rem(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim([x % p for x in a.copy()])
    b = trim([x % p for x in b.copy()])
    assert b != [0]
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        u = a[-1] * inv % p
        shift = len(a) - len(b)
        for i in range(len(b)):
            a[i + shift] = (a[i + shift] - u * b[i]) % p
        trim(a)
    return a


def mulmod(a: list[int], b: list[int], f: list[int], p: int) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return poly_rem(c, f, p)


def x_to_qminus1_minus1(f: list[int], q: int) -> list[int]:
    a, b, e = [1], poly_rem([0, 1], f, q), q - 1
    while e:
        if e & 1:
            a = mulmod(a, b, f, q)
        e //= 2
        if e:
            b = mulmod(b, b, f, q)
    a[0] = (a[0] - 1) % q
    return trim(a)


def poly_gcd(a: list[int], b: list[int], q: int) -> list[int]:
    a, b = trim(a.copy()), trim(b.copy())
    while b != [0]:
        a, b = b, poly_rem(a, b, q)
    if a == [0]:
        return a
    inv = pow(a[-1], -1, q)
    return [(x * inv) % q for x in a]


def forced_polynomial(k: int, q: int) -> list[int]:
    """G_k(X)=product_{t=1}^{k-1}(X-t)-k!*X in Fq[X]."""
    a = [1]
    for t in range(1, k):
        b = [0] * (len(a) + 1)
        for i, z in enumerate(a):
            b[i] = (b[i] - t * z) % q
            b[i + 1] = (b[i + 1] + z) % q
        a = b
    a[1] = (a[1] - math.factorial(k)) % q
    return trim(a)


def q_forced(k: int, q: int, R: int) -> bool:
    assert q > k and isprime(q)
    if R % q:
        return False
    G = forced_polynomial(k, q)
    return poly_gcd(G, x_to_qminus1_minus1(G, q), q) == [1]


def D(d: int) -> int:
    return math.comb((d + 1)**2, 2*d + 1)


def unit_identity(k: int, d: int, R: int) -> dict:
    q = k + d
    assert k % 2 == 1 and d % 2 == 0 and d >= 2
    assert isprime(q) and q > (d + 1)**2
    assert R % q == 0
    assert D(d) < q**D(d).bit_length()  # harmless very weak positivity check
    assert ((R // q) * D(d) - 2*d) % q == 0
    return {"k": k, "q": q, "d": d, "D_d": D(d),
            "R_over_q_mod_q": (R // q) % q}


def two_primes(k: int, d1: int, d2: int) -> dict:
    assert k % 2 == 1 and 2 <= d1 < d2 and d1 % 2 == d2 % 2 == 0
    q1, q2 = k + d1, k + d2
    assert isprime(q1) and isprime(q2)
    assert k > max(2**(d1 - 1) + d1*d1 + d1 + 1,
                   2**(d2 - 1) + d2*d2 + d2 + 1)
    R = math.comb(k*k, 2*k-1)
    U1, U2 = unit_identity(k, d1, R), unit_identity(k, d2, R)
    Q = q1*q2
    assert R % Q == 0 and k*k < Q
    h = d2-d1
    a = Fraction(2*d1*d1, h*D(d1))
    b = Fraction(2*d2*d2, h*D(d2))
    assert 0 < a < 1 and 0 < b < 1
    m1 = -a.numerator * pow(a.denominator, -1, q1) % q1
    m2 = b.numerator * pow(b.denominator, -1, q2) % q2
    S = R // Q
    actual = k*S % Q
    assert m1 == actual % q1 and m2 == actual % q2
    finite_b = a.denominator*b.denominator*(h+a+b)
    assert finite_b.denominator == 1
    # The mathematical implication: ANY putative solution must satisfy q1<finite_b.
    # This is NOT a brute-force bound or a claim that this particular k is >bound.
    return {"k": k, "primes": [q1,q2], "offsets": [d1,d2],
            "a": str(a), "b": str(b), "derived_strict_q1_upper": finite_b.numerator,
            "m_mod_q1": m1, "m_mod_q2": m2,
            "remaining_m_if_eq": m1 if m1 == m2 and 0 < m1 < k else None,
            "discharged_by_crt_collision": m1 != m2,
            "R_bits": R.bit_length(),
            "unit_checks": [U1,U2]}


def verify() -> dict:
    # Unlike v105, NO restriction on the distance q-k in this certificate.
    nonlocal_rows=[]
    for k, pair in [(7,[41,43]), (41,[1601,1609])]:
        R=math.comb(k*k,2*k-1)
        root_flags=[q_forced(k,q,R) for q in pair]
        assert all(root_flags)
        product=math.prod(pair)
        assert product > k**3
        nonlocal_rows.append({"k":k,"primes":pair,
                              "root_free_over_each_Fq":root_flags,
                              "factor_product":product,"height_k_cubed":k**3,
                              "result":"NO SOLUTION FOR ANY i"})
    # k even: X=-1 is automatically a nonzero root, and the forced-gcd
    # criterion does not apply; test this boundary explicitly.
    assert forced_polynomial(8,11)[0] != 0
    f=forced_polynomial(8,11)
    assert sum(c*pow(10,j,11) for j,c in enumerate(f))%11==0

    pair_rows=[two_primes(k,d1,d2) for k,d1,d2 in
               [(99,2,4),(819,2,4),(821,2,6)]]
    assert all(z["discharged_by_crt_collision"] for z in pair_rows)
    assert pair_rows[-1]["m_mod_q1"]==209
    assert pair_rows[-1]["m_mod_q2"]==545
    assert pair_rows[0]["derived_strict_q1_upper"]==261501808
    assert pair_rows[2]["derived_strict_q1_upper"]==33218493146713
    return {"status":"PASS_EXACT_V106_NONLOCAL_AND_CRT",
            "scope":"original j=1, ell=k-1, odd k; all k theorem is written, NOT Lean formalized",
            "nonclose_factor_examples":nonlocal_rows,
            "fixed_two_prime_CRT_examples":pair_rows,
            "global_formula":"R_k/(k+d) mod(k+d) = 2d / C((d+1)^2,2d+1)",
            "local_polynomial_test":"gcd_Fq(G_k(X), X^(q-1)-1)=1",
            "full_original_equation_resolved":False}


if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--output",type=Path)
    o=arg.parse_args()
    data=verify()
    print("V106_RESULT",json.dumps(data,ensure_ascii=False),flush=True)
    if o.output:
        o.output.parent.mkdir(parents=True,exist_ok=True)
        o.output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
