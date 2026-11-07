# v19 supplement: integral residual 3-covers and an exact finite-field sieve

2026-11-07 JST. Written algebra, symbolic elimination identities, and exact
integer / finite-field certificates. No new Lean or DeepSeek execution.

**What is added.** The residual square condition is normalized into two
positive integer factors with a cubic product. Their cube-free parts give
an explicit finite collection of genus-one covers for every fixed coefficient
pair. The maps have an integer polynomial ideal-membership certificate.
Complete finite-field tables and a separate verifier exercise this reduction.

**Important dependency correction.** Positivity of the new parameter `Z`
already follows from the v17 square-root gap. The 6,221-case finite-field
audit below is an independent verification from weaker residual inputs;
it is **not a new narrowing of the original solution set**. No claim of
novelty for the general method of 3-descent is made.

## 1. Scope and inherited variables

The original equation remains

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

We study \(\ell=1,j=i-3\), with
\(n=i,A=\binom n3,r=\min(k,A-k),t=r-3n\), for both branches of k.
The v17/v18 residual variables obey

\[
\frac ab=\frac{(9t^2+27t+27)n+t^3}{81n(n-1)},\quad
\gcd(a,b)=1,\quad b\mid486,\quad 27a\ge31b,
\tag{1}
\]
\[
\rho=a^2+ab(9n-t-6)-b^2(t^2+3t+3)>0,
\quad\rho\equiv a^2\pmod b,
\quad1377\rho<216a^2+760b^2.
\tag{2}
\]

There is an integer y, which we take nonnegative, with

\[
\begin{aligned}
y^2=F(a,b,\rho)={}&4a^6+(24b^2-12\rho)a^4\\
&+(36b^4+60b^2\rho+12\rho^2)a^2-3b^2\rho^2-4\rho^3.
\end{aligned}\tag{3}
\]

These inputs and the reconstruction formulas are in
`v17_square_root_gap.md`, `v18_residual_gap.md`, and
`v19_elliptic_residual.md`. In particular, v17 gives
\(n\ge104\) and \(t^2>9n\).

## 2. An integral normalization of the order-three factorization

Set

\[
z=a^2-b^2-\rho,\qquad
L=6a^2+2b^2+3\rho=9a^2-b^2-3z.
\]

Direct polynomial elimination gives

\[
\boxed{F(a,b,\rho)-b^2L^2=4z^3.}\tag{4}
\]

Since (2) gives b|z, put \(Z=z/b\). Equation (4) shows b²|y²,
and prime valuations imply b|y. Write \(Y=y/b\). Then

\[
Y^2-L^2=4bZ^3.
\]

Squares modulo 4 show that Y and L have the same parity. Consequently

\[
U=\frac{Y-L}{2},\qquad V=\frac{Y+L}{2}
\]

are integers, and the square condition becomes the exact pair

\[
\boxed{UV=bZ^3,\qquad V-U+3bZ=D,\quad D=9a^2-b^2.}\tag{5}
\]

Conversely, integer U,V,Z satisfying (5), with
\(\rho=a^2-b^2-bZ\) and \(y=b(U+V)\), satisfy (3) and
\(\rho\equiv a^2\pmod b\). Thus no residual square is lost in this
normalization. Positivity, (1)–(2), integer reconstruction of n,t, and
the original binomial equation remain separate requirements.

This is the residual-family version of the factorization attached to the
rational order-three point. The earlier `v12_three_descent.md` used the
different curve \(Y^2=X^3+(6HT^2)^2\). The v19 residual Tate equation was
already known; its precise integral normalization (5) is the addition here.

### The sign follows exactly from the old gap

Substituting (1)–(2), with no approximation, gives

\[
\boxed{
81n(n-1)\frac Zb=(t^2-9n)(9n+t^2+6t).
}\tag{6}
\]

All factors other than \(t^2-9n\) are positive. Hence v17 immediately
implies \(Z>0\). Equation (4), y≥0, and L>0 then give Y>L, so

