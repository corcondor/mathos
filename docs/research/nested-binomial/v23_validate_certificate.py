#!/usr/bin/env python3
"""v23: exact small-final-candidate validation and cross-algorithm certificate.

No floating point, external packages, or reliance on enumeration implementation.
Full-domain completeness relies on two independently authored C++ enumerators.
"""
import json
from math import gcd, isqrt, comb
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
PRODUCER = [
    'v23_residual_extension_4097_8192.log',
    'v23_residual_extension_8193_16384.log',
    'v23_residual_extension_16385_24576.log',
    'v23_residual_extension_24577_32768.log',
]
PATTERN = re.compile(r'^POINT rho=(\d+) n=(\d+) t=(\d+) a=(\d+) b=(\d+) delta=(\d+)(?: p1=(\d+) p2=(\d+))?$')
COUNT_RE = re.compile(r'^COUNTS (.*)$')


def extract(name):
    points = []
    counts = None
    for line in (BASE / name).read_text().splitlines():
        match = PATTERN.match(line)
        if match:
            data = {k: int(v) for k, v in zip(
                ('rho', 'n', 't', 'a', 'b', 'delta', 'p1', 'p2'),
                match.groups()) if v is not None}
            points.append(data)
        m = COUNT_RE.match(line)
        if m:
            counts = {k: int(v) for k, v in (item.split('=') for item in m[1].split())}
    assert counts is not None, name
    return points, counts


def cube_core(n):
    """Unique n=d*x^3, d cubefree, with simple exact trial division."""
    d = x = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            d *= p ** (e % 3)
            x *= p ** (e // 3)
        p += 1
    if n > 1:
        d *= n
    return d, x


def prime_support(n):
    ps = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            ps.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ps.append(n)
    return ps


def lucas(n, k, p):
    if not (0 <= k <= n):
        return 0
    result = 1
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return 0
        result = (result * comb(a, b)) % p
        n //= p
        k //= p
    return result


def verify(point):
    rho, n, t, a, b, delta = (point[k] for k in ('rho', 'n', 't', 'a', 'b', 'delta'))
    r = 3*n+t
    M = gcd(n, 3)*gcd(n-1, 6)
    Q = n*(n-1)//M
    A = comb(n, 3)
    q = t*t+3*t+3
    H = 9*n*q+t**3
    assert (a,b) == (H//gcd(H,81*n*(n-1)),81*n*(n-1)//gcd(H,81*n*(n-1)))
    assert 81*a*n*(n-1) == b*H
    assert rho == a*a+a*b*(9*n-t-6)-b*b*q
    assert delta == Q//gcd(Q,r*r)
    assert delta**3 and 4*Q % delta**3 == 0
    dplus,x = cube_core(n)
    dminus,y = cube_core(n-1)
    assert dplus*x**3-dminus*y**3 == 1
    assert r % (x*y) == 0
    assert (2*x*y) % delta == 0
    assert all(p in prime_support(6*(3*a+b)) for p in prime_support(dplus))
    assert all(p in prime_support(6*(3*a-b)) for p in prime_support(dminus))
    assert dplus > 0 and dminus > 0
    assert n >= 104 and t*t > 9*n and 3*r < 10*n
    assert gcd(a,b)==1 and 486%b==0 and 1377*rho < 216*a*a+760*b*b
    assert a*a < 152*rho*rho.bit_length() + 1  # conservative envelope
    f = (4*a**6+(24*b*b-12*rho)*a**4 +
         (36*b**4+60*b*b*rho+12*rho*rho)*a*a -3*b*b*rho*rho-4*rho**3)
    root=isqrt(f)
    assert root*root == f
    z=(a*a-b*b-rho)//b
    L=9*a*a-b*b-3*b*z
    assert (a*a-b*b-rho)%b==0
    assert root % b == 0
    U=(root//b-L)//2
    V=(root//b+L)//2
    assert (root//b-L)%2==0
    assert U>0 and V>0 and z>0
    assert U*V==b*z**3
    assert U*729*n*n*(n-1)==b*b*(t*t-9*n)**3
    assert V*729*n*(n-1)**2==b*b*(t*t+6*t+9*n)**3
    C=M*delta; K=delta*r*r//Q
    g=gcd(C,K)
    c=C//g;h=K//g
    assert gcd(c,h)==1
    LL=(a*a-6*a*b-rho-3*b*b)*(a*a+6*a*b-rho-3*b*b)
    TT=13*a**4-17*a*a*rho-6*a*a*b*b+4*rho*rho+15*rho*b*b+9*b**4
    W=5*a*a+4*rho+3*b*b
    assert LL*h*h-18*TT*h*c+81*W*W*c*c==0
    lhs = lucas(A,r,point['p1'])
    rhs = (lucas(n*n,6*n-9,point['p1'])+(r*r)%point['p1'])%point['p1']
    assert lhs!=rhs
    k2=A-r
    lhs2=lucas(A,r,point['p2'])
    rhs2=(lucas(n*n,6*n-9,point['p2'])+(k2*k2)%point['p2'])%point['p2']
    assert lhs2!=rhs2
    return dict(**point, r=r, cube_cores={'dplus':dplus,'dminus':dminus,'x':x,'y':y},
                common={'C':C,'K':K,'c':c,'h':h},
                modular_witnesses={'r':{'p':point['p1'],'lhs':lhs,'rhs':rhs},
                                   'A-r':{'p':point['p2'],'lhs':lhs2,'rhs':rhs2}})


def main():
    producer_points=[]
    stat=[]
    for filename in PRODUCER:
        pts,stats=extract(filename)
        producer_points.extend(pts)
        stat.append(dict(filename=filename,**stats))
    independent_points, independent_stats=extract('v23_independent_4097_32768.log')
    p1={tuple(pt[k] for k in ('rho','n','t','a','b','delta')) for pt in producer_points}
    p2={tuple(pt[k] for k in ('rho','n','t','a','b','delta')) for pt in independent_points}
    assert p1 == p2 and len(p1)==8
    assert [sum(it[k] for it in stat) for k in ('attempts','primitive','square','t','n','branch','delta25')] == [935154540,76648501,129,18,16,8,5]
    assert [independent_stats[k] for k in ('square','t','n','branch','delta25')] == [129,18,16,8,5]
    certified=[verify(pt) for pt in sorted(producer_points,key=lambda x:x['rho'])]
    assert len([pt for pt in certified if pt['delta']>=25])==5
    result={
        'title':'v23 finite exhaustive residual-range audit',
        'range':{'min':4097,'max':32768},
        'previously_excluded':{'min':13,'max':4096},
        'uniform_necessary_residual_lower_bound':32770,
        'logical_scope':'original binomial equation; ell=1, j=i-3 branch, k=r or A-r',
        'method':'v21 proven a-height bound, exact integer enumerators, exact point reconstruction, Lucas mismatch',
        'algorithm_A':{'source':'v23_residual_extension.cpp','subranges':stat},
        'algorithm_B':{'source':'v23_independent_checker.cpp',**independent_stats},
        'candidate_points':certified,
        'status':'Two enumerators agree. Full first-order formal verification and external peer review not performed.'
    }
    (BASE/'v23_certificate.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('PASS independent candidate sets, all stage counts, exact identities, cubic cores and Lucas witnesses')
    print('Eight auxiliary candidates, five pass delta>=25; zero pass the original equation')
    print('rho >= 32770')

if __name__=='__main__':
    main()
