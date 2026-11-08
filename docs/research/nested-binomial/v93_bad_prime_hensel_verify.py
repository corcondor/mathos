#!/usr/bin/env python3
"""v93. Construct local 2-,3- and p|M-adic points on all ten v91 covers.

rho=100003, b=9 or18. The equations are
    d*v^3-c*u^3=6*b*t*u*v+M,  a^2=t*u*v+b^2+rho.
At p=3, rescale u=3U,v=3V, divide by81, and use strong Hensel
v3(f)>=3>2*v3(f')=2. Check original recovered t,n 3-adic
integrality modulo9. At p=2, use odd derivative plus exact unit-square
criterion mod8 (b18) or valuation-two square criterion mod32 (b9).
At primes p>=5 dividing M, divide the cubic by p when p|c,d,t,
or solve via z=v/u otherwise. The square has a unit root in all cases.
p=100003 is handled separately and sharply in v92.

This is a local-solubility certificate at specified primes, NOT a
global integer-point theorem and not a proof of all-prime local
solubility of the genus-four square covering.
"""
from itertools import product
from math import gcd
from sympy import factorint, sqrt_mod

RHO=100003
PR={9:(3,5,4003),18:(2,3,100291)}
def cases(b):
    M=b*(8*b*b+9*RHO)
    for ex in product(range(3),repeat=3):
        es=dict(zip(PR[b],ex))
        if es[3]==0 or (b==18 and es[2]==0):continue
        c=d=t=1
        for p,e in es.items():
            if e==1:c*=p;d*=p*p;t*=p
            elif e==2:c*=p*p;d*=p;t*=p
        if pow(c,(RHO-1)//3,RHO)!=1:continue
        if b==9:
            sq={z*z%7 for z in range(7)}
            if not any((d*v**3-c*u**3-6*b*t*u*v-M)%7==0
                and (t*u*v+b*b+RHO)%7 in sq
                for u,v in product(range(7),repeat=2)):continue
        assert c*d==t**3
        yield c,d,t,es

def certificate_3(b,c,d,t):
    M=b*(8*b*b+9*RHO)
    assert c%3==d%3==t%3==0 and M%81==0
    C,D,k,m=c//3,d//3,2*b*t//3,M//81
    sqrt_roots={}
    for a in range(81):
        if a%3:sqrt_roots.setdefault(a*a%81,[]).append(a)
    for U,V in product(range(27),repeat=2):
        f=D*V**3-C*U**3-k*U*V-m
        if f%27:continue
        fu=-3*C*U*U-k*V
        fv=3*D*V*V-k*U
        if not ((fu%3==0 and fu%9!=0) or (fv%3==0 and fv%9!=0)):continue
        X=t*9*U*V
        Y=c*27*U**3
        for a in sqrt_roots.get((X+b*b+RHO)%81,[]):
            top=(a+b)**3-a*RHO+Y
            if top%9:continue
            torig9=(top//9)*pow((b//9)*RHO,-1,9)%9
            Xb=(X//9)*pow(b//9,-1,9)%9
            # Original n numerator after dividing b must be 0 mod9.
            if (b*(torig9**2+3*torig9+2)+a*(torig9+6)-Xb)%9:continue
            assert a%3 and X%27==0
            return (U,V,a,torig9,((fu if fu%9 else fv)%9))
    raise AssertionError("No strong Hensel / 3-adic t,n witness")

def certificate_2(b,c,d,t):
    M=b*(8*b*b+9*RHO)
    if b==9:
        for u,v in product(range(32),repeat=2):
            if (d*v**3-c*u**3-6*b*t*u*v-M)%32:continue
            # a²=4 modulo32 -> 2-adic square with v2(a)=1.
            if (t*u*v+b*b+RHO)%32!=4:continue
            dfu=(-3*c*u*u-6*b*t*v)%2
            dfv=(3*d*v*v-6*b*t*u)%2
            if dfu or dfv:return (u,v,dfu,dfv)
    else:
        assert b==18 and c%2==d%2==t%2==M%2==0
        for u,v in product(range(8),repeat=2):
            f=(d//2)*v**3-(c//2)*u**3-(6*b*t//2)*u*v-M//2
            if f%8:continue
            if (t*u*v+b*b+RHO)%8!=1:continue
            dfu=(-3*(c//2)*u*u-(6*b*t//2)*v)%2
            dfv=(3*(d//2)*v*v-(6*b*t//2)*u)%2
            if dfu or dfv:return (u,v,dfu,dfv)
    raise AssertionError("No p=2 square-lift and smooth cubic witness")

def certificate_M(b,c,d,t,p):
    M=b*(8*b*b+9*RHO)
    assert p>=5 and M%p==0 and RHO%p and b%p
    ndiv=sum(z%p==0 for z in (c,d,t))
    if ndiv==3:
        t0=t//p;M0=M//p
        if (c//p)%p:
            c0=c//p
            for u in range(1,min(p,50)):
                v=(-(c0*pow(u,3,p)+M0)*pow(6*b*t0*u,-1,p))%p
                if v:break
            derivative=(-6*b*t0*u)%p
        else:
            d0=d//p
            for v in range(1,min(p,50)):
                u=((d0*pow(v,3,p)-M0)*pow(6*b*t0*v,-1,p))%p
                if u:break
            derivative=(-6*b*t0*v)%p
        assert (d*v**3-c*u**3-6*b*t*u*v-M)//p%p==0
    else:
        assert ndiv==0 and gcd(c*d*t,p)==1
        for z in range(1,p):
            den=(d*pow(z,3,p)-c)%p
            if not den or (2*d*pow(z,3,p)+c)%p==0:continue
            u=6*b*t*z*pow(den,-1,p)%p
            v=z*u%p
            square=(t*u*v+b*b+RHO)%p
            if square and pow(square,(p-1)//2,p)==1:break
        assert (d*v**3-c*u**3-6*b*t*u*v-M)%p==0
        derivative=(3*d*v*v-6*b*t*u)%p
    assert u%p and v%p and derivative%p
    square=(t*u*v+b*b+RHO)%p
    a=sqrt_mod(square,p)
    assert a is not None and a%p and (a*a-square)%p==0
    return (int(p),int(u),int(v),int(a),int(derivative))

num=0
for b in (9,18):
    M=b*(8*b*b+9*RHO)
    tps=list(cases(b))
    assert len(tps)==(6 if b==9 else 4)
    for c,d,t,e in tps:
        p2=certificate_2(b,c,d,t)
        p3=certificate_3(b,c,d,t)
        pm=[certificate_M(b,c,d,t,int(p)) for p in factorint(M) if p>=5]
        num+=1
        print("V93_BAD_PRIME_CERTIFICATE",b,e,"p2",p2,"p3",p3,"pM",pm)
assert num==10
print("PASS: all ten cubic+square systems have smooth local solutions at 2,3 and all p>=5 dividing M")
print("PASS: 3-adic original t,n integrality witnesses; 2-adic and pM-adic integrality follow from parity/unit denominators")
print("WITH V92: prime p=100003 also poses no further local cubic-cover obstruction")
print("LIMIT: no claim of all-global-integral points or of all-primes genus-four local solubility")
