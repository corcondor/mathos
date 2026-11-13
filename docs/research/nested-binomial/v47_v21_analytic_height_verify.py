#!/usr/bin/env python3
"""v47: independent exact audit of the algebra behind v21's analytic height bound.

Mathematical input (NOT re-proved here): original-solution branch has n>=104,
t>3sqrt(n), 0<t<n/3, rho>=13 and for n>=1024,
t>2n/(5 log n). This checks every stated polynomial identity and
numeric rational inequality in the consequent a^2<152*rho*log(rho).
"""
import sympy as s

n,t=s.symbols("n t", integer=True, positive=True)
q=t*t+3*t+3
H=9*n*q+t**3
D=81*n*(n-1)
P=s.expand(H**2+H*D*(9*n-t-6)-q*D**2)
expected=(t**6+n*(18*t**5+135*t**4+540*t**3)
          +n**2*(1215*t*t-2916*t-5832)
          +n**3*(4374*t+6561))
assert s.expand(P-expected)==0
assert 31**2-30*31-30>0  # q <= (11/10)t^2 when t>=31
assert 1215*31**2-2916*31-5832>0
assert s.Rational(99,10)+s.Rational(1,3)<11
assert 64*2**42>2278125*35**5
assert s.Rational(5445,36)<152
assert s.Rational(121*32,54)<72
print("PASS: P polynomial identity and positive-term lower bound")
print("PASS: q, H and n=2^25 endpoint rational inequalities")
print("PASS: final height constant 5445/36 < 152")
print("SCOPE: v20 gap inequality and v18 input assumptions remain external.")
