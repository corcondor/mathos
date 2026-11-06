# v19: canonical-numerator obstructions and a finite elimination certificate

Date: 2026-11-07 JST. This note records written deductions, actual SymPy
elimination, and independently checked integer/finite-field certificates.
It is not a new Lean proof or a DeepSeek run. Existing formal goals and
successful proof bodies were not changed.

## 1. Equation, scope, and new conclusions

The original right-hand side has **squared binomial indices**. In the
inherited branch `ell=1, j=i-3`, put `n=i` and

\[
A=\binom n3,\qquad
\binom A k=\binom{n^2}{6n-9}+k^2,\qquad
r=\min(k,A-k),\quad t=r-3n.
\]

Retain the necessary conditions from v16-v18:

\[
n\ge104,\quad 3n<r<10n/3,\quad t\ge3\sqrt n,\quad
Q=\frac{n(n-1)}{M}\mid r^3,
\]
\[
g=\gcd(n,3),\quad d=\gcd(n-1,6),\quad M=gd,
\quad Q_0=n/g,\quad Q_1=(n-1)/d.
\]

For `epsilon=0` when `k=r`, and `epsilon=1` when `k=A-r`, define

\[
N=n^2+2,\qquad
T_\epsilon=(r-\epsilon)^2-9n^2-6n-10>0,
\]
\[
G=\gcd(N,T_\epsilon),\qquad w=N/G,\quad J=T_\epsilon/G.
\tag{1}
\]

Thus `gcd(w,J)=1`. The canonical lower bound `w>=65` is the result of
v18 cofactor Section 7, which transfers the complete v17 certificate
and uses the inherited `delta>=13` for its small-q part. We do not rerun
that older certificate here.

In the small branch, put

\[
c_0=10w+2J,\qquad c_1=25w+3J.
\]

v18 cofactor Section 2 proves

\[
Q_0^2\mid c_0^3,\qquad Q_1^2\mid c_1^3.
\tag{2}
\]

**New conclusions.**

1. In both branches, the canonical numerator satisfies
   \(J\not\equiv2\pmod4\).
2. In the small branch,
   \(v_2(J)\in\{0,2\}\), equivalently
   \(J\bmod8\in\{1,3,4,5,7\}\).
3. In the small branch, every positive canonical pair obeys the uniform
   quartic inequality (7) below.
4. A finite divisor elimination certificate, with all bounds derived
   from (1)-(2) and the inherited gap, excludes **all `1<=J<=16`**.
   Hence

\[
\boxed{J\ge17\qquad(k=r).}
\tag{3}
\]

The second 2-adic strengthening was proposed by the root researcher and
independently checked here. No upper bound on J is obtained. The
complementary case `J=1`, either entire branch, and the four-variable
problem remain unresolved.

## 2. A uniform 2-adic obstruction

Write `R=r-epsilon`. If n is even, `v2(N)=1` and

\[
9n^2+6n\equiv0\pmod8.
\]

The possible square residues modulo 8 give

\[
T_\epsilon\equiv R^2-2\in\{2,6,7\}\pmod8.
\]

Thus `v2(T_epsilon)` is either 0 or 1, and its entire 2-part is removed
by `G=gcd(N,T_epsilon)`. Consequently J is odd.

If n is odd, N and G are odd. For even R, T and J are odd. For odd R,
`R^2=n^2=1 (mod4)` and `6n=2 (mod4)`, so `4|T`, hence `4|J`.
This proves the first conclusion for every n and R with positive T;
the cube-divisibility hypothesis is not needed for it.

Now take the small branch. If J is even, the preceding argument gives
odd n and odd r. Since `Q|r^3`, Q is odd. For odd n,

\[
v_2(Q)=v_2(n-1)-1,
\]

because `g` is odd and `v2(d)=1`. Therefore `v2(n-1)=1`, or
`n=3 (mod4)`. Reducing the same expression modulo 8 now gives
`T_0=4 (mod8)`. As G is odd, `v2(J)=2` exactly. In particular this
excludes J=2,6,8,10,14,16 and every member of the corresponding
infinite residue families.

