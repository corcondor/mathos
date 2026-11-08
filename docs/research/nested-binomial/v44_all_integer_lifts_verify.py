#!/usr/bin/env python3
"""v44 complete original-solution-relevant rational point scan, rho<=100000.

Exhausts every (rho,b,a) that a solution of the original nested binomial
equation could induce. NO assumption that the elliptic point belongs to
<R>, <R,H>, or any known Mordell-Weil subgroup.

The theorem is conditional on the established v21 necessary bound
a^2 < 152*rho*ln(rho) and v20 congruence/integer-recovery formulas.
It is NOT an enumeration of all rational points of E_T(Q).
"""
from concurrent.futures import ProcessPoolExecutor, as_completed
from math import gcd, isqrt, comb
import json
import hashlib
import os
from pathlib import Path

START, END=32770,100000
B_VALUES=(1,2,3,6,9,18,27,54,81,162,243,486)
PRIMES=(5,7,11,13,17,19,23,29,31,37,41,43,47,53)
LUCAS_PRIMES=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
RESIDUES={p:{x*x%p for x in range(p)} for p in PRIMES}

def F(a,b,r):
    x=a*a;v=b*b
    return 4*x**3+12*(2*v-r)*x*x+12*(3*v*v+5*v*r+r*r)*x-r*r*(3*v+4*r)

def prime_masks(r,b):
    out=[]
    for p in PRIMES:
        rr=r%p; bb=b*b%p
        allowed=tuple((
          (4*(z:=a*a%p)**3+(24*bb-12*rr)*z*z+
           (36*bb*bb+60*bb*rr+12*rr*rr)*z-
           3*bb*rr*rr-4*rr**3)%p in RESIDUES[p])
          for a in range(p))
        out.append((p,allowed))
    return out

def segment(lo,hi):
    count=[0]*6
    squares=[]; branch=[]; zero=0
    for r in range(lo,hi+1):
        if r%9 not in (1,4,6,7):continue
        count[0]+=1
        amax=isqrt(152*r*r.bit_length())
        sqr=0
        for b in B_VALUES:
            amin=max(b+1,isqrt(b*b+r)+1)
            if amin>amax:continue
            step=b if b%2==0 else 2*b
            allowed_starts=[a for a in range(step)
                if (a*a-r)%b==0 and (r-a-b)%2==0]
            masks=prime_masks(r,b)
            for u in allowed_starts:
                first=amin+(u-amin)%step
                for a in range(first,amax+1,step):
                    count[1]+=1
                    if gcd(a,b)>1 or gcd(a,r)!=gcd(a,3):continue
                    count[2]+=1
                    if any(not mask[a%p] for p,mask in masks):continue
                    count[3]+=1
                    ff=F(a,b,r)
                    if ff<0:continue
                    y=isqrt(ff)
                    if y*y!=ff:continue
                    count[4]+=1
                    sqr+=1
                    squares.append((r,b,a,y))
                    for sg in (-1,1):
                        top=2*a*(a*a+3*b*b)-r*(3*b+2*a)+sg*y
                        bot=2*b*r
                        if top%bot:continue
                        t=top//bot
                        if t<=0:continue
                        count[5]+=1
                        q=t*t+3*t+3
                        ntop=b*b*q+a*b*(t+6)-a*a+r
                        if ntop%(9*a*b):continue
                        n=ntop//(9*a*b)
                        R=3*n+t
                        if n<104 or t*t<=9*n or 3*R>=10*n:continue
                        # Recompute both integer reconstruction identities.
                        assert 81*a*n*(n-1)==b*(9*n*q+t**3)
                        assert r==a*a+a*b*(9*n-t-6)-b*b*q
                        branch.append((r,b,a,y,t,n))
        if not sqr:zero+=1
    return {'segment':[lo,hi],'counts':count,'squares':squares,'branch':branch,'zero_rho':zero}

