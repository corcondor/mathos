#!/usr/bin/env python3
"""Independent review of the elliptic agent's rho<=10 certificate.

Does not import or modify that agent's code. The finite reconstruction uses
the integer-separation remainder expression for F and a different lower-bound
generation. SymPy separately checks the polynomial geometry identities.
"""
from fractions import Fraction
from hashlib import sha256
from math import gcd,isqrt
from pathlib import Path
import argparse
import json
import sympy as S


def algebra():
    a,b,r,x=S.symbols('a b rho x')
    F=4*a**6+(24*b*b-12*r)*a**4+(36*b**4+60*b*b*r+12*r*r)*a*a-3*b*b*r*r-4*r**3
    A=48*b*b*(9*r-b*b)
    B=1296*r*r*b*b-2880*r*b**4-128*b**6
    X=4*a*a+8*b*b-4*r
    C=-3*b*b*(72*a*a+b*b)
    D=2*b*b*(648*a**4+180*a*a*b*b-b**4)
    U=4*a*a-b*b-4*r
    identities={
        'first_curve_map':X**3+A*X+B-16*F,
        'first_curve_discriminant':-16*(4*A**3+27*B**2)+995328*r*b**4*(9*r+8*b*b)**3,
        'second_curve_map':U**3+C*U+D-16*F,
        'second_curve_discriminant':-16*(4*C**3+27*D**2)+995328*a*a*b**4*(3*a-b)**3*(3*a+b)**3,
        'second_c4':-48*C-144*b*b*(72*a*a+b*b),
        'quotient_discriminant':S.discriminant(4*x**3+(24*b*b-12*r)*x*x+(36*b**4+60*b*b*r+12*r*r)*x-3*b*b*r*r-4*r**3,x)+3888*r*b**4*(9*r+8*b*b)**3,
        'T_curve':(12*b*b)**3+A*12*b*b+B-(4*b*(9*r+8*b*b))**2,
        'T_tangent':3*(12*b*b)**2+A-12*b*(4*b*(9*r+8*b*b)),
        'T_flex':(x+12*b*b)**3+A*(x+12*b*b)+B-(4*b*(9*r+8*b*b)+6*b*x)**2-x**3,
        'S_curve':(3*b*b)**3+C*3*b*b+D-(4*b*(9*a*a-b*b))**2,
        'S_tangent':3*(3*b*b)**2+C+6*b*(4*b*(9*a*a-b*b)),
        'S_flex':(x+3*b*b)**3+C*(x+3*b*b)+D-(4*b*(9*a*a-b*b)-3*b*x)**2-x**3,
        'boundary':F.subs(r,a*a-b*b)-b*b*(9*a*a-b*b)**2,
        'remainder':F-(2*a**3+(6*b*b-3*r)*a)**2-3*r*(r+32*b*b)*a*a+r*r*(3*b*b+4*r),
    }
    for label,value in identities.items():
        assert S.expand(value)==0,label
    r0=a*a-b*b
    y0=b*(9*a*a-b*b)
    ts=[-2*(3*a+b)/(a+b),(3*a+b)/(a-b)]
    ns=[8*b*(3*a+b)/(9*(a+b)**2),(3*a+b)**2/(9*(a-b)**2)]
    for sign,t0,n0 in zip((-1,1),ts,ns):
        t=(2*a*(a*a+3*b*b)-r0*(3*b+2*a)+sign*y0)/(2*b*r0)
        assert S.factor(t-t0)==0
        n=(b*b*(t*t+3*t+3)+a*b*(t+6)-a*a+r0)/(9*a*b)
        assert S.factor(n-n0)==0
    return list(identities)


def value_from_remainder(a,b,r):
    q0=a*(2*a*a+6*b*b-3*r)
    return q0*q0+3*r*(r+32*b*b)*a*a-r*r*(3*b*b+4*r)


