#!/usr/bin/env python3
"""Independent standard-library verifier of the integer elimination certificates.

The producer is not imported. Rational Groebner output is not the arithmetic
certificate: the actual Z[r,n,h,c] combinations are checked here.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ZERO=(0,0,0,0)


def clean(poly):
    return {m:k for m,k in poly.items() if k}


def add(*polys):
    ans={}
    for poly in polys:
        for m,k in poly.items():
            ans[m]=ans.get(m,0)+k
    return clean(ans)


def scale(poly,k):
    return clean({m:k*v for m,v in poly.items()})


def mul(p,q):
    ans={}
    for a,x in p.items():
        for b,y in q.items():
            m=tuple(u+v for u,v in zip(a,b))
            ans[m]=ans.get(m,0)+x*y
    return clean(ans)


def power(p,e):
    ans={ZERO:1}
    for _ in range(e):
        ans=mul(ans,p)
    return ans


def const(k):
    return {ZERO:k} if k else {}


def var(i):
    m=[0]*4;m[i]=1
    return {tuple(m):1}


def decode(rows):
    ans={}
    for m,k in rows:
        assert len(m)==4 and all(type(v) is int and v>=0 for v in m)
        assert type(k) is int and k!=0
        assert tuple(m) not in ans
        ans[tuple(m)]=k
    return ans


def main():
    root=Path(__file__).resolve().parent
    path=root/"v19_canonical_defect_elimination_certificate.json"
    cert=json.loads(path.read_text())
    assert cert["schema"]==1
    assert len(cert["branches"])==2
    r,n,h,c=[var(i) for i in range(4)]
    N=add(power(n,2),const(2))
    F=add(mul(c,power(r,2)),scale(mul(h,mul(n,add(n,const(-1)))),-1))
    identities=[]
    for eps, branch in enumerate(cert["branches"]):
        assert branch["epsilon"]==eps
        assert branch["variable_order"]==["r","n","h","c"]
        assert branch["generator_order"]==["N","F","B"]
        B=add(power(add(r,const(-eps)),2),scale(n,-6),const(8))
        expected_generators=[N,F,B]
        stored=[decode(v) for v in branch["generators"]]
        assert stored==expected_generators
        if eps==0:
            target=add(scale(power(h,2),6),scale(mul(c,h),-8),scale(power(c,2),136))
        else:
            target=add(scale(power(h,4),36),scale(mul(c,power(h,3)),-48),
                       scale(mul(power(c,2),power(h,2)),1212),
                       scale(mul(power(c,3),h),-5256),scale(power(c,4),23409))
        assert decode(branch["integer_eliminant"])==target
        assert len(branch["multipliers"])==3
        computed=add(*(mul(decode(a),p) for a,p in
                       zip(branch["multipliers"],expected_generators)))
        assert computed==target
        identities.append({"epsilon":eps,"generator_count":3,
                           "multiplier_term_counts":[len(a) for a in branch["multipliers"]],
                           "eliminant_degree":max(sum(m) for m in target),
                           "integer_coefficient_identity":True})

    # Exact endpoint/sign checks for the written monotonicity proof.
    lo,hi=Fraction(9),Fraction(45,4)
    assert 12*lo-8>0                     # derivative of 2*(3*x^2-4*x+68)
    assert 4*lo*lo+10*lo-108>0
    assert 8*lo+10>0                    # derivative of U(x)
    assert 2*lo*lo-52*lo+9<0
    assert 4*hi-52<0                    # derivative of V(x) is negative
    e0=2*(3*hi*hi-4*hi+68)
    e1=(2*hi*hi-52*hi+9)**2+2*(4*hi*hi+10*hi-108)**2
    assert e0*36==Fraction(57987,2)<2**15
    assert e1*1296==Fraction(3245077161,4)<2**30
    small=Fraction(8,7)*(6*2**15+60+Fraction(207**2,2))
    comp=Fraction(8,7)*(6*2**30+54+Fraction(287**2,2))
    assert small==Fraction(1744740,7)<2**18
    assert comp==Fraction(51539937460,7)<2**33
    assert 2**30<2**22*18**2
    assert 2**60<2**52*17**2

    # Verify both reconstruction identities directly as polynomials; this
    # additional variable is represented by treating JG as one symbolic z.
    # All degrees in (r,n,h,c,z) are <= 4, so a 5^5 exact integer grid
    # proves these polynomial equalities once the degree bound is read off.
    # The main Bezout checks above are coefficient checks, not grid samples.
    checks=0
    for rr in range(5):
        for nn in range(5):
            for hh in range(5):
                for cc in range(5):
                    for zz in range(5):
                        f=cc*rr*rr-hh*nn*(nn-1)
                        for ep in (0,1):
                            canonical=(rr-ep)**2-9*nn*nn-6*nn-10-zz
                            L=(hh-9*cc)*nn*nn-(hh+6*cc)*nn-cc*(zz+10-ep*ep)-2*ep*cc*rr
                            assert L==cc*canonical-f
                        checks+=1
    assert checks==3125
    report={"status":"PASS","checker":"Python standard library only",
            "producer_or_sympy_imported":False,
            "integer_bezout_identities":identities,
            "rational_height_constants_checked":True,
            "reconstruction_identity_grid":{"points":checks,"coordinate_count":5,
                  "values_per_coordinate":5,"coordinate_degree_upper_bound":4,
                  "scope":"Polynomial identity verification, not a bound on original integer solutions"},
            "certificate_sha256":sha256(path.read_bytes()).hexdigest(),
            "scope":"Integer eliminant certificates and exact constant margins; written argument supplies arithmetic implication",
            "not_verified":"No Lean, no full original equation classification, no external human review"}
    (root/"v19_canonical_defect_elimination_verification.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
