#!/usr/bin/env python3
"""Exact lower-branch certificates for j=i-2, ell>=2, all indices.

The proof bounds i<2^21. For i>=1024, X<L<2X restricts B to the
certified fixed-A windows. Window endpoints are independently verified
by v4_upper_complement_two_l1_verify.cpp; that check is a separate
required step. No floating point is used here.
"""
import argparse
import bisect
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import struct
import time

from v4_lower_l1_single_top import lucas_fast, FACT

LIMIT = 2**21
B_LIMIT = 5*(LIMIT-3)-1
WINDOW_FILE = Path('v4_upper_complement_two_l1_extended.bin')
CERT_FILE = Path('v4_first_complement_two_lower_certificates.json')
REPORT_FILE = Path('v4_first_complement_two_lower_verification.json')


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2,isqrt(n)+1))


PRIMES = [p for p in range(2,1000) if is_prime(p)]
for _p in PRIMES:
    if _p not in FACT:
        _fac=[1]*_p
        for _n in range(1,_p):
            _fac[_n]=_fac[_n-1]*_n%_p
        FACT[_p]=_fac


def generator_representations():
    """Enumerate effective lower index first, then grow the top."""
    result = {}
    e = 2
    while comb(2*e,e) <= B_LIMIT:
        k = 2*e
        value = comb(k,e)
        while value <= B_LIMIT:
            for ell in sorted({e,k-e}):
                result.setdefault(value,[]).append((k,ell))
            value = value*(k+1)//(k+1-e)
            k += 1
        e += 1
    return result


