#!/usr/bin/env python3
"""Independent audit for genuinely rational T=rho/b^2, including b not dividing rho.

This verifies a necessary 5-adic genus-two square condition; it does not
claim to solve the original nested binomial equation.
"""
def F(a,b,r):
    return (4*a**6+(24*b*b-12*r)*a**4+
            (36*b**4+60*b*b*r+12*r*r)*a*a-3*b*b*r*r-4*r**3)

def val(x):
    if x==0:return 10**9
    x=abs(x);v=0
    while x%5==0:x//=5;v+=1
    return v

def qsq(x):
    if x==0:return True
    v=val(x)
    return v%2==0 and x//5**v%5 in (1,4)

def chi(x):
    return 1 if x%5 in (1,4) else -1

def predict(a,b,r):
    u0=a*pow(b,-1,5)%5
    k=val(4*r+3*b*b);d=val(9*r+8*b*b)
    assert k>=1 and d>=1 and min(k,d)==1
    H=6*a*a+2*b*b+3*r
    Z=a*a-b*b-r
    if u0 in (1,4):return True
    if k==1:
        if u0==0:return False
        if d%2:return H%5**((3*d+1)//2)!=0
        h=3*d//2;t=val(H)
        q=-((9*r+8*b*b)//5**d)%5
        if t<h:return True
        if t>h:return chi(q)==1
        assert Z%5**d==0
        G=(b*(H//5**h))**2+4*(Z//5**d)**3
        return qsq(G)
    if u0 in (2,3):return H%25!=0
    s=val(a)
    if k%2:return 2*s<k
    e=k//2;q=(4*r+3*b*b)//5**k
    if s<e:return True
    if s>e:return chi(q)==1
    A=a//5**e
    G=(4*5**(4*e)*A**6+(24*b*b-12*r)*5**(2*e)*A**4+
       (36*b**4+60*b*b*r+12*r*r)*A*A-r*r*q)
    return qsq(G)

def kind(b,r):
    k=val(4*r+3*b*b);d=val(9*r+8*b*b)
    if min(k,d)!=1:return None
    if k==1:
        if d%2:return ('A',d,'odd')
        return ('A',d,'square' if chi(-((9*r+8*b*b)//5**d))==1 else 'nonsquare')
    if k%2:return ('B',k,'odd')
    return ('B',k,'square' if chi((4*r+3*b*b)//5**k)==1 else 'nonsquare')

cases=[]
for b in (2,3,486):
    found={}
    for rho in range(32770,35000):
        if (rho%5)!=(3*b*b)%5 or rho%9 not in (1,4,6,7):continue
        category=kind(b,rho)
        if category and category not in found:found[category]=rho
    for category,rho in found.items():
        count=0
        for a in range(3125):
            oracle=qsq(F(a,b,rho))
            expected=predict(a,b,rho)
            assert oracle==expected,(b,rho,a,category)
            count+=oracle
        cases.append((b,rho,category,count))
print('PASS: rational T=rho/b^2,',len(cases),'families,',
      len(cases)*3125,'exact local comparisons')
print('Class representatives (b,rho,kind,passes):')
for case in cases:print(case)
