#!/usr/bin/env python3
"""Independent standard-library verifier for the v19 canonical-J certificate.

No import from the producer and no computer-algebra package is used.
The mathematical coverage and monotonicity proofs are in the companion note.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt, prod
from pathlib import Path
import argparse
import json


def prime_factors(value):
    result=[]
    p=2
    while p*p<=value:
        e=0
        while value%p==0:
            value//=p
            e+=1
        if e:
            result.append((p,e))
        p=3 if p==2 else p+2
    if value>1:
        result.append((value,1))
    return result


def integer_roots_of_divisibility(c):
    powers=[(p,3*e//2) for p,e in prime_factors(c)]
    result=[]
    def visit(i,d):
        if i==len(powers):
            result.append(d)
            return
        p,e=powers[i]
        for k in range(e+1):
            visit(i+1,d*p**k)
    visit(0,1)
    assert len(result)==len(set(result))==prod(e+1 for _,e in powers)
    assert all(c**3%(d*d)==0 for d in result)
    return sorted(result)


def bound(j):
    # Sequential boundary detection, independent of producer's binary search.
    c=Fraction(9*1667**4*j**4,30000**4)
    w=1
    while Fraction(w**4,(10*w+2*j)**3)<c:
        w+=1
    return w-1


def trim(a,p):
    a=[v%p for v in a]
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a or [0]


def add(a,b,p):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c,p)


def multiply(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            c[i+j]+=u*v
    return trim(c,p)


def remainder(a,b,p):
    a,b=trim(a,p),trim(b,p)
    assert b!=[0]
    while a!=[0] and len(a)>=len(b):
        offset=len(a)-len(b)
        factor=a[-1]*pow(b[-1],-1,p)%p
        for i,v in enumerate(b):
            a[i+offset]=(a[i+offset]-factor*v)%p
        a=trim(a,p)
    return a


def is_prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def main(certificate,output):
    saved=json.loads(certificate.read_text())
    expected_rows=[]
    expected_groups=defaultdict(list)
    totals=Counter()
    families={f['J']:f for f in saved['families']}
    assert sorted(families)==list(range(1,17))
    for j in range(1,17):
        family=families[j]
        if j%8 in {0,2,6}:
            assert family['method']=='universal 2-adic obstruction'
            continue
        assert family['method']=='finite divisor elimination'
        W=bound(j)
        assert family['w_max']==W
        counts=Counter()
        for w in range(65,W+1):
            if gcd(w,j)>1:
                continue
            counts['primitive_w']+=1
            c0,c1=10*w+2*j,25*w+3*j
            D0=integer_roots_of_divisibility(c0)
            counts['raw_divisor_records']+=2*len(D0)
            Ns=sorted({a for a in D0 if a%3} | {3*a for a in D0})
            Ns=[n for n in Ns if n>=104]
            counts['normalized_n']+=len(Ns)
            for n in Ns:
                if Fraction(n*j*j,w*w)<=Fraction(30000**2,1667**2):
                    continue
                counts['height_compatible']+=1
                g,d=gcd(n,3),gcd(n-1,6)
                Q0,Q1=n//g,(n-1)//d
                rem=c1**3%(Q1*Q1)
                assert rem!=0
                expected_rows.append({'J':j,'w':w,'n':n,'g':g,'d':d,
                                      'Q0':Q0,'Q1':Q1,'c0':c0,'c1':c1,
                                      'second_divisor_remainder':rem})
                expected_groups[(j,w)].append(n)
        assert dict(counts)==family['counts']
        totals.update(counts)
    key=lambda row:(row['J'],row['w'],row['n'])
    assert sorted(expected_rows,key=key)==sorted(saved['height_candidates'],key=key)
    assert dict(totals)==saved['totals']
    seen=set()
    for cert in saved['bezout_certificates']:
        j,w=cert['J'],cert['w']
        assert (j,w) not in seen
        seen.add((j,w))
        ns=expected_groups[(j,w)]
        assert cert['first_n']==ns
        p=cert['prime']
        assert is_prime(p)
        P=[1]
        for n in ns:
            P=multiply(P,[-n,1],p)
        assert P==cert['P']
        c1=25*w+3*j
        Ds=integer_roots_of_divisibility(c1)
        Hroots=sorted({d*z+1 for d in (1,2,3,6) for z in Ds if gcd(d*z,6)==d})
        assert len(Hroots)==cert['second_domain_size']
        H=[1]
        for n in Hroots:
            H=remainder(multiply(H,[-n,1],p),P,p)
        assert H==cert['H_remainder']
        assert add(multiply(cert['U'],P,p),multiply(cert['V'],H,p),p)==[1]
        assert cert['groebner_basis']==[1]
    assert seen==set(expected_groups)
    assert len(seen)==saved['certificate_count']
    assert max(c['prime'] for c in saved['bezout_certificates'])==saved['max_certificate_prime']
    # Complete residue-class checks of the polynomial assertions in the
    # written 2-adic proof; these are finite coverage, not sampled n values.
    for n in range(8):
        for R in range(8):
            T=R*R-9*n*n-6*n-10
            if n%2==0:
                assert (9*n*n+6*n)%8==0 and T%8 in (2,6,7)
            elif R%2:
                assert T%4==0
            else:
                assert T%2==1
            if n%4==3 and R%2:
                assert T%8==4
    short=9*Fraction(132,13)**3*Fraction(1667,6000)**4
    assert short<65 and str(short)==saved['symbolic_checks']['J_le_5_w_bound']
    result={'status':'PASS','certificate_sha256':sha256(certificate.read_bytes()).hexdigest(),
            'checker':'Python standard library only; no producer import or SymPy',
            'complete_reconstructed_rows':len(expected_rows),
            'bezout_identities':len(seen),'max_prime':saved['max_certificate_prime'],
            'totals':dict(totals),
            'scope':'Finite canonical J <= 16 only, under the stated inherited conditions.'}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    root=Path(__file__).resolve().parent
    p.add_argument('--certificate',type=Path,default=root/'v19_canonical_J_certificate.json')
    p.add_argument('--output',type=Path,default=root/'v19_canonical_J_verification.json')
    args=p.parse_args()
    main(args.certificate,args.output)
