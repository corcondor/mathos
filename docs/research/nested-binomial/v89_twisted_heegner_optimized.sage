# v89: PARI ellheegnertwist on the two proven rank-one curves, using a
# conductor-lowering quadratic twist when available. The ordinary
# ellheegner (v88) timed out at 270s on both conductors.
#
# PARI doc: ellheegnertwist(E) automatically starts from a quadratic
# twist of smaller conductor and may be much faster. The algorithm is
# HEURISTIC, but the returned point itself is exact rational arithmetic
# and can be checked on E(Q). No theorem is inferred from a timeout.
# The true algebraic rank1 input is independently certified by v81.
#
# sage -python .../v89_twisted_heegner_optimized.sage 9
from sage.all import *
from sage.env import SAGE_VERSION
import json,sys,time,traceback

rho=ZZ(100003)
b=ZZ(sys.argv[1])
assert b in (9,18)
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
assert E.root_number()==-1 and E.conductor()=={9:486379090935,18:9748577648556}[int(b)]
Emin=E.minimal_model()
toE=Emin.isomorphism_to(E)
t0=time.time()
print("V89_BEGIN",json.dumps({"b":int(b),"rho":int(rho),"sage":SAGE_VERSION,
     "rank_certified":1,"curve_conductor":str(E.conductor()),
     "minimal_model":[str(x) for x in Emin.a_invariants()]}),flush=True)
try:
    F,D=Emin.minimal_quadratic_twist()
    print("V89_OPTIMAL_TWIST",json.dumps({
        "b":int(b),"twist_parameter":str(D),
        "smaller_twist_conductor":str(F.conductor()),
        "original_conductor":str(Emin.conductor()),
        "smaller":bool(F.conductor()<Emin.conductor())}),flush=True)
except Exception as ex:
    print("V89_TWIST_DIAGNOSTIC_UNAVAILABLE",str(ex)[:400],flush=True)
try:
    ep=pari.ellinit(list(Emin.a_invariants()))
    print("V89_HEEGNER_TWIST_START",flush=True)
    pair=ep.ellheegnertwist()
    Q=Emin([QQ(pair[0]),QQ(pair[1])])
    assert Q!=Emin(0) and Q in Emin
    P=toE(Q)
    assert P in E and P[0]!=0
    print("V89_EXACT_FREE_POINT",json.dumps({"b":int(b),
        "point_original":str(P),"point_minimal":str(Q),
        "x_numerator_digits":len(str(P[0].numerator())),
        "x_denominator_digits":len(str(P[0].denominator())),
        "elapsed_s":float(round(time.time()-t0,2))}),flush=True)
    basis,index,reg=E.saturation([P],max_prime=-1)
    assert len(basis)==1
    print("V89_FULL_SATURATION",json.dumps({"b":int(b),
        "basis":[str(x) for x in basis],"index":int(index),
        "regulator":str(reg)}),flush=True)
    pts=list(E.integral_points(mw_base=basis,both_signs=True,verbose=False))
    rows=[];square=[]
    for Q in pts:
        X,Y=ZZ(Q[0]),ZZ(Q[1])
        assert Y*Y+6*b*X*Y+M*Y==X**3
        a2=X+b*b+rho
        row={"X":str(X),"Y":str(Y),"a_squared":str(a2)}
        if X>0 and a2.is_square():
            row["a"]=str(a2.sqrt());square.append(row)
        rows.append(row)
    print("V89_COMPLETE",json.dumps({"status":"CERTIFIED_ALL_INTEGRAL_POINTS",
        "b":int(b),"count":len(rows),"square_lifts":square,
        "all_integral_points":rows,"free_generator":str(basis[0]),
        "saturation_index":int(index)}),flush=True)
except Exception as ex:
    print("V89_INCOMPLETE",json.dumps({"b":int(b),
        "error_type":type(ex).__name__,"error":str(ex)[:1100],
        "trace":traceback.format_exc()[-1500:],
        "elapsed_s":float(round(time.time()-t0,2))}),flush=True)
    sys.exit(2)
