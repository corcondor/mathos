# v63: complete unconditional quartic Thue classification of rational order-12
# torsion on E1_T for T=rho/b²>0 with b|486.
#
# For 12-torsion, the unique rational 2-torsion S=(-v²,-v³)
# is divisible by 2, and T=2(v-1)(v+2)^2/9, v>1.
# Under x->X-v² and Y=y+3x+(8+9T)/2, the curve is
# Y²=X(X²+(9-3v²)X+3v³(v+2)).
# S can be halved only if 3v(v+2)=w². Write w=t*v, so
# v=6/(t²-3), sqrt3<t<3 (taking w>0).
# The second halving condition requires (t-1)(t+3)=k².
# Parameterize by t=(z²-2z+4)/(2z), z=m/n reduced.
# Then 8+9T=3456*m^4*(m-2n)^2*(m²+4n²)*n^4 /
#            (m^4-4m³n-16mn³+16n^4)^3.
# If b|486 and rho integer, D4 has NO prime factor >=5,
# by resultant calculations (powers of 2 only). The primitive
# quartic D4 has v2 in {0,4,5} and v3 in {0,1}, so positive
# D4 must belong to {1,3,16,32,48,96}.
# Solve ALL these Thue equations with PARI flag1 (no GRH).
from sage.all import ZZ, QQ, pari
from sage.env import SAGE_VERSION
from math import gcd
import json

B=(1,2,3,6,9,18,27,54,81,162,243,486)
RIGHT=(1,3,16,32,48,96)
P=pari('x^4-4*x^3-16*x+16')
print("BEGIN",json.dumps({"sage":SAGE_VERSION,"poly":str(P),
    "right_hand_sides":RIGHT,"unconditional":True,
    "thueinit_flag":1}),flush=True)
tnf=pari.thueinit(P,1)
print("THUEINIT_CERTIFIED",flush=True)
all_sols={}
valid=[]
for d in RIGHT:
    sols=[]
    for pair in pari.thue(tnf,d):
        m,n=map(int,pair)
        D=m**4-4*m**3*n-16*m*n**3+16*n**4
        assert D==d
        if gcd(m,n)!=1:continue
        sols.append((m,n))
        if not m or not n or m==2*n:continue
        v=QQ(24*m*m*n*n)/d
        if v<=1:continue
        a3=QQ(3456*m**4*(m-2*n)**2*(m*m+4*n*n)*n**4)/d**3
        assert a3==2*v*v*(v+3)
        if a3<=8:continue
        for b in B:
            rho=QQ(b*b)*(a3-8)/9
            if rho not in ZZ or rho<=0:continue
            valid.append({"m":m,"n":n,"D":int(d),"v":str(v),
                          "a3":str(a3),"b":b,"rho":int(rho),
                          "rho_mod9":int(rho%9),
                          "admissible_rho_congruence":rho%9 in(1,4,6,7)})
    all_sols[str(d)]=sorted(sols)
    print("THUE d",d,"primitive solutions",len(sols),flush=True)
valid.sort(key=lambda z:(z["rho"],z["b"],z["m"],z["n"]))
print(json.dumps({"status":"UNCONDITIONAL_THUE_COMPLETE",
  "all_primitive_solutions":all_sols,"valid_order12_params":valid,
  "valid_count":len(valid),"unique_rho_b":sorted(set((v["rho"],v["b"]) for v in valid)),
  "scope":"necessary complete modular parameter classification for rational 12-torsion with T>0,b|486"
  },indent=2),flush=True)
