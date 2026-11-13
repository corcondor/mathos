#!/usr/bin/env python3
"""v43: canonical-height bound 8/3 for quadratic K3 MW sections.

New cases: 6R, 2Q, R+2Q, -R+2Q. All other h<8/3 cases
are covered by previously checked v35-v42 notes.
"""
from fractions import Fraction as F
from math import isqrt
import sympy as s
q=s.symbols("q");T=q*q-1
A=-T*T*(4*T+3);B=12*(T*T+5*T+3);C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
Q=(A/q**2,A*(9*T+8)/q**3)
def add(P,V):
    if P is None:return V
    if V is None:return P
    x,y=P;u,v=V
    if s.cancel(x-u)==0 and s.cancel(y+v)==0:return None
    t=(3*x*x+2*B*x+A*C)/(2*y) if s.cancel(x-u)==0 else (v-y)/(u-x)
    X=s.factor(s.cancel(t*t-B-x-u))
    return X,s.factor(s.cancel(t*(x-X)-y))
P=R
for _ in range(5):P=add(P,R)
assert s.cancel(A/P[0]-T*(4*T+3)/(3*(T+32)))==0
QQ=add(Q,Q)
ratios={
"2Q":4*q*q*(q-1)*(q+1)*(2*q-1)*(2*q+1)/((4*q*q-q+1)*(4*q*q+q+1)),
"R+2Q":(q-1)**2*(4*q+1)**2/(8*(q+1)*(2*q+1)),
"-R+2Q":(q+1)**2*(4*q-1)**2/(8*(q-1)*(2*q-1))}
for key,S in [("2Q",QQ),("R+2Q",add(R,QQ)),
              ("-R+2Q",add((R[0],-R[1]),QQ))]:
    assert s.cancel(A/S[0]-ratios[key])==0,key
    assert s.factor(S[1]**2-S[0]**3-B*S[0]**2-A*C*S[0]-4*A*A)==0
assert s.cancel(ratios["2Q"]-q*q+
  3*q*q*(3*q-1)*(3*q+1)/((4*q*q-q+1)*(4*q*q+q+1)))==0
assert s.cancel(ratios["R+2Q"]-q*q+
  (3*q+1)*(16*q*q-3*q-1)/(8*(q+1)*(2*q+1)))==0

p,b=s.symbols("p b")
D=p*p+31*b*b;N=(p*p-b*b)*(4*p*p-b*b)
assert s.expand(N-D*(4*p*p-129*b*b)-4000*b**4)==0
assert 4000==2**5*5**3

cyclic=[0,0,0,0];minus=[0,0,0]
for e in (0,1):
 for f in range(6):
  bv=2**e*3**f
  for i in range(6+4*e):
   for j in range(1+4*f):
    for k in range(4):
     d=2**i*3**j*5**k;cyclic[0]+=1
     p2=d-31*bv*bv
     if p2<=bv*bv:continue
     pv=isqrt(p2)
     if pv*pv!=p2:continue
     cyclic[1]+=1
     v=(pv*pv-bv*bv)*(4*pv*pv-bv*bv)
     if v%(3*d):continue
     cyclic[2]+=1
     aa=isqrt(v//(3*d))
     if aa*aa==v//(3*d):cyclic[3]+=1
  for i in range(3+4*e):
   for j in range(3+4*f):
    d=2**i*3**j;minus[0]+=1
    pv=bv+d
    v=(pv+bv)**2*(4*pv-bv)**2
    den=8*(pv-bv)*(2*pv-bv)
    if v%den:continue
    minus[1]+=1
    aa=isqrt(v//den)
    if aa*aa==v//den:minus[2]+=1
assert cyclic==[4224,79,70,0],cyclic
assert minus==[780,0,0],minus

height=lambda m,n:F((2*m+n)**2+9*n*n,60)
for n in range(-4,5):
 for m in range(-15,16):
  if height(m,n)>=F(8,3):continue
  if n==0:assert abs(m)<=6
  elif abs(n)==1:assert abs(m)<=6
  elif n==2:assert abs(m+1)<=5
  elif n==-2:assert abs(m-1)<=5
  elif n==3:assert -5<=m<=2
  elif n==-3:assert -2<=m<=5
  elif n==4:assert -3<=m<=-1
  elif n==-4:assert 1<=m<=3
  else:raise AssertionError((m,n))
assert all(height(-n//2,n)>=F(8,3) for n in range(5,50))
print("PASS: symbolic 2Q and ±R+2Q; two fail a²>p²")
print("PASS: m=6 cyclic: D|4000b^4 => 4224 divisors, 0 integer squares",cyclic)
print("PASS: -R+2Q: p-b|36b^4 => 780 divisors, 0 integer a²",minus)
print("PASS: entire generic MW height ball h<8/3 excluded by v35-v43")
print("Scope: section height over Q(q), NOT full E_T0(Q) for specialized T0")
