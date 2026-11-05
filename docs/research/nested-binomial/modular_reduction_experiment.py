"""Exact modular obstruction experiment; no unbounded-search claims.

Lower branch: B < 12 max(j,l), enumerate the resulting finite k.
Upper branch: t=A-B < 12 max(j,l), solve two congruences over F_p.
The global r bound is proved in proof_reduction.md.
"""
import json
import math
import sys
import time
from pathlib import Path
import numpy as np

def primes_after(n, count):
    out=[]
    q=n+1
    while len(out)<count:
        if all(q%d for d in range(2,math.isqrt(q)+1)):
            out.append(q)
        q+=1
    return out

def main(N=5, num_primes=80, gap_constant=12):
    lower=[]
    upper=[]
    for j in range(1,N+1):
        for l in range(1,N+1):
            M=max(j,l)
            for k in range(l+1,gap_constant*M):
                B=math.comb(k,l)
                if B>=gap_constant*M:
                    break
                if B>=j+2:
                    lower.append((j,l,k,B))
            for t in range(M+2,gap_constant*M):
                upper.append((j,l,t))
    initial=(len(lower),len(upper))
    lc=[];uc=[]
    limit=max(N*N,gap_constant*N)
    start=time.monotonic()
    for pn,p in enumerate(primes_after(limit,num_primes)):
        vals=np.arange(p,dtype=np.int64)
        square=vals*vals%p
        cols=np.empty((limit+1,p),dtype=np.int64)
        cols[0,:]=1
        for r in range(1,limit+1):
            cols[r,:]=cols[r-1,:]*(vals-r+1)%p*pow(r,-1,p)%p
        A={j:cols[j] for j in range(1,N+1)}
        X={j:cols[j*j,square] for j in range(1,N+1)}
        keep=[]
        for j,l,k,B in lower:
            Y=int(cols[l*l,(k*k)%p])
            diff=(cols[B,A[j]]-X[j])%p
            if np.any(diff==Y):
                keep.append((j,l,k,B))
            else:
                lc.append([j,l,k,B,p])
        lower=keep
        masks={}
        for l in {v[1] for v in upper}:
            mask=np.zeros((p,p),dtype=np.bool_)
            mask[cols[l],cols[l*l,square]]=True
            masks[l]=mask
        keep=[]
        for j,l,t in upper:
            required_B=(A[j]-t)%p
            required_Y=(cols[t,A[j]]-X[j])%p
            if np.any(masks[l][required_B,required_Y]):
                keep.append((j,l,t))
            else:
                uc.append([j,l,t,p])
        upper=keep
        if pn%10==0 or not lower and not upper:
            print({'prime':p,'primes_tested':pn+1,'remaining_lower':len(lower),'remaining_upper':len(upper),'seconds':round(time.monotonic()-start,2)},flush=True)
        if not lower and not upper:
            break
    path=Path(__file__).with_name(f'modular_obstructions_N{N}.json')
    path.write_text(json.dumps({'N':N,'gap_constant':gap_constant,'initial_counts':initial,'lower_certificates':lc,'upper_certificates':uc,'remaining_lower':lower,'remaining_upper':upper},indent=2))
    print({'file':str(path),'certified_lower':len(lc),'certified_upper':len(uc),'remaining_lower':lower[:30],'remaining_upper':upper[:50]},flush=True)

if __name__=='__main__':
    main(*(map(int,sys.argv[1:])))
