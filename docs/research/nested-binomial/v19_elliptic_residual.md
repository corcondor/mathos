# v19: residual elliptic quotients, a uniform mod-5 obstruction, and rho >= 11

Date: 2026-11-07 JST. This is written mathematics with exact coefficient
checks and a finite, proof-bounded integer certificate. It is not a new Lean
verification or a DeepSeek run. Existing proofs and fixed goals are unchanged.

## 1. Scope and inputs

Keep the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

The branch is \(\ell=1,j=i-3\), for both \(k=r\) and \(k=A-r\), with
\(n=i,A=\binom n3,r=\min(k,A-k),t=r-3n\).
Use the v17/v18 reduced residual variables

\[
M=\gcd(n,3)\gcd(n-1,6),\quad h/(81M)=a/b,\quad\gcd(a,b)=1,
\]
\[
\rho=a^2+ab(9n-t-6)-b^2(t^2+3t+3)>0.
\]

The established necessary conditions for original solutions include

\[
n\ge104,\quad 3n<r<10n/3,\quad Q=n(n-1)/M\mid r^3,
\]
\[
b\in B:=\{1,2,3,6,9,18,27,54,81,162,243,486\},
\quad27a\ge31b,
\]
\[
\rho\equiv a^2\pmod b,\qquad
1377\rho<216a^2+760b^2,
\qquad a<\rho(\rho+32b^2).
\tag{1}
\]

The final inequality is v18, equation (13), derived from integer separation;
it is a proved height bound, not a computational cutoff. The discriminant is
the square

\[
\begin{aligned}
F(a,b,\rho)={}&4a^6+(24b^2-12\rho)a^4\\
&+(36b^4+60b^2\rho+12\rho^2)a^2-3b^2\rho^2-4\rho^3=y^2.
\end{aligned}
\tag{2}
\]

### Correction to the separate descent plan

The separate branch `research/v18-next-descent`, at the snapshot identified
by the root reviewer as `73cdb502392b61db093c7a50d44f5efb21f9e2e2`, used
\(27a<31b\) as an admissible domain. The v17 main proof instead excludes
this domain for original solutions: \(h\ge93M\) gives \(27a\ge31b\).
The present certificate uses the latter inequality. A list or rank experiment
restricted to \(27a<31b\) cannot by itself advance the surviving branch.
This correction follows directly from the checked v17 definition and theorem;
it does not depend on trusting that separate branch's curve tables or rank
placeholders.

## 2. The two elliptic fibrations must be distinguished

### 2.1 Fixed (b,rho): elliptic quotient of a genus-two curve

For fixed positive \(b,\rho\), set

\[
X=4a^2+8b^2-4\rho,\qquad Y=4y.
\]

Then (2) maps exactly to

\[
E_{b,\rho}:\quad Y^2=X^3+48b^2(9\rho-b^2)X
+1296\rho^2b^2-2880\rho b^4-128b^6.
\tag{3}
\]

Its discriminant is

\[
\Delta(E_{b,\rho})=-995328\rho b^4(9\rho+8b^2)^3\ne0.
\tag{4}
\]

The cubic in \(a^2\) in (2) has discriminant
\(-3888\rho b^4(9\rho+8b^2)^3\ne0\), and its constant term is
\(-\rho^2(3b^2+4\rho)\ne0\). Thus the even sextic in a is squarefree:
a common root with its derivative would be zero or give a common root of
the cubic and its derivative. Neither is possible. Consequently its smooth
projective model has genus two and has two rational points at infinity,
since its leading coefficient is 4.

An arbitrary rational or integral point of (3) need not come from (2).
In particular, the original problem requires
\((X-8b^2+4\rho)/4=a^2\), with positive integer a and all of (1), as well
as integer reconstruction below. This square restriction is essential.

### 2.2 Fixed (a,b): an elliptic curve with variable rho

Alternatively put

\[
U=4a^2-b^2-4\rho,\qquad V=4y.
\]

Then

\[
\mathcal E_{a,b}:\quad
V^2=U^3-3b^2(72a^2+b^2)U
+2b^2(648a^4+180a^2b^2-b^4),
\tag{5}
\]

with

\[
c_4=144b^2(72a^2+b^2),\qquad
\Delta=-995328a^2b^4(3a-b)^3(3a+b)^3.
\tag{6}
\]

This is nonsingular when \(a>b>0\). These are two different elliptic
fibrations of the residual surface, not a claim that the two specialized
curves attached to an arbitrary point are isomorphic or isogenous.

