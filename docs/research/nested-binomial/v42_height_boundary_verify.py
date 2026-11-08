#!/usr/bin/env python3
"""Exact v42 boundary h=13/6: 6R-H,2R+3H,-5R+3H.

No arbitrary cutoff on p: use polynomial resultants in p to show
D(p,b) divides K*b^8, then enumerate the finite divisors.
"""
import sympy as s
from math import isqrt,gcd
q=s.symbols("q");T=q*q-1
A=-T*T*(4*T+3);B=12*(T*T+5*T+3);C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
H=(-2*(q-1)*(q+1)**2*(2*q+1),
   6*(q-1)*(q+1)**2*(2*q+1)*(3*q-1))
def add(P,V):
    if P is None:return V
    if V is None:return P
    x,y=P;u,v=V
    if s.cancel(x-u)==0 and s.cancel(y+v)==0:return None
    t=(3*x*x+2*B*x+A*C)/(2*y) if s.cancel(x-u)==0 else (v-y)/(u-x)
    xx=s.factor(s.cancel(t*t-B-x-u))
    return xx,s.factor(s.cancel(t*(x-xx)-y))
def mul(P,n):
    V=None
    for i in range(abs(n)):
        V=add(V,P if n>0 else (P[0],-P[1]))
    return V
forms={
"6R-H":(6,-1,(q-7)**2*(q+1)*(2*q-1)/(2*(q*q-30*q-79))),
"2R+3H":(2,3,(q-1)*(2*q-1)*(7*q+1)**2/(2*(13*q*q-10*q+13))),
"-5R+3H":(-5,3,(q+1)*(2*q+1)*(7*q-1)**2/(2*(13*q*q+10*q+13)))}
for name,(m,n,formula) in forms.items():
    P=add(mul(R,m),mul(H,n))
    assert s.cancel(A/P[0]-formula)==0,(name,s.factor(A/P[0]))
    assert s.factor(P[1]**2-P[0]**3-B*P[0]**2-A*C*P[0]-4*A*A)==0

p,b=s.symbols("p b")
numerators={
"6R-H":(p-7*b)**2*(p+b)*(2*p-b),
"2R+3H":(p-b)*(2*p-b)*(7*p+b)**2,
"-5R+3H":(p+b)*(2*p+b)*(7*p-b)**2}
denominators={
"6R-H":p*p-30*p*b-79*b*b,
"2R+3H":13*p*p-10*p*b+13*b*b,
"-5R+3H":13*p*p+10*p*b+13*b*b}
Kvals={"6R-H":1036800000,"2R+3H":373248000,"-5R+3H":373248000}
fac={"6R-H":(12,4,5),"2R+3H":(12,6,3),"-5R+3H":(12,6,3)}
for name in forms:
    assert s.factor(s.resultant(numerators[name],denominators[name],p))==Kvals[name]*b**8
assert 1036800000==2**12*3**4*5**5
assert 373248000==2**12*3**6*5**3

out={}
for name in forms:
    i0,j0,k0=fac[name]
    stats={"divisors":0,"integer_p":0,"strict_boundary":0,
           "integer_a2":0,"square_a2":0}
    squares=[];near=[]
    for e in (0,1):
      for f in range(6):
        bv=2**e*3**f
        for i in range(i0+8*e+1):
         for j in range(j0+8*f+1):
          for k in range(k0+1):
            d=2**i*3**j*5**k
            stats["divisors"]+=1
            if name=="6R-H":
                r=isqrt(304*bv*bv+d)
                if r*r!=304*bv*bv+d:continue
                pv=15*bv+r
            else:
                rad=13*d-144*bv*bv
                if rad<0:continue
                r=isqrt(rad)
                if r*r!=rad:continue
                np=(5*bv+r) if name=="2R+3H" else (r-5*bv)
                if np%13:continue
                pv=np//13
            if pv<=bv:continue
            assert int(denominators[name].subs({p:pv,b:bv}))==d
            stats["integer_p"]+=1
            N=int(numerators[name].subs({p:pv,b:bv}))
            if N<=2*d*pv*pv:continue
            stats["strict_boundary"]+=1
            if N%(2*d):continue
            stats["integer_a2"]+=1
            av=isqrt(N//(2*d))
            if av*av!=N//(2*d):continue
            stats["square_a2"]+=1
            rho=pv*pv-bv*bv
            squares.append((bv,pv,av,rho))
            if rho>=32770 and gcd(av,bv)==1 and rho%9 in (1,4,6,7):
                near.append((bv,pv,av,rho,gcd(av,rho),gcd(av,3)))
    expected={
       "6R-H":(30600,202,202,148,0),
       "2R+3H":(22032,60,60,30,12),
       "-5R+3H":(22032,24,24,24,0)}[name]
    assert tuple(stats.values())==expected,(name,stats)
    if name=="2R+3H":
        assert sorted(squares)==sorted((2**e*3**f,5*2**e*3**f,
                     9*2**e*3**f,24*(2**e*3**f)**2)
                     for e in (0,1) for f in range(6))
    assert near==[],(name,near)
    out[name]=stats
    print("PASS",name,stats)
print("PASS: h=13/6 boundary completely excluded; next h=34/15 already covered by v37")
print("SCOPE: only generic K3 sections at T=(p/b)^2-1, not new specialized points.")
