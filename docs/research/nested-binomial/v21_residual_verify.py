#!/usr/bin/env python3
"""Independent v21 audit: residue-class iterator, factorized sextic,
integer n-discriminant, sparse-polynomial coefficient identities, Lucas CRT.
Does NOT import v21_residual_audit.py.
"""
from math import comb, gcd, isqrt
from pathlib import Path
import json


def poly_const(c, variables):
    return {(0,)*variables: c} if c else {}


def add(*ps):
    ans = {}
    for p in ps:
        for e, v in p.items():
            ans[e] = ans.get(e, 0)+v
            if ans[e] == 0:
                del ans[e]
    return ans


def neg(p):
    return {e:-v for e,v in p.items()}


def scale(p, k):
    return {e:v*k for e,v in p.items() if v*k}


def mul(p,q):
    z = {}
    for ep,vp in p.items():
        for eq,vq in q.items():
            e=tuple(i+j for i,j in zip(ep,eq))
            z[e] = z.get(e,0)+vp*vq
    return {e:v for e,v in z.items() if v}


def power(p,k):
    z=poly_const(1,len(next(iter(p))) if p else 2)
    for _ in range(k):
        z=mul(z,p)
    return z


def identities():
    # Direct elimination certificate. Variables are (n,t); denominators
    # cleared before any cancellation, no bounded random spot-checks.
    n={(1,0):1};t={(0,1):1}; c=lambda x: poly_const(x,2)
    q=add(power(t,2),scale(t,3),c(3))
    e=mul(n,add(n,c(-1)))
    H=add(scale(mul(n,q),9),power(t,3))
    den=scale(e,81)
    D=add(power(H,2),mul(H,mul(den,add(scale(n,9),neg(t),c(-6)))),neg(mul(q,power(den,2))))
    hn=power(H,2);dd=power(den,2)
    left=mul(add(hn,scale(mul(H,den),-6),neg(D),scale(dd,-3)),
             add(hn,scale(mul(H,den),6),neg(D),scale(dd,-3)))
    middle=add(scale(power(H,4),13),scale(mul(hn,D),-17),
               scale(mul(hn,dd),-6),scale(power(D,2),4),
               scale(mul(D,dd),15),scale(power(dd,2),9))
    w=add(scale(hn,5),scale(D,4),scale(dd,3))
    r=add(scale(n,3),t)
    expr=add(mul(left,power(r,4)),
             scale(mul(middle,mul(power(r,2),e)),-18),
             scale(mul(power(w,2),power(e,2)),81))
    assert not expr, f'quadratic polynomial has {len(expr)} nonzero coefficients'

    # Discriminant certificate in variables (a,b,rho).
    a={(1,0,0):1};b={(0,1,0):1};s={(0,0,1):1}
    a2=power(a,2);b2=power(b,2);s2=power(s,2)
    L=mul(add(a2,scale(mul(a,b),-6),neg(s),scale(b2,-3)),
          add(a2,scale(mul(a,b),6),neg(s),scale(b2,-3)))
    T=add(scale(power(a,4),13),scale(mul(a2,s),-17),
          scale(mul(a2,b2),-6),scale(s2,4),scale(mul(s,b2),15),
          scale(power(b,4),9))
    W=add(scale(a2,5),scale(s,4),scale(b2,3))
    F=add(scale(power(a,6),4),
          mul(add(scale(b2,24),scale(s,-12)),power(a,4)),
          mul(add(scale(power(b,4),36),scale(mul(b2,s),60),scale(s2,12)),a2),
          scale(mul(b2,s2),-3),scale(power(s,3),-4))
    delta=add(scale(power(T,2),324),scale(mul(L,power(W,2)),-324),
              scale(mul(a2,F),-11664))
    assert not delta, f'discriminant polynomial has {len(delta)} nonzero coefficients'
    return {'quadratic_coefficient_identity':True,'discriminant_identity':True}


