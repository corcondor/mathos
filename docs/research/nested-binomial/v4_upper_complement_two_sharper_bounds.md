# Sharper explicit cutoffs for upper-branch ell = k-2

This note strengthens the cutoffs in `v4_upper_complement_two.md`, using
its same shared-product divisibility and its sharper lower bound (5).
The definitions, necessary conditions, and external prime-sum estimates
are exactly those in that note. In particular, the argument here is
applied only when \(k\ge802\), so \(t<5k\).

Put \(P=\prod_{s=1}^{\lfloor k/2\rfloor}(B+s)\), where
\(B=k(k-1)/2\), and let \(P_{>5k}\) retain the full powers of primes
larger than \(5k\). The established results are

\[
P_{>5k}\mid X,
\qquad
\log P_{>5k}
>\frac{k-1}{2}\log\frac{k-1}{10}
 -\frac{23k}{4}-2k^{2/3}. \tag{1}
\]

## Exact constants

We use

\[
\log2>\frac{693}{1000},\qquad
\log10<\frac{231}{100},\qquad
\log16<3. \tag{2}
\]

The first follows from the first three positive terms of the atanh
series for \(\log2\):

\[
\log2>2\left(\frac13+\frac1{81}+\frac1{1215}\right)
=\frac{842}{1215}>\frac{693}{1000}.
\]

For the second, a finite rational comparison gives

\[
\sum_{n=0}^{7}\frac{(231/100)^n}{n!}-10
=\frac{381233705038797}{8000000000000000}>0.
\]

Thus \(e^{231/100}>10\). For the third, \(e>8/3\) implies
\(e^3>(8/3)^3>16\).

For \(k\ge2\), integration of \(1/(1-x)\) gives

\[
\log(1-1/k)>-\frac1{k-1}\ge-\frac2k.
\]

Consequently (1) yields

\[
\boxed{
\log P_{>5k}
>\frac{k-1}{2}\log k-\frac{k-1}{2}\log10
-1-\frac{23k}{4}-2k^{2/3}.
} \tag{3}
\]

## 1. The j=1 case: k < 2^20

Here \(X=A^2<k^4\). Suppose \(k\ge2^{20}\). Since
\(100^3<2^{20}\), one has \(k^{2/3}<k/100\). Also,
\(\log k\ge20\log2>693/50\).

Subtract \(4\log k\) from (3). Since \((k-9)/2>0\), the constants
in (2) can be substituted with the indicated directions:

\[
\begin{aligned}
\log P_{>5k}-4\log k
&>\frac{k-9}{2}\log k-
   \frac{k-1}{2}\log10-1-\frac{23k}{4}-\frac{k}{50}\\
&>\frac{693(k-9)}{100}-\frac{231(k-1)}{200}
 -1-\frac{23k}{4}-\frac{k}{50}\\
&=\frac{k-12443}{200}>0.
\end{aligned}
\]

This would make \(P_{>5k}>X\), contradicting \(P_{>5k}\mid X\).
Therefore

\[
\boxed{j=1,\ \ell=k-2,\ t\le B\quad\Longrightarrow\quad k<2^{20}.}
\tag{4}
\]

## 2. The effective-index d>=3 case: k < 2^22

Here \(d=\min(j,i-j)\ge3\), \(i<k\), and
\(\binom i3\le A<k^2\). Thus

\[
(i-2)^3<6k^2,
\qquad
i<\frac{11}{6}k^{2/3}+2,
\]

since \((11/6)^3>6\). The established bound
\(X<16A^{2j}\) and \(j<i\) imply

\[
\log X<\log16+
\left(\frac{22}{3}k^{2/3}+8\right)\log k. \tag{5}
\]

Suppose \(k\ge2^{22}\). Since \(160^3<2^{22}\), one has
\(k^{2/3}<k/160\), and \(\log k>22(693/1000)=7623/500\).
Subtracting (5) from (3) gives

\[
\begin{aligned}
\log P_{>5k}-\log X
&>\left(\frac{109k}{240}-\frac{17}{2}\right)\log k
 -\frac{k-1}{2}\log10-1-\frac{23k}{4}-\frac{k}{80}-\log16\\
&>\left(\frac{109k}{240}-\frac{17}{2}\right)\frac{7623}{500}
 -\frac{231(k-1)}{200}-1-\frac{23k}{4}-\frac{k}{80}-3\\
&=\frac{269k}{40000}-\frac{33109}{250}>0.
\end{aligned}
\]

The logarithm's coefficient is positive in this range. The final
expression is increasing in \(k\), and its value at \(2^{22}\) is
the positive rational number \(35092823/1250\).
Again divisibility is contradicted. Hence

\[
\boxed{d\ge3,\ \ell=k-2,\ t\le B\quad\Longrightarrow\quad k<2^{22}.}
\tag{6}
\]

For finite enumeration, an exact integer bound is obtained directly
from \((i-2)^3<6\cdot2^{44}\). The stronger small-gap condition
\(A=B+t<B+10(k-2)\) gives an even smaller bound by inserting its
largest possible integer value of \(A\) into
\((i-2)^3<6A\). Both versions use integer cube roots and have no
floating-point dependency.

## Status

These are analytic upper bounds, not by themselves exclusions of the
finite remainders. The separate finite verification must cover all
\(23\le k<2^{20}\) in the first case and all
\(23\le k<2^{22}\) in the second case, with the earlier necessary
conditions. No Lean formalization of these logarithmic and prime-sum
bounds is claimed here.