All transformations and discriminants in this section are checked by exact
integer-polynomial coefficient arithmetic in the accompanying checker.

## 3. A uniform local obstruction: rho is not b squared modulo 5

**Theorem 1.** If \(a,b,\rho,y\in\mathbb Z\), \(5\nmid b\), and
\(y^2=F(a,b,\rho)\), then

\[
\boxed{\rho\not\equiv b^2\pmod5.}
\tag{7}
\]

**Proof.** Suppose \(\rho/b^2=1\) in \(\mathbb F_5\), and write
\(z=a^2/b^2\in\{0,1,4\}\). Dividing (2) by the nonzero square \(b^6\)
gives

\[
(y/b^3)^2=4z^3+2z^2+3z+3.
\]

For \(z=0,1,4\), the right side is respectively \(3,2,3\), all
nonsquares in \(\mathbb F_5\). This is impossible. QED.

Every denominator in B is a unit modulo 5, so this is an unconditional
necessary condition for both original k branches. It places a restriction
on an unbounded residual parameter; no height, rank, prime cutoff, or
unproved conjecture is used.

This is the exact finite-field obstruction step in the local-integral-point
method of Stoll (2025/2026), Section 3, Algorithm 3.4. We use only that step,
not the paper's full Mordell-Weil-sieve/Chabauty algorithm.
The distinction between affine integral points and projective rational
points matters here: the genus-two curve always has rational points at
infinity. A test asking whether the projective curve has any local point
would therefore pass, even in the cases excluded by (7).

## 4. The known square-root boundary is the rational 3-torsion section

**Theorem 2.** Curve (3) contains the point

\[
T=(12b^2,\,4b(9\rho+8b^2))
\tag{8}
\]

of exact order 3. A point from (2) maps to \(T\) or \(-T\) precisely
when \(\rho=a^2-b^2\). Every such point with \(a>b>0\) reconstructs
either a negative t or \(t^2=9n\).

**Proof.** The second coordinate of T is nonzero. Its tangent has slope
\(6b\). Substitution of
\(Y=4b(9\rho+8b^2)+6b(X-12b^2)\) into the cubic gives
\((X-12b^2)^3=0\). Thus the tangent has triple contact and the elliptic
group law gives \(3T=O\); T is not O, so its order is exactly 3.
Equivalently, the translation to T gives the Tate form

\[
v^2+12buv+8b(9\rho+8b^2)v=u^3.
\]

The X coordinate in (3) equals \(12b^2\) exactly when
\(\rho=a^2-b^2\). At this residual,

\[
F(a,b,a^2-b^2)=b^2(9a^2-b^2)^2.
\]

The v17 reconstruction formulas are

\[
t=\frac{2a(a^2+3b^2)-\rho(3b+2a)\pm y}{2b\rho},
\tag{9}
\]
\[
n=\frac{b^2(t^2+3t+3)+ab(t+6)-a^2+\rho}{9ab}.
\tag{10}
\]

Putting \(\rho=a^2-b^2\) and \(y=b(9a^2-b^2)>0\), these give

\[
\begin{array}{c|c}
t&n\\ \hline
-2(3a+b)/(a+b)&8b(3a+b)/(9(a+b)^2)\\
(3a+b)/(a-b)&(3a+b)^2/(9(a-b)^2).
\end{array}
\]

The first t is negative. The second has \(t^2=9n\), as asserted. QED.

The fixed-(a,b) fibration (5) has the matching order-3 section

\[
S=(3b^2,\,4b(9a^2-b^2)).
\]

Its tangent has slope \(-3b\), and the resulting Tate form is
\(v^2-6buv+8b(9a^2-b^2)v=u^3\). Its preimage is the same locus
\(\rho=a^2-b^2\). This second observation was independently supplied
by the root reviewer and is included in the coefficient checks.

**Consequence.** Since v17 excludes \(t^2=9n\) for the original equation,
an original solution maps outside \(\{O,T,-T\}\) on (3). If a
specialized curve has rank 0 and rational torsion group of order 3, that
entire (b,rho) fiber is excluded, for all a and n. We do not infer rank
positivity without the torsion-group hypothesis: extra rational torsion
occurs in this family, for example (b,rho)=(1,24) has order-6 torsion in
the separate PARI experiment.

## 5. A complete, proof-bounded exclusion of rho = 1,...,10

