#!/usr/bin/env python3
"""Exact v32 audit of every positive T=3 (mod 5) collision fibre.

The genus-2 square condition is necessary, not sufficient for the binomial equation.
Independent valuation classifications are compared with the original sextic.
"""
from fractions import Fraction
import json

B_VALUES = (1, 2, 3, 486)
T_VALUES = (3, 8, 23, 13, 38, 63, 88, 113, 1388, 18, 43, 68, 93, 118, 143,
            32773, 32788, 32838, 33013, 32793, 32818, 33343, 32968)


def F(a, b, rho):
    return (4*a**6 + (24*b*b - 12*rho)*a**4
            + (36*b**4 + 60*b*b*rho + 12*rho**2)*a*a
            - 3*b*b*rho*rho - 4*rho**3)


def valuation5(n):
    if n == 0:
        return None
    n = abs(n)
    r = 0
    while n % 5 == 0:
        r += 1
        n //= 5
    return r


def v(n):
    r = valuation5(n)
    return float('inf') if r is None else r


def square5(n):
    if not n:
        return True  # including zero; root loci are classified separately
    t = valuation5(n)
    return t % 2 == 0 and n // (5**t) % 5 in (1, 4)


def chi5(n):
    return 1 if n % 5 in (1, 4) else -1 if n % 5 in (2, 3) else 0


def predict(a, b, T):
    """Valuation analysis plus normalized local polynomial on critical boundaries."""
    assert b % 5 != 0 and T > 0 and T % 5 == 3
    rho = b*b*T
    u0 = a * pow(b, -1, 5) % 5
    k, d = valuation5(4*T+3), valuation5(9*T+8)
    assert (k == 1 and d >= 1) or (d == 1 and k >= 2)
    H = 6*a*a+2*b*b+3*rho
    Z = a*a-b*b-rho
    if u0 in (1, 4):
        return True
    if k == 1:
        if u0 == 0:
            return False
        if d % 2:
            return H % (5**((3*d+1)//2)) != 0
        h = 3*d//2
        t = v(H)
        q = -((9*T+8)//(5**d)) % 5
        if t < h:
            return True
        if t > h:
            return chi5(q) == 1
        assert H % (5**h) == 0 and Z % (5**d) == 0
        # Independent cusp-coordinate formula, not the original sextic.
        G = (b*(H//(5**h)))**2 + 4*(Z//(5**d))**3
        return square5(G)
    # d=1, k>=2
    if u0 in (2, 3):
        return H % 25 != 0
    s = v(a)
    if k % 2:
        return 2*s < k
    e = k//2
    q = (4*T+3)//(5**k)
    if s < e:
        return True
    if s > e:
        return chi5(q) == 1
    A = a//(5**e)
    # Independently expanded, normalized polynomial for u=5^e*w.
    G = (4*5**(4*e)*A**6 + (24-12*T)*b*b*5**(2*e)*A**4
         + 12*(T*T+5*T+3)*b**4*A*A - b**6*T*T*q)
    return square5(G)


def predicted_measure(T):
    k, d = valuation5(4*T+3), valuation5(9*T+8)
    if k == 1:
        if d % 2:
            return Fraction(4, 5)-Fraction(2, 5**((3*d+1)//2))
        e = d//2
        q = -((9*T+8)//(5**d)) % 5
        correction = Fraction(23, 15) if chi5(q) == 1 else Fraction(6, 5)
        return Fraction(4, 5)-correction/(5**(3*e))
    if k % 2:
        return Fraction(23,25)-Fraction(1,5**((k+1)//2))
    e = k//2
    q = ((4*T+3)//(5**k)) % 5
    correction = Fraction(23, 6) if chi5(q) == 1 else Fraction(3)
    return Fraction(23,25)-correction/(5**(e+1))


def expected_root_count(T):
    k, d = valuation5(4*T+3), valuation5(9*T+8)
    if k == 1:
        return 4 if d % 2 == 0 and chi5(-((9*T+8)//5**d)) == 1 else 0
    return 2 if k % 2 == 0 and chi5((4*T+3)//5**k) == 1 else 0


def simple_root_lift(poly, roots, depth):
    """Lift every simple root by one 5-adic digit; assert uniqueness at each stage."""
    for level in range(1, depth):
        step = 5**level
        raised = []
        for r in roots:
            options = [r+step*t for t in range(5)
                       if poly(r+step*t) % (5*step) == 0]
            assert len(options) == 1, (level,r,options)
            raised.extend(options)
        roots = raised
    return roots


def explicit_roots(T):
    k, d = valuation5(4*T+3), valuation5(9*T+8)
    if k == 1:
        if d % 2 or chi5(-((9*T+8)//(5**d))) != 1:
            return []
        h = 3*d//2
        H = lambda u: 6*u*u+2+3*T
        bases = simple_root_lift(H, [2,3], h)
        roots = []
        for base in bases:
            mod = 5**h

            def reduced(j):
                a=base+mod*j
                numerator=F(a,1,T)
                assert numerator % 5**(3*d) == 0
                return numerator//5**(3*d)

            seeds=[j for j in range(5) if reduced(j) % 5 == 0]
            assert len(seeds)==2, (T,base,seeds)
            lifts=simple_root_lift(reduced,seeds,4)
            for j in lifts:
                assert reduced(j) % 5**4 == 0
                roots.append(base+mod*j)
        assert len(roots)==4
        return roots
    if k % 2 or chi5((4*T+3)//5**k) != 1:
        return []
    e=k//2

    def reduced(w):
        a=5**e*w
        numerator=F(a,1,T)
        assert numerator % 5**k == 0
        return numerator//5**k

    seeds=[w for w in range(5) if reduced(w) % 5 == 0]
    assert len(seeds)==2
    lifts=simple_root_lift(reduced,seeds,4)
    assert len(lifts)==2 and all(reduced(w)%5**4==0 for w in lifts)
    return [5**e*w for w in lifts]


def main():
    results=[]
    for T in T_VALUES:
        N=5**5
        roots=explicit_roots(T)
        expected=expected_root_count(T)
        assert len(roots)==expected,(T,len(roots),expected)
        for b in B_VALUES:
            rho=b*b*T
            passed=0
            for a in range(N):
                oracle=square5(F(a,b,rho))
                prediction=predict(a,b,T)
                assert oracle==prediction,(T,b,a,oracle,prediction)
                passed+=oracle
            measured=Fraction(passed,N)
            density=predicted_measure(T)
            assert abs(float(measured-density))<0.006,(T,b,measured,density)
            if b==1:
                results.append({
                    "T":T,"k":valuation5(4*T+3),"d":valuation5(9*T+8),
                    "square_density_exact":str(density),
                    "empirical_3125":str(measured),
                    "root_count_over_Z5":expected,
                    "root_lifts_example":roots[:4],
                })
    # A fully finite residue sieve for an actual residual parameter >=32770.
    excluded = [a for a in range(25) if not predict(a,1,32793)]
    assert excluded == [0,7,10,15,18], excluded
    assert all(square5(F(a,1,32793)) == (a not in excluded)
               for a in range(25))
    for b in B_VALUES:
        for T in T_VALUES:
            for a in (0,1,2,5,18,125):
                rho=b*b*T
                Z=a*a-b*b-rho
                H=b*(6*a*a+2*b*b+3*rho)
                assert F(a,b,rho)==H*H+4*Z**3
    print(json.dumps({"status":"PASS", "cases":len(T_VALUES)*len(B_VALUES)*5**5,
        "sources":"v31 sextic; independently reduced v32 5-adic branches",
        "data":results,"original_equation_solved":False},indent=2))


if __name__ == "__main__":
    main()
