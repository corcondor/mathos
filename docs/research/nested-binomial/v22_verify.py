#!/usr/bin/env python3
"""v22 exact integer check, no external modules.

Complete n-range audit on n=104..5000, 3*sqrt(n)<t<n/3, b|486;
and eight saved v21 reconstructed points (some outside that n-range).
The mathematical proof of unbounded claims is in v22_theorems_ja.md.
"""
import json
from math import gcd, isqrt
from pathlib import Path

ROOT=Path(__file__).parent
DIVISORS_486={v for v in range(1,487) if 486%v==0}


def factor(n):
    assert n>=1
    d={}
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p;e+=1
            d[p]=e
        p+=1 if p==2 else 2
    if n>1:
        d[n]=d.get(n,0)+1
    return d


def core(n):
    k=1; c=1
    for p,e in factor(n).items():
        k *= p**(e%3)
        c *= p**(e//3)
    assert k*c**3==n
    return k,c


def row_from_n_t(n,t):
    q=t*t+3*t+3
    H=9*n*q+t*t*t
    D=81*n*(n-1)
    g=gcd(H,D)
    a,b=H//g,D//g
    rho=a*a+a*b*(9*n-t-6)-b*b*q
    M=gcd(n,3)*gcd(n-1,6)
    Q=n*(n-1)//M
    r=3*n+t
    delta=Q//gcd(Q,r*r)
    return dict(n=n,t=t,a=a,b=b,rho=rho,M=M,Q=Q,r=r,delta=delta)


def check(row):
    n,t,a,b,rho,M,Q,r,delta=[row[k] for k in ('n','t','a','b','rho','M','Q','r','delta')]
    assert b in DIVISORS_486 and gcd(a,b)==1
    assert 81*a*n*(n-1)==b*(9*n*(t*t+3*t+3)+t**3)
    assert n>=104 and t*t>9*n and 3*t<n
    assert rho>0 and 27*a>=31*b
    assert (4*Q)%(delta**3)==0
    assert (n%2==1 or b%2==1) or (Q%(delta**3)==0 or b%2==0)
    if n%2 or b%2: assert Q%(delta**3)==0

    # Additional algebraic bridge: δ|c and c|ℒ, h|81W².
    d=gcd(Q,r*r)
    K=r*r//d; C=M*delta; g=gcd(C,K)
    assert gcd(delta,K)==1 and g==gcd(M,K) and M%g==0
    c=C//g; h=K//g
    assert c%delta==0 and gcd(c,h)==1

    znum=a*a-b*b-rho
    assert znum%b==0
    Z=znum//b
    assert Z>0
    L=6*a*a+2*b*b+3*rho
    y2=b*b*L*L+4*znum**3
    y=isqrt(y2)
    assert y*y==y2 and y%b==0
    U,V=(y//b-L)//2,(y//b+L)//2
    assert U>0 and V>0 and U*V==b*Z**3
    X=t*t-9*n; Y=t*t+6*t+9*n
    assert Z*81*n*(n-1)==b*X*Y
    assert U*729*n*n*(n-1)==b*b*X**3
    assert V*729*n*(n-1)**2==b*b*Y**3
    assert U*n*Y**3==V*(n-1)*X**3

    minus=Z-2*b-6*a;plus=Z-2*b+6*a
    assert minus==t*(a+b*(t+3))-9*a*n
    assert plus==(t+3)*(a+b*t)-9*a*(n-1)
    ell=minus*plus*b*b
    aa=a*a
    assert ell==(aa-6*a*b-rho-3*b*b)*(aa+6*a*b-rho-3*b*b)
    assert ell%c==0
    W=5*aa+4*rho+3*b*b
    assert (81*W*W)%h==0

    dn=dm=1
    for p,e in factor(delta).items():
        if n%p==0:
            dn*=p**e
        else:
            assert (n-1)%p==0
            dm*=p**e
    assert dn*dm==delta and gcd(dn,dm)==1
    epsilon=2 if n%2==0 and b%2==0 else 1
    assert (epsilon*minus)%dn==0 and plus%dm==0
    assert (epsilon*minus*plus)%delta==0

    du,x=core(n);dv,yc=core(n-1)
    assert du*x**3-dv*yc**3==1
    ap=3*a+b;am=3*a-b
    assert ap>0 and am>0
    for p in factor(du):
        assert p in (2,3) or ap%p==0
    for p in factor(dv):
        assert p in (2,3) or am%p==0
    for p,e in factor(n).items():
        if p>=5 and e%3: assert ap%p==0
    for p,e in factor(n-1).items():
        if p>=5 and e%3: assert am%p==0
    assert all(e<=2 for e in factor(du).values())
    assert all(e<=2 for e in factor(dv).values())
    return dict(n=n,t=t,a=a,b=b,rho=rho,delta=delta,
                Q=Q,delta_cube_div_Q=(Q%(delta**3)==0),
                dn=dn,dm=dm,epsilon=epsilon,L_minus=minus,L_plus=plus,
                d_plus=du,x=x,d_minus=dv,y=yc)


def enumerate_band(nmax=5000):
    rows=[]
    count_t=0
    for n in range(104,nmax+1):
        for t in range(isqrt(9*n)+1,(n-1)//3+1):
            count_t+=1
            row=row_from_n_t(n,t)
            if row['b'] in DIVISORS_486:
                rows.append(check(row))
    return rows,count_t


if __name__=='__main__':
    rows,attempts=enumerate_band()
    assert len(rows)==10, len(rows)
    exception=[r for r in rows if not r['delta_cube_div_Q']]
    assert [(r['n'],r['t'],r['b']) for r in exception]==[(400,130,486),(2058,371,486)],exception
    prior=json.loads((ROOT/'v21_residual_certificate.json').read_text())['points']
    saved=[]
    for item in prior:
        row=row_from_n_t(item['n'],item['t'])
        assert all(row[k]==item[k] for k in ('n','t','a','b','rho','delta'))
        saved.append(check(row))
    uniqueness={(p['n'],p['t']) for p in rows+saved}
    certificate={'status':'PASS','scope':'complete n=104..5000 and strict 3sqrt(n)<t<n/3 with b|486; plus v21 eight archived points',
        'all_n_t_pairs':attempts,'band_hits':len(rows),'v21_retested':len(saved),
        'distinct_points':len(uniqueness),'Q_exception_points':exception,
        'band_rows':rows,'v21_rows':saved,
        'unbounded_proof':'not numerical; see v22_theorems_ja.md and Bennett (2004) Theorem 1.1'}
    (ROOT/'v22_certificate.json').write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+'\n')
    print('PASS', 'pairs',attempts,'band_hits',len(rows),'prior',len(saved),
          'distinct',len(uniqueness),'strict δ³|Q exceptions',len(exception))
