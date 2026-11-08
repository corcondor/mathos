#!/usr/bin/env python3
"""v86: compact F_100291 Frobenius-Bezout certificates for 3 cubic covers.

All three polynomials below have no Fp root. Unlike exhaustive 100291
trial evaluation, this certificate can be checked using O(log p) exact
finite-field operations:
   R(Z) = Z^p - Z mod f(Z),  B(Z)*R(Z) = 1 mod f(Z).
If f(z)=0 for z∈Fp, Fermat z^p=z and polynomial congruence imply
R(z)=0. The Bezout certificate then gives 0=1, contradiction.
"""
from math import isqrt
p=100291
assert p>2 and all(p%q!=0 for q in range(2,isqrt(p)+1))

def trim(a):
    a=[x%p for x in a]
    while len(a)>1 and not a[-1]:a.pop()
    return a

def remainder(a,b):
    a=trim(a);b=trim(b)
    while len(a)>=len(b) and a!=[0]:
        lead=a[-1]*pow(b[-1],-1,p)%p
        offset=len(a)-len(b)
        for i,z in enumerate(b):
            a[i+offset]=(a[i+offset]-lead*z)%p
        a=trim(a)
    return a

def mul_mod(a,b,mod):
    prod=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):prod[i+j]=(prod[i+j]+x*y)%p
    return remainder(prod,mod)

def power_mod(a,n,mod):
    out=[1]
    while n:
        if n&1:out=mul_mod(out,a,mod)
        a=mul_mod(a,a,mod);n//=2
    return out

# monic f=Z^3+coefficient_Z*Z+constant; centered residues to aid audit
cases=[
 ("6z³-108z-1", [16715,-18,0,1],
  [-3644,19031,33734], [30620,6407,2083]),
 ("3z³-108z-2", [-33431,-36,0,1],
  [-23662,-21155,-40802],[-39152,9132,-17303]),
 ("z³-108z-6",[-6,-108,0,1],
  [-7362,-10457,25175],[14325,-13932,22900]),
]
for name,f,h,inv in cases:
    zpow=power_mod([0,1],p,f)
    hcalc=zpow[:]
    while len(hcalc)<2:hcalc.append(0)
    hcalc[1]=(hcalc[1]-1)%p
    assert trim(hcalc)==trim(h),(name,"Frobenius remainder",hcalc,h)
    assert mul_mod(h,inv,f)==[1],(name,"Bezout inverse")
    assert f[0]%p or f[1]%p
    print("CERTIFIED_NO_FP_ROOT",name,
      "Frob_minus_z_coefficients",h,
      "inverse_coefficients",inv)
print("PASS: all three F100291 cubic root obstructions with short Frobenius/Bezout certificates")
print("Scope: eliminates 3 of 12 original-branch cube-core coefficient types for b=18 at rho=100003; positive-rank integral point classification remains open")