## 3. What exact elimination does, and what it does not do

Use the two polynomial equations

\[
f=qw-n^2-2=0,\qquad
h=qJ-R^2+9n^2+6n+10=0.
\]

Their resultant with respect to q is `-F`, where

\[
\boxed{F=wR^2-(9w+J)n^2-6wn-10w-2J.}
\tag{4}
\]

The exact identity `w*h-J*f=-F` also proves this elimination directly.
On the chart `w!=0`, recovery is `q=(n^2+2)/w`. An integer point must
still satisfy `w|(n^2+2)` and `q>0`; the rational polynomial equation
alone does not enforce those conditions.

For J=1 and J=2, SymPy 1.14.0 actually computed lexicographic bases over
QQ, then used the Rabinowitsch equation

\[
1-swn(n-1)=0
\]

and eliminated s. The saturated ideal is unchanged in both cases, and
the ideals are not zero-dimensional. For J=1 the basis is exactly

\[
q-R^2+9n^2+6n+10,\qquad
wR^2-(9w+1)n^2-6wn-10w-2.
\]

For J=2 the first polynomial is `q-T/2` and the second is (4) with
J=2. After q is removed, one nonzero equation in `(R,n,w)` remains:
the algebraic set has dimension 2. Equivalently, (4) is a primitive
linear polynomial in w with relatively prime coefficient and constant
term in QQ[n,R], so it is irreducible. Saturation does not create a
finite set of rational or integer points.

The auxiliary inverse s is a rational/algebraic coordinate, not an
additional integer unknown. Saturation describes the Zariski closure
of the open part; it does not replace the explicit inequalities
`n>=104,w>0`. Likewise, rational Bézout variables for `gcd(w,J)=1`
would not encode integer coprimality. We retain that gcd condition
directly in the finite integer domain.

This is where the recent RUR literature changes the workflow: its
zero-dimensional input condition has to be proved before applying the
algorithm. A basis of the positive-dimensional system (4) is not an
integer-point completeness result. The complementary J=1 computation
has not met that condition.

## 4. A uniform quartic bound on w

For the small branch,

\[
T_0=6n(t-1)+t^2-10
\ge18n^{3/2}+3n-10>18n^{3/2}.
\]

Since n>=104,

\[
N<(5001/5000)n^2.
\]

Using `w/J=N/T_0`, we obtain

\[
\boxed{\frac wJ<\frac{1667}{30000}\sqrt n.}
\tag{5}
\]

The first nonzero positive divisibility in (2) gives

\[
n^2\le g^2c_0^3\le9(10w+2J)^3.
\tag{6}
\]

Combining (5) and (6), without division by a potentially zero quantity,
proves

\[
\boxed{30000^4w^4<9\,1667^4J^4(10w+2J)^3.}
\tag{7}
\]

All variables in the denominators used above are positive. This bound
is valid for every positive J, rather than just the finite families
certified below. For fixed J the function

\[
\frac{w^4}{(10w+2J)^3}
\]

is strictly increasing on w>0, because its derivative is

\[
\frac{w^3(10w+8J)}{(10w+2J)^4}>0.
\]

It tends to infinity. Thus (7) gives a unique finite upper interval
for w. Its last admissible integer is found entirely by exact integer
comparisons; the producer uses binary search and the independent
verifier uses sequential boundary detection.

### A short exclusion of J<=6

For J<=5 and w>=65, (5) implies `sqrt(n)>(6000/1667)w`, while
`c0<=10w+10<=(132/13)w`. Equation (6) consequently forces

\[
w<9(132/13)^3(1667/6000)^4
=\frac{30834840728763753}{549250000000000}<65,
\]

a contradiction. J=6 is excluded by Section 2. Therefore `J>=7`
already follows without new finite reconstruction. The stronger
`J>=17` uses the finite certificate in the next section.

## 5. Complete divisor domains and the J<=16 certificate

For a positive integer c, define

