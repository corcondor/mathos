#!/usr/bin/env python3
"""v66: prime-5 square obstruction for original integer lifts of ANY rational point.

The preceding v28 T=1 mod5 result concerned a cyclic subgroup.
This proof uses the full genus-two sextic F(a,b,rho), assuming ONLY
b|486 (so b is a 5-adic unit) and S²=F. No MW subgroup or height bound.
"""
from math import gcd
import sympy as s

u,T=s.symbols('u T')
f=s.expand((6*u*u+2+3*T)**2+4*(u*u-1-T)**3)
square_mod5={0,1,4}
table={}
for t in range(5):
    row=[]
    for a in range(5):
        val=int(f.subs({u:a,T:t}))%5
        row.append(val)
    table[t]=row
assert table=={
    0:[0,4,4,4,4],
    1:[3,2,3,3,2],
    2:[1,4,3,3,4],
    3:[0,1,0,0,1],
    4:[1,4,0,0,4],
},table
# For T=1, all x=u² in {0,1,4} yield non-square (3,2,3).
assert all(x not in square_mod5 for x in table[1])
# For T=2, exclude u≡±2: those values are 3 (nonsquare).
assert [a for a in range(5) if table[2][a] not in square_mod5]==[2,3]
print("PASS: full normalized F/b^6 residue table for all 25 (u,T) mod5")

bs=[x for x in range(1,487) if 486%x==0]
assert len(bs)==12
for b in bs:
    assert gcd(b,5)==1
    invb=pow(b,-1,5)
    for rho in range(5):
        normalized_t=rho*pow(b*b,-1,5)%5
        for a in range(5):
            numerator=int(s.cancel((b**6)*f.subs({u:s.Rational(a,b),T:s.Rational(rho,b*b)})))
            # Integral polynomial F(a,b,rho), independent of rational scaling:
            F=(4*a**6+(24*b*b-12*rho)*a**4
               +(36*b**4+60*b*b*rho+12*rho*rho)*a*a
               -3*b*b*rho*rho-4*rho**3)
            assert numerator==F
            reduced=F*pow(b**6,-1,5)%5
            assert reduced==table[normalized_t][a*invb%5]
            if rho%5==(b*b)%5:
                assert reduced not in square_mod5
            if rho%5==(2*b*b)%5 and a%5 in ((2*b)%5,(-2*b)%5):
                assert reduced not in square_mod5
print("PASS: for all b|486, rho≡b² (mod5) is impossible for an integral genus-two square lift")
print("PASS: for rho≡2b² (mod5), a≢±2b (mod5) is necessary")
print("Scope: every original-integer-solution point, not only <R>,<R,H> or rank-zero fibres")