def main(source_dir,output):
    source=source_dir/'v19_elliptic_residual_checks.json'
    saved=json.loads(source.read_text())
    old=saved['certificate']
    B=[d for d in range(1,487) if 486%d==0]
    assert B==old['denominators']
    by_key={(row['b'],row['rho']):row for row in old['rows']}
    actual=[]
    rows=[]
    totals={'fibers':0,'mod5_blocked':0,'candidates':0,'square_tests':0}
    for rho in range(1,11):
        for b in B:
            roots=[s for s in range(1,b+1) if gcd(s,b)==1 and s*s%b==rho%b]
            if not roots:
                assert (b,rho) not in by_key
                continue
            stored=by_key[(b,rho)]
            assert sorted(r%b for r in roots)==stored['classes_mod_b']
            lower=max(b+1,(31*b+26)//27)
            upper=rho*rho+32*rho*b*b-1
            assert lower==stored['lower_a'] and upper==stored['upper_a']
            # Move the strict residual inequality into the lower endpoint.
            threshold=1377*rho-760*b*b
            if threshold>=0:
                lower=max(lower,isqrt(threshold//216)+1)
            blocked=rho%5==(b*b)%5
            assert blocked==stored['uniform_mod5_obstruction']
            totals['fibers']+=1
            totals['mod5_blocked']+=int(blocked)
            candidate_count=test_count=square_count=0
            for s in roots:
                first_k=-((s-lower)//b)
                last_k=(upper-s)//b
                for k in range(first_k,last_k+1):
                    a=s+b*k
                    assert a>=lower and a<=upper
                    assert gcd(a,b)==1 and (a*a-rho)%b==0
                    assert 1377*rho<216*a*a+760*b*b
                    candidate_count+=1
                    if blocked:
                        continue
                    test_count+=1
                    F=value_from_remainder(a,b,rho)
                    assert F>0
                    y=isqrt(F)
                    if y*y==F:
                        square_count+=1
                        branches=[]
                        for sign in (-1,1):
                            t=Fraction(a*(2*a*a+6*b*b)-rho*(3*b+2*a)+sign*y,2*b*rho)
                            n=(b*b*(t*t+3*t+3)+a*b*(t+6)-a*a+rho)/Fraction(9*a*b)
                            assert t.denominator!=1 or t<4 or n.denominator!=1 or n<104
                            branches.append({'sign':sign,'t':str(t),'n':str(n)})
                        actual.append({'a':a,'b':b,'rho':rho,'y':y,'roots':branches})
            assert candidate_count==stored['candidates']
            assert test_count==stored['square_tests']
            assert square_count==stored['squares']
            totals['candidates']+=candidate_count
            totals['square_tests']+=test_count
            rows.append({'b':b,'rho':rho,'candidate_count':candidate_count,'square_tests':test_count})
    assert totals=={'fibers':45,'mod5_blocked':11,'candidates':886683,'square_tests':775235}
    reduced_old=[]
    for point in old['points']:
        p={k:v for k,v in point.items() if k!='roots'}
        p['roots']=[{k:v for k,v in root.items() if k!='disposition'} for root in point['roots']]
        reduced_old.append(p)
    key=lambda p:(p['rho'],p['b'],p['a'])
    assert sorted(actual,key=key)==sorted(reduced_old,key=key)
    assert len(actual)==5
    mod5=[]
    for b in range(1,5):
        for a in range(5):
            residue=value_from_remainder(a,b,b*b)%5
            assert residue not in (0,1,4)
            mod5.append([a,b,residue])
    paths=[source_dir/'v19_elliptic_residual.md',source_dir/'v19_elliptic_residual_checks.py',source]
    result={'status':'PASS','scope':'rho<=10 coverage, five reconstructed points, uniform mod5, elliptic coefficient identities',
            'source_sha256':{p.name:sha256(p.read_bytes()).hexdigest() for p in paths},
            'finite_domain':totals,'all_five_points':actual,'mod5_complete_residue_classes':mod5,
            'symbolic_identity_checks':algebra(),'torsion_boundary_rational_reconstructions':True,
            'independence':'No source import; distinct remainder formula and lower-bound generation; SymPy coefficient algebra instead of producer sparse-polynomial class',
            'conclusion':'rho>=11 follows for both original k branches from the cited v17/v18 necessary conditions.',
            'not_reviewed':'External literature completeness/termination claims, optional PARI rank outputs, or new Lean formalization.'}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('all_five_points','mod5_complete_residue_classes')},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    here=Path(__file__).resolve().parent
    p.add_argument('--source-dir',type=Path,default=here)
    p.add_argument('--output',type=Path,default=here/'v19_elliptic_independent_audit.json')
    args=p.parse_args()
    main(args.source_dir,args.output)
