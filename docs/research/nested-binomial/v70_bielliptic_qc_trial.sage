# v70: actual Bianchi--Padurariu quadratic Chabauty trial on a genus-two fibre
# whose two elliptic quotient ranks are independently PROVED equal to 1 (v69).
# Uses upstream QC_bielliptic at pinned Git commit; not our own implementation.
#
# Requires upstream script at external/QC_bielliptic/qc_g2_bielliptic.sage.
# Usage: sage v70_bielliptic_qc_trial.sage 7 5 14
#
# Important: quadratic Chabauty computes a finite p-adic candidate set.
# If unresolved p-adic points remain, a MW sieve and/or higher precision
# is required. This program never equates no sampled rational points with
# a proof of no rational points.
import sys, json, traceback, time
from sage.all import *
from sage.env import SAGE_VERSION

T=QQ(sys.argv[1]) if len(sys.argv)>1 else QQ(7)
p=ZZ(sys.argv[2]) if len(sys.argv)>2 else ZZ(5)
prec=ZZ(sys.argv[3]) if len(sys.argv)>3 else ZZ(14)
assert T>0 and p>=5 and prec>=10
R=PolynomialRing(QQ,"u")
u=R.gen()
f=4*u**6+(24-12*T)*u**4+(36+60*T+12*T*T)*u**2-T*T*(4*T+3)
a6,a4,a2,a0=f[6],f[4],f[2],f[0]
E1=EllipticCurve(QQ,[0,a4,0,a2*a6,a0*a6*a6])
E2=EllipticCurve(QQ,[0,a2,0,a0*a4,a0*a0*a6])
r1=int(E1.rank(proof=True,algorithm="pari",pari_effort=1))
r2=int(E2.rank(proof=True,algorithm="pari",pari_effort=1))
assert r1==r2==1,(T,r1,r2)
assert E1.has_good_reduction(p) and E2.has_good_reduction(p)
assert E1.is_ordinary(p) and E2.is_ordinary(p)
print("QC_START",json.dumps({"T":str(T),"p":int(p),"precision":int(prec),"sage":SAGE_VERSION,
 "ranks_proved":[r1,r2],"coefficients":[str(a6),str(a4),str(a2),str(a0)]}),flush=True)

upstream="external/QC_bielliptic/qc_g2_bielliptic.sage"
try:
    print("QC_LOADING_PINNED_UPSTREAM",upstream,flush=True)
    load(upstream)
    print("QC_UPSTREAM_LOADED",flush=True)
    start=time.time()
    rational, unresolved=quadratic_chabauty_bielliptic(f,p,prec)
    # Rational points found must satisfy the sextic exactly.
    Hcurve=HyperellipticCurve(f)
    for P in rational:
        if P[2]!=0:
            assert QQ(P[1])**2==f(QQ(P[0]))
    print("QC_FINISHED",json.dumps({
        "T":str(T),"p":int(p),"precision":int(prec),
        "ranks_proved":[r1,r2],"rational_points_found":[str(z) for z in rational],
        "unresolved_padic_candidate_count":len(unresolved),
        "unresolved_padic_candidates":[str(z)[:500] for z in unresolved[:20]],
        "elapsed_seconds":round(time.time()-start,1),
        "status":"NO_UNRESOLVED_QC_CANDIDATES" if len(unresolved)==0 else "REQUIRES_MW_SIEVE_OR_HIGHER_PRECISION",
        "warning":"Complete rational point classification needs published QC precision and MW saturation assumptions verified; a numerical list alone is not a theorem."
    },ensure_ascii=False),flush=True)
except Exception as ex:
    print("QC_INCOMPLETE",json.dumps({
       "T":str(T),"p":int(p),"precision":int(prec),
       "error_type":type(ex).__name__,"message":str(ex)[:1500],
       "trace":traceback.format_exc()[-6000:]
    },ensure_ascii=False),flush=True)
    sys.exit(2)
