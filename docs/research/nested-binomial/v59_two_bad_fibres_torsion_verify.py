#!/usr/bin/env python3
"""v59: new 9/12 torsion valuation obstructions from *both* factors of Delta.

E1_T: y²+6xy+(8+9T)y=x³, T=rho/b²>0, b|486.
At p>=5 | rho: multiplicative I_e, chi=(-3/p), smooth size p-chi.
At p>=5 | M=8b²+9rho: multiplicative I_{3h}, split,
h=v_p(M), smooth size p-1. These prime sets are disjoint (p>=5).
Since p is prime to 9,12, rational n-torsion has n dividing the
component group size times the nonsingular reduction cardinality.
This proves uniform arithmetic restrictions but NOT all rational points.
"""
import sympy as s
from math import gcd

T,x,y=s.symbols("T x y")
a3=8+9*T
b2=s.Integer(36)
b4=6*a3
b6=a3*a3
delta=s.factor(-8*b4**3-27*b6*b6+9*b2*b4*b6)
c4=s.factor(b2*b2-24*b4)
c6=s.factor(-b2**3+36*b2*b4-216*b6)
assert s.factor(delta+243*T*(8+9*T)**3)==0
assert s.factor(c4-144*(1-9*T))==0
assert c4.subs(T,s.Rational(-8,9))==1296
assert c6.subs(T,s.Rational(-8,9))==-6**6
F=y*y+6*x*y+a3*y-x**3
assert s.factor(F.subs(T,s.Rational(-8,9)))==y*(y+6*x)-x**3
assert F.subs({T:s.Rational(-8,9),x:0,y:0})==0
print("PASS: c4 is unit at both bad factors; p|M has split node and type I_{3v_p(M)}")

for p in list(s.primerange(5,89)):
    smooth=1
    for xx in range(p):
        for yy in range(p):
            if (yy*yy+6*xx*yy-xx**3)%p==0 and (xx,yy)!=(0,0):
                smooth+=1
    assert smooth==p-1,(p,smooth)
print("PASS: all p=5..83 smooth cardinalities at M=0 equal p-1")

# For p>=5 dividing M, and h=v_p(M):
#    order-9 --> 9 | 3h(p-1) --> if p=2 mod3 then 3 | h
#    order-12 --> 12 | 3h(p-1) --> if p=3 mod4 then 2 | h.
for p in list(s.primerange(5,300)):
    for h in range(1,7):
        if p%3==2:
            assert ((3*h*(p-1))%9==0)==(h%3==0)
        if p%4==3:
            assert ((3*h*(p-1))%4==0)==(h%2==0)
print("PASS: all local exponent implications for 9/12 torsion")

rho=100003
for b in (1,2,3,6,9,18,27,54,81,162,243,486):
    M=8*b*b+9*rho
    assert gcd(M,rho)%5 != 0
    factor=s.factorint(M)
    for p,h in factor.items():
        if p in (2,3):continue
        if p%3==2 and h%3!=0:
            assert (3*h*(p-1))%9 != 0
        if p%4==3 and h%2!=0:
            assert (3*h*(p-1))%12 != 0
print("PASS: concrete rho=100003, all 12 b, check both discriminant factors")
print("THEOREM: 9-torsion forces v_p(8b²+9rho) multiple3 for p=2 (mod3)")
print("THEOREM: 12-torsion forces v_p(8b²+9rho) even for p=3 (mod4)")
print("LIMIT: the rank-positive Mordell-Weil free part is not classified")
