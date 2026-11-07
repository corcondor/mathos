#!/usr/bin/env python3
"""Exact constants and polynomial algebra for the written v20 analytic proof.

No floating-point logarithms, numerical binomial approximations, arbitrary n
scan, SymPy, Lean, or remote proof API is used. The integral/monotonicity
arguments are in the companion note; these finite checks are not a substitute
for those quantified arguments.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


def plus(*polys):
    result={}
    for p in polys:
        for monomial, coefficient in p.items():
            result[monomial]=result.get(monomial,Q(0))+coefficient
    return {m:c for m,c in result.items() if c}


def scale(poly,k):
    return {m:c*k for m,c in poly.items() if c*k}


def multiply(p,q):
    result={}
    for a,x in p.items():
        for b,y in q.items():
            m=tuple(u+v for u,v in zip(a,b))
            result[m]=result.get(m,Q(0))+x*y
    return {m:c for m,c in result.items() if c}


def const(k):
    return {(0,0,0,0):Q(k)} if k else {}


def var(i):
    m=[0,0,0,0];m[i]=1
    return {tuple(m):Q(1)}


def poly_value(coefficients,x):
    return sum((Q(c)*x**i for i,c in enumerate(coefficients)),Q(0))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args=parser.parse_args()
    records=[]

    def positive(label,value,expected=None):
        value=Q(value)
        if expected is not None:
            assert value==Q(expected),(label,value,expected)
        assert value>0,(label,value)
        records.append({"label":label,"positive_margin":str(value)})

    def identity(label,left,right):
        assert plus(left,scale(right,-1))=={},label
        records.append({"label":label,"coefficient_identity":True})

    # Four formal independent variables n, log(n), log(2), log(3).
    n,L,l2,l3=[var(i) for i in range(4)]
    m=plus(scale(n,6),const(-9))
    numerator=plus(multiply(n,n),scale(n,-6),const(10))
    identity("binomial_ratio_margin",
             plus(scale(numerator,6),scale(multiply(plus(n,const(-5)),m),-1)),
             plus(scale(n,3),const(15)))
    identity("product_loss_is_less_than_31",
             plus(scale(plus(n,const(-5)),31),scale(m,-5)),
             plus(n,const(-110)))
    D=plus(scale(L,2),const(1),scale(l2,-1),scale(l3,-2))
    lower=plus(multiply(m,plus(const(1),L,scale(l2,-1),scale(l3,-1))),
               const(-32),scale(l2,-1),scale(l3,-1),scale(L,-1),
               scale(multiply(n,D),-3))
    simplified=plus(scale(multiply(n,plus(const(1),scale(l2,-1))),3),
                    scale(L,-10),scale(l2,8),scale(l3,8),const(-41))
    identity("log_B_minus_3nD_expansion",lower,simplified)

    positive("exp_series_at_7_over_10",
             sum((Q(7,10)**a/Q(factorial(a)) for a in range(4)),Q(0))-2,
             Q(13,6000))
    positive("exp_series_at_25_over_36",
             sum((Q(25,36)**a/Q(factorial(a)) for a in range(5)),Q(0))-2,
             Q(43441,40310784))
    positive("e_less_than_3_implies_log6_gt_3over2",36-27)
    positive("first_gap_threshold",Q(1024,10)-70-29,Q(17,5))
    positive("first_gap_derivative",Q(1,10)-Q(10,1024))
    positive("second_gap_threshold",Q(32768,60)-105-29,Q(6182,15))
    positive("second_gap_derivative",Q(1,60)-Q(10,32768))
    positive("t_greater_than_5_at_first_threshold",Q(2,5)*Q(1024,7)-5)
    positive("N_less_than_5001_over_5000_n_squared",104**2-10000)

    coeff1=Q(12,5)-Q(12*7,1024)
    coeff2=Q(27,10)-Q(12*21,2*32768)
    assert coeff1==Q(2967,1280)
    assert coeff2==Q(220869,81920)
    w1=Q(5001,5000)/coeff1
    w2=Q(5001,5000)/coeff2
    assert w1==Q(53344,123625)
    assert w2==Q(3414016,9202875)
    positive("first_w_coefficient",Q(7,16)-w1)
    positive("second_w_coefficient",Q(3,8)-w2)

    # Independently substitute w=(3/8)*J*x in the inherited cubic expressions.
    substituted_complement=[Q(481),Q(5400)*Q(3,8),Q(15552)*Q(3,8)**2]
    substituted_small=[Q(36*784),Q(36*9600)*Q(3,8),Q(36*30000)*Q(3,8)**2]
    P1=[481,2025,2187]
    P0=[28224,129600,151875]
    assert substituted_complement==list(map(Q,P1))
    assert substituted_small==list(map(Q,P0))
    records.append({"label":"both_fixed_J_polynomial_substitutions",
                    "coefficient_identity":True})

    difference1=[P1[0]-P1[1],P1[1]-2*P1[2],P1[2]]
    difference0=[2*P0[0]-P0[1],2*P0[1]-2*P0[2],2*P0[2]]
    assert difference1==[-1544,-2349,2187]
    assert difference0==[-73152,-44550,303750]
    positive("P1_minus_derivative_at_2",poly_value(difference1,Q(2)),2506)
    positive("P1_minus_derivative_increases_above_2",difference1[1]+4*difference1[2])
    positive("2P0_minus_derivative_at_2",poly_value(difference0,Q(2)),1052748)
    positive("2P0_minus_derivative_increases_above_2",difference0[1]+4*difference0[2])
    assert 42*poly_value(P1,Q(35,2))==Q(59277729,2)
    positive("complement_near_cubic_global_height",2**25-1-42*poly_value(P1,Q(35,2)))
    assert poly_value(P0,Q(42,5))==11833164
    positive("small_near_three_halves_global_height",(2**12-1)**2-poly_value(P0,Q(42,5)))
    positive("small_global_height_covers_low_n_using_J_ge_17",2**24*17**3-32768**2)
    positive("log_H1_scale_coefficient",Q(35,2)-5)
    positive("log_H0_scale_coefficient",Q(42,5)-Q(5,2))

    positive("J_le_8_low_n_w_bound",16-Q(5001,85000)*8*32)
    positive("J_le_8_middle_n_w_bound",65-Q(7,16)*8*Q(21,2),Q(113,4))
    positive("J_le_8_endpoint_exponent",Q(65,3)-21)
    positive("J_le_8_exact_integer_endpoint",8**21-3**22*601**3)
    positive("J_le_8_monotonicity",1-Q(81,9*65+16))

    note=Path(__file__).with_name("v20_logarithmic_gap.md")
    report={
        "status":"PASS",
        "date_jst":"2026-11-07",
        "scope":"Exact algebra and rational margins supporting the written universal analytic proof",
        "check_count":len(records),
        "records":records,
        "lower_gap_thresholds":[
            {"n_minimum":1024,"bound":"t > 2*n/(5*log(n))","w_bound":"w < (7/16)*J*log(n)"},
            {"n_minimum":32768,"bound":"t > 9*n/(20*log(n))","w_bound":"w < (3/8)*J*log(n)"}],
        "global_heights":{
            "small":"n < 2^12*J^(3/2)*(1+log(J)); uses existing J>=17 for low n",
            "complement":"n < 2^25*J^3*(1+log(J))^2"},
        "analytic_complement_J_exclusion":"All 1<=J<=8, without a delta or n scan",
        "note_sha256":sha256(note.read_bytes()).hexdigest(),
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "limits":[
            "The integral factorial inequalities and monotonicity arguments are written proofs, not Lean certificates",
            "No numerical logarithm or floating-point comparison was used",
            "No arbitrary n or delta scan was performed",
            "No new original solution, DeepSeek API execution, or full classification is claimed"]}
    args.output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["status","check_count","lower_gap_thresholds","global_heights","analytic_complement_J_exclusion","note_sha256","checker_sha256"]},indent=2))


if __name__=="__main__":
    main()