\[
Z,U,V\in\mathbb Z_{>0},\qquad V>U.
\]

In particular \(\rho\le a^2-b^2-b\). This is an exact translation of
the inherited gap, not an independently stronger original bound.
The positive integer U also gives the useful cover constraint

\[
\boxed{b(Z^3+3Z)\ge D+1,}\tag{7}
\]

because \(UV=U(U+L)\ge L+1\).

## 3. Explicit finite cube classes for fixed (a,b)

Let \(S\) be the set of primes dividing \(bD\). For any prime
\(p\notin S\), p cannot divide both U and V: otherwise (5) gives
p|Z and p|L, hence p|D, a contradiction. Taking valuations in UV=bZ³
therefore proves

\[
p\notin S\quad\Longrightarrow\quad
v_p(U)\equiv v_p(V)\equiv0\pmod3.
\tag{8}
\]

This includes 2 and 3 whenever they are outside S; no exceptional-prime
argument is suppressed. Some additional exact gcd statements are

\[
\gcd(U,V)\mid L,\qquad \gcd(U,V,Z)\mid D,
\qquad\operatorname{rad}(\gcd(U,V))\mid\operatorname{rad}(bD).
\]

Write uniquely

\[
U=\alpha u^3,\qquad V=\beta v^3,
\]

where u,v are positive and α,β are positive cube-free integers supported
on S. Equation (5) implies

\[
\alpha\beta b^2=\gamma^3,\qquad
Z=\frac{\gamma uv}{b},\qquad b\mid\gamma uv
\tag{9}
\]

for an integer γ>0. To see that γ is integral, first
\(\gamma=bZ/(uv)\) is rational and its cube is the integer αβb²;
a rational number with integral cube is integral.

For each p∈S, choose \(i=v_p(\alpha)\in\{0,1,2\}\). With
\(e=v_p(b)\), the exponent \(j=v_p(\beta)\in\{0,1,2\}\)
is uniquely determined by \(i+j+2e\equiv0\pmod3\). Thus there are
exactly \(3^{|S|}\) formal coefficient choices before any local or
positivity exclusions. Every original residual point is covered by one of

\[
\boxed{\beta v^3-\alpha u^3+3\gamma uv=D.}\tag{10}
\]

The recovery conditions are

\[
u,v>0,\quad b\mid\gamma uv,\quad
\rho=a^2-b^2-\gamma uv>0,\quad
y=b(\alpha u^3+\beta v^3),
\tag{11}
\]

together with the inherited restrictions and reconstruction of n,t.
The coefficient set depends on (a,b); its size is not a uniform constant
as a varies. This is an explicit finite cover, not a Selmer-group
computation or a solution of all the cover curves.

### An integer ideal-membership certificate

Put

\[
H=\beta v^3-\alpha u^3+3\gamma uv-D,
\quad R=\gamma^3-\alpha\beta b^2,\quad
L_c=D-3\gamma uv.
\]

The exact identity

\[
\begin{aligned}
&F(a,b,a^2-b^2-\gamma uv)-b^2(\alpha u^3+\beta v^3)^2\\
&\qquad=-b^2(L_c+\beta v^3-\alpha u^3)H+4u^3v^3R
\end{aligned}\tag{12}
\]

certifies membership in the ideal \(\langle H,R\rangle\) over the
integer polynomial ring. This explicitly checks the cover-to-residual
map; it does not rely on a CAS reporting that a Gröbner basis vanishes.
The reverse direction was proved by the integer factorization above.

### Why these covers still have genus one

Homogenize (10):

\[
\beta v^3-\alpha u^3+3\gamma uvs-Ds^3=0.
\tag{13}
\]

A singular projective point would satisfy
\(\alpha u^2=\gamma vs\), \(\beta v^2=-\gamma us\),
\(\gamma uv=Ds^2\). If any coordinate is zero, all three are zero,
which is not a projective point. Otherwise multiplying the first two
and using the third gives \(\alpha\beta D=-\gamma^3\). By (9),
this would force D=−b², hence a=0. Therefore (13) is smooth in
characteristic zero and has genus one.

