# v45 experiment: proof-oriented complete Mordell--Weil group of a fixed fibre.
# Execute in SageMath, not standard Python. NOT executed as part of this commit.
# Usage: sage docs/research/nested-binomial/v45_sage_full_fiber_group.sage 32770 1
# A complete MW certificate requires proven rank, certain generators, and
# complete torsion. If any proof step fails, report INCOMPLETE.
from sage.all import *
import json, sys

rho=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(32770)
b=ZZ(sys.argv[2]) if len(sys.argv)>2 else ZZ(1)
assert rho>0 and b>0 and 486 % b == 0
T=QQ(rho)/b**2
A=-T**2*(4*T+3)
B=12*(T**2+5*T+3)
C=12*(2-T)
E=EllipticCurve(QQ,[0,B,0,A*C,4*A**2])
R=E([8*T*(4*T+3),6*T*(4*T+3)*(9*T+8)])
print("FIBER",json.dumps(dict(rho=int(rho),b=int(b),T=str(T))))
print("R",R)
print("minimal_discriminant",E.minimal_discriminant())
try:
    rank=ZZ(E.rank(proof=True))
    basis=list(E.gens(proof=True))
    # The generators must be provably complete, not merely found by search.
    if not E.gens_certain():
        raise RuntimeError("gens_certain() returned False")
    if len(basis)!=rank:
        raise RuntimeError("Unexpected generator count")
    saturated,index,regulator=E.saturation(basis)
    tor=E.torsion_subgroup()
    print("CERTIFIED MW SUMMARY")
    print(json.dumps({
        "status":"CERTIFIED_BY_SAGE_PROOF",
        "rho":int(rho),"b":int(b),
        "rank":int(rank),
        "free_generators":[str(P) for P in saturated],
        "torsion_order":int(tor.order()),
        "torsion_invariants":[int(x) for x in tor.invariants()],
        "saturation_index":int(index),
        "regulator":str(regulator),
        "R":str(R),
        "proof_status":"rank proved, free generators certain, saturation computed"
    },indent=2,ensure_ascii=False))
except Exception as error:
    print(json.dumps({
        "status":"INCOMPLETE_NOT_CERTIFIED",
        "rho":int(rho),"b":int(b),
        "error":str(error)[:1000],
        "next_step":"Try stronger descent/rank certificate; never guess the Mordell-Weil group"
    },indent=2,ensure_ascii=False))
