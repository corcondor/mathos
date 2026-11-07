#!/usr/bin/env python3
"""v25: independent symbolic/numerical checks for elliptic 3-torsion surface.

This checks algebraic identities and supplied auxiliary examples. The
Shioda--Tate generic rank 0 and Mordell--Weil torsion Z/3Z rely on the
known classification of the extremal rational elliptic surface
    y^2 + xy + t*y = x^3
and are NOT proved by this script.
"""
import json
from math import gcd, isqrt
from pathlib import Path
from fractions import Fraction
import sympy as sp

HERE=Path(__file__).resolve().parent
REFERENCE=HERE/'v24_certificate_reference.json'
a,b,r,z,S=sp.symbols('a b r z S', integer=True)
U=sp.symbols('U')
F=4*a**6+(24*b*b-12*r)*a**4+(36*b**4+60*b*b*r+12*r*r)*a*a-3*b*b*r*r-4*r**3
Z=a*a-b*b-r
H=b*(6*a*a+2*b*b+3*r)
C=b*(8*b*b+9*r)
A=48*b*b*(9*r-b*b)
B=16*b*b*(81*r*r-180*b*b*r-8*b**4)
Xp=12*b*b;Yp=4*C
# exact algebraic identities
assert sp.expand(F-H**2-4*Z**3)==0
assert sp.expand(Yp**2-Xp**3-A*Xp-B)==0
assert sp.factor((3*Xp**2+A)/(2*Yp))==6*b
assert sp.expand((6*b)**2-2*Xp-Xp)==0
assert sp.expand(4*(a*a+2*b*b-r)-Xp-4*Z)==0

# Generalized Weierstrass to standard extremal rational elliptic surface
xx,yy=sp.symbols('xx yy')
z_scaled=36*b*b*xx
v_scaled=-216*b**3*yy
lam=C/(216*b**3)
expr=v_scaled**2-6*b*z_scaled*v_scaled-C*v_scaled-z_scaled**3
assert sp.simplify(sp.expand(expr)/(216*b**3)**2 - (yy**2+xx*yy+lam*yy-xx**3))==0
# generalized Weierstrass coefficients a1=1,a3=lambda => delta=lambda^3(1-27lambda)
assert sp.simplify(lam**3*(1-27*lam)*(12*b)**12-(-16*(4*A**3+27*B**2)))==0
# The original short-Weierstrass x coordinate scales by (12*b)^2.

# Universal minimal model y^2+x*y+lambda*y=x^3: c4 and Delta.
ll=sp.symbols('ll')
assert sp.factor((ll**3*(1-27*ll)).subs(ll,lam)*(12*b)**12)==sp.factor(-16*(4*A**3+27*B**2))
# At lambda=0, vDelta=3 and c4(0)!=0 (I3), at 1/27 ord=1 (I1).
# At infinity mu=1/lambda, after scaling: y^2+mu*x*y+mu^2*y=x^3.
mu=sp.symbols('mu')
DeltaInf=sp.factor((mu**2)**3*((mu)**3-27*mu**2))
c4Inf=sp.factor(mu**4-24*mu*(mu**2))
assert DeltaInf==mu**8*(mu-27)
assert c4Inf==mu**3*(mu-24)
# Unconditional rational 3-torsion: normalized (0,0) is order 3.
# Check a good rational specialization lambda=2 for a torsion sanity check:
def count_points_standard(p,lam):
    return 1+sum((y*y+x*y+lam*y-x*x*x)%p==0 for x in range(p) for y in range(p))
assert count_points_standard(5,2)==3 and count_points_standard(7,2)==6

# Velu 3-isogenous quotient curve (short Weierstrass)
g=3*Xp**2+A
Aprime=sp.factor(A-10*g)
Bprime=sp.factor(B-7*(4*Yp**2+2*Xp*g))
assert Aprime==-3888*b*b*(b*b+r)
assert Bprime==-11664*b*b*(8*b**4+12*b*b*r+3*r*r)
DeltaPrime=sp.factor(-16*(4*Aprime**3+27*Bprime**2))
assert DeltaPrime==-58773123072*b**4*r**3*(8*b*b+9*r)
velu_x=sp.factor((sp.Symbol('X')+2*g/(sp.Symbol('X')-Xp)+4*Yp**2/(sp.Symbol('X')-Xp)**2))
# x'(X) = X + 2g/(X-Xp) + 4Yp^2/(X-Xp)^2

# genus two curve S^2=f(a^2), two genus-one degree-two quotients
f=4*U**3+(24*b*b-12*r)*U**2+(36*b**4+60*b*b*r+12*r*r)*U-3*b*b*r*r-4*r**3
DiscF=sp.factor(sp.discriminant(f,U))
assert DiscF==-3888*b**4*r*(8*b*b+9*r)**3
# f(0) not zero (r>0): six distinct roots of f(a^2) and genus 2.
w=sp.symbols('w')
g2=sp.expand(w**3*f.subs(U,1/w))
assert sp.expand(g2 - (4+(24*b*b-12*r)*w+(36*b**4+60*b*b*r+12*r*r)*w**2-r*r*(3*b*b+4*r)*w**3))==0
assert sp.factor(sp.discriminant(g2,w))==DiscF

# arithmetic from v19 cubic cover / isogeny Tate coordinate
points=json.loads(REFERENCE.read_text())['points']
assert len(points)==16

def prime_factors_positive(n):
    if n<=0: raise ValueError(n)
    primes=[]; d=2
    while d*d<=n:
        if n%d==0:
            primes.append(d)
            while n%d==0:n//=d
        d+=1 if d==2 else 2
    if n>1:primes.append(n)
    return primes

