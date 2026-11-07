#!/usr/bin/env python3
"""Independent audit: rescale all ratios to M=6 and eliminate raw h,J.
Does not import or invoke v17_square_root_gap.py. Python standard library.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

# Four-variable integer polynomials. Symbol meanings change between checks.
ZERO = (0, 0, 0, 0)
def const(c):
    return {ZERO: c} if c else {}
def var(i):
    e = [0]*4; e[i] = 1
    return {tuple(e): 1}
def plus(*ps):
    d = Counter()
    for p in ps:
        for e,c in p.items(): d[e] += c
    return {e:c for e,c in d.items() if c}
def times(p,q):
    d = Counter()
    for e,c in p.items():
        for f,b in q.items(): d[tuple(x+y for x,y in zip(e,f))] += c*b
    return {e:c for e,c in d.items() if c}
def scale(c,p): return {e:c*b for e,b in p.items() if c*b}
def power(p,k):
    out = const(1)
    for _ in range(k): out = times(out,p)
    return out
def coeff(p,i,k):
    d = {}
    for e,c in p.items():
        if e[i] != k: continue
        f = list(e); f[i] = 0; d[tuple(f)] = c
    return d
def ev(p,values):
    s=0
    for e,c in p.items():
        term=c
        for v,a in zip(values,e): term*=v**a
        s+=term
    return s

def algebra_checks():
    h,M,J,t = [var(i) for i in range(4)]
    U = plus(power(t,2),scale(3,t),const(3))
    numerator = plus(J,scale(-1,power(h,2)),scale(81,times(times(M,h),plus(t,const(6)))),scale(6561,times(power(M,2),U)))
    raw = plus(power(numerator,2),scale(-729,times(times(M,plus(h,scale(9,times(M,U)))),numerator)),scale(-531441,times(times(power(M,3),h),power(t,3))))
    assert all(e[3]<=2 for e in raw)
    raw_coeff = [coeff(raw,3,k) for k in range(3)]
    # Build the normalized polynomial afresh from the defining h-equation.
    a,b,j,t = [var(i) for i in range(4)]
    U = plus(power(t,2),scale(3,t),const(3))
    N = plus(j,scale(-1,power(a,2)),times(times(a,b),plus(t,const(6))),times(power(b,2),U))
    normalized = plus(power(N,2),scale(-1,times(plus(scale(9,times(a,b)),times(power(b,2),U)),N)),scale(-1,times(times(a,power(b,3)),power(t,3))))
    assert all(e[3]<=2 for e in normalized)
    C,B,A = [coeff(normalized,3,k) for k in range(3)]
    discriminant = plus(power(B,2),scale(-4,times(A,C)))
    assert all(e[1]>=2 for e in discriminant)
    F={ (e[0],e[1]-2,e[2],e[3]): c for e,c in discriminant.items() }
    X=plus(scale(4,power(a,2)),scale(-1,power(b,2)),scale(-4,j))
    EC_A=scale(-3,times(power(b,2),plus(scale(72,power(a,2)),power(b,2))))
    EC_B=scale(2,times(power(b,2),plus(scale(648,power(a,4)),scale(180,times(power(a,2),power(b,2))),scale(-1,power(b,4)))))
    assert not plus(scale(16,F),scale(-1,power(X,3)),scale(-1,times(EC_A,X)),scale(-1,EC_B))
    EC_disc=scale(-16,plus(scale(4,power(EC_A,3)),scale(27,power(EC_B,2))))
    factored=scale(-995328,times(times(power(a,2),power(b,4)),times(power(plus(scale(3,a),scale(-1,b)),3),power(plus(scale(3,a),b),3))))
    assert EC_disc==factored
    singular={}
    for e,c in F.items():
        exponent=e[2]
        singular[exponent]=singular.get(exponent,0)+c*3**e[1]
    # (j+8)^2(49-4j) = -4j^3-15j^2+528j+3136.
    assert {k:v for k,v in singular.items() if v}=={3:-4,2:-15,1:528,0:3136}
    # The square-root boundary, with n=s^2 and t=3s.
    s=var(0); nn=power(s,2); tt=scale(3,s)
    boundary=plus(times(plus(scale(9,power(tt,2)),scale(27,tt),const(27)),nn),power(tt,3),scale(-1,times(nn,plus(scale(81,plus(nn,const(-1))),scale(108,plus(s,const(1)))))))
    assert not boundary
    n,u=var(0),var(1)
    E=plus(times(plus(scale(9,power(u,2)),scale(-27,u),const(27)),n),power(plus(u,const(-3)),3),scale(-93,times(n,plus(n,const(-1)))))
    threeB=plus(times(n,plus(const(360),scale(-50,u))),scale(-27,power(u,2)),scale(81,u),const(-81))
    factored_difference=times(plus(scale(9,n),u),plus(scale(31,n),scale(-3,power(u,2))))
    assert not plus(threeB,scale(-3,E),scale(-1,factored_difference))
    assert Fraction(93,4)>23 and 120-Fraction(50,3)*27<0
    Fq=Fraction
    assert Fq(2187,68)*(24*4+Fq(28,27)*16)==Fq(61560,17)
    assert Fq(2187,68)*Fq(8,6561)*4==Fq(8,51)
    assert Fq(61560,17*81**2)==Fq(760,1377)
    assert Fq(8,51)==Fq(216,1377)
    return raw_coeff, {
        'raw_elimination': 'Constructed directly from the raw J definition and h-quadratic; all t^4,t^3 terms cancel.',
        'normalized_elimination': 'Constructed directly from residual n numerator and h/(81M)=a/b; all t^4,t^3 terms cancel.',
        'elliptic_coordinate_identity': 'all coefficients zero',
        'elliptic_discriminant_factorization': 'exact coefficient equality',
        'singular_family_factorization': 'F(1,3,j)=(j+8)^2*(49-4*j)',
        'boundary_h_ratio': 'all coefficients zero',
        'stronger_shifted_gap': '3*(B-E)=(9*n+u)*(31*n-3*u^2), all coefficients zero; h>=93M and h<4Mt force t>=24,u>=27, hence B<0 in the excluded region.',
        'residual_bound_constants': 'exact rational equality',
    }

def pascal_table(p):
    rows=[[1]]
    for n in range(1,p):
        prev=rows[-1]
        rows.append([1]+[prev[k-1]+prev[k] for k in range(1,n)]+[1])
    return [[v%p for v in row] for row in rows]
def lucas(N,K,p):
    T=pascal_table(p); ans=1
    while N or K:
        n,k=N%p,K%p
        if k>n:return 0
        ans=ans*T[n][k]%p
        N//=p;K//=p
    return ans

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,default=Path(__file__).with_name('v17_square_root_gap_results.json'))
    ap.add_argument('--generator',type=Path,default=Path(__file__).with_name('v17_square_root_gap.py'))
    ap.add_argument('--note',type=Path,default=Path(__file__).with_name('v17_square_root_gap.md'))
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args()
    source=json.loads(args.input.read_text())
    assert source['source_sha256']==hashlib.sha256(args.generator.read_bytes()).hexdigest()
    assert source['proof_note_sha256']==hashlib.sha256(args.note.read_bytes()).hexdigest()
    raw_coeff, algebra=algebra_checks()
    expected_families={(f['a'],f['b']):f for f in source['families']}
    mapped=set(); totals=Counter(); low=Counter(); integer_t=[]; necessary=[]; family_checks=[]
    for H in range(1,558):
        G=gcd(H,486); a,b=H//G,486//G
        assert (a,b) not in mapped
        mapped.add((a,b)); totals['coefficient_pairs']+=1
        if H<=486:low['coefficient_pairs']+=1
        expected=expected_families[(a,b)]
        step=486*G
        first=H*H%step or step
        maximum=(8*H*H+184680*36-1)//51
        assert first%(G*G)==0
        assert expected['first_j']==first//(G*G)
        assert expected['maximum_j']==maximum//(G*G)
        assert expected['step']==b
        classes=[]; squared=[]
        for JR in range(first,maximum+1,step):
            assert JR%(G*G)==0
            j=JR//(G*G)
            totals['residual_values']+=1
            if H<=486:low['residual_values']+=1
            C,B,A=[ev(p,(H,6,JR,0)) for p in raw_coeff]
            assert A>0
            d=B*B-4*A*C
            if d<0:
                classes.append('-');continue
            q=isqrt(d)
            if q*q!=d:
                classes.append('.');continue
            classes.append('s');totals['square_discriminants']+=1
            if H<=486:low['square_discriminants']+=1
            square_scale=G**4*b
            assert q%square_scale==0
            y=q//square_scale
            roots=sorted({Fraction(-B-q,2*A),Fraction(-B+q,2*A)})
            root_records=[]
            for root in roots:
                rr={'t_numerator':root.numerator,'t_denominator':root.denominator}
                if root.denominator!=1:
                    rr['disposition']='nonintegral_t'
                elif root<4:
                    rr['disposition']='t_below_4'
                else:
                    t=root.numerator;totals['integer_t_ge_4']+=1
                    if H<=486:low['integer_t_ge_4']+=1
                    D=9*t*t+27*t+27;P=H+6*D
                    dn=P*P+24*H*t**3;sn=isqrt(dn)
                    assert sn*sn==dn
                    n=Fraction(P+sn,2*H)
                    rr.update(n_numerator=n.numerator,n_denominator=n.denominator)
                    integer_t.append({'a':a,'b':b,'j':j,'t':t,'n_numerator':n.numerator,'n_denominator':n.denominator})
                    if n.denominator!=1:
                        rr['disposition']='nonintegral_n'
                    elif n<104:
                        rr['disposition']='n_below_104'
                    else:
                        n=n.numerator;totals['integer_n_ge_104']+=1
                        if H<=486:low['integer_n_ge_104']+=1
                        M=gcd(n,3)*gcd(n-1,6);Q=n*(n-1)//M;r=3*n+t
                        assert (81*M)%b==0
                        h=(81*M*a)//b
                        assert 3*t<n and r**3%Q==0
                        assert h*n*(n-1)==M*(D*n+t**3)
                        assert t*t==9*n
                        totals['restored_necessary_pairs']+=1;totals['equality_pairs']+=1
                        rr['disposition']='equality_candidate'
                        necessary.append({'a':a,'b':b,'j':j,'t':t,'n':n,'r':r,'M':M,'h':h,'delta':Q//gcd(Q,r*r)})
                root_records.append(rr)
            squared.append({'j':j,'F':y*y,'sqrt_F':y,'roots':root_records})
        assert ''.join(classes)==expected['classifications'],(a,b,'classes')
        assert len(classes)==expected['count']
        assert squared==expected['square_records'],(a,b,'square records')
        family_checks.append({'rescaled_h':H,'g':G,'a':a,'b':b,'residual_count':len(classes),'square_count':len(squared),'all_dispositions_and_roots_match':True})
    assert mapped==set(expected_families)
    expected_domain={(a,b) for b in range(1,487) if 486%b==0 for a in range(1,558) if gcd(a,b)==1 and 27*a<31*b}
    assert mapped==expected_domain
    key=lambda x:(x['a'],x['b'],x['j'],x['t'])
    assert sorted(integer_t,key=key)==sorted(source['integer_t_records'],key=key)
    ss=[d+1 for d in range(1,649) if (324*gcd(d,2))%d==0 and (d+1)**2>=104]
    assert ss==source['elementary_equality_s']
    assert sorted((p['n'],p['r']) for p in necessary)==[(s*s,3*s*(s+1)) for s in ss]
    source_pairs={p['n']:p for p in source['necessary_pairs']}
    both_zero=0;witnesses=[]
    for pair in necessary:
        n,r=pair['n'],pair['r'];old=source_pairs[n]
        for field,value in pair.items():assert old[field]==value
        A=n*(n-1)*(n-2)//6
        for witness in old['witnesses']:
            p=witness['prime'];k=r if witness['branch']=='r' else A-r
            assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
            left=lucas(A,k,p);inner=lucas(n*n,(n-3)**2,p);square=k*k%p;right=(inner+square)%p
            assert witness==dict(branch=witness['branch'],k=k,prime=p,left=left,inner=inner,square=square,right=right)
            assert left!=right
            both_zero+=left==0 and inner==0
            totals['original_branch_exclusions']+=1
            witnesses.append(dict(n=n,**witness))
    assert both_zero==source['both_binomials_zero_witnesses']==24
    assert max(w['prime'] for w in witnesses)==source['max_witness_prime']==13
    assert {k:totals[k] for k in source['statistics']}==source['statistics']
    assert {k:low[k] for k in source['low_h_subdomain']}==source['low_h_subdomain']
    assert not source['original_equation_survivors']
    assert max(p['delta'] for p in necessary)==6
    singular=[(j,(j+8)**2*(49-4*j)) for j in range(1,6) if j%3==1]
    assert all(isqrt(f)**2!=f for j,f in singular)
    report={'status':'PASS','method':'Rescale every original M|6 to M=6, H=6h/M in 1..557; enumerate raw residual JR modulo 486*gcd(H,486); raw elimination quadratic for t; original h-quadratic for n. Generator not imported or executed.',
      'algebra':algebra,'statistics':dict(totals),'low_h_subdomain':{k:low[k] for k in source['low_h_subdomain']},'families':family_checks,
      'integer_t_records':sorted(integer_t,key=key),'necessary_pairs':sorted(necessary,key=lambda x:x['n']),
      'elementary_equality_s':ss,'original_binomial_witnesses':sorted(witnesses,key=lambda x:(x['n'],x['branch'])),
      'singular_pair':{'a':1,'b':3,'residual_values_and_F':singular,'integer_points':[]},
      'stronger_original_equation_consequence':'No original solution has h/M<93, because the coefficient enumeration imposed no t^2<=9n filter and all 13 reconstructed pairs have original-equation witnesses.',
      'stronger_shifted_gap_consequence':'Every original solution has (t+3)^2>31*n/3, by the audited exact difference factorization and h>=93M.',
      'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),'generator_sha256':source['source_sha256'],'proof_note_sha256':source['proof_note_sha256'],
      'auditor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'new_lean_execution':False,'new_deepseek_api_calls':0,'external_peer_review':False,'universal_scope_boundary':'Written v16 and v17 inequalities establish completeness of this finite audit. No claim to solve the whole branch or original four-variable equation.'}
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','statistics':dict(totals),'low_h_subdomain':dict(low),'algebra':algebra,'both_binomials_zero':both_zero,'input_sha256':report['input_sha256'],'output_bytes':args.output.stat().st_size},indent=2))

if __name__=='__main__':main()
