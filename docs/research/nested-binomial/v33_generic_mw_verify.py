#!/usr/bin/env python3
"""Exact arithmetic inputs for geometric MW theorem E_{Qbar(T)} = Z*R.
Uses Shioda-Tate and height theory as stated external theorems, not CAS axioms.
"""
import sympy as s
from fractions import Fraction

T,X,v=s.symbols("T X v")
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
f=X**3+B*X**2+A*C*X+4*A*A
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
assert s.factor(R[1]**2-f.subs(X,R[0]))==0
c4=s.factor(16*(B*B-3*A*C))
Delta=s.factor(16*s.discriminant(f,X))
assert s.expand(c4-576*(45*T**3+130*T**2+120*T+36))==0
assert s.expand(Delta+62208*T**5*(4*T+3)**2*(9*T+8)**3)==0

finite=[(s.Rational(0),5,20736),
        (-s.Rational(3,4),2,81),
        (-s.Rational(8,9),3,256)]
for t0,m,c4val in finite:
    assert c4.subs(T,t0)==c4val
    rx,ry=(s.cancel(z.subs(T,t0)) for z in R)
    assert ry==0 and f.subs({T:t0,X:rx})==0
    assert s.factor(s.diff(f,X).subs({T:t0,X:rx}))==0
    assert s.factor(s.diff(R[1],T).subs(T,t0))!=0

# At infinity: x=v^2*X, y=v^3*Y, v=1/T.
b2=s.factor(v**2*B.subs(T,1/v))
b4=s.factor(v**4*(A*C).subs(T,1/v))
b6=s.factor(v**6*(4*A*A).subs(T,1/v))
assert (b2.subs(v,0),b4.subs(v,0),b6.subs(v,0))==(12,48,64)
assert s.expand(X**3+12*X**2+48*X+64-(X+4)**3)==0
Dinf=s.factor(v**12*Delta.subs(T,1/v))
c4inf=s.factor(v**4*c4.subs(T,1/v))
assert Dinf.subs(v,0)==0 and s.simplify((Dinf/v**2).subs(v,0))!=0
assert c4inf.subs(v,0)==0 and s.simplify((c4inf/v).subs(v,0))!=0
# Type II at infinity, I5/I2/I3 at finite roots; chi=1, NS geometric rank=10.
rank=10-2-((5-1)+(2-1)+(3-1))
assert rank==1

I5=[Fraction(j*(5-j),5) for j in range(5)]
I3=[Fraction(j*(3-j),3) for j in range(3)]
I2=[Fraction(j*(2-j),2) for j in range(2)]
contributions={a+b+c for a in I5 for b in I3 for c in I2}
assert Fraction(2) not in contributions
assert max(contributions)==Fraction(71,30)
assert all((q*30).denominator==1 for q in contributions)
hR=Fraction(2)-Fraction(4,5)-Fraction(2,3)-Fraction(1,2)
assert hR==Fraction(1,30)
# If torsion P != O, h(P)=0. P.O >=1 gives h(P) >= 4-71/30>0.
# P.O=0 would require a component-correction sum=2, which is absent.
# Thus torsion=0. All nonzero heights are positive integers /30.
# Consequently R is indivisible in the rank-one geometric MW group.

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,w=Q
    if s.cancel(x-u)==0 and s.cancel(y+w)==0:return None
    slope=s.cancel((3*x*x+2*B*x+A*C)/(2*y)
                   if s.cancel(x-u)==0 else (w-y)/(u-x))
    nx=s.factor(slope*slope-B-x-u)
    ny=s.factor(slope*(x-nx)-y)
    assert s.factor(ny*ny-f.subs(X,nx))==0
    return nx,ny

P=R
for m in range(1,7):
    if m==2:assert s.factor(P[0]-5*T*T)==0
    if m==3:assert P[0]==0
    if m==4:assert s.factor(P[0]+T*(7*T+24)/4)==0
    if m!=3:
        assert s.limit(P[0]/T**2,T,s.oo)==s.Rational(36,m*m)-4
        assert s.limit(s.factor(A/P[0])/T,T,s.oo)==s.Rational(m*m,m*m-9)
    P=add(P,R)

# Explicit genus-two-to-elliptic quotient, x=A/u², y=A*sqrt(f(u,T))/u³.
u=s.symbols("u")
fu=4*u**6+C*u**4+B*u*u+A
assert s.factor((A*A/u**6)*fu-f.subs(X,A/u**2))==0
assert s.factor(fu-(6*u*u+2+3*T)**2-4*(u*u-1-T)**3)==0
assert fu.subs(u,0)==A  # A=-T²(4T+3) has a simple odd-order zero at T=-3/4.
print("PASS: invariants and fibres I5/I3/I2/II; geometric MW rank one")
print("PASS: geometric torsion=0, height(R)=1/30, R primitive")
print("PASS: genus-2 quotient and mR leading X(T) for m=1..6; odd infinity pole")
print("Scope: exact algebra and enumeration, plus cited Shioda/Neron theorems; no Lean proof")
