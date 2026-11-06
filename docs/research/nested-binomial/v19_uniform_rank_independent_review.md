# Independent review: the uniform positive-rank section

Reviewer: residual-geometry agent. Date: 2026-11-07 JST.
Target: `v19_residual_positive_rank.md` and its exact checker.
Result: **PASS; no mathematical correction requested.**

The Nagell–Lutz theorem is used with its proper hypotheses: the displayed
short Weierstrass coefficients are integers, and the discriminant is nonzero
for coprime positive a>b. It does not require that the model be minimal.
The point P0 has positive, hence nonzero, y coordinate, so under the torsion
assumption its double is an affine torsion point. Its integral x coordinate
makes the square of the rational tangent slope integral, hence the slope
itself integral. The cancellation from d|24ab² to d|24a is justified by
gcd(d,b)=gcd(a²,b)=1. No potentially nonunit factor is silently cancelled.

The uniform exception classification is sound. Since gcd(d,a)=gcd(3,a),
a prime >=5 dividing d contradicts d|24a. Coprimality gives v2(d)=2
exactly when a,b are both odd, and 0 otherwise. At 3, v3(d)=1 when
3 divides a, and 0 otherwise. Thus d|12. For a>b>0, d>=7; b>=2 would
give d>=21. Therefore b=1, a=3 is the only exception. Its explicitly
computed double is (-61,0), a nonidentity point of order2, so P0 has
exact order4. Its only allowed positive residual rho=1 has F=4853,
strictly between 69² and 70².

The rank conclusion concerns the fixed-(a,b) genus-one fibration. It
does not contradict rank-zero specializations of the different
fixed-(b,rho) quotient, and does not determine the Jacobian rank of the
genus-two curve. The supplied note makes this distinction correctly.
The ordinary rank<genus Chabauty condition is unavailable on the
surviving fixed-(a,b) genus-one curves, but this does not rule out
other integral-point methods.

For a computational check independent of the producer's sparse-polynomial
implementation, `v19_uniform_rank_independent_review.py` verifies five
polynomial identities on a full 13x13 grid. Each difference has degree
at most12 in each variable; polynomial interpolation uniqueness therefore
makes these coefficient-identity certificates, rather than a finite sample
of the uniform theorem. The exceptional doubling uses exact fractions.
The JSON binds this reviewer script and both target files by SHA256.

The external integrality theorem was checked in Andrew V. Sutherland,
MIT 18.782, Lecture24 (2013-12-03), Theorem24.21,
https://math.mit.edu/classes/18.782/2013fa/LectureNotes24.pdf.
This review is not a new Lean verification or an external peer review.
