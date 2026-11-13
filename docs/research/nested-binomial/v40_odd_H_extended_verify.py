#!/usr/bin/env python3
"""v40: exact arithmetic and group-law certificate for 3R±H,4R±H,5R±H.

The domain is T=(p/b)^2-1, p>b, b|486. No cutoff on p in the
divisor cases. Necessary integer recovery is not the original equation.
"""
from math import gcd,isqrt
import sympy as s

q=s.symbols("q");T=q*q-1
A=-T*T*(4*T+3);B=12*(T*T+5*T+3);C=12*(2-T)
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
H=(-2*(q-1)*(q+1)**2*(2*q+1),
   6*(q-1)*(q+1)**2*(2*q+1)*(3*q-1))
def add(P,Q):
    x,y=P;u,v=Q
    t=((3*x*x+2*B*x+A*C)/(2*y) if s.cancel(x-u)==0 else (v-y)/(u-x))
    t=s.cancel(t)
    xx=s.factor(s.cancel(t*t-B-x-u))
    yy=s.factor(s.cancel(t*(x-xx)-y))
    return xx,yy
forms={
(3,1):(q+1)**2*(2*q+1)/(2*(q+13)),
(3,-1):(q-1)*(q+1)*(2*q+1)/(2*(q-7)),
(4,1):(q+1)*(q+3)**2*(2*q-1)/(2*(q*q+20*q-29)),
(4,-1):(q-1)**2*(2*q-1)/(2*(q-13)),
(5,1):(q-1)*(q+7)**2*(2*q+1)/(2*(q*q+30*q-79)),
(5,-1):(q-3)**2*(q-1)*(2*q+1)/(2*(q*q-20*q-29))}
P=R
for m in range(1,6):
    if m>1:P=add(P,R)
    if m>=3:
        for eps in (1,-1):
            V=add(P,(H[0],eps*H[1]))
            assert s.cancel(A/V[0]-forms[m,eps])==0
            assert s.factor(V[1]**2-V[0]**3-B*V[0]**2-A*C*V[0]-4*A*A)==0
assert s.cancel((forms[3,1]-q*q)+(3*q-1)*(7*q+1)/(2*(q+13)))==0
assert s.cancel((forms[4,1]-q*q)+3*(q-3)*(3*q-1)*(3*q+1)/(2*(q*q+20*q-29)))==0
assert s.cancel((forms[5,1]-q*q)+(q-7)*(3*q+1)*(11*q-7)/(2*(q*q+30*q-79)))==0

p,b=s.symbols("p b")
D=p*p-20*p*b-29*b*b
N=(p-3*b)**2*(p-b)*(2*p+b)
# If D|N, these two polynomial identities give D|19200 b^5:
assert s.expand(N-D*(2*p*p+27*p*b+621*b*b)-1200*b**3*(11*p+15*b))==0
assert s.expand(121*D-(11*p-235*b)*(11*p+15*b)-16*b*b)==0
assert 19200==2**8*3*5**2

out={}
for mode in ((3,-1),(4,1),(4,-1),(5,1),(5,-1)):
    m,eps=mode
    count=integral=squares=0
    near=[]
    for e in (0,1):
      for f in range(6):
        bv=2**e*3**f
        if mode==(3,-1):
            pp=[7*bv+2**i*3**j*5**k
                for i in range(5+3*e) for j in range(3+3*f) for k in range(2)]
        elif mode==(4,-1):
            pp=[13*bv+2**i*3**j*5**k
                for i in range(5+3*e) for j in range(3+3*f) for k in range(3)]
        elif mode==(5,-1):
            pp=[]
            for i in range(9+5*e):
              for j in range(2+5*f):
               for k in range(3):
                dv=2**i*3**j*5**k
                count+=1
                t=isqrt(129*bv*bv+dv)
                if t*t==129*bv*bv+dv:pp.append(10*bv+t)
        elif mode==(4,1):
            pp=range(bv+1,3*bv)
        else:
            pp=range(bv+1,7*bv)
        for pv in pp:
            if mode==(3,-1):num=(pv*pv-bv*bv)*(2*pv+bv);den=2*(pv-7*bv)
            elif mode==(4,-1):num=(pv-bv)**2*(2*pv-bv);den=2*(pv-13*bv)
            elif mode==(5,-1):
                num=(pv-3*bv)**2*(pv-bv)*(2*pv+bv)
                den=2*(pv*pv-20*pv*bv-29*bv*bv)
            elif mode==(4,1):
                num=(pv+bv)*(pv+3*bv)**2*(2*pv-bv)
                den=2*(pv*pv+20*pv*bv-29*bv*bv)
            else:
                num=(pv-bv)*(pv+7*bv)**2*(2*pv+bv)
                den=2*(pv*pv+30*pv*bv-79*bv*bv)
            if mode!=(5,-1):
                if den<=0 or num<=0 or num<=pv*pv*den:continue
                count+=1
            assert den>0 and num>pv*pv*den,(mode,bv,pv)
            if num%den:continue
            integral+=1
            av=isqrt(num//den)
            if av*av!=num//den:continue
            squares+=1
            rho=pv*pv-bv*bv
            if rho>=32770 and gcd(av,bv)==1 and rho%9 in (1,4,6,7):
                near.append((bv,pv,av,rho,gcd(av,rho),gcd(av,3)))
    expected={
        (3,-1):(1638,1260,0,[]),
        (4,1):(1788,19,0,[]),
        (4,-1):(2457,1890,57,[(9,317,385,100408,77,1),
                              (18,298,595,88480,35,1)]),
        (5,1):(4980,44,10,[]),
        (5,-1):(6003,86,12,[])}
    assert (count,integral,squares,sorted(near))==expected[mode],(mode,count,integral,squares,near)
    assert all(g!=h for _,_,_,_,g,h in near)
    out[str(mode)]={"candidates":count,"integer_a2":integral,
                    "square_a2":squares,"near":near,"valid":0}
assert sum(v["candidates"] for v in out.values())==16866
print("PASS: exact six symbolic group-law identities; inequality excludes 3R+H")
print("PASS: Bezout D | 19200*b^5 for 5R-H, all 16866 candidates tested")
print("PASS: |m|=3,4,5 with H coefficient ±1: zero accepted integer candidates")
for mode,entry in out.items():print(mode,entry)
