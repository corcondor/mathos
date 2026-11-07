"""Exact upper-branch exclusions using two-variable nonsingular Hensel lifting.

The height lemma and r<12M are proved in proof_reduction.md.
All arithmetic here is integer arithmetic. No remote prover is invoked.
"""
import json
import math
import sys
import time
from functools import lru_cache
from pathlib import Path
import numpy as np
from modular_reduction_experiment import primes_after

def bp(n,r,q):
    v=1;d=0
    for h in range(r):
        z=(n-h)%q
        d=(d*z+v)%q
        v=v*z%q
    inv=pow(math.factorial(r),-1,q)
    return v*inv%q,d*inv%q

def equations(x,y,j,l,t,q):
    A,Ad=bp(x,j,q)
    B,Bd=bp(y,l,q)
    X,Xd=bp(x*x%q,j*j,q)
    Y,Yd=bp(y*y%q,l*l,q)
    L,Ld=bp(A,t,q)
    Xd=Xd*2*x%q;Yd=Yd*2*y%q
    return ((A-B-t)%q,(L-X-Y)%q,
            Ad,-Bd%q,(Ld*Ad-Xd)%q,-Yd%q)

def floor_root(n,d):
    if d==1:return n
    low=0;high=1<<((n.bit_length()+d-1)//d)
    while high-low>1:
        mid=(low+high)//2
        if mid**d<=n:low=mid
        else:high=mid
    return high if high**d<=n else low

def bound(j,l,t):
    M=max(j,l)
    K=M**(2*M*M)
    H0=2*(6*M**3)**M
    if t<2*M:
        return max(H0,floor_root(2**(2*M+1)*math.factorial(M*M),2*M-t))
    if t>2*M:
        return floor_root(2*K*t**t,t-2*M)
    c=(j==M)+(l==M)
    num=math.factorial(M)**(2*M)
    den=math.factorial(M*M)
    assert den!=c*num*math.factorial(t),'Unresolved equal leading coefficient'
    C=9*M**3+6*M*M+3
    return max(H0,(C*math.factorial(t)*den)**M)

@lru_cache(maxsize=64)
def residue_columns(p):
    n=np.arange(p,dtype=np.int64)
    cols=np.empty((p,p),dtype=np.int64)
    cols[0,:]=1
    for r in range(1,p):
        cols[r,:]=cols[r-1,:]*(n-r+1)%p*pow(r,-1,p)%p
    return cols,n*n%p

def roots_mod(j,l,t,p):
    cols,square=residue_columns(p)
    tab={}
    for y in range(p):
        B=int(cols[l,y]);Y=int(cols[l*l,square[y]])
        tab.setdefault((B,Y),[]).append(y)
    roots=[]
    for x in range(p):
        A=int(cols[j,x]);X=int(cols[j*j,square[x]])
        L=int(cols[t,A])
        for y in tab.get(((A-t)%p,(L-X)%p),[]):
            roots.append((x,y))
    return roots

def coordinate_bound(H,m):
    r=floor_root(H,m)
    if r**m<H:r+=1
    return min(H,m*r)

def viable(x,q,lo,hi):
    return x+max(0,(lo-x+q-1)//q)*q<=hi

def certify(j,l,t,p):
    H=bound(j,l,t)
    I=coordinate_bound(H,j);K=coordinate_bound(H,l)
    roots=roots_mod(j,l,t,p)
    for x,y in roots:
        if not (viable(x,p,j+1,I) and viable(y,p,l+1,K)):
            continue
        f,g,a,b,c,d=equations(x,y,j,l,t,p)
        assert f==g==0
        if (a*d-b*c)%p==0:
            return {'status':'singular','root':[x,y],'p':p,'root_count':len(roots)}
    records=[]
    for x,y in roots:
        initial=[x,y]
        q=p;e=1
        while viable(x,q,j+1,I) and viable(y,q,l+1,K):
            qq=q*q
            f,g,a,b,c,d=equations(x,y,j,l,t,qq)
            inv=pow((a*d-b*c)%qq,-1,qq)
            nx=(x-(d*f-b*g)*inv)%qq
            ny=(y-(-c*f+a*g)*inv)%qq
            assert nx%q==x and ny%q==y
            assert equations(nx,ny,j,l,t,qq)[:2]==(0,0)
            x,y=nx,ny;q=qq;e*=2
            if q>max(I,K) and viable(x,q,j+1,I) and viable(y,q,l+1,K) and q.bit_length()>2*max(I.bit_length(),K.bit_length())+50:
                A=math.comb(x,j);B=math.comb(y,l)
                if A-B==t and B>=t and math.comb(A,t)==math.comb(x*x,j*j)+math.comb(y*y,l*l):
                    return {'status':'witness','i':x,'j':j,'k':y,'l':l}
                return {'status':'unresolved_lift','p':p,'exponent':e,'i':x,'k':y}
        records.append({'initial':initial,'exponent':e,
                        'x_excluded':not viable(x,q,j+1,I),'y_excluded':not viable(y,q,l+1,K)})
    return {'status':'certified','j':j,'l':l,'t':t,'p':p,
            'height_bits':H.bit_length(),'roots':records}

def main(N=5,prime_tries=20):
    path=Path(__file__).with_name(f'modular_obstructions_N{N}.json')
    data=json.loads(path.read_text())
    results=[];start=time.monotonic()
    for j,l,t in data['remaining_upper']:
        for p in primes_after(max(j*j,l*l,t),prime_tries):
            out=certify(j,l,t,p)
            if out['status']!='singular':
                break
        results.append(out|{'j':j,'l':l,'t':t})
        print({'case':[j,l,t],'status':out['status'],'p':p,'roots':len(out.get('roots',[])),
               'height_bits':out.get('height_bits'),'seconds':round(time.monotonic()-start,2)},flush=True)
    dest=path.with_name(f'hensel_certificates_N{N}.json')
    dest.write_text(json.dumps(results,indent=2))
    print({'file':str(dest),'certified':sum(r['status']=='certified' for r in results),
           'remaining':[r for r in results if r['status']!='certified']},flush=True)

if __name__=='__main__':
    main(*(map(int,sys.argv[1:])))
