#!/usr/bin/env python3
"""v92. Sharpness of v90's cubic-norm obstruction at p|rho.

Let p>=5 divide rho and p not divide bcdt, with c*d=t^3 and
M=b(8b^2+9rho). If c is a cubic residue mod p, choose alpha^3=c,
beta=t/alpha, u=2b/alpha, v=4b/beta, a=-3b modulo p.
Then F=d*v^3-c*u^3-6b*t*u*v-M=0,
a^2=t*u*v+b^2+rho, and the numerator
(a+b)^3-a*rho+c*u^3=0. The Jacobian determinant in (v,a)
is (36*beta*b^2)*(2*a) != 0; Hensel gives a Qp solution.
For v_p(rho)=1, the original recovered t and n are p-adic integers.
For p=1 (mod3) and c noncube, v90 proves no Qp cubic-cover point.
Hence the local criterion is sharp. No global rational/integer solution
is asserted by this construction.
"""
from itertools import product
from math import gcd,isqrt

RHO=P=100003
assert P%3==1 and all(P%q for q in range(2,isqrt(P)+1))
PRIMES={9:(3,5,4003),18:(2,3,100291)}

def cases(b):
    m=b*(8*b*b+9*RHO)
    for exs in product(range(3),repeat=3):
        e=dict(zip(PRIMES[b],exs))
        if e[3]==0 or (b==18 and e[2]==0):continue
        c=d=t=1
        for p,alpha in e.items():
            if alpha==1:c*=p;d*=p*p;t*=p
            elif alpha==2:c*=p*p;d*=p;t*=p
        assert c*d==t**3
        if b==9:
            squares={x*x%7 for x in range(7)}
            if not any((d*v**3-c*u**3-6*b*t*u*v-m)%7==0 and
                       (t*u*v+b*b+RHO)%7 in squares
                       for u,v in product(range(7),repeat=2)):
                continue
        if pow(c,(P-1)//3,P)!=1:continue
        yield e,c,d,t

# Construct all cubic roots once; finite integer arithmetic only.
roots={}
for x in range(1,P):roots.setdefault(pow(x,3,P),x)
assert len(roots)==(P-1)//3

total=0
for b in (9,18):
    m=b*(8*b*b+9*RHO)
    these=list(cases(b))
    assert len(these)==(6 if b==9 else 4)
    for e,c,d,t in these:
        alpha=roots[c%P]; beta=t*pow(alpha,-1,P)%P
        u=2*b*pow(alpha,-1,P)%P
        v=4*b*pow(beta,-1,P)%P
        a=(-3*b)%P
        assert pow(alpha,3,P)==c%P and pow(beta,3,P)==d%P
        assert alpha*beta%P==t%P
        assert (d*v**3-c*u**3-6*b*t*u*v-m)%P==0
        assert (a*a-t*u*v-b*b-RHO)%P==0
        assert ((a+b)**3-a*RHO+c*u**3)%P==0
        assert t*u*v%P==8*b*b%P
        assert c*u**3%P==8*b**3%P
        df_dv=(3*d*v*v-6*b*t*u)%P
        assert df_dv==36*beta*b*b%P and df_dv!=0
        assert 2*a%P!=0 and gcd(a,P)==1
        total+=1
        print("V92_CERTIFIED_SMOOTH_LOCAL",b,e,
              "alpha",alpha,"beta",beta,
              "u",u,"v",v,"a",a,"X",t*u*v%P,
              "Y",c*u**3%P,"dF_dv",df_dv)
assert total==10
print("PASS: all 10 corrected cubic-core classes have smooth local lifts at p=100003")
print("PASS: square recovery and original t numerator vanish mod p")
print("THEOREM: for p||rho, v90's cubic-residue test is NECESSARY AND SUFFICIENT for local cubic-cover + square + recovered t,n integrality at p")
print("LIMIT: no global original integer solution or full rational point classification")
