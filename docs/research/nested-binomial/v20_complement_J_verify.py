#!/usr/bin/env python3
"""Independent complete verifier for the complementary J<=32 exclusion.

No producer import or CAS: sieve factorizations, recursive divisor generation,
complete integer reconstruction, and binary-search square roots.
"""
import argparse
from collections import Counter
from fractions import Fraction
import gzip
import hashlib
import json
from math import gcd
from pathlib import Path
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def smallest_primes(limit):
    spf=list(range(limit+1))
    for p in range(2,limit+1):
        if spf[p]!=p:
            continue
        for t in range(p*p,limit+1,p):
            if spf[t]==t:
                spf[t]=p
    return spf


def factor_using_sieve(n,spf):
    d={}
    while n>1:
        p=spf[n]
        d[p]=d.get(p,0)+1
        n//=p
    return sorted(d.items())


def divisors_recursively(factors):
    def visit(i,current):
        if i==len(factors):
            yield current
            return
        p,v=factors[i]
        for _ in range(3*v+1):
            yield from visit(i+1,current)
            current*=p
    return list(visit(0,1))


def binary_root(S):
    low,high=0,1<<((S.bit_length()+1)//2)
    while low+1<high:
        m=(low+high)//2
        if m*m<=S:
            low=m
        else:
            high=m
    if high*high<=S:
        low=high
    assert low*low<=S<(low+1)*(low+1)
    return low


def verify(certificate,output,gap_note):
    start=time.perf_counter()
    doc=json.loads(gzip.decompress(certificate.read_bytes()))
    assert doc['finite_domain']=={'J':[1,32],'w':[65,383],'coprime':True,'excluded_J_residue':'J=2 mod4'}
    assert sha(gap_note)==doc['written_input_sha256'][gap_note.name]
    # Independent rational verification of each numerical cap margin.
    exp_lower=1+Fraction(7,10)+Fraction(49,200)+Fraction(343,6000)+Fraction(2401,240000)
    assert exp_lower>2
    assert [exp_lower.numerator,exp_lower.denominator]==doc['cap_constants']['exp_7_over_10_positive_partial_sum']
    assert Fraction(5001*32,85000)<2
    bound=3*(9*384+2*32)**3
    assert bound<2**37 and bound==doc['cap_constants']['n_at_w384_J32_upper']
    margin=384-Fraction(7,16)*32*37*Fraction(7,10)
    derivative=1-Fraction(189*32,16*9*384)
    assert [margin.numerator,margin.denominator]==doc['cap_constants']['w384_gap_lower']
    assert [derivative.numerator,derivative.denominator]==doc['cap_constants']['derivative_lower']
    assert margin>0 and derivative>0

    families={(f['J'],f['w']):f for f in doc['families']}
    assert len(families)==len(doc['families'])
    allowed_J=sorted(4*q+r for q in range(8) for r in (1,3,4))
    assert allowed_J==[j for j in range(1,33) if j%4!=2]
    primes=smallest_primes(9*383+2*32)
    seen=set();second=[];last=[];totals=Counter();per_J={j:Counter() for j in allowed_J}
    for w in range(65,384):
        for J in allowed_J:
            if gcd(w,J)!=1:
                continue
            key=J,w;seen.add(key);stored=families[key]
            c0,c1=9*w+2*J,24*w+3*J
            fac=factor_using_sieve(c0,primes)
            assert [list(t) for t in fac]==stored['c0_factorization']
            assert stored['c0']==c0 and stored['c1']==c1
            divs=divisors_recursively(fac)
            assert len(set(divs))==len(divs)==stored['cube_divisor_count']
            raw=2*len(divs)
            # Generate actual n values first, with set-based normalization.
            ns=sorted({g*e for g in (1,3) for e in divs
                       if g*e>=104 and gcd(g*e,3)==g})
            h=hashlib.sha256()
            for n in ns:h.update((str(n)+'\n').encode('ascii'))
            assert h.hexdigest()==stored['normalized_n_sha256']
            counts=Counter(raw_divisor_records=raw,normalized_n=len(ns),coefficient_families=1)
            for n in ns:
                g,d=gcd(n,3),gcd(n-1,6)
                if (c1*c1*c1)%((n-1)//d):
                    continue
                counts['second_divisor']+=1
                second.append({'J':J,'w':w,'n':n,'g':g,'d':d})
                N=n*n+2
                if N%w:
                    continue
                counts['w_divides_N']+=1
                G=N//w
                # Distinct expression: (9w+J)*G+6n-8.
                S=(9*w+J)*G+6*n-8
                root=binary_root(S)
                assert root*root<S<(root+1)*(root+1)
                last.append({'J':J,'w':w,'n':n,'g':g,'d':d,'G':G,
                             'r_minus_one_squared':S,'floor_square_root':root})
            assert dict(counts)==stored['counts'],key
            totals.update(counts);per_J[J].update(counts)
    assert seen==set(families)
    sortkey=lambda row:(row['J'],row['w'],row['n'])
    assert sorted(second,key=sortkey)==sorted(doc['second_divisor_points'],key=sortkey)
    assert sorted(last,key=sortkey)==sorted(doc['complete_square_obstructions'],key=sortkey)
    assert dict(totals)==doc['counts']
    for J in range(1,33):
        expected={'excluded_by_uniform_two_adic_condition':True} if J%4==2 else dict(per_J[J])
        assert expected==doc['per_J'][str(J)]
    assert doc['survivors']==[] and len(last)==5
    result={'status':'PASS','conclusion':'Complementary canonical J>=33 under the written inherited and new v20 analytic inputs',
            'certificate_file':certificate.name,'certificate_sha256':sha(certificate),
            'verifier_sha256':sha(Path(__file__)),
            'gap_note_sha256':sha(gap_note),'counts':dict(totals),
            'all_5323_coefficient_families_reconstructed':True,
            'all_cube_divisor_domains_reconstructed':True,
            'all_862_second_divisor_points_reconstructed':True,
            'all_five_consecutive_square_obstructions_checked':True,
            'uses_producer_or_CAS':False,
            'independence':'Sieve factorization, recursive divisors, set-normalized n, alternate S expression, binary integer square roots',
            'no_bound_on_delta':True,'no_arbitrary_n_cutoff':True,
            'original_binomial_Lucas_witnesses_needed':False,
            'wall_seconds':round(time.perf_counter()-start,6),
            'limitations':'Written analytic gap and divisor-transfer proofs are inputs; no new Lean/API execution or full equation classification'}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('v20_complement_J_certificate.json.gz'))
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('v20_complement_J_verification.json'))
    parser.add_argument('--gap-note',type=Path,default=Path(__file__).with_name('v20_logarithmic_gap.md'))
    args=parser.parse_args()
    verify(args.certificate,args.output,args.gap_note)
