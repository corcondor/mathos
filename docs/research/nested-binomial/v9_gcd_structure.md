# Exact gcd defects and effective finiteness for every fixed cofactor

## Scope and results

The equation remains

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns the branch \(\ell=1,\ j=i-3\). Write

\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
G=\gcd(A,X),\quad S=A/G.
\]

Every remaining solution in this branch has \(n\ge104\), and v8 proved

\[
S\mid n-2,\qquad \log n<128S,\qquad n<2^{192S}.
\tag{1}
\]

The new result computes a prime component of S exactly. In particular,
it gives a finite upper bound for **every prescribed cofactor** in
\(n=wp^a+2\), including small prime bases and arbitrarily large exponents.
It does not claim that the resulting finite ranges have all been excluded.

For a positive integer w define

\[
B_w=\binom{6w}{2w},\qquad D_w=\frac{B_w}{\gcd(B_w,6)},
\qquad c_w=\frac{w}{\gcd(w,6)}.
\tag{2}
\]

**Exact defect theorem.** Let p be any prime, \(p\nmid w\),
\(q=p^a>4w\), and \(n=wq+2\). Then

\[
\boxed{v_p(S)=v_p(D_w),\qquad
S\mid c_w\,p^{v_p(D_w)}.}
\tag{3}
\]

The valuation identity in (3) is an arithmetic identity for the two
binomial coefficients; it does not assume that the original equation
has a solution. The divisibility uses the common-divisor theorem
behind \(S\mid n-2\).

For any solution satisfying these hypotheses, (1) therefore gives

\[
\boxed{\log n<128c_w\,p^{v_p(D_w)},\qquad
n<2^{192c_w p^{v_p(D_w)}}.}
\tag{4}
\]

In particular, \(p>6w\) implies \(p\nmid D_w\), so

\[
\boxed{p>6w\quad\Longrightarrow\quad S\mid c_w,
\qquad\log n<128c_w,
\qquad n<2^{192c_w}.}
\tag{5}
\]

There is also a simple bound requiring neither a factorization of
\(B_w\) nor coprimality in the prescribed parametrization:

\[
\boxed{\ell=1,\ j=i-3,\ i=wp^a+2
\quad\Longrightarrow\quad
\log i<\frac{768w^2}{\gcd(w,6)},\qquad
i<2^{1152w^2/\gcd(w,6)}.}
\tag{6}
\]

Here w is any positive integer, p any prime, and \(a\ge1\).
Both choices of the outer index k are included, through the established
common-divisor and logarithmic results.

## 1. Separating the lower p-adic digit block

Assume the hypotheses of (3), and put

\[
U=qw^2+4w,\qquad V=6w.
\]

The relevant integers split exactly as

\[
n^2=qU+4,\qquad 6n-9=qV+3,
\qquad n^2-(6n-9)=q(U-V)+1.
\tag{7}
\]

Because \(q>4w\ge4\), the remainders 4, 3, and 1 all lie in
\([0,q)\). Apply Legendre's formula for each factorial valuation.
At powers \(p^h\) with \(h\le a\), the upper-block terms cancel;
the remaining sum is exactly \(v_p\binom43=v_p(4)\).
At powers \(p^{a+h}\) the floors reduce to those for U, V, and U-V.
Consequently

\[
\boxed{v_p(X)=v_p(4)+v_p\binom UV.}
\tag{8}
\]

This identity also handles p=2. The two binary carries in \(3+1=4\)
are the contribution \(v_2(4)=2\); they must not be discarded.
For p=3 the lower block contributes zero.

## 2. The central factor gives the exact valuation

The numerator product in \(\binom UV\) has factors

\[
qw^2-2w+1,\ qw^2-2w+2,\ldots,\ qw^2+4w.
\]

The central factor \(qw^2\) has valuation a, since \(p\nmid w\).
Every other factor is \(qw^2+c\), where

\[
-2w+1\le c\le4w,\qquad c\ne0.
\]

The strict inequality \(q>4w\) implies \(0<|c|<q=p^a\), so

\[
v_p(qw^2+c)=v_p(c).
\]

Thus, writing \(b=v_p(B_w)\),

\[
\begin{aligned}
v_p\binom UV
&=a+v_p((2w-1)!)+v_p((4w)!)-v_p((6w)!)\\
&=a-v_p(2w)-v_p\binom{6w}{2w}\\
&=a-v_p(2)-b.
\end{aligned}
\tag{9}
\]

Combining (8) and (9) gives the exact formula

\[
\boxed{v_p(X)=a+\mathbf1_{p=2}-b.}
\tag{10}
\]

This formula has no restriction such as \(p>6w\). The prime base may
be small; the exponent enters only through \(p^a>4w\).

## 3. The contribution to the full gcd defect

For \(p\ge5\), the numbers n and n-1 are units modulo p, and
\(n-2=wq\). Hence \(v_p(A)=a\).

For p=3, the first two factors of \(6A=n(n-1)(n-2)\) are still
units, and division by 6 gives \(v_3(A)=a-1\).

For p=2, w is odd and \(q>4w\) implies \(a\ge3\). Thus
\(v_2(n)=1\), n-1 is odd, and again \(v_2(A)=a\).
All three cases are summarized by

\[
v_p(A)=a-\mathbf1_{p=3}.
\tag{11}
\]

Since \(S=A/\gcd(A,X)\), formulas (10)-(11) yield

\[
v_p(S)=
\begin{cases}
\max(b-1,0),&p=2\text{ or }3,\\
b,&p\ge5.
\end{cases}
\tag{12}
\]

By (2), this is precisely \(v_p(D_w)\), proving the first part
of (3). To obtain the strongest cofactor bound, retain the small
prime factors in the explicit common divisor from v6:

\[
Q=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid G.
\]

