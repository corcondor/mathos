"""Exact finite certificates for prime i=p>=2j, ell=2, B<p.

The caller's analytic argument handles p>=1,000,000. This script
covers the finite necessary-congruence set below that threshold.
The large A=C(p,j) is evaluated modulo prime powers, not expanded.
Generator and verifier use independent enumeration and binomial-
mod-prime-power algorithms.
"""
from array import array
from collections import defaultdict
from math import comb, isqrt
from pathlib import Path
import argparse
import hashlib
import json


LIMIT=1_000_000
CERT=Path('v4_prime_ell_two_finite_certificates.json')
REPORT=Path('v4_prime_ell_two_finite_verification.json')


def prime_trial(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def sieve_primes(limit):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p]=b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(2,limit+1) if sieve[p]]


def generator_candidates():
    rows=set()
    for k in range(4,isqrt(2*(LIMIT-1)+3)+1):
        B=k*(k-1)//2
        for m in [1,2]:
            for c in [2,3]:
                numerator=k*k-c
                if numerator%m:
                    continue
                p=numerator//m
                if not 43<=p<LIMIT or B>=p or not prime_trial(p):
                    continue
                for epsilon in [-1,1]:
                    coefficient=m if c==2 else 3*m
                    rhs=-12*epsilon*(k+2) if c==2 else 4*epsilon*(k+3)
                    j=rhs*pow(coefficient,-1,p)%p
                    if (21<=j and 2*j<=p and j+2<=B<2*j
                            and (-1)**(j+B-2)==epsilon):
                        rows.add((p,j,k,m,c))
    return sorted(rows)


