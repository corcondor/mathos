#!/usr/bin/env python3
"""Exact certificates for upper j=i-2 with min(ell,k-ell)>=3.

Uses the proved strict analytic bound i<2^22.  Triangular A=C(i,2)
lies just above B=C(k,e). Generator enumerates k first; independent
verifier enumerates e first and searches the triangular interval with
different inequalities. Both ell orientations are covered.
"""
import argparse
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import time

from v4_lower_l1_single_top import lucas_fast, lucas_check, nth_root_floor, PRIMES
from v4_upper_complement_two_dge3 import choose_valuation_floor, choose_valuation_carries

I_STRICT = 2**22
B_MAX = (I_STRICT-1)*(I_STRICT-2)//2-1
K_MAX = nth_root_floor(6*B_MAX,3)+2


def admissible(i,k,b):
    if not (23<=i<I_STRICT and k+2<=i):
        return False
    a=i*(i-1)//2
    t=a-b
    return i<=t<=b and t<(5 if i>=802 else 10)*(i-2)


def generate_candidates():
    for k in range(6,K_MAX+1):
        e=3
        b=comb(k,e)
        while 2*e<=k and b<=B_MAX:
            i=max(23,k+2,(1+isqrt(8*b+1))//2+1)
            while i<I_STRICT:
                a=i*(i-1)//2
                t=a-b
                # A(i)-10(i-2) is strictly increasing for i>=23.
                # Stop only with the coarse gap, to preserve coverage.
                if t>=10*(i-2):
                    break
                if admissible(i,k,b):
                    for ell in sorted({e,k-e}):
                        yield i,k,ell,a,b,t
                i+=1
            b=b*(k-e)//(e+1)
            e+=1


def verification_candidates():
    e=3
    while comb(2*e,e)<=B_MAX:
        k=2*e
        b=comb(k,e)
        while b<=B_MAX:
            # First triangular A>B.
            lo,hi=23,I_STRICT
            while lo<hi:
                mid=(lo+hi)//2
                if mid*(mid-1)//2>b:
                    hi=mid
                else:
                    lo=mid+1
            first=max(lo,k+2)
            # First i violating A(i)-10(i-2)<B.
            lo,hi=23,I_STRICT
            while lo<hi:
                mid=(lo+hi)//2
                if mid*(mid-1)//2-10*(mid-2)>=b:
                    hi=mid
                else:
                    lo=mid+1
            last=min(I_STRICT-1,lo-1)
            for i in range(first,last+1):
                a=i*(i-1)//2
                t=a-b
                limit=5*(i-2) if i>=802 else 10*(i-2)
                if i<=t<=b and t<limit:
                    for ell in ([e] if k==2*e else [e,k-e]):
                        yield i,k,ell,a,b,t
            b=b*(k+1)//(k+1-e)
            k+=1
        e+=1


def generate(path):
    start=time.monotonic()
    records=[]
    unresolved=[]
    count_val=0
    max_i=max_k=max_ell=max_p=0
    for i,k,ell,a,b,t in generate_candidates():
        for p in PRIMES:
            left=lucas_fast(a,t,p)
            right=(lucas_fast(i*i,4*i-4,p)+lucas_fast(k*k,ell*ell,p))%p
            if left!=right:
                records.append([i,k,ell,p,0])
                max_p=max(max_p,p)
                break
        else:
            for p in PRIMES:
                vals=[choose_valuation_floor(a,t,p),
                      choose_valuation_floor(i*i,4*i-4,p),
                      choose_valuation_floor(k*k,ell*ell,p)]
                if vals.count(min(vals))==1:
                    records.append([i,k,ell,p,1])
                    count_val+=1
                    max_p=max(max_p,p)
                    break
            else:
                unresolved.append([i,k,ell])
        max_i=max(max_i,i)
        max_k=max(max_k,k)
        max_ell=max(max_ell,ell)
        if len(records)%50000==0:
            print(json.dumps({"excluded":len(records),"last_k":k,
                              "unresolved":len(unresolved),
                              "elapsed_seconds":round(time.monotonic()-start,3)}),flush=True)
    data={"equation":"C(C(i,i-2),C(k,ell))=C(i^2,(i-2)^2)+C(k^2,ell^2)",
          "scope":"upper branch, min(ell,k-ell)>=3, all original indices",
          "analytic_i_strict_bound":I_STRICT,
          "derived_B_inclusive_bound":B_MAX,
          "derived_k_inclusive_bound":K_MAX,
          "record_format":["i","k","ell","prime","mode_0_residue_1_valuation"],
          "candidate_count":len(records)+len(unresolved),
          "largest_i":max_i,"largest_k":max_k,"largest_ell":max_ell,
          "largest_obstruction_prime":max_p,
          "valuation_certificates":count_val,
          "unresolved":unresolved,"records":records}
    path.write_text(json.dumps(data,separators=(",",":"))+"\n")
    print(json.dumps({k:v for k,v in data.items() if k!="records"},indent=2),flush=True)
    print(json.dumps({"elapsed_seconds":round(time.monotonic()-start,3)}),flush=True)


def verify(path,report_path):
    start=time.monotonic()
    raw=path.read_bytes()
    data=json.loads(raw)
    assert data["analytic_i_strict_bound"]==I_STRICT
    assert data["derived_B_inclusive_bound"]==B_MAX
    assert data["derived_k_inclusive_bound"]==K_MAX
    assert not data["unresolved"]
    cert={(i,k,ell):(p,mode) for i,k,ell,p,mode in data["records"]}
    assert len(cert)==len(data["records"])
    count=val_count=0
    max_i=max_k=max_ell=max_p=0
    checked_primes=set()
    for i,k,ell,a,b,t in verification_candidates():
        p,mode=cert.pop((i,k,ell))
        assert comb(k,ell)==b
        assert 3<=min(ell,k-ell) and k+2<=i<I_STRICT
        if p not in checked_primes:
            assert isinstance(p,int) and p>=2
            assert all(p%q for q in range(2,isqrt(p)+1))
            checked_primes.add(p)
        if mode==0:
            left=lucas_check(a,t,p)
            right=(lucas_check(i*i,4*i-4,p)+lucas_check(k*k,ell*ell,p))%p
            assert left!=right,(i,k,ell,p)
        else:
            assert mode==1
            vals=[choose_valuation_carries(a,t,p),
                  choose_valuation_carries(i*i,4*i-4,p),
                  choose_valuation_carries(k*k,ell*ell,p)]
            assert vals.count(min(vals))==1,(i,k,ell,p,vals)
            val_count+=1
        count+=1
        max_i=max(max_i,i)
        max_k=max(max_k,k)
        max_ell=max(max_ell,ell)
        max_p=max(max_p,p)
    assert not cert
    assert count==data["candidate_count"]
    assert val_count==data["valuation_certificates"]
    assert [max_i,max_k,max_ell,max_p]==[data[x] for x in
            ["largest_i","largest_k","largest_ell","largest_obstruction_prime"]]
    report={"verified":True,
            "uniform_statement":"No upper-branch solution with j=i-2 and min(ell,k-ell)>=3",
            "analytic_i_strict_bound":I_STRICT,
            "candidate_count":count,"valuation_certificates":val_count,
            "largest_i":max_i,"largest_k":max_k,"largest_ell":max_ell,
            "largest_obstruction_prime":max_p,"unresolved":0,
            "certificate_sha256":hashlib.sha256(raw).hexdigest(),
            "elapsed_seconds":round(time.monotonic()-start,3),
            "formal_proof_assistant_executed":False,
            "prerequisites":"Symmetric shared-prime-part analytic i bound; prior upper ordering/endpoint/gap reductions."}
    report_path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("action",choices=["generate","verify"])
    parser.add_argument("--certificate",type=Path,default=Path("v4_upper_first_complement_two_ege3_certificates.json"))
    parser.add_argument("--report",type=Path,default=Path("v4_upper_first_complement_two_ege3_verification.json"))
    args=parser.parse_args()
    if args.action=="generate":generate(args.certificate)
    else:verify(args.certificate,args.report)
