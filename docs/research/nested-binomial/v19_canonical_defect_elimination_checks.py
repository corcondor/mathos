#!/usr/bin/env python3
"""Actual elimination plus exact integer certificates; no Lean claim."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import gzip
import json
from math import gcd
from pathlib import Path

import sympy as sp


def terms(expr, variables):
    p = sp.Poly(sp.expand(expr), *variables, domain=sp.ZZ)
    return [[list(m), int(c)] for m, c in p.terms()]


def monic_basis(expressions, variables):
    return sp.groebner(expressions, *variables, order="lex", domain=sp.QQ)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inherited-certificate", type=Path)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    output = args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    r, n, h, c, s = sp.symbols("r n h c s")
    variables = (r, n, h, c)
    N = n*n+2
    F = c*r*r-h*n*(n-1)
    branch_certificates = []
    cas = []

    for epsilon in (0, 1):
        B = (r-epsilon)**2-6*n+8
        a = h+6*c
        if epsilon == 0:
            b = 2*h-8*c
            ell = a*n+b
            E = b*b+2*a*a
            multipliers = [a*a-h*(a*n-b), -(a*n-b), c*(a*n-b)]
            assert sp.expand(ell-(F-c*B+h*N)) == 0
            expected = 2*(3*h*h-4*c*h+68*c*c)
        else:
            b = 2*h-9*c
            ell = 2*c*r+a*n+b
            U = 4*c*h+2*a*b
            V = b*b+8*c*h-2*a*a
            P = 2*c*r-a*n-b
            Z = U*n-V
            E = V*V+2*U*U
            multipliers = [U*U-Z*(4*c*h-a*a)+h*Z*P,
                           Z*(P-4*c), -c*Z*P]
            assert sp.expand(ell-(F-c*B+h*N)) == 0
            assert sp.expand(U*n+V-(4*c*F+(4*c*h-a*a)*N-P*ell)) == 0
            expected = 3*(12*h**4-16*c*h**3+404*c*c*h*h
                          -1752*c**3*h+7803*c**4)
        assert sp.expand(E-expected) == 0
        assert sp.expand(sum(A*H for A,H in zip(multipliers,(N,F,B)))-E) == 0
        gb = monic_basis((F,N,B), variables)
        eliminated = [sp.factor(p.as_expr()) for p in gb.polys
                      if not p.as_expr().has(r,n)]
        assert len(eliminated) == 1
        assert sp.Poly(eliminated[0],h,c).monic() == sp.Poly(E,h,c).monic()

        saturated = monic_basis((F,N,B,1-s*c*h*n*(n-1)), (s,)+variables)
        projected = [p.as_expr() for p in saturated.polys if not p.as_expr().has(s)]
        sat_gb = monic_basis(projected, variables)
        same = all(gb.reduce(p.as_expr())[1] == 0 for p in sat_gb.polys)
        same = same and all(sat_gb.reduce(p.as_expr())[1] == 0 for p in gb.polys)
        assert same

        first = sp.resultant(F,B,r)
        second = sp.factor(sp.resultant(N,first,n))
        assert sp.expand(second-(E**2 if epsilon==0 else E)) == 0
        branch_certificates.append({
            "epsilon":epsilon,
            "variable_order":[str(v) for v in variables],
            "generator_order":["N","F","B"],
            "generators":[terms(H,variables) for H in (N,F,B)],
            "multipliers":[terms(A,variables) for A in multipliers],
            "integer_eliminant":terms(E,variables),
        })
        cas.append({
            "epsilon":epsilon,
            "basis":[str(p.as_expr()) for p in gb.polys],
            "elimination_generator":str(eliminated[0]),
            "is_zero_dimensional":bool(gb.is_zero_dimensional),
            "saturation_factor":"c*h*n*(n-1)",
            "saturated_basis":[str(p.as_expr()) for p in sat_gb.polys],
            "saturation_unchanged":same,
            "iterated_resultant":str(second),
            "raw_resultant_has_unnecessary_square":epsilon==0,
        })

    x = Fraction(45,4)
    E0end = 2*(3*x*x-4*x+68)
    Uend = 4*x*x+10*x-108
    Vend = 2*x*x-52*x+9
    E1end = Vend*Vend+2*Uend*Uend
    assert E0end == Fraction(6443,8)
    assert E1end == Fraction(40062681,64)
    assert E0end*6**2 < 2**15
    assert E1end*6**4 < 2**30
    small_height = Fraction(8,7)*(6*2**15+60+Fraction(207**2,2))
    comp_height = Fraction(8,7)*(6*2**30+54+Fraction(287**2,2))
    assert small_height == Fraction(1744740,7) < 2**18
    assert comp_height == Fraction(51539937460,7) < 2**33
    assert 18**2>2**8 and 17**2>2**8
    constants = {
        "ratio_upper_bound":str(x),
        "small_norm_endpoint":str(E0end),
        "complement_norm_endpoint":str(E1end),
        "small_norm_delta_bound":str(E0end*6**2),
        "complement_norm_delta_bound":str(E1end*6**4),
        "small_n_squared_coefficient":str(small_height),
        "complement_n_squared_coefficient":str(comp_height),
    }
    certificate={"schema":1,"branches":branch_certificates,"constants":constants}
    certificate_path=output/"v19_canonical_defect_elimination_certificate.json"
    certificate_path.write_text(json.dumps(certificate,indent=2)+"\n")

    regression=None
    if args.inherited_certificate:
        raw=gzip.decompress(args.inherited_certificate.read_bytes())
        previous=json.loads(raw)
        count=0
        examples=[]
        for row in previous["candidates"]:
            nn,rr,dd,MM,KK=(int(row[v]) for v in ("n","r","delta","M","K"))
            CC=MM*dd;gg=gcd(CC,KK);cc=CC//gg;hh=KK//gg
            assert cc*rr*rr==hh*nn*(nn-1)
            for eps in (0,1):
                NN=nn*nn+2; TT=(rr-eps)**2-9*nn*nn-6*nn-10
                assert TT>0
                GG=gcd(NN,TT);JJ=TT//GG;ww=NN//GG
                if eps==0:
                    EE=2*(3*hh*hh-4*cc*hh+68*cc*cc)
                    assert (hh-9*cc)*nn*nn-(hh+6*cc)*nn-cc*(JJ*GG+10)==0
                    assert nn*nn < 2**18*dd**3*JJ
                    assert nn**3 < 2**22*dd**4*JJ**2
                else:
                    UU=4*hh*hh+10*cc*hh-108*cc*cc
                    VV=2*hh*hh-52*cc*hh+9*cc*cc
                    EE=VV*VV+2*UU*UU
                    LL=(hh-9*cc)*nn*nn-(hh+6*cc)*nn-cc*(JJ*GG+9)
                    assert LL==2*cc*rr
                    assert LL*LL-4*cc*hh*nn*(nn-1)==0
                    assert nn*nn < 2**33*dd**5*JJ
                    assert nn**3 < 2**52*dd**8*JJ**2
                assert EE%GG==0
                count+=1
                if len(examples)<2:
                    examples.append({"epsilon":eps,"delta":dd,"C":CC,"K":KK,
                                     "c":cc,"h":hh,"G":GG,"E":EE,
                                     "n_decimal_digits":len(str(nn)),
                                     "J_decimal_digits":len(str(JJ))})
        regression={"inherited_certificate_uncompressed_sha256":sha256(raw).hexdigest(),
                    "previous_candidates":len(previous["candidates"]),
                    "branch_checks":count,"examples":examples,
                    "scope":"Supporting regression only; these candidates were already excluded in v19"}

    report={"status":"PASS","sympy_version":sp.__version__,
            "cas":cas,"constants":constants,"integer_bezout_certificates":2,
            "regression":regression,
            "certificate_sha256":sha256(certificate_path.read_bytes()).hexdigest(),
            "proof_scope":"Exact identities plus written inequalities; no Lean execution"}
    (output/"v19_canonical_defect_elimination_checks.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","sympy_version","integer_bezout_certificates","regression","certificate_sha256")},indent=2))


if __name__=="__main__":
    main()
