#!/usr/bin/env python3
"""Standard-library-only independent audit of v20 residual integrality.

Does not execute/import the producer or SymPy. Complete residue enumeration
supports the written universal Bezout and valuation proofs, not an extrapolation.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

HERE=Path(__file__).resolve().parent


def ring(n):
    class P:
        def __init__(self,x=0):
            if isinstance(x,P):x=x.d
            if isinstance(x,int):x={(0,)*n:x}
            self.d={e:c for e,c in x.items() if c}
        def __add__(self,x):
            d=self.d.copy()
            for e,c in P(x).d.items():d[e]=d.get(e,0)+c
            return P(d)
        __radd__=__add__
        def __neg__(self):return P({e:-c for e,c in self.d.items()})
        def __sub__(self,x):return self+-P(x)
        def __rsub__(self,x):return P(x)+-self
        def __mul__(self,x):
            d={}
            for e,c in self.d.items():
                for f,v in P(x).d.items():
                    g=tuple(a+b for a,b in zip(e,f));d[g]=d.get(g,0)+c*v
            return P(d)
        __rmul__=__mul__
        def __pow__(self,k):
            p=P(1)
            for _ in range(k):p=p*self
            return p
    return [P({tuple(int(i==j) for j in range(n)):1}) for i in range(n)]


def F(a,b,r):
    return 4*a**6+24*b*b*a**4-12*r*a**4+36*b**4*a*a+60*b*b*r*a*a+12*r*r*a*a-3*b*b*r*r-4*r**3


def identities():
    out=[]
    def zero(label,p):
        assert not p.d,label
        out.append(label)
    a,b,n,t,r=ring(5);q=t*t+3*t+3
    E1=81*a*n*(n-1)-b*(9*n*q+t**3)
    E2=r-a*a-a*b*(9*n-t-6)+b*b*q
    N=b*b*q+a*b*(t+6)-a*a+r
    P=N*N-(9*a*b+b*b*q)*N-a*b**3*t**3
    S=a**3-a*a*b*(2*t+3)-21*a*b*b-a*r-b**3*(6*t+9)+b*r*(t-3)
    zero('bezout_9',(2*t*t-3*t+3)*q-(2*t+3)*t**3-9)
    zero('defining_equation_elimination',b*E1+9*n*E2-9*n*(r-a*a+a*b*(t-3))+b*b*t**3)
    zero('square_to_quartic',(2*b*r*t-2*a*(a*a+3*b*b)+r*(3*b+2*a))**2-F(a,b,r)-4*r*P)
    zero('denominator_saturation',P-r*N-a*S)
    rr=a*a+a*b*(9*n-t-6)-b*b*q
    NN=b*b*q+a*b*(t+6)-a*a+rr
    PP=NN*NN-(9*a*b+b*b*q)*NN-a*b**3*t**3
    zero('rational_reverse_reconstruction',PP-a*b*b*E1)
    zero('Z_rearrangement',a*a-b*b-rr-b*(b*(t+1)*(t+2)+a*(t+6-9*n)))
    return out


def val(n,p):
    assert n
    n=abs(n);e=0
    while not n%p:n//=p;e+=1
    return e


def residue_audit(cert):
    expected_q=[]
    for t in range(9):
        q=t*t+3*t+3
        assert ((2*t*t-3*t+3)*q-(2*t+3)*t**3)==9
        if t%3==0:assert q%9==3
        else:assert t**3%3!=0
        expected_q.append({'t_mod9':t,'q_mod9':q%9,'t_cubed_mod9':t**3%9,'gcd_allowed':gcd(t,3)})
    assert expected_q==cert['residue_tables']['q_mod9']
    rows=[];count=0;global_classes=set()
    for b in sorted({2**e*3**d for e in range(2) for d in range(6)}):
        d=val(b,3)
        for a in range(9):
            if gcd(gcd(a,b),3)>1:continue
            rho_set=set()
            for rho in range(9):
                for t in range(9):
                    if d<4 and t%3!=0:continue
                    for n in range(9):
                        residue=(rho-a*a-a*b*(9*n-t-6)+b*b*(t*t+3*t+3))%9
                        if residue:continue
                        assert rho%3==a*a%3
                        if a%3==0:assert rho==6
                        rho_set.add(rho);global_classes.add(rho);count+=1
            rows.append({'b':b,'a_mod9':a,'rho_mod9':sorted(rho_set)})
    assert rows==cert['residue_tables']['rho_rows']
    assert count==cert['residue_tables']['rho_tuples_checked']==3402
    assert global_classes=={1,4,6,7}
    parity=[]
    for a in range(2):
        for b in range(2):
            if gcd(gcd(a,b),2)>1 or a==b==0:continue
            rows=[]
            for n in range(2):
                for t in range(2):
                    if (81*a*n*(n-1)-b*(9*n*(t*t+3*t+3)+t**3))%2:continue
                    possible=[rho for rho in range(2) if (rho-a*a-a*b*(9*n-t-6)+b*b*(t*t+3*t+3))%2==0]
                    assert possible==[(a+b)%2]
                    Z=(b*(t+1)*(t+2)+a*(t+6-9*n))%2
                    if b:assert Z==0
                    rows.append([n,t,possible[0],Z])
            parity.append({'a_mod2':a,'b_mod2':b,'rows_n_t_rho_Z':rows})
    assert parity==cert['residue_tables']['parity_rows']
    assert all(r not in global_classes for r in (11%9,12%9))
    return {'rho_tuples':count,'global_mod9_classes':sorted(global_classes),'rho11_and12_excluded':True,
            'parity_cases':sum(len(x['rows_n_t_rho_Z']) for x in parity),
            'gcd_proof':'Bezout forces gcd|9; full mod9 table removes a second factor3. No prime bound is used.'}


def core_audit(cert):
    rows=cert['cube_core_tables']['prime3'];sizes=[]
    for d,row in enumerate(rows):
        formal=[[0,0]] if d==0 else [[i,j] for i in range(3) for j in range(3) if (i+j-d)%3==0]
        assert formal==row['formal_pairs']
        if d<=1:allowed=formal
        else:allowed=sorted({(2,(d-2)%3),((d-2)%3,2)})
        assert [list(x) for x in allowed]==row['allowed_pairs']
        assert row['proof_uses_exponent_cutoff'] is False
        sizes.append(len(allowed))
    assert sizes==[1,3,2,2,1,2]
    assert cert['cube_core_tables']['prime2'][0]['allowed_pairs']==[[0,1],[1,0]]
    count_rows=cert['cube_core_tables']['type_counts']
    for row in count_rows:
        b=row['b'];odd=row['a_odd'];d=val(b,3)
        assert b%2 or odd
        two=2 if b%2==0 else 3 if odd else 1
        oldtwo=3 if b%2==0 or odd else 1
        assert row['old_small_prime_types']==oldtwo*(3 if d else 1)
        assert row['new_small_prime_types']==two*sizes[d]
    assert len(count_rows)==18
    return {'N3_sizes':sizes,'coefficient_count_cases':len(count_rows),
            'unbounded_argument':'v3(V-U)=2 forces unequal pair(2,d+3f-2) when sum>4, and(2,2) when sum=4; modulo3 eliminates f.'}


def point_audit(cert):
    counts={'residual_examples':0,'integer_source_examples':0,'reverse_roots':0,'gcd_rejections':0,'rho_rejections':0}
    for category in('overinclusive_sextic_examples','integer_reconstruction_examples'):
        for row in cert['examples'][category]:
            a,b,rho=row['a'],row['b'],row['rho'];y=row['y'];Z=row['Z']
            assert y*y==F(a,b,rho)
            assert (a*a-b*b-rho)==b*Z and Z>0
            D=9*a*a-b*b;L=D-3*b*Z;U=row['U'];V=row['V']
            assert U*V==b*Z**3 and V-U==L and b*(U+V)==y
            g0=gcd(U,V)
            assert g0==row['common_factor'] and D**3%(g0*g0)==0 and gcd(g0,a)==1
            assert 9%gcd(g0,b)==0
            assert row['gcd_filter']==(gcd(a,rho)==gcd(a,3))
            assert row['rho_filter']==(rho%3==a*a%3 and (a%3!=0 or rho%9==6))
            counts['gcd_rejections']+=not row['gcd_filter']
            counts['rho_rejections']+=not row['rho_filter']
            C=(3*a+b)*(a+b)+a*Z
            roots=[]
            # Producer uses the sqrt formula. Here use the integral cover factors.
            for sign,T in((-1,Fraction(C-V,rho)),(1,Fraction(C+U,rho))):
                N=b*b*(T*T+3*T+3)+a*b*(T+6)-a*a+rho
                n=N/(9*a*b)
                assert 81*a*n*(n-1)==b*(9*n*(T*T+3*T+3)+T**3)
                assert rho==a*a+a*b*(9*n-T-6)-b*b*(T*T+3*T+3)
                if T.denominator==1:
                    assert (9*gcd(a,rho))%n.denominator==0
                roots.append({'sign':sign,'t':str(T),'n':str(n),'t_integer':T.denominator==1,'n_integer':n.denominator==1})
                counts['reverse_roots']+=1
            assert roots==row['roots']
            if category=='integer_reconstruction_examples':
                n=row['source_n'];t=row['source_t']
                assert row['source_r']==3*n+t
                assert any(Fraction(x['n'])==n and Fraction(x['t'])==t for x in roots)
                assert row['gcd_filter'] and row['rho_filter']
                assert rho%2==(a+b)%2
                d=val(b,3)
                if d<=3:assert t%3==0
                if 1<=d<=3:assert Z%3==0
                if d==0:assert Z%3==(-b)%3
                if b%2:assert Z%2==0
                pair=[val(U,3)%3,val(V,3)%3]
                assert pair==row['v3_core_pair'] and pair in cert['cube_core_tables']['prime3'][d]['allowed_pairs']
                if b%2==0:assert [val(U,2)%3,val(V,2)%3] in [[0,1],[1,0]]
                counts['integer_source_examples']+=1
            counts['residual_examples']+=1
    assert counts['residual_examples']==10 and counts['reverse_roots']==20
    assert counts['integer_source_examples']==6
    return counts


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp=HERE/'v20_residual_integrality_certificate.json'
    cert=json.loads(cp.read_text())
    assert cert['note_sha256']==sha(HERE/'v20_residual_integrality.md')
    result={'status':'PASS','date_jst':'2026-11-07','coefficient_identities':identities(),
        'residues':residue_audit(cert),'cube_cores':core_audit(cert),'reverse_reconstruction':point_audit(cert),
        'certificate_sha256':sha(cp),'note_sha256':sha(HERE/'v20_residual_integrality.md'),
        'verifier_sha256':sha(Path(__file__)),'producer_imported':False,'sympy_used':False,
        'scope':'Written universal proof plus exact independent arithmetic; no Lean or original-equation solution claim'}
    (HERE/'v20_residual_integrality_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