**Theorem 3.** Every original solution in the stated branch satisfies

\[
\boxed{\rho\ge11.}
\tag{11}
\]

**Proof by the accompanying exact finite certificate.** For each
\(1\le\rho\le10\) and \(b\in B\), use the finite interval

\[
\max(b+1,\lceil31b/27\rceil)\le a
\le\rho(\rho+32b^2)-1.
\tag{12}
\]

This covers every possible a by (1). Enumerate precisely the residue
classes \(a^2\equiv\rho\pmod b\), \(\gcd(a,b)=1\), and retain the
strict residual inequality in (1). There are 45 (b,rho) fibers with any
such residue class; Theorem 1 eliminates 11 of them independently of a.
The domain contains 886,683 candidate coefficients. After this whole-fiber
mod-5 filter, 775,235 exact square tests remain. For these test (2) using
integer square roots, with an exact
\(\lfloor\sqrt F\rfloor^2=F\) equality test. The only square cases are:

| a | b | rho | y | (t,n), minus sign | (t,n), plus sign |
|---:|---:|---:|---:|---|---|
| 13 | 2 | 1 | 4674 | (0,0) | (2337,281219/3) |
| 7 | 1 | 4 | 660 | (0,0) | (165,1375/3) |
| 7 | 2 | 7 | 798 | (-3,2/21) | (54,729/7) |
| 4 | 3 | 7 | 405 | (-30/7,40/49) | (15,25) |
| 10 | 3 | 10 | 2430 | (-3,1/10) | (78,2197/10) |

Every case fails integer reconstruction, positivity, or \(n\ge104\).
Both signs are checked exactly with rational arithmetic. This covers the
full range (12), not merely a sample below an arbitrary a or n bound.
The per-fiber endpoints, residue classes, counts, all five square cases,
and both reconstructed roots are stored in the JSON certificate. QED.

This is an application of the elementary Runge/integer-separation part
recalled in Gajović–Müller, *Linear quadratic Chabauty* (2025), Appendix A,
with the sharper problem-specific height already proved in v18.
It is not a claim to have executed their p-adic-height algorithm.

The optional PARI/GP script separately computes `ellrank` bounds and
`elltors` for these 45 fibers. Its output is useful for prioritizing
future fibers, but is not an input to Theorem 3's certificate. The observed
output gives rank upper bound 0 on 22 fibers and rational torsion order 3
on all 45 fibers. In
particular, the certificate is reproducible using only Python's standard
library. No BSD, analytic-rank inference, or height-limited rational-point
search is used in it.

## 6. Why fixed-S Modular Chabauty does not immediately solve the family

For (5), if \(p\ge5\) divides \(a(3a-b)(3a+b)\), then p is a unit
on b, since b divides 486 and gcd(a,b)=1. Formula (6) gives
\(v_p(\Delta)>0\) and \(v_p(c_4)=0\): modulo p the final factor in
\(c_4\) is \(b^2\) if p divides a, and \(81a^2\) if p divides
\(3a-b\) or \(3a+b\). Thus the displayed model is minimal at p
and has multiplicative bad reduction there.

In fact every a>b in this coefficient family has at least one such
prime p>=5. Here is an elementary proof. Suppose the positive integer
\(a(3a-b)(3a+b)\) is supported only at 2 and 3.

- If 6 divides b, coprimality forces a=1, impossible.
- If b=2, a is a positive power of 3; both \(3a\pm2\) are odd,
  coprime to 3, and greater than 1, impossible.
- If b=3^j, j>=1, a is a power of 2 exceeding b. If j>=2,
  \(a\pm3^{j-1}\) are odd, coprime to 3, and the plus expression
  exceeds 1. If j=1, the two odd numbers a-1 and a+1 differ by 2
  and exceed 1; at most one is divisible by 3. Both cases contradict
  the alleged prime support of \(3a\pm b\).
- If b=1 and a is even, \(3a\pm1\) are odd, coprime to 3, and
  greater than 1. If b=1 and a is odd, the two numbers \(3a\pm1\)
  must be powers of 2 differing by 2; the only such positive powers
  are 2 and 4, giving a=1, again impossible.

Therefore none of these fibers has good reduction outside {2,3}.
Moreover the bad-prime support is not bounded across the entire
coefficient family: taking a to be arbitrarily large primes coprime to b
introduces those primes as multiplicative bad primes. This last statement
concerns the coefficient family; it does not assert that those fibers
contain original solutions.

