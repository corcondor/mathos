#!/usr/bin/env python3
"""v109: root-agnostic TWO-prime CRT and square-window polynomial-gcd certificates.

Mathematical theorem in V109_ANY_ROOT_TWO_PRIME_CRT_AND_SQUARE_WINDOW_DEGREE_REDUCTION_ja.md.

NO search over the original integer i (which can be as large as k^3).
1. Reduce q|R_k via one small square-window digit k² mod q <2k-1.
2. Classify ALL finite-field roots using polynomial Euclid:
   gcd(G_k(X), X^(q-1)-1).  Verify a complete factorization, not
   approximate samples.
3. Convert i=a+q*t, with t in {0,1,...,k+2}, and prove
   gcd(prod_(admissible t)(Z-t), D_k(a+qZ))=1 over F_p.
4. Independently assemble all CRT classes of the two prime fields,
   showing none lies in the strictly proved height 2k<i<k³.

These are exact finite arithmetic *certificates for selected k*, not a
universal theorem that two primes can always be chosen.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from v106_nonlocal_prime_units_audit import (
    forced_polynomial, isprime, poly_gcd, x_to_qminus1_minus1,
)


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def from_linear_roots(roots: list[int], p: int) -> list[int]:
    prod=[1]
    for a in roots:
        prod=poly_mul(prod, [(-a)%p, 1],p)
    return prod


def certified_local_roots(k: int, q: int, claimed: list[int]) -> dict:
    """Full root classification by GCD in Fq[X], not residue enumeration."""
    assert isprime(q) and q>2*k-1
    assert 0 in claimed and len(claimed)==len(set(claimed))
    assert all(0<=x<q for x in claimed)
    assert k*k%q <2*k-1, "q must divide R_k"
    g=forced_polynomial(k,q)
    gcd=poly_gcd(g, x_to_qminus1_minus1(g,q),q)
    expected=from_linear_roots([r for r in claimed if r!=0],q)
    assert gcd==expected, (k,q,gcd,expected)
    return {"q":q,"root_set":claimed,
            "nonzero_gcd_degree":len(gcd)-1,
            "monic_fermat_gcd_coefficients_low_to_high":gcd,
            "num_possible_residues":len(claimed)}


def two_prime_crt(q1:int, A:list[int], q2:int, B:list[int]) -> tuple[int,list[int]]:
    assert q1!=q2
    Q=q1*q2
    inv=pow(q1,-1,q2)
    reps=sorted({a+q1*((b-a)*inv%q2) for a in A for b in B})
    assert len(reps)==len(A)*len(B)
    assert all(0<=x<Q for x in reps)
    assert all(x%q1 in A and x%q2 in B for x in reps)
    return Q,reps


def low_degree_reduction(k:int,q:int,p:int,root_a:int) -> dict:
    """Prove polynomial gcd=1 on all t such that i=a+qt is in 2k<i<k³."""
    assert isprime(q) and isprime(p) and p!=q and p>2*k-1
    assert (k-1)**2<q<k*k
    assert q>= k*k-2*k+2
    assert (k+3)*(k*k-2*k+2)>k**3
    assert 0<=root_a<q
    assert p>k+2

    admissible=[t for t in range(k+3) if 2*k<root_a+q*t<k**3]
    lo= min(admissible) if admissible else None
    hi= max(admissible) if admissible else None
    P=from_linear_roots(admissible,p)

    D=[1]
    for j in range(k):
        D=poly_mul(D, [(root_a-j)%p, q%p],p)
    fact=math.factorial(k)%p
    if len(D)<3:
        D += [0]*(3-len(D))
    D[0]=(D[0]-fact*root_a*root_a)%p
    D[1]=(D[1]-2*fact*root_a*q)%p
    D[2]=(D[2]-fact*q*q)%p
    while len(D)>1 and D[-1]==0:D.pop()

    gcd=poly_gcd(P,D,p)
    assert gcd==[1],(k,q,p,root_a,admissible,gcd)
    return {"a":root_a,
            "quotient_t_interval":[lo,hi],
            "t_polynomial_degree":len(P)-1,
            "binomial_shift_polynomial_degree":len(D)-1,
            "gcd_over_second_prime":[1],
            "original_i_examined_individually":False}


CASES=[
    (6,29,[0,28],31,[0,11,30],[0,290,434,464,724,898]),
    (9,79,[0],23,[0],[0]),
    (14,191,[0,62,190],181,[0,170,180],
       [0,3247,3438,5792,9039,9230,31132,34379,34570]),
    (8,59,[0,58],61,[0,60],[0,1769,1829,3598]),
]


def verify():
    allcases=[]
    for k,q,A,p,B,expected_reps in CASES:
        first=certified_local_roots(k,q,A)
        second=certified_local_roots(k,p,B)
        Q,reps=two_prime_crt(q,A,p,B)
        assert reps==expected_reps,(k,reps,expected_reps)
        assert Q>k**3
        assert not any(2*k<x<k**3 for x in reps)
        direct_reduction=[low_degree_reduction(k,q,p,a) for a in A]
        allcases.append({
            "k":k,"primes":[q,p],"square_window_first_prime":True,
            "R_divisible_both":"exactly certified by k² mod q < 2k−1",
            "roots":[first,second],
            "CRT_modulus":Q,"CRT_all_representatives":reps,
            "least_positive_representative":min(x for x in reps if x>0),
            "exclusive_i_upper_bound":k**3,
            "small_degree_gcd_certificates":direct_reduction,
            "conclusion":"NO ORIGINAL SOLUTION FOR ANY i, conditional on v101 global height"
        })
    k14=next(x for x in allcases if x["k"]==14)
    assert all(len(x['root_set'])>2 for x in k14['roots'])
    k6=next(x for x in allcases if x["k"]==6)
    assert k6["least_positive_representative"]==290>216
    return {
      "status":"PASS_V109_TWO_PRIME_ROOT_AGNOSTIC_AND_DEGREE_REDUCTION",
      "scope":"four selected k values; general two-prime and square-window theorems in written proof",
      "all_prime_root_sets_complete_via_fermats_polynomial_gcd":True,
      "root_free_primes_NOT_required":True,
      "cases":allcases,
      "all_k_j1_ell_kminus1_solved":False,
      "whole_four_variable_equation_solved":False,
      "next_missing_theorem":"existence of a suitable CRT-collision certificate for every unbounded k; not proved"
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    data=verify()
    print("V109_RESULT",json.dumps({k:v for k,v in data.items() if k!='cases'},ensure_ascii=False),flush=True)
    for row in data['cases']:
        print("V109_CASE",json.dumps({k:v for k,v in row.items() if k!='small_degree_gcd_certificates'},ensure_ascii=False),flush=True)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
