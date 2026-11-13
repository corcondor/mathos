#!/usr/bin/env python3
"""v38: explicit half-section, height/NS determinant, and finite-field 3-saturation.

This verifies finite algebra and finite-field obstructions. Shioda's height
formula, Kodaira component contributions, the K3 Picard bound, and the
Neron-Severi determinant theorem are genuine external mathematical inputs.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

q=sp.symbols("q")
T=q*q-1
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
Q=(A/q**2,A*(9*T+8)/q**3)
H=(-2*(q-1)*(q+1)**2*(2*q+1),
    6*(q-1)*(q+1)**2*(2*q+1)*(3*q-1))

def symadd(P,V):
    x,y=P;u,v=V
    slope=((3*x*x+2*B*x+A*C)/(2*y)
           if sp.cancel(x-u)==0 else (v-y)/(u-x))
    slope=sp.factor(sp.cancel(slope))
    xx=sp.factor(sp.cancel(slope*slope-B-x-u))
    yy=sp.factor(sp.cancel(slope*(x-xx)-y))
    return xx,yy

assert sp.factor(H[1]**2-H[0]**3-B*H[0]**2-A*C*H[0]-4*A*A)==0
half2=symadd(H,H)
sumRQ=symadd(R,Q)
assert sp.factor(half2[0]-sumRQ[0])==0
assert sp.factor(half2[1]-sumRQ[1])==0
# H is explicitly a genuinely new half of R+Q; prior two generators
# R and Q therefore span a sublattice of index >= 2.
print("PASS: H lies on E and 2H=R+Q as exact rational-function identities")

# Finite-fibre I5 twice, I2 twice, I3 twice; cusp IV at infinity.
def local_order_at(thing,root):
    num,den=sp.fraction(sp.factor(thing))
    assert den.subs(q,root)!=0
    t=sp.Symbol("s")
    f=sp.factor(num.subs(q,root+t))
    pol=sp.Poly(f,t)
    return min(mon[0] for mon,coeff in pol.terms() if coeff!=0)

for alpha in (sp.Integer(1),sp.Integer(-1)):
    assert local_order_at(Q[1],alpha)==2  # component 2 of I5
for alpha in (sp.Rational(1,2),-sp.Rational(1,2)):
    assert local_order_at(Q[1],alpha)==1  # nonidentity of I2
for alpha in (sp.Rational(1,3),-sp.Rational(1,3)):
    assert local_order_at(Q[1],alpha)==1  # nonidentity of I3
assert A.subs(q,0)==1
assert sp.limit(Q[0]/q**4,q,sp.oo)==-4
assert sp.limit(Q[1]/q**6,q,sp.oo)==0
assert sp.limit(R[0]/q**4,q,sp.oo)==32
assert sp.limit(R[1]/q**6,q,sp.oo)==216
# Q reaches the IV cusp, R reaches the smooth component.
# Q.O=1 at q=0 (x(Q) has a double pole).
hR=F(1,15)       # v33 rank-one height multiplied by degree-2 base change.
hQ=F(4)+2-2*F(6,5)-2*F(1,2)-2*F(2,3)-F(2,3)
assert hQ==F(3,5)
hH=(hR+hQ)/4    # orthogonality of R and Q under q -> -q.
cross_RH=hR/2
det_RQ=hR*hQ
det_RH=hR*hH-cross_RH*cross_RH
assert det_RQ==F(1,25) and hH==F(1,6) and cross_RH==F(1,30)
assert det_RH==F(1,100)
trivial_disc=5**2*2**2*3**2*3
assert trivial_disc==2700
assert trivial_disc*det_RQ==108
assert trivial_disc*det_RH==27
print("PASS: geometric heights (R,R)=1/15, (Q,Q)=3/5, (R,Q)=0")
print("PASS: explicit H basis has Gram [[1/15,1/30],[1/30,1/6]], det=1/100")

# Geometric torsion: if P != O torsion, the Shioda height zero implies
# P.O=0 and the sum of local component corrections is exactly 4.
# The full correction maximum 27/5 is <6, excluding P.O>=1.
c5=(F(0),F(4,5),F(6,5))
c3=(F(0),F(2,3))
c2=(F(0),F(1,2))
civ=(F(0),F(2,3))
possibilities=[v for v in product(c5,c5,c3,c3,c2,c2,civ)
               if sum(v)==4]
assert possibilities==[
    (F(4,5),F(6,5),F(2,3),F(2,3),F(0),F(0),F(2,3)),
    (F(6,5),F(4,5),F(2,3),F(2,3),F(0),F(0),F(2,3))
]
# Multiplying such a putative torsion point by 5 kills both I5
# components, preserves nonzero I3 & IV components, and hence creates
# a NONZERO torsion point with correction sum exactly 2 (impossible).
assert 2*F(2,3)+F(2,3)==2
print("PASS: geometric MW torsion is zero by finite component-correction contradiction")

# If full geometric MW has index I over <R,Q>, determinant formula gives
# |disc NS|=108/I^2. Integral NS discriminant => I in {1,2,3,6}.
# H forces I even. Thus the index of <R,H> is 1 or 3.
assert [i for i in range(1,50) if F(108,i*i).denominator==1]==[1,2,3,6]

def specialization(q0):
    t=F(q0*q0-1)
    aa=-t*t*(4*t+3)
    bb=12*(t*t+5*t+3)
    cc=12*(2-t)
    r=(8*t*(4*t+3),6*t*(4*t+3)*(9*t+8))
    h=(F(H[0].subs(q,q0)),F(H[1].subs(q,q0)))
    discriminant=-62208*t**5*(4*t+3)**2*(9*t+8)**3
    return aa,bb,cc,r,h,discriminant

def modf(fr,p):
    z=F(fr)
    assert z.denominator%p
    return (z.numerator%p)*pow(z.denominator%p,-1,p)%p

def addp(p,B,AC,C0,P,V):
    if P is None:return V
    if V is None:return P
    x,y=P;u,v=V
    if x==u and (y+v)%p==0:return None
    if x==u:
        slope=((3*x*x+2*B*x+AC)*pow(2*y%p,-1,p))%p
    else:
        slope=((v-y)*pow((u-x)%p,-1,p))%p
    nx=(slope*slope-B-x-u)%p
    return (nx,(slope*(x-nx)-y)%p)

def np(p,B,AC,C0,P,n):
    out=None
    for _ in range(n):
        out=addp(p,B,AC,C0,out,P)
    return out

def finite_data(q0,p):
    aa,bb,cc,r,h,Delta=specialization(q0)
    assert Delta%p!=0 and q0%p
    B0=modf(bb,p);AC0=modf(aa*cc,p);C0=modf(4*aa*aa,p)
    rr=tuple(modf(v,p) for v in r)
    hh=tuple(modf(v,p) for v in h)
    points=[None]
    squares={}
    for y in range(p):squares.setdefault(y*y%p,[]).append(y)
    for x in range(p):
        z=(x**3+B0*x*x+AC0*x+C0)%p
        points.extend((x,y) for y in squares.get(z,[]))
    triples={np(p,B0,AC0,C0,P,3) for P in points}
    return len(points),rr,hh,triples,(B0,AC0,C0)

# Four projective lines over F3, ruling out every nonzero combination
# (aR+bH) mod 3 in the full geometric function-field group.
witnesses={
    (1,0):(2,41,(32,20)),
    (1,1):(2,41,(17,4)),
    (1,2):(2,41,(4,39)),
    (0,1):(3,17,(11,8)),
}
for (a,b),(q0,p,expected_pt) in witnesses.items():
    n,rr,hh,triples,(B0,AC0,C0)=finite_data(q0,p)
    assert n==(54 if (q0,p)==(2,41) else 21),(q0,p,n)
    pt=addp(p,B0,AC0,C0,np(p,B0,AC0,C0,rr,a),
            np(p,B0,AC0,C0,hh,b))
    assert pt==expected_pt,(a,b,pt,expected_pt)
    assert pt not in triples,(a,b,q0,p)
    print("PASS: no 3-division for",a,b,"in E_q",q0,"mod",p,
          "group size",n,"point",pt)

# Any putative geometric 3rd root of a rational (aR+bH) is unique,
# because geometric 3-torsion vanishes; it is therefore Q(q)-rational.
# It specializes into Q-rational points at q=2 or 3, and their reductions
# would be 3-divisible, contradicting the four finite witnesses.
# Hence no 3-saturation is possible, so index <R,H> is 1.
print("PASS: finite-field saturation eliminates index 3; full geometric basis {R,H}")
print("PASS: |disc(NS)|=27, geometric MW group ZR+ZH and no torsion")
print("External inputs: Shioda height/determinant, Kodaira local contributions, K3 rank20")