def lucas_prime(n, r, p):
    if r < 0 or r > n:
        return 0
    acc=1
    while r > 0 or n > 0:
        a=n%p; b=r%p
        if a < b:
            return 0
        # Multiplicative formula instead of math.comb on each digit.
        up=dn=1
        for j in range(1,b+1):
            up=up*(a-j+1)%p
            dn=dn*j%p
        acc=acc*up*pow(dn,-1,p)%p
        n//=p;r//=p
    return acc


def independent_scan(bound=4096):
    bs=[b for b in range(1,487) if 486%b==0]
    points=[]
    totals=dict(primitive_filtered=0,residual_squares=0,
                positive_integer_t=0,integer_n=0,branch_points=0)
    # Important: outer-loop order and residue enumeration differ from producer.
    for b in bs:
        b2=b*b
        for rho in range(13,bound+1):
            if rho%9 not in {1,4,6,7}:
                continue
            # Since 0 < ln(rho) < bit_length(rho), this is safe.
            amax=isqrt(152*rho*(rho.bit_length()))
            valid_residues=[r for r in range(b) if r*r% b == rho%b]
            for rem in valid_residues:
                start=b+1+((rem-(b+1))%b)
                for a in range(start,amax+1,b):
                    if (gcd(a,b)!=1 or gcd(a,rho)!=gcd(a,3)
                        or 27*a<31*b or (a+b-rho)%2):
                        continue
                    a2=a*a
                    if a2<=b2+rho or 1377*rho>=216*a2+760*b2:
                        continue
                    totals['primitive_filtered']+=1
                    z=a2-b2-rho
                    L=6*a2+2*b2+3*rho
                    f=b2*L*L+4*z*z*z
                    if f<0:
                        continue
                    y=isqrt(f)
                    if y*y!=f:
                        continue
                    totals['residual_squares']+=1
                    for root in (y, -y):
                        numer=2*a*(a2+3*b2)-rho*(3*b+2*a)+root
                        denom=2*b*rho
                        t,rem=divmod(numer,denom)
                        if rem or t<=0:
                            continue
                        totals['positive_integer_t']+=1
                        q=t*t+3*t+3
                        # Entirely different n reconstruction: a quadratic
                        # discriminant and an integer square test.
                        C=81*a+9*b*q
                        disc=C*C+324*a*b*t**3
                        nd=isqrt(disc)
                        if nd*nd!=disc:
                            continue
                        n,remainder=divmod(C+nd,162*a)
                        if remainder:
                            continue
                        assert 81*a*n*(n-1)==b*(9*n*q+t**3)
                        assert rho==a2+a*b*(9*n-t-6)-b2*q
                        totals['integer_n']+=1
                        r=3*n+t
                        if n<104 or t*t<=9*n or 3*r>=10*n:
                            continue
                        totals['branch_points']+=1
                        A=n*(n-1)*(n-2)//6
                        violations={}
                        for key,k in (("k=r",r),("k=A-r",A-r)):
                            p=next(p for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47)
                                   if (lucas_prime(A,r,p)-lucas_prime(n*n,6*n-9,p)-k*k)%p)
                            violations[key]=p
                        M=gcd(n,3)*gcd(n-1,6)
                        Q=n*(n-1)//M
                        de=Q//gcd(Q,r*r)
                        points.append({'a':a,'b':b,'rho':rho,'n':n,'t':t,
                                       'delta':de,'witnesses':violations})
    return totals,sorted(points,key=lambda p:(p['rho'],p['a'],p['b']))


if __name__=='__main__':
    base=Path(__file__).parent
    cert=json.loads((base/'v21_residual_certificate.json').read_text())
    proofs=identities()
    counts,points=independent_scan(cert['bound'])
    assert counts=={k:v for k,v in cert['counts'].items() if k in counts},(counts,cert['counts'])
    assert points==cert['points'],(points,cert['points'])
    assert len(points)==8
    print(json.dumps(dict(status='PASS', identities=proofs,
                          counts=counts, valid_points=points,
                          conclusion='No original solution with 13<=rho<=4096'),indent=2))
