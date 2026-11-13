# v48 alternative certified rank-1 + saturated generator method on rho=100003.
# Execute with 'sage -python'. This is NOT pre-certified or a substitute for proof.
from sage.all import QQ, ZZ, EllipticCurve
from sage.env import SAGE_VERSION
import json, sys

rho=ZZ(100003)
T=QQ(rho)
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
E=EllipticCurve(QQ,[0,B,0,A*C,4*A*A])
R=E([8*T*(4*T+3),6*T*(4*T+3)*(9*T+8)])
print("BEGIN",json.dumps({"rho":int(rho),"sage":SAGE_VERSION,"known_R":str(R)}),flush=True)
try:
    print("STEP: PARI two-descent, rank(proof=True,algorithm=pari)",flush=True)
    rank=E.rank(proof=True,algorithm="pari",pari_effort=1)
    print("PROVED_RANK:",rank,flush=True)
    if rank!=1:
        raise RuntimeError("Rank is not one; cannot certify complete group from R alone")
    print("STEP: complete saturation of the known infinite-order section R",flush=True)
    generators,index,regulator=E.saturation([R],max_prime=-1)
    if len(generators)!=1:
        raise RuntimeError("Unexpected number of saturated generators")
    tor=E.torsion_subgroup()
    if tor.order()!=1:
        raise RuntimeError("Unexpected torsion; independently known to be trivial")
    print(json.dumps({
      "status":"CERTIFIED_BY_SAGE_PROOF",
      "rho":int(rho),
      "rank":int(rank),
      "free_generators":[str(z) for z in generators],
      "R_saturation_index":int(index),
      "torsion_order":int(tor.order()),
      "regulator":str(regulator),
      "method":"Sage rank(proof=True,algorithm=pari) + complete saturation, no guessed generators",
      "original_nested_binomial_equation_solved":False
    },indent=2),flush=True)
except Exception as exc:
    print(json.dumps({
        "status":"INCOMPLETE_NOT_CERTIFIED",
        "rho":int(rho),
        "error_type":type(exc).__name__,
        "error":str(exc)[:1500],
        "next_step":"Do not label rank or basis proven until PARI descent / rank proof / saturation completes."
    },indent=2),flush=True)
    sys.exit(2)
