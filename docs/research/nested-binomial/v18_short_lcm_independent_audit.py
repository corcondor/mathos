#!/usr/bin/env python3
"""Independent complete 830-point exception audit for v18_short_lcm.md."""
from pathlib import Path
import argparse, hashlib, json
from math import gcd

def floor_root(n):
    lo,hi=0,1
    while hi*hi<=n:hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid*mid<=n:lo=mid
        else:hi=mid
    return lo
def primes_sieve(n):
    flags=[True]*n;flags[0]=flags[1]=False
    for p in range(2,n):
        if flags[p]:
            for x in range(2*p,n,p):flags[x]=False
    return [p for p in range(2,n) if flags[p]]
def factor_all(n):
    out=[]
    for p in primes_sieve(floor_root(n)+2):
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append([p,e])
    if n>1:out.append([n,1])
    return out

def main():
    here=Path(__file__).resolve().parent
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,default=here/'v18_short_lcm_checks.json')
    ap.add_argument('--note',type=Path,default=here/'v18_short_lcm.md')
    ap.add_argument('--output',type=Path,default=here/'v18_short_lcm_independent_audit.json')
    args=ap.parse_args()
    producer=json.loads(args.input.read_text())
    domain=producer['complete_exception_domain']
    cs=[c for c in range(2,16) if floor_root(c)**2!=c]
    assert cs==[2,3,5,6,7,8,10,11,12,13,14,15]
    primes=[p for p in primes_sieve(75) if p>=11]
    assert primes==domain['primes']
    constants=[]
    for c in cs:
        for t in range(c+1):
            D=(t+9)**2-36*c
            assert D and -459<=D<=49
            for p in primes_sieve(22):
                if p>=11:assert D%(p*p)
            constants.append({'c':c,'t':t,'D':D})
    assert constants==[{k:x[k] for k in ['c','t','D']} for x in producer['endpoint_constants']]
    triples=[];squares=[]
    # Iterate c first; compare complete sets, not the producer's traversal order.
    for c in cs:
        for w in range(1,9):
            for p in primes:
                if 9*w>=p:continue
                v=p**3*w+c;a=floor_root(v)
                assert a*a<=v<(a+1)**2
                triples.append([p,w,c,v,a])
                if a*a==v:squares.append([p,w,c,a])
    assert sorted(triples)==sorted(domain['cubic_square_records'])
    assert sorted(squares)==sorted(domain['cubic_squares'])
    seventh=[]
    for p,c in [(11,12),(13,14)]:
        v=p**7+c;a=floor_root(v);assert a*a<v<(a+1)**2
        seventh.append([p,1,c,v,a])
    assert seventh==domain['seventh_square_records']
    exclusions=[]
    for p,w,c,n in sorted(squares):
        if n<104:continue
        M=gcd(n,3)*gcd(n-1,6);Q=n*(n-1)//M
        fs=factor_all(Q);forced=1
        for p,e in fs:forced*=p**((e+2)//3)
        assert forced**3%Q==0 and 3*forced>10*n
        exclusions.append({'n':n,'M':M,'Q':Q,'factorization':fs,
        'least_cube_divisor':forced,'strict_interval_margin':3*forced-10*n})
    assert exclusions==domain['forced_divisor_exclusions']
    assert len(triples)==828 and len(seventh)==2 and len(squares)==3
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    report={'status':'PASS','producer_imported_or_executed':False,
    'prime_method':'Eratosthenes sieve through 74',
    'square_method':'integer binary search with consecutive-square inequalities',
    'factor_method':'sieve of divisors through square root, independent reconstruction',
    'complete_endpoint_constants':len(constants),'complete_cubic_candidates':len(triples),
    'complete_seventh_candidates':len(seventh),'all_candidate_records_match':True,
    'square_candidates':sorted(squares),'forced_divisor_exclusions':exclusions,
    'all_remaining_survivors':[],
    'written_proof_review':[
    'Endpoint-square obstruction is proved uniformly modulo 4 and 9.',
    'Inner carry levels 2,...,e each contribute one; no condition p^e>m is assumed.',
    'Pplus(Nc)<r is inherited, so floor(log_p r)>=1 in the shorter excess theorem.',
    'The p|Q overlap is exactly (11,12) or (13,14) with valuation one.',
    'Parity formulas for J leave only J=1, or J=3 in the two overlap cases.',
    'Square-LCM and odd-cofactor conclusions are restricted to k=r.',
    'The simultaneous excess and v_p(B)>=v_p(Nc)-1 conclusions cover both branches.',
    'The positive-neighbor theorem is not upgraded from L_m to L_r.'],
    'source_sha256':sha(__file__),'producer_report_sha256':sha(args.input),
    'proof_note_sha256':sha(args.note),'new_lean_execution':False,
    'external_peer_review':False,'verification_boundary':
    'Written coverage proof reviewed internally; complete finite candidates independently reconstructed. No whole-problem solution claimed.'}
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','complete_candidate_records':len(triples)+len(seventh),
    'squares':len(squares),'survivors':0}))
if __name__=='__main__':main()

