# v78: independent analytic rank-zero certification candidate
# for the two rho=100003 original fibres whose 2-descent stopped at rank0..1.
#
# Crucial: E.lseries().L_ratio() is exact only subject to a Manin constant
# condition, which Sage documents. We therefore record it as observational
# UNLESS a precise independent Manin bound has been established.
# If an exact modular symbol shows L(E,1)!=0, Kolyvagin proves MW rank0.
# A vanishing central L-value does NOT prove rank1 without a certified
# non-torsion point or a rank-one nonvanishing theorem.
from sage.all import *
from sage.env import SAGE_VERSION
import sys,json,time
rho=ZZ(100003)
b=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(9)
assert b in (9,18)
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
print("V78_BEGIN",json.dumps({"sage":SAGE_VERSION,"rho":int(rho),"b":int(b),
    "model":[str(v) for v in E.a_invariants()]}),flush=True)
for name,fn in [
    ("root_number",lambda:int(E.root_number())),
    ("conductor",lambda:str(E.conductor())),
    ("rank_bounds",lambda:[int(v) for v in E.rank_bounds(algorithm="pari")]),
    ("analytic_rank_pari_NONPROOF",lambda:int(E.analytic_rank(algorithm="pari"))),
    ("L_ratio_NOT_AUTOMATICALLY_CERTIFIED",lambda:str(E.lseries().L_ratio())),
    ("modular_symbol_sign_plus_at_zero",lambda:str(E.modular_symbol(sign=1)(QQ(0)))),
]:
    start=time.time()
    try:
        result=fn()
        print("V78_RESULT",json.dumps({"b":int(b),"check":name,
             "value":result,"elapsed_s":float(round(time.time()-start,2))}),flush=True)
    except Exception as exc:
        print("V78_UNAVAILABLE",json.dumps({"b":int(b),"check":name,
             "error":type(exc).__name__+":"+str(exc)[:500],
             "elapsed_s":float(round(time.time()-start,2))}),flush=True)
print("V78_FINISHED",json.dumps({"b":int(b),
    "interpretation":"Numerical analytic rank and L_ratio require independent proof checks; never guess Mordell-Weil rank."}),flush=True)
