# v53: independent mwrank-based attempts on unresolved fibres.
# Outputs rigorously proved ranks only when Sage returns with proof=True.
# For E1 with known 0<=rank<=1, an explicit non-3-torsion rational point
# also proves rank=1; this is reported separately from a full MW basis.
from sage.all import QQ, ZZ, EllipticCurve
from sage.env import SAGE_VERSION
import sys,json

kind=sys.argv[1];rho=ZZ(sys.argv[2]);b=ZZ(sys.argv[3])
assert kind in ("E1","E2") and rho>0 and 486%b==0
T=QQ(rho)/b**2
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
E=(EllipticCurve(QQ,[6,0,8+9*T,0,0]) if kind=="E1"
   else EllipticCurve(QQ,[0,B,0,A*C,4*A*A]))
print("BEGIN",json.dumps(dict(kind=kind,rho=int(rho),b=int(b),
    sage=SAGE_VERSION)),flush=True)
try:
    print("ROOT_NUMBER",int(E.root_number()),flush=True)
except Exception as e:
    print("ROOT_NUMBER_UNAVAILABLE",str(e)[:250],flush=True)
try:
    rank=E.rank(proof=True,algorithm="mwrank")
    print("PROVED_RANK_BY_MWRANK",int(rank),flush=True)
    print(json.dumps({"status":"CERTIFIED_RANK","kind":kind,
                      "rho":int(rho),"b":int(b),"rank":int(rank)},indent=2),flush=True)
except Exception as e:
    print("MWRANK_RANK_PROOF_UNAVAILABLE",type(e).__name__,str(e)[:800],flush=True)

# This is only a point search, not a full basis certification.
try:
    pts=list(E.gens(proof=False))
    print("FOUND_GENERATORS_UNCERTAIN",len(pts),[str(x) for x in pts],flush=True)
    if kind=="E1":
        nontrivial=[P for P in pts if P!=E(0) and P[0]!=0]
        if nontrivial:
            print(json.dumps({"status":"CERTIFIED_NONTORSION_POINT",
              "kind":kind,"rho":int(rho),"b":int(b),
              "point":str(nontrivial[0]),
              "reason":"rational torsion is exactly Z/3 and all nonzero torsion x=0",
              "rank_upper_bound_from_previous_pari":1},indent=2),flush=True)
except Exception as e:
    print("POINT_SEARCH_INCOMPLETE",type(e).__name__,str(e)[:800],flush=True)
print("DONE: see individual proof and uncertainty markers",flush=True)
