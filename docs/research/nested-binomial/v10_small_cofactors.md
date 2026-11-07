# Complete exclusion of every cofactor w/gcd(w,6) at most twelve

## Theorem and scope

The original equation is the squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

**Theorem.** There is no solution in any of the families

\[
\boxed{\ell=1,\quad j=i-3,\quad i=wp^a+2,
\quad p\text{ prime},\ a\ge1,\quad
\frac{w}{\gcd(w,6)}\le12.}
\tag{1}
\]

The prescribed cofactor w need not be coprime to p. Both outer
branches are included. The complete set of such cofactors is

\[
\boxed{
\begin{gathered}
1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,21,22,24,\\
27,30,33,36,42,48,54,60,66,72.
\end{gathered}}
\tag{2}
\]

Thus all thirty fixed-cofactor families are excluded for every
prime base and every positive exponent. The cases w=1,2,3 recover
previous results; the other twenty-seven cofactors are added here.
Some individual indices admit more than one parametrization, so
these are not asserted to be disjoint sets.

The proof uses the v10 local recovery of a divisor of r^3, the v9
complete small-defect continued-fraction certificates, and a new
finite remainder of 983 parameter records, representing 955 distinct
first indices. The finite domain is derived from a valuation theorem;
no upper cutoff for i is chosen empirically.

This does not solve the whole four-variable equation.

## 1. Established input

Throughout this note put

\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),\quad L=\binom Ar.
\]

Binomial symmetry gives L=X+k^2. The prior endpoint and small-index
results leave only n>=104. The v5-v6 gap theorems give

\[
3n<r<10n/3,
\tag{3}
\]

and, for n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{4}
\]

With G=gcd(A,X), the prior common-divisor theorem gives G|r^3.
The stronger divisor in `v9_gcd_structure.md` gives

\[
\frac{A}{G}\mid\frac{n-2}{\gcd(n-2,6)}.
\tag{5}
\]

The height proof in `v8_gcd_defect_height.md` and the exact finite
continued-fraction proof in `v9_gcd_defect_continued_fractions.md`
will be used with a larger divisor of A and r^3. Section 3 below
spells out why the same complete certificates apply.

## 2. Recovering prime factors missing from the common gcd

For a prime p|A write

\[
\alpha=v_p(A),\qquad x=v_p(X),\qquad e=v_p(r).
\]

The binomial identity k*C(A,k)=A*C(A-1,k-1), together with the
original equation, implies

\[
\boxed{A\mid k(X+k^2).}
\tag{6}
\]

Suppose 3e<alpha. Then e<alpha, so both k=r and k=A-r have
v_p(k)=e. The two terms kX and k^3 in (6) have valuations e+x
and 3e. If they were unequal, the valuation of their sum would be
their minimum, at most 3e<alpha. That contradicts (6). Hence

\[
\boxed{3e<\alpha\quad\Longrightarrow\quad x=2e.}
\tag{7}
\]

In particular a prime-power deficiency can remain only when x is
even and 3x<2alpha. Define

\[
d_p=\begin{cases}
\alpha-3x/2,&x\text{ even and }3x<2\alpha,\\
0,&\text{otherwise},
\end{cases}
\]

\[
B=\prod_{p\mid A}p^{\alpha-d_p},\qquad
S_*=\frac AB,\qquad
R=\prod_{p\mid A}p^{\lceil(\alpha-d_p)/3\rceil}.
\tag{8}
\]

The alternatives in (7) prove

\[
\boxed{B\mid A,\qquad B\mid r^3,\qquad R\mid r.}
\tag{9}
\]

Moreover G|B. At a prime where d_p=0 this is immediate. Otherwise
the exponent of B is 3x/2, which is at least x=min(alpha,x).
Consequently

\[
\boxed{G\mid B,\qquad S_*\mid A/G,
\qquad S_*\mid\frac{n-2}{\gcd(n-2,6)}.}
\tag{10}
\]

