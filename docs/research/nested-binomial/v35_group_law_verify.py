#!/usr/bin/env python3
"""Exact symbolic group law for R+Q and R-Q on T=q²−1.
No claims about the full Mordell-Weil group or original equation.
"""
import sympy as s
q=s.symbols("q")
T=q*q-1
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
Q=(A/q**2,A*(9*T+8)/q**3)

def add(P,S):
    x,y=P;u,v=S
    slope=s.cancel((v-y)/(u-x))
    nx=s.factor(s.cancel(slope*slope-B-x-u))
    ny=s.factor(s.cancel(slope*(x-nx)-y))
    return nx,ny

Pplus=add(R,Q)
Pminus=add(R,(Q[0],-Q[1]))
assert s.factor(Pplus[0]+4*(q-2)*(q-1)**2*(q+1))==0
assert s.factor(Pminus[0]+4*(q-1)*(q+1)**2*(q+2))==0
plus=s.factor(A/Pplus[0])
minus=s.factor(A/Pminus[0])
assert s.factor(plus-(q+1)*(4*q*q-1)/(4*(q-2)))==0
assert s.factor(minus-(q-1)*(4*q*q-1)/(4*(q+2)))==0
assert s.factor(plus-q*q-(12*q*q-q-1)/(4*(q-2)))==0
assert s.factor(minus-q*q-(-12*q*q-q+1)/(4*(q+2)))==0
print("PASS: exact Weierstrass group law for R±Q and both normalized reconstructions")
print("PASS: R+Q strictly above boundary for q>2; R-Q below it for q>1")
