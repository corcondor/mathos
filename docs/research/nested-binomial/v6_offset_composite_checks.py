#!/usr/bin/env python3
"""Exact, derived finite remainder for offset-three ell=1 and R<=12.

R=n/c3(n/gcd(n,3)); the uniform proof bounds n<8192. This is not a
rectangular search in the original four variables.
"""

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, gcd, isqrt
from pathlib import Path
import time

N_MAX = 8191
R_MAX = 12
HERE = Path(__file__).resolve().parent
CERT = HERE / "v6_offset_composite_certificates.json"
REPORT = HERE / "v6_offset_composite_verification.json"
PRIMES = [p for p in range(2,1000)
          if all(p%d for d in range(2,isqrt(p)+1))]
FACT = {}
for p in PRIMES:
    row=[1]*p
    for j in range(1,p):
        row[j]=row[j-1]*j%p
    FACT[p]=row


def smallest_prime_factors(limit):
    table=list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if table[p]==p:
            for m in range(p*p,limit+1,p):
                if table[m]==m:table[m]=p
    return table


SPF=smallest_prime_factors(N_MAX)


def cube_divisor_spf(n):
    answer=1
    while n>1:
        p=SPF[n];a=0
        while n%p==0:
            n//=p;a+=1
        answer*=p**((a+2)//3)
    return answer


def cube_divisor_trial(n):
    answer=1
    p=2
    while p*p<=n:
        a=0
        while n%p==0:
            n//=p;a+=1
        if a:
            answer*=p**((a+2)//3)
        p+=1
    if n>1:answer*=n
    return answer


def lucas_factorial(n,k,p):
    if not 0<=k<=n:return 0
    answer=1
    row=FACT[p]
    while n or k:
        a,b=n%p,k%p
        if b>a:return 0
        answer=answer*row[a]*pow(row[b]*row[a-b]%p,-1,p)%p
        n//=p;k//=p
    return answer


def lucas_direct(n,k,p):
    if k<0 or k>n:return 0
    out=1
    while k:
        a=n%p;b=k%p
        if b>a:return 0
        out=out*comb(a,b)%p
        n//=p;k//=p
    return out


def generated_candidates():
    for n in range(104,N_MAX+1):
        c=cube_divisor_spf(n//gcd(n,3))
        assert n%c==0
        R=n//c
        if R>R_MAX:continue
        A=n*(n-1)*(n-2)//6
        for t in range(1,(R-1)//3+1):
            r=c*(3*R+t)
            assert 3*n<r and 3*r<10*n and 2*r<A
            yield n,R,c,t,r,A


def verified_candidates():
    for R in range(1,R_MAX+1):
        for c in range(1,N_MAX//R+1):
            n=R*c
            if n<104:continue
            if cube_divisor_trial(n//gcd(n,3))!=c:continue
            A=comb(n,3)
            # Enumerate the multiples of c in the original strict interval,
            # rather than reusing the generator's t upper bound.
            for r in range(c*((3*n)//c+1),(10*n-1)//3+1,c):
                assert 3*n<r and 3*r<10*n and 2*r<A
                yield n,R,c,r,A


def exact_constants():
    constants={
        "e_upper_rational":str(F(65,24)+F(1,100)),
        "e_upper_less_than_68_over_25":F(65,24)+F(1,100)<F(68,25),
        "log_48_over_25_comparison_positive_integer":
            48**20-68**13*25**7,
        "log_625_over_32_comparison_positive_integer":
            27**3*32-625*10**3,
        "e9_below_8192_positive_integer":8192*25**9-68**9,
        "initial_exponential_comparison_positive_integer":
            2**17-42*1024,
        "initial_log_comparison_positive_integer":1024-3**6,
    }
    assert constants["e_upper_less_than_68_over_25"]
    for key,value in constants.items():
        if key.endswith("positive_integer"):assert value>0
    return constants


def generate():
    begin=time.monotonic()
    rows=[];unresolved=[]
    for n,R,c,t,r,A in generated_candidates():
        witnesses=[]
        for k in (r,A-r):
            found=None
            for p in PRIMES:
                left=lucas_factorial(A,r,p)
                right=(lucas_factorial(n*n,6*n-9,p)+k*k)%p
                if left!=right:
                    found=p;break
            witnesses.append(found)
        if all(p is not None for p in witnesses):
            rows.append([n,R,c,t,r,*witnesses])
        else:
            unresolved.append([n,R,c,t,r,*witnesses])
    out={
        "equation":"C(C(n,3),k)=C(n^2,(n-3)^2)+k^2",
        "scope":"ell=1, j=n-3, R=n/c3(n/gcd(n,3))<=12, both branches",
        "proved_n_inclusive_bound":N_MAX,
        "proved_R_inclusive_bound":R_MAX,
        "record_format":["n","R","c3(q)","t","r","prime_for_k_r","prime_for_k_A_minus_r"],
        "candidate_pairs":len(rows)+len(unresolved),
        "branch_equations":2*(len(rows)+len(unresolved)),
        "unresolved":unresolved,
        "records":rows,
    }
    CERT.write_text(json.dumps(out,separators=(",",":"))+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="records"},indent=2))
    print(json.dumps({"generation_seconds":time.monotonic()-begin}))
    assert not unresolved


def verify():
    begin=time.monotonic()
    raw=CERT.read_bytes()
    data=json.loads(raw)
    assert data["proved_n_inclusive_bound"]==N_MAX
    assert data["proved_R_inclusive_bound"]==R_MAX
    assert not data["unresolved"]
    records={}
    for n,R,c,t,r,pl,pu in data["records"]:
        key=n,r
        assert key not in records and r==c*(3*R+t)
        for p in (pl,pu):
            assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
        records[key]=(R,c,pl,pu)
    assert len(records)==data["candidate_pairs"]
    count=0;maxp=0;maxn=0;by_R={};examples=[]
    for n,R,c,r,A in verified_candidates():
        old_R,old_c,pl,pu=records.pop((n,r))
        assert (old_R,old_c)==(R,c)
        for k,p in ((r,pl),(A-r,pu)):
            L=lucas_direct(A,r,p)
            X=lucas_direct(n*n,(n-3)**2,p)
            Y=pow(k,2,p)
            assert L!=(X+Y)%p
            maxp=max(maxp,p)
        count+=1;maxn=max(maxn,n)
        by_R[R]=by_R.get(R,0)+1
        if len(examples)<8:
            examples.append({"n":n,"R":R,"r":r,"prime_witnesses":[pl,pu]})
    assert not records
    assert count==data["candidate_pairs"]
    out={
        "status":"pass",
        "uniform_statement":"No solution with ell=1,j=i-3 and i/c3(i/gcd(i,3))<=12",
        "exact_constant_checks":exact_constants(),
        "verified_candidate_pairs":count,
        "verified_branch_equations":2*count,
        "by_R":by_R,
        "max_n":maxn,
        "max_prime":maxp,
        "unresolved":0,
        "certificate_sha256":hashlib.sha256(raw).hexdigest(),
        "coverage_independence":"n-first versus R/c-first; t-bound versus original strict r inequalities",
        "residue_independence":"factorial tables versus direct math.comb on Lucas digits; complementary X index in verifier",
        "factorization_independence":"smallest-prime-factor sieve versus trial division",
        "examples":examples,
        "formalized_in_Lean":False,
        "verification_seconds":time.monotonic()-begin,
    }
    REPORT.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("action",choices=("generate","verify","all"))
    args=parser.parse_args()
    exact_constants()
    if args.action in ("generate","all"):generate()
    if args.action in ("verify","all"):verify()