This local recovery is a consequence of the original equality,
not an assertion that the ordinary gcd itself has become larger.

## 3. The existing complete continued-fraction result applies to S_*

Set T=r^3/B. By (9) this is a positive integer, and

\[
T=\frac{S_*r^3}{A}
=\frac{6S_*r^3}{n(n-1)(n-2)}.
\]

The proof in `v8_gcd_defect_height.md` uses only this integrality,
the gap (3)-(4), and S_*>=1. It therefore gives

\[
\log n<128S_*,\qquad n<2^{192S_*}.
\tag{11}
\]

The same broad gap gives 162S_*<T<229S_*. Thus, setting y=n-1,

\[
6S_*r^3=T(y^3-y),\qquad y\ge103,\qquad y+1<2^{192S_*}.
\tag{12}
\]

Together with S_*|n-2 from (10), these are exactly the necessary
conditions whose entire S=1,...,12 domain was excluded by the v9
continued-fraction certificates. The proof does not require B|X;
it requires B|A, B|r^3 and the resulting integrality and divisor
conditions. Therefore every solution must satisfy

\[
\boxed{S_*\ge13.}
\tag{13}
\]

No new continued-fraction range or unverified extrapolation is used.

## 4. Only finitely many exponents can retain a defect

First normalize the parametrization. If p^h exactly divides a
prescribed w, write w=p^h*w0. Then n=w0*p^(a+h)+2 and p does
not divide w0. The reduced cofactor c(u)=u/gcd(u,6) cannot decrease
when u is multiplied by a prime. Indeed,

\[
\frac{c(pu)}{c(u)}
=\frac{p\gcd(u,6)}{\gcd(pu,6)}\ge1.
\]

So c(w0)<=c(w)<=12, and w0 is again in (2). It suffices to prove
the theorem for p not dividing w.

Put q=p^a and define

\[
D_w=\frac{\binom{6w}{2w}}{\gcd(\binom{6w}{2w},6)},
\qquad c_w=\frac{w}{\gcd(w,6)},\qquad b=v_p(D_w).
\]

If q<=4w, the parameter is already in a finite set, with
n<=4w^2+2 and p<=4w. Suppose q>4w. The exact v9 formulas give

\[
v_p(A)=\alpha=a-\mathbf1_{p=3},\qquad
v_p(A/G)=b,\qquad A/G\mid c_wp^b.
\tag{14}
\]

If b=0, then (10) gives S_*|c_w, contradicting c_w<=12 and (13).
If b>0, the equality v_p(A/G)=b implies

\[
x=v_p(X)=\alpha-b.
\]

The p-free part of S_* still divides c_w. Hence (13) requires a
positive p-defect, and Section 2 forces x even and 3x<2alpha.
Equivalently,

\[
\boxed{
\alpha\in\{b,b+2,\ldots,3b-2\},\qquad
a=\alpha+\mathbf1_{p=3},\qquad b\ge1.
}
\tag{15}
\]

Also p divides D_w, so p<=6w. Thus the entire possible domain is
contained in the following explicitly derived finite set:

- w is one of the thirty numbers in (2);
- p<=6w is prime and does not divide w;
- either p^a<=4w, or the exponent satisfies (15);
- n=wp^a+2>=104.

For example, if b=1 and p!=3, only a=1 can retain a deficiency.
All exponents a>=2 are excluded at once, without checking their
numerical sizes.

### A short example: the whole cofactor-four family

For w=4 one has

\[
c_4=2,\qquad D_4=3\cdot11\cdot17\cdot19\cdot23.
\]

