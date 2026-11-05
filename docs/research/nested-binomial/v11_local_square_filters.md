# Explicit local square filters for the recovered divisor

## Scope and results

The original equation remains
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
This note concerns \(\ell=1,\ j=i-3\). Put
\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},
\quad r=\min(k,A-k).
\]
The established branch reductions give n>=104 and
\[
3n<r<10n/3,\qquad A\mid r(X+r^2).
\tag{1}
\]
The v10 local recovery theorem says that, for p|A, if
\(\alpha=v_p(A),x=v_p(X),e=v_p(r)\) and 3e<alpha, then
\[
x=2e,\qquad
(r/p^e)^2\equiv-X/p^{2e}\pmod{p^{\alpha-3e}}.
\tag{2}
\]
Thus a nonsquare leading unit restores the entire p-part of A in
r cubed. This note supplies a formula for that leading unit,
an exact efficient way to compute every higher unit needed by CRT,
and a uniform family of new exclusions.

### Main unit formula

Let
\[
n=wp^a+2,\quad p\text{ odd prime},\quad p\nmid w,
\quad q=p^a>4w,
\]
and put
\[
B_w=\binom{6w}{2w},\quad \beta=v_p(B_w),\quad
U_w=B_w/p^\beta.
\]
Then the following exact leading-unit formula holds, without
assuming the original binomial equation has a solution:
\[
\boxed{
v_p(X)=a-\beta,\qquad
\frac{X}{p^{a-\beta}}\equiv-\frac{2w}{U_w}\pmod p.
}
\tag{3}
\]
In particular, the square test for any critical odd prime is
\[
\boxed{
\left(\frac{-X/p^{v_p(X)}}p\right)
=\left(\frac{2wU_w}p\right).
}
\tag{4}
\]
The right side depends on w and p, but not on the exponent a.
Every inverse in these formulas is of a p-unit.

### New uniform exclusion

If
\[
4w<p<6w,
\quad
\left(\frac{\binom{2w-1}{p-4w-1}}p\right)=-1,
\tag{5}
\]
then the original branch has no solution with
\[
\boxed{n=wp^{3t+1}+2\qquad(t\ge0).}
\tag{6}
\]
The cofactor w is not bounded. One explicit consequence is
\[
\boxed{
n=\frac{p+1}{6}\,p^{3t+1}+2,
\quad p\equiv17\text{ or }23\pmod{24}\text{ prime},
\quad t\ge0
\quad\Longrightarrow\quad\text{no solution}.
}
\tag{7}
\]
For example this excludes every n=19*113^(3t+1)+2 and every
n=23*137^(3t+1)+2. These cofactors exceed the v10 small-cofactor
condition. Other constant offsets give further families through
the same theorem, as described in Section 5.

The original four-variable problem and the unrestricted mixed-prime
branch remain unresolved.

## 1. Stripping powers of a prime from a binomial coefficient

For a nonzero rational number z define its p-unit part by
\(z^\circ=z/p^{v_p(z)}\). Products and quotients of unit parts
remain multiplicative. We use this notation only when the
denominators of the resulting units are invertible modulo p.

For nonnegative integers M>=R, splitting the factorials into
multiples and nonmultiples of p gives
\[
\binom{pM}{pR}
=\binom MR\,
\frac{\prod_{1\le h\le pM,\ p\nmid h}h}
{\prod_{1\le h\le pR,\ p\nmid h}h
 \prod_{1\le h\le p(M-R),\ p\nmid h}h}.
\tag{8}
\]
The extra factor is a p-unit. Every full p-block of its numerator
or denominators has residue (p-1)!=-1 modulo p; their numbers
are M, R and M-R. Therefore this extra factor is 1 modulo p.
Iterating (8) proves
\[
v_p\binom{qM}{qR}=v_p\binom MR,
\qquad\binom{qM}{qR}^{\circ}\equiv\binom MR^{\circ}\pmod p
\tag{9}
\]
for every q=p^a.

## 2. Derivation of the exponent-independent unit

With n=wq+2, write
\[
M=qw^2+4w,\qquad R=6w.
\]
Then
\[
X=\binom{qM+4}{qR+3}.
\]
Its ratio to \(\binom{qM}{qR}\) is exactly
\[
\frac{(qM+1)(qM+2)(qM+3)(qM+4)}
{(qR+1)(qR+2)(qR+3)(q(M-R)+1)}.
\tag{10}
\]
Since q>4w>=4, every nonzero integer h<=4 has v_p(h)<a.
The p-adic valuation and leading unit of qZ+h agree with those
of h. For odd p, (10) has valuation 0 and unit 4 modulo p.
This remains valid at p=3: the factors with h=3 cancel in
valuation and in their stripped units.

