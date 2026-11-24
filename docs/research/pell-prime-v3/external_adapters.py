"""Exact certificate adapters. External provers are checked independently in CI."""
from pathlib import Path
from math import gcd,prod
import sys
ROWS = dict([[2,[]],[3,[[2,1,2]]],[5,[[2,2,2]]],[7,[[3,1,2]]],[11,[[5,1,2]]],[17,[[2,4,3]]],[19,[[3,2,2]]],[29,[[7,1,2]]],[31,[[5,1,2],[3,1,3]]],[41,[[5,1,2],[2,3,3]]],[67,[[11,1,2]]],[239,[[17,1,2]]],[269,[[67,1,2]]],[2281,[[19,1,2],[5,1,2]]],[44560482149,[[239,1,2],[41,1,2],[31,2,2]]],[63018038201,[[269,1,2],[239,1,2],[29,1,2]]],[13558774610046711780701,[[63018038201,1,2],[269,1,2]]],[19175002942688032928599,[[63018038201,1,2],[2281,1,2]]]])
TARGETS = [(3,7,5),(5,41,29),(29,63018038201,44560482149),(59,19175002942688032928599,13558774610046711780701)]
HITS = [(189257,1,728701147781),(189913,0,613336567759),(190669,0,699320504681),(191533,1,923245370701)]
def xy(s,m=None):
    x,y=1,0
    for b in bin(s)[2:]:
        x,y=x*x+2*y*y,2*x*y
        if b=='1': x,y=x+2*y,x+y
        if m: x,y=x%m,y%m
    return x,y
def verify():
    proved={2}
    for n,fs in ROWS.items():
        if n==2: continue
        F=prod(q**e for q,e,a in fs)
        assert F*F>n and (n-1)%F==0 and len({q for q,e,a in fs})==len(fs)
        for q,e,a in fs:
            assert q in proved and e>0 and pow(a,n-1,n)==1 and gcd(pow(a,(n-1)//q,n)-1,n)==1
        proved.add(n)
    for s,x,y in TARGETS: assert xy(s)==(x,y) and x in proved and y in proved and x*x-2*y*y==-1
    for s,c,d in HITS: assert 1<d<2**(s-1) and xy(s,d)[c]==0
    print("PASS: 18-node Pocklington DAG, 8 target primes, 4 extra proper factors")
def hexcert(n):
    if n<100000: return f"(.small {n})"
    return f"(.pock {n} ["+", ".join(f"({a}, {e-1}, {hexcert(q)})" for q,e,a in sorted(ROWS[n]))+"])"
def generate(d):
    d.mkdir(parents=True,exist_ok=True)
    ns=[n for _,x,y in TARGETS for n in (x,y)]
    lines=["import HexPrimality","set_option maxRecDepth 100000","set_option maxHeartbeats 0"]
    for n in ns:
        lines.append(f"theorem pellPrime{n} : Hex.Nat.Prime {n} := by\n  apply Hex.Nat.prime_of_checkPrimeAt (c := {hexcert(n)})\n  decide +kernel\n#print axioms pellPrime{n}")
    (d/"HexPell.lean").write_text("\n\n".join(lines)+"\n")
    rows=[f"{{ n := {n}, witnesses := ["+", ".join(f"({q}, {e}, {a})" for q,e,a in fs)+"] }" for n,fs in ROWS.items() if n>=2**32]
    lines=["import PrimeFactorLean.Proofs.Pocklington","set_option maxRecDepth 100000","set_option maxHeartbeats 0","open PrimeFactorLean.Pocklington"]
    for n in ns:
        lines.append(f"def cert{n} : Certificate := {{ n := {n}, steps := ["+",\n".join(rows)+"] }")
        lines.append(f"theorem pellPrime{n} : Nat.Prime {n} := Certificate.check_sound cert{n} (by first | rfl | decide)\n#print axioms pellPrime{n}")
    (d/"PFLPell.lean").write_text("\n\n".join(lines)+"\n")
    lines=["From Coqprime Require Import PocklingtonRefl.","Local Open Scope positive_scope.","Import ListNotations."]
    for n,fs in ROWS.items():
        if n==2: continue
        a=next(a for a in range(2,10000) if pow(a,n-1,n)==1 and all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q,e,_ in fs))
        fac="["+"; ".join(f"({q},{e})" for q,e,_ in fs)+"]"
        child="["+"; ".join(f"Proof_certif {q} "+("prime_2" if q==2 else f"pell{q}") for q,e,_ in fs)+"]"
        lines.append(f"Lemma pell{n} : prime {n}.\nProof.\n  apply (Pocklington_refl (SPock_certif {n} {a} {fac}) {child}).\n  vm_compute. reflexivity.\nQed.\nPrint Assumptions pell{n}.")
    (d/"PellCoq.v").write_text("\n\n".join(lines)+"\n")
    gp=["default(parisize, 100000000);"]
    gp.append("pell(k) = { my(a=[1,0;0,1],m=[2,1;1,0],n=k); while(n, if(n%2,a*=m);m*=m;n=n\\2); [a[1,1]-a[2,1],a[2,1]]; };")
    for s,x,y in TARGETS:
        gp.append(f'if(pell({s}) != [{x},{y}], error("Pell mismatch"));')
        for n in (x,y):
            gp.append(f'c=primecert({n}); if(!isprime({n}) || !primecertisvalid(c), error("prime certificate rejected")); write("cert_{n}.gp",c); print("PASS PARI {n}");')
    gp.append("quit(0);")
    (d/"Pell.gp").write_text("\n".join(gp)+"\n")
    print("Generated Hex, PFL, CoqPrime and PARI input files")
if __name__=="__main__":
    verify()
    generate(Path(sys.argv[1]) if len(sys.argv)>1 else Path("generated"))