The base p=2 reduces to the already excluded w=1 family. For odd p,
if q<=16 then n<=66, already excluded by the small-index theorem.
If q>16, (13) and c4=2 force p to be one of the five displayed
prime divisors of D4. At p=3 the only exponent allowed by (15)
would be a=2, giving q=9 and contradicting q>16. At every other
displayed prime, b=1 and (15) forces a=1, so n=4p+2<=94.
This too contradicts n>=104. Thus the entire w=4 family follows
without adding any new finite arithmetic certificate beyond the
shared v9 small-defect result.

### A uniform polynomial upper bound

The Legendre floor sum for C(6w,2w) has summands zero or one, so
p^v_p(C(6w,2w))<=6w. In the q>4w remainder, (15) gives:

| Prime | Bound on p^b | Bound on q |
|---|---|---|
| p>=5 | p^b<=6w | q<=216w^3/25 |
| p=2 | 2^b<=3w | q<=27w^3/4 |
| p=3 | 3^b<=2w | q<=8w^3/3 |

The factor p^-2 in the first two rows comes from a<=3b-2.
For p=3, a<=3b-1 gives the factor 3^-1. The largest of these
three coefficients is 216/25. The q<=4w case is smaller as well.
Consequently every hypothetical solution with c_w<=12 would obey

\[
\boxed{n\le\frac{216}{25}w^4+2<9w^4+2.}
\tag{16}
\]

Normalization only decreases w, so this also holds for a prescribed
cofactor sharing p. The checker uses the sharper prime-and-exponent
domain above, not a scan of all integers in (16).

## 5. Complete finite certificates

The exact domain in Section 4 contains 983 parameter records,
representing 955 distinct n. The largest is

\[
(w,p,a,n)=(66,7,7,54353840).
\]

For every distinct n, `v10_small_cofactors_certificates.json`
records the complete prime factorization of A, all valuations of X
at those primes, the forced exponents in R, S_*, and the first
multiple of R strictly above 3n:

\[
r_0=\left(\left\lfloor\frac{3n}{R}\right\rfloor+1\right)R.
\tag{17}
\]

No factorization of the enormous binomial coefficient X is needed.
Its relevant valuations are computed by Legendre's formula and
independently verified by counting carries in base p.

Every parameter record is excluded in one of three ways:

| Exclusion | Parameter records | Distinct n |
|---|---:|---:|
| S_*<=12, contradicting (13) | 480 | 453 |
| 3r0>=10n, contradicting (3) and R|r | 502 | 501 |
| The logarithmic gap at n=6860 | 1 | 1 |
| Total | **983** | **955** |

The second line does not enumerate r: r0 is the first possible
multiple, so if it is already beyond the strict upper bound, every
larger multiple is also impossible.

For instance, n=289 has R=204. The first multiple exceeding
3n=867 is 1020, whereas 10n/3<964. This removes the case even
though R itself is smaller than the upper bound.

### The only case needing the logarithmic gap

The final record is

\[
(w,p,a,n)=(54,127,1,6860).
\]

Its exact data are

\[
A=2^2 3^2 5\,7^3 19^3 127,
\]

\[
\begin{array}{c|rrrrrr}
p&2&3&5&7&19&127\\ \hline
v_p(X)&13&0&5&6&6&0
\end{array}
\]

and hence R=2*5*7*19=1330 and S_*=3^2*127=1143. Formula (17)
gives r0=21280. Since e<11/4 and

\[
6860\cdot4^8-11^8=235218079>0,
\]

we have log(6860)>8. Therefore (4) gives

\[
r<3n+\frac{3n}{32}=\frac{99n}{32}<21280.
\]

The final strict inequality is the integer comparison

\[
32\cdot21280-99\cdot6860=1820>0.
\]

Thus no multiple allowed by R|r lies in the required interval.
This closes every record in the finite domain and proves (1).

## 6. Consequence for every prime-power factor of a general n-2

Let p^a be any exact prime-power factor of n-2 in a hypothetical
solution, and put w=(n-2)/p^a. The theorem gives

\[
\boxed{\frac{w}{\gcd(w,6)}\ge13.}
\tag{18}
\]

