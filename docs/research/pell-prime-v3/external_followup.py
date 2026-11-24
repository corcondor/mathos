"""Check N+1 certificates, trace polynomial recurrence and Coq compatibility.
Certificate data obtained by factoring the half-index product; validation is independent of SymPy.
"""
import sys
from math import gcd,prod
from pathlib import Path
from external_adapters import TARGETS,xy,generate,verify
DAG=dict([[2,[]],[3,[[2,1,2]]],[5,[[2,2,2]]],[7,[[3,1,2]]],[11,[[5,1,2]]],[17,[[2,4,3]]],[19,[[3,2,2]]],[31,[[5,1,2],[3,1,3]]],[41,[[5,1,2],[2,3,3]]],[67,[[11,1,2]]],[113,[[7,1,2],[2,4,3]]],[239,[[17,1,2]]],[269,[[67,1,2]]],[337,[[7,1,2],[3,1,2]]],[2281,[[19,1,2],[5,1,2]]],[44560482149,[[239,1,2],[41,1,2],[31,2,2]]]])
STEPS=[[7,3,[[2,3,1,1]]],[5,2,[[3,1,1,1],[2,1,2,1]]],[41,3,[[7,1,1,1],[3,1,4,1]]],[29,2,[[5,1,1,1],[3,1,3,1]]],[63018038201,3,[[337,1,1,1],[113,1,1,1],[41,1,1,1]]],[44560482149,2,[[337,1,3,1],[269,1,3,1],[113,1,3,1]]],[19175002942688032928599,3,[[44560482149,1,1,1],[269,1,1,1]]],[13558774610046711780701,2,[[44560482149,1,3,1],[2281,1,3,1]]]]
def mul(A,B,n,D):
    a,b=A;c,d=B
    return ((a*c+D*b*d)%n,(a*d+b*c)%n)
def pw(a,k,n,D):
    R=(1,0)
    while k:
        if k&1:R=mul(R,a,n,D)
        a=mul(a,a,n,D);k//=2
    return R
def check():
    primes={2}
    for n,fs in DAG.items():
        if n==2:continue
        F=prod(q**e for q,e,a in fs)
        assert F*F>n and (n-1)%F==0 and len({q for q,e,a in fs})==len(fs)
        for q,e,a in fs:
            assert q in primes and e>0 and pow(a,n-1,n)==1 and gcd(pow(a,(n-1)//q,n)-1,n)==1
        primes.add(n)
    assert {n for n,_,_ in STEPS}=={n for _,x,y in TARGETS for n in (x,y)}
    for n,D,ws in STEPS:
        F=prod(q**e for q,e,u,v in ws)
        assert (F-1)**2>n and (n+1)%F==0 and gcd(2*D,n)==1 and len({q for q,e,u,v in ws})==len(ws)
        for q,e,u,v in ws:
            assert q in primes and e>0 and gcd(u*u-D*v*v,n)==1
            assert pw((u,v),n+1,n,D)[1]==0 and gcd(pw((u,v),(n+1)//q,n,D)[1],n)==1
        print("PASS N+1 certificate",n,"D",D,"F",F)
    # Independent linear recurrence versus Chebyshev/trace evaluation.
    x,y=1,0; a,b=2,6; c,d=2,-6; A=B=1
    for s in range(1,10002):
        x,y=x+2*y,x+y
        if s==1:assert (x,y)==(1,1)
        if s>1 and s%2:
            h=(s-1)//2
            A+=b;B+=d
            assert (A,(-1)**h*B)==(x,y)
            a,b=b,6*b-a;c,d=d,-6*d-c
    print("PASS trace identity: 5000 odd indices")
def write(d):
    generate(d)
    coq=d/"PellCoq.v"
    coq.write_text(coq.read_text().replace("From Coqprime Require Import PocklingtonRefl.","From Coq Require Import List ZArith Znumtheory.\nFrom Coqprime Require Import Pock.").replace("prime_2)","prime_2)").replace("vm_compute. reflexivity.","vm_compute; reflexivity."))
    # Upstream v4.24 uses well-founded runtime definitions; rfl/decide got stuck.
    # Use the native backend for the PFL checker; strict kernel replay is separate in Hex.
    pfl=d/"PFLPell.lean"
    pfl.write_text(pfl.read_text().replace("by first | rfl | decide","by native_decide"))
    # Use the proof-producing n+1 checker in PrimeFactorLean, for all eight targets.
    pre=["import PrimeFactorLean.Proofs.Pocklington","set_option maxRecDepth 100000","set_option maxHeartbeats 0","open PrimeFactorLean.Pocklington"]
    leaf="{ n := 44560482149, witnesses := [(239,1,2),(41,1,2),(31,2,2)] }"
    pre.append("def depCert : Certificate := { n := 44560482149, steps := ["+leaf+"] }")
    pre.append("theorem depPrime : Nat.Prime 44560482149 := Certificate.check_sound depCert (by native_decide)")
    for n,D,ws in STEPS:
        lit="{ n := "+str(n)+", witnesses := [], D := "+str(D)+", plus := ["+", ".join(f"({q},{e},{u},{v})" for q,e,u,v in ws)+"] }"
        pre.append(f"def step{n} : Step := {lit}")
        pre.append(f"theorem plusPrime{n} : Nat.Prime {n} := Step.check_sound step{n} [44560482149] (by intro p hp; simp at hp; subst p; exact depPrime) (by native_decide)\n#print axioms plusPrime{n}")
    (d/"PlusPell.lean").write_text("\n\n".join(pre)+"\n")
if __name__=="__main__":
    verify();check();write(Path(sys.argv[1]))
