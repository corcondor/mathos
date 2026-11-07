#!/usr/bin/env python3
"""Exact algebra and supporting checks for v18_residual_gap.md.

The universal result is the written proof, not finite extrapolation.
No external algebra package, Lean, API, or complete point solver is used.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as R
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import argparse
import json

# Three-variable polynomials; exponents correspond to (a,b,rho).
def clean(p):
    return {e:c for e,c in p.items() if c}
def const(c):
    return {(0,0,0):R(c)} if c else {}
def var(i):
    e=[0,0,0];e[i]=1
    return {tuple(e):R(1)}
def add(*ps):
    z={}
    for p in ps:
        for e,c in p.items(): z[e]=z.get(e,R(0))+c
    return clean(z)
def mul(p,q):
    z={}
    for e,c in p.items():
        for f,d in q.items():
            g=tuple(e[i]+f[i] for i in range(3))
            z[g]=z.get(g,R(0))+c*d
    return clean(z)
def scale(c,p): return {e:R(c)*v for e,v in p.items() if c*v}
def neg(p): return scale(-1,p)
def power(p,n):
    z=const(1)
    for _ in range(n): z=mul(z,p)
    return z
def mon(c,ea=0,eb=0,er=0):
    return {(ea,eb,er):R(c)} if c else {}
def equal(p,q):
    assert add(p,neg(q))=={}, add(p,neg(q))

def exact_algebra():
    a,b,r=var(0),var(1),var(2)
    F=add(mon(4,6),mon(24,4,2),mon(-12,4,0,1),mon(36,2,4),
          mon(60,2,2,1),mon(12,2,0,2),mon(-3,0,2,2),mon(-4,0,0,3))
    q0=add(mon(2,3),mon(6,1,2),mon(-3,1,0,1))
    d0=add(mon(96,2,2,1),mon(3,2,0,2),mon(-3,0,2,2),mon(-4,0,0,3))
    equal(add(F,neg(power(q0,2))),d0)
    grouped=add(mul(mon(3,0,2,1),add(mon(32,2),neg(r))),
                mul(power(r,2),add(mon(3,2),scale(-4,r))))
    equal(d0,grouped)
    four_a_q1=add(mul(mon(4,1),q0),mul(scale(3,r),add(r,mon(32,0,2))))
    clear_left=add(mul(mon(16,2),F),neg(power(four_a_q1,2)))
    clear_right=add(
        mul(mon(8,2,0,1),add(power(r,2),mon(264,0,2,1),mon(-576,0,4))),
        scale(-9,mul(power(r,2),power(add(r,mon(32,0,2)),2))))
    equal(clear_left,clear_right)
    x=a
    envelope=add(const(R(1,2)),scale(132,x),scale(-288,power(x,2)),
                 scale(R(-27,64),power(add(const(1),scale(32,x)),2)))
    equal(envelope,add(const(R(5,64)),scale(105,x),scale(-720,power(x,2))))
    retained_left=add(mon(R(162,17),1,1),mon(R(81,17),2),
                      mon(R(54,17),3,-1))
    retained_right=mul(mon(R(27,17),1,-1),
                      add(mon(2,2),mon(3,1,1),mon(6,0,2)))
    equal(retained_left,retained_right)
    return {
        "cubic_polynomial_difference":"all coefficients zero",
        "positive_grouping":"all coefficients zero",
        "denominator_cleared_second_difference":"all coefficients zero",
        "positive_envelope_for_rho_ge_7b2":"all coefficients zero",
        "height_with_residual_retained":"all coefficients zero",
    }

def exact_constants():
    K5=R(33*297**2,17**2)*56**5
    K7=R(297,17)**3*1095*486*56**7
    assert K5==R(1603123474563072,289)
    assert K7==R(24078860209989084260597760,4913)
    margins={
        "q0_lower":R(26,17)-R(3,2),
        "rho_upper":R(3,4)-R(976,1377),
        "positive_envelope_slope":R(105)-R(720,7),
        "region_I_constant":R(26)-R(542,21),
        "fixed_residual_height_constant":R(36)-R(10164,289),
        "five_eighths_constant":R(40**8)-K5,
        "seven_elevenths_constant":R(96**11)-K7,
    }
    assert all(v>0 for v in margins.values())
    assert R(28*486,243)==56
    assert R(28,243)*R(297,17)**2==R(10164,289)
    assert R(1,2)+R(132,7)==R(271,14)
    return {k:str(v) for k,v in margins.items()},str(K5),str(K7)

def smallest_prime_factors(limit):
    spf=list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for n in range(p*p,limit+1,p):
                if spf[n]==n: spf[n]=p
    return spf

def factor(n,spf):
    ans=Counter()
    while n>1:
        p=spf[n];ans[p]+=1;n//=p
    return ans

def support(limit):
    """Complete old necessary-condition enumeration only up to explicit limit."""
    spf=smallest_prime_factors(limit)
    rows=[]
    region=Counter()
    for n in range(104,limit+1):
        M=gcd(n,3)*gcd(n-1,6)
        factors=factor(n,spf)+factor(n-1,spf)
        factors.subtract(factor(M,spf))
        forced=1
        for p,e in factors.items():
            assert e>=0
            forced*=p**((e+2)//3)
        lo=forced*(3*n//forced+1)
        hi=(10*n-1)//3
        for r in range(lo,hi+1,forced):
            Q=n*(n-1)//M
            assert r**3%Q==0
            t=r-3*n;u=t+3
            h,rem=divmod(M*((9*t*t+27*t+27)*n+t**3),n*(n-1))
            assert rem==0 and h>81*M
            g=gcd(h,81*M);a=h//g;b=81*M//g
            rho=a*a+a*b*(9*n-t-6)-b*b*(t*t+3*t+3)
            assert a>b>0 and 486%b==0 and rho>0
            assert 1377*rho<216*a*a+760*b*b
            F=(4*a**6+24*a**4*b*b-12*a**4*rho+36*a*a*b**4
               +60*a*a*b*b*rho+12*a*a*rho*rho-3*b*b*rho*rho-4*rho**3)
            y=isqrt(F)
            assert y*y==F
            q0=2*a**3+(6*b*b-3*rho)*a
            assert 2*q0>3*a**3 and 4*rho<3*a*a and y>=q0+1
            d0=F-q0*q0
            assert d0==3*rho*(32*b*b+rho)*a*a-rho*rho*(3*b*b+4*rho)
            assert a<rho*(rho+32*b*b)<=33*b*b*rho*rho
            assert 17*b*rho*u<27*a*(2*a*a+3*a*b+6*b*b)<297*a**3
            assert 243*n*a<28*b*u*u and n*a<56*u*u
            # q1 is represented by the integer numerator Q1 = 4*a*q1.
            Q1=4*a*q0+3*rho*(rho+32*b*b)
            rem1=16*a*a*F-Q1*Q1
            assert rem1==(8*a*a*rho*(rho*rho+264*b*b*rho-576*b**4)
                          -9*rho*rho*(rho+32*b*b)**2)
            if rho>=7*b*b:
                region["rho_ge_7b2"]+=1
                assert rem1>0 and 4*a*y-Q1>=1
                assert 4*rem1>3*a*a*16*a*a
                assert 14*rem1<271*rho**3*16*a*a
                assert 21*a*a<542*rho**3
            else:
                region["rho_lt_7b2"]+=1
            assert a*a<1095*b**4*rho**3
            assert n**5*289<1603123474563072*u**8
            assert n**7*4913<24078860209989084260597760*u**11
            assert n**5<40**8*u**8 and n**7<96**11*u**11
            assert 289*b*rho*rho*n<10164*a**5
            assert b*n<36*rho**3*(rho+32*b*b)**5
            assert n**3*289**3<10164**3*1095**2*b**5*a**11
            assert n*n*289**2<10164**2*1095**5*b**18*rho**11
            rows.append({"n":n,"r":r,"M":M,"t":t,"u":u,"h":h,"a":a,"b":b,
                         "rho":rho,"y":y,"q0":q0,"y_minus_q0":y-q0,
                         "four_a_q1":Q1,"four_a_y_minus_four_a_q1":4*a*y-Q1,
                         "region":"I" if rho>=7*b*b else "II"})
    return rows,dict(region)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit",type=int,default=100000)
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args=parser.parse_args()
    assert args.limit>=104
    algebra=exact_algebra()
    margins,K5,K7=exact_constants()
    rows,region=support(args.limit)
    source=Path(__file__).resolve()
    proof=source.with_name("v18_residual_gap.md")
    report={
        "status":"PASS",
        "date":"2026-11-07 JST",
        "scope":"ell=1,j=i-3; both k branches; original squared-index equation",
        "universal_inputs":"n>=104, Q=n(n-1)/M divides r^3, 3n<r<10n/3; written v16/v17 deductions including h>81M",
        "universal_conclusions":["n^5<40^8*(r-3n+3)^8","n^7<96^11*(r-3n+3)^11"],
        "residual_heights":{
            "a_by_rho":"a<rho*(rho+32*b^2)",
            "a_by_large_rho":"a^2<26*rho^3 for rho>=7*b^2",
            "a_by_all_rho":"a^2<1095*b^4*rho^3",
            "n_by_a":"n^3<(10164/289)^3*1095^2*b^5*a^11",
            "n_by_rho":"n^2<(10164/289)^2*1095^5*b^18*rho^11",
            "unbounded_parameters_excluded":False,
        },
        "exact_polynomial_identities":algebra,
        "exact_positive_rational_margins":margins,
        "K5":K5,"K7":K7,
        "supporting_sample":{
            "n_limit":args.limit,"necessary_first_indices":len({x["n"] for x in rows}),
            "necessary_pairs":len(rows),"regions":region,"records":rows,
            "original_solutions":False,"finite_samples_prove_universal_result":False,
        },
        "source_sha256":sha256(source.read_bytes()).hexdigest(),
        "proof_note_sha256":sha256(proof.read_bytes()).hexdigest(),
        "new_lean_execution":False,"new_deepseek_api_calls":0,
        "complete_CAS_solver_called":False,"external_peer_review":False,
        "verification_boundary":"Written universal inequalities plus exact polynomial coefficient identities and rational margins; finite old-necessary-condition samples are supplementary only.",
    }
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","identities":len(algebra),
                      "positive_margins":len(margins),"limit":args.limit,
                      "necessary_pairs":len(rows),"regions":region,
                      "report":str(args.output)},ensure_ascii=False))
if __name__=="__main__":
    main()

