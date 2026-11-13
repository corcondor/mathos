#!/usr/bin/env python3
"""v36: exact symbolic and finite-certificate sieve for mR +/- Q, m=2,3,4.

Parameter family: T=(p/b)^2-1, b>0 divides 486, p>b integers.
The original binomial equation is NOT claimed solved. Rational points on the
elliptic quotient yield only necessary integer recovery conditions.
"""
from __future__ import annotations
from math import gcd, isqrt
from fractions import Fraction
import sympy as sp

q=sp.symbols("q", positive=True)
T=q*q-1
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
R=(8*T*(4*T+3), 6*T*(4*T+3)*(9*T+8))
Q=(A/q**2,A*(9*T+8)/q**3)

def E_add(P,S):
    x,y=P
    u,v=S
    if sp.cancel(x-u)==0:
        slope=sp.factor((3*x*x+2*B*x+A*C)/(2*y))
    else:
        slope=sp.factor((v-y)/(u-x))
    X=sp.factor(sp.cancel(slope*slope-B-x-u))
    Y=sp.factor(sp.cancel(slope*(x-X)-y))
    return X,Y

expect={
(2,1):((q-1)*(q+1)**2/(q-5)),
(2,-1):((q-1)**2*(q+1)/(q+5)),
(3,1):((q-1)**2*(q+1)*(4*q*q-1)/(4*q*(q*q-10*q+1))),
(3,-1):((q-1)*(q+1)**2*(4*q*q-1)/(4*q*(q*q+10*q+1))),
(4,1):((q-2)**2*(q-1)/(q-17)),
(4,-1):((q+2)**2*(q+1)/(q+17)),
}
P=R
for m in range(1,5):
    if m>1:
        P=E_add(P,R)
    if m>=2:
        for sign in (1,-1):
            point=E_add(P,(Q[0],sign*Q[1]))
            formula=sp.factor(sp.cancel(A/point[0]))
            assert sp.cancel(formula-expect[(m,sign)])==0,(m,sign,formula)
            assert sp.factor(point[1]**2-point[0]**3-B*point[0]**2-A*C*point[0]-4*A*A)==0
assert sp.cancel((sp.factor(expect[(2,-1)]-q*q))-(-(2*q+1)*(3*q-1)/(q+5)))==0
assert sp.cancel((sp.factor(expect[(3,-1)]-q*q))-(-(3*q-1)*(3*q+1)*(4*q*q+q+1)/(4*q*(q*q+10*q+1))))==0
assert sp.cancel((sp.factor(expect[(4,-1)]-q*q))-(-4*(q-1)*(3*q+1)/(q+17)))==0
assert sp.cancel((sp.factor(expect[(2,1)]-q*q))-((2*q-1)*(3*q+1)/(q-5)))==0
assert sp.cancel((sp.factor(expect[(3,1)]-q*q))-((3*q-1)*(3*q+1)*(4*q*q-q+1)/(4*q*(q*q-10*q+1))))==0
assert sp.cancel((sp.factor(expect[(4,1)]-q*q))-(4*(q+1)*(3*q-1)/(q-17)))==0

def candidates(m):
    """Purely arithmetic resultant/divisor reduction, independent of SymPy."""
    rows=[]
    tested=integral=0
    for e in (0,1):
      for f in range(6):
        b=2**e*3**f
        if m in (2,4):
            prime5range=range(1 if m==2 else 3)
            for i in range(5+3*e):
              for j in range(3+3*f):
                for h5 in prime5range:
                    d=2**i*3**j*5**h5
                    tested+=1
                    p=(5 if m==2 else 17)*b+d
                    if m==2:
                        N=(p+b)**2*(p-b)
                    else:
                        N=(p-2*b)**2*(p-b)
                    assert N%d==0,(m,b,d)
                    integral+=1
                    a2=N//d
                    a=isqrt(a2)
                    if a*a==a2:
                        rho=p*p-b*b
                        assert a2>p*p
                        rows.append((b,d,p,a,rho))
        elif m==3:
            for i in range(5*e+1):
              for j in range(5*f+1):
                p=2**i*3**j
                quadratic=p*p-10*p*b+b*b
                if not (p>b and quadratic>0):continue
                tested+=1
                N=(p-b)**2*(p+b)*(4*p*p-b*b)
                den=4*p*quadratic
                if N%den:continue
                integral+=1
                a=isqrt(N//den)
                if a*a==N//den:
                    rows.append((b,0,p,a,p*p-b*b))
    return tested,integral,sorted(rows)

def squarefactor_candidates(m):
    """Independent parametrization via reduced k/h: d=c*h² and k²-h²=L*b/c."""
    assert m in (2,4)
    shift,L,off = (5,4,6) if m==2 else (17,16,15)
    rows=[]
    for e in (0,1):
      for f in range(6):
        b=2**e*3**f
        for c in range(1,L*b+1):
            if L*b%c:continue
            z=L*b//c
            for u in range(1,isqrt(z)+1):
                if z%u:continue
                w=z//u
                if u>=w or (u+w)%2:continue
                h=(w-u)//2; k=(w+u)//2
                if gcd(h,k)!=1 or (off*b)%h:continue
                d=c*h*h
                p=shift*b+d
                a=((p+b) if m==2 else (p-2*b))*k//h
                rho=p*p-b*b
                assert a*a*d==((p+b)**2*(p-b) if m==2 else (p-2*b)**2*(p-b))
                rows.append((b,d,p,a,rho))
    return sorted(rows)

def necessary(row):
    b,d,p,a,rho=row
    return (rho>=32770 and gcd(a,b)==1 and rho%9 in (1,4,6,7)
            and gcd(a,rho)==gcd(a,3) and a*a>p*p)

counters={}
for m,expected in ((2,(819,819,25)),(3,(391,0,0)),(4,(2457,2457,81))):
    tested,integral,rows=candidates(m)
    assert (tested,integral,len(rows))==expected,(m,tested,integral,len(rows))
    if m in (2,4):
        alt=squarefactor_candidates(m)
        assert rows==alt,(m,rows,alt)
    after_three=[row for row in rows if row[4]>=32770 and gcd(row[3],row[0])==1
                 and row[4]%9 in (1,4,6,7)]
    if m==2:
        assert after_three==[(18,128,218,295,47200)],after_three
        assert gcd(295,47200)==295 and gcd(295,3)==1
    if m==4:
        assert after_three==[(18,1,307,4607,93925)],after_three
        assert gcd(4607,93925)==17 and gcd(4607,3)==1
    assert not any(necessary(row) for row in rows)
    counters[m]={"tested":tested,"integral_a_squared":integral,
                 "perfect_square_cases":len(rows),
                 "after_lower_bound_gcd_ab_and_rho_mod9":after_three,
                 "full_necessary_condition_survivors":0}
print("PASS: symbolic elliptic group law for 2R±Q,3R±Q,4R±Q")
print("PASS: 819+391+2457=3667 structural divisor tests")
print("PASS: independent coprime-square factorization confirms all 25+81 square cases")
print("PASS: only two near-survivors, both violate gcd(a,rho)=gcd(a,3)")
for m,v in counters.items():print("m=",m,v)
print("Limit: m in {2,3,4}, coefficient of Q=±1; original equation still open.")
