# v52: higher-effort PARI proof of ranks left uncertain by v50.
# Usage: sage -python .../v52_retry_pari_ranks.sage E1|E2 rho b effort
# A rank is certified ONLY when rank(proof=True) returns successfully.
from sage.all import QQ, ZZ, EllipticCurve
from sage.env import SAGE_VERSION
import json,sys

kind=sys.argv[1]
rho=ZZ(sys.argv[2])
b=ZZ(sys.argv[3])
effort=ZZ(sys.argv[4]) if len(sys.argv)>4 else ZZ(10)
assert kind in ("E1","E2") and rho>0 and b>0 and ZZ(486)%b==0
T=QQ(rho)/b**2
A=-T**2*(4*T+3)
B=12*(T**2+5*T+3)
C=12*(2-T)
if kind=="E1":
    E=EllipticCurve(QQ,[6,0,8+9*T,0,0])
    P=E([0,0])
    assert 3*P==E(0) and P!=E(0)
else:
    E=EllipticCurve(QQ,[0,B,0,A*C,4*A**2])
    P=E([8*T*(4*T+3),6*T*(4*T+3)*(9*T+8)])
assert E.discriminant()!=0
print("BEGIN",json.dumps(dict(kind=kind,rho=int(rho),b=int(b),
                              T=str(T),pari_effort=int(effort),sage=SAGE_VERSION)),flush=True)
try:
    rank=ZZ(E.rank(proof=True,algorithm="pari",pari_effort=int(effort)))
    print("PROVED_RANK",int(rank),flush=True)
    tors=E.torsion_subgroup()
    torsorder=int(tors.order())
    result={"kind":kind,"rho":int(rho),"b":int(b),
            "rank":int(rank),"torsion_order":torsorder,
            "torsion_invariants":[int(x) for x in tors.invariants()]}
    if kind=="E1" and rank==0 and torsorder==3:
        result.update(status="CERTIFIED_FULL_GENUS2_RATIONAL_POINTS",
                      affine_C_rational_points=0 if not (b*b+rho).is_square() else 4,
                      projective_C_rational_points=2 if not (b*b+rho).is_square() else 6)
    elif kind=="E2" and rank==1 and torsorder==1:
        print("SATURATING_KNOWN_R",flush=True)
        basis,index,reg=E.saturation([P],max_prime=-1)
        assert len(basis)==1
        result.update(status="CERTIFIED_FULL_SECOND_ELLIPTIC_MW_GROUP",
                      free_generators=[str(x) for x in basis],
                      index_of_R=int(index),regulator=str(reg))
    else:
        result["status"]="CERTIFIED_RANK_ONLY_NOT_FULL_GENUS2"
    print(json.dumps(result,indent=2,ensure_ascii=False),flush=True)
except Exception as exc:
    print(json.dumps({"status":"INCOMPLETE_RANK_NOT_PROVED",
                      "kind":kind,"rho":int(rho),"b":int(b),
                      "error_type":type(exc).__name__,
                      "error":str(exc)[:1200]},indent=2),flush=True)
    sys.exit(2)
