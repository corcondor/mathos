"""Exact exploration of the proof-bounded gcd-defect cubic curves."""
from math import gcd, isqrt, comb
from time import perf_counter
import json
import sys


def icbrt(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 2) // 3)
    while True:
        y = (2*x + n//(x*x)) // 3
        if y >= x:
            while (x+1)**3 <= n:
                x += 1
            while x**3 > n:
                x -= 1
            return x
        x = y


def exact_prefix(T, S):
    hbits = 192*S
    bound = 1 << hbits
    c = gcd(T, 6*S)
    num, den = T//c, 6*S//c
    if icbrt(num)**3 == num and icbrt(den)**3 == den:
        return None
    bits = 2*hbits + 64
    while True:
        D = 1 << bits
        lo = icbrt((T << (3*bits)) // (6*S))
        ln, ld, hn, hd = lo, D, lo+1, D
        p0, p1, q0, q1 = 0, 1, 1, 0
        out = []
        while True:
            a = ln//ld
            if a != hn//hd:
                break
            p, q = a*p1+p0, a*q1+q0
            out.append((a,p,q))
            p0,p1,q0,q1 = p1,p,q1,q
            if q >= bound:
                return out
            lu, hu = ln-a*ld, hn-a*hd
            if lu == 0:
                break
            ln,ld,hn,hd = hd,hu,ld,lu
        bits *= 2


def curve_points(S,T,prefix):
    if prefix is None:
        # A rational cube root has denominator at most cubert(6*S).
        # The approximation lemma forces n-1 < 3*denominator/2.
        assert 3*icbrt(6*S) < 206
        return [], 0
    H=1 << (192*S)
    points=[]; tested=0
    for n in range(len(prefix)-1):
        _,pn,qn=prefix[n]
        if n:
            _,pp,qp=prefix[n-1]
        else:
            pp,qp=1,0
        qnext=prefix[n+1][2]
        qhi=min(qnext-1,H-1)
        for b in range(-2,3):
            alo=-(-(qn-b*qp)//qn)
            ahi=(qhi-b*qp)//qn
            # The elementary approximation lemma confines a to a fixed
            # set near 0 or b*a_next; see the forthcoming proof note.
            anext=prefix[n+1][0]
            choices=set(range(-1,5)) | {b*anext+c for c in range(-3,4)}
            for a in sorted(choices):
                if a<alo or a>ahi:
                    continue
                if gcd(a,b)!=1:
                    continue
                p=a*pn+b*pp; q=a*qn+b*qp
                if p<=3*q or q<=0:
                    continue
                tested+=1
                gap=T*q*q*q-6*S*p*p*p
                if gap<=0 or T*q % gap:
                    continue
                g2=T*q//gap; g=isqrt(g2)
                if g*g != g2:
                    continue
                x=g*q; r=g*p; N=x+1
                if N<104 or N>=H or (N-2)%S or not 9*N<3*r<10*N:
                    continue
                assert 6*S*r**3==T*N*(N-1)*(N-2)
                points.append((N,r))
    return sorted(set(points)),tested


def primes_upto(n):
    s=bytearray(b'\x01')*(n+1)
    s[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if s[p]:
            s[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if s[p]]


def lucas(N,K,p):
    result=1
    while N or K:
        a,b=N%p,K%p
        if b>a:
            return 0
        result=result*comb(a,b)%p
        N//=p;K//=p
    return result


def obstruction(N,r,prime_list):
    A=N*(N-1)*(N-2)//6
    ans=[]
    for k in (r,A-r):
        for p in prime_list:
            left=lucas(A,r,p)
            right=(lucas(N*N,6*N-9,p)+k*k)%p
            if left!=right:
                ans.append((p,left,right))
                break
        else:
            ans.append(None)
    return ans


if __name__=='__main__':
    stop=int(sys.argv[1]) if len(sys.argv)>1 else 1
    allpts=[]; curves=0; tested=0; maxpartial=0; steps=0
    prime_list=primes_upto(251)
    start=perf_counter()
    for S in range(1,stop+1):
        before=len(allpts)
        for T in range(162*S+1,229*S):
            prefix=exact_prefix(T,S)
            if prefix:
                maxpartial=max(maxpartial,max(x[0] for x in prefix))
                steps+=len(prefix)
            pts,count=curve_points(S,T,prefix)
            tested+=count;curves+=1
            for N,r in pts:
                allpts.append({'S':S,'T':T,'n':N,'r':r,'obstructions':obstruction(N,r,prime_list)})
        print(json.dumps({'S':S,'curves':curves,'fractions':tested,'points_for_S':len(allpts)-before,'points':len(allpts),'steps':steps,'max_partial':maxpartial,'seconds':perf_counter()-start}),flush=True)
    print(json.dumps({'points':allpts},indent=2),flush=True)
