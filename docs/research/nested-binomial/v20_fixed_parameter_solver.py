#!/usr/bin/env python3
"""Complete fixed-(delta,J) reconstruction from the v19 eliminants.

SymPy proposes factorizations only. Every prime is certified recursively by
an integer Lucas order certificate, independently checkable without SymPy.
Quadratics use integer square roots; complementary quartics use the proved
strict monotonicity of L(n)/sqrt(n(n-1)), retaining the positive sign.
No floating roots, Pell point generation, or chosen n cutoff is used.
"""
import argparse
from collections import Counter
from functools import lru_cache
import gzip
import hashlib
import json
from math import comb,gcd,isqrt
from pathlib import Path
import time
import sympy


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


class ExactFactorizations:
    def __init__(self):self.primes={2:{'p':2,'base':True}};self.cache={}

    def prime_certificate(self,p):
        if p in self.primes:return
        fac=self.factor(p-1)
        # A primitive root supplies a witness for every genuine prime p.
        # Keep the complete lazy range; no arbitrary witness-search cutoff.
        for a in range(2,p):
            if pow(a,p-1,p)!=1:continue
            if all(gcd(pow(a,(p-1)//q,p)-1,p)==1 for q,e in fac):
                self.primes[p]={'p':p,'a':a,'p_minus_one':fac}
                return
        raise RuntimeError(f'No complete primality certificate found for factor {p}')

    def factor(self,n):
        if n in self.cache:return self.cache[n]
        proposed=sorted((int(p),int(e)) for p,e in sympy.factorint(n).items())
        value=1
        for p,e in proposed:
            assert p>=2 and e>=1
            value*=p**e
            self.prime_certificate(p)
        assert value==n
        fac=[list(t) for t in proposed]
        self.cache[n]=fac
        return fac


def divisors(factors):
    ds=[1]
    for p,e in factors:
        before=ds[:]
        for i in range(1,e+1):ds.extend(d*p**i for d in before)
    return sorted(ds)


def eliminant(c,h,branch):
    if branch=='small':return 2*(3*h*h-4*c*h+68*c*c)
    U=4*h*h+10*c*h-108*c*c
    V=2*h*h-52*c*h+9*c*c
    return V*V+2*U*U


def quartic_sign(n,c,h,J,G):
    L=(h-9*c)*n*n-(h+6*c)*n-c*(J*G+9)
    if L<=0:return -1
    f=L*L-4*c*h*n*(n-1)
    return (f>0)-(f<0)


def isolate(c,h,J,G,branch,nmin=104):
    a,b=h-9*c,h+6*c
    assert a>0 and c>0 and J>0 and G>0 and nmin>=2
    if branch=='small':
        D=b*b+4*a*c*(J*G+10)
        s=isqrt(D)
        root=None
        if s*s==D and (b+s)%(2*a)==0 and (b+s)//(2*a)>=nmin:
            root=(b+s)//(2*a)
        return {'kind':'quadratic','floor_sqrt_discriminant':s,'root':root}
    sign=quartic_sign(nmin,c,h,J,G)
    if sign>=0:
        return {'kind':'domain_start','root':nmin if sign==0 else None}
    d=c*(J*G+9)
    B=b+7*c
    hi=max(nmin+1,(B+isqrt(B*B+4*a*d))//(2*a)+2)
    assert a*hi*hi-B*hi-d>0
    assert quartic_sign(hi,c,h,J,G)>0
    lo=nmin
    while lo+1<hi:
        mid=(lo+hi)//2
        if quartic_sign(mid,c,h,J,G)>=0:hi=mid
        else:lo=mid
    assert quartic_sign(lo,c,h,J,G)<0<=quartic_sign(hi,c,h,J,G)
    return {'kind':'adjacent_bracket','lower':lo,'upper':hi,
            'root':hi if quartic_sign(hi,c,h,J,G)==0 else None}


def lucas(N,R,p):
    value=1
    while N or R:
        a,b=N%p,R%p
        if b>a:return 0
        value=value*comb(a,b)%p
        N//=p;R//=p
    return value


def inspect_root(n,c,h,J,G,M,delta,branch):
    if branch=='small':
        numerator=h*n*(n-1)
        if numerator%c:return {'reason':'nonintegral_r_squared'}
        R=numerator//c;r=isqrt(R)
        if r*r!=R:return {'reason':'nonsquare_r_squared','floor_sqrt':r}
    else:
        L=(h-9*c)*n*n-(h+6*c)*n-c*(J*G+9)
        if L%(2*c):return {'reason':'nonintegral_r'}
        r=L//(2*c)
    assert c*r*r==h*n*(n-1)
    if gcd(n,3)*gcd(n-1,6)!=M:return {'reason':'wrong_M','r':r}
    Q=n*(n-1)//M
    if Q//gcd(Q,r*r)!=delta:return {'reason':'wrong_delta','r':r}
    eps=int(branch=='complement')
    N=n*n+2;T=(r-eps)**2-9*n*n-6*n-10
    assert T==J*G
    if gcd(N,T)!=G:return {'reason':'wrong_canonical_G','r':r}
    w=N//G
    if w<65:return {'reason':'w_below_65','r':r,'w':w}
    if not(3*n<r and 3*r<10*n):return {'reason':'coarse_interval','r':r,'w':w}
    if pow(r,3,Q):return {'reason':'cube_divisibility','r':r,'w':w}
    if (r-3*n)**2<=9*n:return {'reason':'square_root_gap','r':r,'w':w}
    A=n*(n-1)*(n-2)//6;k=r if branch=='small' else A-r
    for p in range(2,98):
        if any(p%d==0 for d in range(2,isqrt(p)+1)):continue
        lhs=lucas(A,r,p);inner=lucas(n*n,6*n-9,p);rhs=(inner+k*k)%p
        if lhs!=rhs:return {'reason':'original_binomial_modulus','r':r,'w':w,
                            'witness':{'p':p,'lhs':lhs,'inner':inner,'k_squared':k*k%p,'rhs':rhs}}
    return {'reason':'undecided_after_moduli','r':r,'w':w}


def solve(queries,output,elimination_note):
    start=time.perf_counter();F=ExactFactorizations();families=[];totals=Counter();roots=[];unresolved=[]
    @lru_cache(None)
    def root_info(c,h,J,G,branch):return isolate(c,h,J,G,branch)
    for delta,J,branch in queries:
        assert delta>=1 and J>=1 and branch in ('small','complement')
        for M in (1,2,3,6):
            C=M*delta
            for K in range(9*C+1,(10400*C-1)//927+1):
                if gcd(K,delta)!=1:continue
                common=gcd(C,K);c,h=C//common,K//common
                E=eliminant(c,h,branch);fac=F.factor(E);ds=divisors(fac)
                rows=[];totals['coefficient_families']+=1
                for G in ds:
                    row={'G':G,**root_info(c,h,J,G,branch)}
                    totals['divisor_polynomials']+=1
                    n=row['root']
                    if n is not None:
                        totals['integer_n_roots']+=1
                        result=inspect_root(n,c,h,J,G,M,delta,branch)
                        row['root_check']=result
                        totals[result['reason']]+=1
                        rec={'delta':delta,'J':J,'branch':branch,'M':M,'K':K,
                             'c':c,'h':h,'G':G,'n':n,**result}
                        roots.append(rec)
                        if result['reason']=='undecided_after_moduli':unresolved.append(rec)
                    rows.append(row)
                families.append({'delta':delta,'J':J,'branch':branch,'M':M,'K':K,
                                 'c':c,'h':h,'E':E,'E_factorization':fac,'divisors':rows})
    data={'status':'COMPLETE_FINITE_RECONSTRUCTION' if unresolved else 'PASS_COMPLETE_EXCLUSION_FOR_QUERIES',
          'queries':[{'delta':d,'J':j,'branch':b} for d,j,b in queries],
          'scope':'Every M,K and every G|E for the stated fixed parameter pairs; all n>=104, no numeric n cutoff',
          'input_theory':'v19_canonical_defect_elimination.md, integer E0/E1 divisibility and n equations',
          'elimination_note_sha256':sha(elimination_note),
          'new_root_theorem':'L(n)/sqrt(n(n-1)) is strictly increasing for n>=2; retains L(n)>0',
          'factor_discovery':'SymPy factorint, with separate complete recursive Lucas primality certificates',
          'sympy_version':sympy.__version__,'producer_sha256':sha(Path(__file__)),
          'prime_certificates':[F.primes[p] for p in sorted(F.primes)],
          'families':families,'counts':dict(totals),'integer_root_records':roots,'undecided':unresolved,
          'claims_not_made':['unbounded delta or J solved','every local root satisfies original equation',
                             'Lean execution','DeepSeek API execution','global parameter exclusion from two example queries']}
    raw=(json.dumps(data,sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    with output.open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as z:z.write(raw)
    summary={k:v for k,v in data.items() if k not in ('families','prime_certificates')}
    summary.update({'certificate_file':output.name,'certificate_sha256':sha(output),
                    'uncompressed_sha256':hashlib.sha256(raw).hexdigest(),
                    'primality_certificate_count':len(F.primes),'wall_seconds':round(time.perf_counter()-start,6)})
    output.with_suffix('').with_suffix('.summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='integer_root_records'},ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--delta',type=int)
    parser.add_argument('--J',type=int)
    parser.add_argument('--branch',choices=['small','complement'],default='complement')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('v20_fixed_parameter_certificate.json.gz'))
    parser.add_argument('--elimination-note',type=Path,default=Path(__file__).with_name('v19_canonical_defect_elimination.md'))
    args=parser.parse_args()
    if args.delta is None and args.J is None:
        queries=[(25,17,'small'),(25,33,'complement')]
    else:
        assert args.delta is not None and args.J is not None
        queries=[(args.delta,args.J,args.branch)]
    solve(queries,args.output,args.elimination_note)
