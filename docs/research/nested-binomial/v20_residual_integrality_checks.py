#!/usr/bin/env python3
"""Exact identities, complete small-residue checks, and reverse reconstruction.

No numerical search is used to prove the unbounded statements. The gcd proof
uses a polynomial Bezout identity; the core exponent proof is symbolic in
v3(Z). No new Lean, DeepSeek, or complete Selmer computation is claimed.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

import sympy as sp

HERE=Path(__file__).resolve().parent
BS=[b for b in range(1,487) if 486%b==0]
ALLOWED3={0:[(0,0)],1:[(0,1),(1,0),(2,2)],2:[(0,2),(2,0)],
          3:[(1,2),(2,1)],4:[(2,2)],5:[(0,2),(2,0)]}


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def vp(n,p):
    assert n
    n=abs(n);e=0
    while n%p==0:n//=p;e+=1
    return e


def F(a,b,r):
    return 4*a**6+(24*b*b-12*r)*a**4+(36*b**4+60*b*b*r+12*r*r)*a*a-3*b*b*r*r-4*r**3


def identities():
    a,b,n,t,r,y=sp.symbols('a b n t rho y')
    q=t*t+3*t+3
    E1=81*a*n*(n-1)-b*(9*n*q+t**3)
    E2=r-a*a-a*b*(9*n-t-6)+b*b*q
    N=b*b*q+a*b*(t+6)-a*a+r
    P=N*N-(9*a*b+b*b*q)*N-a*b**3*t**3
    S=a**3-a*a*b*(2*t+3)-21*a*b*b-a*r-b**3*(6*t+9)+b*r*(t-3)
    checks={
      'bezout_9':sp.expand((2*t*t-3*t+3)*q-(2*t+3)*t**3-9)==0,
      'combined_defining_equations':sp.expand(b*E1+9*n*E2-(9*n*(r-a*a+a*b*(t-3))-b*b*t**3))==0,
      'square_to_quartic':sp.expand((2*b*r*t-2*a*(a*a+3*b*b)+r*(3*b+2*a))**2-F(a,b,r)-4*r*P)==0,
      'rational_reconstruction':sp.cancel(a*b*b*E1.subs(n,N/(9*a*b))-P)==0,
      'saturation_identity':sp.expand(P-r*N-a*S)==0,
      'Z_rearrangement':sp.expand(a*a-b*b-(a*a+a*b*(9*n-t-6)-b*b*q)-b*(b*(t+1)*(t+2)+a*(t+6-9*n)))==0,
    }
    assert all(checks.values())
    return checks


def residue_tables():
    q_table=[]
    for t in range(9):
        q=t*t+3*t+3
        assert gcd(t**3,q)==gcd(t,3)
        if t%3==0:assert q%9==3
        q_table.append({'t_mod9':t,'q_mod9':q%9,'t_cubed_mod9':t**3%9,
                        'gcd_allowed':gcd(t,3)})
    rho_rows=[];global_rhos=set();examined=0
    for b in BS:
        d=vp(b,3) if b%3==0 else 0
        for a in range(9):
            if a%3==b%3==0:continue
            allowed=set()
            for n in range(9):
                for t in range(9):
                    if d<=3 and t%3:continue
                    rho=(a*a+a*b*(9*n-t-6)-b*b*(t*t+3*t+3))%9
                    assert rho%3==a*a%3
                    if a%3==0:assert rho==6
                    assert rho in(1,4,6,7)
                    allowed.add(rho);global_rhos.add(rho);examined+=1
            rho_rows.append({'b':b,'a_mod9':a,'rho_mod9':sorted(allowed)})
    assert global_rhos=={1,4,6,7}
    parity=[]
    for a in range(2):
        for b in range(2):
            if not(a or b):continue
            rows=[]
            for n in range(2):
                for t in range(2):
                    if b and n!=t:continue
                    rho=(a*a+a*b*(9*n-t-6)-b*b*(t*t+3*t+3))%2
                    Z=(b*(t+1)*(t+2)+a*(t+6-9*n))%2
                    assert rho==(a+b)%2
                    if b:assert Z==0
                    rows.append([n,t,rho,Z])
            parity.append({'a_mod2':a,'b_mod2':b,'rows_n_t_rho_Z':rows})
    return {'q_mod9':q_table,'rho_rows':rho_rows,'rho_global_classes':sorted(global_rhos),
            'rho_tuples_checked':examined,'parity_rows':parity,
            'role':'Complete residue tables for the stated congruences. The all-prime gcd theorem uses Bezout plus the q mod9 table.'}


def core_tables():
    three=[]
    for d in range(6):
        formal=[(0,0)] if d==0 else [(i,j) for i in range(3) for j in range(3) if (i+j+2*d)%3==0]
        allowed=ALLOWED3[d]
        assert set(allowed)<=set(formal)
        if d>=2:
            # In the unbounded rule (2,d+3f-2), reducing modulo3 removes f.
            formula=sorted({(2,(d-2)%3),((d-2)%3,2)})
            assert formula==allowed
        three.append({'v3_b':d,'formal_pairs':formal,'allowed_pairs':allowed,
                      'Z_divisible_by3_required':1<=d<=3,
                      'infinite_exponent_rule':None if d<2 else 'If d+3f>4: (2,d+3f-2) or reverse; if d+3f=4: (2,2).',
                      'proof_uses_exponent_cutoff':False})
    two=[{'b_even':True,'a_odd':True,'formal_pairs':[(0,1),(1,0),(2,2)],'allowed_pairs':[(0,1),(1,0)]},
         {'b_even':False,'a_odd':True,'formal_pairs':[(0,0),(1,2),(2,1)],'allowed_pairs':[(0,0),(1,2),(2,1)]},
         {'b_even':False,'a_odd':False,'formal_pairs':[(0,0)],'allowed_pairs':[(0,0)]}]
    count_rows=[]
    for b in BS:
        d=vp(b,3) if b%3==0 else 0
        for a_odd in (False,True):
            if b%2==0 and not a_odd:continue
            n2=2 if b%2==0 else 3 if a_odd else 1
            old2=3 if b%2==0 or a_odd else 1
            old3=3 if d else 1
            count_rows.append({'b':b,'a_odd':a_odd,'old_small_prime_types':old2*old3,
                               'new_small_prime_types':n2*len(ALLOWED3[d]),
                               'multiply_by':'3^omega_{p>=5}(9a^2-b^2)'})
    return {'prime3':three,'prime2':two,'type_counts':count_rows}


def reconstruction(a,b,rho):
    ff=F(a,b,rho);y=isqrt(ff)
    assert y*y==ff
    Z=(a*a-b*b-rho)//b
    assert a*a-b*b-rho==b*Z and Z>0
    L=9*a*a-b*b-3*b*Z
    assert y%b==0 and (y//b-L)%2==0
    U,V=(y//b-L)//2,(y//b+L)//2
    assert U>0 and V>0 and U*V==b*Z**3
    g0=gcd(U,V);D=9*a*a-b*b
    assert D**3%(g0*g0)==0 and gcd(g0,a)==1 and 9%gcd(g0,b)==0
    roots=[]
    for sign in(-1,1):
        t=Fraction(2*a*(a*a+3*b*b)-rho*(3*b+2*a)+sign*y,2*b*rho)
        n=(b*(t+1)*(t+2)+a*(t+6)-Z)/(9*a)
        assert 81*a*n*(n-1)==b*(9*n*(t*t+3*t+3)+t**3)
        assert rho==a*a+a*b*(9*n-t-6)-b*b*(t*t+3*t+3)
        if t.denominator==1:
            assert (9*gcd(a,rho))%n.denominator==0
        roots.append({'sign':sign,'t':str(t),'n':str(n),'t_integer':t.denominator==1,
                      'n_integer':n.denominator==1})
    return {'a':a,'b':b,'rho':rho,'y':y,'Z':Z,'U':U,'V':V,'common_factor':g0,
            'gcd_filter':gcd(a,rho)==gcd(a,3),
            'rho_filter':rho%3==a*a%3 and (a%3!=0 or rho%9==6),
            'roots':roots}


def examples():
    bad=[reconstruction(*x) for x in[(31,1,124),(84,1,477),(373,2,13573),(77,9,520)]]
    for row in bad:
        a,b,rho=row['a'],row['b'],row['rho']
        assert gcd(a,b)==1 and 486%b==0 and 27*a>=31*b and rho>=13
        assert 1377*rho<216*a*a+760*b*b and (rho-b*b)%5!=0
    # Existing v19 necessary-condition points; all were already excluded
    # by original binomial congruences. They are not original solutions.
    original_pairs=[(41553,126882),(73696,223720),(138625,421420),
      (108785369383737973503877149475097188315,327052706826716357119041354754724800365),
      (20977142168815802252502431909486399850592,63021008653584142840540672897688746194336),
      (170263459131429393121255301571296045256626383,511154058734342489503225686588245360405929209)]
    valid=[]
    for n,r in original_pairs:
        t=r-3*n
        ab=Fraction((9*t*t+27*t+27)*n+t**3,81*n*(n-1))
        a,b=ab.numerator,ab.denominator
        rho=a*a+a*b*(9*n-t-6)-b*b*(t*t+3*t+3)
        row=reconstruction(a,b,rho)
        assert row['gcd_filter'] and row['rho_filter']
        assert rho%2==(a+b)%2 and rho%9 in(1,4,6,7)
        assert any(Fraction(z['t'])==t and Fraction(z['n'])==n for z in row['roots'])
        d=vp(b,3) if b%3==0 else 0
        if d<=3:assert t%3==0
        if 1<=d<=3:assert row['Z']%3==0
        if d==0:assert row['Z']%3==(-b)%3
        if b%2:assert row['Z']%2==0
        uv3=(vp(row['U'],3)%3,vp(row['V'],3)%3)
        assert uv3 in ALLOWED3[d]
        if b%2==0:assert (vp(row['U'],2)%3,vp(row['V'],2)%3) in ((0,1),(1,0))
        row.update({'source_n':n,'source_r':r,'source_t':t,
                    'source_status':'v19 auxiliary candidate, already rejected by original-equation modular witnesses',
                    'v3_core_pair':uv3})
        valid.append(row)
    return {'overinclusive_sextic_examples':bad,'integer_reconstruction_examples':valid,
            'examples_are_original_solutions':False}


def main():
    result={'status':'PASS','date_jst':'2026-11-07',
       'identity_checks':identities(),'residue_tables':residue_tables(),'cube_core_tables':core_tables(),
       'examples':examples(),
       'new_uniform_conclusions':['gcd(a,rho)=gcd(a,3)','rho mod9 in {1,4,6,7}','rho>=13 using prior rho>=11',
         'rho=a+b mod2','at most N2*N3(v3(b))*3^omega_{p>=5}(D) cube coefficient types'],
       'proof_scope':'Written Bezout/valuation proof plus exact finite residue verification; not a search-based universal inference',
       'producer_sha256':sha(Path(__file__)),'note_sha256':sha(HERE/'v20_residual_integrality.md'),
       'claims_not_made':['Lean execution','DeepSeek execution','full original equation solved','complete Selmer group']}
    path=HERE/'v20_residual_integrality_certificate.json'
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','identities':len(result['identity_checks']),
        'rho_residue_tuples':result['residue_tables']['rho_tuples_checked'],
        'coefficient_count_rows':len(result['cube_core_tables']['type_counts']),
        'examples':len(result['examples']['integer_reconstruction_examples'])+len(result['examples']['overinclusive_sextic_examples']),
        'certificate_sha256':sha(path)},indent=2))


if __name__=='__main__':main()
