#!/usr/bin/env python3
"""Independent exact witness replay via integer matrix powers and sieve."""
import csv,sys,math
def mm(a,b,l):
    x,y,z,w=a;u,v,r,t=b
    return ((x*u+y*r)%l,(x*v+y*t)%l,(z*u+w*r)%l,(z*v+w*t)%l)
def coeff(s,l):
    a=(1,0,0,1);b=(1,2,1,1)
    while s:
        if s&1:a=mm(a,b,l)
        s//=2
        if s:b=mm(b,b,l)
    return a[0],a[2]
def bound(s,l):
    a=b=1
    for _ in range((s-1)//2):
        a,b=3*a+4*b,2*a+3*b
        if b>l:return True
    return False
def check(path,L,N,old=None):
    flags=bytearray(b'\x01')*(L+1);flags[:2]=b'\x00\x00'
    for i in range(2,math.isqrt(L)+1):
        if flags[i]: flags[i*i:L+1:i]=b'\x00'*((L-i*i)//i+1)
    seen=set();prime_factors=set();indices=set();sides={'X':0,'Y':0};high=set()
    with open(path) as f:
        for row in csv.DictReader(f):
            s,l,k,chi=map(int,(row['s'],row['ell'],row['k'],row['sign']));side=row['side']
            assert 5<=s<=N and 3<=l<=L and flags[s] and flags[l] and bound(s,l)
            assert chi==(1 if l%8 in (1,7) else -1) and l==2*k*s+chi
            assert l not in prime_factors and side in sides
            x,y=coeff(s,l);assert (x==0 if side=='X' else y==0) and (x*x-2*y*y+1)%l==0
            assert int(row['real'])==(1 if side=='X' else l-1) and int(row['radical'])==0
            seen.add((s,side,l));prime_factors.add(l);indices.add(s);sides[side]+=1
            if k>32:high.add(s)
    print(f'PASS: {len(seen)} distinct verified proper divisors, {len(indices)} excluded indices; sides={sides}; k>32 indices={len(high)}')
    if old:
        with open(old) as f:previous={(int(r['s']),r['side'],int(r['ell'])) for r in csv.DictReader(f)}
        oldindices={s for s,_,_ in previous}
        assert previous<=seen,(len(previous-seen),list(previous-seen)[:5])
        print(f'All {len(previous)} previous witnesses retained; new witnesses={len(seen-previous)}, new indices={len(indices-oldindices)}, survivors={sum(flags[5:N+1])-len(indices)}')
if __name__=='__main__':
    check(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4] if len(sys.argv)>4 else None)