The numerator product for \(\binom MR\) has the centered form
\[
\binom MR
=\frac{\prod_{s=-2w+1}^{4w}(qw^2+s)}{(6w)!}.
\tag{11}
\]
The s=0 term has valuation a and unit w^2. All other offsets
s have 0<|s|<=4w<q, so their valuations and leading units
agree with those of s. There are 2w-1 negative offsets. Hence
\[
\frac{\prod_{s\ne0}s}{(6w)!}
=-\frac{(2w-1)!(4w)!}{(6w)!}
=-\frac1{2wB_w}.
\tag{12}
\]
Because p is odd and does not divide w, equations (11)-(12) give
\[
v_p\binom MR=a-\beta,
\qquad
\binom MR^{\circ}\equiv-\frac{w}{2U_w}\pmod p.
\]
Combining this with (9)-(10) proves (3). Nonnegativity of a-beta
also follows from this valuation calculation; alternatively, the
floor-sum bound p^beta<=6w<2q excludes beta>a for odd p.

Multiplicativity of the quadratic character and the equality of
the characters of a unit and its inverse give (4).

### Consequence for the recovered divisor

If the right side of (4) is -1, no solution of (1) can have
3v_p(r)<v_p(A). Indeed, (2) would require exactly that nonsquare
unit to be a square modulo p. Thus
\[
\boxed{
\left(\frac{2wU_w}p\right)=-1
\quad\Longrightarrow\quad p^{v_p(A)}\mid r^3.
}
\tag{13}
\]
This holds for all exponents a satisfying q>4w. If x is odd,
the same conclusion already follows from parity; formula (13)
also handles the possible even-x cancellation cases.

Equivalently, this prime contributes no factor to the square-filtered
defect E_sq of the v10 note. The conclusion is uniform in a and
does not extrapolate from a finite exponent test.

## 3. Exact higher-unit computation for every critical prime

Formula (3) is particularly short in the dominant-power range.
For an arbitrary candidate n and any prime p, every unit needed
for the v10 CRT conditions can still be computed without forming X.

Fix a precision d>=1 and put P=p^d. Define
\[
F_p(N)=N!/p^{v_p(N!)},\qquad
U_p(N)=\prod_{1\le h\le N,\ p\nmid h}h.
\]
The exact factorial identity gives
\[
F_p(N)=\prod_{j\ge0}U_p(\lfloor N/p^j\rfloor).
\tag{14}
\]
All but finitely many terms are 1. A complete block of P integers
has the same unit product as the invertible residues modulo P.
That product is
\[
\varepsilon(P)=
\begin{cases}
-1\pmod P,&p\text{ odd},\\
1\pmod2,&P=2,\\
-1\pmod4,&P=4,\\
1\pmod P,&p=2,\ d\ge3.
\end{cases}
\tag{15}
\]
For odd p, pair every invertible residue with its inverse; the
only self-inverse residues are 1 and -1. For powers of 2, the same
pairing and the four self-inverse residues when d>=3 give (15).
Consequently
\[
U_p(N)\equiv
\varepsilon(P)^{\lfloor N/P\rfloor}
\prod_{\substack{1\le h\le N\bmod P\\p\nmid h}}h
\pmod P.
\tag{16}
\]
Once the partial products for one block are available, (14)-(16)
take only logarithmically many stages in N.

For N=n^2, K=6n-9, D=N-K, compute
\[
x=v_p(N!)-v_p(K!)-v_p(D!)
\]
by floor sums. Then
\[
\boxed{
X/p^x\equiv F_p(N)F_p(K)^{-1}F_p(D)^{-1}\pmod{p^d}.
}
\tag{17}
\]
All three factorial units are invertible. This is an exact
computation; it uses neither large-binomial approximation nor
probabilistic primality testing.

At precision 1, writing N,K,D in base p gives the useful independent
digit formula
\[
\boxed{
X/p^x\equiv(-1)^x
\prod_{h\ge0}\frac{N_h!}{K_h!D_h!}\pmod p.
}
\tag{18}
\]
The exponent of -1 is the difference of the three factorial
valuations. Each digit factorial is a unit.

For odd p, a critical unit is a square modulo p^d exactly when
it is a square modulo p. For p=2, only precision min(d,3) is
needed to decide square existence: an odd square is 1 modulo 8,
with the usual reductions at d=1,2. Higher precision from (17)
can then supply the actual root classes used by CRT.

### Proof-producing CRT records

