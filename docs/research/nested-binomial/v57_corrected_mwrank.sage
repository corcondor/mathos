# v57: corrected Sage rank proof attempt for the remaining E1/E2 fibres.
# The previous v53 used algorithm="mwrank" which is NOT accepted by Sage's
# EllipticCurve_rational_field.rank(). Correct choices are mwrank_lib,
# mwrank_shell and pari; this script uses mwrank_lib.
# Usage: sage -python .../v57_corrected_mwrank.sage E1|E2 rho b
from sage.all import QQ, ZZ, EllipticCurve
from sage.env import SAGE_VERSION
import json, sys

kind=sys.argv[1]; rho=ZZ(sys.argv[2]); b=ZZ(sys.argv[3])
assert kind in ("E1","E2") and rho>0 and b>0 and ZZ(486)%b==0
T=QQ(rho)/b**2
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
E=(EllipticCurve(QQ,[6,0,8+9*T,0,0]) if kind=="E1"
   else EllipticCurve(QQ,[0,B,0,A*C,4*A*A]))
print("BEGIN",json.dumps({"kind":kind,"rho":int(rho),"b":int(b),
                         "sage":SAGE_VERSION,"algorithm":"mwrank_lib",
                         "T":str(T)}),flush=True)
try:
    rank=E.rank(proof=True,algorithm="mwrank_lib")
    print("PROVED_RANK_BY_MWRANK_LIB",int(rank),flush=True)
    tors=E.torsion_subgroup()
    obj={"status":"CERTIFIED_RANK","kind":kind,"rho":int(rho),
         "b":int(b),"rank":int(rank),"torsion_order":int(tors.order()),
         "torsion_invariants":[int(x) for x in tors.invariants()]}
    if kind=="E1" and rank==0 and tors.order()==3:
        assert not (b*b+rho).is_square()
        obj["status"]="CERTIFIED_ALL_GENUS2_RATIONAL_POINTS"
        obj["genus2_affine_points"]=0
        obj["genus2_projective_points"]=2
    print(json.dumps(obj,indent=2),flush=True)
except Exception as e:
    print(json.dumps({"status":"INCOMPLETE","error_type":type(e).__name__,
                      "error":str(e)[:900]},indent=2),flush=True)
    sys.exit(2)
