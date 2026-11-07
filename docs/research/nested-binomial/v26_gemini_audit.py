#!/usr/bin/env python3
"""v26: exact SymPy and integer proof checks; Python 3 / SymPy 1.14.

The word 'PASS' only denotes checks implemented here; Shioda-Tate
and Nagell-Lutz (if used) are mathematical theorems, not CAS-certified.
"""
import itertools
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import sympy as sp

b, rho, lam, t, x, y, u = sp.symbols('b rho lam t x y u', nonzero=True)
report = {}

# Gamma0(3) normal form and correct Hauptmodul substitution.
lam0 = (8*b*b + 9*rho)/(216*b*b)
tH = sp.factor((1 - 27*lam0)/lam0)
assert sp.simplify(tH + 243*rho/(8*b*b + 9*rho)) == 0
c4E = 1 - 24*lam
DeltaE = lam**3*(1-27*lam)
jE = sp.factor(c4E**3/DeltaE)
assert sp.simplify(jE.subs(lam, 1/(t+27))-(t+27)*(t+3)**3/t) == 0

# 3-isogeny quotient (Deuring normal form), plus explicit rational map.
x_prime = (x**3 + lam*x + lam**2)/x**2
y_prime = (y*(x**3-lam*x-2*lam**2) - lam*(x+lam)**2)/x**3
EqD = sp.together(y_prime*y_prime + x_prime*y_prime+lam*y_prime
                    -x_prime**3 + 5*lam*x_prime +lam +7*lam*lam)
numerator = sp.together(EqD).as_numer_denom()[0]
rem = sp.rem(numerator, y*y+(x+lam)*y-x**3,y)
assert sp.simplify(rem) == 0
# standard invariant formulas for y^2+a1*x*y+a3*y=x^3+a4*x+a6
ap4 = -5*lam
ap6 = -lam-7*lam*lam
bp2=1;bp4=2*ap4+lam;bp6=lam*lam+4*ap6;bp8=ap6-ap4*ap4+lam*ap4
c4D=sp.factor(bp2**2-24*bp4)
c6D=sp.factor(-bp2**3+36*bp2*bp4-216*bp6)
DeltaD=sp.factor((c4D**3-c6D**2)/1728)
assert sp.simplify(c4D-(1+216*lam)) == 0
assert sp.simplify(DeltaD-lam*(1-27*lam)**3) == 0
jD=sp.factor(c4D**3/DeltaD)
assert sp.simplify(jD.subs(lam,1/(t+27))-(t+27)*(t+243)**3/t**3)==0
report['E1'] = {'c4': str(c4E),'discriminant':str(DeltaE),
                'Hauptmodul_t':str(tH),'j':str(jE)}
report['E_dual']={'equation_a4':'-5*lam','equation_a6':'-lam-7*lam**2',
                  'c4':str(c4D),'discriminant':str(DeltaD),
                  'discriminant_specialized':str(sp.factor(DeltaD.subs(lam,lam0)))}

# E2 quotient normalized by t=rho/b^2, w=b^2/a^2.
A = -t**2*(4*t+3)
B = 12*(t**2+5*t+3)
C = 12*(2-t)
f2 = x**3 + B*x*x + A*C*x + 4*A*A
b2=4*B; b4=2*A*C; b6=16*A*A
c42=sp.factor(b2*b2-24*b4)
c62=sp.factor(-b2**3+36*b2*b4-216*b6)
Delta2=sp.factor((c42**3-c62**2)/1728)
assert sp.factor(Delta2+62208*t**5*(4*t+3)**2*(9*t+8)**3)==0
mu = sp.symbols('mu')
assert sp.factor(mu**12*Delta2.subs(t,1/mu)).subs(mu,0)==0
assert sp.factor(mu**4*c42.subs(t,1/mu)).subs(mu,0)==0
assert sp.factor((mu**12*Delta2.subs(t,1/mu))/mu**2).subs(mu,0)!=0
assert sp.factor((mu**4*c42.subs(t,1/mu))/mu).subs(mu,0)!=0
for t0, exponent in [(0,5),(-sp.Rational(8,9),3),(-sp.Rational(3,4),2)]:
    assert c42.subs(t,t0)!=0

# Complete elliptic group law in the Y^2=X^3+B X^2+AC X+4A^2 model.
def ECadd(P,Q):
    if P is None: return Q
    if Q is None: return P
    X1,Y1=P; X2,Y2=Q
    if sp.simplify(X1-X2)==0 and sp.simplify(Y1+Y2)==0:return None
    if sp.simplify(X1-X2)==0:
        if sp.simplify(Y1)==0:return None
        m = sp.factor((3*X1*X1+2*B*X1+A*C)/(2*Y1))
    else:
        m = sp.factor((Y2-Y1)/(X2-X1))
    X3=sp.factor(m*m-B-X1-X2)
    Y3=sp.factor(-Y1+m*(X1-X3))
    return X3,Y3
