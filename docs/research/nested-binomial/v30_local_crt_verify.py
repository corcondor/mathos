#!/usr/bin/env python3
"""Verify v30 local congruences inherited from v28/v29, not the original equation.
Python 3.10+ standard library only; exact modular and rational arithmetic.
"""
from fractions import Fraction
from math import gcd

RHO_MOD9 = {1, 4, 6, 7}
GENERIC_T = {8: {8, 12}, 23: {2, 18}}
DEEP_T = {13, 18}

def z_mod_p(m, p):
    r = m % 5
    if r not in (2, 3):
        return None
    k = (m-r) // 5
    q = pow(-4, k, p)
    return (1+4*q) % p if r == 2 else (1-pow(q, -1, p)) % p

def seven_ok(m):
    z = z_mod_p(m, 7)
    return z is not None and z != 0 and pow((-3*pow(z,-1,7)) % 7, 3, 7) == 1

assert [m for m in range(30) if seven_ok(m)] == [12,13,17,18]
for t, expected in {8:[12,48],23:[18,42]}.items():
    got=[m for m in range(60) if m%20 in GENERIC_T[t] and seven_ok(m)]
    assert got == expected, (t,got)

def survives(t,m,rho):
    if t in GENERIC_T:
        keep = m%20 in GENERIC_T[t]
    elif t in DEEP_T:
        keep = m%5 in (2,3)
    else:
        return False
    return keep and (rho%7 != 0 or seven_ok(m))

# One complete CRT period, no guessed cutoff.
rho_period = 9*25*7*13
m_period = 60
for b in (1,2,3,486):
    assert gcd(b,5)==1
    inverse = pow(b*b,-1,25)
    survivors=0
    for rho in range(rho_period):
        if rho%9 not in RHO_MOD9 or rho%13==0:
            continue
        t=(rho*inverse)%25
        survivors+=sum(survives(t,m,rho) for m in range(m_period))
    assert survivors==18240, (b,survivors)

expected=(Fraction(4,9)*Fraction(12,13)*
          (Fraction(6,7)*Fraction(1,25)+Fraction(1,7)*Fraction(1,75)))
observed=Fraction(18240,rho_period*m_period)
assert observed==expected==Fraction(304,20475)

# Independent numerical check of the v28 local coordinate formula by
# rational elliptic-curve addition at four T values divisible by seven.
def point_add(P,Q,T):
    A=-T*T*(4*T+3)
    B=12*(T*T+5*T+3)
    C=12*(2-T)
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u and y==-v: return None
    slope=((3*x*x+2*B*x+A*C)/(2*y) if x==u else (v-y)/(u-x))
    X=slope*slope-B-x-u
    Y=slope*(x-X)-y
    assert Y*Y==X**3+B*X**2+A*C*X+4*A*A
    return X,Y

def unit_mod(z,p):
    assert z.denominator%p != 0
    return (z.numerator%p)*pow(z.denominator%p,-1,p)%p

for val in (7,14,21,28):
    T=Fraction(val)
    R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
    P=None
    for m in range(1,19):
        P=point_add(P,R,T)
        if m%5 in (2,3) and P is not None and P[0]!=0:
            z=P[0]/T**2
            if z.denominator%7:
                assert unit_mod(z,7)==z_mod_p(m,7),(val,m)

print("PASS: p=7 m mod30 = 12,13,17,18")
print("PASS: CRT m mod60 = {8:[12,48], 23:[18,42]}")
print("PASS: 18240 / 1228500 = 304/20475 = %.9f%%" % (100*float(observed)))
print("PASS: rational point-law checks T=7,14,21,28, m<=18")
