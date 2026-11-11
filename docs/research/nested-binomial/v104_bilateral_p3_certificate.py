#!/usr/bin/env python3
"""v104. All-prime certificate for both residue edges in j=1, ell=p-1.

NO experimental upper bound on p or i. Every prime considered is either
<= a symbolically derived U (for fixed edge distance d) or divides one
of the explicitly nonzero integers 2*L**2*(M+t/V). See the complete
mathematical derivation in V104_BILATERAL_P3_OBSTRUCTION_ja.md.
Exceptions are discharged using exact p**4/p**5 residue computations,
or proved strict real binomial size inequalities for very large primes.
This integer certificate is NOT a Lean-kernel proof.
"""
from __future__ import annotations
import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def sieve(n):
    f=bytearray(b'\x01')*(n+1)
    f[:2]=b'\x00\x00'
    for d in range(2,math.isqrt(n)+1):
        if f[d]:
            f[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [j for j in range(2,n+1) if f[j]]


def factors(n,primes):
    assert n>0
    orig=n;out={}
    for p in primes:
        if p*p>n:
            break
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
    if n>1:
        out[n]=out.get(n,0)+1
    assert math.prod(p**v for p,v in out.items())==orig
    return out


def ratmod(x,mod):
    assert math.gcd(x.denominator,mod)==1
    return (x.numerator*pow(x.denominator,-1,mod))%mod


def choosemod(n,k,p,exponent=4):
    """Binomial modulo p**exponent, removing p-powers from each factor."""
    if k>n or k<0:
        return 0
    k=min(k,n-k);m=p**exponent
    num=den=1;v=0
    for j in range(1,k+1):
        a=n-k+j;b=j
        while a%p==0:
            a//=p;v+=1
        while b%p==0:
            b//=p;v-=1
        num=num*a%m;den=den*b%m
    assert v>=0
    return 0 if v>=exponent else num*pow(den,-1,m)*p**v%m


def coeffs(d,side):
    assert d>=1 and side in ("low","high")
    a=d*d
    if side=="low":
        H=sum((Fraction(1,j) for j in range(1,d+1)),Fraction())
        J=sum((Fraction(1,j*j) for j in range(1,d+1)),Fraction())
        L=math.lcm(*range(1,d+1))
        B=a*(2*d-H)
        M=1-a*a-a*(2*d-H)**2+Fraction(a,2)*(H*H-(2*a-1)*J)
        wraps=range(B.denominator)
        assert B>0 and M<=-1
    else:
        H=sum((Fraction(1,j) for j in range(1,d)),Fraction())
        J=sum((Fraction(1,j*j) for j in range(1,d)),Fraction())
        L=math.lcm(*range(1,d)) if d>1 else 1
        B=-a*H-2*d*(a+1)
        M=B*(H+2*d)+Fraction(a,2)*(H*H+(2*a+1)*J)-(a+1)**2+1
        wraps=range(1,B.denominator+1)
        assert B<0 and M<-1
    assert L%B.denominator==0 and (2*L*L*M).denominator==1
    return {"distance":d,"side":side,"B":B,"M":M,"L":L,"wraps":wraps}


def q2(p,m):
    d=m["distance"]
    return (d*d+p*ratmod(m["B"],p))%(p*p)


def modp3_unit(p,m):
    d=m["distance"];q=q2(p,m)
    alpha=(Fraction(q)-d*d-p*m["B"])/(p*p)
    assert math.gcd(alpha.denominator,p)==1
    # Exactly F(i)/p**2 modulo p, proved from Wolstenholme and Vandermonde.
    return ratmod(m["M"]+alpha,p)


def exact_modular_gap(p,i,exponent):
    m=p**exponent
    return (choosemod(i,p,p,exponent)-i*i-
            choosemod(p*p,2*p-1,p,exponent))%m


def exceptions(m,primes):
    d=m["distance"];B=m["B"];M=m["M"];L=m["L"]
    U,V=B.numerator,B.denominator
    cutoff=max(5,d+1,d*d,abs(U))
    low=[p for p in primes if 5<=p and d<p<=cutoff and modp3_unit(p,m)==0]
    high=set();ledger=[]
    for t in m["wraps"]:
        N=2*L*L*(M+Fraction(t,V))
        assert N.denominator==1 and N!=0
        assert abs(N.numerator)<(14 if m["side"]=="low" else 40)*d**4*L*L
        ff=factors(abs(N.numerator),primes)
        ledger.append({"t":t,"N":N.numerator,"factorization":ff})
        for p in ff:
            if p>cutoff and (U+t*p)%V==0:
                assert modp3_unit(p,m)==0
                high.add(p)
    return sorted(set(low)|high),{"derived_small_prime_cutoff":cutoff,
                                  "small_p3_exceptions":low,
                                  "large_p3_exceptions":sorted(high),
                                  "nonzero_integer_factorizations":ledger}


def discharge(m,p):
    d=m["distance"]
    r=d if m["side"]=="low" else p-d
    q=q2(p,m);i=p*q+r
    assert 0<r<p and 0<=q<p*p and i<p**3
    # BOTH inequalities are proved for ALL p above the given threshold.
    if p>=1000 and 5*i<=3*p**3:
        return {"p":p,"q":q,"i":i,"reason":"uniform exact inequality C(i,p)<R_p if p>=1000 and 5i<=3p^3"}
    if p>=64 and 4*i>=3*p**3:
        return {"p":p,"q":q,"i":i,"reason":"uniform exact inequality C(i,p)>2R_p>R_p+i^2 if p>=64 and 4i>=3p^3"}
    v4=exact_modular_gap(p,i,4)
    assert v4%p**3==0
    if v4:
        return {"p":p,"q":q,"i":i,"reason":"nonzero mod p^4",
                "p3_digit":v4//p**3}
    v5=exact_modular_gap(p,i,5)
    assert v5%p**4==0 and v5!=0
    return {"p":p,"q":q,"i":i,"reason":"nonzero mod p^5",
            "p4_digit":v5//p**4}


EXPECTED={
 ("low",1):[],("low",2):[5,53],("low",3):[7,433],
 ("low",4):[5,2039],("low",5):[29,137,241,423847],
 ("low",6):[59],("low",7):[11,1279,43933129],
 ("low",8):[127,229],("low",9):[11,31,31466713,2737611311],
 ("low",10):[231799,10947653,1718780009],
 ("high",1):[5],("high",2):[11,41],("high",3):[5,2131],
 ("high",4):[7,11,29,2749],("high",5):[23],
 ("high",6):[29],("high",7):[139],("high",8):[12037],
 ("high",9):[],("high",10):[101,113,1139321,1377499],
}


def run(max_distance):
    assert 1<=max_distance<=10
    metas=[coeffs(d,side) for d in range(1,max_distance+1)
                              for side in ("low","high")]
    root=small=2
    for m in metas:
        d=m["distance"];B=m["B"]
        small=max(small,abs(B.numerator),d*d,d+1)
        for t in m["wraps"]:
            N=2*m["L"]**2*(m["M"]+Fraction(t,B.denominator))
            assert N.denominator==1 and N!=0
            root=max(root,math.isqrt(abs(N.numerator))+1)
    primes=sieve(max(root,small))
    rows=[]
    for m in metas:
        ps,ledger=exceptions(m,primes)
        key=(m["side"],m["distance"])
        assert ps==EXPECTED[key],(key,ps)
        done=[discharge(m,p) for p in ps]
        record={"side":m["side"],"distance":m["distance"],
                "B":str(m["B"]),"M":str(m["M"]),"L":m["L"],
                "all_p3_exceptions":ps,"discharged":done,**ledger}
        rows.append(record)
        print("V104_EDGE",json.dumps({k:v for k,v in record.items()
              if k!="nonzero_integer_factorizations"},ensure_ascii=False),flush=True)
    total=sum(len(row["all_p3_exceptions"]) for row in rows)
    assert max_distance!=10 or (len(rows)==20 and total==40)
    result={"status":"PASS_COMPLETE_EXACT_ALL_PRIME_EDGE_CERTIFICATE",
            "range":"all primes p>=5, no arbitrary cap on p or i",
            "scope":"j=1, ell=k-1, k=p prime, i mod p in {1..d,p-d..p-1}",
            "max_edge_distance":max_distance,
            "residue_class_families":len(rows),
            "third_digit_prime_exceptions_dispatched":total,
            "mathematics":"finite-factor p^3 obstruction and two universal binomial size inequalities",
            "lean_status":"NOT FULLY FORMALIZED",
            "rows":rows}
    print("V104_RESULT",json.dumps({k:v for k,v in result.items()
          if k!="rows"},ensure_ascii=False),flush=True)
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-distance",type=int,default=10)
    ap.add_argument("--output",type=Path)
    opt=ap.parse_args()
    data=run(opt.max_distance)
    if opt.output:
        opt.output.parent.mkdir(parents=True,exist_ok=True)
        opt.output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")


if __name__=="__main__":
    main()