For a candidate n, a local record contains p, alpha, x, d and
the normalized unit (17). Its independent verifier reconstructs
x and the unit using the factorial formulas. The record may
also list roots of the v10 congruence, but root enumeration is
not required. Nonsquare critical primes are removed from
E before the global CRT product is formed. With the resulting
divisor B_sq=A/E_sq and F=c_3(B_sq), write r=Fu. At every
remaining critical prime, the complete alternatives are
\[
u=0\pmod{p^d}\quad\text{or}\quad
u^2=-\lambda_p\pmod{p^d},
\]
where
\[
\lambda_p=(X/p^x)(F/p^{x/2})^{-2}\pmod{p^d}.
\]
The short interval is still u^3<229E_sq. The v10 transfer gives
H=E_sq/gcd(E_sq,u)>=13; the independent v11 calculation in
`v11_effective_defect_cf.md` improves this to H>=14. These exact
conditions can reject an entire candidate without constructing
X or enumerating an interval proportional to n.

For an alternative to listing roots, the theorem in
`v11_simultaneous_square_interval.md` applies CRT directly to
the squared value. For each unitary zero support Z it constructs
a unique residue R and tests at most four possible integers
R+mH, and at most one when the relevant scale is at least 512.
The factorial-unit computation here supplies its local residues.
No claim is made here that all remaining CRT intersections are
empty. The uniform exclusion in Section 4 and the following
n=6860 certificate use only the earlier threshold 13.

### A short local certificate for n=6860

This index required a separate logarithmic comparison in v10.
The square test gives an independent shorter exclusion. Its
factorization and valuations are
\[
A=2^2 3^2\cdot5\cdot7^3\cdot19^3\cdot127,
\qquad
(v_2X,v_3X,v_5X,v_7X,v_{19}X,v_{127}X)
=(13,0,5,6,6,0).
\]
Consequently the recovered defect before square filtering is
E=3^2\cdot127=1143. At the prime 127, the base-127 digits of
N=n^2, K=6n-9 and D=N-K, written from the least significant
digit to the most significant digit, are
\[
N=(4,89,123,22),\quad K=(3,70,2,0),\quad D=(1,19,121,22).
\]
The addition K+D=N has no carries, so x=0. Formula (18) gives
\[
X\equiv\binom43\binom{89}{70}\binom{123}{2}\binom{22}0
\equiv4\cdot112\cdot10\cdot1\equiv35\pmod{127}.
\]
But 92^63=-1 modulo 127. Thus -X=92 modulo 127 is a nonresidue,
and the full 127-part of A is restored to r cubed. At 3 the unit
-X is a square, leaving
\[
\boxed{E_{\rm sq}=9<13.}
\]
This contradicts the existing continued-fraction threshold for
every putative solution with n=6860. The calculation does not
need the v10 logarithmic-gap estimate or the v11 improvement of
that threshold.

## 4. A quadratic-character criterion in the band 4w<p<6w

Assume now 4w<p<6w. Then beta=1: the numerator factorial (6w)!
contains exactly one p and the two denominator factorials contain
none. Put t=p-4w. It is odd and 1<=t<2w.

Wilson's theorem and reflection below p give
\[
U_w=\frac{\binom{6w}{2w}}p
\equiv\frac1{t\binom{2w}{t}}\pmod p.
\tag{19}
\]
Indeed (6w)!/p=-(6w-p)! modulo p, and
(4w)!=(p-t)!=(-1)^t/(t-1)! modulo p. Since t is odd,
their two signs cancel.

Substitute (19) into (3) and use
\(t\binom{2w}{t}=2w\binom{2w-1}{t-1}\). We obtain
\[
\boxed{
-\frac{X}{p^{a-1}}
\equiv(2w)^2\binom{2w-1}{p-4w-1}\pmod p.
}
\tag{20}
\]
Thus the nonsquare condition (5) gives p^a|r^3 for every a>=1.

Suppose a=3s+1. Then p^(s+1)|r, hence p^(a+2)|r^3.
The established common divisor
\[
Q=\frac{n(n-1)\gcd(n-2,6)}6
\]
also divides r^3 and is coprime to p. Therefore
\[
p^{a+2}Q\le r^3<1000n^3/27.
\]
Using Q>=n(n-1)/6 and n^2/(n-1)<n+2 yields
\[
\boxed{p^2<\frac{2000}{9}\left(w+\frac4{p^a}\right).}
\tag{21}
\]
Since w<p/4 and p^a>=p, this implies
\[
9p^3-500p^2-8000<0.
\tag{22}
\]
For p=59+h, h>=0, the left side is
\[
9h^3+1093h^2+34987h+99911>0.
\]
Thus p<59. Every remaining prime p<=53 has w<=13. If w<=12,
the complete v10 fixed-cofactor theorem already excludes the
family for every exponent. The only possibility with w=13 is
p=53. In that case p-4w-1=0, so the binomial in (5) equals 1,
contradicting its assumed nonsquareness. This proves (6).

