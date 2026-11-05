#!/usr/bin/env python3
"""Exact certificates for the entire lower L1 band 8j/3<=b<=3j.

The analytic proof bounds j<=1023, 4<=i-j<=14, b³/4<A<b⁴.
Generation and verification enumerate this complete region differently.
"""
import argparse
import hashlib
import json
from math import comb,isqrt
from pathlib import Path
import time

from v4_lower_l1_single_top import lucas_fast,lucas_check,nth_root_floor,FACT
from v4_upper_complement_two_dge3 import choose_valuation_floor,choose_valuation_carries

J_MAX=1023
PRIMES=[p for p in range(2,1000) if all(p%d for d in range(2,isqrt(p)+1))]
for p in PRIMES:
    if p not in FACT:
        row=[1]*p
        for n in range(1,p):row[n]=row[n-1]*n%p
        FACT[p]=row


def generated_candidates():
    for j in range(8,J_MAX+1):
        for d in range(4,15):
            i=j+d
            A=comb(i,j)
            low=max(22,(8*j+2)//3,nth_root_floor(A,4)+1)
            high=min(3*j,nth_root_floor(4*A-1,3))
            for b in range(low,high+1):
                yield i,j,b,A


def verified_candidates():
    for b in range(22,3*J_MAX+1):
        first=max(8,(b+2)//3)
        last=min(J_MAX,3*b//8)
        for j in range(first,last+1):
            for i in range(j+4,j+15):
                A=comb(i,j)
                if b**3<4*A and A<b**4:
                    yield i,j,b,A


def terms(i,j,b,A):
    return [(A,b),(i*i,j*j),(b*b,2*b-1)]


def generate(path):
    started=time.monotonic()
    records=[]
    unresolved=[]
    valuation_count=0
    for i,j,b,A in generated_candidates():
        ts=terms(i,j,b,A)
        for p in PRIMES:
            if p>101:break
            left,x,y=[lucas_fast(n,r,p) for n,r in ts]
            if left!=(x+y)%p:
                records.append([i,j,b,p,0])
                break
        else:
            raise AssertionError('prime loop must break at p>101 or a witness')
        if records and records[-1][:3]==[i,j,b]:continue
        for p in PRIMES:
            if p>101:break
            vals=[choose_valuation_floor(n,r,p) for n,r in ts]
            if vals.count(min(vals))==1:
                records.append([i,j,b,p,1]);valuation_count+=1
                break
        if records and records[-1][:3]==[i,j,b]:continue
        for p in PRIMES:
            if p<=101:continue
            left,x,y=[lucas_fast(n,r,p) for n,r in ts]
            if left!=(x+y)%p:
                records.append([i,j,b,p,0]);break
        else:
            unresolved.append([i,j,b])
    data={'equation':'C(C(i,j),b)=C(i^2,j^2)+C(b^2,2b-1)',
          'scope':'L1, 8j/3<=b<=3j, all original indices',
          'proved_j_inclusive_bound':J_MAX,
          'proved_offset_range':[4,14],
          'record_format':['i','j','b','prime','mode_0_residue_1_valuation'],
          'candidate_count':len(records)+len(unresolved),
          'valuation_certificates':valuation_count,
          'unresolved':unresolved,'records':records}
    path.write_text(json.dumps(data,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2),flush=True)
    print(json.dumps({'seconds':time.monotonic()-started}),flush=True)
    assert not unresolved


def verify(path,output):
    started=time.monotonic()
    raw=path.read_bytes();data=json.loads(raw)
    assert data['proved_j_inclusive_bound']==J_MAX
    assert data['proved_offset_range']==[4,14]
    assert not data['unresolved']
    cert={}
    for i,j,b,p,mode in data['records']:
        key=i,j,b
        assert key not in cert
        assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
        assert mode in (0,1)
        cert[key]=(p,mode)
    assert len(cert)==data['candidate_count']
    count=val_count=0
    max_i=max_j=max_b=max_p=0
    examples=[]
    for i,j,b,A in verified_candidates():
        p,mode=cert.pop((i,j,b))
        ts=terms(i,j,b,A)
        if mode==0:
            left,x,y=[lucas_check(n,r,p) for n,r in ts]
            assert left!=(x+y)%p
        else:
            vals=[choose_valuation_carries(n,r,p) for n,r in ts]
            assert vals.count(min(vals))==1
            val_count+=1
            if len(examples)<3:
                examples.append({'indices':[i,j,b,b-1],'p':p,'valuations_L_X_Y':vals})
        count+=1
        max_i=max(max_i,i);max_j=max(max_j,j);max_b=max(max_b,b);max_p=max(max_p,p)
    assert not cert
    assert count==data['candidate_count'] and val_count==data['valuation_certificates']
    result={'status':'pass','uniform_statement':'No L1 solution with 8j/3<=b<=3j',
            'verified_candidates':count,'valuation_certificates':val_count,
            'valuation_examples':examples,'max_i':max_i,'max_j':max_j,'max_b':max_b,'max_prime':max_p,
            'unresolved':0,'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'independent_coverage':'b-first instead of j/offset-first; direct inequalities instead of root-derived intervals',
            'independent_residues':'direct small combinations in Lucas digits',
            'independent_valuations':'Kummer carries instead of Legendre floor sums',
            'formalized_in_Lean':False,'seconds':time.monotonic()-started}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['generate','verify'])
    parser.add_argument('--certificate',type=Path,default=Path('v5_l1_expanded_band_certificates.json'))
    parser.add_argument('--report',type=Path,default=Path('v5_l1_expanded_band_verification.json'))
    args=parser.parse_args()
    if args.action=='generate':generate(args.certificate)
    else:verify(args.certificate,args.report)
