#!/usr/bin/env python3
"""Independent reproducibility audit for primitive H=14..20.

Reads NO primary certificate and imports NO primary source. Builds the cube
root CF by rational dyadic interval transformations (not algebraic cubic
transformations), and enumerates all 65-pair union fractions, checking
D|6HT via distinct modulus 12HT+1 (not 6HT+1 in primary).
"""
import hashlib, json, math, sys, time
from pathlib import Path
P=Path(__file__).parent

def icbrt(n):
    assert n>=0
    if n<2:return n
    x=1 << ((n.bit_length()+2)//3)
    while True:
        y=(2*x+n//(x*x))//3
        if y>=x:
            while x*x*x>n:x-=1
            while (x+1)**3<=n:x+=1
            return x
        x=y

def cf_prefix(H,T):
    bound=1<<(192*H)
    bits=384*H+64
    for _ in range(8):
        scale=1<<bits
        below=icbrt((T<<(3*bits))//(6*H))
        assert 6*H*below**3 <= T*scale**3 < 6*H*(below+1)**3
        ln,ld,hn,hd=below,scale,below+1,scale
        qprev,qcur=1,0
        word=[]
        while True:
            lo=ln//ld;hi=hn//hd
            if lo!=hi:break
            a=lo
            word.append(a)
            qprev,qcur=qcur,a*qcur+qprev
            if qcur>=bound:return word
            rl=ln-a*ld;rh=hn-a*hd
            if rl==0 or rh==0:break
            ln,ld,hn,hd=hd,rh,ld,rl
        bits*=2
    raise AssertionError('precision did not certify prefix')

def trial_divisors(n):
    remaining=n;values=[1]
    p=2
    while p*p<=remaining:
        if remaining%p:
            p+=1 if p==2 else 2
            continue
        pw=[1]
        while remaining%p==0:
            remaining//=p;pw.append(pw[-1]*p)
        values=[a*b for a in values for b in pw]
        p+=1 if p==2 else 2
    if remaining>1:values.extend([x*remaining for x in values])
    return set(values)

def run(H):
    st=time.monotonic()
    bound=1<<(192*H)
    pts=set();survivors=set()
    stats={'H':H,'curves':0,'terms':0,'reduced_fractions':0,'modulus_passes':0,'cubic_checks':0}
    word_hasher=hashlib.sha256()
    for T in range(162*H+1,229*H):
        if math.gcd(H,T)>1:continue
        # All primitive cases below 21 have an Eisenstein-prime obstruction
        # to T/(6H) being a rational cube; the generator would otherwise end.
        tmp=math.gcd(T,6*H);a,b=T//tmp,6*H//tmp
        assert not (icbrt(a)**3==a and icbrt(b)**3==b)
        word=cf_prefix(H,T)
        assert word[0]==3 and word[1]>=2
        word_hasher.update(json.dumps([T,word],separators=(',',':')).encode()+b'\n')
        stats['curves']+=1;stats['terms']+=len(word)
        pp,pn,qp,qn=0,1,1,0
        conv=[]
        for a in word:
            pp,pn=pn,pp+a*pn
            qp,qn=qn,qp+a*qn
            conv.append((pn,qn))
        assert conv[-2][1]<bound<=conv[-1][1]
        left=6*H*pn**3-T*qn**3
        right=6*H*(pn+pp)**3-T*(qn+qp)**3
        assert left*right<0
        M=12*H*T+1
        mods=[(p%M,q%M) for p,q in conv]
        divs=trial_divisors(6*H*T)
        for idx in range(len(word)-1):
            P0,Q0=conv[idx]
            PP,QP=conv[idx-1] if idx else (1,0)
            PR,QR=mods[idx]
            PL,QL=mods[idx-1] if idx else (1,0)
            bound_stage=min(conv[idx+1][1],bound)
            nxt=word[idx+1]
            for b in range(-2,3):
                aset=set(range(-1,5)) | {b*nxt+c for c in range(-3,4)}
                for a in aset:
                    if math.gcd(a,b)!=1:continue
                    q=a*Q0+b*QP
                    if not Q0<=q<bound_stage:continue
                    p=a*P0+b*PP
                    if p<=3*q:continue
                    stats['reduced_fractions']+=1
                    pm=(a*PR+b*PL)%M
                    qm=(a*QR+b*QL)%M
                    dmod=(T*pow(qm,3,M)-6*H*pow(pm,3,M))%M
                    if dmod not in divs:continue
                    stats['modulus_passes']+=1
                    stats['cubic_checks']+=1
                    D=T*q**3-6*H*p**3
                    if D!=dmod or D<=0 or (T*q)%D:continue
                    g2=T*q//D
                    g=math.isqrt(g2)
                    if g*g!=g2:continue
                    n,r=g*q+1,g*p
                    assert 6*H*r**3==T*n*(n-1)*(n-2)
                    pts.add((T,n,r))
                    if n>=104 and n<bound and (n-2)%H==0 and 3*n<r and 3*r<10*n:
                        survivors.add((T,n,r))
        if stats['curves']%200==0:
            print(f'Independent H={H}: curves {stats["curves"]}, terms {stats["terms"]}, survivors {len(survivors)}, seconds {time.monotonic()-st:.1f}',flush=True)
    results={**stats,'status':'PASS' if len(survivors)==0 else 'CANDIDATES',
            'points':[{'T':t,'n':n,'r':r} for t,n,r in sorted(pts)],
            'survivors':[{'T':t,'n':n,'r':r} for t,n,r in sorted(survivors)],
            'certificate_read':False,'primary_source_imported':False,
            'CF_method':'Exact rational dyadic interval transformations',
            'modulus':'12HT+1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'generation_digest':word_hasher.hexdigest(),'seconds':round(time.monotonic()-st,2)}
    (P/f'h{H}_independent.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'H':H,'status':results['status'],'curves':stats['curves'],'fractions':stats['reduced_fractions'],'points':len(pts),'survivors':len(survivors),'seconds':results['seconds']}),flush=True)

if __name__=='__main__':
    if len(sys.argv)>1:run(int(sys.argv[1]))
    else:
        for h in range(14,21):run(h)
