# v62: certify full C_T(Q) for the ONE possible 9-torsion fibre,
# T=46648/9, E1: y²+6xy+46656y=x³.
# All b|486 cases with 9-torsion necessarily have this same T (v61).
# PARI rank(proof=True) is required; no numeric guess accepted.
from sage.all import QQ,ZZ,EllipticCurve
from sage.env import SAGE_VERSION
import json,sys
T=QQ(46648)/9
E=EllipticCurve(QQ,[6,0,46656,0,0])
Q=E([-648,-7776])
O=E(0)
assert 3*Q==E([0,0])
assert 9*Q==O and 3*Q!=O
tors=E.torsion_subgroup()
assert int(tors.order())==9
x_values=[]
for k in range(1,9):
    P=k*Q
    u2=P[0]+1+T
    x_values.append(dict(k=k,x=str(P[0]),u_squared=str(u2),
                         u_rational=bool(u2.is_square())))
assert all(not a["u_rational"] for a in x_values)
print("BEGIN",json.dumps({"sage":SAGE_VERSION,"T":str(T),
    "torsion_order":9,"torsion_points":x_values},indent=2),flush=True)
try:
    rank=E.rank(proof=True,algorithm="pari",pari_effort=1)
    print("PROVED_RANK",int(rank),flush=True)
    if rank!=0:
        print(json.dumps({"status":"NOT_CLASSIFIED_POSITIVE_RANK",
              "rank":int(rank),"reason":"9 torsion points alone do not list all rational E points"}),flush=True)
        sys.exit(2)
    print(json.dumps({
        "status":"CERTIFIED_ALL_RATIONAL_GENUS2_POINTS",
        "T":str(T),"rank_E1":0,"torsion_E1":"Z/9",
        "affine_C_rational_points":0,"projective_C_rational_points":2,
        "claim":"Every rational point of C_T is one of the two points at infinity"
    },indent=2),flush=True)
except Exception as exc:
    print(json.dumps({"status":"INCOMPLETE_RANK_NOT_PROVED",
                      "error_type":type(exc).__name__,
                      "error":str(exc)[:1100]}),flush=True)
    sys.exit(2)
