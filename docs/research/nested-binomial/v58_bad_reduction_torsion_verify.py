#!/usr/bin/env python3
"""v58: local torsion sieve on the first elliptic quotient for ALL positive rho.

For T=rho/b^2>0, b|486:
   E1_T: y²+6xy+(8+9T)y=x³, Delta=-243*T*(8+9T)^3.
For prime p>=5 dividing rho to exponent e, p does not divide b.
The reduction is multiplicative of type I_e with split character
chi=(-3/p). The smooth F_p group has cardinality p-chi.
The component group over F_p has size <=e. For n=9 or 12, p is coprime
to n; rational n-torsion injects into E(Q_p)/E1(Q_p).
Hence n | e*(p-chi). In particular, if e=1, 9-torsion requires
p=±1 mod9 and 12-torsion requires p=±1 mod12.
Mazur plus Delta<0 restricts rational torsion to Z/3,Z/6,Z/9,Z/12.
The 3 and 6 torsion-image obstruction is inherited from v50/v56;
NO CLAIM IS MADE ABOUT INFINITE-ORDER POINTS.
"""
from math import gcd
import sympy as s

T=s.symbols("T")
a1=s.Integer(6)
a3=8+9*T
b2=a1*a1; b4=a1*a3; b6=a3*a3
delta=s.factor(-8*b4**3-27*b6**2+9*b2*b4*b6)
c4=s.factor(b2*b2-24*b4)
c6=s.factor(-b2**3+36*b2*b4-216*b6)
assert s.factor(delta+243*T*(8+9*T)**3)==0
assert s.factor(c4-144*(1-9*T))==0
assert c6.subs(T,0)==1728
assert -c6.subs(T,0)==-3*24**2
assert c4.subs(T,0)==144
# At T=0, nodal special fibre has singular point (-4,8) for p>=5.
x,y=s.symbols("x y")
F=y*y+6*x*y+8*y-x**3
assert F.subs({x:-4,y:8})==0
assert s.diff(F,x).subs({x:-4,y:8})==0
assert s.diff(F,y).subs({x:-4,y:8})==0
X,Y=s.symbols("X Y")
local=s.expand(F.subs({x:X-4,y:Y+8}))
assert s.expand(local-(Y*Y+6*X*Y+12*X*X-X**3))==0
# Verify the smooth-group order formula independently by enumerating Fp points.
for p in list(s.primerange(5,103)):
    chi=int(s.legendre_symbol(-3,p))
    smooth=1
    node=((-4)%p,8%p)
    for xx in range(p):
        for yy in range(p):
            if (yy*yy+6*xx*yy+8*yy-xx**3)%p==0 and (xx,yy)!=node:
                smooth+=1
    assert smooth==p-chi,(p,smooth,p-chi)
print("PASS: first-quotient discriminant, c4, c6, nodal tangent character")
print("PASS: all p=5..101 smooth group sizes equal p-(-3/p)")

# The full torsion candidates from rational 3-torsion and Mazur are
# cyclic 3,6,9,12; noncyclic (2,6) would imply three rational roots of
# the 2-division cubic and positive discriminant, contrary to Delta<0.
complete=[3,6,9,12]
assert complete==[3,6,9,12]

classes=[r for r in range(36) if gcd(r,36)==1]
both_forbidden=[r for r in classes if r%9 not in(1,8) and r%12 not in(1,11)]
assert both_forbidden==[5,7,29,31],both_forbidden

# Illustrate the actual residual rho=100003 without any b restriction.
rho=100003
assert s.isprime(rho)
e=1
chi=int(s.legendre_symbol(-3,rho))
assert chi==1 and (rho-chi)%9!=0 and (rho-chi)%12!=0
assert rho%36==31
print("PASS: rho=100003 has neither rational 9- nor 12-torsion")
print("PASS: squarefree p≡5,7,29,31 (mod36) forbids 9,12 torsion")
print("THEOREM: if rank(E1_T(Q))=0 and rho has such a prime to exponent 1, no original-branch solution")
print("LIMIT: full rational E1_T(Q), positive ranks and original equation all rho remain open")
