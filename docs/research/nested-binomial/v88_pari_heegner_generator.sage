# v88: direct PARI/GP Heegner point computation on the ACTUAL high-conductor
# rank-one elliptic curves E_{b,100003} for b=9 and b=18.
#
# Unlike a bounded low-height point search, ellheegner computes a rational
# nontorsion point from the modular parametrization, even if its coordinates
# are huge. PARI official manual: ellheegner(E), conditional INPUT is analytic
# rank1. This INPUT was rigorously established in v81 using an L' error bound:
# https://github.com/corcondor/mathos/actions/runs/42480661353
#
# Important: (1) exact rational Heegner point is NOT automatically a
# saturated generator; (2) full integral point classification requires
# E.saturation(...,max_prime=-1) and E.integral_points(); (3) any timeout
# is INCOMPLETE. No unverified non-torsion claim is accepted.
#
# sage -python .../v88_pari_heegner_generator.sage 9
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
Em=E.minimal_model()
iso=Em.isomorphism_to(E)
print("V88_BEGIN",json.dumps({"b":int(b),"rho":int(rho),
    "sage":SAGE_VERSION,"conductor":str(N),
    "analytic_rank_certified":1,
    "v81_proof":"https://github.com/corcondor/mathos/actions/runs/42480661353",
    "minimal_model":[str(z) for z in Em.a_invariants()]}),flush=True)
t0=time.time()
try:
    print("V88_PARI_HEEGNER_BEGIN",flush=True)
    # Both b cases are modular curves of analytic rank exactly 1,
    # so PARI's ellheegner is justified mathematically.
    ep=pari.ellinit(list(Em.a_invariants()))
    hp=ep.ellheegner()
    x=QQ(hp[0]);y=QQ(hp[1])
    Pm=Em([x,y])
    assert Pm!=Em(0)
    assert Pm in Em
    P=iso(Pm)
    assert P in E and P[0]!=0
    # Rational torsion E(Q) = Z/3 proved in v51, so x != 0
    # is an exact proof that P is NON-TORSION, not a height heuristic.
    print("V88_EXACT_NONTORSION_POINT",json.dumps({
       "b":int(b),"P_on_original_model":str(P),
       "P_on_minimal_model":str(Pm),
       "x_num_digits":len(str(P[0].numerator())),
       "x_den_digits":len(str(P[0].denominator())),
       "elapsed_seconds":float(round(time.time()-t0,2))}),flush=True)
    print("V88_FULL_SATURATION_BEGIN",flush=True)
    basis,index,reg=E.saturation([P],max_prime=-1)
    assert len(basis)==1 and index>=1
    print("V88_SATURATED_FREE_GENERATOR",json.dumps({
       "b":int(b),"generator":str(basis[0]),
       "index":int(index),"regulator":str(reg),
       "saturation_verified":True,
       "rank_proved_by_v81":1}),flush=True)
    print("V88_ALL_INTEGRAL_POINT_SEARCH_BEGIN",flush=True)
    pts=list(E.integral_points(mw_base=basis,both_signs=True,verbose=False))
    rows=[];lifted=[]
    for Q in pts:
        X,Y=ZZ(Q[0]),ZZ(Q[1])
        assert Y*Y+6*b*X*Y+M*Y==X**3
        a2=X+b*b+rho
        row={"X":str(X),"Y":str(Y),"a_squared":str(a2)}
        if X>0 and a2.is_square():
            row["a"]=str(a2.sqrt())
            lifted.append(row)
        rows.append(row)
    print("V88_COMPLETE_ALL_INTEGRAL_POINTS",json.dumps({
       "status":"CERTIFIED_FULL_INTEGRAL_POINTS",
       "b":int(b),"rho":int(rho),"rank":1,
       "generator":str(basis[0]),
       "integral_point_count":len(rows),
       "positive_X_square_lifts":lifted,
       "full_points":rows,
       "elapsed_seconds":float(round(time.time()-t0,2))}),flush=True)
except Exception as ex:
    print("V88_INCOMPLETE",json.dumps({
        "b":int(b),
        "error_type":type(ex).__name__,"error":str(ex)[:1200],
        "trace":traceback.format_exc()[-1500:],
        "elapsed_seconds":float(round(time.time()-t0,2))}),flush=True)
    sys.exit(2)
