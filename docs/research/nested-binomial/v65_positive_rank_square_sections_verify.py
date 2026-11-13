#!/usr/bin/env python3
"""v65: two polynomial square-cover sections on the positive-rank first quotient.

Independent SymPy identities and integer resultant/divisor certificates.
No claim of full classification of all positive-rank E1(Q) or C_T(Q).
"""
from math import gcd, isqrt
import sympy as s

x,u,a,b,k=s.symbols("x u a b k")
c=s.factor((x*x-k*(k+6)*x)/k)
T=s.factor((c-8)/9)
U2=s.factor(x+1+T)
assert s.factor(U2-(x*x+k*(3-k)*x+k)/(9*k))==0
quad=x*x+k*(3-k)*x+k
assert s.factor(s.discriminant(quad,x)-k*(k-1)**2*(k-4))==0
assert s.factor(k*(3-k)**2-4)==(k-1)**2*(k-4)
# Only k=1,4 give identically polynomial-square u(x).
print("PASS: only constant slopes y=kx with polynomial square cover are k=1,4")

for slope,tt,xx,ss in (
    (1,u*(u-3),3*u-1,3*u*(3*u-1)),
    (4,u*u-6*u-3,6*u+2,3*(u+3)*(3*u+1))
):
    C=8+9*tt
    y=slope*xx
    f=(6*u*u+2+3*tt)**2+4*(u*u-1-tt)**3
    assert s.factor(y*y+6*xx*y+C*y-xx**3)==0
    assert s.factor(xx-u*u+1+tt)==0
    assert s.factor(ss*ss-f)==0
    tm=s.factor((2*u*(u*u+3)-tt*(3+2*u)-ss)/(2*tt))
    tp=s.factor((2*u*(u*u+3)-tt*(3+2*u)+ss)/(2*tt))
    nm=s.factor((tm*tm+3*tm+3+u*(tm+6)-u*u+tt)/(9*u))
    np=s.factor((tp*tp+3*tp+3+u*(tp+6)-u*u+tt)/(9*u))
    if slope==1:
        assert tm==-3 and nm==1/(3*u)
        assert s.factor(tp-6*(u+1)/(u-3))==0
    else:
        assert tm==0 and nm==0
        assert s.factor(tp-3*(u+3)*(3*u+1)/tt)==0
        assert s.factor(np-(u+3)**3*(3*u+1)/(3*tt**2))==0
print("PASS: both affine genus-two sections and both exact t,n recovery signs")

rho=a*a-6*a*b-3*b*b
G=3*(a+3*b)*(3*a+b)
L=7*a+3*b
assert s.factor(G-9*rho-12*b*L)==0
assert s.factor(L*L-48*b*L-49*rho-12*b*b)==0
assert s.factor(s.resultant(rho,G,a)+1728*b**4)==0
# t=G/rho integer -> rho|12bL. The second identity implies
# rho|(12b)^2*(L^2-48bL)=1728*b^4, while gcd(rho,b)=1 if gcd(a,b)=1.
# Therefore rho | 1728 for EVERY original integer lift on k=4 section.
bs=[v for v in range(1,487) if 486%v==0]
ds=s.divisors(1728)
assert len(bs)==12 and len(ds)==28
primitive=[]; lifted=[]
for bb in bs:
    for rr in ds:
        square=12*bb*bb+rr
        root=isqrt(square)
        if root*root!=square:continue
        aa=3*bb+root
        if gcd(aa,bb)!=1:continue
        assert aa*aa-6*aa*bb-3*bb*bb==rr
        primitive.append((aa,bb,rr))
        tv=s.Rational(3*(aa+3*bb)*(3*aa+bb),rr)
        nv=s.Rational((aa+3*bb)**3*(3*aa+bb),3*rr*rr)
        if tv.q==1 and nv.q==1:
            lifted.append((aa,bb,rr,int(tv),int(nv)))
assert sorted(primitive)==[(7,1,4),(9,1,24),(13,2,1)]
assert lifted==[(9,1,24,42,28)]
print("PASS: resultant rho|1728, 12*28=336 structural cases, only integral t,n is (9,1,24,42,28)")
print("PASS: n=28<104, so the entire rank-positive polynomial section is excluded")

# Prove for every integer u>=7 except u=9 that the first quotient is
# positive rank. E1 has a point of exact order 3, and Delta<0.
# Mazur then restricts rational torsion to cyclic 3,6,9,12.
# x(P)=6u+2>0 excludes order3, Y(P)>0 excludes order2;
# x(2P)=0 is possible only at u=9 (order6).
# Order9 would require x(3P)=0, which has no integer root u>=7.
# Order12 requires x(4P)=0, and order4 requires 4P=O.
v=s.symbols("v")
t0=v*v-6*v-3
C0=8+9*t0
X0=6*v+2
Y0=s.factor(7*X0+C0/2)
assert s.factor(Y0-s.Rational(3,2)*(v+3)*(3*v+1))==0
P=(X0,Y0)
B0=s.Integer(9)
A0=3*C0
D0=C0*C0/4
def add(P,Q):
    x0,y0=P;x1,y1=Q
    slope=s.cancel((3*x0*x0+2*B0*x0+A0)/(2*y0)
                   if s.cancel(x0-x1)==0 else (y1-y0)/(x1-x0))
    x2=s.factor(s.cancel(slope*slope-B0-x0-x1))
    y2=s.factor(s.cancel(slope*(x0-x2)-y0))
    assert s.factor(y2*y2-(x2**3+B0*x2*x2+A0*x2+D0))==0
    return x2,y2
P2=add(P,P)
P3=add(P2,P)
P4=add(P3,P)
X2=-4*(v-9)*(v-3)*(3*v+1)/(v+3)**2
X3=((v-5)*(v-1)*(v*v-18*v-15)*(v*v+6*v-87)
    /(4*(v*v-6*v+21)**2))
Q4=v**4-48*v**3+426*v*v-1224*v+333
G4=v**4+24*v**3-222*v*v+432*v-747
X4=(8*(v-9)*(v-3)*(3*v+1)*t0*(v*v-6*v+69)*G4
    /((v+3)**2*Q4**2))
for actual,expected in ((P2[0],X2),(P3[0],X3),(P4[0],X4)):
    assert s.factor(s.cancel(actual-expected))==0
assert s.discriminant(v*v-18*v-15,v)==384
assert s.discriminant(v*v+6*v-87,v)==384
assert all(Q4.subs(v,d)!=0 for d in s.divisors(333) if d>=7)
assert G4.subs(v,7)==2032
for derivative in (1,2,3,4):
    assert s.diff(G4,v,derivative).subs(v,7)>0
# These facts establish no integer u>=7 can give order 4,9 or12,
# and order6 occurs only at u=9. Not based on a bounded search.
assert P2[0].subs(v,9)==0
print("PASS: for EVERY integer u>=7 except 9, the section point has infinite order")

ex=320
res=ex*ex-6*ex-3
assert res==100477 and res%9 in (1,4,6,7)
assert gcd(ex,res)==gcd(ex,3)
assert (res-ex-1)%2==0
assert (3*(ex+3)*(3*ex+1))%res!=0
print("PASS: u=320 gives rho=100477, positive-rank affine point meeting preliminary congruences but nonintegral t")
print("ALL v65 CHECKS PASSED; original nested-binomial equation remains open.")
