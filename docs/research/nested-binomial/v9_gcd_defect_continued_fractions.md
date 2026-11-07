# A complete continued-fraction reduction for a bounded gcd defect

## Scope

The equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

In this note \(\ell=1,\ j=i-3\), and

\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
G=\gcd(A,X),\quad S=A/G,\quad r=\min(k,A-k).
\]

Every remaining solution has \(n\ge104\). Both outer branches are
covered by the preceding gap and gcd theorems. The v8 results give

\[
G\mid r^3,\qquad 3n<r<10n/3,\qquad S\mid n-2,
\qquad n<2^{192S}.
\tag{1}
\]

This note turns every bounded range of S into finitely many short
continued-fraction computations. The large bound in (1) is used as
a denominator bound, without enumerating every n below it.

The complete finite application \(1\le S\le12\) has been verified.
It gives the following uniform necessary condition for the original
offset-three branch:

\[
\boxed{\ell=1,\ j=i-3\text{ and the original equation}
\quad\Longrightarrow\quad S\ge13.}
\tag{0}
\]

In particular, every case with \(A\mid X\) is excluded. No restriction
on the number of distinct prime factors of n-2 is made here.

## 1. A fixed list of cubic curves

The integer

\[
T=\frac{r^3}{G}=\frac{6S r^3}{n(n-1)(n-2)}
\]

satisfies

\[
\boxed{162S<T<229S.}
\tag{2}
\]

The lower bound follows from \(r>3n\) and
\(n(n-1)(n-2)<n^3\). For the upper bound, the functions
\(n/(n-1)\) and \(n/(n-2)\) are decreasing for \(n>2\).
Thus

\[
T<\frac{2000S}{9}\frac{n^2}{(n-1)(n-2)}
\le\frac{2000S}{9}\frac{104^2}{103\cdot102}<229S.
\]

The last comparison is an integer inequality, with positive margin

\[
229\cdot9\cdot103\cdot102-2000\cdot104^2=20866.
\]

Put \(x=n-1\). The curve equation becomes

\[
\boxed{6S r^3=T(x^3-x),\qquad
x\ge103,\quad x+1<2^{192S}.}
\tag{3}
\]

For each positive S, the full possible list is
\(T=162S+1,\ldots,229S-1\). This finite list follows from the
gap, rather than an empirical restriction on T.

## 2. The approximation constant and rational exceptions

Define

\[
\alpha=\left(\frac{T}{6S}\right)^{1/3}.
\]

Equation (3) gives \(\alpha>r/x>3\). Also

\[
\begin{aligned}
0<\alpha-\frac rx
&=\frac{\alpha^3-(r/x)^3}
{\alpha^2+\alpha r/x+(r/x)^2}\\
&<\frac{229}{162x^2}<\frac{3}{2x^2}.
\end{aligned}
\tag{4}
\]

Here \(\alpha^3-(r/x)^3=\alpha^3/x^2\), the denominator
is greater than 27, and \(\alpha^3<229/6\).

If \(\alpha=u/v\) is rational in lowest terms, then \(v^3\mid6S\).
The positive difference in (4) is at least \(1/(vx)\), so

\[
x<3v/2.
\tag{5}
\]

For \(S\le12\), one has \(v^3\le72\), hence \(v\le4\).
Equation (5) would give \(x<6\), contradicting \(x\ge103\).
Every rational cube-root case is therefore excluded uniformly.

We may now take \(\alpha\) irrational. Write

\[
g=\gcd(r,x),\qquad r=gp,\qquad x=gq,
\qquad \gcd(p,q)=1.
\]

Then (4) implies

\[
0<\alpha-\frac pq<\frac{3}{2q^2},\qquad
1\le q<2^{192S}.
\tag{6}
\]

The coefficient 3/2 does not justify restricting p/q to convergents
alone. The next elementary lemma includes all additional cases.

## 3. A complete approximation lemma with at most 65 pairs per step

Let \(P_m/Q_m\) be the regular continued-fraction convergents of
the irrational \(\alpha\). We use \(P_{-1}=1,Q_{-1}=0\).
Since \(3<\alpha<(229/6)^{1/3}<7/2\), its first partial
quotient is 3 and its second is at least 2. Thus the positive
denominators strictly increase from \(Q_0=1\).

Choose the unique m with

\[
Q_m\le q<Q_{m+1}.
\tag{7}
\]

The determinant of consecutive convergents is \(\pm1\), so there
are unique integers a,b such that

\[
p=aP_m+bP_{m-1},\qquad q=aQ_m+bQ_{m-1}.
\tag{8}
\]

We will prove that every fraction satisfying (6) occurs among

