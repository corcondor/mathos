#!/usr/bin/env python3
"""Exact finite certificates completing upper ell=k-2, effective d>=3.

The analytic bound k<2^22 is proved in
v4_upper_complement_two_sharper_bounds.md.  The generator enumerates i
first; the independent verifier enumerates d first and finds a triangular
interval via a different inequality. Both orientations j=d and j=i-d
are covered. All congruences are exact Lucas calculations.
"""
import argparse
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import time

from v4_lower_l1_single_top import lucas_fast, lucas_check, nth_root_floor, PRIMES

K_LIMIT = 2**22
A_LIMIT = (K_LIMIT-1)*(K_LIMIT-2)//2 + 10*(K_LIMIT-3)-1
I_LIMIT = nth_root_floor(6*A_LIMIT,3)+2


def choose_valuation_floor(n,m,p):
    """Generator: Legendre factorial differences, using floor divisions."""
    value=0
    a,b,c=n,m,n-m
    while a:
        a//=p
        b//=p
        c//=p
        value+=a-b-c
    return value


def choose_valuation_carries(n,m,p):
    """Verifier: Kummer carries in m+(n-m), independent of factorials."""
    a,b=m,n-m
    carry=0
    count=0
    while a or b or carry:
        a,ad=divmod(a,p)
        b,bd=divmod(b,p)
        carry=int(ad+bd+carry>=p)
        count+=carry
    return count


def allowed(i,k,a):
    if not (23<=k<K_LIMIT and i+2<=k):
        return False
    b=k*(k-1)//2
    t=a-b
    if not (k<=t<=b):
        return False
    if t >= (5 if k>=802 else 10)*(k-2):
        return False
    return True


