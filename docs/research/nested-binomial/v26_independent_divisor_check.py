#!/usr/bin/env python3
"""Independent pure-Python exhaustive enumeration for the 4R integer-lift theorem."""
from math import gcd, isqrt
from itertools import product

counts = dict(divisors_checked=0, positive_rho_from_divisors=0,
              integer_a_squared=0,square_a_squared=0,primitive=0,
              primitive_and_z_positive=0,primitive_and_v20_rho_mod9=0)
solutions=[]
for e in (0,1):
 for f in range(6):
  b=(2**e)*(3**f)
  for i,j,k in product(range(6+4*e),range(3+4*f),range(3)):
   d=2**i * 3**j * 5**k
   counts['divisors_checked']+=1
   if d<=24*b*b or (d-24*b*b)%7:continue
   rho=(d-24*b*b)//7
   counts['positive_rho_from_divisors']+=1
   numerator=4*rho*(4*rho+3*b*b)
   if numerator%d:continue
   counts['integer_a_squared']+=1
   a2=numerator//d
   a=isqrt(a2)
   if a*a!=a2:continue
   counts['square_a_squared']+=1
   if gcd(a,b)!=1: continue
   counts['primitive']+=1
   solutions.append((b,rho,a))
   if a2<=b*b+rho:continue
   counts['primitive_and_z_positive']+=1
   if rho%9 in (1,4,6,7):
    counts['primitive_and_v20_rho_mod9']+=1
assert sorted(solutions)==[(1,3,2),(1,18,6)]
assert counts=={'divisors_checked':3744,'positive_rho_from_divisors':346,
               'integer_a_squared':346,'square_a_squared':24,'primitive':2,
               'primitive_and_z_positive':1,'primitive_and_v20_rho_mod9':0}
print('PASS independent pure-Python divisor enumeration')
print('counts:',counts)
print('primitive points:',solutions)