In particular,

\[
\boxed{p^{v_p(n-2)}\le\frac{n-2}{13}}
\tag{19}
\]

for every prime divisor p of n-2. The gcd factor in (18) can make
this bound stronger. No large-base hypothesis p>6w is required.

If n-2 has exactly two distinct prime divisors, each of its two
exact prime powers is the complementary cofactor for the other.
Consequently an exact power of 2 must be at least 32, an exact
power of 3 at least 81, and primes 5,7,11 must occur to at least
the second power. An exact power based at a prime at least 13
already meets this numerical threshold, but still has to satisfy
the other original-equation constraints. This is a necessary
condition, not an existence assertion.

## 7. Reproduction and verification scope

Run

```sh
python3 v10_small_cofactors_checks.py generate
python3 v10_small_cofactors_checks.py verify
```

The first command regenerates all certificates and then verifies
them. The second reads the saved complete certificates and independently
reconstructs the whole finite domain.

The two calculations deliberately use different routes:

- The generator obtains cofactors by w<=72 and c_w<=12. The
  verifier reconstructs them from c=1,...,12 and g|6 with w=cg
  and gcd(w,6)=g.
- The generator uses a prime sieve and exact binomial coefficients
  to obtain D_w. The verifier uses deterministic trial division and
  factorial valuation sums, checking the full factor products.
- The generator uses the arithmetic progression (15). The verifier
  examines every exponent up to the proved maximum and directly
  applies x even, 3x<2alpha, or q<=4w.
- The generator computes v_p(X) by factorial valuations. The
  verifier instead counts carries in k+(N-k) for N=n^2 and
  k=6n-9.
- The generator applies the closed formula (8). The verifier
  enumerates the finite local alternatives 3e>=alpha or 2e=x
  and takes their smallest e before reconstructing R and S_*.

Every displayed factorization is verified by deterministic primality
tests and exact multiplication. All 5,717 prime-factor records and
all 5,717 independent carry valuations passed. The result is in
`v10_small_cofactors_verification.json`, with hashes of the checker,
proof note and complete certificate file.

### A separate reproduction on a larger domain

The root reviewer independently reproduced the exclusion in
`v10_small_cofactors_independent_reproduction.py`. This implementation
does not read the certificates, D_w, or the exponent progression
(15). It uses only the proved bounds p<=6w and p^a<9w^3, enumerating
the resulting larger domain of 2,423 parameter records and 2,393
distinct indices. Its largest index is 238,172,330. It computes
15,408 valuations by base-p digit sums, another formula distinct
from both the generator's factorial-floor computation and the
primary verifier's carry counting.

The independent exclusion counts are 1,920 small-recovered-defect
records, 502 broad-gap records, and the same final logarithmic-gap
record (6860, R=1330, S_*=1143). All candidates are excluded. The
extra records in this larger domain disappear at the recovered-
defect test, which explains why the first count differs from 480.
Its complete result is saved in
`v10_small_cofactors_independent_reproduction_verification.json`.

The root reviewer also independently audited this entire proof and
the primary generator/verifier code on 2026-11-05 and reported PASS.
This was an independent AI mathematical audit, not external peer
review. No source changes were required to the mathematical argument.

The unbounded statements rely on the written local-divisibility
proof, the established gap and small-index theorems, and the complete
v9 continued-fraction result. The finite checks do not extrapolate
from a bounded box. The local recovery is also developed in
`v10_valuation_recovery.md`. The shared v10 formal source
`v10_formal/ValuationRecovery.lean` proves the outer-binomial cubic
divisibility, local odd/even recovery, critical valuation dichotomy,
and finite-exponent parametrization, and was actually kernel-checked
by the root reviewer. The construction of the full product B, the
continued-fraction transfer, the completeness and exclusion of the
983-record domain, and the whole theorem (1) have not been formalized
in Lean. The entire original equation remains unsolved.
