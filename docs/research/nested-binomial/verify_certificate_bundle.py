"""Independent verifier: factorial residue tables and digit-correction Hensel.

Does not import the search/generation programs. Python standard library only.
The analytic prerequisites are proved in proof_reduction.md.
"""
import collections
import hashlib
import json
import math
import sys
import time
from functools import lru_cache
from pathlib import Path

@lru_cache(None)
def prime(p):
    return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))

def nth_floor(n,d):
    lo=0;hi=1<<((n.bit_length()+d-1)//d)
    while lo<hi:
        mid=(lo+hi+1)//2
        if mid**d<=n:lo=mid
        else:hi=mid-1
    return lo

def bounds(j,l,t):
    m=max(j,l);h0=2*(6*m**3)**m
    if t<2*m:
        h=max(h0,nth_floor((1<<(2*m+1))*math.factorial(m*m),2*m-t))
    elif t>2*m:
        h=nth_floor(2*m**(2*m*m)*t**t,t-2*m)
    else:
        den=math.factorial(m*m)
        num=math.factorial(m)**(2*m)
        c=int(j==m)+int(l==m)
        assert den-c*num*math.factorial(t)!=0
        assert num<=den
        h=max(h0,((9*m**3+6*m*m+3)*math.factorial(t)*den)**m)
    out=[]
    for s in (j,l):
        r=nth_floor(h,s)
        ceil=r+int(r**s<h)
        out.append(min(h,s*ceil))
    return tuple(out)

def intersects(x,q,lo,hi):
    # Independent formulation: there exists a multiple of q between lo-x and hi-x.
    return -((x-lo)//q) <= (hi-x)//q

class Tables:
    def __init__(self,p):
        assert prime(p)
        self.p=p;self.fact=[1]*p
        for n in range(1,p):self.fact[n]=self.fact[n-1]*n%p
        self.inv=[0]*p;self.inv[-1]=pow(self.fact[-1],-1,p)
        for n in range(p-1,0,-1):self.inv[n-1]=self.inv[n]*n%p
        self.columns={};self.squares={}
    def col(self,r):
        assert 0<=r<self.p
        if r not in self.columns:
            p=self.p;z=[0]*p;v=self.inv[r]
            for n in range(r,p):z[n]=self.fact[n]*v%p*self.inv[n-r]%p
            self.columns[r]=z
        return self.columns[r]
    def sq(self,r):
        if r not in self.squares:
            col=self.col(r*r);p=self.p
            self.squares[r]=[col[n*n%p] for n in range(p)]
        return self.squares[r]

@lru_cache(maxsize=64)
def tables(p):return Tables(p)

def roots(j,l,t,p):
    z=tables(p);a=z.col(j);b=z.col(l);x=z.sq(j);y=z.sq(l);lt=z.col(t)
    indexed=collections.defaultdict(list)
    for v in range(p):indexed[(b[v],y[v])].append(v)
    out=set()
    for u in range(p):
        for v in indexed.get(((a[u]-t)%p,(lt[a[u]]-x[u])%p),[]):out.add((u,v))
    return out

def value_derivative(n,r,q):
    # Product derivative from prefix/suffix products, not the generator's dual recurrence.
    factors=[(n-h)%q for h in range(r)]
    pre=[1]
    for x in factors:pre.append(pre[-1]*x%q)
    suffix=1;der=0
    for h in range(r-1,-1,-1):
        der=(der+pre[h]*suffix)%q
        suffix=suffix*factors[h]%q
    inv=pow(math.factorial(r),-1,q)
    return pre[-1]*inv%q,der*inv%q

def evaluate(u,v,j,l,t,q):
    a,ad=value_derivative(u,j,q);b,bd=value_derivative(v,l,q)
    x,xd=value_derivative(u*u,j*j,q);y,yd=value_derivative(v*v,l*l,q)
    z,zd=value_derivative(a,t,q)
    return ((a-b-t)%q,(z-x-y)%q,ad,(-bd)%q,
            (zd*ad-2*u*xd)%q,(-2*v*yd)%q)

def main(N=20):
    base=Path(__file__).parent
    mp=base/f'modular_obstructions_N{N}.json';hp=base/f'hensel_certificates_N{N}.json'
    m=json.loads(mp.read_text());h=json.loads(hp.read_text())
    assert m['N']==N
    G=m.get('gap_constant',32);assert G>=12
    expected_lo=set();expected_up=set()
    for j in range(1,N+1):
        for l in range(1,N+1):
            M=max(j,l)
            for k in range(l+1,G*M):
                b=math.comb(k,l)
                if j+2<=b<G*M:expected_lo.add((j,l,k,b))
            expected_up.update((j,l,t) for t in range(M+2,G*M))
    lower=m['lower_certificates'];upper=m['upper_certificates']
    assert not m['remaining_lower']
    assert len(lower)==len({tuple(v[:-1]) for v in lower})
    assert {tuple(v[:-1]) for v in lower}==expected_lo
    mod_up={tuple(v[:-1]) for v in upper}
    lift_up={(v['j'],v['l'],v['t']) for v in h}
    assert len(mod_up)==len(upper) and len(lift_up)==len(h)
    assert mod_up.isdisjoint(lift_up)
    assert lift_up=={tuple(v) for v in m['remaining_upper']}
    assert mod_up|lift_up==expected_up
    assert list(m['initial_counts'])==[len(expected_lo),len(expected_up)]
    start=time.monotonic();done=0
    for j,l,k,b,p in sorted(lower,key=lambda v:v[-1]):
        assert p>max(j*j,l*l,b) and prime(p)
        z=tables(p);a=z.col(j);x=z.sq(j);outer=z.col(b)
        y=z.col(l*l)[k*k%p]
        assert all((outer[a[n]]-x[n]-y)%p for n in range(p)),('lower',j,l,k,p)
        done+=1
    print({'verified_lower':done,'seconds':round(time.monotonic()-start,2)},flush=True)
    pair_cache={};current_p=None
    for j,l,t,p in sorted(upper,key=lambda v:v[-1]):
        assert p>max(j*j,l*l,t) and prime(p)
        if p!=current_p:pair_cache={};current_p=p
        z=tables(p)
        if l not in pair_cache:
            b=z.col(l);y=z.sq(l);pair_cache[l]={(b[n],y[n]) for n in range(p)}
        a=z.col(j);x=z.sq(j);outer=z.col(t);pairs=pair_cache[l]
        assert all(((a[n]-t)%p,(outer[a[n]]-x[n])%p) not in pairs for n in range(p)),('upper',j,l,t,p)
    print({'verified_upper_modular':len(upper),'seconds':round(time.monotonic()-start,2)},flush=True)
    branches=0;lift_steps=0
    for idx,rec in enumerate(h):
        assert rec['status']=='certified'
        j,l,t,p=(rec[s] for s in ('j','l','t','p'))
        assert p>max(j*j,l*l,t) and prime(p)
        I,K=bounds(j,l,t)
        listed=[tuple(v['initial']) for v in rec['roots']]
        assert len(listed)==len(set(listed))
        assert set(listed)==roots(j,l,t,p),('root coverage',j,l,t,p)
        for rr in rec['roots']:
            u,v=rr['initial'];q=p;e=1;target=rr['exponent']
            assert target>=1 and target&(target-1)==0
            possible=lambda:intersects(u,q,j+1,I) and intersects(v,q,l+1,K)
            if possible():
                f,g,a,b,c,d=evaluate(u,v,j,l,t,p)
                assert f==g==0 and (a*d-b*c)%p!=0
            while e<target:
                assert possible(),('unnecessary certificate step',j,l,t,p,e)
                qq=q*q
                f,g,a,b,c,d=evaluate(u,v,j,l,t,qq)
                assert f%q==g%q==0
                # Solve for the next q-adic digit using J modulo q.
                inv=pow((a*d-b*c)%q,-1,q)
                du=(-d*(f//q)+b*(g//q))*inv%q
                dv=(c*(f//q)-a*(g//q))*inv%q
                u+=q*du;v+=q*dv;q=qq;e*=2;lift_steps+=1
                assert evaluate(u,v,j,l,t,q)[:2]==(0,0)
            assert not possible(),('surviving branch',j,l,t,p,rr)
            branches+=1
        if (idx+1)%2000==0:
            print({'verified_hensel':idx+1,'seconds':round(time.monotonic()-start,2)},flush=True)
    report={'verification_passed':True,'N':N,'gap_constant':G,
            'lower_modular_families':len(lower),'upper_modular_families':len(upper),
            'upper_hensel_families':len(h),'total_families':len(expected_lo)+len(expected_up),
            'initial_hensel_branches_checked':branches,'hensel_lift_steps_checked':lift_steps,
            'unresolved_families':0,'seconds':round(time.monotonic()-start,2),
            'certificate_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (mp,hp)},
            'scope':'No valid nonnegative integer solution with 1 <= j,l <= N; i,k arbitrary.',
            'method':'Separate standard-library verifier; factorial residue tables, prefix/suffix derivatives, q-adic digit corrections.'}
    (base/f'verification_result_N{N}.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report),flush=True)

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 20)
