#!/usr/bin/env python3
"""v95: exact necessary twisted-cube coefficient reduction for the frozen CF goal.

For 6S*r³=T*n(n−1)(n−2), S|(n−2), g=gcd(r,n−1),
r=g*p, n−1=g*q, gcd(p,q)=1, and D=T*q³−6S*p³>0, g²*D=T*q:
 h=gcd(D,q)=gcd(6,q) divides 6, e=D/h divides T,
 T/e=s*A² (s squarefree), q=h*s*z², g=A*s*z,
 n−1=h*A*s²*z³, (6S/h)*p³+e=T*h²*s³*z^6.
 Required: gcd(h,S)=1, gcd(e,s)=1, gcd(T/e,S)=1,
 gcd(s,6/h)=1, h*A*s²*z³=1 mod S, gcd(z,e)=1.

Enumerates only necessary coefficient (h,e,s,A) options for all
1<=S<=12, 162S<T<229S, NOT the integer or rational points.
"""
import json
from math import gcd,isqrt
from pathlib import Path

MAX=229*12
spf=list(range(MAX+1))
for p in range(2,isqrt(MAX)+1):
    if spf[p]==p:
        for n in range(p*p,MAX+1,p):
            if spf[n]==n:spf[n]=p

def factor(n):
    f={}
    while n>1:
        p=spf[n];f[p]=f.get(p,0)+1;n//=p
    return f

def divisors(n):
    ans=[1]
    for p,e in factor(n).items():
        ans=[x*p**i for x in ans for i in range(e+1)]
    return sorted(ans)

def sqpart(n):
    s=A=1
    for p,e in factor(n).items():
        s*=p**(e%2);A*=p**(e//2)
    assert n==s*A*A
    return s,A

def valid(S,T):
    counts=[0]*5
    hvals=divisors(6*S); evals=divisors(T)
    selected=[]
    for h in hvals:
        for e in evals:
            counts[0]+=1
            if 6%h or gcd(h,S)!=1:continue
            counts[1]+=1
            w=T//e;s,A=sqpart(w)
            if gcd(e,s)!=1 or gcd(w,S)!=1:continue
            counts[2]+=1
            if gcd(s,6//h)!=1:continue
            counts[3]+=1
            if not any((h*A*s*s*pow(z,3,S)-1)%S==0
                    for z in range(S) if gcd(z,S)==1):
                continue
            counts[4]+=1
            selected.append((h,e,s,A))
    return counts,selected

# Verify all identities on a documented small solution with S|(n−2).
S,T,n,r=13,2352,28,84
g=gcd(r,n-1);p=r//g;q=(n-1)//g
D=T*q**3-6*S*p**3
h=gcd(D,q);e=D//h;s,A=sqpart(T//e)
z=isqrt(q//h//s)
assert 6*S*r**3==T*n*(n-1)*(n-2) and (n-2)%S==0
assert g*g*D==T*q and h==gcd(6,q) and T%e==0
assert z*z==q//h//s and q==h*s*z*z and g==A*s*z
assert n-1==h*A*s*s*z**3
assert (6*S//h)*p**3+e==T*h*h*s**3*z**6
assert (h*A*s*s*z**3-1)%S==0
print("PASS: known small rational point satisfies all v95 identities")

total=[0]*5; rows=[]
for S in range(1,13):
    counts=[0]*5
    for T in range(162*S+1,229*S):
        steps,selected=valid(S,T)
        for i,v in enumerate(steps):
            counts[i]+=v;total[i]+=v
    rows.append({"S":S,"curves":67*S-1,"before":counts[0],
       "after_h":counts[1],"after_squarefree":counts[2],
       "after_exact_gcd_h":counts[3],"after_cubic_mod_S":counts[4]})
    print("PASS S",S,"curves",67*S-1,"necessary parameter counts",counts)
assert sum(r["curves"] for r in rows)==5214
assert total==[409728,104588,61571,53003,43922],total
print("CERTIFIED_V95_5214_CURVE_PARAMETER_COUNTS",json.dumps({
    "curves":5214,"stages":total,"by_S":rows,
    "status":"complete necessary finite-coefficient sieve, not integer-point certificate"
},ensure_ascii=False))
