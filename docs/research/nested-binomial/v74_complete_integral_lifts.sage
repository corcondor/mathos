# v74: COMPLETE integral points on an integral first-quotient model,
# and exact reconstruction of original integer candidates.
#
# Executed with SageMath:
#   sage -python docs/research/nested-binomial/v74_complete_integral_lifts.sage RHO B
#
# Important: this calls integral_points() with a certified full MW basis.
# It is not a small-height search. On large fibres it may be too expensive,
# in which case the program reports INCOMPLETE, never 'no solution'.
from sage.all import *
from sage.env import SAGE_VERSION
from math import gcd, comb
import json,sys,time,traceback

rho=ZZ(sys.argv[1]) if len(sys.argv)>1 else ZZ(7)
b=ZZ(sys.argv[2]) if len(sys.argv)>2 else ZZ(1)
pari_effort=int(sys.argv[3]) if len(sys.argv)>3 else 1
assert 1<=pari_effort<=40
assert rho>0 and b>0 and ZZ(486)%b==0
M=b*(8*b*b+9*rho)
E=EllipticCurve(QQ,[6*b,0,M,0,0])
assert E.discriminant()!=0
print("V74_BEGIN",json.dumps({"rho":int(rho),"b":int(b),
   "sage":SAGE_VERSION,"pari_effort":pari_effort,"integral_model_ainvariants":[str(v) for v in E.a_invariants()],
   "original_lift_equation":"X=a²-b²-rho; Y²+6bXY+b(8b²+9rho)Y=X³",
   "mathematical_scope":"ALL integral points on THIS chosen integral Weierstrass model, provided proven saturated MW generators"}),flush=True)

def lucas(n,k,p):
    if not (0<=k<=n):return 0
    v=1
    while n or k:
        nn=n%p;kk=k%p
        if kk>nn:return 0
        v=v*comb(nn,kk)%p
        n//=p;k//=p
    return v

prime_list=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103)
def original_congruence_witness(n,k):
    A=n*(n-1)*(n-2)//6
    r=3*n+k
    # Here k is t; both original branches have lower choose index r.
    target=(n*n,6*n-9)
    for K in (r,A-r):
        if K<0 or K>A: return [{"invalid_original_k":str(K)}]
    out=[]
    for K in (r,A-r):
        example=None
        for p in prime_list:
            left=lucas(A,r,p)
            right=(lucas(*target,p)+(K*K)%p)%p
            if left!=right:
                example={"prime":p,"lhs":left,"rhs":right}
                break
        out.append({"k":str(K),"disproved_mod_prime":example})
    return out

try:
    t0=time.time()
    rank=ZZ(E.rank(proof=True,algorithm="pari",pari_effort=pari_effort))
    basis=list(E.gens(proof=True))
    certain=bool(E.gens_certain())
    print("V74_MW",json.dumps({"rank_proved":int(rank),
       "basis":[str(P) for P in basis],"gens_certain":certain,
       "seconds":float(round(time.time()-t0,1))}),flush=True)
    if len(basis)!=rank or not certain:
        raise RuntimeError("Sage could not prove a complete saturated Mordell-Weil free basis")
    # The docs state complete integral_points if a full MW basis is supplied.
    points=list(E.integral_points(mw_base=basis,both_signs=True,verbose=False))
    records=[]
    original_candidates=[]
    square_count=0
    for P in points:
        X=ZZ(P[0]);Y=ZZ(P[1])
        assert Y*Y+6*b*X*Y+M*Y==X*X*X
        a2=X+b*b+rho
        row={"X":str(X),"Y":str(Y),"a_squared":str(a2)}
        if a2>0 and a2.is_square() and X>0:
            a=ZZ(a2.sqrt())
            S=2*Y+6*b*X+M
            target=(6*b*X+M)**2+4*X**3
            assert S*S==target
            # Independent explicit sextic identity:
            F=(4*a**6+(24*b*b-12*rho)*a**4+
               (36*b**4+60*b*b*rho+12*rho*rho)*a*a-
               3*b*b*rho*rho-4*rho**3)
            assert F==S*S
            row["a"]=str(a)
            row["S"]=str(S)
            square_count+=1
            if rho%9 in (1,4,6,7) and gcd(int(a),int(b))==1 and gcd(int(a),int(rho))==gcd(int(a),3):
                if (a*a-rho)%b==0 and (rho-a-b)%2==0:
                    num=2*a*(a*a+3*b*b)-rho*(3*b+2*a)+S
                    den=2*b*rho
                    if num%den==0:
                        t=ZZ(num//den)
                        if t>0:
                            nt=b*b*(t*t+3*t+3)+a*b*(t+6)-a*a+rho
                            if nt%(9*a*b)==0:
                                n=ZZ(nt//(9*a*b))
                                r=3*n+t
                                if n>=104 and t*t>9*n and 3*r<10*n:
                                    record={"rho":int(rho),"b":int(b),"a":str(a),
                                        "S":str(S),"t":str(t),"n":str(n),
                                        "lucas_witnesses":original_congruence_witness(int(n),int(t))}
                                    original_candidates.append(record)
        records.append(row)
    result={"status":"CERTIFIED_COMPLETE_INTEGRAL_POINTS",
        "rho":int(rho),"b":int(b),
        "rank_proved":int(rank),"gens_certain":certain,
        "integral_point_count":len(points),
        "positive_X_square_lifts":square_count,
        "original_branch_candidate_count":len(original_candidates),
        "original_branch_candidates":original_candidates,
        "all_integral_points":records,
        "seconds":float(round(time.time()-t0,1)),
        "qualification":"ALL integral points on the selected model, not all E(Q) rational points and not all rho."}
    print("V74_COMPLETE",json.dumps(result,ensure_ascii=False),flush=True)
except Exception as e:
    print("V74_INCOMPLETE",json.dumps({
        "status":"INCOMPLETE_NOT_A_CERTIFICATE","rho":int(rho),"b":int(b),
        "error":type(e).__name__+": "+str(e)[:1100],
        "trace":traceback.format_exc()[-1600:]}),flush=True)
    sys.exit(2)
