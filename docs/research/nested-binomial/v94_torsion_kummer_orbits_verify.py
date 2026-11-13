#!/usr/bin/env python3
"""v94: exact rational 3-torsion translation and 10->6 Kummer torsion orbits.

E: Y²+6bXY+MY=X³, P=(0,0) order3, Q=(X,Y), X != 0.
Q+P=(-M*Y/X², -M²*Y/X³). Thus cube class [Y(Q+P)] =
[M²]*[Y(Q)] in Q^*/Q^{*3}; multiplication by M gives the same
cyclic orbit of order3. For b=9 or18, remaining ten ORIGINAL
coefficient types occupy 3+3=6 rational-Kummer torsion orbits.

CRITICAL: translation by P does not generally preserve integrality,
X>0, or the original integer square recovery. Therefore 10 original
integer-point coefficient types are NOT reduced to 6 cases; only
rational descent/Kummer-orbit directions become 6.
"""
from itertools import product
from fractions import Fraction as F
import sympy as s

X,Y,b,M=s.symbols("X Y b M")
E=Y**2+6*b*X*Y+M*Y-X**3
slope=Y/X
xcalc=slope*slope+6*b*slope-X
xplus=-M*Y/X**2
ycalc=-(slope+6*b)*xplus-M
yplus=-M*M*Y/X**3
assert s.factor((xcalc-xplus)*X*X-E)==0
assert s.factor((ycalc-yplus)*X**3-M*E)==0
assert s.factor((yplus*yplus+6*b*xplus*yplus+M*yplus-xplus**3)
                *X**6-M**3*Y*E)==0
C=6*b*X+M
xref=M*(Y+C)/X**2
yref=M*M*(Y+C)/X**3
assert s.factor((yref*yref+6*b*xref*yref+M*yref-xref**3)
                *X**6+M**3*(Y+C)*E)==0
print("PASS: exact torsion translation and reflection on first elliptic quotient")

def add_mod3(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def add_twice(a,b):return add_mod3(add_mod3(a,b),b)
cases={
9:  {"M_mod_cubes":(1,2,1),
     "remaining":{(1,2,k) for k in range(3)} | {(2,1,k) for k in range(3)}},
18: {"M_mod_cubes":(1,1,1),
     "remaining":{(1,1,1),(1,2,0),(2,1,0),(2,2,2)}}
}
for bb,datum in cases.items():
    Mexp=datum["M_mod_cubes"]
    rem=datum["remaining"]
    grouped=[]
    found=set()
    for e in sorted(rem):
        if e in found:continue
        orbit={e,add_mod3(e,Mexp),add_twice(e,Mexp)}
        subset=orbit & rem
        found |= subset
        grouped.append({"representative":e,"orbit":sorted(orbit),
                        "original_types_in_orbit":sorted(subset)})
    assert found==rem
    assert len(grouped)==3
    assert len(rem)==(6 if bb==9 else 4)
    print("V94_ORBITS",bb,grouped)
assert sum(len(c["remaining"]) for c in cases.values())==10

# Real integral elliptic points can sometimes be torsion-reflections,
# without any guarantee that integrality is preserved in general.
bb,rr=1,63
mm=bb*(8*bb*bb+9*rr)
xx,yy=F(50),F(125)
assert yy*yy+6*bb*xx*yy+mm*yy==xx**3
refx=F(mm)*(yy+6*bb*xx+mm)/xx**2
refy=F(mm*mm)*(yy+6*bb*xx+mm)/xx**3
assert (refx,refy)==(230,2645)
assert refy**2+6*bb*refx*refy+mm*refy==refx**3
print("PASS: sample 3-torsion reflection (X,Y)=(50,125) -> (230,2645)")
print("THEOREM: ten original square-lift coefficient classes lie in six 3-torsion Kummer orbits")
print("LIMIT: ten ORIGINAL integer-point classes remain; reduction to six applies only to group-theoretic rational descent")
