# Lower branch with j=i-2 and ell>=2

This note addresses the original squared-index equation, with

\[
A=\binom i2,\quad B=\binom{k}{\ell},\quad
L=\binom AB,\quad X=\binom{i^2}{4i-4},\quad
Y=\binom{k^2}{\ell^2},\quad j=i-2.
\]

The branch in this note is \(B\le A/2\), and \(\ell\ge2\).
The previous small-M result excludes every candidate with
\(\max(j,\ell)\le20\). The previous lower-branch classification
excludes \(\ell>j\) here: every remaining candidate in that family
requires \(i-j\ge4\). Equality \(\ell=j\) is also already excluded.
Thus \(M=j=i-2\), so every remaining candidate has
\(i\ge23\) and \(2\le\ell<j=i-2\).

## 1. The second upper index is at most of square-root size

Let \(e=\min(\ell,k-\ell)\). The endpoint exclusions give
\(1\le\ell\le k-1\). If \(e=1\), then \(\ell=k-1\), as
\(\ell\ge2\); this makes \(B=k=\ell+1\le j\), contradicting
the established \(B>\varphi j\). Thus \(e\ge2\), and

\[
\binom k2\le B.
\]

For \(i\ge802\), the prior gap bound \(r<5M\), with
\(r=B\) and \(M=j=i-2\), gives

\[
B<5(i-2)<5i,
\qquad k(k-1)<10i,
\qquad k<\sqrt{10i}+1. \tag{1}
\]

In this branch \(k-\ell\ge2\), so the previously proved ratio
bound applies:

\[
\boxed{Y<16B^{2\ell}<16(5i)^{2k}.} \tag{2}
\]

## 2. A common large-prime factor must divide Y

Put

\[
h=\lfloor i/2\rfloor,
\qquad P=\prod_{s=0}^{h-1}(A-s),
\]

and let \(P_{>5i}\) denote the product of the full prime powers in P
whose primes are larger than \(5i\).

For \(i\ge802\), the prior boundary reduction gives
\(B\ge j+2=i\). Thus the numerator of \(L=\binom AB\)
contains all h displayed factors of P. Its denominator B! contains
no prime above \(5i\) by (1).

The numerator of \(X=\binom{i^2}{4i-4}\) contains all the distinct
integers

\[
2(A-s)=i^2-i-2s,\qquad 0\le s<h.
\]

Indeed they lie between \(i^2-4i+5\) and \(i^2\). The
denominator \((4i-4)!\) also contains no prime above \(5i\).
The factor 2 does not affect valuations at those primes. Therefore

\[
\boxed{P_{>5i}\mid L,\quad P_{>5i}\mid X,\quad
P_{>5i}\mid Y.} \tag{3}
\]

The full prime multiplicities are retained. This is a divisibility
of a difference \(Y=L-X\), not an assertion that a sum of smooth
integers is smooth.

Counting prime powers in the consecutive product as in
`v4_upper_complement_two.md` gives

\[
\log P_{>5i}
>h\log\frac{A-h+1}{5i}-\frac{23i}{4}-2i^{2/3}.
\]

Since \(A-h+1>i(i-2)/2\), this implies

\[
\log P_{>5i}
>\frac{i-1}{2}\log\frac{i-2}{10}
-\frac{23i}{4}-2i^{2/3}.
\tag{4}
\]

For \(i\ge4\), \(\log(1-2/i)>-4/i\). Consequently

\[
\boxed{\log P_{>5i}
>\frac{i-1}{2}\log i-\frac{i-1}{2}\log10
-2-\frac{23i}{4}-2i^{2/3}.} \tag{5}
\]

The external prime-sum bounds and their hypotheses are stated with
primary references in the companion note. All their uses here have
\(5i\ge4010>319\).

## 3. Absolute bound i<2^21

Suppose \(i\ge2^{21}\). Since
\(2^{21}>10\cdot420^2=1,764,000\), (1) gives

\[
k<\frac{i}{420}+1<\frac{i}{400}.
\]

The second inequality uses \(i>8400\). Hence (2) gives

\[
\log Y<\log16+\frac{i}{200}\log(5i).
\tag{6}
\]

Use the exact inequalities

\[
\log i>\frac{29}{2},\qquad
\log10<\frac{231}{100},\qquad
\log5<2,\qquad \log16<3,\qquad
i^{2/3}\le\frac i{128}.
\]

Their elementary justifications appear in
`v4_upper_complement_two_sharper_bounds.md`; for the first,
\(21\log2>21\cdot693/1000>29/2\).
Subtracting (6) from (5), with the positive coefficient
\(99i/200-1/2\) for \(\log i\), yields

\[
\begin{aligned}
\log P_{>5i}-\log Y
&>\left(\frac{99i}{200}-\frac12\right)\log i
-\frac{i-1}{2}\log10-2-\frac{23i}{4}
-\frac i{64}-\log16-\frac i{200}\log5\\
&>\frac{79i}{320}-\frac{2219}{200}>0.
\end{aligned}
\]

This contradicts \(P_{>5i}\mid Y\). Therefore

\[
\boxed{j=i-2,\quad \ell\ge2,\quad B\le A/2
\quad\Longrightarrow\quad i<2^{21}.} \tag{7}
\]

## 4. A certified narrow window for B

For \(i\ge1024\), (1) also implies
\(\sqrt{10i}\le i/10\), and \(i/10+1<i/8\).
Thus \(k<i/8\), and (2) gives

\[
Y<16(5i)^{i/4}.
\]

On the other hand, the elementary binomial lower bound gives

\[
X\ge\left(\frac{i^2}{4i-4}\right)^{4i-4}
>\left(\frac i4\right)^{4i-4}
>(5i)^{2i-2}>16(5i)^{i/4}>Y.
\]

Here \((i/4)^2>5i\) follows from \(i>80\), and the next
comparison is immediate from \(5i>16\) and
\(2i-2-i/4>1\). Therefore every such solution must satisfy

\[
\boxed{X<\binom AB<2X.} \tag{8}
\]

The binomial coefficient is strictly increasing for
\(0\le B\le\lfloor A/2\rfloor\). The exact integer
logarithm intervals for the fixed top \(A=\binom i2\), saved in
the symmetric complement-two certificate, thus restrict B to the
strictly intervening integers between two certified endpoints.
For \(23\le i<1024\), no logarithmic truncation is required:
the full previously necessary interval is retained.

## Status

The unbounded part (7) and the window reduction (8) are written
proofs. Finite congruence certificates for all the remaining
\(23\le i<2^{21}\), together with independent verification of
the binomial representations and endpoints, are recorded separately.
This note alone must not be read as having excluded that finite part
until those checks have completed.
