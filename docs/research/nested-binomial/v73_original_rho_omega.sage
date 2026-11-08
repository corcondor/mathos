# v73: screen the real residual rho=100003 for Bianchi-Padurariu QC.
# b|486, rho mod9=1, and both elliptic quotient ranks are proved 1
# for b=81,162,243 (v72).
#
# The integer polynomial F(a,b,rho) is Q-isomorphic to
# C_{rho/b²} via a=b*u, S=b³*s. This is needed because
# the published QC routine requires a6,a4,a2,a0 all integral.
#
# Usage: sage .../v73_original_rho_omega.sage 81 7
# This ONLY computes the p-adic bad-prime Omega set size.
from sage.all import *
from sage.env import SAGE_VERSION
import json,sys,time

b=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(81)
p=ZZ(sys.argv[2]) if len(sys.argv)>2 else ZZ(7)
rho=ZZ(100003)
assert 486%b==0 and b in (81,162,243)
assert rho%9 in (1,4,6,7)
R=PolynomialRing(QQ,"a")
a=R.gen()
b2=b*b
f=4*a**6+(24*b2-12*rho)*a**4+(36*b2*b2+60*b2*rho+12*rho*rho)*a**2-3*b2*rho*rho-4*rho**3
assert all(c in ZZ for c in f.list())
a6,a4,a2,a0=f[6],f[4],f[2],f[0]
E1=EllipticCurve(QQ,[0,a4,0,a2*a6,a0*a6*a6])
E2=EllipticCurve(QQ,[0,a2,0,a0*a4,a0*a0*a6])
assert E1.has_good_reduction(p) and E2.has_good_reduction(p)
assert E1.is_ordinary(p) and E2.is_ordinary(p)
print("ORIGINAL_RESIDUAL_OMEGA_BEGIN",json.dumps({"rho":int(rho),"b":int(b),
    "T":str(QQ(rho)/b2),"p":int(p),"sage":SAGE_VERSION}),flush=True)
load("external/QC_bielliptic/qc_g2_bielliptic.sage")
try:
    start=time.time()
    omega=Omega_set(f,p,10,Es=[E1,E2],Emins=[E1.minimal_model(),E2.minimal_model()])
    print("ORIGINAL_RESIDUAL_OMEGA_SUCCESS",json.dumps({"rho":int(rho),
        "b":int(b),"p":int(p),"omega_count":int(len(omega)),
        "elapsed_seconds":float(round(time.time()-start,1)),
        "warning":"This is only an Omega cardinality; no rational-point classification."}),flush=True)
except Exception as ex:
    print("ORIGINAL_RESIDUAL_OMEGA_INCOMPLETE",json.dumps({
        "b":int(b),"error":type(ex).__name__,"message":str(ex)[:500]}),flush=True)
    sys.exit(2)
