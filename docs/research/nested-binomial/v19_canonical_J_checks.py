#!/usr/bin/env python3
"""Produce exact elimination/Bézout certificates for small-branch J <= 16.

Coverage is proved in v19_canonical_J_elimination.md. All bounds are derived
from previously proved necessary conditions. SymPy generates the polynomial
certificates; v19_canonical_J_verify.py independently checks them with integer
and finite-field arithmetic and does not import this producer or SymPy.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import argparse
import json
import sympy as sp


def allowed_w(w, j):
    return 30000**4*w**4 < 9*1667**4*j**4*(10*w+2*j)**3


def w_bound(j):
    lo, hi = 0, 1
    while allowed_w(hi,j):
        lo, hi = hi, 2*hi
    while hi-lo > 1:
        mid = (hi+lo)//2
        if allowed_w(mid,j):
            lo = mid
        else:
            hi = mid
    assert not allowed_w(lo+1,j)
    assert lo == 0 or allowed_w(lo,j)
    return lo


def square_cube_divisors(c):
    fac = {int(p):int(e) for p,e in sp.factorint(c).items()}
    divs = [1]
    for p,e in fac.items():
        divs = [a*p**b for a in divs for b in range(3*e//2+1)]
    return sorted(divs)


def coeffs(poly, p):
    return [int(c)%p for c in reversed(poly.all_coeffs())]


def bezout_for_group(j,w,first_n):
    x = sp.Symbol('x')
    c1 = 25*w+3*j
    second_n = sorted({d*v+1 for v in square_cube_divisors(c1)
                       for d in (1,2,3,6) if gcd(d*v,6)==d})
    assert not set(first_n).intersection(second_n)
    p = 2
    while set(n%p for n in first_n).intersection(n%p for n in second_n):
        p = int(sp.nextprime(p))
    P = sp.Poly(1,x,modulus=p)
    for n in first_n:
        P *= sp.Poly(x-n,x,modulus=p)
    Hbar = sp.Poly(1,x,modulus=p)
    for n in second_n:
        Hbar = (Hbar*sp.Poly(x-n,x,modulus=p)).rem(P)
    U,V,C = sp.gcdex(P,Hbar)
    assert C == sp.Poly(1,x,modulus=p)
    assert U*P+V*Hbar == C
    gb = sp.groebner([P.as_expr(),Hbar.as_expr()],x,modulus=p)
    assert [f.as_expr() for f in gb.polys] == [sp.Integer(1)]
    return {'J':j,'w':w,'first_n':first_n,'second_domain_size':len(second_n),
            'prime':p,'P':coeffs(P,p),'H_remainder':coeffs(Hbar,p),
            'U':coeffs(U,p),'V':coeffs(V,p),'groebner_basis':[1]}


def symbolic_checks():
    s,q,R,n,w,J = sp.symbols('s q R n w J')
    f=q*w-n*n-2
    g=q*J-R*R+9*n*n+6*n+10
    F=w*R*R-(9*w+J)*n*n-6*w*n-10*w-2*J
    assert sp.expand(w*g-J*f+F)==0
    assert sp.expand(sp.resultant(f,g,q)+F)==0
    rows=[]
    for j in (1,2):
        base=sp.groebner([f,g.subs(J,j)],q,R,n,w,order='lex',domain=sp.QQ)
        aug=sp.groebner([f,g.subs(J,j),1-s*w*n*(n-1)],
                       s,q,R,n,w,order='lex',domain=sp.QQ)
        elim=[a.as_expr() for a in aug.polys if not a.as_expr().has(s)]
        sat=sp.groebner(elim,q,R,n,w,order='lex',domain=sp.QQ)
        assert sat==base and not base.is_zero_dimensional
        rows.append({'J':j,'QQ_lex_basis':[str(a.as_expr()) for a in base.polys],
                     'saturating_polynomial':'w*n*(n-1)',
                     'Rabinowitsch_basis_size':len(aug.polys),
                     'saturation_unchanged':True,'zero_dimensional':False})
    short_bound=9*Fraction(132,13)**3*Fraction(1667,6000)**4
    assert short_bound<65
    return {'sympy_version':sp.__version__,'q_elimination':str(F),
            'fixed_J_saturation':rows,
            'J_le_5_w_bound':str(short_bound)}


def main(output_dir):
    output_dir.mkdir(parents=True,exist_ok=True)
    report={'scope':'canonical small branch k=r; 1 <= J <= 16',
            'prerequisites':['n >= 104','Q | r^3','t=r-3n >= 3*sqrt(n)',
                             'w >= 65','gcd(w,J)=1','Q0^2 | c0^3','Q1^2 | c1^3'],
            'w_bound_inequality':'30000^4*w^4 < 9*1667^4*J^4*(10*w+2*J)^3',
            'symbolic_checks':symbolic_checks(),'families':[],
            'height_candidates':[],'bezout_certificates':[]}
    totals=Counter()
    groups=defaultdict(list)
    for j in range(1,17):
        if j%8 in (0,2,6):
            report['families'].append({'J':j,'method':'universal 2-adic obstruction'})
            continue
        W=w_bound(j)
        counts=Counter()
        for w in range(65,W+1):
            if gcd(w,j)!=1:
                continue
            counts['primitive_w']+=1
            c0,c1=10*w+2*j,25*w+3*j
            for Q0 in square_cube_divisors(c0):
                for g in (1,3):
                    counts['raw_divisor_records']+=1
                    n=g*Q0
                    if n<104 or gcd(n,3)!=g:
                        continue
                    counts['normalized_n']+=1
                    if 30000**2*w*w>=1667**2*j*j*n:
                        continue
                    counts['height_compatible']+=1
                    d=gcd(n-1,6)
                    Q1=(n-1)//d
                    rem=c1**3%(Q1*Q1)
                    row={'J':j,'w':w,'n':n,'g':g,'d':d,'Q0':Q0,'Q1':Q1,
                         'c0':c0,'c1':c1,'second_divisor_remainder':rem}
                    report['height_candidates'].append(row)
                    groups[(j,w)].append(n)
                    if rem==0:
                        counts['second_divisor_survivors']+=1
        report['families'].append({'J':j,'method':'finite divisor elimination',
                                   'w_max':W,'counts':dict(counts)})
        totals.update(counts)
    assert totals['second_divisor_survivors']==0
    for (j,w),ns in sorted(groups.items()):
        assert len(ns)==len(set(ns))
        report['bezout_certificates'].append(bezout_for_group(j,w,sorted(ns)))
    report['totals']=dict(totals)
    report['certificate_count']=len(report['bezout_certificates'])
    report['max_certificate_prime']=max(c['prime'] for c in report['bezout_certificates'])
    report['conclusion']='Every original solution in the stated branch has canonical J >= 17.'
    report['remaining_scope']='J is unbounded; complementary J=1 and the full equation are not solved.'
    target=output_dir/'v19_canonical_J_certificate.json'
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':str(target),'sha256':sha256(target.read_bytes()).hexdigest(),
                      'totals':report['totals'],'bezout_certificates':report['certificate_count'],
                      'max_certificate_prime':report['max_certificate_prime']},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=p.parse_args()
    main(args.output_dir)
