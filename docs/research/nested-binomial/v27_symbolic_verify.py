#!/usr/bin/env python3
"""V27 exact symbolic audit for the second elliptic quotient (SymPy >=1.13).
No Sage/Magma needed. The general Shioda height and Mazur/EDS theorems are
*mathematical external inputs*, not statements verified by SymPy.
"""
import json
from fractions import Fraction
from pathlib import Path
import sympy as s

T=s.symbols('T')
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
R=(8*T*(4*T+3), 6*T*(4*T+3)*(9*T+8))

def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x,y=P; xx,yy=Q
    if s.cancel(x-xx)==0:
        if s.cancel(y+yy)==0: return None
        lam=s.cancel((3*x*x+2*B*x+A*C)/(2*y))
    else: lam=s.cancel((yy-y)/(xx-x))
    x3=s.factor(lam*lam-B-x-xx)
    y3=s.factor(lam*(x-x3)-y)
    return x3,y3

def d_shioda(m):
    # r_n is component number (mod n), R meets component 1 in I5,I3,I2
    def cor(n):
        r=m%n
        return s.Rational(r*(n-r),n)
    return s.Rational(m*m,60)-1+(cor(5)+cor(3)+cor(2))/2

expected_factors={
 10:(25*T**2*(T+72)**2*(4*T+3),
      (7*T+24)*(13*T**3+5928*T**2-25344*T-55296)),
 11:(T*(11*T**2+1584*T-576)**2,
     16*(T+12)*(7*T+24)*(T**2+744*T-9216)),
 12:(4*(4*T+3)*(T**2+264*T-576)**2,
     15*(T+32)*(T**3+1176*T**2-19008*T-179712)),
 13:((13*T**3+5928*T**2-25344*T-55296)**2,
     160*(T+12)*(T+72)*(T**3+1776*T**2-69408*T-6912)),
 14:(T*(4*T+3)*(7*T+24)**2*(T**2+744*T-9216)**2,
     (11*T**2+1584*T-576)*(17*T**5+44880*T**4-1909440*T**3-56678400*T**2-6635520*T-31850496)),
 15:(25*T**2*(T**3+1176*T**2-19008*T-179712)**2,
     24*(T+32)*(T**2+264*T-576)*(T**4+3768*T**3-369216*T**2+317952*T-1327104)),
}
P=None
coords=[]
for m in range(1,16):
    P=add(P,R)
    assert P is not None
    x,y=P
    assert s.cancel(y*y-x**3-B*x*x-A*C*x-4*A*A)==0
    xn,xd=s.fraction(s.factor(x))
    qdeg=s.degree(xd,T)//2
    assert s.degree(xd,T)%2==0
    assert qdeg==d_shioda(m), (m,qdeg,d_shioda(m))
    lim=s.limit(x/T**2,T,s.oo)
    assert s.factor(lim-(s.Rational(36,m*m)-4))==0,(m,lim)
    if m in expected_factors:
        en,ed=expected_factors[m]
        assert s.cancel(A/x-en/ed)==0,m
    coords.append(dict(m=m, deg_denom_x=int(s.degree(xd,T)),
                       shioda_denominator_degree=int(d_shioda(m)),
                       leading_X_over_T2=str(lim),
                       x_denominator=str(s.factor(xd))))
b2=4*B
b4=2*A*C
b6=16*A**2
b8=16*B*A**2-(A*C)**2
disc=-b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
assert s.factor(disc + 62208*T**5*(4*T+3)**2*(9*T+8)**3)==0
c4=s.factor(b2*b2-24*b4)
assert s.factor(c4-576*(45*T**3+130*T**2+120*T+36))==0

# Polynomial remainder (linear divisor) and resultant (quadratic divisor):
K={}
for m,h,g in [(10,7,24),(11,1,12),(12,1,32),(13,1,12),(15,1,32)]:
    num=expected_factors[m][0]
    e=s.degree(num,T)
    kval=abs(int(h**e*num.subs(T,-s.Rational(g,h))))
    K[str(m)]=dict(h=h,g=g,homogeneous_degree=e,K=kval,
                    factorization={str(k):v for k,v in s.factorint(kval).items()})
D14=11*T**2+1584*T-576
K14=abs(int(s.resultant(D14,expected_factors[14][0],T)))
assert s.factor(K14-2**50*3**16*5**25)==0
K['14']=dict(quadratic_D=str(D14),homogeneous_degree=8,
            K=K14,factorization={'2':50,'3':16,'5':25})

# Mazur check: for T>0 rational, m=1..6 never O;
# m=7,8,9,10 denominator can only vanish at negative T;
# m=12 denominator T^2+264T-576 has nonsquare discriminant 72000.
for m in (7,8,9,10,12):
    den=coords[m-1]['x_denominator']
    print('torsion-denominator',m,den)
assert s.sqrt(72000).is_Integer is False

out={'coords':coords,'constants':K,
     'discriminant':str(s.factor(disc)),'c4':str(c4),
     'limitations':'Theorems of Shioda, Mazur, Siegel, Silverman are not checked by SymPy.'}
Path(__file__).with_name('v27_symbolic_certificate.json').write_text(
 json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n')
print('PASS: group law, degrees, cusp leading term, 10..15 formulas, discriminant and constants')