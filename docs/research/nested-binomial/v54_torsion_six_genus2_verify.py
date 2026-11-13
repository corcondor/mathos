#!/usr/bin/env python3
"""Exact torsion-six extension of genus-two rational-point classification.

If E1_T(Q) has rank0 and torsion Z/6, with 3-torsion P=(0,0)
and 2-torsion S=(-v²,-v³) for a3=2v²(v+3), then all C_T(Q)
points come from O, ±P, S, S±P. This verifier checks the maps and
T=24,v=4 example. Sage rank proof is separate.
"""
import sympy as s
from math import gcd

v=s.symbols('v')
a3=2*v*v*(v+3)
T=(a3-8)/9
X=2*v*(v+3)
h=6*X+a3
Y=-4*v*(v+3)**2
ss=s.factor(2*Y+h)
assert s.factor(ss+6*v*(v+3)*(v+2))==0
assert s.factor(1+T-v*v-(v-1)**2*(2*v+1)/9)==0
assert s.factor(1+T+X-(1+2*v*(v+3)*(v+9))/9)==0
assert s.factor(Y*Y+6*X*Y+a3*Y-X**3)==0
assert s.factor((-v**3)**2+6*(-v**2)*(-v**3)+a3*(-v**3)-(-v**2)**3)==0
assert s.factor(2*(-v**3)+6*(-v**2)+a3)==0
print('PASS: P order3, S order2, S+P x/y and genus-two lift identities')

def Ecount(t,p):
    aa=8+9*t
    Delta=-243*t*aa**3
    assert Delta%p
    total=1
    for x in range(p):
        d=((6*x+aa)**2+4*x*x*x)%p
        total+=1 if d==0 else 2 if pow(d,(p-1)//2,p)==1 else 0
    return total

assert Ecount(24,5)==6 and Ecount(24,11)==12
assert gcd(6,12)==6 and 12%5 and 6%11
print('PASS: E1_24(Q)_tors exactly Z/6 by two good reductions')

def sextic(u,t):
    return (6*u*u+2+3*t)**2+4*(u*u-1-t)**3

points=[(u,ss) for u in (-5,5) for ss in (-224,224)]
points.extend((u,0) for u in (-3,3))
points.extend((u,ss) for u in (-9,9) for ss in (-1008,1008))
assert len(points)==10 and len(set(points))==10
assert all(sextic(u,24)==ss*ss for u,ss in points)
print('PASS: ten explicit affine rational C_24 points',points)
print('CONDITIONAL: if Sage proves rank E1_24=0, all C_24(Q) are these 10 + 2 infinities')