\[
\boxed{b\in\{-2,-1,0,1,2\},\qquad
a\in\{-1,0,1,2,3,4\}
\ \cup\ \{b a_{m+1}+c:-3\le c\le3\}.}
\tag{9}
\]

Here \(a_{m+1}\) is the next continued-fraction partial quotient.
There are at most \(5(6+7)=65\) proposed integer pairs at each
step, regardless of how large \(a_{m+1}\) is.

### 3.1 The standard convergent estimates used

The complete quotient \(\alpha_{m+1}>a_{m+1}\) gives the exact
identity

\[
\alpha=\frac{P_m\alpha_{m+1}+P_{m-1}}
{Q_m\alpha_{m+1}+Q_{m-1}}.
\]

Taking determinants yields

\[
|Q_m\alpha-P_m|
=\frac1{Q_m\alpha_{m+1}+Q_{m-1}}
<\frac1{Q_{m+1}}.
\tag{10}
\]

Thus no external classification theorem about good rational
approximations is needed for the finite set (9).

### 3.2 Bounding b

Equations (8), (10), and the determinant identity give

\[
\begin{aligned}
|b|&=|pQ_m-qP_m|\\
&<\frac{3Q_m}{2q}+\frac q{Q_{m+1}}
<\frac52.
\end{aligned}
\]

Since b is an integer, \(|b|\le2\).

### 3.3 The smaller-denominator half

Suppose \(q<Q_{m+1}/2\). If \(b\ne0\), the preceding bound
implies

\[
1\le|b|<\frac{3Q_m}{2q}+\frac12,
\qquad q<3Q_m.
\]

As \(0\le Q_{m-1}\le Q_m\), equation (8) and (7) now give
\(-1\le a<5\), hence \(-1\le a\le4\).
If \(b=0\), the fraction in (8) is reduced only when \(a=1\),
which is already in this list.

### 3.4 The larger-denominator half

Suppose \(q\ge Q_{m+1}/2\). Set \(c=a-b a_{m+1}\).
The recurrence for convergents rewrites (8) as

\[
p=bP_{m+1}+cP_m,\qquad q=bQ_{m+1}+cQ_m.
\]

Therefore

\[
|c|=|pQ_{m+1}-qP_{m+1}|
<\frac{3Q_{m+1}}{2q}+\frac q{Q_{m+2}}<4.
\]

Thus \(-3\le c\le3\), establishing the second set in (9).
Both denominator halves have been covered, proving completeness.

## 4. Recovering the common factor exactly

For a reduced positive p/q from (9), substitute \(r=gp,x=gq\)
in (3) and cancel the positive factor g:

\[
g^2\bigl(Tq^3-6Sp^3\bigr)=Tq.
\]

Consequently every solution must have

\[
\boxed{D=Tq^3-6Sp^3>0,\qquad D\mid Tq,
\qquad g^2=\frac{Tq}{D}.}
\tag{11}
\]

The last quotient must be an integer square. When it is, there is
exactly one positive g, and then

\[
n=gq+1,\qquad r=gp.
\]

All tests in (11) use integers. Afterwards we impose \(n\ge104\),
\(n<2^{192S}\), \(3n<r<10n/3\), and \(S\mid n-2\).
These are necessary conditions from (1). The exact value of the
full gcd need not be reconstructed to exclude a candidate: this
procedure deliberately includes any extra candidates permitted by
the weaker necessary conditions.

## 5. Certifying every continued-fraction prefix without rounding

The generator encloses the positive cube root in a dyadic interval
using an exact integer cube-root computation, refining its precision
until a continued-fraction prefix reaches denominator
\(Q_M\ge2^{192S}\). This precision choice affects only generation,
not the correctness criterion for the certificate.

The independent verifier reconstructs the convergents from the
recorded partial quotients and checks that

\[
\alpha\text{ lies strictly between }
\frac{P_M}{Q_M}
\quad\text{and}\quad
\frac{P_M+P_{M-1}}{Q_M+Q_{M-1}}.
\tag{12}
\]

It checks (12) by comparing the cubes of these positive rational
numbers with \(T/(6S)\), using only integer multiplication.
These are the two endpoints of the cylinder of real numbers with
the recorded continued-fraction prefix. To see this directly, let
the next complete quotient range over all real values greater than
one in

\[
\frac{P_M u+P_{M-1}}{Q_M u+Q_{M-1}}.
\]

Its endpoint values are exactly (12), and its derivative has constant
nonzero sign by the determinant identity. Thus (12) certifies the
entire prefix, not only its last rational approximation.

The verifier also checks that all partial quotients after the first
are positive, \(Q_{M-1}<2^{192S}\le Q_M\), and the list of (S,T)
contains every pair in (2), without omissions or duplicates. It then
reconstructs every candidate in (9) independently and applies (11).

## 6. The complete finite result

The full number of curves is