def generate_candidates():
    for i in range(6,I_LIMIT+1):
        a=comb(i,3)
        d=3
        while 2*d<=i and a<=A_LIMIT:
            k=min(K_LIMIT-1,(1+isqrt(8*(a-1)+1))//2)
            while k>=max(23,i+2):
                b=k*(k-1)//2
                t=a-b
                # Use the weaker 10(k-2) bound for the stopping condition:
                # its monotonicity remains valid across k=802.
                if t>=10*(k-2):
                    break
                if allowed(i,k,a):
                    for j in sorted({d,i-d}):
                        yield i,j,k,a,t
                k-=1
            a=a*(i-d)//(d+1)
            d+=1


def verification_candidates():
    d=3
    while comb(2*d,d)<=A_LIMIT:
        i=2*d
        a=comb(i,d)
        while a<=A_LIMIT:
            # Find the first k with B(k)+10(k-2)>A by binary search.
            lo,hi=23,K_LIMIT
            while lo<hi:
                mid=(lo+hi)//2
                if mid*(mid-1)//2+10*(mid-2)>a:
                    hi=mid
                else:
                    lo=mid+1
            first=max(lo,i+2)
            # Independently find the last k with B(k)<A.
            lo,hi=23,K_LIMIT
            while lo<hi:
                mid=(lo+hi)//2
                if mid*(mid-1)//2>=a:
                    hi=mid
                else:
                    lo=mid+1
            last=min(K_LIMIT-1,lo-1)
            for k in range(first,last+1):
                b=k*(k-1)//2
                t=a-b
                limit=(5*(k-2) if k>=802 else 10*(k-2))
                if not (k<=t<=b and t<limit):
                    continue
                for j in ([d] if i==2*d else [d,i-d]):
                    yield i,j,k,a,t
            a=a*(i+1)//(i+1-d)
            i+=1
        d+=1


def generate(path):
    start=time.monotonic()
    records=[]
    unresolved=[]
    max_i=max_k=max_j=max_p=0
    valuation_count=0
    for i,j,k,a,t in generate_candidates():
        for p in PRIMES:
            lhs=lucas_fast(a,t,p)
            rhs=(lucas_fast(i*i,j*j,p)+lucas_fast(k*k,4*k-4,p))%p
            if lhs!=rhs:
                records.append([i,j,k,p,0])
                max_p=max(max_p,p)
                break
        else:
            # All ordinary residues may vanish. Compare the exact p-adic
            # valuations of the three terms before declaring this unresolved.
            for p in PRIMES:
                values=[choose_valuation_floor(a,t,p),
                        choose_valuation_floor(i*i,j*j,p),
                        choose_valuation_floor(k*k,4*k-4,p)]
                if values.count(min(values))==1:
                    records.append([i,j,k,p,1])
                    valuation_count+=1
                    max_p=max(max_p,p)
                    break
            else:
                unresolved.append([i,j,k])
        max_i=max(max_i,i)
        max_j=max(max_j,j)
        max_k=max(max_k,k)
        if len(records)%50000==0:
            print(json.dumps({"excluded":len(records),"last_i":i,
                              "unresolved":len(unresolved),
                              "elapsed_seconds":round(time.monotonic()-start,3)}),flush=True)
    data={"equation":"C(C(i,j),C(k,k-2))=C(i^2,j^2)+C(k^2,(k-2)^2)",
          "scope":"upper branch, min(j,i-j)>=3, all original indices",
          "analytic_k_strict_bound":K_LIMIT,
          "derived_A_inclusive_bound":A_LIMIT,
          "derived_i_inclusive_bound":I_LIMIT,
          "record_format":["i","j","k","prime","mode_0_residue_1_valuation"],
          "candidate_count":len(records)+len(unresolved),
          "largest_i":max_i,"largest_j":max_j,"largest_k":max_k,
          "largest_obstruction_prime":max_p,
          "valuation_certificates":valuation_count,
          "unresolved":unresolved,"records":records}
    path.write_text(json.dumps(data,separators=(",",":"))+"\n")
    print(json.dumps({k:v for k,v in data.items() if k!="records"},indent=2),flush=True)
    print(json.dumps({"elapsed_seconds":round(time.monotonic()-start,3)}),flush=True)


def verify(path,report_path):
    start=time.monotonic()
    raw=path.read_bytes()
    data=json.loads(raw)
    assert data["analytic_k_strict_bound"]==2**22
    assert data["derived_A_inclusive_bound"]==A_LIMIT
    assert data["derived_i_inclusive_bound"]==I_LIMIT
    assert not data["unresolved"]
    supplied={(i,j,k):(p,mode) for i,j,k,p,mode in data["records"]}
    assert len(supplied)==len(data["records"]),"duplicate candidate"
    count=0
    max_i=max_j=max_k=max_p=0
    checked_primes=set()
    valuation_count=0
    for i,j,k,a,t in verification_candidates():
        p,mode=supplied.pop((i,j,k))
        assert comb(i,j)==a
        assert 3<=min(j,i-j) and i+2<=k<K_LIMIT
        assert t==a-k*(k-1)//2
        if p not in checked_primes:
            assert isinstance(p,int) and p>=2
            assert all(p%q for q in range(2,isqrt(p)+1))
            checked_primes.add(p)
        if mode==0:
            left=lucas_check(a,t,p)
            right=(lucas_check(i*i,j*j,p)+lucas_check(k*k,4*k-4,p))%p
            assert left!=right,(i,j,k,p)
        else:
            assert mode==1
            values=[choose_valuation_carries(a,t,p),
                    choose_valuation_carries(i*i,j*j,p),
                    choose_valuation_carries(k*k,4*k-4,p)]
            assert values.count(min(values))==1,(i,j,k,p,values)
            valuation_count+=1
        count+=1
        max_i=max(max_i,i)
        max_j=max(max_j,j)
        max_k=max(max_k,k)
        max_p=max(max_p,p)
    assert not supplied,"unexamined or extra certificate candidate"
    assert count==data["candidate_count"]
    assert valuation_count==data["valuation_certificates"]
    assert [max_i,max_j,max_k,max_p]==[data[x] for x in
            ["largest_i","largest_j","largest_k","largest_obstruction_prime"]]
    report={"verified":True,
            "uniform_statement":"No upper-branch solution with ell=k-2 and min(j,i-j)>=3",
            "analytic_k_strict_bound":K_LIMIT,
            "candidate_count":count,
            "largest_i":max_i,"largest_j":max_j,"largest_k":max_k,
            "largest_obstruction_prime":max_p,"unresolved":0,
            "valuation_certificates":valuation_count,
            "certificate_sha256":hashlib.sha256(raw).hexdigest(),
            "elapsed_seconds":round(time.monotonic()-start,3),
            "formal_proof_assistant_executed":False,
            "prerequisites":"Shared-prime-part analytic k bound; prior upper-branch ordering/endpoint/gap reductions."}
    report_path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("action",choices=["generate","verify"])
    parser.add_argument("--certificate",type=Path,default=Path("v4_upper_complement_two_dge3_certificates.json"))
    parser.add_argument("--report",type=Path,default=Path("v4_upper_complement_two_dge3_verification.json"))
    args=parser.parse_args()
    if args.action=="generate":generate(args.certificate)
    else:verify(args.certificate,args.report)