Zehavi's 2025 Modular Chabauty requires a fixed finite S and an elliptic
scheme over the corresponding integral moduli problem. One may use it
after imposing additional control on this bad-prime support, but the
restriction b|486 alone supplies no such control. Likewise the j-invariant
of (5),

\[
j=-\frac{3b^2(72a^2+b^2)^3}{a^2(9a^2-b^2)^3},
\]

varies with a/b. Thus Choi's fixed-curve quadratic-twist theorem cannot be
applied to this entire family as if it were a single twist family.

## 7. Literature selected and actual use

Detailed dates, authors, URLs, retrieval identifiers, hypotheses, and
applicability are in `v19_elliptic_literature.json`. The main primary
sources are:

1. Michael Stoll, *Determining the rational points on a curve of genus 2
   and Mordell-Weil rank 1*, arXiv:2509.24604, 2025-09; ICM 2026.
   [Author manuscript](https://arxiv.org/html/2509.24604v1).
   Section 3's local-integral-point step is used in Theorem 1. The full
   algorithm needs a finite-index rank-at-most-one subgroup; it has not
   been executed here. Its stated general termination involves conjectures.
2. Stevan Gajović and J. Steffen Müller, *Linear quadratic Chabauty*,
   Israel J. Math. 270 (2025), 381–411; arXiv:2307.15781v4, 2025-11.
   [Author manuscript](https://arxiv.org/html/2307.15781v4).
   Appendix A's Runge method applies to the square-leading even sextic.
   The main p-adic method requires a Jacobian rank condition, not verified
   uniformly for our family.
3. Marius Leonhardt and Martin Lüdtke, *Affine Chabauty II*,
   arXiv:2602.05643v2, 2026-06.
   [Author manuscript](https://arxiv.org/html/2602.05643v2),
   [author implementation](https://github.com/martinluedtke/AffChab2).
   For the present genus-two curve with two rational boundary points over
   Q and S empty, its rank inequality becomes rank(J)<3. This numerical condition alone is
   not an execution of the method. An affine rational base point, a
   regular model, full-rank Mordell-Weil subgroup, bad-fiber data and
   Coleman-integral inputs remain to be supplied, with verification that
   the chosen integral model covers our original integer points. The two
   points at infinity are not affine base points. The author's Sage code
   has not been run here.
4. Sa'ar Zehavi, *Modular Chabauty: Effective S-Integral Point Computation
   On Curves with Elliptic Fibrations*, arXiv:2505.12947v1, 2025-05.
   [Author manuscript](https://arxiv.org/html/2505.12947v1).
   Section 6 diagnoses the missing fixed-S input on the actual family.
5. Seokhyun Choi, *Number of integral points on quadratic twists of
   elliptic curves*, arXiv:2509.03274v3, 2026-03 revision.
   [Author manuscript](https://arxiv.org/html/2509.03274v3).
   Its fixed-base-curve hypothesis is not available for the varying
   j-invariant here; a point-count bound is also not a list of all points.
6. PARI/GP official documentation, `ellrank`, `elltors`, `ellratpoints`.
   [Documentation](https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html).
   `ellrank` provides algebraic lower/upper bounds; a zero upper bound
   is meaningful. `ellratpoints` only searches a specified height and
   would not prove completeness. We do not use the latter.

Finite-field ECC discrete-log algorithms do not determine the full set
of rational or integral points of an elliptic curve over Q. Here finite
fields provide one-way congruence obstructions, while completeness in
Theorem 3 comes from the separately proved integer height bound.

## 8. Reproduction and limits

Run `python3 v19_elliptic_residual_checks.py` beside this note. It checks
14 multivariate polynomial identities, the uniform mod-5 obstruction,
and the complete domain (12). All comparisons and reconstruction use
integers or exact fractions. The JSON binds the checker, this note, and
the v17/v18 inputs by SHA256.

The optional `v19_elliptic_rank_audit.gp` can be run using PARI/GP. The
observed runtime was version 2.17.4; raw output and a summarized JSON are
saved separately. Those computations are not substituted for an exported
descent certificate or a Lean proof.

The new results do not bound rho globally, determine all Mordell-Weil
groups, or solve the original branch. They give an unbounded local
restriction, a geometric interpretation of the excluded boundary, and
the new finite exclusion rho<=10. Canonical cofactor J is a different
parameter from rho throughout; no equality between them is assumed.