\[
\sum_{S=1}^{12}(67S-1)=5214.
\]

Exactly one has a rational cube root: \(S=9,T=2000\), with
\(\alpha=10/3\). Section 2 excludes it. The other 5213 curves
have certified continued-fraction prefixes containing a total of
4,877,566 partial quotients. All required prefixes reach their
proved denominator bound.

| S | Curves | Certified partial quotients | Reduced fractions checked | Surviving points |
|---:|---:|---:|---:|---:|
| 1 | 66 | 7412 | 38185 | 0 |
| 2 | 133 | 29999 | 155542 | 0 |
| 3 | 200 | 67610 | 350369 | 0 |
| 4 | 267 | 119657 | 623155 | 0 |
| 5 | 334 | 188373 | 975346 | 0 |
| 6 | 401 | 269886 | 1404511 | 0 |
| 7 | 468 | 367130 | 1913847 | 0 |
| 8 | 535 | 480002 | 2501278 | 0 |
| 9 | 602 | 607177 | 3160468 | 0 |
| 10 | 669 | 751641 | 3910137 | 0 |
| 11 | 736 | 907633 | 4728751 | 0 |
| 12 | 803 | 1081046 | 5632741 | 0 |
| Total | **5214** | **4877566** | **25394330** | **0** |

Thus no point can satisfy all the necessary conditions in (1)-(3),
proving (0). The actual gcd need not be recomputed, because even the
larger set specified by the necessary conditions is empty.

The complete prefixes are stored, without omitted coefficients,
in `v9_cf_certificates/S01.json` through `S12.json`. Each is a
losslessly compressed text certificate with explicit hashes and a
documented base64/zlib encoding. The checker uses only the Python
standard library. From the parent directory, run

    python3 v9_gcd_defect_cf_checks.py verify

To regenerate every prefix, run

    python3 v9_gcd_defect_cf_checks.py generate

The verification output is `v9_gcd_defect_cf_verification.json`.
The actual full verification completed with exit code 0 on 2026-11-05.

### A different full reproduction

`v9_gcd_defect_cf_reproduction.py` does not read the saved prefixes.
It generates exact dyadic enclosures independently for every curve,
then enumerates the union in (9) at every stage. The main verifier
instead authenticates each saved prefix by its cylinder and partitions
the two denominator halves in Sections 3.3-3.4. Consequently the
reproduction includes some unnecessary extra fractions. It checked
30,534,156 fractions, again with no surviving point, and reproduced
the same 5214 curves and 4,877,566 partial quotients.

The delivered reproduction source is byte-for-byte identical to the
source actually executed under its original working filename;
the SHA-256 and successful execution are recorded in
`v9_gcd_defect_cf_reproduction_verification.json`. Reproduce it with

    python3 v9_gcd_defect_cf_reproduction.py 12

The wider initial enumeration, the separate denominator-half
enumeration, and the exact prefix-cylinder checks all agree.

## 7. Consequences for prime-power families

The independent general formula in `v9_gcd_structure.md` says that
for \(n=wp^a+2\), \(p\nmid w\), and \(p^a>4w\),

\[
S\mid c_w p^{v_p(D_w)},\quad
c_w=w/\gcd(w,6),\quad
D_w=\binom{6w}{2w}/\gcd\!\left(\binom{6w}{2w},6\right).
\]

For w=1, \(c_1=1,D_1=5\). Every remaining n>=104 therefore
has \(S\in\{1,5\}\), contradicting (0). For w=2 and an odd
prime base, \(c_2=1,D_2=165=3\cdot5\cdot11\), so
\(S\in\{1,3,5,11\}\), again impossible. When w=2 and p=2,
absorb the extra factor 2 into the exponent to use w=1.

This reproves the whole families \(i=P^a+2\) and \(i=2P^a+2\)
without using their separate finite noncube certificates. Its inputs
are the common-divisor and gap theorems, the general v8 height bound,
the v9 exact defect formula, and the complete CF computation above.

More generally, for \(p>6w\), the same formula gives
\(S\mid w/\gcd(w,6)\). Therefore every solution in that range
must satisfy

\[
\boxed{w/\gcd(w,6)\ge13.}
\]

## 8. Audit and limits

The gcd-structure reviewer independently audited Sections 1-5 and
the entire generation/verification implementation, and reported PASS.
The audit covered both halves of the approximation lemma, noncoprime
original r and x, rational cube roots, cylinder authentication of
the complete prefix, and recovery of g. This is independent AI review,
not external peer review.

No Lean formalization of the continued-fraction completeness proof
or this complete curve computation is claimed. The separately executed
v9 Lean source checks the 2592 noncube records in the cofactor-two proof.

This result does not bound S from above for arbitrary n. Larger
defects, other offsets, and other values of ell remain unresolved.
