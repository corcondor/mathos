#!/usr/bin/env python3
"""Complete, exact L1 exclusion in the unbounded parameter band 3j<=b<=4j.

The written proof shows j<1536 and 4<=i-j<=11 before these certificates
are generated. Generator and verifier enumerate the finite set differently.
"""
import argparse
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import time

from v4_lower_l1_single_top import lucas_fast, lucas_check, nth_root_floor, PRIMES


def generate(path):
    start = time.monotonic()
    records = []
    unresolved = []
    pairs = 0
    max_offset = 0
    for j in range(6,1536):
        i = j+4
        while comb(i,j) < (4*j)**3:
            a = comb(i,j)
            lower = max(22,3*j,nth_root_floor(a,3)+1)
            upper = min(4*j,nth_root_floor(4*a-1,3))
            if lower <= upper:
                pairs += 1
                max_offset = max(max_offset,i-j)
            for b in range(lower,upper+1):
                for p in PRIMES:
                    left = lucas_fast(a,b,p)
                    right = (lucas_fast(i*i,j*j,p)
                             + lucas_fast(b*b,2*b-1,p)) % p
                    if left != right:
                        records.append([j,i,b,p])
                        break
                else:
                    unresolved.append([j,i,b])
            i += 1
        if j % 200 == 0:
            print(json.dumps({"progress_j":j,"excluded":len(records),
                              "unresolved":len(unresolved),
                              "elapsed_seconds":round(time.monotonic()-start,3)}),flush=True)
    data={"equation":"C(C(i,j),b)=C(i^2,j^2)+C(b^2,2b-1)",
          "scope":"L1, 3j<=b<=4j; all original upper indices included",
          "proved_reductions":{"j_min":6,"j_max":1535,
                               "offset_min":4,"offset_max":11,
                               "b_min":22,"height":"b^3/4<C(i,j)<b^3"},
          "candidate_count":len(records)+len(unresolved),
          "ij_pairs":pairs,"max_offset_observed":max_offset,
          "unresolved":unresolved,"records":records}
    path.write_text(json.dumps(data,separators=(",",":"))+"\n")
    print(json.dumps({"certificate":str(path),"excluded":len(records),
                      "ij_pairs":pairs,"max_offset":max_offset,
                      "unresolved":unresolved,
                      "elapsed_seconds":round(time.monotonic()-start,3)}),flush=True)


def verify(path,report_path):
    start=time.monotonic()
    raw=path.read_bytes()
    data=json.loads(raw)
    assert not data["unresolved"]
    assert comb(18,12)>64*6**3
    cert={(j,i,b):p for j,i,b,p in data["records"]}
    assert len(cert)==len(data["records"]),"Repeated candidates"
    count=0
    pairs=set()
    max_p=0
    # Independent enumeration: b first, then its admissible j interval.
    # The proved offset bound 4<=d<=11 permits a short binary search in i.
    for b in range(22,4*1535+1):
        for j in range(max(6,(b+3)//4),min(1535,b//3)+1):
            lo,hi=j+4,j+12
            while lo<hi:
                mid=(lo+hi)//2
                if 4*comb(mid,j)<=b**3:
                    lo=mid+1
                else:
                    hi=mid
            for i in range(lo,j+12):
                a=comb(i,j)
                if a>=b**3:
                    break
                assert b**3<4*a and 3*j<=b<=4*j
                assert a>=2*b
                p=cert.pop((j,i,b))
                assert p>=2 and all(p%q for q in range(2,isqrt(p)+1))
                left=lucas_check(a,b,p)
                right=(lucas_check(i*i,j*j,p)
                       +lucas_check(b*b,2*b-1,p))%p
                assert left!=right,(j,i,b,p)
                count+=1
                pairs.add((j,i))
                max_p=max(max_p,p)
    assert not cert,"Extra or unexamined candidate in certificate"
    assert count==data["candidate_count"]
    assert len(pairs)==data["ij_pairs"]
    report={"verified":True,
            "uniform_statement":"No solution in L1 with 3j<=b<=4j",
            "proved_finite_j_range":[6,1535],
            "candidate_count":count,"ij_pairs":len(pairs),
            "max_obstruction_prime":max_p,"unresolved":0,
            "certificate_sha256":hashlib.sha256(raw).hexdigest(),
            "elapsed_seconds":round(time.monotonic()-start,3),
            "formal_proof_assistant_executed":False,
            "prerequisites":"Previously proved L1 structure, b>=22, i-j>=4, b^3/4<A<b^3; written band-height proof."}
    report_path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("action",choices=["generate","verify"])
    parser.add_argument("--certificate",type=Path,default=Path("v4_lower_l1_band_certificates.json"))
    parser.add_argument("--report",type=Path,default=Path("v4_lower_l1_band_verification.json"))
    args=parser.parse_args()
    if args.action=="generate":generate(args.certificate)
    else:verify(args.certificate,args.report)