def verifier_representations():
    """Independent top-first enumeration, using direct combinations."""
    result = {}
    k_max = (1+isqrt(1+8*B_LIMIT))//2
    for k in range(4,k_max+1):
        for e in range(2,k//2+1):
            value = comb(k,e)
            if value > B_LIMIT:
                break
            for ell in ([e] if 2*e == k else [e,k-e]):
                result.setdefault(value,set()).add((k,ell))
    return result


def windows(path, verify_bounds=False):
    raw = path.read_bytes()
    assert raw[:8] == b'V4JC2L1\0'
    first,last,small = struct.unpack_from('<III',raw,8)
    assert (first,last,small) == (23,LIMIT,1024)
    position = 20
    for i in range(first,last):
        lo,hi = struct.unpack_from('<II',raw,position)
        position += 8
        if verify_bounds:
            j=i-2
            A=i*(i-1)//2
            lower=max(i,(j+isqrt(5*j*j))//2+1)
            upper=min(A//2,(5 if i>=802 else 10)*j-1)
            assert lower-1 <= lo < hi <= upper+1
            if i < small:
                assert (lo,hi) == (lower-1,upper+1)
        position += 2*(hi-lo-1)
        assert position <= len(raw)
        yield i,lo,hi
    assert position == len(raw)


def valuation_floors(n,m,p):
    value=0
    a,b,c=n,m,n-m
    while a:
        a//=p
        b//=p
        c//=p
        value += a-b-c
    return value


def valuation_carries(n,m,p):
    a,b=m,n-m
    carry=count=0
    while a or b or carry:
        ad,bd=a%p,b%p
        a//=p
        b//=p
        carry=int(ad+bd+carry>=p)
        count+=carry
    return count


def lucas_check(n,m,p):
    if m<0 or m>n:
        return 0
    value=1
    while m:
        nd,md=n%p,m%p
        if md>nd:
            return 0
        value=value*comb(nd,md)%p
        n//=p
        m//=p
    return value


def candidate_terms(i,k,ell,B):
    A=i*(i-1)//2
    return [(A,B),(i*i,4*i-4),(k*k,ell*ell)]


def witness(i,k,ell,B):
    terms=candidate_terms(i,k,ell,B)
    for p in PRIMES:
        if p>101:
            break
        a,b,c=[lucas_fast(n,m,p) for n,m in terms]
        if a!=(b+c)%p:
            return p,0
    for p in PRIMES:
        if p>101:
            break
        vals=[valuation_floors(n,m,p) for n,m in terms]
        if vals.count(min(vals))==1:
            return p,1
    for p in PRIMES:
        if p<=101:
            continue
        a,b,c=[lucas_fast(n,m,p) for n,m in terms]
        if a!=(b+c)%p:
            return p,0
    return None


def generate():
    started=time.monotonic()
    reps=generator_representations()
    keys=sorted(reps)
    rows=[]
    unresolved=[]
    valuation_count=0
    covered=0
    for i,lo,hi in windows(WINDOW_FILE):
        covered+=1
        for B in keys[bisect.bisect_right(keys,lo):bisect.bisect_left(keys,hi)]:
            for k,ell in reps[B]:
                if not (2<=ell<i-2):
                    continue
                found=witness(i,k,ell,B)
                if found is None:
                    unresolved.append([i,k,ell])
                else:
                    p,mode=found
                    rows.append([i,k,ell,p,mode])
                    valuation_count+=mode
    data={
        'equation':'C(C(i,i-2),C(k,ell))=C(i^2,(i-2)^2)+C(k^2,ell^2)',
        'scope':'lower branch, j=i-2, ell>=2, all valid original indices',
        'analytic_i_exclusive_bound':LIMIT,
        'window_file':str(WINDOW_FILE),
        'window_sha256':hashlib.sha256(WINDOW_FILE.read_bytes()).hexdigest(),
        'endpoint_verification_required':'v4_upper_complement_two_l1_verify.cpp on the extended file',
        'first_indices_covered':covered,
        'inner_representation_count':sum(map(len,reps.values())),
        'distinct_inner_binomial_values':len(reps),
        'record_format':['i','k','ell','prime','mode_0_residue_1_valuation'],
        'candidate_count':len(rows)+len(unresolved),
        'valuation_certificates':valuation_count,
        'unresolved':unresolved,
        'records':rows
    }
    CERT_FILE.write_text(json.dumps(data,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))
    print(json.dumps({'seconds':time.monotonic()-started}))
    assert not unresolved


def verify():
    started=time.monotonic()
    raw=CERT_FILE.read_bytes()
    data=json.loads(raw)
    assert data['analytic_i_exclusive_bound']==LIMIT
    assert data['window_sha256']==hashlib.sha256(WINDOW_FILE.read_bytes()).hexdigest()
    assert not data['unresolved']
    certs={}
    for i,k,ell,p,mode in data['records']:
        key=i,k,ell
        assert key not in certs
        assert is_prime(p) and mode in (0,1)
        certs[key]=p,mode
    assert len(certs)==data['candidate_count']
    reps=verifier_representations()
    assert len(reps)==data['distinct_inner_binomial_values']
    assert sum(map(len,reps.values()))==data['inner_representation_count']
    count=valuation_count=covered=0
    max_i=max_k=max_ell=max_p=0
    mode_one_examples=[]
    for i,lo,hi in windows(WINDOW_FILE,verify_bounds=True):
        covered+=1
        # Directly examine each intervening integer, rather than the
        # generator's binary searches in the list of representable values.
        for B in range(lo+1,hi):
            for k,ell in reps.get(B,()):
                if not (2<=ell<i-2):
                    continue
                assert B==comb(k,ell)
                p,mode=certs.pop((i,k,ell))
                terms=candidate_terms(i,k,ell,B)
                if mode==0:
                    a,b,c=[lucas_check(n,m,p) for n,m in terms]
                    assert a!=(b+c)%p
                else:
                    vals=[valuation_carries(n,m,p) for n,m in terms]
                    assert vals.count(min(vals))==1
                    valuation_count+=1
                    if len(mode_one_examples)<3:
                        mode_one_examples.append({'i':i,'j':i-2,'k':k,'ell':ell,'p':p,'valuations_L_X_Y':vals})
                count+=1
                max_i=max(max_i,i)
                max_k=max(max_k,k)
                max_ell=max(max_ell,ell)
                max_p=max(max_p,p)
    assert not certs
    assert count==data['candidate_count']
    assert covered==data['first_indices_covered']==LIMIT-23
    assert valuation_count==data['valuation_certificates']
    report={'status':'pass','verified_candidates':count,
            'first_indices_covered':covered,
            'analytic_i_exclusive_bound':LIMIT,
            'valuation_certificates':valuation_count,
            'valuation_examples':mode_one_examples,
            'max_i':max_i,'max_k':max_k,'max_ell':max_ell,'max_prime':max_p,
            'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'window_sha256':data['window_sha256'],
            'coverage':'independent top-first binomial representations and direct intervening-integer enumeration',
            'residue_check':'direct small combinations in Lucas theorem',
            'valuation_check':'Kummer carries, independent of generator Legendre floors',
            'endpoint_check':'separate required C++ verifier on exact same extended binary',
            'formalized_in_Lean':False,
            'seconds':time.monotonic()-started}
    REPORT_FILE.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('command',choices=['generate','verify'])
    args=parser.parse_args()
    if args.command=='generate':
        generate()
    else:
        verify()
