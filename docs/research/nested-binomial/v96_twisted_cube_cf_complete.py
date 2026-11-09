#!/usr/bin/env python3
"""v96 rigorous all-5214-curve certificate using the new v95 twisted-cube form.

The complete CF approximant lemma and irrational prefix cylinder are proved
in v9_gcd_defect_continued_fractions.md. Unlike the old v9 arithmetic verifier,
this program reconstructs every CF prefix from an exact dyadic cube-root
interval and checks every recovered point via the v95 twisted-cube identity:

 D=T*q³-6*S*p³, g²*D=T*q, gcd(p,q)=1, S|(n-2), n-1=g*q
 => h=gcd(6,q)|6, e=D/h | T, T/e=s*A² (s squarefree),
    q=h*s*z², g=A*s*z, (6*S/h)*p³+e=T*h²*s³*z^6.

The square filter on q is EXACT, not a heuristic. It allows the full 5214
curves to be independently checked without re-running the expensive v9
25 million large-cube computations. The code verifies that the original
CF denominator bound 2^(192S) is covered and the prefix cylinder contains
the exact cubic irrational. It does not say the CF-completeness lemma itself
is proved in Lean (currently written proof and exact execution only).
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys, time
from math import gcd, isqrt
from pathlib import Path

MAX_S=12

def icbrt_floor(n):
    if n<2:return n
    x=1<<((n.bit_length()+2)//3)
    while True:
        y=(2*x+n//(x*x))//3
        if y>=x:
            while (x+1)**3<=n:x+=1
            while x**3>n:x-=1
            return x
        x=y

def exact_cf_prefix(S,T):
    d=gcd(T,6*S)
    num,den=T//d,(6*S)//d
    if icbrt_floor(num)**3==num and icbrt_floor(den)**3==den:
        return None
    bits=384*S+64
    H=1<<(192*S)
    while True:
        scale=1<<bits
        low=icbrt_floor((T<<(3*bits))//(6*S))
        ln,ld,hn,hd=low,scale,low+1,scale
        qprev,qcur=1,0
        word=[]
        while True:
            a=ln//ld
            if a!=hn//hd:break
            word.append(a)
            qprev,qcur=qcur,a*qcur+qprev
            if qcur>=H:return word
            lrem,hrem=ln-a*ld,hn-a*hd
            if lrem==0:break
            ln,ld,hn,hd=hd,hrem,ld,lrem
        bits*=2

def verify_prefix(S,T,word):
    if word is None:
        root=[(u,v) for v in range(1,5) for u in range(1,15)
              if gcd(u,v)==1 and 6*S*u**3==T*v**3]
        assert len(root)==1,(S,T,root)
        assert root[0][1]<=4
        # Rational-root branch excluded by the written v9 gap estimate:
        # 0 < alpha - r/(n-1) < 3/(2(n-1)^2) and
        # reduced alpha=u/v gives 1/(v*(n-1)) <= the difference,
        # hence n-1 < 3*v/2 <= 6, contradicting n>=104.
        return None
    assert len(word)>=2 and word[0]==3 and word[1]>=2
    assert all(isinstance(a,int) and a>=1 for a in word[1:])
    pm,pc,qm,qc=0,1,1,0
    conv=[]
    for i,a in enumerate(word):
        pn,qn=a*pc+pm,a*qc+qm
        assert abs(pn*qc-pc*qn)==1,(S,T,i)
        if conv:assert qn>conv[-1][1]
        conv.append((pn,qn));pm,pc,qm,qc=pc,pn,qc,qn
    H=1<<(192*S)
    assert conv[-2][1]<H<=conv[-1][1]
    # Strict endpoint cross-products authenticate the ENTIRE prefix.
    left=6*S*pc**3-T*qc**3
    right=6*S*(pc+pm)**3-T*(qc+qm)**3
    assert left*right<0,(S,T)
    return conv

def make_spf(limit):
    spf=list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for j in range(p*p,limit+1,p):
                if spf[j]==j:spf[j]=p
    return spf
SPF=make_spf(229*MAX_S)

def factor(n):
    ans={}
    while n>1:
        p=SPF[n];ans[p]=ans.get(p,0)+1;n//=p
    return ans

def divisors(n):
    ds=[1]
    for p,e in factor(n).items():ds=[d*p**j for d in ds for j in range(e+1)]
    return ds

def square_part(n):
    s=A=1
    for p,e in factor(n).items():s*=p**(e%2);A*=p**(e//2)
    assert n==s*A*A
    return s,A

def eligible_coefficients(S,T):
    by_h={};N=0
    for h in divisors(6*S):
        if 6%h or gcd(h,S)!=1:continue
        for e in divisors(T):
            w=T//e;s,A=square_part(w)
            if gcd(e,s)!=1 or gcd(w,S)!=1 or gcd(s,6//h)!=1:continue
            if not any((h*A*s*s*pow(z,3,S)-1)%S==0
                       for z in range(S) if gcd(z,S)==1):continue
            by_h.setdefault(h,{}).setdefault(s,[]).append((e,A))
            N+=1
    return by_h,N

class Engine:
    def __init__(self,S,T,conv):
        self.S=S;self.T=T;self.H=1<<(192*S)
        self.coefficients,self.types=eligible_coefficients(S,T)
        self.stats={'reduced_positive_approximants':0,'twisted_square_matches':0,
                    'equation_matches':0,'strict_survivors':0,
                    'recovered_points':[]}
        self.sample_checked=0
        self.conv=conv

    def candidate(self,p,q,small_a,small_b):
        S,T=self.S,self.T
        if p<=3*q or gcd(small_a,small_b)!=1:return
        if gcd(q,S)!=1:return  # S|n-2 and q|(n-1)
        if self.sample_checked<40:
            assert gcd(p,q)==1,(S,T,p,q,small_a,small_b)
            self.sample_checked+=1
        self.stats['reduced_positive_approximants']+=1
        h=gcd(6,q)
        for s,e_values in self.coefficients.get(h,{}).items():
            hs=h*s
            if q%hs:continue
            t=q//hs
            z=isqrt(t)
            if z*z!=t or z<=0:continue
            self.stats['twisted_square_matches']+=1
            left=(6*S//h)*p**3
            right=T*h*h*s**3*z**6
            for e,A in e_values:
                if gcd(z,e)!=1:continue
                if (h*A*s*s*pow(z,3,S)-1)%S:continue
                if left+e!=right:continue
                self.stats['equation_matches']+=1
                g=A*s*z;n=g*q+1;r=g*p
                assert g>0 and n>1 and 6*S*r**3==T*n*(n-1)*(n-2)
                assert S==1 or (n-2)%S==0
                D=T*q**3-6*S*p**3
                assert D==h*e and gcd(D,q)==h and g*g*D==T*q
                item={'S':S,'T':T,'n':str(n),'r':str(r),
                      'h':h,'e':e,'s':s,'A':A,'z':str(z)}
                if n>=104 and n<self.H and 3*n<r and 3*r<10*n:
                    self.stats['strict_survivors']+=1
                    item['result']='SURVIVES'
                else:item['result']='excluded by n>=104 / r-gap / height'
                self.stats['recovered_points'].append(item)

    def run(self):
        conv=self.conv
        for m in range(len(conv)-1):
            p0,q0=conv[m]
            pm,qm=conv[m-1] if m else (1,0)
            p1,q1=conv[m+1]
            upper=min(q1,self.H)
            for bb in range(-2,3):
                for aa in range(-1,5):
                    q=aa*q0+bb*qm
                    if not(q0<=q<upper and 2*q<q1):continue
                    self.candidate(aa*p0+bb*pm,q,aa,bb)
                for cc in range(-3,4):
                    q=bb*q1+cc*q0
                    if not(q0<=q<upper and 2*q>=q1):continue
                    self.candidate(bb*p1+cc*p0,q,bb,cc)
        return self.stats

def run(min_s,max_s):
    summary={'status':'RUNNING','range':[min_s,max_s],
             'curves':0,'irrational_curves':0,'rational_curves':0,
             'continued_fraction_terms':0,'coefficient_types':0,
             'reduced_positive_approximants':0,'twisted_square_matches':0,
             'equation_matches':0,'strict_survivors':0,'recovered_points':[],
             'by_S':[],'complete_5214_curves':(min_s,max_s)==(1,12),
             'proof_scope':'v9 CF coefficient completeness as documented, v95 exact twisted cube checks; not Lean-finalized'}
    start=time.monotonic()
    for S in range(min_s,max_s+1):
        by={'S':S,'curves':0,'irrational_curves':0,'rational_curves':0,
            'continued_fraction_terms':0,'coefficient_types':0,
            'reduced_positive_approximants':0,'twisted_square_matches':0,
            'equation_matches':0,'strict_survivors':0,'recovered_points':[]}
        for T in range(162*S+1,229*S):
            word=exact_cf_prefix(S,T)
            conv=verify_prefix(S,T,word)
            by['curves']+=1
            if conv is None:
                by['rational_curves']+=1
                # Even the rational-root curve is counted for v95 coefficient types.
                _,ct=eligible_coefficients(S,T)
                by['coefficient_types']+=ct
                continue
            by['irrational_curves']+=1
            by['continued_fraction_terms']+=len(word)
            e=Engine(S,T,conv)
            stats=e.run()
            by['coefficient_types']+=e.types
            for key in ('reduced_positive_approximants','twisted_square_matches','equation_matches','strict_survivors'):
                by[key]+=stats[key]
            by['recovered_points'].extend(stats['recovered_points'])
        assert by['curves']==67*S-1
        assert by['strict_survivors']==0,by
        for key in ('curves','irrational_curves','rational_curves','continued_fraction_terms',
                    'coefficient_types','reduced_positive_approximants','twisted_square_matches',
                    'equation_matches','strict_survivors'):
            summary[key]+=by[key]
        summary['recovered_points'].extend(by['recovered_points'])
        summary['by_S'].append({k:v for k,v in by.items() if k!='recovered_points'})
        print('V96_S_CERTIFIED',json.dumps({**by,'recovered_points':len(by['recovered_points']),
            'seconds_cumulative':round(time.monotonic()-start,3)},ensure_ascii=False),flush=True)
    if (min_s,max_s)==(1,12):
        assert summary['curves']==5214
        assert summary['irrational_curves']==5213
        assert summary['rational_curves']==1
        assert summary['continued_fraction_terms']==4877566
        assert summary['coefficient_types']==43922,summary['coefficient_types']
    assert summary['strict_survivors']==0
    summary['status']='COMPLETE_EXACT_PYTHON_CERTIFICATE'
    summary['elapsed_s']=round(time.monotonic()-start,3)
    summary['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print('V96_RESULT',json.dumps({k:v for k,v in summary.items() if k not in ('by_S','recovered_points')}),flush=True)
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--min-s',type=int,default=1)
    parser.add_argument('--max-s',type=int,default=12)
    parser.add_argument('--output',type=Path)
    a=parser.parse_args()
    assert 1<=a.min_s<=a.max_s<=12
    data=run(a.min_s,a.max_s)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
