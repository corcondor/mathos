# v68: certified rank and good-ordinary-prime precheck for quadratic Chabauty.
# Source method: Bianchi--Padurariu https://github.com/bianchifrancesca/QC_bielliptic
# Their rank-2 bielliptic genus-two code requires BOTH elliptic factors rank1.
# No claim of complete rational points until an actual QC+MW sieve certificate.
from sage.all import QQ, ZZ, PolynomialRing, EllipticCurve
from sage.env import SAGE_VERSION
import json,sys

T=QQ(sys.argv[1]) if len(sys.argv)>1 else QQ(13)
assert T>0
R=PolynomialRing(QQ,'u')
u=R.gen()
a6=QQ(4)
a4=24-12*T
a2=36+60*T+12*T*T
a0=-T*T*(4*T+3)
f=a6*u**6+a4*u**4+a2*u**2+a0
E1=EllipticCurve(QQ,[0,a4,0,a2*a6,a0*a6*a6])
E2=EllipticCurve(QQ,[0,a2,0,a0*a4,a0*a0*a6])
assert f.degree()==6 and E1.discriminant()!=0 and E2.discriminant()!=0
example_u=QQ(8) if T==13 else QQ(7) if T==4 else None
if example_u is not None:
    val=f(example_u)
    assert val.is_square()
    print("KNOWN_AFFINE_POINT",example_u,val.sqrt(),flush=True)
print("BEGIN",json.dumps({"T":str(T),"sage":SAGE_VERSION,
   "f_coefficients":[str(a0),str(a2),str(a4),str(a6)],
   "E1_a_invariants":[str(v) for v in E1.a_invariants()],
   "E2_a_invariants":[str(v) for v in E2.a_invariants()]}),flush=True)

report={"T":str(T),"rank_certified":{},"good_ordinary_primes":[]}
for name,E in (("E1",E1),("E2",E2)):
    try:
        rank=int(E.rank(proof=True,algorithm="pari",pari_effort=1))
        report["rank_certified"][name]=rank
        print("RANK_PROVED",name,rank,flush=True)
    except Exception as e:
        report["rank_certified"][name]=None
        print("RANK_INCOMPLETE",name,type(e).__name__,str(e)[:400],flush=True)
for p in (5,7,11,13,17,19,23,29,31,37,41,43):
    try:
        if E1.has_good_reduction(p) and E2.has_good_reduction(p) and E1.is_ordinary(p) and E2.is_ordinary(p):
            report["good_ordinary_primes"].append(int(p))
    except Exception as e:
        print("LOCAL_PRIME_SKIPPED",p,type(e).__name__,flush=True)
report["qc_bianchi_padurariu_applicable"]=(report["rank_certified"].get("E1")==1 and report["rank_certified"].get("E2")==1 and bool(report["good_ordinary_primes"]))
print(json.dumps(report,indent=2,ensure_ascii=False),flush=True)
