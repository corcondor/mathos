# v50: SageMath proof of rank and rational torsion of FIRST elliptic quotient.
# For a fixed rho,b, proves ALL rational points on the associated genus-2
# curve if the elliptic quotient rank is zero and torsion is Z/3.
# Execute: sage -python docs/research/nested-binomial/v50_first_quotient_all_b.sage RHO B
#
# The script NEVER claims the full second elliptic quotient or the original
# nested binomial equation is solved. A rank proof failure is INCOMPLETE.
from sage.all import QQ, ZZ, EllipticCurve
from sage.env import SAGE_VERSION
import json, sys

rho=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(100003)
b=ZZ(sys.argv[2]) if len(sys.argv)>2 else ZZ(1)
assert rho>0 and b>0 and ZZ(486)%b==0
T=QQ(rho)/b**2
E=EllipticCurve(QQ,[6,0,8+9*T,0,0])
P=E([0,0])
assert 3*P==E(0) and P!=E(0)
sq=(b*b+rho).is_square()
meta={"rho":int(rho),"b":int(b),"T":str(T),
      "sage":SAGE_VERSION,"one_plus_T_rational_square":bool(sq)}
print("BEGIN",json.dumps(meta),flush=True)

try:
    rank=E.rank(proof=True,algorithm="pari",pari_effort=1)
    print("PROVED_RANK",int(rank),flush=True)
    tors=E.torsion_subgroup()
    order=int(tors.order())
    invariants=[int(x) for x in tors.invariants()]
    assert order%3==0
    if rank==0 and order==3:
        # The only rational elliptic points are O, P, 2P.
        # The quotient map is x=u²-1-T, y=(s-6x-8-9T)/2.
        # Affine genus-two points must map to x=0 and satisfy u²=1+T.
        if sq:
            root=QQ(b*b+rho).sqrt()/b
            a3=8+9*T
            affine=[(str(uu),str(ss)) for uu in (root,-root)
                    for ss in (a3,-a3)]
        else:
            affine=[]
        status="CERTIFIED_FULL_GENUS2_RATIONAL_POINTS"
        print(json.dumps({**meta,"status":status,"rank_E1":0,
           "torsion_order_E1":3,"torsion_invariants_E1":invariants,
           "affine_C_rational_points":affine,
           "number_affine_C":len(affine),
           "number_rational_infinities":2,
           "number_projective_C_rational_points":len(affine)+2,
           "claim":"ALL rational points of the smooth projective genus-two curve C_T; NOT all points of second elliptic quotient"
        },indent=2),flush=True)
    else:
        print(json.dumps({**meta,
          "status":"NOT_CLASSIFIED_BY_RANK_ZERO_METHOD",
          "rank_E1":int(rank),"torsion_order_E1":order,
          "torsion_invariants_E1":invariants,
          "explanation":"Full genus-two rational points NOT classified; positive rank or unexpected torsion"
        },indent=2),flush=True)
except Exception as err:
    print(json.dumps({**meta,"status":"INCOMPLETE_RANK_NOT_PROVED",
          "error_type":type(err).__name__,
          "error":str(err)[:1200]},indent=2),flush=True)
    sys.exit(2)
