# v19: a uniform non-torsion section on the residual elliptic family

Date: 2026-11-07 JST. Written proof and exact polynomial verification;
this is not a new Lean proof. No assertion of literature-wide novelty is made.

## 1. Statement and scope

For coprime positive integers \(a>b\), consider

\[
E_{a,b}:\quad Y^2=X^3+A_4X+A_6,
\]
\[
A_4=-3b^2(72a^2+b^2),\qquad
A_6=2b^2(648a^4+180a^2b^2-b^4).
\tag{1}
\]

This is the fixed-\((a,b)\) residual curve from v17/v18. Its discriminant is

\[
\Delta=-995328a^2b^4(3a-b)^3(3a+b)^3\ne0.
\tag{2}
\]

**Theorem.** The rational point

\[
P_0=\bigl(4a^2-b^2,\ 8a(a^2+3b^2)\bigr)
\tag{3}
\]

has infinite order for every such pair except \((a,b)=(3,1)\).
At \((3,1)\) it has exact order four. In particular,
\(\operatorname{rank}E_{a,b}(\mathbb Q)\ge1\) for every pair other than
that exception. This theorem does **not** require \(b\mid486\), a height
bound, or an unproved rank assumption.

## 2. Proof

Substitution proves that (3) lies on (1). Its Y coordinate is nonzero.
Put \(d=a^2+3b^2\). The tangent slope at \(P_0\) is

\[
\lambda=\frac{3(4a^2-b^2)^2+A_4}{16a(a^2+3b^2)}
=\frac{3a(a^2-5b^2)}{d}.
\tag{4}
\]

Suppose that \(P_0\) has finite order. Since \(Y(P_0)\ne0\), its double
is an affine point, also of finite order. The Nagell–Lutz integrality
theorem applies to the integral short Weierstrass equation (1), without
a minimal-model assumption. Consequently

\[
x(2P_0)=\lambda^2-2(4a^2-b^2)\in\mathbb Z.
\]

Thus \(\lambda^2\) is an integer. A rational number whose square is an
integer is itself an integer, so (4) implies

\[
d\mid3a(a^2-5b^2)=3a(d-8b^2),\qquad d\mid24ab^2.
\]

As \(\gcd(a,b)=1\), we have \(\gcd(d,b)=1\); hence

\[
d\mid24a.\tag{5}
\]

Furthermore \(\gcd(d,a)=\gcd(3,a)\), which divides 3. A prime at least
5 dividing d could therefore not divide a, contradicting (5). Only 2
and 3 can divide d. Their exact possible valuations are elementary:

- If a and b are both odd, \(d\equiv4\pmod8\), so \(v_2(d)=2\).
  Otherwise coprimality forces one odd and one even, and d is odd.
- If \(3\mid a\), then \(3\nmid b\) and \(d\equiv3\pmod9\), so
  \(v_3(d)=1\). If \(3\nmid a\), then \(d\equiv1\pmod3\).

It follows that \(d\mid12\). Since a>b>0, d is at least 7. If b were
at least 2, it would be at least \(3^2+3\cdot2^2=21\), impossible.
Therefore b=1 and \(a^2+3\mid12\), which forces a=3.

For (a,b)=(3,1), equation (1) has \((A_4,A_6)=(-1947,108214)\),
and (3) is (35,288). Its tangent slope is 3 and the group law gives

\[
2P_0=(-61,0).
\]

This is a nonidentity point of order two; consequently \(P_0\) has
exact order four. All other pairs have already been proved non-torsion.
QED.

The external theorem used here is Andrew V. Sutherland, MIT 18.782,
Lecture 24 (2013-12-03), Theorem 24.21:
[official lecture notes](https://math.mit.edu/classes/18.782/2013fa/LectureNotes24.pdf).
Only the integrality conclusion for finite-order affine points is used.
The reduction from that theorem to (5) and the uniform exception
classification above are proved here.

## 3. Consequence for the original residual problem

In the branch \(\ell=1,j=i-3\) of the original squared-index equation,
v17/v18 give coprime a>b>0, b|486 and

\[
0<\rho<\frac{216a^2+760b^2}{1377},\qquad
y^2=F(a,b,\rho).
\]

The map to (1) is

\[
X=4a^2-b^2-4\rho,\qquad Y=4y.
\]

Point \(P_0\) occurs at \(\rho=0\), so it is **not** an admissible
residual solution; its purpose is to prove a statement about the whole
curve's Mordell–Weil rank. At the exceptional pair (3,1), the strict
residual upper bound is \(\rho<2704/1377<2\). Only \(\rho=1\)
could remain. But

\[
F(3,1,1)=4853,\qquad 69^2<4853<70^2,
\]

so it is not a square. Equivalently it violates the independent v19
mod-5 obstruction \(\rho\not\equiv b^2\pmod5\).

**Every fixed-\((a,b)\) residual curve capable of containing a solution
of the original branch therefore has positive rational rank.** A
strategy that tries to eliminate all these curves by proving rank zero
cannot succeed. The ordinary Chabauty condition rank<genus is likewise
unavailable on this genus-one family. This does not prevent descent,
elliptic logarithms, integral-point algorithms, or methods using a
different fibration with additional conditions.

In particular the fixed-\((b,\rho)\) elliptic quotient in
`v19_elliptic_residual.md` is a different family; some of its fibers do
have rank zero. No conflict exists between these statements. The
genus-two curve before taking that quotient has its own Jacobian rank,
which is not determined by the theorem above.

## 4. A related order-three section

Equation (1) also has

\[
P_3=(3b^2,\ 4b(9a^2-b^2))
\]

of exact order three: the tangent slope is -3b, and doubling gives
\(2P_3=-P_3\). Under
\(X=x+3b^2,\ Y=y-3bx+4b(9a^2-b^2)\), its Tate equation is

\[
y^2-6bxy+8b(9a^2-b^2)y=x^3.
\]

Its residual coordinate is \(\rho=a^2-b^2\), exactly the square-root
boundary already excluded in v17. The detailed reconstruction is in
`v19_elliptic_residual.md`. We exclude the known order-three subgroup
there, not every possible torsion point on every curve.

## 5. Verification and limits

`v19_residual_positive_rank_checks.py` checks the defining point,
discriminant, tangent numerator and order-three identities by sparse
polynomial arithmetic over the integers. It checks the exceptional
doubling with exact fractions, and the finite residue classes used for
the two valuation assertions. These tests support the written uniform
proof; they are not a substitute for Nagell–Lutz or its formalization.

An optional PARI/GP experiment, stored separately, returned
`ellrank(E_3,1)=[0,0,0,[]]` and rational torsion group of order 12
with invariant factors [12]. Neither the rank computation nor the full
torsion classification is required for the theorem or the original
residual exclusion. The proof needs only the explicitly doubled point.

The original four-variable equation and the unbounded residual family
remain unsolved. No new Lean execution, complete Mordell–Weil basis,
or new analytic-rank-to-algebraic-rank inference is claimed.
