#!/usr/bin/env python3
"""v83 AUDITED correction (2026-11-09).

The F7 cubic+square test for b=9 is valid and excludes 6 of 18
cube-core types. The earlier "F100291 rootlessness" exclusion for
b=18 was INVALID: substituting v=z*u leaves an essential factor u,
giving u*(d*z^3-c)-6*b*t*z=0, NOT d*z^3-6*b*t*z-c=0.
All four b18,p-core=0 types have explicit nonsingular F100291
points that also satisfy the a-square condition. Do not reject any
of those b18 coefficient types by the old test.
Correct v83 output: b9 12, b18 12, total 24. The independent
v90 cubic norm condition at p|rho later reduces 24 to 10.
"""
from itertools import product
from sympy import factorint

RHO=100003
def cores(b):
    M=b*(8*b*b+9*RHO)
    ps=sorted(int(p) for p in factorint(M))
    for ex in product((0,1,2),repeat=len(ps)):
        es=dict(zip(ps,ex))
        if es.get(3,0)==0 or (b%2==0 and es.get(2,0)==0):continue
        c=d=t=1
        for p,e in es.items():
            if e==1:c*=p;d*=p*p;t*=p
            if e==2:c*=p*p;d*=p;t*=p
        assert c*d==t**3
        yield c,d,t,es

def mod7_square_possible(b,c,d,t):
    p=7;M=b*(8*b*b+9*RHO)
    sq={x*x%p for x in range(p)}
    return any((d*v**3-c*u**3-6*b*t*u*v-M)%p==0 and
        (t*u*v+b*b+RHO)%p in sq
        for u in range(p) for v in range(p))

items9=list(cores(9))
items18=list(cores(18))
assert len(items9)==18 and len(items18)==12
remaining9=[e for c,d,t,e in items9 if mod7_square_possible(9,c,d,t)]
assert len(remaining9)==12
assert len(items9)-len(remaining9)==6

# Actual square-lift witnesses modulo p=100291, including ALL three
# types falsely excluded in the original v83 note.
p=100291
M=18*(8*18*18+9*RHO)
witnesses=[
 ((1,1,0),6,36,6,40138,40138,22353),
 ((1,2,0),18,12,6,18457,73828,6941),
 ((2,1,0),12,18,6,54714,9137,16071),
 ((2,2,0),36,6,6,60153,60153,22353),
]
for e2e3ep,c,d,t,u,v,a in witnesses:
    assert (c,d,t,dict(zip((2,3,100291),e2e3ep))) in items18
    assert u%p and v%p
    assert (d*v**3-c*u**3-6*18*t*u*v-M)%p==0
    assert (a*a-t*u*v-18**2-RHO)%p==0
    z=v*pow(u,-1,p)%p
    assert (u*(d*z**3-c)-6*18*t*z)%p==0
    assert (-6*18*t*u*v)%p!=0
    print("V83_INVALID_EXCLUSION_COUNTEREXAMPLE",e2e3ep,u,v,a)
print("PASS: F7 excludes 6 of 18 b9 types, 12 valid b9 types remain")
print("PASS: b18 has 12 types; F100291 provides NO exclusion of the four p-free types")
print("CORRECTED: 30 -> 24 (b9:12,b18:12); v90 later reduces to 10")
