#!/usr/bin/env python3
"""Finite proof certificates for the first nine sections of E2(Q(t)).

Only finite section mR for 1 <= |m| <= 9.  This is NOT a theorem about all
rational points of every specialized elliptic curve.
"""
from itertools import product
from math import gcd,isqrt
from pathlib import Path
import json
import sympy as sp

t, rho, b = sp.symbols('t rho b')
A=-t**2*(4*t+3)
B=12*(t*t+5*t+3)
C=12*(2-t)
R=(8*t*(4*t+3), 6*t*(4*t+3)*(9*t+8))

def add(P,Q):
 if P is None: return Q
 if Q is None: return P
 x1,y1=P; x2,y2=Q
 if sp.cancel(x1-x2)==0 and sp.cancel(y1+y2)==0: return None
 if sp.cancel(x1-x2)==0:
  slope=sp.cancel((3*x1**2+2*B*x1+A*C)/(2*y1))
 else:
  slope=sp.cancel((y2-y1)/(x2-x1))
 xn=sp.factor(slope**2-B-x1-x2)
 yn=sp.factor(-y1+slope*(x1-xn))
 return xn,yn

# Expected ratio a^2/b^2 = A(t)/X_m(t), independently computed from EC group law.
expected = {
 1:-t/8,
 2:-(4*t+3)/5,
 4:4*t*(4*t+3)/(7*t+24),
 5:25*t*t/(16*(t+12)),
 6:t*(4*t+3)/(3*(t+32)),
 7:(7*t+24)**2/(40*(t+72)),
 8:16*(t+12)**2*(4*t+3)/(5*(11*t*t+1584*t-576)),
 9:9*t*(t+32)**2/(8*(t*t+264*t-576)),
}
section_formulas={}
P=None
for m in range(1,10):
 P=add(P,R)
 if m==3:
  assert sp.simplify(P[0])==0
  section_formulas[str(m)]={'X':'0','outcome':'w=0, no finite a'}
  continue
 a2t=sp.factor(A/P[0])
 assert sp.cancel(a2t-expected[m])==0,(m,a2t)
 a2rho=sp.factor((b*b*a2t).subs(t,rho/(b*b)))
 section_formulas[str(m)]={'X':str(P[0]),'a2_over_b2':str(a2t),'a2_b_rho':str(a2rho)}

# For linear denominators h*rho+g*b^2, integrality forces denominator
# d=h*rho+g*b^2 dividing a fixed constant times b^4.
linear={
 4:(7200,7,24, lambda r,bb:(4*r*(4*r+3*bb*bb), 7*r+24*bb*bb)),
 5:(3600,1,12, lambda r,bb:(25*r*r,16*(r+12*bb*bb))),
 6:(4000,1,32, lambda r,bb:(r*(4*r+3*bb*bb),3*(r+32*bb*bb))),
 7:(230400,1,72,lambda r,bb:((7*r+24*bb*bb)**2,40*(r+72*bb*bb))),
}
# factorization of resultant(constants) for quadratic denominators m=8 and 9.
quadratic={8:(16,6,11),9:(18,6,6)}
D8=11*rho**2+1584*b*b*rho-576*b**4
N8=16*(rho+12*b*b)**2*(4*rho+3*b*b)
D9=rho**2+264*b*b*rho-576*b**4
N9=9*rho*(rho+32*b*b)**2
assert sp.factor(sp.resultant(D8,N8,rho)+2332800000000000*b**12)==0
assert sp.factor(sp.resultant(D9,N9,rho)+2985984000000*b**12)==0

counts={}
all_pass=[]

def check_row(m,bb,rr):
 if m==4:num,den=linear[4][3](rr,bb)
 elif m==5:num,den=linear[5][3](rr,bb)
 elif m==6:num,den=linear[6][3](rr,bb)
 elif m==7:num,den=linear[7][3](rr,bb)
 elif m==8:num,den=16*(rr+12*bb*bb)**2*(4*rr+3*bb*bb),5*(11*rr*rr+1584*bb*bb*rr-576*bb**4)
 elif m==9:num,den=9*rr*(rr+32*bb*bb)**2,8*(rr*rr+264*bb*bb*rr-576*bb**4)
 else:raise ValueError(m)
 assert rr>0
 if den<=0 or num%den:return None
 aa2=num//den;aa=isqrt(aa2)
 if aa*aa!=aa2:return ('a2_not_square',)
 return ('square',aa)

