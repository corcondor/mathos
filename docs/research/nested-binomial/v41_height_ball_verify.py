#!/usr/bin/env python3
"""v41: a canonical-height ball excluded from integer recovery.

For P=mR+nH on the quadratic base change T=(p/b)^2-1, b|486.
Uses v35-v40 certificates for n=±1,±2, and checks remaining
n=0,±3 independently. Does not classify extra specialized points.
"""
import sympy as s
from math import isqrt
from fractions import Fraction
q=s.symbols("q"); T=q*q-1
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
def times(P,n):
    out=None
    for j in range(abs(n)):
        out=add(out,P if n>0 else (P[0],-P[1]))
    return out
height=lambda m,n:Fraction((2*m+n)**2+9*n*n,60)
assert height(1,0)==Fraction(1,15) and height(0,1)==Fraction(1,6)
assert height(1,1)-height(1,0)-height(0,1)==Fraction(1,15)

# Height < 13/6 implies |n|<=3 and |m|<=5.
# Check every lattice case via the quadratic form, no search cutoff on
# integers p or rho.
classes={}
for n in range(-3,4):
    ms=[m for m in range(-20,21) if height(m,n)<Fraction(13,6)]
    classes[n]=ms
    for m in ms:
        if n==0:assert abs(m)<=5
        elif abs(n)==1:assert abs(m)<=5
        elif n==2:assert abs(m+1)<=5  # P=(m+1)R+Q
        elif n==-2:assert abs(m-1)<=5 # P=(m-1)R-Q
        elif n==3:assert -4<=m<=1
        else:assert -1<=m<=4
assert all(height(-n//2,n)>=Fraction(13,6) for n in list(range(4,100))+list(range(-99,-3)))
assert all(height(-n//2+1,n)>=Fraction(13,6) for n in list(range(4,100))+list(range(-99,-3)))

# All six n=3 cases in the height ball have a²/b²=A/X<0 (q>1).
negative_ratios={
 -4:-(2*q-1)*(5*q+1)**2/(2*(11*q+7)),
 -3:-(q-1)*(2*q+1)/6,
 -2:-(q-1)**2*(q+1)*(2*q-1)/(2*(5*q-1)*(7*q-1)),
 -1:-(q-1)*(q+1)**2*(2*q+1)/(2*(5*q+1)*(7*q+1)),
 0:-(q+1)*(2*q-1)/6,
 1:-(2*q+1)*(5*q-1)**2/(2*(11*q-7))}
base=times(H,3)
for m,F in negative_ratios.items():
    P=add(base,times(R,m))
    assert s.cancel(A/P[0]-F)==0,(m,F)
    assert s.factor(P[1]**2-P[0]**3-B*P[0]**2-A*C*P[0]-4*A*A)==0
    assert all(F.subs(q,x)<0 for x in (s.Rational(11,10),2,10,100))
# All factors in the displayed fractions have fixed positive signs for q>1.

# Cyclic n=0, |m|<=5: for m<=2 the ratio A/X is negative, for
# m=3 X=0, and for m=4 or5 exact resultant divisors yield only
# the equality boundary a=p. This audits the latter independently.
assert s.factor(A/R[0]+T/8)==0
assert s.factor(A/times(R,2)[0]+(4*T+3)/5)==0
assert times(R,3)[0]==0
assert s.cancel(A/times(R,4)[0]-4*T*(4*T+3)/(7*T+24))==0
assert s.cancel(A/times(R,5)[0]-25*T*T/(16*(T+12)))==0
bs=[2**e*3**f for e in (0,1) for f in range(6)]
for m in (4,5):
    counts=[0,0,0,0];squares=[]
    for e in (0,1):
      for f in range(6):
        bv=2**e*3**f
        ex=(5,2,2) if m==4 else (4,2,2)
        for i in range(ex[0]+4*e+1):
         for j in range(ex[1]+4*f+1):
          for k in range(ex[2]+1):
            d=2**i*3**j*5**k;counts[0]+=1
            if m==4:
                if (d-17*bv*bv)%7:continue
                p2=(d-17*bv*bv)//7
            else:p2=d-11*bv*bv
            if p2<=bv*bv:continue
            p=isqrt(p2)
            if p*p!=p2:continue
            counts[1]+=1
            num=4*(p*p-bv*bv)*(4*p*p-bv*bv) if m==4 else 25*(p*p-bv*bv)**2
            den=d if m==4 else 16*d
            if num%den:continue
            counts[2]+=1
            a=isqrt(num//den)
            if a*a!=num//den:continue
            counts[3]+=1
            squares.append((bv,p,a))
    assert counts==({4:[3744,84,84,12],5:[3276,120,78,12]}[m]),(m,counts)
    assert sorted(squares)==sorted((bv,m//2*bv if m==4 else 5*bv,
                                     m//2*bv if m==4 else 5*bv) for bv in bs)
    print("PASS: n=0, m=%d complete divisors -> boundary a=p only"%m,counts)

print("PASS: n=±3 six nonpositive recoveries; ±1 and ±2 covered by v35-v40")
print("PASS: all P=mR+nH with height(P)<13/6 excluded in this quadratic base change")
for n,ms in classes.items():print("n",n,"allowed m:",ms)
print("Only section points in <R,H>; no claim about full E_T(Q) after specialization.")
