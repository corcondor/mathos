#!/usr/bin/env python3
"""Independent SymPy audit of both normalized v32 deep 5-adic charts."""
import sympy as sp

a,b,r,u,T,w,D0=sp.symbols('a b r u T w D0')
F=(4*a**6+(24*b**2-12*r)*a**4
   +(36*b**4+60*b**2*r+12*r**2)*a**2-3*b**2*r**2-4*r**3)
H=b*(6*a*a+2*b*b+3*r)
Z=a*a-b*b-r
assert sp.expand(F-H**2-4*Z**3)==0
f=sp.expand(F.subs({a:u,b:1,r:T}))
assert sp.Poly(f.subs(T,3)+u**2*(u**2+1)**2,u,modulus=5).is_zero
for e in (1,2,3):
    d=2*e
    Hloc=5**(3*e)*w
    Dloc=5**(2*e)*D0
    Zloc=(Hloc-Dloc)/6
    G=sp.expand((Hloc**2+4*Zloc**3)/5**(3*d))
    target=w**2+(5**e*w-D0)**3/sp.Integer(54)
    assert sp.expand(G-target)==0
    q=sp.symbols('q')
    Tsub=(5**(2*e)*q-3)/4
    g=sp.expand((f.subs(u,5**e*w).subs(T,Tsub))/5**(2*e))
    target_b=4*5**(4*e)*w**6+(24-12*Tsub)*5**(2*e)*w**4+12*(Tsub**2+5*Tsub+3)*w**2-Tsub**2*q
    assert sp.expand(g-target_b)==0
print('PASS: sextic identity, mod-5 factorization and both normalized deep collision charts')