The use of the v10 small-cofactor theorem handles only these
small boundary parameters. The cofactor w and exponent in (6)
are otherwise unrestricted.

## 5. Fixed-offset families with a constant quadratic character

Let c be a positive odd integer not divisible by 3. Suppose p is
a prime with p>2c and p+c divisible by 6, and put w=(p+c)/6.
Then 4w<p<6w and p=6w-c. Symmetry in (20) gives
\[
\binom{2w-1}{p-4w-1}=\binom{2w-1}{c}.
\]
Its residue is the fixed rational number
\[
\boxed{
R_c=\frac{\prod_{h=0}^{c-1}(c-3-3h)}{3^c c!}\pmod p.
}
\tag{23}
\]
Every numerator factor has absolute value at most 2c<p, and the
denominator is also a p-unit. Thus R_c is nonzero modulo p.
Whenever its quadratic character is -1, theorem (6) excludes
\[
n=\frac{p+c}{6}p^{3t+1}+2\quad(t\ge0).
\tag{24}
\]
This is a systematic family of uniform obstructions, one for
each admissible constant c.

| c | R_c | Equivalent integer quadratic character |
|---:|---|---|
|1| -2/3 | -6 |
|5| 14/729 | 14 |
|7| -88/19683 | -66 |
|11| 3952/14348907 | 741 |

For c=1, p=5 modulo 6. Gauss's lemma gives that -6 is a
quadratic nonresidue for p=17 or 23 modulo 24. To check the signs
explicitly, 2 is a residue in both classes; 3 is a nonresidue
in the first and a residue in the second, while -1 has the
opposite two signs. The formula for 3 follows by counting
integers in p/6<h<p/3 in Gauss's lemma; the one for 2 counts
p/4<h<=(p-1)/2. This proves (7).

For c=5, the condition is that 14 be a nonresidue. For example
p=241 gives w=41, and 14^120=-1 modulo 241. Hence every
n=41*241^(3t+1)+2 is excluded as well. The table's other entries
are likewise exact constant-character criteria, not finite
exponent observations.

## 6. Verification boundary

The companion checker validates the unit theorem by comparing
the centered-product expression against independent factorial-unit
and base-p digit computations. It also compares the general
higher-precision algorithm against direct stripped products and
exact binomial coefficients on structured finite inputs, including
p=2 and p=3. The finite input ranges are recorded explicitly;
they check the uniform proofs rather than establish them by
extrapolation.

The new exclusion (6) uses only the previously proved branch gap,
common divisor, local recovery, and the complete v10 small-cofactor
theorem. Precisely, the inputs are the gap in
`v6_offset_composite.md`, the common divisor in
`v6_common_divisor.md` and `v9_gcd_structure.md`, the recovery and
continued-fraction transfer in `v10_valuation_recovery.md`, and
the complete w<=12 subcase of `v10_small_cofactors.md`.
The elementary Legendre-symbol and factorial identities
are proved above. No new external classification theorem, no
probabilistic primality assumption, and no whole-equation
solution is claimed. Formal verification status and independent
audit records are stated below.

The companion checker executed successfully. It compared 9,382
instances of (3) with independent unit and digit computations,
including 424 instances with beta>1 and 103 at p=3. Of these,
123 were also compared with exact binomial coefficients.
The general higher-unit algorithm passed 963 direct-product and
exact-binomial comparisons; (20) passed 5,118 band instances;
and (23) passed 326 fixed-offset comparisons. These finite
checks support the written proofs and are not their substitutes.
The n=6860 certificate was checked independently by its base-127
digits, the four small binomial residues, and Euler's criterion.
The unbounded v11 theorems in this note are not Lean-formalized.

On 2026-11-05 the root reviewer and the mixed-structure reviewer
independently audited the full written proof and reported PASS.
They checked the p=3 boundary, signs and inverses in the unit
formulas, higher-precision recursion, n=6860 certificate, exact
large-prime bound, finite boundary, and fixed-offset characters.
The mixed-structure reviewer also reran the checker with output
redirected to a separate directory and reproduced all PASS
counts without changing these files. These are independent AI
mathematical and computational audits, not external peer review.
