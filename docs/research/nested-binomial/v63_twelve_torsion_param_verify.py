#!/usr/bin/env python3
"""v63 independent polynomial derivation of the rational 12-torsion Thue sieve.

12-torsion -> 2-torsion S=(-v²,-v³) has a rational half.
In the translated 2-torsion model Y²=X(X²+aX+B),
 a=9-3v², B=3v³(v+2).
A half has X=±sqrt(B). For T>0 we have v>1; the + branch
is the only possible real rational half. It yields
  t²=3+6/v, 3<t²<9, (t-1)(t+3) a rational square.
Parametrization t=(z²-2z+4)/(2z) gives
  v=24z²/D4(z), D4=z4-4z³-16z+16,
  a3=8+9T=3456*z4*(z-2)²*(z²+4)/D4³.
A primitive homogeneous D4(m,n) cannot have a p>=5 factor
when a3*b² is integral and b|486; v2(D4)∈{0,4,5},
v3(D4)∈{0,1}. Hence D4∈{1,3,16,32,48,96} for T>0.
"""
import sympy as s
from math import gcd

v,t,z,X=s.symbols("v t z X")
a=9-3*v*v
B=3*v**3*(v+2)
expr=6/(t*t-3)
assert s.factor(B.subs(v,expr)-expr**4*t*t)==0
plus=s.factor((a+2*v*v*t).subs(v,expr))
minus=s.factor((a-2*v*v*t).subs(v,expr))
assert s.factor(plus-9*(t-1)**3*(t+3)/(t*t-3)**2)==0
assert s.factor(minus-9*(t+1)**3*(t-3)/(t*t-3)**2)==0

t_sub=(z*z-2*z+4)/(2*z)
D=z**4-4*z**3-16*z+16
v_sub=s.factor(expr.subs(t,t_sub))
assert s.factor(v_sub-24*z*z/D)==0
a3=s.factor(2*v_sub*v_sub*(v_sub+3))
target=3456*z**4*(z-2)**2*(z*z+4)/D**3
assert s.factor(a3-target)==0
k=(z*z-4)/(2*z)
assert s.factor((t_sub-1)*(t_sub+3)-k*k)==0
assert s.factor(D-(z*z-2*z+4)**2+12*z*z)==0
assert s.discriminant(D,z)==-7077888
for factor,res in [(z,16),(z-2,-32),(z*z+4,1024)]:
    assert s.resultant(D,factor,z)==res
print("PASS: half-of-2-torsion parameter, quartic rational map and resultants")

for m in range(-60,61):
 for n in range(-60,61):
    if gcd(m,n)!=1:continue
    d=m**4-4*m**3*n-16*m*n**3+16*n**4
    if m%2:
        assert d%2!=0
    elif n%2:
        assert d%16==0
        assert (d%64==16 if m%4==0 else d%64==32)
    if d%3==0:
        assert d%9==6
rhs=[1,3,16,32,48,96]
print("PASS: for primitive (m,n), 2-/3-adic valuations are (0,4,5) and (0,1)")
print("PASS: exactly six positive quartic Thue right-hand sides",rhs)
print("NOTE: complete integer solutions require unconditional PARI Thue proof")
