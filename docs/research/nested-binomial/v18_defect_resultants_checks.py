#!/usr/bin/env python3
"""Exact v18 resultant identities and bounds; stdlib only.
Finite residue checks support, but do not prove, the universal written arguments.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import argparse, hashlib, json

CS=[2,3,5,6,7,8,10,11,12,13,14,15]
PRIMES=[17,19,23,29,31,37,41,43]
class Poly:
    def __init__(self,v=0):
        self.d=dict(v) if isinstance(v,dict) else ({(0,0,0):v} if v else {})
        self.d={k:v for k,v in self.d.items() if v}
    def __add__(self,o):
        o=o if isinstance(o,Poly) else Poly(o);d=dict(self.d)
        for k,v in o.d.items():d[k]=d.get(k,0)+v
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+-o
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        o=o if isinstance(o,Poly) else Poly(o);d={}
        for a,x in self.d.items():
            for b,y in o.d.items():
                k=tuple(a[i]+b[i] for i in range(3));d[k]=d.get(k,0)+x*y
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,e):
        r=Poly(1)
        for _ in range(e):r=r*self
        return r
    def zero(self):return not self.d

n=Poly({(1,0,0):1});C=Poly({(0,1,0):1});K=Poly({(0,0,1):1})
rows=[];identity_count=0
for c in CS:
    U=6*C*c*(c+2)-36*K
    V=c*(36*K-C*(c*c+13*c+4))
    D=(36*K-C*c*(c+8))**2-C*C*c*(5*c+4)**2
    assert (36*K*n*(n-1)-C*((c+2)*n-3*c)**2-
            ((36*K-C*(c+2)**2)*(n*n-c)+U*n+V)).zero()
    assert (V*V-c*U*U-c*(c-1)*D).zero()
    coeff=[1296,-72*c*(c+8),c*(c-1)*(c-4)**2]
    g=gcd(gcd(*coeff[:2]),coeff[2])
    gg=g
    for p in [2,3]:
        while gg%p==0:gg//=p
    assert gg==1
    E=coeff[0]//g*K*K+coeff[1]//g*C*K+coeff[2]//g*C*C
    assert (D-g*E).zero();identity_count+=3
    lo,hi=F(9),F(10400,927)
    vertex=F(c*(c+8),36)
    pts=[lo,hi]+([vertex] if lo<=vertex<=hi else [])
    values=[abs((coeff[0]*x*x+coeff[1]*x+coeff[2])/g) for x in pts]
    mx=max(values)
    assert mx<F(250000,9)
    if c==10:assert mx<33
    rows.append({'c':c,'content':g,'coefficients_K2_CK_C2':[a//g for a in coeff],
                 'checked_points':[str(x) for x in pts],
                 'absolute_values':[str(x) for x in values],'maximum':str(mx)})
assert max(F(row['maximum']) for row in rows)==F(293437045,10609)
for sigma, coeff in [(1,[648,36,25]),(-1,[648,1764,1681])]:
    U=36*K+6*C*(1-2*sigma);V=36*K+C*(44-36*sigma)
    E=coeff[0]*K*K+coeff[1]*C*K+coeff[2]*C*C
    assert (U*U+V*V-4*E).zero()
    assert (36*K*n*(n-1)-C*(n+3-6*sigma)**2-
            ((36*K-C)*(n*n+1)-U*n-V)).zero()
    identity_count+=2

margins={
'K_over_delta':F(68)-F(62400,927),
'negative_primitive_max':F(250000,9)-F(293437045,10609),
'negative_height':F(2**38)-F(10**12+9,6),
'c10_height':F(2**18)-F(1188**2+9,6),
'positive_small_prime':F(10000)-36*(F(45,4)**2+F(49,4)**2),
'positive_complementary_prime':F(4*10**6)-36*(648*F(45,4)**2+1764*F(45,4)+1681),
'positive_small_height':F(2**24)-F(10**8+9,6),
'positive_complementary_height':F(2**42)-F((4*10**6)**2+9,6)}
assert all(x>0 for x in margins.values())

negative_checks=0;positive_checks=0;examples=[]
for c,row in zip(CS,rows):
    a,b,d=row['coefficients_K2_CK_C2']
    for p in PRIMES:
        for e in [1,2]:
            q=p**e;inv6=pow(6,-1,q)
            for nn in range(q):
                if (nn*nn-c)%q:continue
                assert gcd(nn*(nn-1),q)==1
                rr=((c+2)*nn-3*c)*inv6%q
                for cc in [1,2,7]:
                    kk=cc*rr*rr*pow(nn*(nn-1),-1,q)%q
                    assert (a*kk*kk+b*cc*kk+d*cc*cc)%q==0
                    negative_checks+=1
                    if len(examples)<12:examples.append([c,p,e,nn,rr,cc,kk])
for p in [5,13,17,29,37,41]:
    for e in [1,2]:
        q=p**e;inv6=pow(6,-1,q)
        for nn in range(q):
            if (nn*nn+1)%q:continue
            for cc in [1,2,7]:
                for sigma in [-1,1]:
                    for branch in [0,1]:
                        rr=sigma if branch==0 else ((nn+3)*inv6-sigma)%q
                        kk=cc*rr*rr*pow(nn*(nn-1),-1,q)%q
                        if branch==0:target=kk*kk+(kk+cc)**2
                        elif sigma==1:target=648*kk*kk+36*cc*kk+25*cc*cc
                        else:target=648*kk*kk+1764*cc*kk+1681*cc*cc
                        assert target%q==0
                        positive_checks+=1

ap=argparse.ArgumentParser()
ap.add_argument('--output',default=str(Path(__file__).with_suffix('.json')))
ap.add_argument('--note',default=str(Path(__file__).with_name('v18_defect_resultants.md')))
args=ap.parse_args()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
result={'status':'PASS','scope':'ell=1,j=i-3, original squared-index equation',
'polynomial_coefficient_identities':identity_count,'complete_interval_extrema':rows,
'exact_positive_margins':{k:str(v) for k,v in margins.items()},
'supporting_residue_checks':{'negative':negative_checks,'positive':positive_checks,
'negative_examples':examples,'these_prove_universal_statements':False},
'source_sha256':sha(__file__),'proof_note_sha256':sha(args.note),
'new_lean_execution':False,'new_deepseek_api_calls':0,'complete_CAS_solver':False,
'whole_problem_solved':False}
Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','identities':identity_count,
'negative_residue_checks':negative_checks,'positive_residue_checks':positive_checks}))

