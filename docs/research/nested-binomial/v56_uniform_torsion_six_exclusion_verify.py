#!/usr/bin/env python3
"""Uniform exclusion of rank-zero first quotient with torsion Z/6.

No arbitrary upper bound on rho, a, t, n or the rational 2-torsion parameter
v is used. The original branch has b|486, n>=104, t>0 and the v20 exact
integer-recovery identities. For T>0 and rational 2-torsion S=(-v²,-v³),
v>1 and T=2(v-1)(v+2)²/9.

If the first quotient's full rational group is Z/6, the original positive
x=u²-1-T forces an image at S+P or S-P, P=(0,0) order 3.
The minus lift has t<0 (1<v<4) or n<0 (v>4), with t=n=0 at v=4.
The plus lift has n<104 for v>=5.
For 1<v<5, v=m/d reduced and integer rho=b²T implies d³|2b²,
leaving 588 (b,v) pairs and only v=4 satisfying the rational-square lift.
For v=4, n=28 (or 0), never n>=104.
"""
from fractions import Fraction as F
from math import gcd,isqrt
import sympy as sp

v,w=sp.symbols('v w')
D=1+2*v*(v+3)*(v+9)
T=2*(v-1)*(v+2)**2/9
u=w/3
ss=6*v*(v+3)*(v+2)

def eq_mod_curve(a,b):
    numerator=sp.fraction(sp.together(a-b))[0]
    rem=sp.rem(sp.Poly(numerator,w),sp.Poly(w*w-D,w))
    assert rem.is_zero,sp.factor(rem.as_expr())

tminus=3*((v+1)*w-5*v*v-14*v+1)/((v-1)*(v+2))
tplus=3*((v+1)*w+4*v*v+13*v+1)/((v-1)*(v+2))
Am=12*v**5+176*v**4+712*v**3+918*v**2+124*v+2
Bm=v**4+32*v**3+111*v**2+74*v-2
Ap=6*v**5+88*v**4+356*v**3+459*v**2+62*v+1
Bp=v**4+17*v**3+54*v**2+35*v+1
nminus=(Am-Bm*w)/(w*(v-1)**2*(v+2)**2)
nplus=2*(Ap+Bp*w)/(w*(v-1)**2*(v+2)**2)
for sign,tf,nf in [(-1,tminus,nminus),(1,tplus,nplus)]:
    t=(2*u*(u*u+3)-T*(3+2*u)+sign*ss)/(2*T)
    n=(t*t+3*t+3+u*(t+6)-u*u+T)/(9*u)
    eq_mod_curve(t,tf)
    eq_mod_curve(n,nf)
print('PASS: exact original integer t,n recovery for both Z/6 torsion lifts')

Fminus=5*v*v+14*v-1
assert sp.factor(Fminus**2-(v+1)**2*D)==-v*(v-4)*(v-1)*(v+3)*(2*v+7)
assert sp.factor((Am**2-Bm**2*D)+v*(v-4)**3*(v-1)**2*(v+3)**2*D)==0
# For 1<v<4, t_minus<0; for v>4, n_minus<0; at v=4 both zero.
assert sp.expand((D-v*v)-(2*v**3+23*v*v+54*v+1))==0
# w>v for v>1. Hence nplus<104 for v>=5 if P(v)>0.
P=sp.expand(104*v*(v-1)**2*(v+2)**2-2*(Ap+v*Bp))
h=sp.symbols('h')
poly=sp.Poly(sp.expand(P.subs(v,h+5)),h)
assert all(coef>0 for coef in poly.all_coeffs())
assert sp.expand(P.subs(v,h+5))==(
    90*h**5+2248*h**4+21328*h**3+93816*h*h+181600*h+104848)
print('PASS: minus sign fails t>0 or n>0; plus sign has n<104 for v>=5')

bs=[b for b in range(1,487) if 486%b==0]
assert bs==[1,2,3,6,9,18,27,54,81,162,243,486]
tested=0;squares=[];distinct=set()
for b in bs:
    for d in range(1,55):
        if (2*b*b)%(d**3):continue
        for m in range(d+1,5*d):
            if gcd(m,d)!=1:continue
            tested+=1
            vv=F(m,d)
            distinct.add(vv)
            w2=1+2*vv*(vv+3)*(vv+9)
            p=isqrt(w2.numerator);q=isqrt(w2.denominator)
            if p*p==w2.numerator and q*q==w2.denominator:
                squares.append((b,m,d,F(p,q)))
assert tested==588,tested
assert len(distinct)==215,len(distinct)
assert squares==[(b,4,1,F(27)) for b in bs],squares
print('PASS: 588 structural (b,v) pairs, 215 distinct v, only v=4 is square')

for b in bs:
    ww=F(27);tt=F(24);uu=ww/3
    for sign,t_expected,n_expected in [(-1,F(0),F(0)),(1,F(42),F(28))]:
        t=(2*uu*(uu*uu+3)-tt*(3+2*uu)+sign*F(6*4*7*6))/(2*tt)
        n=(t*t+3*t+3+uu*(t+6)-uu*uu+tt)/(9*uu)
        assert (t,n)==(t_expected,n_expected)
        assert n<104
print('PASS: only v=4 has (t,n)=(0,0) or (42,28), never n>=104')
print('THEOREM: no original-branch integer solution if E1_T(Q)=Z/6')
print('Limit: positive-rank first quotients and rank-zero torsion 9/12 not covered')
