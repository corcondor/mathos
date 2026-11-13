# v81: analytically certify rank ONE for the two remaining rho=100003 fibres.
# WHY: both b=9 and b=18 have two-descent rank bounds [0,1] but rank
# was not proved by PARI effort20. The functional equation sign is -1,
# so exact nonzero L'(E,1), with a documented rigorous numerical error
# bound, implies algebraic rank1 by Gross--Zagier and Kolyvagin.
#
# Sage's E.lseries().deriv_at1(k,prec) returns (value,err) with an
# EXPLICIT PROVEN error bound; do not confuse with unbounded numerical
# pari analytic_rank (diagnostic only) or conjectural BSD.
#
# The output is CERTIFIED_ANALYTIC_RANK_ONE only if abs(value)>2*err
# and root_number=-1. A failure/timeout is INCOMPLETE, not rank0.
# Usage: sage -python .../v81_rigorous_Lprime_rank_one.sage 9
from sage.all import *
from sage.env import SAGE_VERSION
from sage.functions.log import log
from sage.symbolic.constants import pi
import sys,json,time

b=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(9)
rho=ZZ(100003)
assert b in (9,18)
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
N=ZZ(E.conductor())
root=ZZ(E.root_number())
print("V81_BEGIN",json.dumps({"sage":SAGE_VERSION,"rho":int(rho),"b":int(b),
   "conductor":str(N),"root_number":int(root)}),flush=True)
assert root==-1
try:
    # Estimate only for choosing the minimum rigorous truncation length.
    r,estimate=E.analytic_rank(algorithm="pari",leading_coefficient=True)
    print("V81_NUMERIC_ESTIMATE_NOT_PROOF",json.dumps({
        "pari_estimated_analytic_rank":int(r),"Lprime_estimate":str(estimate)}),flush=True)
    assert int(r)==1 and abs(estimate)>0
    rootN=RealField(100)(N).sqrt()
    # Tail estimate from Sage's documented rigorous deriv_at1 algorithm.
    est=abs(RealField(100)(estimate))
    k=ZZ(ceil(rootN/(2*RealField(100).pi()) *
        log(100*rootN/(RealField(100).pi()*est))))+50
    k=max(1000,int(k))
    # Avoid unbounded GitHub CPU/memory spending.
    if k>10000000:
        print("V81_INCOMPLETE",json.dumps({
            "reason":"rigorous truncation requires more than ten million coefficients",
            "k":k}),flush=True)
        sys.exit(2)
    print("V81_RIGOROUS_SERIES_REQUEST",json.dumps({"k":k,
      "sqrt_conductor":str(rootN)}),flush=True)
    start=time.time()
    val,err=E.lseries().deriv_at1(k=k,prec=128)
    print("V81_RIGOROUS_SERIES_RESULT",json.dumps({
       "Lprime_value":str(val),"rigorous_absolute_error_bound":str(err),
       "terms":k,"elapsed_seconds":float(round(time.time()-start,1))}),flush=True)
    if abs(val)>2*err:
        print("V81_CERTIFIED_RANK_ONE",json.dumps({
           "rho":int(rho),"b":int(b),"conductor":str(N),
           "functional_equation_sign":-1,
           "Lprime_nonzero_by_error_bound":True,
           "algebraic_Mordell_Weil_rank":1,
           "proof_theorem":"Gross-Zagier + Kolyvagin (modularity of E/Q); no Sha finiteness assumption",
           "limitations":"No full saturated basis or integral point set yet",
           "k_terms":k}),flush=True)
    else:
        print("V81_INCOMPLETE",json.dumps({"reason":"Lprime interval contains zero",
          "terms":k}),flush=True)
        sys.exit(2)
except Exception as exc:
    print("V81_INCOMPLETE",json.dumps({"reason":type(exc).__name__,
       "message":str(exc)[:900]}),flush=True)
    sys.exit(2)
