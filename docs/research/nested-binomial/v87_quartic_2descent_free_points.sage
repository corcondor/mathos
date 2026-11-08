# v87: quartic-cover 2-descent instead of repeated low-height searches.
#
# For the two actual first elliptic quotients E_{b,100003}, b=9,18,
# rank=1 has been rigorously proved by the v81 L'(E,1) interval:
# https://github.com/corcondor/mathos/actions/runs/42480661353
# But v82/v84 direct points searches to log height12 yielded no free
# point. This program tries eclib/Cremona two_descent with an explicit
# quartic second-stage sieve. It never calls a point a full MW generator
# until full saturation has been verified.
#
# Sage 10.10: sage -python .../v87_quartic_2descent_free_points.sage 9
from sage.all import *
from sage.env import SAGE_VERSION
from sage.libs.eclib.interface import mwrank_EllipticCurve
import sys,json,time,traceback
rho=ZZ(100003)
b=ZZ(sys.argv[1])
assert b in (9,18)
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
assert E.conductor()=={9:486379090935,18:9748577648556}[int(b)]
Em=E.minimal_model()
back=Em.isomorphism_to(E)
start=time.time()
print("V87_BEGIN",json.dumps({
    "sage":SAGE_VERSION,"rho":int(rho),"b":int(b),
    "rank_analytic_proof":"v81; Gross-Zagier-Kolyvagin",
    "minimal_model":[str(z) for z in Em.a_invariants()]}),flush=True)
try:
    MWC=mwrank_EllipticCurve(list(Em.a_invariants()))
    # Quartic two-descent searches on everywhere locally soluble
    # spaces; second_limit is a *logarithmic* bound, not a proof cutoff.
    print("V87_QUARTIC_DESCENT_START",json.dumps({
      "first_limit":30,"second_limit":17}),flush=True)
    MWC.two_descent(verbose=False,selmer_only=False,
                   first_limit=30,second_limit=17,second_descent=True)
    print("V87_QUARTIC_DESCENT_RESULT",json.dumps({
      "rank_lower_bound":int(MWC.rank()),
      "known_eclib_basis":[str(z) for z in MWC.gens()],
      "elapsed_s":float(round(time.time()-start,2))}),flush=True)
    # The lower bound can be 0 even though the true rank=1.
    pts=[]
    for g in MWC.gens():
        Pmin=Em([QQ(z) for z in g])
        if Pmin==Em(0):continue
        P=back(Pmin)
        if P[0]!=0:
            assert P in E
            pts.append(P)
    if not pts:
        raise RuntimeError("No certified nontorsion point recovered by quartic covering search")
    print("V87_FREE_POINT",json.dumps({"b":int(b),
       "point":str(pts[0])}),flush=True)
    basis,index,reg=E.saturation([pts[0]],max_prime=-1)
    assert len(basis)==1 and index>=1
    print("V87_SATURATED_BASIS",json.dumps({
       "b":int(b),"generator":str(basis[0]),"index":int(index),
       "regulator":str(reg)}),flush=True)
    points=list(E.integral_points(mw_base=basis,both_signs=True,verbose=False))
    square=[]
    all_points=[]
    for P in points:
        X,Y=ZZ(P[0]),ZZ(P[1])
        assert Y*Y+6*b*X*Y+M*Y==X**3
        av=X+b*b+rho
        row={"X":str(X),"Y":str(Y),"a_squared":str(av)}
        if X>0 and av.is_square():
            row["a"]=str(av.sqrt());square.append(row)
        all_points.append(row)
    print("V87_ALL_INTEGRAL_POINTS",json.dumps({
      "status":"CERTIFIED_ALL_INTEGRAL_POINTS",
      "b":int(b),"rank":1,"saturation_index":int(index),
      "generator":str(basis[0]),
      "integral_point_count":len(all_points),
      "positive_square_lifts":square,
      "full_integral_points":all_points,
      "elapsed_s":float(round(time.time()-start,2))}),flush=True)
except Exception as exc:
    print("V87_INCOMPLETE",json.dumps({
       "b":int(b),"error_type":type(exc).__name__,
       "error":str(exc)[:1200],
       "traceback":traceback.format_exc()[-1200:],
       "elapsed_s":float(round(time.time()-start,2))}),flush=True)
    sys.exit(2)
