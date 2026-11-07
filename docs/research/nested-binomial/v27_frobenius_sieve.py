#!/usr/bin/env python3
"""v27 addendum: exact Frobenius / local-multiple sieve, standard Python only.

Proves (by an algebraic argument recorded in V27_FROBENIUS_ja.md) the
mod-5 and division-polynomial mod-p necessary conditions.  This program
checks their finite-field instances and performs a finite-prefix test.
Neither the generic m nor generic rho are bounded by the finite audit.
"""
from __future__ import annotations
import hashlib
import json
from math import gcd, lcm
from pathlib import Path

Point = tuple[int, int] | None
B_CHOICES = [2**i * 3**j for i in range(2) for j in range(6)]


def primes_upto(n: int):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for k in range(i*i, n+1, i): sieve[k] = False
    return [i for i in range(2, n+1) if sieve[i]]


def chi(a: int, p: int) -> int:
    a %= p
    if not a: return 0
    z = pow(a, (p-1)//2, p)
    return 1 if z == 1 else -1


def norm_model(t: int, p: int):
    A = -t*t*(4*t+3) % p
    B = 12*(t*t+5*t+3) % p
    C = 12*(2-t) % p
    R = (8*t*(4*t+3) % p, 6*t*(4*t+3)*(9*t+8) % p)
    return (A, B, C, R)


def ec_add(P: Point, Q: Point, A: int, B: int, C: int, p: int) -> Point:
    if P is None: return Q
    if Q is None: return P
    x, y = P
    u, v = Q
    if x == u:
        if (y+v)%p == 0: return None
        if 2*y%p == 0: return None
        slope = ((3*x*x+2*B*x+A*C)*pow(2*y, -1, p)) % p
    else:
        slope = ((v-y)*pow((u-x)%p, -1, p))%p
    x3 = (slope*slope-B-x-u)%p
    y3 = (slope*(x-x3)-y)%p
    assert (y3*y3-x3**3-B*x3*x3-A*C*x3-4*A*A)%p == 0
    return (x3,y3)


def cubic(q: int, b: int, rho: int) -> int:
    q2 = q*q
    return (4*q2*q + (24*b*b-12*rho)*q2 +
            (36*b**4+60*b*b*rho+12*rho*rho)*q -
            rho*rho*(3*b*b+4*rho))


def fiber(b: int, rho: int, p: int, counts: bool = True) -> dict | None:
    # 'Good' includes the nonsingularity of C as well as E_1, E_2.
    if p < 5 or b%p == 0 or rho%p == 0 or (4*rho+3*b*b)%p == 0 or (8*b*b+9*rho)%p == 0:
        return None
    t = rho*pow(b*b, -1, p)%p
    A,B,C,R = norm_model(t,p)
    assert (R[1]**2 - R[0]**3-B*R[0]**2-A*C*R[0]-4*A*A)%p == 0
    m = 0
    P = None
    allowed=[]; poles=[]; nonresidue=[]
    while True:
        if m > 3*p+3: raise AssertionError('Hasse bound violated')
        if P is None:
            allowed.append(m)
        elif P[0]==0:
            poles.append(m)
        elif chi(A*pow(P[0],-1,p),p)==1:
            allowed.append(m)
        else:
            nonresidue.append(m)
        P = ec_add(P,R,A,B,C,p)
        m+=1
        if P is None:break
    if sorted(set((3%m, (-3)%m))) != sorted(poles):
        raise AssertionError(('unexpected pole loci',p,t,m,poles))
    row = dict(p=p, t=t, h=m, allowed=allowed, poles=poles,
               excluded_nonresidue=nonresidue)
    if counts:
        n1 = p+1+sum(chi(cubic(q,b,rho),p) for q in range(p))
        n2 = p+1+sum(chi(x**3+B*x*x+A*C*x+4*A*A,p) for x in range(p))
        nc = p+2+sum(chi(cubic(x*x,b,rho),p) for x in range(p))
        assert nc==n1+n2-(p+1)
        assert n2 % m == 0  # Lagrange's theorem
        assert n1%3 == 0    # rational 3-torsion on E1
        row.update(E1_points=n1,E2_points=n2,C_points=nc,
                   trace_E1=p+1-n1,trace_E2=p+1-n2)
    return row


def filter_prefix(rows: list[dict], N: int) -> tuple[list[int], list[dict]]:
    rows=sorted(rows,key=lambda r:(len(r['allowed'])/r['h'],r['p']))
    candidates=list(range(1,N+1))
    stages=[]
    for row in rows:
        arr=[False]*row['h']
        for residue in row['allowed']:arr[residue]=True
        result=[m for m in candidates if arr[m%row['h']]]
        if len(result)<len(candidates):
            stages.append(dict(p=row['p'],h=row['h'],allowed=row['allowed'],
                               remaining=len(result), sample=result[:4]))
            candidates=result
        if not candidates: break
    return candidates,stages


def check_special_primes():
    results={}
    for t in (1,2,4):
        row=fiber(1,t,5)
        assert row['h']==5
        assert row['allowed']==([0,1,4] if t==2 else [0]),row
        results[str(t)]={k:row[k] for k in ('h','allowed','poles','E1_points','E2_points')}
    checked=[]
    for p in primes_upto(251):
        if p<11:continue
        t=(-24*pow(7,-1,p))%p
        row=fiber(1,t,p)
        assert row is not None and row['h']==7,(p,row)
        predicted=[0]
        if chi(21,p)==1:predicted += [1,6]
        if chi(105,p)==1:predicted += [2,5]
        assert sorted(row['allowed'])==sorted(predicted),(p,t,row,predicted)
        checked.append(dict(p=p,t=t,chi_21=chi(21,p),chi_105=chi(105,p),
                            allowed=row['allowed'],trace_E1=row['trace_E1'],trace_E2=row['trace_E2']))
    return {'p5':results,'p_divides_7rho_plus_24b2':checked}


def main():
    N=1_000_000; rho=32770; bound_p=239
    examples=check_special_primes()
    rows=[]
    for b in B_CHOICES:
        prime_rows=[fiber(b,rho,p) for p in primes_upto(bound_p)]
        prime_rows=[r for r in prime_rows if r is not None]
        candidates,stages=filter_prefix(prime_rows,N)
        assert not candidates, (b,candidates[:10])
        rows.append(dict(b=b,prime_count_good=len(prime_rows),
                         stages=stages, eliminated_up_to=N,remaining=0))
        print(f'b={b:3d}: no m in [1,{N}]; '
              f'finite-field obstructions from {len(stages)} primes, max used {max(s["p"] for s in stages)}')
    # The following is *periodic for the fixed rho and b*, no infinite exclusion.
    ps=[11,13,17,19,23,41,67]
    cr=[fiber(1,rho,p) for p in ps]
    assert all(cr)
    M=1
    for row in cr:M=lcm(M,row['h'])
    survivors=[m for m in range(M) if all(m%row['h'] in row['allowed'] for row in cr)]
    assert M==5040
    assert survivors==[0,630,810,1260,2070,2970,3780,4230,4410]
    obj={'claim_scope':'Necessary conditions for sections mR; not all E2(Q).',
         'rho_example':rho,'m_finite_upper_bound':N,'max_tested_prime':bound_p,
         'b_divisors_486':B_CHOICES,
         'special_prime_theorems_checks':examples,
         'periodic_fiber_b1': {'primes':ps,'period':M,'allowed_m_mod_period':survivors,
                               'traces_and_orders':cr},
         'prefix_sieve_per_b':rows,
         'no_exclusion_for_all_m':True,
         'does_not_exclude_all_rho':True}
    output=Path(__file__).with_name('v27_frobenius_certificate.json')
    output.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    print('CERTIFICATE',output)
    print('DONE: 5-torsion, 7-torsion, Frobenius identity and 12 finite prefixes PASS')

if __name__ == '__main__': main()