Checking the six residues of n modulo 6 gives

\[
\gcd(n,3)\gcd(n-1,6)=\frac6{\gcd(n-2,6)}.
\]

Consequently

\[
\boxed{S\mid A/Q=\frac{n-2}{\gcd(n-2,6)}.}
\tag{12a}
\]

Since \(p\nmid w\), the p-free part of this last integer is
\(c_w=w/\gcd(w,6)\). At every prime other than p, the valuation
of S is therefore bounded by its valuation in \(c_w\); at p it
is exactly the value in (12). This proves
\(S\mid c_w p^{v_p(D_w)}\).

For a hypothetical solution, insert this divisor bound into (1)
to obtain (4). When \(p>6w\), none of the factorials defining
\(B_w\) contains p, so \(v_p(D_w)=0\). This proves (5).

## 4. Bounding the fixed coefficient without factorization

Legendre's formula expresses b as

\[
b=\sum_{h\ge1}\left(
\left\lfloor\frac{6w}{p^h}\right\rfloor
-\left\lfloor\frac{2w}{p^h}\right\rfloor
-\left\lfloor\frac{4w}{p^h}\right\rfloor\right).
\tag{13}
\]

Each summand is 0 or 1, since \(6w=2w+4w\). It is zero for
\(p^h>6w\). Therefore

\[
b\le\lfloor\log_p(6w)\rfloor,
\qquad p^{v_p(D_w)}\le p^b\le6w.
\tag{14}
\]

This covers equality at the top digit as well; no strict upper bound
on \(p^h\) is substituted for the necessary \(p^h\le6w\).
Under \(p^a>4w\), (4) and (14) give

\[
\log n<768w c_w,\qquad n<2^{1152w c_w}.
\tag{15}
\]

If instead \(p^a\le4w\), then \(n\le4w^2+2\). The elementary
inequality \(\log x<x-1\) gives

\[
\log n<4w^2+1\le5w^2<128w^2
\le\frac{768w^2}{\gcd(w,6)}.
\]

Also \(4w^2+2\le6w^2<8^{w^2}=2^{3w^2}\), by the integer
inequality \(8^m\ge1+7m>6m\) for \(m\ge1\). Since
\(\gcd(w,6)\le6\), this also lies below
\(2^{1152w^2/\gcd(w,6)}\). Thus the same power-of-two bound holds
in this small-power case.

Finally, if a prescribed w is divisible by p, write
\(w=p^h w_0\), where \(p\nmid w_0\). Then

\[
n=w_0p^{a+h}+2,
\qquad w_0\le w.
\]

Apply the already proved result to \(w_0\) and \(a+h\). The
function \(u^2/\gcd(u,6)\) does not decrease when u is multiplied
by a prime power: the numerator grows by \(p^{2h}\), whereas the
gcd grows by at most \(p^h\). Therefore

\[
\frac{w_0^2}{\gcd(w_0,6)}\le\frac{w^2}{\gcd(w,6)}.
\]

Weakening the bound by this inequality proves (6) without a
coprimality hypothesis.

## 5. A quantitative restriction on every prime-power factor

For a general integer n in the offset-three branch, take any exact
prime power \(q=p^{v_p(n-2)}\) in n-2 and put \(w=(n-2)/q\).
Equation (6), weakened by \(\gcd(w,6)\ge1\), implies

\[
\boxed{\frac{n-2}{p^{v_p(n-2)}}
>\sqrt{\frac{\log n}{768}}.}
\tag{16}
\]

Equivalently, the largest prime-power factor

\[
Q_{\max}(n-2)=\max_{p\mid n-2}p^{v_p(n-2)}
\]

must satisfy

\[
\boxed{Q_{\max}(n-2)
<\sqrt{768}\,\frac{n-2}{\sqrt{\log n}}.}
\tag{17}
\]

The complementary factor therefore cannot remain bounded along an
unbounded sequence of solutions in this branch. When the exact prime
base additionally satisfies \(p>6w\), the stronger result (5) gives
\(w/\gcd(w,6)>\log n/128\).

This is a restriction on each prime-power factor, rather than merely
the number of distinct prime factors. It does not exclude all mixed
factorizations of n-2.

## 6. Reproducibility and limits

The companion script `v9_gcd_structure_checks.py` verifies the
valuation formulas by an independent base-p carry count, and checks
the full gcd divisor bound on smaller examples by constructing the
two binomial coefficients exactly. The checks include p=2 and p=3,
cases with \(v_p(B_w)>1\), and powers immediately above \(4w\).
It also checks the factor bound (14) and normalization when p divides
the originally prescribed cofactor.

These examples test the formulas; the uniform statements follow from
the written Legendre and central-factor proofs. The script does not
scan the original equation for solutions, and no finite check is
used to extrapolate a universal theorem. The finite upper bound for
each fixed cofactor is proved, but the full bounded remainder for
an arbitrary cofactor has not been evaluated here.

No new Lean formalization of these theorems is claimed.

The root reviewer and the fixed-cofactor reviewer independently
audited the proof on 2026-11-05 and reported PASS. The audits covered
the lower-block contribution at p=2, every central-factor valuation,
the p=2 and p=3 gcd corrections, the floor-sum bound at its endpoint,
normalization when p divides the prescribed cofactor, and the
restriction on every exact prime-power factor. The fixed-cofactor
reviewer identified the stronger divisor (12a); it yields the
coefficient \(c_w\) used in the final statement. These were
independent AI mathematical audits, not external peer review.

The completed exact checker passed 3,196 valuation comparisons,
including 307 cases with \(v_p(B_w)>1\) and 407 first powers above
\(4w\); 238 direct full-binomial gcd comparisons; and 1,000
normalization examples. These checks support the identities but do
not replace their uniform proofs.
