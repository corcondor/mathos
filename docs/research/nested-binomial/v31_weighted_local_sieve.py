#!/usr/bin/env python3
"""Exact v31 arithmetic audit: split-5-adic lemma + CRT density refinement.
No claims about all rational points or about original Diophantine solutions.
Uses standard Python only, never floats for certification.
"""
import json
from math import gcd, lcm, prod
from fractions import Fraction
from pathlib import Path

PRIMES=(7,11,17,19,23,29,31,37,41,43)
B_VALUES=(1,2,3,6,9,18,27,54,81,162,243,486)
# Actually divisors of 486 = 2*3**5. Need check.
assert B_VALUES==tuple(sorted(d for d in range(1,487) if 486%d==0))

def ord_mod(a,p):
    x=1
    for n in range(1,p):
        x=x*a%p
        if x==1:return n
    raise AssertionError((a,p))

def z_value(m,p):
    r=m%5
    if r not in (2,3):return None
    k=(m-r)//5
    q=pow(p-4,k,p)
    return (1+4*q)%p if r==2 else (1-pow(q,-1,p))%p

def passes(m,p):
    z=z_value(m,p)
    return z is not None and z!=0 and pow((-3*pow(z,-1,p))%p,(p-1)//2,p)==1

def base_count(m):
    return int(m%20 in (8,12))+int(m%20 in (2,18))+2*int(m%5 in (2,3))

ordp={p:ord_mod(-4%p,p) for p in PRIMES}
L=20
for p in PRIMES:L=lcm(L,5*ordp[p])
assert L==69300,L

# Algorithm 1: take a weighted average across m, integrating independent rho mod p.
prodprimes=prod(PRIMES)
weighted_sum=0
for m in range(L):
    ways=prod(p if passes(m,p) else p-1 for p in PRIMES)
    weighted_sum+=base_count(m)*ways
result=Fraction(4,9)*Fraction(12,13)*Fraction(weighted_sum,25*L*prodprimes)

# Algorithm 2: literally enumerate which primes divide rho (2^10 subsets),
# then use independent finite-field tables and bitsets over all m mod L.
fullmask=(1<<L)-1
pmasks=[]
for p in PRIMES:
    good_m=set()
    order=ordp[p]
    for k in range(order):
        q=pow(-4,k,p)
        for r in (2,3):
            z=((1+4*q)%p if r==2 else (1-pow(q,-1,p))%p)
            # independent quadratic test by enumeration, not Euler criterion:
            if z and ((-3*pow(z,-1,p))%p in {(i*i)%p for i in range(1,p)}):
                good_m.add((5*k+r)%(5*order))
    modulus=5*order
    bits=sum(1<<m for m in range(L) if m%modulus in good_m)
    pmasks.append(bits)
base_masks=[]
for t in (8,13,18,23):
    bits=sum(1<<m for m in range(L) if (
        (m%20 in (8,12)) if t==8 else
        ((m%20 in (2,18)) if t==23 else (m%5 in (2,3)))))
    base_masks.append(bits)
independent_num=0
for subset in range(1<<len(PRIMES)):
    bits=fullmask
    p_weight=1
    for i,p in enumerate(PRIMES):
        if (subset>>i)&1: bits &= pmasks[i]
        else:p_weight*=p-1
    independent_num+=p_weight*sum((bits & bm).bit_count() for bm in base_masks)
independent=Fraction(4,9)*Fraction(12,13)*Fraction(independent_num,25*L*prodprimes)
assert result==independent,(result,independent)

# V30 stage, compare precisely.
def legacy_density():
    S=(7,)
    M=60
    sums=0
    for m in range(M):
        sums+=base_count(m)*(7 if passes(m,7) else 6)
    return Fraction(4,9)*Fraction(12,13)*Fraction(sums,25*M*7)
old=legacy_density()
assert old==Fraction(304,20475),old
assert result<old

# Full genus-2 square obstruction, independent of cyclic subgroup.
def F(a,b,rho):
    return (4*a**6+(24*b*b-12*rho)*a**4 +
        (36*b**4+60*b*b*rho+12*rho**2)*a*a -
        3*b*b*rho**2-4*rho**3)

def v5(n):
    if n==0:return None
    v=0
    while n%5==0:n//=5;v+=1
    return v
for b in B_VALUES:
    for T in (13,38,63,88,113,138,163,188,213):
        assert T%25==13
        rho=b*b*T
        for j in range(-8,9):
            a=5*j
            assert v5(F(a,b,rho))==1,(a,b,rho,v5(F(a,b,rho)))

# Two explicit congruence branches of the opposite deep collision (k=2).
# For a=5*b*w (w unit), F/(25*b**6) == 4*w^2 + q (mod 5),
# q=(4*T+3)/25. If q=3, only w=+/-2 pass; if q=2,
# only w=+/-1 pass. Higher v5(a) is impossible for these classes.
for T,allowed in ((18,{2,3}),(43,{1,4})):
    assert T%25==18 and v5(4*T+3)==2
    q=(4*T+3)//25%5
    assert (q==3 if T==18 else q==2)
    for b in B_VALUES:
        rho=T*b*b
        for w in range(1,5):
            f=F(5*b*w,b,rho)
            assert v5(f)==2
            assert ((f//25//b**6)%5)==(4*w*w+q)%5
            assert ((f//25)%5 in (1,4))==(w in allowed)
        for w in (1,2,3):
            f=F(25*b*w,b,rho)
            assert v5(f)==2 and (f//25)%5 not in (1,4)

# Refined valuation identity for 5 | a, T equiv 3 mod 5.
# f(u,T)=F(a,b,b^2 T)/b^6, with u=a/b. b is a 5-adic unit.
# The coefficient of u^2 is 12(T^2+5T+3), a 5-adic unit.
# If 2s<k: valuation=2s and unit square. If 2s>k: valuation=k.
for T in (13,18,43,68,93,118,143,163,188,213,263,313,388):
    if T%5!=3:continue
    k=v5(4*T+3)
    for b in B_VALUES:
        rho=T*b*b
        for a in [5*b,10*b,25*b,50*b,125*b,250*b]:
            s=v5(a)
            v=v5(F(a,b,rho))
            if 2*s<k:assert v==2*s,(T,b,a,v,k,s)
            if 2*s>k:assert v==k,(T,b,a,v,k,s)

# Exact local 5-adic square criterion when T=13 (mod25), ell=v5(9T+8) odd.
def is_Q5_square(z):
    if z==0: return True
    d=v5(z)
    return d%2==0 and z//(5**d)%5 in (1,4)

def sqrt_mod_5n(unit,n):
    assert unit%5 in (1,4)
    roots=[x for x in range(5) if x*x%5==unit%5]
    for k in range(1,n):
        step=5**k
        roots=[r+t*step for r in roots for t in range(5) if (r+t*step)**2% (5*step)==unit%(5*step)]
    return sorted(roots)

local_records=[]
for T,search_limit in ((13,3125),(37513,3125),(1388,3125)):
    assert T%25==13
    ell=v5(9*T+8)
    assert ell%2==1 and ell>=3
    hcrit=(3*ell+1)//2
    rootmod=5**hcrit
    for b in B_VALUES:
        rho=b*b*T
        # The H=0 congruence has two classes (Hensel roots).
        root_rhs=(-(2*b*b+3*rho)*pow(6,-1,rootmod))%rootmod
        roots=sqrt_mod_5n(root_rhs,hcrit)
        assert len(roots)==2 and all((6*r*r+2*b*b+3*rho)%rootmod==0 for r in roots)
        for a in range(search_limit):
            expected=(a%5!=0 and (6*a*a+2*b*b+3*rho)%rootmod!=0)
            assert expected==is_Q5_square(F(a,b,rho)),(T,b,a,expected)
        if b==1:local_records.append({'T':T,'ell':ell,'threshold':hcrit,'roots_modulus':rootmod,'roots':roots,'tested_a':search_limit})

# Concrete rho >= 32770 respecting the previously established rho mod 9 filter.
assert 37513%9 in (1,4,6,7) and 37513>=32770
assert (6*1292**2+2+3*37513)%(5**5)==0
assert v5(F(1292,1,37513))==9
assert gcd(1292,37513)==gcd(1292,3)==1

report={
 'status':'PASS',
 'local_5adic_odd_ell_records':local_records,
 'local_5adic_counterexample':{'a':1292,'b':1,'rho':37513,'valuation_F':9},
 'stage':'v31_weighted_local_sieve',
 'primes':list(PRIMES),
 'orders':{str(p):ordp[p] for p in PRIMES},
 'm_period':L,
 'old_fraction':str(old),'old_percent':format(100*float(old),'.12f'),
 'new_fraction':str(result),'new_percent':format(100*float(result),'.12f'),
 'relative_improvement':str((old-result)/old),
 'independent_agreement':result==independent,
 'bitset_subsets_checked':2**len(PRIMES),
 'base_modulo':25,
 'prime_13_forbidden':True,
 'original_equation_solved':False,
 'scope':'necessary local conditions for solutions whose auxiliary point lies in <R>; one independent genus-2 5-adic lemma'
}
Path(__file__).with_name('v31_certificate.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
