#!/usr/bin/env python3
"""v37: exact two-sign sieve for 5R +/- Q, on T=(p/b)^2-1 and b|486.

No arbitrary bound on p. The plus case uses a polynomial resultant-like
Bezout identity and exact divisor enumeration; minus uses an inequality bound.
No claim about all mR+nQ or about the original binomial equation.
"""
import sympy as sp
from math import isqrt

q=sp.symbols("q")
T=q*q-1
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
Q=(A/q**2,A*(9*T+8)/q**3)

def add(P,V):
    x,y=P;u,v=V
    slope=(3*x*x+2*B*x+A*C)/(2*y) if sp.cancel(x-u)==0 else (v-y)/(u-x)
    slope=sp.factor(sp.cancel(slope))
    X=sp.factor(sp.cancel(slope*slope-B-x-u))
    Y=sp.factor(sp.cancel(slope*(x-X)-y))
    return X,Y

P=R
for n in range(2,6):
    P=add(P,R)
plus=add(P,Q)
minus=add(P,(Q[0],-Q[1]))
fplus=sp.factor(sp.cancel(A/plus[0]))
fminus=sp.factor(sp.cancel(A/minus[0]))
expected_plus=(q-5)**2*(4*q*q-1)/(4*(q*q-25*q-44))
expected_minus=(q+5)**2*(4*q*q-1)/(4*(q*q+25*q-44))
assert sp.cancel(fplus-expected_plus)==0
assert sp.cancel(fminus-expected_minus)==0
assert sp.factor(plus[1]**2-plus[0]**3-B*plus[0]**2-A*C*plus[0]-4*A*A)==0
assert sp.factor(minus[1]**2-minus[0]**3-B*minus[0]**2-A*C*minus[0]-4*A*A)==0

p,b=sp.symbols("p b")
N=(p-5*b)**2*(4*p*p-b*b)
D=p*p-25*p*b-44*b*b
L=209*p+347*b
assert sp.expand(N-D*(4*p*p+60*p*b+1775*b*b)-225*b**3*L)==0
assert sp.expand(209**2*D-L*(209*p-5572*b)-11520*b*b)==0
# For integer a²=N/(4D), first D|N, then D|225*b³*L.
# Multiplying the second Bezout identity by 225*b³ proves
# D|K*b^5 where K=225*11520=2^8*3^4*5^3.
K=225*11520
assert K==2**8*3**4*5**3==2592000

plus_counts={"divisors":0,"discriminant_p":0,"integer_a2":0,"square_a2":0}
minus_counts={"interval_p":0,"integer_a2":0,"square_a2":0}
for e in (0,1):
 for f in range(6):
    bv=2**e*3**f
    assert 486%bv==0
    for i in range(8+5*e+1):
     for j in range(4+5*f+1):
      for k in range(4):
        d=2**i*3**j*5**k
        plus_counts["divisors"]+=1
        radicand=801*bv*bv+4*d
        r=isqrt(radicand)
        if r*r!=radicand or (25*bv+r)%2:
            continue
        pv=(25*bv+r)//2
        if pv<=bv or pv*pv-25*pv*bv-44*bv*bv!=d:
            continue
        plus_counts["discriminant_p"]+=1
        numerator=(pv-5*bv)**2*(4*pv*pv-bv*bv)
        denominator=4*d
        if numerator%denominator:continue
        plus_counts["integer_a2"]+=1
        z=numerator//denominator
        av=isqrt(z)
        if av*av==z:
            plus_counts["square_a2"]+=1
            raise AssertionError(("5R+Q integer square found",bv,pv,av))

    # For q>1, 5R-Q could have a²>q² only if
    # q²+25q-44>0 and 4q²-17q-5<0, implying 1<q<5.
    for pv in range(bv+1,5*bv):
        denpoly=pv*pv+25*pv*bv-44*bv*bv
        if denpoly<=0 or 4*pv*pv-17*pv*bv-5*bv*bv>=0:
            continue
        minus_counts["interval_p"]+=1
        numerator=(pv+5*bv)**2*(4*pv*pv-bv*bv)
        denominator=4*denpoly
        if numerator%denominator:continue
        minus_counts["integer_a2"]+=1
        z=numerator//denominator
        av=isqrt(z)
        if av*av==z:
            minus_counts["square_a2"]+=1
            raise AssertionError(("5R-Q integer square found",bv,pv,av))

assert plus_counts=={"divisors":9660,"discriminant_p":136,
                     "integer_a2":42,"square_a2":0},plus_counts
assert minus_counts=={"interval_p":3141,"integer_a2":22,"square_a2":0},minus_counts
print("PASS: symbolic group law and two rational recovery formulae for 5R±Q")
print("PASS: exact polynomial Bezout gives D | 2592000*b^5 in the plus case")
print("PASS: plus 9660 complete divisors -> 136 integer p -> 42 integral a² -> 0 squares")
print("PASS: minus 3141 bounded p -> 22 integral a² -> 0 squares")
print("Therefore neither 5R+Q nor 5R-Q can recover a positive integer a.")
print("Scope: b|486, T=(p/b)^2-1; arbitrary p>b; original equation remains open.")
