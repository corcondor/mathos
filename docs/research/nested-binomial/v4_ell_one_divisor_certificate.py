"""Complete ell=1 exclusion for fixed j using i | j*r^3.

For j>=21, the written proofs give r<2j when i>=2j.  This turns the
unbounded first upper index into divisors of j*r^3.  The i<2j branch
uses the established offset-dependent gap bounds.  Both k=r and
k=binom(i,j)-r are included.

Generate and verify use distinct candidate enumeration and Lucas
implementations. The proof of the range reduction is in
v4_prime_power_reduction.md, with prerequisite gap bounds in
sharp_q_bounds.md. No floating point arithmetic is used.
"""
import argparse
import hashlib
import json
from functools import lru_cache
from math import comb, gcd, isqrt
from pathlib import Path


CERTIFICATE = Path('v4_ell_one_divisor_certificates.json')
REPORT = Path('v4_ell_one_divisor_verification.json')


@lru_cache(maxsize=None)
def factor_small(n):
    result = {}
    divisor = 2
    while divisor*divisor <= n:
        while n % divisor == 0:
            result[divisor] = result.get(divisor,0)+1
            n //= divisor
        divisor += 1
    if n > 1:
        result[n] = result.get(n,0)+1
    return result


def divisors_from_factors(factors):
    result = [1]
    for prime, exponent in sorted(factors.items()):
        result = [d*prime**power for d in result for power in range(exponent+1)]
    return result


