# v61: fully certified finite Thue reduction for rational order-9 torsion
# on the FIRST elliptic quotient E1_T, T=rho/b²>0, b|486.
#
# From Kubert's Tate normal form for a rational order-9 point,
# the order-3 point 3P is moved to (0,0), with transformed
# a1'=-z³+3z²-1 and a3'=-z³(z-1)³.
# Scaling to a1=6 forces a3=8+9T=(6z(z-1)/(z³-3z²+1))³.
# Writing z=x/y in lowest terms, D=x³-3x²y+y³ and q=6xy(x-y)/D.
# If b|486 and rho=b²(q³-8)/9 integer, the denominator of q
# satisfies s³|b²; s|27. Since gcd(D,xy(x-y))=1, D|6s|162.
# Solve ALL signed divisors of 162 with PARI thueinit(P,1):
# flag 1 is UNCONDITIONAL, not GRH-conditional.
from sage.all import ZZ, QQ, pari
from sage.env import SAGE_VERSION
from math import gcd
import json

bs=(1,2,3,6,9,18,27,54,81,162,243,486)
dpos=[d for d in range(1,163) if 162%d==0]
ds=sorted([-d for d in dpos]+dpos)
assert len(ds)==20
P=pari('x^3-3*x^2+1')
print("BEGIN",json.dumps({"sage":SAGE_VERSION,"poly":str(P),
    "discriminant":81,"thue_rhs":ds,"flag":1,
    "unconditional":True}),flush=True)
tnf=pari.thueinit(P,1)  # IMPORTANT: flag 1 certifies unconditionally.
print("THUEINIT_CERTIFIED",flush=True)
alls={}
eligible=[]
solcount=0
for d in ds:
    points=[]
    for pair in pari.thue(tnf,d):
        x,y=map(int,pair)
        D=x*x*x-3*x*x*y+y*y*y
        assert D==d
        if gcd(x,y)!=1: continue  # All z have a primitive representative.
        if not y or not x or x==y:
            continue
        N=6*x*y*(x-y)
        q=QQ(N)/D
        if q<=2:continue
        assert q.denominator() in (1,3,9,27)
        for b in bs:
            rho=QQ(b*b)*(q**3-8)/9
            if rho not in ZZ:continue
            rho=ZZ(rho)
            if rho<=0:continue
            entry=dict(x=x,y=y,z=str(QQ(x)/y),q=str(q),
                       b=b,rho=int(rho),rho_mod9=int(rho%9),
                       original_rho_congruence=rho%9 in (1,4,6,7),
                       above_v44_lower_bound=rho>=100003)
            eligible.append(entry)
        points.append((x,y))
    solcount+=len(points)
    alls[str(d)]=sorted(points)
    print("THUE d=",d,"admissible z count=",len(points),flush=True)
eligible.sort(key=lambda e:(e["rho"],e["b"],e["x"],e["y"]))
print(json.dumps({"status":"UNCONDITIONAL_THUE_COMPLETE",
                   "total_positive_z_thue_solutions":solcount,
                   "candidate_rho_b":eligible,
                   "candidate_count":len(eligible),
                   "above_lower_bound_and_mod9":[e for e in eligible
                     if e["above_v44_lower_bound"] and e["original_rho_congruence"]],
                   "all_positive_z_solutions_by_d":alls,
                   "scope":"order-9 rational torsion NECESSARY parametrization, all b|486; not original-solution proof"
                   },indent=2,ensure_ascii=False),flush=True)
