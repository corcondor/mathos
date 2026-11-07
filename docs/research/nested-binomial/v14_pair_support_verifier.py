#!/usr/bin/env python3
"""Audit the finite union for two smooth cube cores among n,n-1,n-2.

Inputs are complete PARI Thue result files, not bounded searches. This
script audits their algebraic coverage and rejects the resulting finite
branch candidates with exact integer arithmetic. It does not independently
establish completeness of PARI/GP's Thue algorithm.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from math import gcd, prod
from pathlib import Path


def require(condition,message):
    if not condition:
        raise ValueError(message)


def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factor(n):
    require(n > 0,'factorization requires positive input')
    value=n
    output=[]
    p=2
    while p*p <= value:
        e=0
        while value % p == 0:
            value//=p
            e+=1
        if e:
            output.append([p,e])
        p=3 if p==2 else p+2
    if value > 1:
        output.append([value,1])
    require(prod(p**e for p,e in output)==n,'factorization reconstruction')
    return output


def cube_core(n):
    return prod(p**(e%3) for p,e in factor(n))


def supported(n,S):
    return all(p in S or e%3==0 for p,e in factor(n))


def core_pairs(S):
    cores=[prod(p**e for p,e in zip(S,E))
           for E in itertools.product(range(3),repeat=len(S))]
    return {(a,b)for a in cores for b in cores if gcd(a,b)==1}


def check_input(path,kind):
    d=json.loads(path.read_text())
    require(d['status']=='PASS','input not PASS')
    S=[2,3,5,7] if kind=='adjacent' else [3,5,7]
    rhs=1 if kind=='adjacent' else 2
    require(d['support_primes']==S,'unexpected prime support')
    require(d['thueinit_flag']==1,'unconditional initialization required')
    if kind=='odd_gap':
        require(d['rhs']==2 and d['odd_bases_required'],'wrong gap/parity')
    rows=d['records']
    observed=[(r['A'],r['B'])for r in rows]
    expected=core_pairs(S)
    require(len(observed)==len(set(observed))==5**len(S),'coefficient pair count')
    require(set(observed)==expected,'complete coefficient pair coverage')
    values=set()
    signed_count=0
    for row in rows:
        a,b=row['A'],row['B']
        direct=sorted(map(tuple,row['all_integer_solutions']))
        monic=sorted(map(tuple,row['transformed_all_integer_solutions']
                            if kind=='adjacent' else row['monic_all_integer_solutions']))
        require(all(a*x**3-b*y**3==rhs for x,y in direct),'direct exact equation')
        require(all(u**3-a*a*b*y**3==rhs*a*a for u,y in monic),'monic exact equation')
        recovered=sorted((u//a,y)for u,y in monic if u%a==0)
        require(recovered==direct,'dual-encoding solution sets')
        positives=[(x,y)for x,y in direct if x>0 and y>0 and
                   (kind=='adjacent' or (x%2==1 and y%2==1))]
        candidates=sorted(a*x**3 for x,y in positives)
        require(candidates==row['positive_n' if kind=='adjacent' else 'selected_n'],
                'per-equation positive first indices')
        values.update(candidates)
        signed_count+=len(direct)
    require(sorted(values)==d['positive_n' if kind=='adjacent' else 'selected_n'],
            'global input first-index list')
    return values,{'file':path.name,'sha256':hash_file(path),
                   'support_primes':S,'rhs':rhs,'coefficient_pairs':len(rows),
                   'signed_solution_count':signed_count,'positive_n':sorted(values)}


def verify(adjacent,odd_gap,destination):
    N,adjacent_report=check_input(adjacent,'adjacent')
    G,gap_report=check_input(odd_gap,'odd_gap')
    families={
        'n_and_n_minus_1':N,
        'n_minus_1_and_n_minus_2':{m+1 for m in N},
        'even_n_and_n_minus_2':{2*m for m in N},
        'odd_n_and_n_minus_2':G,
    }
    raw_union=set().union(*families.values())
    legal=sorted(n for n in raw_union if n>=3)
    witnessed=[]
    for n in legal:
        locations=[name for name,values in families.items() if n in values]
        actual_support=[supported(n-j,{2,3,5,7})for j in range(3)]
        require(sum(actual_support)>=2,'candidate does not have two supported cores')
        witnessed.append({'n':n,'case_sources':locations,
                          'cube_cores':[cube_core(n-j)for j in range(3)],
                          'supported_core_flags':actual_support})
    remaining=[n for n in legal if n>=104]
    rejections=[]
    for n in remaining:
        A=n*(n-1)*(n-2)//6
        D=A//gcd(A,n-2)
        pf=factor(D)
        F=prod(p**((e+2)//3)for p,e in pf)
        first=F*(3*n//F+1)
        require(first>3*n and first-F<=3*n,'first forced multiple')
        upper=Fraction(10*n,3)
        loglower=None
        if n>=1024:
            L=0
            while 3**(L+1)<n:
                L+=1
            require(L>0 and 3**L<n,'logarithm lower bound certificate')
            sharper=Fraction(3*n)+Fraction(3*n,4*L)
            if sharper<upper:
                upper=sharper
                loglower=L
        require(first*upper.denominator>=upper.numerator,'candidate not excluded')
        rejections.append({'n':n,'binomial_n_3':A,'D':D,'D_factorization':pf,
                           'forced_divisor_F':F,'strict_lower_bound':3*n,
                           'first_forced_multiple_above_lower':first,
                           'strict_upper_bound':[upper.numerator,upper.denominator],
                           'logarithm_lower_bound_L':loglower,
                           'cleared_denominator_nonnegative_gap':
                           first*upper.denominator-upper.numerator,'excluded':True})
    report={
        'status':'PASS','support_primes':[2,3,5,7],
        'scope':'ell=1,j=i-3; given prior H|n-2,n>=104 and strict r bounds',
        'input_checks':[adjacent_report,gap_report],
        'families':{k:sorted(v)for k,v in families.items()},
        'raw_union':sorted(raw_union),'raw_union_count':len(raw_union),
        'valid_auxiliary_indices_n_ge_3':legal,'valid_auxiliary_index_count':len(legal),
        'indices_below_104_count':sum(n<104 for n in legal),
        'indices_n_ge_104':remaining,'rejections':rejections,
        'remaining_after_exact_interval_checks':0,
        'core_witnesses':witnessed,
        'conclusion':'At most one of n,n-1,n-2 has cube-free core supported on {2,3,5,7}. Thus at least two different factors have distinct primes>=11 with valuations not divisible by3.',
        'boundary':'No new Lean execution. Completeness of finite candidate sets depends on the recorded PARI complete solver results, not on checking listed solutions alone.',
        'source_sha256':hash_file(Path(__file__)),
    }
    destination.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ['rejections','core_witnesses']}))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--adjacent',type=Path,required=True)
    parser.add_argument('--odd-gap',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    verify(args.adjacent,args.odd_gap,args.output)