def ordinary_divisors(n):
    low, high = [], []
    for d in range(1,isqrt(n)+1):
        if n % d == 0:
            low.append(d)
            if d*d != n:
                high.append(n//d)
    return low+high[::-1]


def independent_cube_divisors(r):
    # Factor r by gcd stripping, independently of factor_small.
    remaining = r
    factors = []
    candidate = 2
    while remaining > 1:
        if candidate*candidate > remaining:
            factors.append((remaining,3))
            break
        if remaining % candidate == 0:
            exponent = 0
            while remaining % candidate == 0:
                remaining //= candidate
                exponent += 3
            factors.append((candidate,exponent))
        candidate += 1
    result = [1]
    for prime, exponent in factors:
        old = result[:]
        multiplier = 1
        for power in range(1,exponent+1):
            multiplier *= prime
            result.extend(d*multiplier for d in old)
    return result


def gap_limit(i,j):
    # Strict upper bounds converted to inclusive integer bounds.
    if i >= 2*j:
        return 2*j-1
    offset = i-j
    if offset >= 5:
        return 3*j-1
    if offset == 4:
        return 4*j-1
    if offset == 3 or j >= 800:
        return 5*j-1
    assert offset == 2
    return 10*j-1


def generate_candidates(j):
    result = set()
    for r in range(j+2,2*j):
        factors = factor_small(j).copy()
        for prime, exponent in factor_small(r).items():
            factors[prime] = factors.get(prime,0)+3*exponent
        for i in divisors_from_factors(factors):
            if i >= 2*j:
                result.add((i,r))
    for i in range(j+2,2*j):
        q = i//gcd(i,j)
        divisor = 1
        for prime, exponent in factor_small(q).items():
            divisor *= prime**((exponent+2)//3)
        last = min(gap_limit(i,j),comb(i,j)//2)
        first = ((j+2+divisor-1)//divisor)*divisor
        result.update((i,r) for r in range(first,last+1,divisor))
    return sorted(result)


def independently_verify_candidates(j):
    result = set()
    gcd_values = ordinary_divisors(j)
    for r in range(j+2,2*j):
        for q in independent_cube_divisors(r):
            for g in gcd_values:
                i = g*q
                if i >= 2*j and gcd(i,j) == g:
                    result.add((i,r))
    # Deliberately use all r first, not multiples of a computed radical.
    for r in range(j+2,10*j):
        for i in range(j+2,2*j):
            if (j*r**3) % i != 0:
                continue
            offset = i-j
            strict = (3*j if offset>=5 else 4*j if offset==4
                      else 5*j if offset==3 or j>=800 else 10*j)
            if r >= strict or 2*r > comb(i,j):
                continue
            result.add((i,r))
    return result


def sieve_primes(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00'*(((limit-p*p)//p)+1)
    return [p for p in range(2,limit+1) if sieve[p]]


def factorial_tables(p):
    factorial = [1]*p
    for n in range(1,p):
        factorial[n] = factorial[n-1]*n % p
    inverse = [1]*p
    inverse[p-1] = pow(factorial[p-1],p-2,p)
    for n in range(p-1,0,-1):
        inverse[n-1] = inverse[n]*n % p
    return factorial,inverse


def lucas_table(n,k,p,table):
    factorial,inverse = table
    residue = 1
    while k:
        nd,kd = n%p,k%p
        if kd > nd:
            return 0
        residue = residue*factorial[nd]*inverse[kd]*inverse[nd-kd] % p
        n//=p
        k//=p
    return residue


def lucas_direct(n,k,p):
    if k < 0 or n < k:
        return 0
    result = 1
    while n or k:
        nd,kd = n%p,k%p
        if kd > nd:
            return 0
        result = result*comb(nd,kd) % p
        n//=p
        k//=p
    return result


def generate(j_min,j_max):
    assert 21 <= j_min <= j_max
    primes = sieve_primes(997)
    tables = {p:factorial_tables(p) for p in primes}
    groups = []
    total=branches=max_i=max_prime=0
    unresolved=[]
    for j in range(j_min,j_max+1):
        records=[]
        coefficient_cache={}
        for i,r in generate_candidates(j):
            A=coefficient_cache.setdefault(i,comb(i,j))
            assert 2*r <= A
            found=[0,0]
            for p in primes:
                difference=(lucas_table(A,r,p,tables[p])-
                            lucas_table(i*i,j*j,p,tables[p]))%p
                if found[0]==0 and difference != r*r%p:
                    found[0]=p
                if found[1]==0 and difference != ((A-r)%p)**2%p:
                    found[1]=p
                if all(found):
                    break
            if not all(found):
                unresolved.append([i,j,r,*found])
            records.append([i,r,*found])
            branches += 1 if A==2*r else 2
            max_i=max(max_i,i)
            max_prime=max(max_prime,*found)
        groups.append({'j':j,'records':records})
        total += len(records)
        print(json.dumps({'j':j,'triples':len(records),'cumulative':total,
                          'unresolved':len(unresolved)}),flush=True)
    data={'equation':'C(C(i,j),k)=C(i^2,j^2)+k^2',
          'j_min':j_min,'j_max':j_max,
          'coverage':'all valid unbounded i and k, using proved reductions',
          'record_format':['i','r','lower_branch_prime','upper_branch_prime'],
          'candidate_triples':total,'candidate_equations':branches,
          'largest_i':max_i,'largest_certificate_prime':max_prime,
          'unresolved':unresolved,'groups':groups}
    CERTIFICATE.write_text(json.dumps(data,separators=(',',':')))
    print(json.dumps({k:v for k,v in data.items() if k!='groups'},indent=2))


def verify():
    data=json.loads(CERTIFICATE.read_text())
    assert data['unresolved']==[]
    assert data['j_min']>=21
    assert [g['j'] for g in data['groups']] == list(range(data['j_min'],data['j_max']+1))
    total=branches=max_i=max_prime=0
    checked_primes=set()
    for group in data['groups']:
        j=group['j']
        records=group['records']
        expected=independently_verify_candidates(j)
        assert len(records)==len(expected)
        coefficient_cache={}
        for i,r,p_lower,p_upper in records:
            assert (i,r) in expected
            expected.remove((i,r))
            A=coefficient_cache.setdefault(i,comb(i,j))
            for p,B in [(p_lower,r),(p_upper,A-r)]:
                if p not in checked_primes:
                    assert isinstance(p,int) and p>=2
                    assert all(p%d for d in range(2,isqrt(p)+1))
                    checked_primes.add(p)
                L=lucas_direct(A,r,p)
                X=lucas_direct(i*i,j*j,p)
                assert (L-X-B*B)%p != 0
            branches += 1 if A==2*r else 2
            max_i=max(max_i,i)
            max_prime=max(max_prime,p_lower,p_upper)
        assert not expected
        total += len(records)
        print(json.dumps({'verified_j':j,'triples':len(records),'cumulative':total}),flush=True)
    assert total==data['candidate_triples']
    assert branches==data['candidate_equations']
    assert max_i==data['largest_i']
    assert max_prime==data['largest_certificate_prime']
    report={'status':'all_candidates_excluded_and_coverage_verified',
            'j_min':data['j_min'],'j_max':data['j_max'],
            'coverage':data['coverage'],
            'candidate_triples':total,'candidate_equations':branches,
            'largest_i':max_i,'largest_certificate_prime':max_prime,
            'unresolved':0,
            'certificate_sha256':hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest(),
            'verification_arithmetic':'exact integers, independent enumeration and Lucas residues',
            'formal_proof_assistant_executed_by_this_script':False}
    REPORT.write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['generate','verify'])
    parser.add_argument('--j-min',type=int,default=21)
    parser.add_argument('--j-max',type=int,default=100)
    args=parser.parse_args()
    if args.mode=='generate':
        generate(args.j_min,args.j_max)
    else:
        verify()
