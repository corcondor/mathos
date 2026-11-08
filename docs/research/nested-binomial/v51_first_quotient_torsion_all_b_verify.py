#!/usr/bin/env python3
"""Exact two-good-prime torsion certificate for rho=100003 and every b|486.

For E1: y²+6xy+(8+9rho/b²)y=x³, P=(0,0) has order 3.
At good primes p!=q, the l-primary torsion injects into E(F_p) if l!=p.
Our witnesses satisfy gcd(#E(F_p),#E(F_q))=3 and
p does not divide #E(F_q), q does not divide #E(F_p).
Hence rational torsion has order exactly 3. Rank remains separate.
"""
from math import gcd, isqrt

RHO=100003
WITNESSES={
    1:((7,6),(13,15)),
    2:((5,9),(7,6)),
    3:((5,9),(11,12)),
    6:((7,6),(11,15)),
    9:((7,6),(23,15)),
    18:((5,9),(13,12)),
    27:((5,9),(7,6)),
    54:((7,6),(31,27)),
    81:((7,9),(13,15)),
    162:((5,9),(7,6)),
    243:((5,9),(7,6)),
    486:((7,9),(11,6)),
}
assert sorted(WITNESSES)==[b for b in range(1,487) if 486%b==0]

def count(b,p):
    assert b%p and RHO%p and (8*b*b+9*RHO)%p
    a3=(8+9*RHO*pow(b*b,-1,p))%p
    result=1
    for x in range(p):
        disc=((6*x+a3)**2+4*x*x*x)%p
        result+=1 if disc==0 else 2 if pow(disc,(p-1)//2,p)==1 else 0
    return result

for b,((p,n),(q,m)) in WITNESSES.items():
    assert p!=q and p>=5 and q>=5
    assert (count(b,p),count(b,q))==(n,m)
    assert gcd(n,m)==3
    assert n%q and m%p
    assert isqrt(b*b+RHO)**2!=b*b+RHO
    print('CERTIFIED b=',b,'#E(F_%d)'%p,n,
          '#E(F_%d)'%q,m,'torsion=Z/3','1+T non-square')

print('PASS: every b|486 has first-quotient rational torsion exactly Z/3')
print('LIMIT: free Mordell-Weil rank requires Sage proof for each b')
