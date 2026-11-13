#!/usr/bin/env python3
"""Independent SymPy identity certificate for the v31 genus-two local proof."""
import json
from pathlib import Path
import sympy as sp

a,b,r,u,T=sp.symbols('a b r u T')
F=4*a**6+(24*b**2-12*r)*a**4+(36*b**4+60*b**2*r+12*r**2)*a**2-3*b**2*r**2-4*r**3
H=b*(6*a*a+2*b*b+3*r)
Z=a*a-b*b-r
assert sp.expand(F-H**2-4*Z**3)==0
f=sp.expand(F.subs({a:u,b:1,r:T}))
assert sp.expand(f- (6*u*u+2+3*T)**2 -4*(u*u-1-T)**3)==0
p5=sp.Poly(f.subs(T,3)+u*u*(u*u+1)**2,u,modulus=5)
assert p5.is_zero
coeff2=sp.Poly(f,u).coeff_monomial(u**2)
assert int(coeff2.subs(T,3))%5==4
assert sp.factor(sp.Poly(f,u).coeff_monomial(u**0))==-T**2*(4*T+3)
print('PASS: F = H^2 + 4Z^3; f(mod 5,T=3) = -u^2(u^2+1)^2')
print('PASS: u^2 coefficient == 4 (mod 5), constant == -T^2(4T+3)')