for m in range(4,10):
 out={'divisors_checked':0,'positive_rho_candidates':0,
      'a2_positive_integer':0,'a2_square':0,'primitive':0,
      'positive_z':0,'rho_mod9_ok':0,'rho_ge32770':0,'remaining':0}
 prim=[];allowed=[];square=[]
 for exp2,exp3 in product(range(2),range(6)):
  bb=2**exp2 * 3**exp3
  if m<=7:
   K,h,g,form=linear[m]
   # 7200 = 2^5*3^2*5^2
   # 3600 = 2^4*3^2*5^2
   # 4000 = 2^5*5^3
   # 230400 = 2^10*3^2*5^2
   Kprimes={4:(5,2,2),5:(4,2,2),6:(5,0,3),7:(10,2,2)}[m]
  else:
   Kprimes=quadratic[m]
  expo2=Kprimes[0]+4*exp2 if m<=7 else Kprimes[0]+12*exp2
  expo3=Kprimes[1]+4*exp3 if m<=7 else Kprimes[1]+12*exp3
  expo5=Kprimes[2]
  for i,j,k in product(range(expo2+1),range(expo3+1),range(expo5+1)):
   d=2**i*3**j*5**k
   out['divisors_checked']+=1
   if m<=7:
    if d<=g*bb*bb or (d-g*bb*bb)%h:continue
    rr=(d-g*bb*bb)//h
   elif m==8:
    # D8(rho) = d (positive because a^2>0 for rho>0).
    disc=((1584**2+44*576)*bb**4+44*d)
    root=isqrt(disc)
    if root*root!=disc or (root-1584*bb*bb)%22:continue
    rr=(root-1584*bb*bb)//22
   else:
    # D9(rho) = d (positive because a^2>0 for rho>0).
    root=isqrt(18000*bb**4+d)
    if root*root!=18000*bb**4+d:continue
    rr=root-132*bb*bb
   if rr<=0:continue
   out['positive_rho_candidates']+=1
   result=check_row(m,bb,rr)
   if result is None:continue
   out['a2_positive_integer']+=1
   if result[0]!='square':continue
   aa=result[1]
   out['a2_square']+=1
   square.append((bb,rr,aa))
   if gcd(bb,aa)>1:continue
   out['primitive']+=1
   prim.append((bb,rr,aa))
   if aa*aa<=rr+bb*bb:continue
   out['positive_z']+=1
   if rr%9 not in (1,4,6,7):continue
   out['rho_mod9_ok']+=1
   if rr<32770:continue
   out['rho_ge32770']+=1
   if rr%5 == bb*bb%5: continue # v19 necessary local condition
   out['remaining']+=1
   allowed.append((bb,rr,aa))
 counts[str(m)]={'counts':out,'square':sorted(square),
                 'primitive':sorted(prim), 'surviving_with_v23':allowed}
 assert not allowed,(m,allowed)

# strict standalone check: m8 and m9 have no square/primitive lifts beyond rho>=32770;
# the direct resulting count is especially strong and does not need v20 congruences.
assert counts['8']['counts']['remaining']==0
assert counts['9']['counts']['remaining']==0

cert={'formulas':section_formulas,'section_sieve':counts,
      'v23_assumption':'rho>=32770 is taken from prior v23, not reverified here',
      'limitations':'Only |m|<=9 in the subgroup generated by R; specialized rank jumps are not excluded.'}
path=Path(__file__).with_name('v26_sections_1_to_9_certificate.json')
path.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print('PASS: symbolic group law for mR, |m|=1..9')
print('PASS: quadratic-denominator resultants for 8R and 9R')
for key,v in counts.items():
 print(f'm={key}:',v['counts'])
print('PASS: no necessary-condition candidates in |m|<=9, assuming v23 rho>=32770')
print('certificate:',path)

