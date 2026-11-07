#!/usr/bin/env python3
"""Standard-library verifier for complete fixed-parameter reconstruction.

No SymPy or producer import. Checks every prime factor by recursive Lucas
order certificates, all divisor domains and coefficient families, and exact
quadratic/positive-sign quartic root certificates.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from math import gcd,isqrt
from pathlib import Path
import time


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def factor_product(factors,certified):
    product=1;seen=set()
    for p,e in factors:
        assert p in certified and e>=1 and p not in seen
        seen.add(p);product*=p**e
    return product


def check_primes(rows):
    proved=set()
    for row in sorted(rows,key=lambda x:x['p']):
        p=row['p'];assert p not in proved
        if row.get('base'):
            assert p==2
        else:
            fac=row['p_minus_one'];a=row['a']
            assert p>2 and factor_product(fac,proved)==p-1
            assert 1<a<p and pow(a,p-1,p)==1
            for q,e in fac:assert gcd(pow(a,(p-1)//q,p)-1,p)==1
        proved.add(p)
    return proved


def all_divisors(factors):
    def recurse(i,value):
        if i==len(factors):
            yield value;return
        p,e=factors[i]
        for _ in range(e+1):
            yield from recurse(i+1,value)
            value*=p
    return sorted(recurse(0,1))


def eval_L(n,c,h,J,G):return (h-9*c)*n*n-(h+6*c)*n-c*(J*G+9)


def sign(n,c,h,J,G):
    L=eval_L(n,c,h,J,G)
    if L<=0:return -1
    norm=L*L-4*c*h*n*(n-1)
    return (norm>0)-(norm<0)


def validate_isolation(record,c,h,J,G,branch):
    a,b=h-9*c,h+6*c
    assert a>0 and c>0 and J>0 and G>0
    if branch=='small':
        assert record['kind']=='quadratic'
        D=b*b+4*a*c*(J*G+10);s=record['floor_sqrt_discriminant']
        assert s*s<=D<(s+1)*(s+1)
        n=None
        if s*s==D and (b+s)%(2*a)==0:
            positive=(b+s)//(2*a)
            if positive>=104:n=positive
    else:
        if record['kind']=='domain_start':
            value=sign(104,c,h,J,G);assert value>=0
            n=104 if value==0 else None
        else:
            assert record['kind']=='adjacent_bracket'
            low,high=record['lower'],record['upper']
            assert low>=104 and high==low+1
            assert sign(low,c,h,J,G)<0
            value=sign(high,c,h,J,G);assert value>=0
            n=high if value==0 else None
        if n is not None:
            L=eval_L(n,c,h,J,G)
            assert L>0 and L*L==4*c*h*n*(n-1)
    assert n==record['root']
    return n


def binomial_mod(N,R,p):
    facts=[1]
    for t in range(1,p):facts.append(facts[-1]*t%p)
    value=1
    while N or R:
        a,b=N%p,R%p
        if b>a:return 0
        value=value*facts[a]*pow(facts[b]*facts[a-b]%p,-1,p)%p
        N//=p;R//=p
    return value


def validate_rejection(n,c,h,J,G,M,delta,branch,result):
    reason=result['reason']
    if branch=='small':
        top=h*n*(n-1)
        if top%c:
            assert reason=='nonintegral_r_squared';return
        square=top//c;r=isqrt(square)
        if r*r!=square:
            assert reason=='nonsquare_r_squared' and result['floor_sqrt']==r;return
    else:
        L=eval_L(n,c,h,J,G)
        if L%(2*c):
            assert reason=='nonintegral_r';return
        r=L//(2*c)
    assert r==result['r'] and c*r*r==h*n*(n-1)
    if reason=='wrong_M':
        assert gcd(n,3)*gcd(n-1,6)!=M;return
    assert gcd(n,3)*gcd(n-1,6)==M
    Q=n*(n-1)//M
    if reason=='wrong_delta':
        assert Q//gcd(Q,r*r)!=delta;return
    assert Q//gcd(Q,r*r)==delta
    eps=int(branch=='complement');N=n*n+2;T=(r-eps)**2-9*n*n-6*n-10
    assert T==J*G
    if reason=='wrong_canonical_G':
        assert gcd(N,T)!=G;return
    assert gcd(N,T)==G and N%G==0;w=N//G;assert w==result['w']
    if reason=='w_below_65':assert w<65;return
    assert w>=65
    if reason=='coarse_interval':assert not(3*n<r and 3*r<10*n);return
    assert 3*n<r and 3*r<10*n
    if reason=='cube_divisibility':assert r**3%Q!=0;return
    assert r**3%Q==0
    if reason=='square_root_gap':assert (r-3*n)**2<=9*n;return
    assert (r-3*n)**2>9*n
    if reason=='undecided_after_moduli':return
    assert reason=='original_binomial_modulus'
    witness=result['witness'];p=witness['p']
    assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
    A=n*(n-1)*(n-2)//6;k=r if branch=='small' else A-r
    left=binomial_mod(A,r,p);inner=binomial_mod(n*n,6*n-9,p)
    assert witness=={'p':p,'lhs':left,'inner':inner,'k_squared':k*k%p,'rhs':(inner+k*k)%p}
    assert left!=(inner+k*k)%p


def verify(certificate,output,note):
    start=time.perf_counter();doc=json.loads(gzip.decompress(certificate.read_bytes()))
    assert sha(note)==doc['elimination_note_sha256']
    primes=check_primes(doc['prime_certificates'])
    supplied={(f['delta'],f['J'],f['branch'],f['M'],f['K']):f for f in doc['families']}
    assert len(supplied)==len(doc['families'])
    visited=set();totals=Counter();root_records=[];undecided=[];types=Counter()
    for query in doc['queries']:
        delta,J,branch=query['delta'],query['J'],query['branch']
        assert delta>=1 and J>=1 and branch in ('small','complement')
        for M in (1,2,3,6):
            C=M*delta
            for K in range(9*C+1,12*C):
                if gcd(K,delta)!=1 or 927*K>=10400*C:continue
                key=delta,J,branch,M,K;visited.add(key);row=supplied[key]
                d=gcd(C,K);c,h=C//d,K//d
                assert c==row['c'] and h==row['h']
                if branch=='small':E=6*h*h-8*c*h+136*c*c
                else:E=36*h**4-48*c*h**3+1212*c*c*h*h-5256*c**3*h+23409*c**4
                assert E==row['E']>0 and factor_product(row['E_factorization'],primes)==E
                divs=all_divisors(row['E_factorization'])
                assert [p['G'] for p in row['divisors']]==divs
                totals['coefficient_families']+=1
                for record in row['divisors']:
                    G=record['G'];types[record['kind']]+=1
                    totals['divisor_polynomials']+=1
                    n=validate_isolation(record,c,h,J,G,branch)
                    if n is not None:
                        totals['integer_n_roots']+=1
                        result=record['root_check'];validate_rejection(n,c,h,J,G,M,delta,branch,result)
                        totals[result['reason']]+=1
                        rec={'delta':delta,'J':J,'branch':branch,'M':M,'K':K,
                             'c':c,'h':h,'G':G,'n':n,**result}
                        root_records.append(rec)
                        if result['reason']=='undecided_after_moduli':undecided.append(rec)
    assert visited==set(supplied)
    assert dict(totals)==doc['counts']
    assert root_records==doc['integer_root_records'] and undecided==doc['undecided']
    expected='COMPLETE_FINITE_RECONSTRUCTION' if undecided else 'PASS_COMPLETE_EXCLUSION_FOR_QUERIES'
    assert doc['status']==expected
    result={'status':'PASS','queries':doc['queries'],'counts':dict(totals),'root_certificate_types':dict(types),
            'primes_proved_by_recursive_Lucas_certificates':len(primes),
            'all_coefficient_families_and_G_divisors_complete':True,
            'all_root_isolation_certificates_checked':True,
            'undecided_count':len(undecided),'imports_producer_or_SymPy':False,
            'certificate_sha256':sha(certificate),'verifier_sha256':sha(Path(__file__)),
            'input_note_sha256':sha(note),'wall_seconds':round(time.perf_counter()-start,6),
            'scope':'Exact finite parameter queries only; general completeness uses the v19 integer eliminant and new monotonicity proof'}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('v20_fixed_parameter_certificate.json.gz'))
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('v20_fixed_parameter_verification.json'))
    parser.add_argument('--elimination-note',type=Path,default=Path(__file__).with_name('v19_canonical_defect_elimination.md'))
    args=parser.parse_args()
    verify(args.certificate,args.output,args.elimination_note)