\[
D(c)=\prod_{p\mid c}p^{\lfloor3v_p(c)/2\rfloor}.
\]

Prime-by-prime comparison proves the exact equivalence

\[
e^2\mid c^3\quad\Longleftrightarrow\quad e\mid D(c).
\tag{8}
\]

Fix an allowed J and a positive w satisfying `w>=65`, (7), and
`gcd(w,J)=1`. Every possible n from the first condition in (2) occurs
in the following finite reconstruction:

1. Take **every** positive divisor e of D(c0).
2. Put n=e or n=3e.
3. Retain only `n>=104` and `gcd(n,3)=n/e`.
4. Retain only the exact consequence of (5),
   `30000^2*w^2 < 1667^2*J^2*n`.

There is no chosen cutoff for n. Its finite domain follows from (8).
For each retained n, compute `d=gcd(n-1,6)` and check
`((n-1)/d)^2 | c1^3` exactly. The complete counts are:

| J | Largest w from (7) | Primitive w>=65 | Normalized n records | After (5) | After second divisibility |
|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 | 0 |
| 3 | 8 | 0 | 0 | 0 | 0 |
| 4 | 24 | 0 | 0 | 0 | 0 |
| 5 | 56 | 0 | 0 | 0 | 0 |
| 7 | 210 | 125 | 1,311 | 2 | 0 |
| 9 | 568 | 336 | 3,757 | 5 | 0 |
| 11 | 1,262 | 1,089 | 15,916 | 27 | 0 |
| 12 | 1,786 | 574 | 4,306 | 0 | 0 |
| 13 | 2,458 | 2,209 | 35,847 | 52 | 0 |
| 15 | 4,352 | 2,287 | 75,715 | 73 | 0 |

J=2,6,8,10,14,16 are excluded for all n by Section 2. Altogether,
there are 6,620 primitive `(J,w)` values, 237,434 raw divisor/g records,
136,852 normalized n records, and **159** values after the gap bound.
All 159 fail the second divisibility in (2). These are complete
structural families, not a sample of small n or r.

No surviving point needs reconstruction of q or r, an original
binomial equality check, or a new defect test. This only excludes
the necessary-condition system for the stated J interval; it makes
no claim that those necessary conditions characterize original
solutions for other J.

## 6. Zero-dimensional elimination certificates for the finite domains

For each `(J,w)` with a nonempty first domain, let X be the complete
set of n values retained in Section 5, and form the monic polynomial

\[
P(x)=\prod_{a\in X}(x-a).
\]

Construct the complete second domain

\[
Y=\{de+1:e\mid D(c_1),\ d\in\{1,2,3,6\},
                    \ \gcd(de,6)=d\},
\]

and its monic polynomial `H(x)=product_{b in Y}(x-b)`.
Every integer n satisfying both divisor conditions must be a common
root of P and H. The ideal generated by P is zero-dimensional: its
finite roots are exactly the explicitly reconstructed integers X.
This finite-domain step, not a generic Gröbner computation, supplies
the missing completeness condition.

For each of the 110 nonempty `(J,w)` domains, the producer chooses a
prime p for which X and Y have disjoint reductions. It computes

\[
\overline H=H\bmod P\quad\text{in }\mathbb F_p[x]
\]

and records polynomials U,V satisfying the directly checkable identity

\[
\boxed{UP+V\overline H=1\quad\text{in }\mathbb F_p[x].}
\tag{9}
\]

SymPy also computes the corresponding one-variable Gröbner basis,
which is `[1]`. The independent verifier does not trust that string:
it reconstructs X,Y,P,H, verifies primality, performs modular
polynomial arithmetic, and checks (9) coefficient by coefficient.
Any common integer root would reduce to a common root modulo p,
contradicting (9). All polynomials are monic before reduction, so
no lost leading coefficient or denominator exception is present.

The largest modulus is 107; P has degree at most 5 and Y has at most
96 elements. Small characteristic is harmless here: (9) is an
identity over the stated prime field. We are not applying a RUR
theorem requiring sufficiently large characteristic.

