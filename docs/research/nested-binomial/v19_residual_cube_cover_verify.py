#!/usr/bin/env python3
"""Independent standard-library verifier of the residual 3-cover certificate.

Does not import or execute the producer and does not import SymPy. The finite
domain is regenerated with a different (coarser) bounding box; nonresidue
witnesses use the original sextic; finite-field tables use explicit point
enumeration. Polynomial identities use exact sparse coefficient arithmetic.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


HERE=Path(__file__).resolve().parent


def ring(n):
    class P:
        def __init__(self,x=0):
            if isinstance(x,P): x=x.d
            if isinstance(x,int): x={(0,)*n:x}
            self.d={e:c for e,c in x.items() if c}
        def __add__(self,x):
            d=self.d.copy()
            for e,c in P(x).d.items(): d[e]=d.get(e,0)+c
            return P(d)
        __radd__=__add__
        def __neg__(self): return P({e:-c for e,c in self.d.items()})
        def __sub__(self,x): return self+-P(x)
        def __rsub__(self,x): return P(x)+-self
        def __mul__(self,x):
            d={}
            for e,c in self.d.items():
                for f,v in P(x).d.items():
                    g=tuple(a+b for a,b in zip(e,f))
                    d[g]=d.get(g,0)+c*v
            return P(d)
        __rmul__=__mul__
        def __pow__(self,k):
            p=P(1)
            for _ in range(k):p=p*self
            return p
    return [P({tuple(int(j==i) for j in range(n)):1}) for i in range(n)]


def f(a,b,r):
    # Direct monomial expansion, rather than producer's grouped expression.
    return 4*a**6+24*b**2*a**4-12*r*a**4+36*b**4*a**2+60*b**2*r*a**2+12*r**2*a**2-3*b**2*r**2-4*r**3


def coefficient_audit():
    checks=[]
    def zero(name,poly):
        assert not poly.d,name
        checks.append(name)
    a,b,r=ring(3)
    zero("unscaled_factorization",f(a,b,r)-b*b*(6*a*a+2*b*b+3*r)**2-4*(a*a-b*b-r)**3)
    a,b,Z=ring(3)
    zero("normalized_factorization",f(a,b,a*a-b*b-b*Z)-b*b*((9*a*a-b*b-3*b*Z)**2+4*b*Z**3))
    n,t=ring(2)
    K=9*n*t*t+27*n*t+27*n+t**3
    zero("sign_elimination_identity",81*n*(n-1)*(t+1)*(t+2)+K*(t+6-9*n)-(t*t-9*n)*(9*n+t*t+6*t))
    a,b,al,be,ga,u,v=ring(7)
    H=be*v**3-al*u**3+3*ga*u*v-9*a*a+b*b
    R=ga**3-al*be*b*b
    L=9*a*a-b*b-3*ga*u*v
    zero("cover_ideal_membership",f(a,b,a*a-b*b-ga*u*v)-b*b*(al*u**3+be*v**3)**2+b*b*(L+be*v**3-al*u**3)*H-4*u**3*v**3*R)
    # Discriminant of g(z)=4z^3+cz^2+dz+e, and disc(g(x^2))=-256 e disc(g)^2.
    (s,)=ring(1)
    c,d,e=24-12*s,36+60*s+12*s*s,-3*s*s-4*s**3
    disc=c*c*d*d-16*d**3-4*c**3*e-432*e*e+72*c*d*e
    zero("cubic_discriminant",disc+3888*s*(9*s+8)**3)
    zero("sextic_discriminant_product",-256*e*disc*disc-3869835264*s**4*(4*s+3)*(9*s+8)**6)
    x,s=ring(2)
    zero("singular_s_zero",f(x,1,0)-4*x*x*(x*x+3)**2)
    # Clear denominators before all sparse coefficient comparisons.
    zero("singular_s_minus_8_9",729*(4*x**6+24*x**4+36*x*x)
         +972*8*x**4-4860*8*x*x+108*64*x*x-27*64+4*512
         -4*(3*x-1)**2*(3*x+1)**2*(9*x*x+80))
    zero("singular_s_minus_3_4",4*f(x,1,0)+36*x**4-180*x*x+27*x*x
         -x*x*(16*x**4+132*x*x-9))
    return checks


def hash_bytes(b): return hashlib.sha256(b).hexdigest()


def encode(x):
    return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()


def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def finite_domain_audit(cert):
    # Independent box: Z<=0 implies a<2b and Z>-2b. Then apply exact
    # original residual conditions, without producer's floor/isqrt endpoints.
    ds=[d for d in range(1,487) if 486%d==0]
    expected={}
    for b in ds:
        for a in range(b+1,2*b):
            if 27*a<31*b or gcd(a,b)!=1: continue
            for Z in range(-2*b,1):
                rho=a*a-b*b-b*Z
                if rho<=0 or 1377*rho>=216*a*a+760*b*b: continue
                expected.setdefault((a,b),[]).append(Z)
    got={(x['a'],x['b']):x for x in cert['sign_audit']['families']}
    assert set(expected)==set(got)
    count=0;hist=Counter();old=0;boundary=0
    for (a,b),Zs in expected.items():
        row=got[a,b]
        assert row['Z_min']==min(Zs)
        ws=row['negative_Z_witnesses']
        assert [w[0] for w in ws]==[Z for Z in Zs if Z<0]
        for Z,p,residue in ws:
            assert isprime(p) and p>=5
            rho=a*a-b*b-b*Z
            value=f(a,b,rho)
            # Independently regenerate the list of quadratic residues.
            assert value%p not in {j*j%p for j in range(p)}
            assert residue==value*pow(b*b,-1,p)%p
            # Good reduction of the actual elliptic quotient, not merely
            # a nonzero discriminant claimed by the producer.
            A=48*b*b*(9*rho-b*b)
            B=1296*rho*rho*b*b-2880*rho*b**4-128*b**6
            assert (4*A**3+27*B*B)%p!=0
            xx=(4*a*a+8*b*b-4*rho)%p
            assert (xx**3+A*xx+B)%p not in {j*j%p for j in range(p)}
            count+=1;hist[p]+=1;old+=(rho-b*b)%5==0
        assert Zs[-1]==0
        rho=a*a-b*b;y=b*(9*a*a-b*b)
        roots=[]
        for sign in (-1,1):
            t=Fraction(2*a*(a*a+3*b*b)-rho*(3*b+2*a)+sign*y,2*b*rho)
            n=(b*b*(t*t+3*t+3)+a*b*(t+6)-a*a+rho)/(9*a*b)
            roots.append({'sign':sign,'t':str(t),'n':str(n)})
            if sign<0: assert t<0
            else: assert t*t==9*n and n<=100
        assert roots==row['Z_zero_roots']
        boundary+=1
    assert count==6221 and boundary==102 and old==1252
    assert {str(k):v for k,v in sorted(hist.items())}==cert['sign_audit']['witness_prime_histogram']
    return {'coefficient_families':len(got),'negative_Z_cases':count,'boundary_cases':boundary,
            'prior_mod5_exclusions':old,'all_negative_cases_have_good_reduction_nonresidue_witness':True,
            'largest_prime':max(hist),'domain_generation':'coarser independent box a<2b and -2b<Z<=0, exact residual inequalities'}


def local_table_audit(tables):
    fibers=0;good_count=0
    for row in tables['rows']:
        p=row['prime'];assert isprime(p)
        assert [x['s'] for x in row['fibers']]==list(range(p))
        empty=[]
        for rr in row['fibers']:
            s=rr['s'];A=48*(9*s-1)%p;B=(1296*s*s-2880*s-128)%p
            # Explicitly enumerate all affine E(Fp) points; no Legendre
            # symbol, producer group-law code, or producer imports.
            points={(x,y) for x in range(p) for y in range(p) if (y*y-x**3-A*x-B)%p==0}
            allowed=sorted({a*a%p for a in range(p)
                if any(((4*a*a+8-4*s)%p,y) in points for y in range(p))})
            assert allowed==rr['allowed_a2_over_b2']
            if not allowed:empty.append(s)
            assert len(points)+1==rr['elliptic_point_count_with_infinity']
            good=(4*A**3+27*B*B)%p!=0
            assert good==rr['elliptic_good_reduction']
            if good:
                x,y=12%p,4*(9*s+8)%p
                assert (x,y) in points and y!=0
                slope=(3*x*x+A)*pow(2*y,-1,p)%p
                xd=(slope*slope-2*x)%p
                yd=(slope*(x-xd)-y)%p
                assert (xd,yd)==(x,(-y)%p)
                assert rr['known_T_order']==3
                assert (len(points)+1)%3==0
                good_count+=1
            else: assert rr['known_T_order'] is None
            fibers+=1
        assert empty==row['empty_affine_genus_two_fibers']==([1] if p==5 else [])
    assert fibers==496
    return {'complete_fibers':fibers,'good_elliptic_fibers':good_count,
            'method':'enumerate all x,y in Fp and reconstruct admissible square x-lifts',
            'group_check':'explicit doubling of T equals -T at every good-reduction fiber'}


def valuation(n,p):
    e=0
    while n%p==0:n//=p;e+=1
    return e


def example_audit(cert):
    counts=[]
    for x in cert['examples']:
        a,b,rho=x['a'],x['b'],x['rho'];U,V=x['U'],x['V'];Z=x['Z']
        assert x['y']**2==f(a,b,rho)
        assert x['y']==b*(U+V)
        assert b*Z==a*a-b*b-rho
        D=9*a*a-b*b
        assert U*V==b*Z**3 and V-U==D-3*b*Z
        assert U>0 and V>0 and b*(Z**3+3*Z)>=D+1
        primes=x['support'];m=b*D
        for p in primes:
            assert isprime(p) and m%p==0
            while m%p==0:m//=p
        assert m==1
        # Independent enumeration orders beta first, then solve the alpha
        # exponents. Canonical sorting by alpha recovers producer's order.
        rows=[]
        for bs in itertools.product(range(3),repeat=len(primes)):
            al=be=ga=1
            ae=[]
            for p,j in zip(primes,bs):
                e=valuation(b,p);i=(-j-2*e)%3
                al*=p**i;be*=p**j;ga*=p**((i+j+2*e)//3);ae.append(i)
            assert ga**3==al*be*b*b
            rows.append((tuple(ae),[al,be,ga]))
        rows=[row for _,row in sorted(rows)]
        assert len(rows)==3**len(primes)==x['cover_count']
        assert hash_bytes(encode(rows))==x['cover_coefficients_sha256']
        al,be,ga=x['alpha'],x['beta'],x['gamma'];u,v=x['u'],x['v']
        assert [al,be,ga] in rows and U==al*u**3 and V==be*v**3
        assert b*Z==ga*u*v and rho==a*a-b*b-ga*u*v
        assert be*v**3-al*u**3+3*ga*u*v==D
        counts.append(len(rows))
    return {'examples':len(counts),'cube_class_counts':counts,
            'all_residual_and_recovery_identities_checked':True,
            'original_binomial_solution_claimed':False}


def main():
    cp=HERE/'v19_residual_cube_cover_certificate.json'
    tp=HERE/'v19_residual_cube_cover_local_tables.json'
    cert=json.loads(cp.read_text());tables=json.loads(tp.read_text())
    assert hash_bytes(tp.read_bytes())==cert['local_tables_sha256']
    report={'status':'PASS','date_jst':'2026-11-07',
        'scope':'independent polynomial, finite-field, and reconstruction audit; no Lean',
        'coefficient_identities':coefficient_audit(),
        'finite_domain':finite_domain_audit(cert),
        'finite_fields':local_table_audit(tables),
        'examples':example_audit(cert),
        'certificate_sha256':hash_bytes(cp.read_bytes()),
        'local_tables_sha256':hash_bytes(tp.read_bytes()),
        'verifier_sha256':hash_bytes(Path(__file__).read_bytes()),
        'producer_imported':False,'sympy_used':False,
        'sign_status':'Z>0 is already implied by v17 via the exact sign identity, not a new original exclusion.'}
    (HERE/'v19_residual_cube_cover_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__': main()
