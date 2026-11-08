# v84: 3-isogeny-assisted search for a provably non-torsion rational point.
# Analytic rank1 for rho=100003,b=9,18 is rigorously certified by v81:
# https://github.com/corcondor/mathos/actions/runs/42480661353
#
# The original E has a rational point of exact order3, P=(0,0).
# Apply an actual Sage 3-isogeny phi:E->E' with kernel <P>; search
# the MINIMAL E' for a nontorsion point, push it back by the dual isogeny,
# and fully saturate in E. If successful, enumerate all E-integral points.
# Any incomplete search / saturation / integral-points call is flagged
# INCOMPLETE; the already certified rank1 is unchanged.
#
# sage -python .../v84_three_isogeny_free_point.sage 9
from sage.all import *
from sage.env import SAGE_VERSION
import json,sys,time,traceback

rho=ZZ(100003)
b=ZZ(sys.argv[1])
assert b in (9,18)
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
assert E.conductor()=={9:486379090935,18:9748577648556}[int(b)]
T3=E([0,0])
assert 3*T3==E(0) and T3!=E(0)
start=time.time()
print("V84_BEGIN",json.dumps({"b":int(b),"rho":int(rho),
 "certified_algebraic_rank":1,"rank_certificate":"v81 Lprime nonvanishing",
 "sage":SAGE_VERSION}),flush=True)
try:
    phi=E.isogeny(T3)
    assert phi.degree()==3
    dual=phi.dual()
    Et=phi.codomain()
    Em=Et.minimal_model()
    toEt=Em.isomorphism_to(Et)
    toE=dual.codomain().isomorphism_to(E)
    print("V84_3ISOGENY",json.dumps({"b":int(b),
       "degree":int(phi.degree()),
       "codomain_model":[str(x) for x in Et.a_invariants()],
       "codomain_minimal":[str(x) for x in Em.a_invariants()]}),flush=True)
    candidates=[]
    for height in (8,10,12):
        tic=time.time()
        print("V84_SEARCH_START",json.dumps({"b":int(b),"height":height}),flush=True)
        points=Em.point_search(height,rank_bound=2)
        mapped=[]
        for P in points:
            Q=toE(dual(toEt(P)))
            if Q!=E(0) and Q[0]!=0:  # E(Q)_tors=Z/3 (v51)
                mapped.append(Q)
        print("V84_SEARCH_RESULT",json.dumps({"b":int(b),
            "height":height,"number_points_on_Eprime":len(points),
            "nontorsion_images":[str(P)[:600] for P in mapped[:5]],
            "seconds":float(round(time.time()-tic,2))}),flush=True)
        if mapped:
            candidates=mapped
            break
    if not candidates:
        raise RuntimeError("No nontorsion point found on 3-isogenous curve through logarithmic height 12")
    P=candidates[0]
    print("V84_NONTORSION",json.dumps({"b":int(b),"point":str(P)}),flush=True)
    print("V84_SATURATION_START",flush=True)
    basis,index,reg=E.saturation([P],max_prime=-1)
    assert len(basis)==1 and index>=1 and basis[0][0]!=0
    print("V84_FULL_MW_BASIS",json.dumps({
        "b":int(b),"free_generator":str(basis[0]),
        "saturation_index":int(index),"regulator":str(reg),
        "rank_proof":"v81","full_saturation":True}),flush=True)
    points=E.integral_points(mw_base=basis,both_signs=True,verbose=False)
    rows=[]
    for Q in points:
        X,Y=map(ZZ,Q[:2])
        assert Y*Y+6*b*X*Y+M*Y==X**3
        z=X+b*b+rho
        rows.append({"X":str(X),"Y":str(Y),"a_squared":str(z),
                     "positive_square_lift":bool(X>0 and z.is_square())})
    print("V84_ALL_INTEGRAL_POINTS",json.dumps({
        "status":"COMPLETE_CERTIFIED","b":int(b),"rank":1,
        "number_integral_points":len(rows),
        "positive_square_lifts":[z for z in rows if z["positive_square_lift"]],
        "all_integral_points":rows,
        "free_basis":[str(x) for x in basis],
        "saturation_index":int(index),
        "seconds":float(round(time.time()-start,2))}),flush=True)
except Exception as ex:
    print("V84_INCOMPLETE",json.dumps({"b":int(b),
        "error":type(ex).__name__+": "+str(ex)[:1200],
        "trace":traceback.format_exc()[-1800:],
        "seconds":float(round(time.time()-start,2))}),flush=True)
    sys.exit(2)
