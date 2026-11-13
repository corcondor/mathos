#!/usr/bin/env python3
"""v107 - exact one-prime compression & p-adic roots (no enumeration of i).

Mathematical proof:
  V107_UNIVERSAL_LARGE_TO_SMALL_PRIME_COMPRESSION_ja.md

For q>m=2*k-1 prime with q|R_k, k*k=A*q+b, b<m,
  (R_k/q) mod q**t
    = A * product_{h!=b}(A*q+b-h) * inverse(m!) mod q**t.
The test compares this *small factor product* with the actual
huge integer, independently, for selected witnesses.

Use the finite-field polynomial gcd to prove f(X)=C(X,k)-X² has
only residue 0 (odd k) or 0,-1 (even k) modulo one chosen q.
For each simple residue, perform standard q-adic Newton digit lifts
mod q² and q³, and compare the one candidate with the rigorously
proved original height i<k³. NOT a search over i or over q.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from v106_nonlocal_prime_units_audit import (
    isprime, forced_polynomial, poly_gcd, x_to_qminus1_minus1,
)


def short_unit(k: int, q: int, precision: int) -> dict:
    assert isprime(q) and q > 2*k-1 and precision >= 1
    n = k*k
    m = 2*k-1
    A, b = divmod(n, q)
    assert A > 0 and 0 <= b < m and n < q*q
    mod = q**precision
    prod = A % mod
    for h in range(m):
        if h != b:
            prod = prod*(A*q+b-h) % mod
    unit = prod*pow(math.factorial(m), -1, mod) % mod
    # A second formula only for the first q-adic unit digit:
    if precision == 1:
        one_digit = ((-1)**b * A
             * pow(m*math.comb(m-1,b), -1, q))%q
        assert unit == one_digit
    return {"A":A,"b":b,"modulus":mod,"unit":unit}


def fmod(k: int, i: int, modulus: int) -> int:
    falling = 1
    for j in range(k):
        falling = falling*(i-j)%modulus
    return (falling*pow(math.factorial(k),-1,modulus)-i*i)%modulus


def fprime_mod(k: int, x: int, q: int) -> int:
    factors = [(x-j)%q for j in range(k)]
    prefix = [1]
    for val in factors:
        prefix.append(prefix[-1]*val%q)
    total = 0
    suffix = 1
    for j in range(k-1,-1,-1):
        total = (total+prefix[j]*suffix)%q
        suffix = suffix*factors[j]%q
    return (total*pow(math.factorial(k),-1,q)-2*x)%q


def lift(k: int, q: int, root: int, quot_units: dict) -> dict:
    assert 0 <= root < q and fmod(k,root,q)==0
    derivative=fprime_mod(k,root,q)
    assert derivative != 0, ("singular-root",k,q,root)
    x=root
    lifts=[root]
    digits=[]
    for t in (1,2):
        mod=q**(t+1)
        # precision 1 is sufficient for R mod q², precision 2 for mod q³.
        Rmod=q*quot_units[t] % mod
        old=fmod(k,x,mod)
        assert (Rmod-old)%(q**t)==0
        digit=(((Rmod-old)//(q**t))*pow(derivative,-1,q))%q
        x+=digit*q**t
        assert 0<=x<mod
        assert fmod(k,x,mod)==Rmod
        digits.append(digit)
        lifts.append(x)
    return {"root_mod_q":root,"f_prime_mod_q":derivative,
            "hensel_digits":digits,
            "unique_mod_q2":lifts[1],
            "unique_mod_q3":lifts[2],
            "q2_exceeds_k3":q*q>k**3,
            "q2_root_too_large":lifts[1]>=k**3,
            "q3_root_too_large":lifts[2]>=k**3}


def one_prime(k: int, q: int) -> dict:
    assert k>=4 and isprime(q) and q>2*k-1
    unit1=short_unit(k,q,1)
    unit2=short_unit(k,q,2)
    R=math.comb(k*k,2*k-1)
    assert R%q==0
    assert R//q%q==unit1["unit"]
    assert R//q%(q*q)==unit2["unit"]
    # No enumeration of even one i: one finite-field polynomial gcd.
    G=forced_polynomial(k,q)
    g=poly_gcd(G,x_to_qminus1_minus1(G,q),q)
    if g==[1]:
        roots=[0]
        claimed="nonzero residue roots absent"
    elif g==[1,1]:
        assert k%2==0
        roots=[0,q-1]
        claimed="only nonzero root is -1"
    else:
        return {"k":k,"q":q,"small_unit":unit1,"gcd":g,
                "status":"NOT_CERTIFIED_BY_THIS_TWO_ROOT_CHECK"}
    if k%2==0:
        H=sum(pow(t,-1,q) for t in range(1,k+1))%q
        assert fprime_mod(k,q-1,q)==(2-H)%q
    assert fprime_mod(k,0,q)==((-1)**(k-1)*pow(k,-1,q))%q
    data=[lift(k,q,r,{1:unit1["unit"],2:unit2["unit"]}) for r in roots]
    assert q**3>k**3
    if q*q>k**3:
        assert all(x["q2_root_too_large"] for x in data), data
    else:
        assert all(x["q3_root_too_large"] for x in data), data
    return {
        "k":k,"q":q,"k_cubed":k**3,
        "q_modular_cubic_bound":q**3,
        "binomial_R_bits":R.bit_length(),
        "digits_of_k_squared": [unit1["A"],unit1["b"]],
        "R_over_q_mod_q":unit1["unit"],
        "R_over_q_mod_q2":unit2["unit"],
        "gcd_G_with_X_q_minus1":g,
        "modular_root_classification":claimed,
        "lifts":data,
        "conclusion":"NO EXACT INTEGER SOLUTIONS FOR ANY i",
        "audit_scope":"exact finite-field polynomial-gcd certificate, NOT a universal q-root-free theorem",
    }


def remainder_mod_x2_minus_b(b: int) -> tuple[int,int]:
    """Reduce P_b(X)=prod_(s=1)^(b+1)(2X-s) modulo X²-b over Z."""
    aa,bb=0,1
    for s in range(1,b+2):
        # (aa X+bb)*(2X-s) mod X²=b
        aa,bb=(-s*aa+2*bb), (2*b*aa-s*bb)
    assert aa or bb
    return aa,bb


def check_fixed_offset_identity() -> dict:
    alpha,beta=remainder_mod_x2_minus_b(2)
    assert (alpha,beta)==(38,-54)
    cases=[]
    for k in (9,43,47):
        q=k*k-2
        assert isprime(q)
        S=short_unit(k,q,1)["unit"]
        assert (((19*k-27)*S-1)%q)==0
        M=(k*S)%q # odd k, possible i/q from q-divisibility
        tnum=(19*k-27)*M-k
        assert tnum%q==0
        cases.append({"k":k,"q":q,"candidate_if_q_divides_i":M,
                      "integer_t":tnum//q,
                      "actual_height_ratio_numerator":M*q,
                      "k_cubed":k**3})
    return {"fixed_offset":2,"polynomial_remainder":[alpha,beta],
            "candidate_sample":cases,
            "all_large_k_theorem":"t converges to irrational 19e/4 if any infinite original solution sequence has q=k²-2 prime and q|i"}


def verify():
    rows=[one_prime(k,q) for k,q in
          [(5,23),(6,29),(10,89),(41,1601),(43,1847)]]
    assert all(row["conclusion"]=="NO EXACT INTEGER SOLUTIONS FOR ANY i" for row in rows)
    k6=next(row for row in rows if row["k"]==6)
    assert [x["unique_mod_q2"] for x in k6["lifts"]]==[348,782]
    k41=next(row for row in rows if row["k"]==41)
    assert k41["lifts"][0]["unique_mod_q2"]==1013433
    fixed=check_fixed_offset_identity()
    return {
        "status":"PASS_EXACT_V107_ONE_PRIME_COMPRESSION",
        "scope":"specified one-prime cases; universal quotient and fixed-offset irrational theorem are written, not Lean-checked",
        "prime_witness_count":len(rows),
        "root_lift_certificates":sum(len(row["lifts"]) for row in rows),
        "all_cases_contradict_i_less_than_k_cubed":True,
        "witnesses":rows,
        "fixed_offset_remainder":fixed,
        "full_four_variable_problem_solved":False,
    }


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=verify()
    print("V107_RESULT",json.dumps({k:v for k,v in report.items() if k!="witnesses"},ensure_ascii=False),flush=True)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
