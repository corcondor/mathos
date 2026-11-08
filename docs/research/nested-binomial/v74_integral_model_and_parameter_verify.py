#!/usr/bin/env python3
"""v74: exact integral elliptic model and birational (k,q) parametrization.

Original integer-solution necessary conditions:
b|486, a>0, rho>0, a²>b²+rho,
gcd(a,b)=1, gcd(a,rho)=gcd(a,3).

A sextic integer point (a,S) gives an INTEGRAL point
X=a²-b²-rho, M=b(8b²+9rho), Y=(S-6bX-M)/2
on Y²+6bXY+MY=X³; no general S-integral enumeration is necessary.

For the rational surface C_T (with x>0, T>0, u>0),
k=y/x and q=(u-1/3)/x give a rational inverse for Delta!=0.
The exceptional Delta=0 lines are excluded for ORIGINAL integer solutions.
"""
import sympy as s

a,b,rho,S,X,Y=s.symbols("a b rho S X Y",integer=True)
x0=a*a-b*b-rho
M=b*(8*b*b+9*rho)
H=6*b*x0+M
F=(4*a**6+(24*b*b-12*rho)*a**4+
   (36*b**4+60*b*b*rho+12*rho*rho)*a*a-
   3*b*b*rho*rho-4*rho**3)
assert s.expand(F-(H**2+4*x0**3))==0
assert s.expand((2*Y+6*b*X+M)**2-4*(Y*Y+6*b*X*Y+M*Y-X**3)-H.subs(x0,X)**2-4*X**3)==0
# The congruence S²=H² (mod 4) implies parity S=H (mod 2)
# because squares modulo 4 are 0 and 1.
assert {z*z%4 for z in (0,2)}=={0}
assert {z*z%4 for z in (1,3)}=={1}
print("PASS: exact sextic F=H²+4X³ and integral generalized Weierstrass model")

k,q=s.symbols("k q",nonzero=True)
Dlt=1-9*k*q*q
x=s.factor(k*(k+6*q-3)/Dlt)
u=s.Rational(1,3)+q*x
T=s.factor((x*x-k*(k+6)*x-8*k)/(9*k))
y=k*x
ss=x*(x+k*k)/k
assert s.cancel(u*u-x-1-T)==0
assert s.cancel(y*y+6*x*y+(8+9*T)*y-x**3)==0
assert s.cancel(ss*ss-(6*x+8+9*T)**2-4*x**3)==0
assert s.cancel(ss-(2*y+6*x+8+9*T))==0
P=6*k*q-k-1
Q=-3*k*k*q+18*k*q*q-9*k*q+3*k-1
B=3*k*q+k-2
E=3*k*k*q+36*k*q*q+3*k-8
assert s.cancel(T+E*Q/(9*Dlt**2))==0
for sign in (+1,-1):
    t=s.factor((2*u*(u*u+3)-T*(3+2*u)+sign*ss)/(2*T))
    n=s.factor((t*t+3*t+3+u*(t+6)-u*u+T)/(9*u))
    desired_t=3*(k-1)*P/Q if sign==1 else 3*(k-4)*B/E
    desired_n=-P**3/Q**2 if sign==1 else -(k-4)**3*Dlt/E**2
    assert s.cancel(t-desired_t)==0
    assert s.cancel(n-desired_n)==0
print("PASS: all user-supplied (k,q) maps and t,n formulas as exact rational identities")

# EXCEPTIONAL FIBRE: Delta=0 and numerator k(k+6q-3)=0.
# With k!=0, this forces k=3-6q, and
#   9(3-6q)q²-1=-(3q-1)²(6q+1).
assert s.factor(9*(3-6*q)*q*q-1)==-(3*q-1)**2*(6*q+1)
# q=-1/6,k=4: u=1/3-X/6. If X>0,u>0, then u<1/3,
# so T=u²-X-1<0, contradicting T>0.
# q=1/3,k=1: u=(1+X)/3 and X=3a/b-1.
# T=u²-X-1=a(a-3b)/b², giving rho=a(a-3b).
# gcd(a,rho)=a>3 for all rho>0 (a>3b), contradicting
# the original necessary gcd(a,rho)=gcd(a,3).
xx=s.symbols("xx")
ue=(xx+1)/3
Te=s.factor(ue*ue-xx-1)
assert s.factor(Te-(xx-8)*(xx+1)/9)==0
assert s.factor((a*a/b**2)-(3*a/b)-a*(a-3*b)/b**2)==0
te=s.factor((2*ue*(ue*ue+3)-Te*(3+2*ue)+xx*(xx+1))/(2*Te))
ne=s.factor((te*te+3*te+3+ue*(te+6)-ue*ue+Te)/(9*ue))
assert te==6*(xx+4)/(xx-8)
assert s.cancel(ne-(xx+4)**3/((xx-8)**2*(xx+1)))==0
print("PASS: Delta=0 exceptional curve classified; excluded by gcd(a,rho) for original solutions")
print("CONCLUSION: all original-solution rational lifts have x>0,k!=0,Delta!=0 and admit (k,q) parametrization")
print("LIMIT: no integral-point enumeration or original-equation proof implied by these identities")