def lucas(n,k,p):
    if k<0 or k>n:return 0
    v=1
    while n or k:
        aa=n%p;bb=k%p
        if bb>aa:return 0
        v=v*comb(aa,bb)%p
        n//=p;k//=p
    return v

def witness(n,k):
    A=n*(n-1)*(n-2)//6
    r=min(k,A-k)
    return next((p, lucas(A,r,p), (lucas(n*n,6*n-9,p)+k*k)%p)
       for p in LUCAS_PRIMES
       if lucas(A,r,p)!=(lucas(n*n,6*n-9,p)+k*k)%p)

def lambda_dummy_segment(x):
    return segment(*x)

if __name__=="__main__":
    ranges=[(x,min(x+1999,END)) for x in range(START,END+1,2000)]
    all_count=[0]*6; sq=[];branches=[];zero=0
    with ProcessPoolExecutor(max_workers=2) as pool:
        for record in pool.map(lambda_dummy_segment,ranges):
            for j,v in enumerate(record['counts']):all_count[j]+=v
            sq.extend(record['squares']);branches.extend(record['branch'])
            zero+=record['zero_rho']
    sq.sort();branches.sort()
    assert len(sq)==987 and len(branches)==9
    assert [v for v in sq if v[0]<=32970]==[
        (32773,3,362,61661061),
        (32784,1,191,550088),
        (32824,81,577,361059120),
        (32884,9,211,4125492)],"Independent 201-rho audit mismatch"
    assert all_count==[29881,685305097,383326698,109488,987,50],all_count
    assert zero==28933
    expected=[
      (34072,27,859,1302,6076),
      (34387,18,1381,8322,101251),
      (37822,81,1195,1092,9126),
      (39115,486,1657,595,11662),
      (42463,27,2278,20418,551368),
      (52258,243,745,80,250),
      (52792,243,2551,2632,73696),
      (65656,243,1927,920,12000),
      (76600,3,1063,9576,29792)]
    assert [(r,b,a,t,n) for r,b,a,y,t,n in branches]==expected
    proof=[]
    for r,b,a,y,t,n in branches:
        R=3*n+t
        AA=n*(n-1)*(n-2)//6
        if R>=AA:raise AssertionError("invalid k")
        witnesses={}
        for name,k in (('k=r',R),('k=A-r',AA-R)):
            witnesses[name]=witness(n,k)
        proof.append(dict(rho=r,b=b,a=a,t=t,n=n,witnesses=witnesses))
    result={'scope':'All possible original-solution integer lifts of any rational elliptic point with rho in [32770,100000], conditional on v20/v21 necessary inequalities; not all E(Q)',
            'rho_range':[START,END],'b_values':B_VALUES,
            'rho_mod9_cases':all_count[0], 'a_b_values_tested':all_count[1],
            'gcd_and_basic_survivors':all_count[2],
            'local_prime_survivors':all_count[3],
            'sextic_squares':all_count[4],
            'positive_integer_t':all_count[5],
            'sextic_square_rho_zero':zero,
            'reconstructed_branch_candidates':proof,
            'original_solutions':0,'new_lower_rho':100003}
    destination=os.environ.get("MATHOS_CERTIFICATE_PATH","")
    if destination:
        out=Path(destination)
        out.parent.mkdir(parents=True,exist_ok=True)
        evidence={"method":"v44 integer-lift exhaustive scan (no MW subgroup assumption)",
                  "rho_range":[START,END],"counts":result,
                  "integer_sextic_square_points":sq,
                  "recovered_branch_points":branches}
        payload=json.dumps(evidence,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
        out.write_text(payload,encoding="utf-8")
        print("WROTE_CERTIFICATE:",out,"SQUARE_POINTS",len(sq),flush=True)
        print("FULL_SQUARE_CERTIFICATE_SHA256:",hashlib.sha256(payload.encode("utf-8")).hexdigest(),flush=True)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    print('PASS: all lifts, original equation modulo Lucas primes, both k branches')
