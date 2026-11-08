#!/usr/bin/env python3
"""Exact finite divisor certificate for (R+Q) and (R-Q) on quadratic K3.

We only classify recovered integral a in the subfamily
b | 486, p^2 = b^2+rho, p,b positive integers, p/b>1.
This is NOT a global classification of the original binomial equation.
"""
from math import gcd, isqrt

bs=sorted(2**e*3**f for e in range(2) for f in range(6))
assert bs==[b for b in range(1,487) if 486%b==0]
survivors=[]
examined=0
integral=0
for e in range(2):
    for f in range(6):
        b=2**e*3**f
        # d=p-2b>0 divides 45*b^3.
        for i in range(3*e+1):
            for j in range(3*f+3):
                for k in (0,1):
                    d=2**i*3**j*5**k
                    examined+=1
                    p=2*b+d
                    numerator=(p+b)*(4*p*p-b*b)
                    denominator=4*d
                    if numerator%denominator:
                        continue
                    integral+=1
                    a2=numerator//denominator
                    a=isqrt(a2)
                    if a*a==a2:
                        rho=p*p-b*b
                        assert a2>p*p
                        survivors.append((b,d,p,a,rho))

expected=[(2*3**h,3**(h+1),7*3**h,12*3**h,45*9**h)
          for h in range(6)]
assert examined==630 and integral==318
assert sorted(survivors)==sorted(expected),survivors
assert all(gcd(a,b)>1 and rho%9==0
           for b,d,p,a,rho in survivors)
# R-Q would have a^2/b^2=(q-1)(4q^2-1)/(4(q+2)).
# For q>1, its difference from q^2 is (-12q^2-q+1)/(4(q+2))<0.
print("PASS: 12 b divisors, 630 structural divisor candidates, 318 integral a²")
print("PASS: exactly six squared a², all fail gcd(a,b)=1 and rho mod9")
print("SQUARES:",survivors)
print("No original integer candidate arises from R+Q or R-Q in this boundary family.")
