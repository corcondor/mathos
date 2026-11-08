# v71: screen the exact size of the p-adic height correction set Omega
# for all eight proved rank1+rank1 bielliptic fibres. This counts
# required quadratic Chabauty work but does NOT compute rational points.
from sage.all import *
import sys,time,json
source="external/QC_bielliptic/qc_g2_bielliptic.sage"
load(source)
R=PolynomialRing(QQ,'u')
u=R.gen()
fibres=[(7,5),(9,19),(11,5),(18,7),(19,7),(22,5),(29,11),(32,5)]
results=[]
for t,p in fibres:
    T=QQ(t)
    f=4*u**6+(24-12*T)*u**4+(36+60*T+12*T*T)*u**2-T*T*(4*T+3)
    a6,a4,a2,a0=f[6],f[4],f[2],f[0]
    E1=EllipticCurve(QQ,[0,a4,0,a2*a6,a0*a6*a6])
    E2=EllipticCurve(QQ,[0,a2,0,a0*a4,a0*a0*a6])
    assert E1.has_good_reduction(p) and E2.has_good_reduction(p)
    start=time.time()
    try:
        Omega=Omega_set(f,p,10,Es=[E1,E2],Emins=[E1.minimal_model(),E2.minimal_model()])
        res={"T":t,"p":p,"Omega_count":len(Omega),"seconds":round(time.time()-start,1)}
        print("OMEGA_RESULT",json.dumps(res),flush=True)
        results.append(res)
    except Exception as e:
        res={"T":t,"p":p,"error":type(e).__name__+":"+str(e)[:300]}
        print("OMEGA_INCOMPLETE",json.dumps(res),flush=True)
        results.append(res)
print("OMEGA_SCREEN_COMPLETE",json.dumps(results,ensure_ascii=False),flush=True)
