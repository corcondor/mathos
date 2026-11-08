#!/usr/bin/env python3
"""v83: exact local obstructions prune v80's 30 cubic-core coefficient types.

Fixed rho=100003; b=9 or 18. All original integer lifts lie on
d*v^3-c*u^3=6*b*t*u*v+M, X=t*u*v, a^2=X+b^2+rho,
where c*d=t^3. The full types are constructed from the primes of M.

For b=9, direct F7 enumeration of both the cubic and a-square
conditions eliminates six of the 18 types.
For b=18, p=100291||M, if p divides none of c,d,t then p cannot
divide u or v (otherwise v79's gcd(U,V)^2|M^3 would fail).
Then z=v/u is a nonzero Fp root of d*z^3-6*b*t*z-c.
The exact polynomial gcd with z^p-z eliminates 3 of four p-free types.

These are NECESSARY local conditions only: 21 cover types remain.
"""
from itertools import product
from math import gcd
from sympy import factorint

RHO=100003
def cores(b):
    M=b*(8*b*b+9*RHO)
    primes=sorted(int(p) for p in factorint(M))
    for indices in product((0,1,2),repeat=len(primes)):
        es=dict(zip(primes,indices))
        if es.get(3,0)==0 or (b%2==0 and es.get(2,0)==0):
            continue  # proven v80 conditions for original solutions
        c=d=t=1
        for p,e in es.items():
            if e==1:c*=p;d*=p*p;t*=p
            if e==2:c*=p*p;d*=p;t*=p
        assert c*d==t**3
        yield c,d,t,es

def f7_possible(b,c,d,t):
    p=7;M=b*(8*b*b+9*RHO)
    squares={x*x%p for x in range(p)}
    return any((d*v**3-c*u**3-6*b*t*u*v-M)%p==0 and
            (t*u*v+b*b+RHO)%p in squares
            for u in range(p) for v in range(p))

def trim(poly,p):
    poly=[x%p for x in poly]
    while len(poly)>1 and poly[-1]==0:poly.pop()
    return poly

def rem(a,b,p):
    a=trim(a,p);b=trim(b,p)
    while a!=[0] and len(a)>=len(b):
        lead=a[-1]*pow(b[-1],-1,p)%p
        off=len(a)-len(b)
        for i,x in enumerate(b):a[off+i]=(a[off+i]-lead*x)%p
        a=trim(a,p)
    return a

def mul(a,b,g,p):
    prod=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):prod[i+j]=(prod[i+j]+x*y)%p
    return rem(prod,g,p)

def powmod(a,n,g,p):
    z=[1]
    while n:
        if n&1:z=mul(z,a,g,p)
        a=mul(a,a,g,p);n//=2
    return z

def root_at_100291(b,c,d,t):
    p=100291
    assert gcd(p,c*d*t)==1
    inv=pow(d,-1,p)
    g=[(-c*inv)%p,(-6*b*t*inv)%p,0,1]
    z=powmod([0,1],p,g,p)
    z=trim([z[0]]+([(z[1]-1)%p] if len(z)>1 else [p-1])+z[2:],p)
    a=g[:]
    while z!=[0]:a,z=z,rem(a,z,p)
    has=len(a)>1
    # Independent brute-force validation of polynomial-gcd certificate.
    brute=any((d*pow(i,3,p)-6*b*t*i-c)%p==0 for i in range(p))
    assert has==brute
    return has

items9=list(cores(9));items18=list(cores(18))
assert len(items9)==18 and len(items18)==12
excluded9=[es for c,d,t,es in items9 if not f7_possible(9,c,d,t)]
assert len(excluded9)==6,excluded9
remaining9=[es for c,d,t,es in items9 if f7_possible(9,c,d,t)]
p0=[(c,d,t,es) for c,d,t,es in items18 if es[100291]==0]
assert len(p0)==4
excluded18=[es for c,d,t,es in p0 if not root_at_100291(18,c,d,t)]
assert len(excluded18)==3,excluded18
remaining18=[es for c,d,t,es in items18 if es not in excluded18]
assert len(remaining9)==12 and len(remaining18)==9
print("PASS: modulo-7 cubic/square condition excludes 6 of 18 b=9 cubic cores")
print("PASS: polynomial gcd in F_100291 eliminates 3 of 12 b=18 cores")
print("PASS: exact original-integer-lift cubic core coefficient types: 12+9=21 remaining")
print("EXCLUDED_b9",excluded9)
print("EXCLUDED_b18",excluded18)
print("LIMIT: 21 cubic covers remain; full integral-point classification not yet obtained")
