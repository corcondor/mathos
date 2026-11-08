#!/usr/bin/env python3
"""v90: cubic-residue local obstruction p|rho, p=1 mod 3.

For c*d=t**3, M=b*(8*b*b+9*rho), and p>=5 dividing rho,
reduce d*v³-c*u³-6*b*t*u*v*w-M*w³ to the cubic norm
Norm_Fp³/Fp(beta*v-alpha*u-2*b*w), where alpha³=c and beta=t/alpha.
If c is noncube in Fp and p=1 mod3, Fp³=Fp(alpha) has basis
(1,alpha,alpha²). Norm zero forces u=v=w=0, impossible for a projective
Fp point, hence also for a Qp point. This is a uniform statement for
ANY residual rho satisfying these conditions, not a height-cutoff search.

Fixed rho=100003, combine the prior F7 and F100291 obstruction tests
to reduce the original-integer-solution cube-core types from 21 to 9.
"""
from itertools import product
from math import gcd,isqrt

RHO=P=100003
assert P%3==1 and all(P%q for q in range(2,isqrt(P)+1))
FACTORS={9:(3,5,4003),18:(2,3,100291)}
assert all(b*(8*b*b+9*RHO)==v for b,v in ((9,8106075),(18,16247142)))

def types(b):
    m=b*(8*b*b+9*RHO)
    for v in product(range(3),repeat=3):
        es=dict(zip(FACTORS[b],v))
        if es.get(3,0)==0 or (b%2==0 and es.get(2,0)==0):continue
        c=d=t=1
        for p,e in es.items():
            if e==1:c*=p;d*=p*p;t*=p
            elif e==2:c*=p*p;d*=p;t*=p
        assert c*d==t**3
        yield c,d,t,es

def f7_possible(b,c,d,t):
    p=7
    sq={a*a%p for a in range(p)}
    m=b*(8*b*b+9*RHO)
    return any((d*v**3-c*u**3-6*b*t*u*v-m)%p==0 and
       (t*u*v+b*b+RHO)%p in sq
       for u in range(p) for v in range(p))

def fp100291_root(b,c,d,t):
    p=100291
    return any((d*pow(z,3,p)-6*b*t*z-c)%p==0 for z in range(p))

# Independent tiny-field sanity checks of the norm obstruction.
for p,c in ((7,2),(13,2),(19,2)):
    assert p%3==1 and pow(c,(p-1)//3,p)!=1
    d=pow(c,-1,p)
    for u,v,w in product(range(p),repeat=3):
        if u==v==w==0:continue
        assert (d*v**3-c*u**3-6*u*v*w-8*w**3)%p !=0
print("PASS: no projective F7,F13,F19 solutions in noncube case")

omega=pow(2,(P-1)//3,P)
assert omega==7120 and omega**3%P==1 and omega!=1
assert omega*omega%P==92882
for q in (2,3,5,100291):assert pow(q,(P-1)//3,P)==omega
assert pow(4003,(P-1)//3,P)==1
print("PASS: all five generator cubic characters modulo 100003")

results={}
for b in (9,18):
    m=b*(8*b*b+9*RHO)
    old=[]
    for c,d,t,es in types(b):
        if b==9 and not f7_possible(b,c,d,t):continue
        if b==18 and es[100291]==0 and not fp100291_root(b,c,d,t):continue
        old.append((c,d,t,es))
    assert len(old)==(12 if b==9 else 9)
    new=[];excluded=[]
    for c,d,t,es in old:
        assert P%gcd(c*d*t*b,P)!=0
        chi=pow(c,(P-1)//3,P)
        assert chi in {1,omega,omega*omega%P}
        entry={"exponents":es,"c":c,"d":d,"t":t,"cubic_character":chi}
        (new if chi==1 else excluded).append(entry)
    assert len(new)==(6 if b==9 else 3)
    results[b]={"surviving":new,"excluded":excluded}
    print("FIBRE",b,"original",len(old),"excluded",len(excluded),
          "remaining",len(new))
    print("REMAINING_EXPONENTS",b,[e["exponents"] for e in new])
assert sum(len(x["surviving"]) for x in results.values())==9
print("PASS: fixed-rho cube-core coefficient classes 21 -> 9")
print("SCOPE: nine coefficient types still need complete integer-point proof")
