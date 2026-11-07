#!/usr/bin/env python3
"""Exact finite checks for the written global n < 2^(24 delta) theorem.

No floating-point logarithms, arbitrary scan, remote API, or Lean invocation.
The quantified mathematical arguments are in v20_binary_height_24.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


DIM=7


def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items():
            out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c}


def mul(p,q):
    out={}
    for a,x in p.items():
        for b,y in q.items():
            m=tuple(u+v for u,v in zip(a,b))
            out[m]=out.get(m,F(0))+x*y
    return {m:c for m,c in out.items() if c}


def scale(p,c):
    return {m:v*c for m,v in p.items() if v*c}


def constant(c):
    return {(0,)*DIM:F(c)} if c else {}


def variable(i):
    m=[0]*DIM;m[i]=1
    return {tuple(m):F(1)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args=parser.parse_args()
    N0=2**600
    lam=F(693147,10**6)
    alpha=F(231,500)
    xmax=alpha/(600*lam)
    records=[]

    def positive(label,value,expected=None):
        value=F(value)
        if expected is not None:
            assert value==F(expected),(label,value,expected)
        assert value>0,(label,value)
        records.append({"label":label,"positive_margin":str(value)})

    def identity(label,p,q):
        assert add(p,scale(q,-1))=={},label
        records.append({"label":label,"coefficient_identity":True})

    # Coefficient identities use formal variables:
    # n, L=log(n), x, log(2), log(3), ell=log(3+x), D=log(4*e*b).
    n,L,x,l2,l3,ell,D=[variable(i) for i in range(DIM)]
    three_plus_x=add(constant(3),x)
    f3x=mul(three_plus_x,add(constant(1),scale(l2,-1),scale(l3,-1),scale(ell,-1)))
    f3=scale(add(constant(1),scale(l2,-1),scale(l3,-2)),3)
    direct=add(mul(mul(three_plus_x,n),add(constant(1),scale(L,2),scale(l2,-1),scale(l3,-1),scale(ell,-1))),
               scale(three_plus_x,-4),scale(D,-1),
               scale(mul(n,add(constant(1),L,scale(l2,-1),scale(l3,-1))),-6))
    proposed=add(mul(n,add(scale(l2,3),constant(-F(519,250)),f3x,scale(f3,-1))),
                 scale(three_plus_x,-4),scale(D,-1))
    relation=mul(n,add(scale(mul(x,L),2),constant(-2*alpha)))
    identity("logarithmic_binomial_comparison_with_2xL_equals_2alpha",
             add(direct,scale(proposed,-1)),relation)

    # Clear L*(n-1) in the rational-function identity for the defect bound.
    L2=mul(L,L)
    lhs=add(mul(mul(add(scale(L,3),constant(alpha)),
                       add(scale(L,3),constant(alpha))),n),
            scale(mul(L2,n),-9),scale(L2,9))
    rhs=add(mul(add(scale(L,6*alpha),constant(alpha*alpha)),n),scale(L2,9))
    identity("intrinsic_defect_finite_n_identity",lhs,rhs)

    partial=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(6)),F(0))
    positive("six_term_integral_series_log2_lower",partial-lam,
             F(335369,4546773000000))
    positive("truncated_exp_log2_upper",
             sum((F(7,10)**j/F(factorial(j)) for j in range(4)),F(0))-2,
             F(13,6000))
    assert 600*lam==F(2079441,5000)
    assert xmax==F(110,99021)
    positive("x_less_than_one_percent",F(1,100)-xmax)
    positive("binomial_bracket_exceeds_one_ten_thousandth",
             3*lam-F(519,250)-3*xmax-F(1,10000),
             F(276387,33007000000))
    positive("log_6y_less_than3",F(8,3)**3-6*F(301,100))
    positive("log48_less_than4",F(8,3)**4-48)
    positive("A_greater_than_n_cubed_over7_threshold",N0-21)
    positive("n_cubed_over7_greater_than16n_squared_threshold",N0-112)
    positive("ceil_a_less_than4n",F(99,100)*N0-1)
    positive("four_times_3_plus_x_less_than13",13-4*F(301,100))
    positive("positive_log_binomial_ratio_at_threshold",F(N0,10000)-437)
    positive("ratio_bound_increases_above_threshold",F(1,10000)-F(1,N0))
    positive("alpha_squared_over_L_bound",F(257,500000)-alpha*alpha/(600*lam),
             F(12799,16503500000))
    positive("nine_log_n_over_n_endpoint",N0-9*420*10**6)
    positive("n_over_nminus1_correction",F(1000001,1000000)-F(N0,N0-1))
    beta=6*(6*alpha+F(257,500000)+F(1,10**6))*F(1000001,1000000)
    assert beta==F(1663510663509,10**11)
    positive("high_n_coefficient_less_than24log2",24*lam-beta,
             F(42136491,10**11))
    assert 24*25==600
    records.append({"label":"entire_low_n_range_covered_by_delta_ge_25",
                    "integer_identity":"24*25=600"})

    note=Path(__file__).with_suffix(".md")
    result={
        "status":"PASS",
        "date_jst":"2026-11-07",
        "scope":"Exact constants/algebra for the written global binary-height theorem",
        "theorem":"Every original solution in ell=1,j=i-3 satisfies n < 2^(24*delta)",
        "upper_gap":"t < 231*n/(500*log(n)) for n>=2^600",
        "threshold_bits":600,
        "inherited_delta_lower_bound":25,
        "log2_rational_lower":str(lam),
        "high_n_only_natural_log_coefficient":str(beta),
        "check_count":len(records),
        "checks":records,
        "note_sha256":sha256(note.read_bytes()).hexdigest(),
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "limits":[
            "The coefficient beta is a high-n bound, not a claimed global rational log-height constant",
            "The global low-n range uses existing delta>=25; no new finite delta scan is used",
            "Integral, monotonicity, and ceil arguments are written proofs rather than Lean certificates",
            "No floating-point logarithm, arbitrary n scan, remote proof API, or original-equation solution is asserted"]}
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","theorem","upper_gap","check_count","note_sha256","checker_sha256"]},indent=2))


if __name__=="__main__":
    main()
