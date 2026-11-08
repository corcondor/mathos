# v49: rigorous MW rank attempt for the FIRST elliptic quotient.
# Conjugate Tate normal form: Y^2+6XY+(8+9T)Y=X^3, T=rho/b^2.
# 'sage -python docs/.../v49_first_quotient_rank.sage RHO B'
# Rank only labelled certified if Sage's proof=True returns an exact value.
from sage.all import QQ, ZZ, EllipticCurve
from sage.env import SAGE_VERSION
import json,sys

rho=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(1)
b=ZZ(sys.argv[2]) if len(sys.argv)>2 else ZZ(1)
assert rho>0 and b>0 and 486 % b==0
T=QQ(rho)/b**2
coefficient=8+9*T
E=EllipticCurve(QQ,[6,0,coefficient,0,0])
P=E([0,0])
assert 3*P==E(0) and P!=E(0)
print("BEGIN",json.dumps({"rho":int(rho),"b":int(b),"T":str(T),"sage":SAGE_VERSION,
                         "a_invariants":[str(x) for x in E.a_invariants()],
                         "three_torsion_point":str(P)}),flush=True)
try:
    rank=E.rank(proof=True,algorithm='pari',pari_effort=1)
    print("PROVED_RANK",rank,flush=True)
    gens=list(E.gens(proof=True))
    if not E.gens_certain():
        raise RuntimeError("Uncertain generator basis")
    if len(gens)!=rank:
        raise RuntimeError("Rank and generator count mismatch")
    basis,index,reg=E.saturation(gens,max_prime=-1)
    tors=E.torsion_subgroup()
    print(json.dumps({
        "status":"CERTIFIED_BY_SAGE_PROOF",
        "rho":int(rho),"b":int(b),
        "rank":int(rank),"free_generators":[str(z) for z in basis],
        "torsion_order":int(tors.order()),
        "torsion_invariants":[int(z) for z in tors.invariants()],
        "saturation_index":int(index),
        "regulator":str(reg),
        "claim":"Full MW group of this ONE fixed FIRST elliptic quotient"
    },indent=2),flush=True)
except Exception as exc:
    print(json.dumps({"status":"INCOMPLETE_NOT_CERTIFIED","rho":int(rho),"b":int(b),
                      "error_type":type(exc).__name__,"error":str(exc)[:1000]},indent=2),flush=True)
    sys.exit(2)