def elliptic_add(P,Q,A):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and y==-v:return None
    if x==u:
        if y==0:return None
        m=(3*x*x+A)/(2*y)
    else:m=(v-y)/(u-x)
    X=m*m-x-u;Y=m*(x-X)-y
    return (X,Y)

witnesses=[]
for d in points:
    aa=int(d['a']);bb=int(d['b']);rr=int(d['rho'])
    n=int(d['n']);tt=int(d['t'])
    N=9*aa*aa-bb*bb
    f_value=4*aa**6+(24*bb*bb-12*rr)*aa**4+(36*bb**4+60*bb*bb*rr+12*rr*rr)*aa*aa-3*bb*bb*rr*rr-4*rr**3
    SS=isqrt(f_value)
    assert SS*SS==f_value
    zz=aa*aa-bb*bb-rr; HH=bb*(6*aa*aa+2*bb*bb+3*rr)
    assert zz>0 and zz%bb==0 and SS%bb==0
    Z0=zz//bb; s0=SS//bb; h0=HH//bb
    assert (s0-h0)%2==0
    lower=(s0-h0)//2; upper=(s0+h0)//2
    assert lower>0 and upper>0 and upper*lower==bb*Z0**3
    assert upper-lower+3*bb*Z0==N
    xsmall=tt*tt-9*n
    ylarge=tt*tt+6*tt+9*n
    assert Fraction(bb*bb*xsmall**3,729*n*n*(n-1))==lower
    assert Fraction(bb*bb*ylarge**3,729*n*(n-1)**2)==upper
    # Stronger gcd support: for p>=5, every gcd prime divides both n(n-1) and N.
    gcdprimes=prime_factors_positive(gcd(lower,upper))
    assert set(gcdprimes)<=set(prime_factors_positive(abs(N)))
    assert all(n*(n-1)%p==0 for p in gcdprimes if p>=5)
    for p in prime_factors_positive(n*(n-1)):
        if p<5:continue
        e=0; nn=n*(n-1)
        while nn%p==0: e+=1;nn//=p
        if e%3:
            assert p in gcdprimes
            def valuation(v):
                q=0
                while v%p==0:q+=1;v//=p
                return q
            # For n, v_p(U)=e and v_p(V)=2e mod 3;
            # for n-1, v_p(U)=2e and v_p(V)=e mod 3.
            if n%p==0:
                assert valuation(lower)%3==e%3
                assert valuation(upper)%3==(2*e)%3
            else:
                assert valuation(lower)%3==(2*e)%3
                assert valuation(upper)%3==e%3
    for w0 in (lower,upper):
        n0=w0
        for p in prime_factors_positive(w0):
            e=0
            while n0%p==0:e+=1;n0//=p
            if p>=5 and p not in prime_factors_positive(abs(N)):
                assert e%3==0
    Ap=48*bb*bb*(9*rr-bb*bb);Bp=16*bb*bb*(81*rr*rr-180*bb*bb*rr-8*bb**4)
    P=(Fraction(12*bb*bb), Fraction(4*bb*(8*bb*bb+9*rr)))
    Q=(Fraction(4*(aa*aa+2*bb*bb-rr)), Fraction(4*SS))
    assert elliptic_add(P,P,Ap)==(P[0],-P[1])
    assert elliptic_add(P,elliptic_add(P,P,Ap),Ap) is None
    QplusP=elliptic_add(Q,P,Ap)
    QminusP=elliptic_add(Q,(P[0],-P[1]),Ap)
    assert QplusP is not None and QminusP is not None
    xvelu=Q[0]+QplusP[0]-P[0]+QminusP[0]-P[0]
    yvelu=Q[1]+QplusP[1]-P[1]+QminusP[1]+P[1]
    # In Velu y correction, Q= -P has y=-P[1], and -y_Q=+P[1].
    xformula=Q[0] + Fraction(2*(3*P[0]**2+Ap),(Q[0]-P[0])) + Fraction(4*P[1]**2,(Q[0]-P[0])**2)
    assert xvelu==xformula
    At=-3888*bb*bb*(bb*bb+rr)
    Bt=-11664*bb*bb*(8*bb**4+12*bb*bb*rr+3*rr*rr)
    assert yvelu*yvelu == xvelu**3+At*xvelu+Bt
    witnesses.append({'rho':rr,'a':aa,'b':bb,'n':n,'t':tt,'z':zz,'Z':Z0,
        'S':SS,'U':lower,'V':upper,'N':N,'p_gcd':prime_factors_positive(gcd(lower,upper)),
        'x_3isog_numerator':xvelu.numerator,'x_3isog_denominator':xvelu.denominator})
print('PASS symbolic: rational 3-torsion, Tate normal form, base reparametrization')
print('PASS symbolic: 3-isogenous curve and discriminant, 2 elliptic quotients of genus 2')
print('PASS arithmetic: v19 cubic cover, gcd prime support, all 16 auxiliary points')
print('PASS independent group-law and Velu isogeny checks on 16 points')
(HERE/'v25_certificate.json').write_text(json.dumps({
    'status':'PASS',
    'scope':'symbolic identities and 16 earlier auxiliary points; generic MW rank theorem cited, not algorithmically certified',
    'num_auxiliary_points':len(witnesses),
    'elliptic_surface':'y^2+xy+lambda*y=x^3',
    'lambda_of_rho':'(8*b^2+9*rho)/(216*b^2)',
    'fiber_types':{'lambda=0':'I_3','lambda=1/27':'I_1','lambda=infinity':'IV*'},
    'generic_rank':'0, by Shioda--Tate and rational elliptic surface classification',
    'point_order':'3, proved algebraically',
    'points':witnesses},indent=2,ensure_ascii=False)+'\n')
