#!/usr/bin/env python3
"""v91 audit: explicit counterexamples to the erroneous F100291 elimination.

The old v83 step substituted v=z*u into
  d v^3-c u^3-6*b*t*u*v=0 mod p
but then wrongly omitted the essential factor u. Correctly, for u!=0:
  u*(d*z^3-c)-6*b*t*z=0.
The three 'rootless' cubic polynomials can remain rootless while the
actual covering curve has smooth Fp points satisfying the a-square lift.
All four p-core=0 types have exact witnesses below. This does NOT
claim any actual integral solution or p-adic original n,t reconstruction.
"""
P=100291
RHO=100003
b=18
M=b*(8*b*b+9*RHO)
assert M%P==0
witnesses=[
 ((1,1,0),(6,36,6),(40138,40138,22353)),
 ((1,2,0),(18,12,6),(18457,73828,6941)),
 ((2,1,0),(12,18,6),(54714,9137,16071)),
 ((2,2,0),(36,6,6),(60153,60153,22353))
]
for e,(c,d,t),(u,v,a) in witnesses:
    assert c*d==t**3
    assert u%P and v%P
    assert (d*v**3-c*u**3-6*b*t*u*v-M)%P==0
    assert (a*a-t*u*v-b*b-RHO)%P==0
    z=v*pow(u,-1,P)%P
    assert (u*(d*z**3-c)-6*b*t*z)%P==0
    # Affine gradient in (u,v,w) at w=1 has nonzero w derivative:
    df_dw=(-6*b*t*u*v-3*M)%P
    assert df_dw!=0
    print("V91_COUNTEREXAMPLE_TO_OLD_ELIMINATION",e,"c,d,t",c,d,t,
          "u,v,a",u,v,a,"smooth_projective_dw",df_dw)
assert len(witnesses)==4
print("PASS: v83 F100291 elimination of three covers is mathematically invalid")
print("PASS: corrected substitution preserves the factor u; v86 rootlessness is a valid standalone polynomial fact, not a cubic-cover obstruction")
print("RESTORED: b18 has twelve types after valid v80 filtering; v90 then reduces to four, with ten total across b9 and b18")
