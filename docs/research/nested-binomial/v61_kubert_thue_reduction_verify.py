#!/usr/bin/env python3
"""Independent symbolic verification of the Kubert 9-torsion -> 20 Thue equations.

Uses the standard Tate form E(b,c) with a rational 9-torsion point P=(0,0):
  c=t²(t−1), b=c(t²−t+1)
  y²+(1−c)xy−by=x³−bx².
The 3-torsion point 3P=(c,b−c). Its tangent has slope (t−1)(t+1).
After shifting 3P and its tangent to the origin, the coefficients are
  a1' = −(t³−3t²+1), a3' = −t³(t−1)³.
Normalizing a1'=6 gives a3= (6t(t−1)/(t³−3t²+1))³.
The rational 9-torsion necessary condition for E1_T then follows.

For t=x/y primitive, denominator D=x³−3x²y+y³ is coprime to xy(x−y).
If cube root q=r/s of 8+9rho/b² has s³|b² and b|486, s|27,
whence D|6s|162. This is a rigorous reduction to 20 Thue equations,
not an unbounded brute-force search.
"""
import sympy as s
from math import gcd

t=s.symbols("t")
c=t*t*(t-1)
b=c*(t*t-t+1)
a1=1-c
a2=-b
a3=-b
xp=c
yp=b-c
eq=s.factor(yp**2+a1*xp*yp+a3*yp-xp**3-a2*xp*xp)
assert eq==0
tangent=s.factor((3*xp*xp+2*a2*xp-a1*yp)/(2*yp+a1*xp+a3))
assert s.factor(tangent-(t-1)*(t+1))==0
aa1=s.factor(a1+2*tangent)
aa3=s.factor(2*yp+a1*xp+a3)
assert s.factor(aa1+t**3-3*t*t+1)==0
assert s.factor(aa3+t**3*(t-1)**3)==0
cprime=s.factor(216*aa3/aa1**3)
assert s.factor(cprime-(6*t*(t-1)/(t**3-3*t*t+1))**3)==0

for x in range(-35,36):
 for y in range(-35,36):
    if gcd(x,y)!=1:continue
    D=x**3-3*x*x*y+y**3
    assert gcd(abs(D),abs(x*y*(x-y)))==1
divs=[d for d in range(1,163) if 162%d==0]
assert divs==[1,2,3,6,9,18,27,54,81,162]
print("PASS: Tate 9-torsion point, 3P tangent, normalized cube coefficient identity")
print("PASS: primitive D and product coprimality in independent sanity audit")
print("PASS: exactly 20 signed Thue right-hand sides ±divisors(162)")
print("NOTE: all integral solutions of the 20 Thue equations require PARI flag1 proof")
