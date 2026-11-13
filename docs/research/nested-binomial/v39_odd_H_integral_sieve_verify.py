#!/usr/bin/env python3
"""v39: first odd-H sections on the saturated K3 basis.

P=mR +/- H, |m|<=2; T=(p/b)^2-1, b divides 486, p>b.
No claim about all E_T(Q) or about the original four-variable equation.
"""
from math import gcd,isqrt
import sympy as sp

q=sp.symbols("q")
T=q*q-1
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
H=(-2*(q-1)*(q+1)**2*(2*q+1),
   6*(q-1)*(q+1)**2*(2*q+1)*(3*q-1))

def plus(P,V):
    x,y=P;u,v=V
    z=sp.factor(sp.cancel((v-y)/(u-x)))
    X=sp.factor(sp.cancel(z*z-B-x-u))
    Y=sp.factor(sp.cancel(z*(x-X)-y))
    return (X,Y)

RplusH=plus(R,H)
RminusH=plus(R,(H[0],-H[1]))
twoR=(5*T*T,3*T*T*(9*T+8)) # checked from the group law for 2R
# Instead calculate 2R exactly via tangent; the supplied y for 2R is checked.
slope=(3*R[0]**2+2*B*R[0]+A*C)/(2*R[1])
X2=sp.factor(sp.cancel(slope*slope-B-2*R[0]))
Y2=sp.factor(sp.cancel(slope*(R[0]-X2)-R[1]))
assert sp.factor(X2-5*T*T)==0
assert sp.factor(Y2-3*T*T*(9*T+8))==0
twoR=(X2,Y2)
plus2=plus(twoR,H)
minus2=plus(twoR,(H[0],-H[1]))
ratios={
    "H":sp.factor(A/H[0]),
    "R+H":sp.factor(A/RplusH[0]),
    "R-H":sp.factor(A/RminusH[0]),
    "2R+H":sp.factor(A/plus2[0]),
    "2R-H":sp.factor(A/minus2[0]),
}
expected={
    "H":(q-1)*(2*q-1)/2,
    "R+H":(q-1)**2*(2*q+1)/(2*(q+3)),
    "R-H":(q+1)*(2*q+1)/2,
    "2R+H":(q-1)*(q+1)*(2*q-1)/(2*(q+7)),
    "2R-H":(q+1)**2*(2*q-1)/(2*(q-3)),
}
for name in ratios:
    assert sp.factor(sp.cancel(ratios[name]-expected[name]))==0,name

# Three cases fail the strict a^2>p^2 immediately:
assert sp.cancel((sp.factor(expected["H"]-q*q))-(-(3*q-1)/2))==0
assert sp.cancel((sp.factor(expected["R+H"]-q*q))-(-(3*q-1)*(3*q+1)/(2*(q+3))))==0
assert sp.cancel((sp.factor(expected["2R+H"]-q*q))-(-(3*q+1)*(5*q-1)/(2*(q+7))))==0

rows_rh=[]
divisor_pairs=0
for e in (0,1):
 for f in range(6):
    b=2**e*3**f
    for u in range(1,b+1):
        if b*b%u:continue
        v=b*b//u
        divisor_pairs+=1
        if v<=u or (v-u)%8 or (u+v-6*b)%8:continue
        a=(v-u)//8
        p=(u+v-6*b)//8
        if p<=b:continue
        assert (4*p+3*b)**2-(4*a)**2==b*b
        assert 2*a*a==(p+b)*(2*p+b)
        rho=p*p-b*b
        rows_rh.append((b,p,a,rho))
assert divisor_pairs==78 and len(rows_rh)==10,(divisor_pairs,rows_rh)
pre=[r for r in rows_rh if r[3]>=32770 and gcd(r[2],r[0])==1
     and r[3]%9 in (1,4,6,7)]
assert pre==[(243,7199,7381,51766552)],pre
assert gcd(7381,51766552)==61 and gcd(7381,3)==1

counts={"structural_divisors":0,"integer_a2":0,"square_a2":0}
rows=[]
for e in (0,1):
 for f in range(6):
    b=2**e*3**f
    for i in range(5+3*e):
     for j in range(3*f+1):
      for k in (0,1):
        d=2**i*3**j*5**k
        counts["structural_divisors"]+=1
        p=3*b+d
        N=(p+b)**2*(2*p-b)
        assert N%d==0
        if N%(2*d):continue
        counts["integer_a2"]+=1
        a2=N//(2*d)
        a=isqrt(a2)
        if a*a!=a2:continue
        counts["square_a2"]+=1
        rho=p*p-b*b
        rows.append((b,p,a,rho))
assert counts=={"structural_divisors":1326,"integer_a2":1020,"square_a2":38},counts
assert not [r for r in rows if r[3]>=32770 and gcd(r[2],r[0])==1
            and r[3]%9 in (1,4,6,7)]

print("PASS: H,R±H,2R±H symbolic group law and boundary inequality")
print("PASS: R-H uses 78 exact factor pairs, 10 integer positive solutions")
print("PASS: the sole R-H near-survivor violates gcd(a,rho)=gcd(a,3)")
print("PASS: 2R-H reduces to 1326 divisors, 1020 integral a², 38 squares")
print("PASS: all odd-H sections mR±H for |m|<=2 excluded by necessary conditions")
