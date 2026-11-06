#!/usr/bin/env python3
"""Independent exact audit of the v17 quadratic-neighbor deductions.

This file imports no producer. Complete exceptional domains and supporting
valuation samples are reported separately. The universal statements depend
on the written proofs, not extrapolation from samples.
"""
from pathlib import Path
from math import gcd, comb, isqrt
from fractions import Fraction
import hashlib
import json
import argparse

ROOT = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--producer-report',type=Path,
                default=ROOT/'v17_quadratic_prime_powers_checks.json')
ap.add_argument('--output',type=Path,
                default=ROOT/'v17_quadratic_independent_audit.json')
args = ap.parse_args()
CSET = (2,3,5,6,7,8,10,11,12,13,14,15)

def factors(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1
            n //= p
        p += 1
    if n > 1: out[n] = out.get(n,0)+1
    return out

def vf(n,p):
    total = 0
    while n:
        n //= p
        total += n
    return total

def vb(n,k,p):
    return vf(n,p)-vf(k,p)-vf(n-k,p)

def vi(n,p):
    assert n > 0
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def power_level(m,p):
    j,q = 0,1
    while q*p <= m:
        j,q = j+1,q*p
    return j

tables = []
remaining = []
constants = []
for c in CSET:
    ps = {29,31,37}
    for t in range(c+1):
        d = (9+t)**2-36*c
        assert d != 0
        f = factors(abs(d))
        assert __import__('math').prod(p**v for p,v in f.items()) == abs(d)
        constants.append({'c':c,'t':t,'D':d,'factors':f})
        ps.update(p for p in f if p >= 29)
    for p in sorted(ps):
        mod = p*p
        # Full residues, independently of any lifted root list.
        roots = [x for x in range(mod) if (x*x-c) % mod == 0]
        assert len(roots) in (0,2)
        upper = (mod+8)//6
        ns = [n for n in roots if 104 <= n <= upper
              and ((c+2)*n-3*c)%6 == 0]
        tables.append({'c':c,'p':p,'roots':roots,'upper':upper,'n':ns})
        for n in ns:
            M = gcd(n,3)*gcd(n-1,6)
            Q = n*(n-1)//M
            F = __import__('math').prod(q**((v+2)//3) for q,v in factors(Q).items())
            assert 3*F > 10*n
            remaining.append({'c':c,'p':p,'n':n,'Q':Q,'F':F})
assert len(constants) == 118 and len(tables) == 69, (len(constants),len(tables))
assert {(x['c'],x['p'],x['n']) for x in remaining} == {
    (7,37,157),(10,71,275),(10,191,5382),(13,43,149)}

primes = [p for p in range(29,240) if factors(p)=={p:1}]
counts = {'n_inputs':0,'n_r_cases':0,'n_minus_one_inputs':0,
          'n_minus_one_r_cases':0,'actual_binomial_checks':0}
details = []
for p in primes:
    for w in range(1,(p-1)//6+1):
        for shift in (0,1):
            n = p*w+shift
            if n < 104: continue
            m,A = 6*n-9,comb(n,3)
            assert p*p > m and p > 6*w and vi(A,p)==1
            inner = vb(n*n,m,p)
            assert inner == 2
            key = 'n' if shift == 0 else 'n_minus_one'
            counts[key+'_inputs'] += 1
            for u in range((3*n)//p+1,(10*n-1)//(3*p)+1):
                r = p*u
                assert 3*n < r and 3*r < 10*n and u<p
                outer = vb(A,r,p)
                alpha = A//p
                b = alpha%p
                assert outer == vb(alpha,u,p)
                if shift == 1:
                    j = (p*w)%6 or 6
                    assert b == (j*p-w)//6
                    assert alpha-b == p*(p*w**3-j)//6
                    assert outer == int(b<u)
                elif n%3 == 0:
                    assert outer == 1
                elif n%3 == 1:
                    assert b == (w+2*p)//3 and b>u and outer==0
                elif outer >= 2:
                    assert 6*w < p < 9*w and (3*w*w+2)%p==0
                counts[key+'_r_cases'] += 1
                if len(details)<32:
                    details.append({'n':n,'p':p,'w':w,'shift':shift,
                                    'r':r,'inner_v':inner,'outer_v':outer})
                if counts['actual_binomial_checks']<12 and n<1000:
                    assert vi(comb(n*n,m),p)==inner
                    assert vi(comb(A,r),p)==outer
                    counts['actual_binomial_checks'] += 1

# Supporting check of the general binomial congruence, using actual binomials.
loss_checks = 0
for p in (2,3,5,7,11,17):
    for e in range(1,5):
        U = p**e
        for s in sorted({1,min(U,7),min(U,31),min(U,67)}):
            level=power_level(s,p)
            if e<=level: continue
            mod=p**(e-level)
            for b in (0,1,3):
                if b>=s: continue
                assert comb(U+b,s)%mod==0
                loss_checks += 1
            assert (comb(U-1,s)-(-1)**s)%mod==0
            loss_checks += 1

assert Fraction(208000,927)<225
for n in range(104,110):
    M=gcd(n,3)*gcd(n-1,6)
    Q=n*(n-1)//M
    assert comb(n,3)%Q==0

producer=json.loads(args.producer_report.read_text())
producer_domain=producer['complete_exception_domain']
producer_tables={(x['c'],x['p']):(x['roots'],x['n_upper'],x['indices'])
                 for x in producer_domain['tables']}
actual_tables={(x['c'],x['p']):(x['roots'],x['upper'],x['n']) for x in tables}
assert producer_tables==actual_tables
assert producer_domain['constants_count']==len(constants)
assert producer_domain['root_table_count']==len(tables)

result = {
 'status':'PASS','scope':'ell=1, j=i-3; both original branches',
 'complete_exception_constants':len(constants),
 'complete_exception_pairs':len(tables),
 'complete_exception_roots':tables,'forced_indices':remaining,
 'supporting_valuation_counts':counts,'supporting_valuation_examples':details,
 'supporting_general_binomial_congruences':loss_checks,
 'complete_producer_table_comparison':'PASS',
 'producer_report_sha256':hashlib.sha256(args.producer_report.read_bytes()).hexdigest(),
 'proof_note_sha256':producer['proof_note_sha256'],
 'independent_producer_imports':False,
 'finite_support_checks_prove_universal_theorems':False,
 'new_lean_execution':False,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out=args.output
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in
 ('complete_exception_roots','supporting_valuation_examples','source_sha256')},ensure_ascii=False))
