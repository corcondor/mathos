#!/usr/bin/env python3
"""v80: uniform 2/3-adic reduction of the v79 cube-core descents.

Uses original necessary conditions: b|486, gcd(a,b)=1, rho=a² mod b,
3|Z=X/b for v3(b)=2,3 (proved from integer n,t in v20), and rho odd
when b is even. For f=v3(b)>=2, rho is a 3-adic unit and
v3(M)=v3(6bX+M)=f+2. Thus the canonical 3 cube-core exponents are
(f+2)%3 and -(f+2)%3. For even b, v2(C)=1, v2(X)>=1
and the canonical 2 cube-core is always NONTRIVIAL.

For rho=100003, b9 admits exactly 18 positive-Y coefficient types,
b18 admits exactly 12, versus 27 each before local filtering.
No full integral-point classification of these cubic covers is claimed.
"""
from math import gcd
from itertools import product
from sympy import factorint

BS=(1,2,3,6,9,18,27,54,81,162,243,486)
RHO=100003

def valuation(n,p):
    assert n!=0
    n=abs(n); z=0
    while n%p==0:
        n//=p;z+=1
    return z

def choices(m):
    primes=tuple(sorted(int(p) for p in factorint(m)))
    for exponents in product((0,1,2),repeat=len(primes)):
        c=d=t=1
        for p,i in zip(primes,exponents):
            if i==1:c*=p;d*=p*p;t*=p
            elif i==2:c*=p*p;d*=p;t*=p
        assert c*d==t**3
        yield dict(c=c,d=d,t=t,exponents=dict(zip(primes,exponents)))

def allowed(bb,item):
    f=valuation(bb,3) if bb%3==0 else 0
    if bb%2==0 and item['exponents'].get(2,0)==0:return False
    if f>=2:
        e=(f+2)%3
        at3=item['exponents'].get(3,0)
        if e==0 and at3!=0:return False
        if e!=0 and at3==0:return False
    return True

for f in (2,3,4,5):
    e=f+2
    minX=f+(1 if f in (2,3) else 0)
    assert 3*minX>=2*e
    assert e%3=={2:1,3:2,4:0,5:1}[f]
print("PASS: f=2,3,4,5 canonical 3-core exponents = (1,2),(2,1),(0,0),(1,2) in either order")

results=[]
for bb in BS:
    assert 486%bb==0 and gcd(bb,RHO)==1
    m=bb*(8*bb*bb+9*RHO)
    fs=factorint(m)
    f=valuation(bb,3) if bb%3==0 else 0
    if f>=2:assert valuation(m,3)==f+2
    if bb%2==0:assert valuation(m,2)==1
    raw=list(choices(m))
    admitted=[z for z in raw if allowed(bb,z)]
    assert admitted
    results.append((bb,len(raw),len(admitted)))
    print("FIBRE",bb,"M",m,"prime_factors",fs,
          "cube_core_types",len(raw),"after_2_3_adic",len(admitted))
assert (9,27,18) in results and (18,27,12) in results
print("PASS: b=9 and b=18 require only 18 and 12 positive-Y cubic-cover types")

for bb,rr,x,y in ((6,100003,221130,97518330),
                  (243,100003,1756217862,72328954537539)):
    m=bb*(8*bb*bb+9*rr)
    C=6*bb*x+m
    U,V=abs(y),abs(y+C)
    assert U*V==x**3
    g=gcd(U,V)
    if bb%2==0:assert valuation(C,2)==valuation(g,2)==1
    f=valuation(bb,3)
    if f>=2:assert valuation(C,3)==valuation(g,3)==f+2
    print("PASS certified sample local valuations",bb,"gcdUV",g)
print("LIMIT: 30 cubic-cover TYPES remain; their full integer-point sets not solved")