One must not call every such curve an elliptic curve with a known group
law: a rational point has not been supplied on every coefficient cover.
When a rational point is available it can be used as an origin. The cover
construction does not turn the unbounded problem into a zero-dimensional
system.

## 4. An actual finite-field computation, with a precise baseline

For each prime 5≤p≤61, b is invertible. Put
\(s=\rho/b^2\), \(q=a^2/b^2\). The elliptic quotient is

\[
E_s:\quad \eta^2=\xi^3+48(9s-1)\xi+1296s^2-2880s-128,
\quad\xi=4q+8-4s.
\tag{14}
\]

The saved tables contain **every** s∈Fₚ and every permitted square q,
not a selection of examples. They also record the complete finite-field
point count. On every nonsingular fiber, the known point
\(T=(12,4(9s+8))\) is doubled with the ordinary group law, verifying
\(2T=-T\), and its group order three is consistent with the point count.
There are 496 fibers in total, 464 nonsingular.

To test the sieve on a mathematically complete domain, temporarily use
only (1)–(3), not the direct sign identity (6), and suppose Z≤0.
The existing strict residual bound gives

\[
1161a^2<2137b^2,\qquad
\frac{1161a^2-2137b^2}{1377b}<Z\le0.
\tag{15}
\]

Since b is one of the 12 divisors of 486, (15) is finite without imposing
an external cutoff on n, a, or ρ. It has 102 coprime coefficient pairs
and 6,323 integer triples, of which 6,221 have Z<0.

For **all 6,221 negative-Z cases**, the certificate supplies a prime at
most 61 of good reduction for (14) such that the prescribed ξ has no
y-coordinate. The independent checker recomputes F modulo that prime,
enumerates all quadratic residues, and separately checks the quotient
curve. The existing whole-fiber mod-5 condition excludes 1,252 of these
cases; using the joint (a/b,ρ/b²) information excludes all 6,221.
These counts measure filtering on this exact same bounded domain;
they are not a runtime claim or evidence of global independence.

For Z=0, the two reconstructed roots have

\[
t_-=-\frac{2(3a+b)}{a+b}<0,\qquad
t_+=\frac{3a+b}{a-b},\qquad n_+=t_+^2/9.
\]

By 27a≥31b, t₊≤30 and n₊≤100<104. Every one of the 102 boundary
cases is also stored and reconstructed in both signs. The resulting
sign exclusion agrees with (6). It is retained as a method-validation
certificate; the direct inherited proof is simpler.

The complete witness histogram is:

| Prime | Excluded negative-Z cases |
|---:|---:|
| 5 | 1731 |
| 7 | 1306 |
| 11 | 1199 |
| 13 | 790 |
| 17 | 487 |
| 19 | 284 |
| 23 | 199 |
| 29 | 110 |
| 31 | 56 |
| 37 | 32 |
| 41 | 10 |
| 43 | 9 |
| 47 | 2 |
| 53 | 1 |
| 59 | 4 |
| 61 | 1 |

This uses finite-field arithmetic also used in elliptic-curve cryptography.
It does **not** compute a discrete logarithm or supply the global
Mordell–Weil information needed for a full Mordell–Weil sieve. In
particular, the previously known non-torsion point alone is not a
certificate that its subgroup contains every rational residual point.

## 5. A uniform limitation of the whole-fiber modular test

There is a useful reason not to keep searching larger primes for a
condition involving only ρ/b².

**Proposition.** For every prime p≥5 and s∈Fₚ, the affine curve
\(y^2=F(x,1,s)\) has an Fₚ-point, except exactly when p=5 and s=1.

**Proof.** The sextic discriminant is

\[
3869835264s^4(4s+3)(9s+8)^6.
\]