R=(8*t*(4*t+3),6*t*(4*t+3)*(9*t+8))
assert sp.factor(R[1]**2-f2.subs(x,R[0])) == 0
R2=ECadd(R,R)
R3=ECadd(R2,R)
R4=ECadd(R3,R)
assert all(sp.simplify(v-w)==0 for v,w in zip(R2,(5*t*t,3*t*t*(9*t+8))))
assert all(sp.simplify(v-w)==0 for v,w in zip(R3,(0,2*t*t*(4*t+3))))
assert all(sp.simplify(v-w)==0 for v,w in zip(R4,(-t*(7*t+24)/4,3*t*(t+12)*(9*t+8)/8)))
P0=(0,2*A)
assert sp.simplify(R3[0]-P0[0])==0 and sp.simplify(R3[1]+P0[1])==0
# E2 map w=b^2/a^2 = X/A, and positive integer a must satisfy formula.
w4=sp.factor(R4[0]/A)
a2formula=sp.factor(b*b/w4.subs(t,rho/(b*b)))
assert sp.simplify(a2formula-4*rho*(4*rho+3*b*b)/(7*rho+24*b*b))==0
report['E2']={'c4':str(c42),'discriminant':str(Delta2),
              'fibers':{'0':'I5','-8/9':'I3','-3/4':'I2','infinity':'II'},
              'R':list(map(str,R)),'2R':list(map(str,R2)),
              '3R':list(map(str,R3)),'4R':list(map(str,R4)),
              'P0':list(map(str,P0)),'w_4R':str(w4),
              'a_squared_4R':str(a2formula)}

# Specialized torsion test: E2 at t=1 has nonzero R and trivial E(Q)_tors.
B1=int(B.subs(t,1));AC1=int((A*C).subs(t,1));D1=int((4*A*A).subs(t,1))
assert (B1,AC1,D1)==(108,-84,196)
finite_counts={}
for p in (5,11):
    assert int(Delta2.subs(t,1))%p !=0
    num=1 # point at infinity
    for xx in range(p):
        rhs=(xx**3+B1*xx**2+AC1*xx+D1)%p
        num+=sum((yy*yy-rhs)%p==0 for yy in range(p))
    finite_counts[str(p)] = num
assert finite_counts == {'5':5,'11':9}
assert gcd(5,9)==1
report['specialization_t1']={'curve':[B1,AC1,D1], 'R':[56,714],
                              'good_reduction_prime_point_counts':finite_counts,
                              'rational_torsion':'trivial'}

# 4R positive integer lifts for every divisor b of 486, no rho cutoff.
counts={'divisors_checked':0,'positive_rho_from_divisors':0,
        'integer_a_squared':0,'square_a_squared':0,'primitive':0,
        'primitive_and_z_positive':0,'primitive_and_v20_rho_mod9':0}
all_square=[];primitive=[]
for bb in sp.divisors(486):
    for dd in sp.divisors(7200*bb**4):
        counts['divisors_checked']+=1
        if dd<=24*bb*bb or (dd-24*bb*bb)%7:continue
        rr=(dd-24*bb*bb)//7
        counts['positive_rho_from_divisors']+=1
        aa2num=4*rr*(4*rr+3*bb*bb)
        if aa2num%dd:continue
        counts['integer_a_squared']+=1
        aa2=aa2num//dd
        aa=isqrt(aa2)
        if aa*aa != aa2: continue
        counts['square_a_squared']+=1
        all_square.append((bb,rr,aa))
        if gcd(aa,bb)>1:continue
        counts['primitive']+=1
        primitive.append((bb,rr,aa))
        if aa2<=bb*bb+rr:continue
        counts['primitive_and_z_positive']+=1
        if rr%9 in (1,4,6,7):counts['primitive_and_v20_rho_mod9']+=1
assert primitive == [(1,3,2),(1,18,6)]
assert counts['primitive_and_v20_rho_mod9']==0
report['4R_lifts']={'counts':counts,'all_square_positive_a':all_square,
                    'primitive_positive_a':primitive,
                    'no_valid_v20_branch_lifts':True}

# Check the scaled original E2 discriminant polynomial in u and the extra factor.
fu = 4 + (24*b*b-12*rho)*u +(36*b**4+60*b*b*rho+12*rho**2)*u*u -rho*rho*(3*b*b+4*rho)*u**3
DiscPoly=sp.factor(sp.discriminant(fu,u))
assert sp.factor(DiscPoly + 3888*b**4*rho*(8*b*b+9*rho)**3)==0
report['E2_unscaled_cubic_discriminant']=str(DiscPoly)

out=Path(__file__).with_name('v26_audit_certificate.json')
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('PASS: Hauptmodul and dual isogeny, including rational map')
print('PASS: E2 discriminants, singular fiber valuation tests')
print('PASS: exact points R, 2R, 3R=-P0, 4R')
print('PASS: t=1 good reduction group orders and nontorsion specialization')
print('PASS: 4R integer lifts sieve, all b|486, no rho upper bound')
print('4R counts:',counts)
print('4R primitive lifts:',primitive)
print('certificate:',out)