def verifier_candidates():
    rows=set()
    for p in sieve_primes(LIMIT-1):
        if p<43:
            continue
        for m in range(1,3):
            for c in range(2,4):
                k=isqrt(m*p+c)
                if k*k != m*p+c or k<4:
                    continue
                B=comb(k,2)
                if B>=p:
                    continue
                for epsilon in [-1,1]:
                    coefficient=m if c==2 else 3*m
                    rhs=-12*epsilon*(k+2) if c==2 else 4*epsilon*(k+3)
                    # coefficient*j = rhs+h*p. No modular inverse is used.
                    h_min=-((rhs-coefficient*21)//p)
                    h_max=(coefficient*(p//2)-rhs)//p
                    for h in range(h_min,h_max+1):
                        numerator=rhs+h*p
                        if numerator%coefficient:
                            continue
                        j=numerator//coefficient
                        if (21<=j<=p//2 and j+2<=B<2*j
                                and (1 if (j+B)%2==0 else -1)==epsilon):
                            rows.add((p,j,k,m,c))
    return rows


def factorial_valuation(n,q):
    result=0
    while n:
        n//=q
        result+=n
    return result


def exponent_for_lower_index(B,q):
    exponent=1
    modulus=q
    while modulus<=B:
        exponent+=1
        modulus*=q
    return exponent,modulus


class BlockBinomial:
    """q-free blocks and recursive factorials modulo q**exponent."""
    def __init__(self,max_n):
        self.max_n=max_n
        self.cache={}

    def table(self,q,modulus):
        key=(q,modulus)
        if key not in self.cache:
            prefix=array('I',[1])
            value=1
            for t in range(1,min(modulus,self.max_n)+1):
                if t%q:
                    value=value*t%modulus
                prefix.append(value)
            self.cache[key]=prefix
        return self.cache[key]

    def choose(self,n,k,q,exponent):
        modulus=q**exponent
        valuation=(factorial_valuation(n,q)-factorial_valuation(k,q)
                   -factorial_valuation(n-k,q))
        if valuation>=exponent:
            return 0
        prefix=self.table(q,modulus)
        block=prefix[modulus] if modulus<=self.max_n else 1
        def unit_factorial(t):
            answer=1
            while t:
                answer=answer*pow(block,t//modulus,modulus)*prefix[t%modulus]%modulus
                t//=q
            return answer
        numerator=unit_factorial(n)
        denominator=unit_factorial(k)*unit_factorial(n-k)%modulus
        return numerator*pow(denominator,-1,modulus)*pow(q,valuation,modulus)%modulus


def lucas_product(n,k,q):
    result=1
    while k:
        nd,kd=n%q,k%q
        if kd>nd:
            return 0
        numerator=denominator=1
        for t in range(1,kd+1):
            numerator=numerator*(nd-t+1)%q
            denominator=denominator*t%q
        result=result*numerator*pow(denominator,-1,q)%q
        n//=q
        k//=q
    return result


def lucas_comb(n,k,q):
    result=1
    while n or k:
        nd,kd=n%q,k%q
        if kd>nd:
            return 0
        result=result*comb(nd,kd)%q
        n//=q
        k//=q
    return result


def test_generator_primitive():
    computer=BlockBinomial(120)
    count=0
    for q in [2,3,5,7]:
        for exponent in range(1,6):
            for n in range(1,121):
                for k in [0,1,n//3,n//2,n-1,n]:
                    assert computer.choose(n,k,q,exponent)==comb(n,k)%q**exponent
                    count+=1
    return count


def generate():
    checks=test_generator_primitive()
    rows=generator_candidates()
    computer=BlockBinomial(max(row[0] for row in rows))
    records=[]
    unresolved=[]
    primes=sieve_primes(997)
    for number,(p,j,k,m,c) in enumerate(rows,1):
        B=comb(k,2)
        for q in primes:
            exponent,modulus=exponent_for_lower_index(B,q)
            A_residue=computer.choose(p,j,q,exponent)
            L=lucas_product(A_residue,B,q)
            rhs=(lucas_product(p*p,j*j,q)+comb(k*k,4))%q
            if L!=rhs:
                records.append([p,j,k,m,c,q])
                break
        else:
            unresolved.append([p,j,k,m,c])
        if number%50==0:
            print(json.dumps({'processed':number,'total':len(rows),'unresolved':len(unresolved)}),flush=True)
    data={'scope':'prime p<1000000, j>=21,2j<=p,ell=2,j+2<=B=C(k,2)<2j; all necessary m,c,unit-congruence cases',
          'limit_exclusive':LIMIT,
          'candidate_count':len(rows),
          'generator_prime_power_primitive_checks':checks,
          'record_format':['p','j','k','m','c','obstruction_prime'],
          'unresolved':unresolved,'records':records}
    CERT.write_text(json.dumps(data,separators=(',',':')))
    print(json.dumps({key:value for key,value in data.items() if key!='records'},indent=2))


def stripped_factorials_at(needed,q,modulus):
    """Independent implementation: strip q from each individual integer."""
    values={0:1}
    product=1
    for t in range(1,max(needed)+1):
        unit=t
        while unit%q==0:
            unit//=q
        product=product*unit%modulus
        if t in needed:
            values[t]=product
    assert all(t in values for t in needed)
    return values


def verify():
    raw=CERT.read_bytes()
    data=json.loads(raw)
    assert data['limit_exclusive']==LIMIT
    assert data['unresolved']==[]
    expected=verifier_candidates()
    assert len(expected)==data['candidate_count']==len(data['records'])
    by_modulus=defaultdict(list)
    for p,j,k,m,c,q in data['records']:
        key=(p,j,k,m,c)
        assert key in expected
        expected.remove(key)
        assert prime_trial(q)
        B=comb(k,2)
        exponent,modulus=exponent_for_lower_index(B,q)
        by_modulus[(q,exponent)].append((p,j,k,B))
    assert not expected
    count=0
    for (q,exponent),rows in sorted(by_modulus.items()):
        modulus=q**exponent
        needed={t for p,j,k,B in rows for t in (p,j,p-j)}
        units=stripped_factorials_at(needed,q,modulus)
        for p,j,k,B in rows:
            # Different valuation expression from the generator's recurrence.
            power=q
            valuation=0
            while power<=p:
                valuation+=p//power-j//power-(p-j)//power
                power*=q
            A_residue=(units[p]*pow(units[j]*units[p-j],-1,modulus)
                       *pow(q,valuation,modulus))%modulus
            L=lucas_comb(A_residue,B,q)
            X=lucas_comb(p*p,j*j,q)
            Y=lucas_comb(k*k,4,q)
            assert (L-X-Y)%q!=0,(p,j,k,q)
            count+=1
        print(json.dumps({'verified_modulus_prime':q,'exponent':exponent,'candidates':len(rows),'total_verified':count}),flush=True)
    assert count==data['candidate_count']
    report={'status':'all_finite_candidates_excluded_with_independent_coverage_and_residues',
            'scope':data['scope'],'candidate_count':count,'unresolved':0,
            'largest_p':max(row[0] for row in data['records']),
            'largest_obstruction_prime':max(row[-1] for row in data['records']),
            'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'formal_proof_assistant_executed_by_this_script':False}
    REPORT.write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['generate','verify'])
    args=parser.parse_args()
    if args.action=='generate':generate()
    else:verify()