At s=0 or s=−3/4 the point (x,y)=(0,0) is present. At s=−8/9,
(x,y)=(1/3,0) is present. The factorizations are checked as exact
polynomial identities. In all other cases the smooth projective curve
has genus two and has two rational points at infinity, since its leading
coefficient is 4. The Hasse–Weil bound gives at least
\(p+1-4\sqrt p>2\) points for p≥19, so at least one is affine.
The displayed inequality follows from (p−1)²>16p for p≥19.
The complete tables for p=5,7,11,13,17 give exactly the asserted exception.
QED.

Thus the original mod-5 whole-fiber exclusion is already the only one of
this particular mod-prime type. Joint restrictions with a, prime-power
tests, the integrality of n,t, or global group information can still give
stronger sieves. This proposition does not assert solubility over Zₚ,
over Q, or over Z.

The only external input for this proposition is Hasse–Weil; see Poonen,
*Lectures on rational points on curves*, Section 3.3, printed page 52.
It is a limitation theorem for the chosen test, not an assertion that
finite-field methods cannot advance the original problem.

## 6. Concrete round trips

For (a,b,ρ)=(13,2,1), the residual square gives

\[
Z=82,\quad U=656=82\cdot2^3,\quad V=1681=41^2,
\]
\[
(\alpha,\beta,\gamma,u,v)=(82,1681,82,2,1),\quad D=1517.
\]

Here S={2,37,41}, so all 27 formal cube classes are generated, including
this one, and
\(1681-82\cdot2^3+3\cdot82\cdot2=1517\).
The reconstruction gives (t,n)=(0,0) or (2337,281219/3), so this is
not a solution of the original equation.

Two further round trips use actual auxiliary candidates already present
in the v19 δ-certificate: (n,r)=(41553,126882) and (73696,223720).
Their (a,b,ρ) values are (6469,486,501997) and (2551,243,52792).
Each produces 2,187 formal cube classes; the class containing its
residual point is checked along with all recovery identities. These
candidates were already rejected by the original binomial congruences
in v19. Their purpose here is to verify the new representation on
nontrivial data, not to claim solutions or new exclusions.

## 7. Reproduction and evidence limits

Run in this directory:

```sh
python3 v19_residual_cube_cover_checks.py
python3 v19_residual_cube_cover_verify.py
```

The producer uses SymPy for exact symbolic identities. Its finite-domain
certificate and local tables contain complete data. The verifier uses
only the Python standard library, does not import the producer, and
independently checks sparse polynomial coefficients, a coarser complete
domain, the original sextic modulo each witness prime, and all points
of every finite-field quotient. It regenerates the cube classes by
choosing β exponents first, whereas the producer chooses α exponents.

The current result is an explicit residual cover and reproducible
finite-field method audit. It does not increase δ≥25, J≥17, or ρ≥11;
does not determine all rational/integer points on the covers; and does
not solve the full original equation. Internal AI review is not external
mathematical peer review.

Primary method references:

- A. Sutherland, MIT 18.783, Lecture 2 (2023):
  <https://math.mit.edu/classes/18.783/2023/LectureNotes2.pdf>.
  The explicit finite-field doubling check uses the short Weierstrass group law.
- N. Bruin and M. Stoll, *The Mordell-Weil sieve: proving non-existence
  of rational points on curves* (2009/2010), Sections 1–3:
  <https://mathe2.uni-bayreuth.de/stoll/papers/MWsieve.pdf>.
  A full sieve needs the appropriate global subgroup and index information;
  local point tables alone do not supply it.
- B. Poonen, *Lectures on rational points on curves* (2006), Section 3.3:
  <https://math.mit.edu/~poonen/papers/curves.pdf>.
  Hasse–Weil supplies the all-primes part of Section 5.
- M. Stoll, *Determining the rational points on a curve of genus 2 and
  Mordell-Weil rank 1*, arXiv:2509.24604, displayed manuscript dated
  2026-08-24: <https://arxiv.org/html/2509.24604v1>.
  Its complete algorithm requires a finite-index subgroup of the Jacobian;
  no execution of that algorithm is claimed here.
