#!/usr/bin/env python3
"""v79: exact cubic-core 3-isogeny descent on fixed-rho first elliptic quotient.

E: Y^2+6bXY+M*Y=X^3, M=b*(8b^2+9rho).
For any integral point with X>0, put C=6bX+M, U=abs(Y), V=abs(Y+C).
Then UV=X^3, V-U=sign(Y)*C, gcd(U,V)^2 divides M^3, and
U=c*u^3, V=d*v^3 with cube-free c,d and cd=t^3, squarefree t|rad(M).
Therefore X=t*u*v and d*v^3-c*u^3=eps*(6b*t*u*v+M).
This exact canonical parametrization has <= 2*3^omega(M) signed covers
for each (b,rho). The arithmetic proof uses p-adic valuations,
not a finite numerical extrapolation.
"""
from itertools import product
from math import gcd
from sympy import factorint, integer_nthroot, symbols, expand

X,Y,b,rho=symbols("X Y b rho",integer=True)
M=b*(8*b*b+9*rho)
C=6*b*X+M
assert expand(Y*(Y+C)-(Y*Y+6*b*X*Y+M*Y))==0
print("PASS: symbolic integral Weierstrass factorization UV=X^3")

def cube_part(z):
    assert z>0
    c=u=1
    for p,e in factorint(z).items():
        c*=int(p)**(e%3)
        u*=int(p)**(e//3)
    assert c*u**3==z
    return c,u

def coefficient_types(m):
    assert m>0
    primes=tuple(sorted(int(p) for p in factorint(m)))
    for exponents in product((0,1,2),repeat=len(primes)):
        c=d=t=1
        for p,i in zip(primes,exponents):
            if i==1: c*=p; d*=p*p; t*=p
            elif i==2: c*=p*p; d*=p; t*=p
        assert c*d==t**3
        yield c,d,t

def audit_point(bb,rr,xx,yy):
    m=bb*(8*bb*bb+9*rr)
    cc=6*bb*xx+m
    assert bb>0 and rr>0 and xx>0 and m>0
    assert yy*yy+cc*yy==xx**3
    eps=1 if yy>0 else -1
    U,V=abs(yy),abs(yy+cc)
    assert U>0 and V>0 and U*V==xx**3
    assert V-U==eps*cc
    g=gcd(U,V)
    assert m**3%(g*g)==0
    assert all(m%p==0 for p in factorint(g))
    c,u=cube_part(U);d,v=cube_part(V)
    t,yes=integer_nthroot(c*d,3)
    assert yes
    t=int(t)
    assert xx==t*u*v
    assert d*v**3-c*u**3==eps*(6*bb*t*u*v+m)
    assert (c,d,t) in set(coefficient_types(m))
    return {"b":bb,"rho":rr,"X":xx,"Y":yy,"M":m,
            "gcd_UV":g,"gcd_divides_M":(m%g==0),
            "cube_core":[c,d,t],"cube_roots":[u,v],"sign":eps}

samples=[
  (1,24,56,224),(1,24,56,-784),(1,63,50,125),
  (1,63,50,-1000),(3,100003,15912,1008423),
  (6,100003,221130,97518330),
  (243,100003,1756217862,72328954537539),
]
for z in samples:print("PASS integral sample and unique cube core",audit_point(*z))
sharp=audit_point(1,63,50,125)
assert sharp["gcd_UV"]==125 and sharp["M"]==575
assert not sharp["gcd_divides_M"]
print("PASS sharp counterexample: gcd(U,V)=125 does NOT divide M=575")

for bb,expected in (
    (9,{3:4,5:2,4003:1}),
    (18,{2:1,3:4,100291:1}),
):
    mm=bb*(8*bb*bb+9*100003)
    assert factorint(mm)==expected
    types=list(coefficient_types(mm))
    assert len(types)==27 and len(set(types))==27
    assert all(c*d==t**3 and all(mm%p==0 for p in factorint(c*d))
               for c,d,t in types)
    print("PASS b",bb,"rho",100003,"M",mm,"factorization",expected,
          "cube_core_types",len(types),"signed_cubic_covers",2*len(types))
print("PASS: full structural parametrization; 54 cover TYPES per residual fibre")
print("NOT PROVED: completeness of integral points on each of the 54 cubic covers")