For illustration only, the J=7,w=101 first domain is `{98304}`. Its
certificate uses p=11, `P=x+3`, `H mod P=9`, `U=0`, `V=5`, so (9)
is `5*9=1 (mod11)`. The complete file contains all 110 identities,
not just this example.

## 7. Literature and its actual role

The paper/source details and access limitations are recorded in
`v19_groebner_sources.json`.

- **Alexander Demin, Fabrice Rouillier, Joao Ruiz**, *Reading Rational
  Univariate Representations on lexicographic Gröbner bases*, first
  submitted 2024-02-11, v3 2025-05-23,
  [arXiv:2402.07141v3](https://arxiv.org/abs/2402.07141v3).
  Its RUR and separation algorithms take zero-dimensional ideals;
  shape position is not required. The proof discussions assume
  characteristic zero or sufficiently large characteristic. We use
  the hypotheses to determine where a finite-domain construction
  is necessary, not as a theorem that the original Diophantine
  problem is finite. The full text was inspected.
- The authors' [RationalUnivariateRepresentation.jl documentation](https://newrur.gitlabpages.inria.fr/RationalUnivariateRepresentation.jl/),
  generated 2026-10-28, documents zero-dimensional systems over QQ
  and prime fields and separating-element checks. The software
  was not installed or run here.
- **Jérémy Berthomieu, Christian Eder, Mohab Safey El Din**, *New
  efficient algorithms for computing Gröbner bases of saturation
  ideals (F4SAT) and colon ideals (Sparse-FGLM-colon)*, first
  submitted 2022-02-27, v2 2023-07-27,
  [arXiv:2202.13387v2](https://arxiv.org/abs/2202.13387v2).
  Section 1 states the Rabinowitsch elimination formula for
  saturation and distinguishes it from zero-dimensional change
  of order. This supplies the precise open-chart interpretation
  used in Section 3. We ran the elementary Rabinowitsch construction
  in SymPy, not the F4SAT implementation.
- The official [msolve release page](https://msolve.lip6.fr/binaries/index.html)
  lists release 0.11.0 dated 2026-10-09. It confirms that recent
  maintained implementations exist, but no msolve performance or
  execution claim is made for this workspace.
- The [SymPy polynomial documentation](https://docs.sympy.org/latest/modules/polys/reference.html)
  documents the actual resultant, Gröbner-basis, extended-gcd and
  zero-dimensionality interfaces used by the producer. The local
  version was 1.14.0.

Thus the substantive new arithmetic is (7), the uniform 2-adic
restriction, and the finite J exclusion. The modern literature
informed the certified elimination design and exposed the remaining
positive-dimensional obstruction; it is not being credited with
proving an integer-point theorem it does not state.

## 8. Reproduction, dependencies, and limits

Run in the directory containing the files:

```sh
python v19_canonical_J_checks.py
python v19_canonical_J_verify.py
```

The first script requires SymPy. The second requires only the Python
standard library and imports neither the producer nor SymPy. It
independently regenerates the complete divisor domains and all exact
boundaries. Its saved result is `v19_canonical_J_verification.json`.

The certificate `v19_canonical_J_certificate.json` has SHA256
`314edd42c7c884de81c46d9a56ba2af9a11d4829bd85c3f2caf699f99305d57e`.
The verifier reports 159 reconstructed records and 110 checked
Bézout identities, with no survivors.

Inherited mathematical inputs are `v17_square_root_gap.md` for the
square-root gap and `v18_neighbor_cofactor_height.md` Sections 2 and
7 for the two square/cube divisibilities and canonical `w>=65`.
The latter depends on the earlier complete cofactor certificate and
defect lower bound as stated there. No new execution of those older
large certificates is claimed.

The universal 2-adic restrictions apply to all J. The finite complete
exclusion in (3) is limited to `J<=16` and the small branch. In
particular, it does not bound J above or solve the complementary
J=1 surface. All computation here is exact arithmetic; none is a
Lean kernel certificate or an external peer review.
