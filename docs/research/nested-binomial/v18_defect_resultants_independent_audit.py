#!/usr/bin/env python3
"""Independent v18 defect-resultant audit; no producer imports/execution.
Identities are checked by exact polynomial interpolation grids of sufficient
degree, not by extrapolating residue examples. Modular checks are supporting.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

CS=(2,3,5,6,7,8,10,11,12,13,14,15)
NODES=(-2,0,3)
def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def roots(c: int, p: int, exponent: int) -> list[int]:
    xs=[a for a in range(p) if (a*a-c)%p==0]
    q=p
    for _ in range(1,exponent):
        xs=[a+q*((-(a*a-c)//q)*pow(2*a,-1,p)%p) for a in xs]
        q*=p
    assert all((a*a-c)%q==0 for a in xs)
    return xs

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--note",type=Path,default=Path(__file__).with_name("v18_defect_resultants.md"))
    ap.add_argument("--producer-report",type=Path,default=Path(__file__).with_name("v18_defect_resultants_checks.json"))
    ap.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    args=ap.parse_args()
    produced=json.loads(args.producer_report.read_text())
    assert produced["status"]=="PASS"
    assert produced["proof_note_sha256"]==sha(args.note)
    lo,hi=Fraction(9),Fraction(10400,927)
    rows=[]
    identity_count=0
    grid_evaluations=0
    for c in CS:
        def uv(C,K):
            return 6*C*c*(c+2)-36*K,c*(36*K-C*(c*c+13*c+4))
        def norm(C,K):
            U,V=uv(C,K)
            value=V*V-c*U*U
            assert value%(c*(c-1))==0
            return value//(c*(c-1))
        constant=norm(1,0)
        value_plus=norm(1,1)
        value_minus=norm(1,-1)
        assert (value_plus+value_minus-2*constant)%2==0
        assert (value_plus-value_minus)%2==0
        aa=(value_plus+value_minus-2*constant)//2
        bb=(value_plus-value_minus)//2
        cc=constant
        content=gcd(gcd(abs(aa),abs(bb)),abs(cc))
        reduced=[aa//content,bb//content,cc//content]
        core=content
        for p in (2,3):
            while core%p==0:core//=p
        assert core==1

        # Each identity has degree at most 2 in each variable separately.
        # Values on three distinct nodes in every variable determine it.
        for n,C,K in product(NODES,repeat=3):
            U,V=uv(C,K)
            D=(36*K-C*c*(c+8))**2-C*C*c*(5*c+4)**2
            f=36*K*n*(n-1)-C*((c+2)*n-3*c)**2
            assert f==(36*K-C*(c+2)**2)*(n*n-c)+U*n+V
            assert V*V-c*U*U==c*(c-1)*D
            assert D==content*(reduced[0]*K*K+reduced[1]*C*K+reduced[2]*C*C)
            grid_evaluations+=3
        identity_count+=3
        a,b,d=map(Fraction,reduced)
        vertex=-b/(2*a)
        points=[lo,hi]
        if lo<=vertex<=hi:points.append(vertex)
        values=[abs(a*x*x+b*x+d) for x in points]
        mx=max(values)
        assert mx<Fraction(250000,9)
        if c==10:assert mx<33
        rows.append({"c":c,"content":content,"coefficients_K2_CK_C2":reduced,
                     "checked_points":[str(x) for x in points],
                     "absolute_values":[str(x) for x in values],"maximum":str(mx)})
    assert rows==produced["complete_interval_extrema"]
    assert max(Fraction(x["maximum"]) for x in rows)==Fraction(293437045,10609)

    for sigma,coeff in ((1,(648,36,25)),(-1,(648,1764,1681))):
        for n,C,K in product(NODES,repeat=3):
            a=3-6*sigma
            U=36*K+2*C*a
            V=36*K+C*(a*a-1)
            target=coeff[0]*K*K+coeff[1]*C*K+coeff[2]*C*C
            f=36*K*n*(n-1)-C*(n+a)**2
            assert f==(36*K-C)*(n*n+1)-U*n-V
            assert U*U+V*V==4*target
            grid_evaluations+=2
        identity_count+=2
    assert identity_count==40

    margins={
        "K_over_delta":Fraction(68)-Fraction(62400,927),
        "negative_primitive_max":Fraction(250000,9)-Fraction(293437045,10609),
        "negative_height":Fraction(2**38)-Fraction(10**12+9,6),
        "c10_height":Fraction(2**18)-Fraction(1188**2+9,6),
        "positive_small_prime":Fraction(10000)-36*(Fraction(45,4)**2+Fraction(49,4)**2),
        "positive_complementary_prime":Fraction(4000000)-36*(648*Fraction(45,4)**2+1764*Fraction(45,4)+1681),
        "positive_small_height":Fraction(2**24)-Fraction(10000**2+9,6),
        "positive_complementary_height":Fraction(2**42)-Fraction(4000000**2+9,6),
    }
    assert all(x>0 for x in margins.values())
    assert {k:str(v) for k,v in margins.items()}==produced["exact_positive_margins"]

    negative=0
    positive=0
    for row in rows:
        c=row["c"]
        aa,bb,cc=row["coefficients_K2_CK_C2"]
        for p in (17,19,23,29,31,37,41,43,47,53,59,61,67,71,73):
            for e in (1,2,3):
                q=p**e
                for n in roots(c,p,e):
                    assert gcd(n*(n-1)*6*c*(c-1)*row["content"],q)==1
                    r=((c+2)*n-3*c)*pow(6,-1,q)%q
                    for C in (1,2,11,p):
                        K=C*r*r*pow(n*(n-1),-1,q)%q
                        assert (aa*K*K+bb*C*K+cc*C*C)%q==0
                        negative+=1
    for p in (5,13,17,29,37,41,53,61,73):
        for e in (1,2,3):
            q=p**e
            for n in roots(-1,p,e):
                for C in (1,2,11,p):
                    for sigma in (-1,1):
                        for small in (True,False):
                            r=sigma if small else ((n+3)*pow(6,-1,q)-sigma)%q
                            K=C*r*r*pow(n*(n-1),-1,q)%q
                            if small:
                                value=K*K+(K+C)**2
                            elif sigma==1:
                                value=648*K*K+36*C*K+25*C*C
                            else:
                                value=648*K*K+1764*C*K+1681*C*C
                            assert value%q==0
                            positive+=1

    review=[
        "The exact-defect equation Cr^2=Kn(n-1) and interval 9C<K<(10400/927)C follow from the definitions and strict r interval.",
        "Negative T_c divides both k and N_c. Only the units 6,c,c-1,g_c are cancelled, and all are units at primes>=17.",
        "Each c is positive nonsquare, so E_c cannot vanish; using a factor of |E_c| for the conditional height is valid.",
        "The maxima use both endpoints and any interior vertex of each quadratic; the extremal value and every integer margin were independently reproduced.",
        "For the positive neighbor n=3 mod6 removes the 2 and 3 excess and makes S coprime to Q.",
        "N_plus<m^2 makes S either 1 or a single odd-prime power; the two roots of one then justify a single global sign.",
        "The signed positive forms were independently recovered by reduction modulo n^2+1 and sum-of-squares norms.",
        "All four delta^4 heights are conditional on the stated large repeated-prime event; no unconditional polynomial height or complete branch solution is claimed.",
        "The main L_m formulation is independent. The appended L_r corollary correctly cites v18_short_lcm.md: its stronger excess still divides k^2, so the same K and E_c divisibilities apply without changing any elimination or constant.",
        "For an individual negative neighbor N_c<r^2, two distinct exact prime powers exceeding r cannot both divide N_c. Its L_r excess therefore has at most one prime base; different neighbors may retain different primes.",
    ]
    report={
        "status":"PASS",
        "review_type":"Independent internal mathematical review plus a separate exact arithmetic implementation; not external peer review or Lean",
        "producer_imported_or_executed":False,
        "polynomial_identity_method":"Tensor interpolation grid {-2,0,3} in each variable; each difference has separate degree<=2",
        "polynomial_identities":identity_count,"exact_grid_evaluations":grid_evaluations,
        "complete_interval_extrema":rows,"positive_margins":{k:str(v) for k,v in margins.items()},
        "supporting_residue_checks":{"negative":negative,"positive":positive,"method":"Hensel lifts at exponents 1,2,3; includes nonunit C residues","finite_extrapolation":False},
        "written_review":review,
        "proof_note_sha256":sha(args.note),"producer_report_sha256":sha(args.producer_report),
        "short_lcm_input_sha256":sha(Path(__file__).with_name("v18_short_lcm.md")),
        "auditor_source_sha256":sha(Path(__file__)),
        "new_lean_execution":False,"new_deepseek_api_calls":0,"external_peer_review":False,
    }
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","identities":identity_count,"exact_grid_evaluations":grid_evaluations,
                      "extrema":len(rows),"negative_supporting_checks":negative,
                      "positive_supporting_checks":positive,"output":str(args.output)}))

if __name__=="__main__":
    main()

