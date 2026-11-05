# Further ordering and divisibility restrictions in the upper branch

The equation and notation are

\[
\binom AB=X+Y,
\quad A=\binom ij,\quad B=\binom{k}{\ell},
\quad X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2},
\quad t=A-B,\quad M=\max(j,\ell).
\]

We use the proved upper-branch prerequisites

\[
0<t\le B,\qquad M\ge21,\qquad \varphi M<t<10M,
\]

\[
1\le j\le i-2,\qquad1\le\ell\le k-2.
\]

The exclusions of equal upper indices in this branch, equal effective
lower indices, and adjacent upper indices are from
`continuation_arithmetic.md`, `equal_effective_upper.md`, and
`adjacent_rows_exclusion.md`, respectively.

## 1. The upper indices and effective lower indices must be oppositely ordered

Put

\[
d=\min(j,i-j),\qquad e=\min(\ell,k-\ell).
\]

Every remaining upper-branch solution satisfies

\[
\boxed{(i-k)(d-e)<0,\qquad |i-k|\ge2.}
\tag{1}
\]

Only the strict opposite ordering needs proof beyond the cited results.
Let \(n>m\) denote the larger and smaller upper indices, and let
\(a,b\) be their respective effective lower indices. Suppose \(a>b\).
Write \(U=\binom na\), \(V=\binom mb\).

If \(n=m+1\), then

\[
U\ge\binom n{b+1}
=\frac n{b+1}\binom{n-1}b\ge2V,
\]

because \(b+1\le a\le n/2\). Equality is possible only when
\(a=b+1=n/2\).

If \(n\ge m+2\), then

\[
\frac UV\ge\frac{\binom{m+2}{b+1}}{\binom mb}
=\frac{(m+2)(m+1)}{(b+1)(m+1-b)}
\ge\frac{4(m+1)}{m+2}>2.
\]

Thus \(U\ge2V\), with equality possible only in the adjacent central
case just described. Since \(A>B\), necessarily \(A=U\), \(B=V\).
But the upper branch requires \(A\le2B\), so only that equality case
could remain. Then \(n\ge M+2\ge23\), and

\[
t=B=\binom{n-1}{n/2-1}
\ge\binom{n-1}2>10n>10M,
\]

again a contradiction. Hence \(a>b\) is impossible. The equality
\(a=b\) has already been excluded, leaving \(a<b\), which is (1).

## 2. An exact separation inequality for unequal upper indices

Continue with the notation \(n>m\), \(a<b\) forced by (1), and put
\(D=n-m\), \(h=b-a\). The coefficient ratio can be written as

\[
\frac VU
=\frac{\binom{n-a}{D}\binom{m-a}{h}}
       {\binom nD\binom bh}
=\frac PQ,
\qquad P,Q\in\mathbb Z_{>0}.
\]

Since \(A\ne B\), the two integers \(P,Q\) are different. Therefore

\[
t=|U-V|\ge\frac UQ.
\]

Every remaining upper-branch solution must consequently satisfy the
explicit integer inequality

\[
\boxed{\binom na<10M\binom n{n-m}\binom ba.}
\tag{2}
\]

This is a necessary separation condition on the positions of the inner
binomial coefficients. It is not merely a comparison of their logarithms.
For adjacent rows, this integer-numerator argument is the source of the
exponential gap in `adjacent_rows_exclusion.md`.

## 3. A divisibility obstruction for every upper-branch candidate with j=1

Suppose \(j=1\). Then \(M=\ell\ge21\), \(A=i=B+t\),
and \(X=A^2\). Define the integer

\[
D_\ell=\frac{(\ell^2)!}{\ell!}.
\]

Then every solution must satisfy

\[
\boxed{B\mid D_\ell(t^2-1).}
\tag{3}
\]

**Proof.** The polynomial

\[
F_\ell(z)=\prod_{s=0}^{\ell^2-1}(z^2-s)
\]

contains \(\prod_{a=0}^{\ell-1}(z-a)\) as a factor in
\(\mathbb Z[z]\): for each \(a\), use the factor
\(z^2-a^2=(z-a)(z+a)\). Hence for some
\(P_\ell\in\mathbb Z[z]\),

\[
D_\ell Y
=\frac{F_\ell(k)}{\ell!}
=\binom{k}{\ell}P_\ell(k)
=B P_\ell(k).
\tag{4}
\]

In particular, \(B\mid D_\ell Y\).

Also

\[
t<10\ell\le\ell^2-\ell,
\qquad
D_\ell=\binom{\ell^2}{\ell}(\ell^2-\ell)!,
\]

so \(t!\mid D_\ell\). Let
\(L=\binom{B+t}{t}\). The product formula gives

\[
t!(L-1)=\prod_{h=1}^t(B+h)-t!\equiv0\pmod B.
\]

Thus \(B\mid D_\ell(L-1)\). Using \(L=A^2+Y\), (4), and
\(A=B+t\), we obtain

\[
0\equiv D_\ell(L-1)
\equiv D_\ell(t^2-1)\pmod B,
\]

proving (3). \(\square\)

### Prime-support consequence

Every prime divisor of \(D_\ell\) is at most \(\ell^2\).
Moreover \(t+1<\ell^2\), so every prime divisor of
\(t^2-1=(t-1)(t+1)\) is also at most \(\ell^2\).
Consequently

\[
\boxed{\text{Every prime divisor of }\binom{k}{\ell}
       \text{ is at most }\ell^2.}
\tag{5}
\]

Equivalently, all \(\ell\) consecutive integers

\[
k-\ell+1,\ k-\ell+2,\ \ldots,\ k
\]

have no prime divisor larger than \(\ell^2\). A prime larger than
\(\ell^2\) dividing their product cannot be cancelled by the
denominator \(\ell!\), so it would contradict (5).

This restriction holds for arbitrarily large \(\ell,k\); it does
not depend on extending the previously checked range of indices.
It does not itself prove that this entire family is empty.
