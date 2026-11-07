# v19 lattice covering: separate written/code review

Date: 2026-11-07 JST. Reviewer: a separate internal AI task that authored
neither lattice implementation. This is not external human peer review
or a Lean verification. The full large lattice workload was **not**
rerun as part of this review; the separate verifier is being executed
by the main task. This review inspected both complete source files and
ran only targeted, small rectangle tests.

Reviewed files:

- `v19_lattice_cover.py`, SHA256
  `40586603e360b5b685fe38029afc41af81b9cf480a6fbc365e7c15b14de642f6`.
- `v19_lattice_verify.py`, SHA256
  `53cd47201507ba71af9e406fda57aa5f5dee3eeda66b7bbd055a8f087ec4ede3`.

**Conclusion: no blocking mathematical or implementation issue found
in the stated finite covering.** The proof of completeness still takes
the v16 height and coefficient interval as inherited inputs; this review
does not independently reprove those older analytic bounds.

## 1. Complete dyadic domain

For a solution of `C r^2=K n(n-1)` put `x=2n-1`, `y=2r` and
`alpha=sqrt(K/C)`. The coefficient interval implies `3<alpha<4`, and

\[
y=\alpha\sqrt{x^2-1}.
\]

The integer height `104<=n<2^(42 delta)` is exactly
`207<=x<=2^(42 delta+1)-3` for odd x. The code's boxes

\[
B=2^b,\quad 7\le b\le42\delta,\qquad
\max(B,207)\le x\le\min(2B-1,2^{42\delta+1}-3)
\]

cover that interval once, including both end cases. The extra even x
are harmless because parity is checked before reconstruction. There is
no unproved truncation of a final box or of a basis coefficient loop.

## 2. Why every conic point enters the rectangle

For `L=B^2`, let `a=floor(L alpha)` and
`e=L y-a x`. Then `(x,e)` is an integer vector in the lattice generated
by `(1,-a)` and `(0,L)`. With `theta=L alpha-a`,

\[
e=-\frac{L\alpha}{x+\sqrt{x^2-1}}+\theta x,\qquad 0\le\theta<1.
\]

As `B<=x<2B`, the first term is greater than `-4B` and negative,
and the second is in `[0,2B)`. Therefore

\[
-4B<e<2B.
\]

The producer's integer rectangle `-4B+1<=e<=2B-1` is complete. The
verifier deliberately uses the larger closed rectangle
`-4B<=e<=2B`; this cannot omit a conic point.

The two floor comparisons `C a^2<=K L^2<C(a+1)^2` certify a exactly,
without floating-point square roots. Under `B -> 2B`, the update
`(x,e) -> (x,4e+(4a_old-a_new)x)` retains the same integer unimodular
coefficient matrix for the new input basis. Both implementations check
this invariant explicitly.

## 3. LLL checks and complete rectangle enumeration

The basis routines preserve an integer matrix with determinant +/-1;
the verifier additionally orients its determinant positively. They
check the resulting determinant is L and each row is the declared
integer combination of the input basis. Hence the reduced rows span
the entire lattice, not a sublattice.

For two rows, the code checks
`2|<b1,b2>|<=||b1||^2` and
`4||b2||^2>=3||b1||^2`. These are exactly size reduction and the
Lovasz condition with delta_LLL=3/4 in dimension two. The second claim
uses `||b2*||^2+mu^2||b1||^2=||b2||^2`; it does not omit a
Gram--Schmidt term. The exact determinant/GSO identity is also checked.

Enumeration is not limited to a few short vectors. The producer bounds
the second integer coefficient by the extrema of its inverse-matrix
linear form at all four rectangle corners. For each such coefficient,
it intersects the exact intervals for the other coefficient obtained
from both coordinates. This exhausts all lattice points in the
rectangle. Negative determinants, negative coordinate slopes, and a
zero coordinate slope are handled correctly. The verifier enumerates
the first coefficient instead, has a different tie convention, and
uses the enlarged error rectangle.

Targeted verification covered **320** small rectangle cases for
`a in {0,1,5,17}`, `L in {1,2,7,16}`, four unimodular row matrices
(both determinant signs), and five rectangles including singleton
coordinate ranges. For each case, both enumeration helpers exactly
matched direct enumeration of the congruence `e+a*x=0 (mod L)`.
These are implementation edge checks; the quantified rectangle
argument above supplies completeness.

## 4. Square-CK exceptional families

If `CK=s^2`, the conic gives

\[
x^2-z^2=1,\qquad z=Cy/s\in\mathbb Q.
\]

Since `z^2=x^2-1` is an integer, z is an integer (reduce its rational
fraction). Thus `(x-z)(x+z)=1`, whose only nonnegative solution has
`x=1,z=0`. There is no point with `x>=207,y>0`. Returning an empty
set for these families is justified, not a numerical square-root
heuristic. The full certificate records four such coefficient families.

## 5. Arithmetic filters and both original branches

The coefficient loops cover all four M values, the exact strict
rational K interval, and `gcd(K,delta)=1`. The verifier uses a wider K
loop followed by direct inequalities, so it independently checks the
producer's endpoint rounding. It also checks every family was consumed.

Reconstruction enforces odd x, positive even y, and the exact conic.
The remaining filters recompute the actual M, the actual delta,
`Q|r^3`, and `3n<r<10n/3`. For the logarithmic filter the integer j
obeys `3^j<n<=3^(j+1)`, so `log(n)>j`. The retained inequality is
therefore a weaker necessary consequence of the inherited logarithmic
bound, and cannot remove an original solution. Exact powers of 3 are
handled correctly by both strict comparison loops.

The original squared-index equation, restricted to this branch, is

\[
\binom{\binom n3}{k}=\binom{n^2}{6n-9}+k^2.
\]

The left side may be evaluated at r for both `k=r` and `k=A-r`, by
binomial symmetry, while the right square uses the correct k separately.
All 93 saved candidate records have exactly two branch witnesses.
Primes are checked as prime; the verifier recomputes the Lucas residues
using factorial inverses instead of the producer's small binomial
routine. No `binom(i,j)^2` substitution occurs.

## 6. Independence and what was not achieved

The producer reads the prior Pell certificate for an **after-the-fact
comparison**. Its lattice covering routine takes only `(C,K,delta)`;
neither units, convergents, old point sets, nor old candidate counts
set a basis or an enumeration bound. The full verifier imports neither
producer nor Pell code and reads no Pell units.

The full saved producer certificate reports 3,571 coefficient families,
2,818,386 dyadic boxes/basis checks, 112,249 positive integral conic
points with n>=104, and 93 final candidates with 186 modular exclusions.
This review read those counts and checked the branch record structure;
it did **not** recompute the full workload. The separate full verifier's
execution result is the appropriate source for recomputation claims.

The lattice calculation reproduces the already established finite
delta=13,...,24 exclusion. It does not improve the numerical lower
bound delta>=25 by itself, cover unbounded delta, solve the full
four-variable equation, execute Coppersmith, or compute an elliptic
discrete logarithm. Those boundaries are accurately stated in the
producer and verifier reports.
