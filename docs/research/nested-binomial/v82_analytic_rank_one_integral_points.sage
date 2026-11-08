# v82: use v81's independently certified algebraic rank ONE, then search,
# fully saturate one nontorsion point and enumerate ALL original-model
# integral points. This route bypasses the inconclusive [0,1] 2-descent.
#
# IMPORTANT: the rank-one proof itself is the separate v81 run
#   https://github.com/corcondor/mathos/actions/runs/42480661353
# and Sage's rigorously bounded L'(E,1) values. We verify the exact curve
# and conductor in this script but DO NOT recompute millions of L coefficients.
# For rank1, E.saturation([P],max_prime=-1) gives a proven FULL free basis
# if E.saturation reports success. Integral point enumeration uses that basis.
#
# sage -python docs/research/nested-binomial/v82_analytic_rank_one_integral_points.sage 9
from sage.all import *
from sage.env import SAGE_VERSION
import json,sys,time,traceback
rho=ZZ(100003)
b=ZZ(sys.argv[1])
assert b in (9,18)
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
N={9:ZZ(486379090935),18:ZZ(9748577648556)}[int(b)]
assert E.conductor()==N and E.root_number()==-1
assert E.discriminant()!=0
# Rational torsion is exactly Z/3 (v51 two finite-field cardinalities).
T0=E([0,0])
assert 3*T0==E(0) and T0!=E(0)
print("V82_BEGIN",json.dumps({"sage":SAGE_VERSION,"rho":int(rho),
 "b":int(b),"model":[str(x) for x in E.a_invariants()],
 "rank_one_certified_by":"v81 Lprime nonvanishing and Gross-Zagier-Kolyvagin",
 "Lprime_proof_run":"https://github.com/corcondor/mathos/actions/runs/42480661353",
 "conductor":str(N),"torsion":"Z/3"}),flush=True)
start=time.time()
try:
    Emin=E.minimal_model()
    iso=Emin.isomorphism_to(E)
    print("V82_MINIMAL_MODEL",json.dumps({"b":int(b),
         "model":[str(x) for x in Emin.a_invariants()]}),flush=True)
    candidates=[]
    # Search logarithmic naive heights sequentially; tight CPU bound is
    # enforced by the GitHub Actions runner.
    for height in (3,5,7):
        print("V82_POINT_SEARCH_START",json.dumps({"b":int(b),
            "height":height}),flush=True)
        found=Emin.point_search(height,rank_bound=1)
        for Pmin in found:
            P=iso(Pmin)
            if P==E(0) or P[0]==0: continue  # Q-torsion exactly Z/3
            assert P in E
            candidates.append(P)
        if candidates:
            print("V82_NONTORSION_FOUND",json.dumps({"b":int(b),
                 "height":height,"point":str(candidates[0])}),flush=True)
            break
    if not candidates:
        raise RuntimeError("No nontorsion generator found to logarithmic height 7; theorem rank=1 still holds")
    # This is a full saturation, NOT a small-prime-only check.
    print("V82_FULL_SATURATION_START",flush=True)
    basis,index,regulator=E.saturation([candidates[0]],max_prime=-1)
    assert len(basis)==1 and index>=1
    P=basis[0]
    assert P!=E(0) and P[0]!=0
    print("V82_FULL_BASIS",json.dumps({"b":int(b),"free_generator":str(P),
         "saturation_index":int(index),"regulator":str(regulator),
         "basis_certification":"full saturation + independently proved rank1"}),flush=True)
    points=E.integral_points(mw_base=basis,both_signs=True,verbose=False)
    entries=[]
    squares=[]
    for Q in points:
        X,Y=map(ZZ,Q[:2])
        assert Y*Y+6*b*X*Y+M*Y==X**3
        z=X+b*b+rho
        row={"X":str(X),"Y":str(Y),"a_squared":str(z)}
        if X>0 and z.is_square():
            a=z.sqrt()
            row["a"]=str(a)
            squares.append(row)
        entries.append(row)
    result={"status":"V82_ALL_INTEGRAL_POINTS_CERTIFIED",
      "b":int(b),"rho":int(rho),"rank":1,"full_generator":str(P),
      "index_initial_to_full":int(index),
      "integral_points":entries,"integral_point_count":len(entries),
      "positive_X_integer_square_candidates":squares,
      "time_seconds":float(round(time.time()-start,2)),
      "qualification":"All integral points in the exact original model; does not classify all rational points of genus-two curve"}
    print("V82_COMPLETE",json.dumps(result,ensure_ascii=False),flush=True)
except Exception as ex:
    print("V82_INCOMPLETE",json.dumps({
        "b":int(b),"reason":type(ex).__name__+": "+str(ex)[:1200],
        "trace":traceback.format_exc()[-1200:],
        "time_seconds":float(round(time.time()-start,2))}),flush=True)
    sys.exit(2)
