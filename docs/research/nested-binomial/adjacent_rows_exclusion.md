# Adjacent upper indices are impossible in the upper branch

We consider

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\qquad
A=\binom ij, B=\binom{k}{\ell},\ t=A-B,
\quad M=\max(j,\ell).
\]

The prerequisites already proved in the existing notes are:

\[
M\ge21,\quad 1\le j\le i-2,\quad
1\le\ell\le k-1,\quad 1<B<A,
\]

and, in the upper branch \(t\le B\),

\[
\varphi M<t<10M,
\qquad \varphi=(1+\sqrt5)/2.
\tag{1}
\]

Here \(M\ge21\) uses the previous complete exclusion of \(M\le20\).
Also the upper branch forces \(\ell\le k-2\): otherwise
\(B=k=\ell+1\), whereas the earlier bound \(t\ge M+2\)
contradicts \(t\le B\).

## Theorem

There is no solution in the upper branch with

\[
\boxed{|i-k|=1.}
\]

The analytic argument below treats all \(\max(i,k)\ge256\).
The remaining, proved finite range is checked by an exact integer
program. The finite check only tests the necessary conditions (1), not
the large nested binomial equation itself.

## 1. A gap lemma for adjacent rows

**Lemma.** Let \(n\ge256\), and let

\[
1\le a\le\lfloor n/2\rfloor,
\qquad 1\le b\le\lfloor(n-1)/2\rfloor.
\]

Put \(U=\binom na\), \(V=\binom{n-1}b\). If

\[
0<|U-V|<10n,
\]

then \((a,b)=(1,1)\) or \((a,b)=(2,2)\).
The corresponding differences are 1 and \(n-1\).

**Proof.** First suppose \(a\ge b\).
If \(a=b\), Pascal's identity gives

\[
U-V=\binom{n-1}{a-1}.
\]

For \(a\ge3\), this is at least \(\binom{n-1}2>10n\).
Thus only \(a=b=1,2\) can remain in this case.

If \(a\ge b+1\) and \(b\ge2\), unimodality gives

\[
U\ge\binom n{b+1}
=\frac n{b+1}V\ge2V,
\]

because \(b+1\le a\le n/2\). Hence
\(U-V\ge V\ge\binom{n-1}2>10n\).
For \(b=1\), instead use
\(U-V\ge\binom n2-(n-1)=\binom{n-1}2>10n\).

Now suppose \(a<b\). For \(a=1\),

\[
V-U\ge\binom{n-1}2-n>10n.
\]

Suppose \(2\le a\le3n/8\). Then \(b\ge a+1\), and

\[
\frac UV
\le\frac{\binom na}{\binom{n-1}{a+1}}
=\frac{n(a+1)}{(n-a)(n-a-1)}.
\]

The last expression increases with \(a\). Consequently

\[
1-\frac UV
\ge \frac{n-104}{25n-40}\ge\frac1{50}
\quad(n\ge256).
\]

Since \(b\ge3\), this gives

\[
V-U\ge\frac1{50}\binom{n-1}3
\ge\frac{n^3}{2400}>10n.
\]

For the second inequality, each of \(n-1,n-2,n-3\) is at
least \(n/2\); the final inequality follows from \(n^2>24000\).

It remains to treat \(a>3n/8\). Put \(h=b-a\ge1\).
The ratio of the two coefficients is exactly

\[
\frac VU
=\frac{(n-a)\binom{n-a-1}h}{n\binom bh}
=\frac PQ,
\]

where \(P,Q\) are positive integers. If \(U\ne V\), then
\(|P-Q|\ge1\). Hence

\[
|U-V|\ge\frac UQ
\ge\frac{\binom{2a}a}{n\,2^b}
\ge\frac{2^{2a-b}}{n(2a+1)}
>\frac{2^{n/4}}{n(n+1)}>10n.
\]

We used \(\binom{2a}a\ge4^a/(2a+1)\),
\(b\le n/2\), and \(a>3n/8\). The final bound holds
at \(n=256\), and the logarithm of
\(2^{n/4}/[10n^2(n+1)]\) has derivative
\((\log2)/4-2/n-1/(n+1)>0\) for \(n\ge256\).
This completes the proof. \(\square\)

The lemma allows exact equalities \(U=V\). They are irrelevant to
the original equation, which requires \(A>B\).

## 2. Application to the equation for large upper indices

Assume \(|i-k|=1\), and put \(n=\max(i,k)\). Replace
each lower index by its effective value, namely the smaller of that
index and its complement in its own row. This puts the two coefficients
in the form \(U,V\) of the lemma.

Both original lower indices are at most their upper index minus 2.
Therefore \(M\le n-2\), and (1) gives

\[
0<|U-V|=t<10M<10n.
\]

If \(n\ge256\), the lemma leaves only two possibilities.

* Effective indices \((1,1)\): then \(t=1\), contradicting
  \(t>\varphi M\).
* Effective indices \((2,2)\): then \(t=n-1\). If both original
  lower indices are 2, then \(M=2\), already excluded.
  Otherwise at least one original lower index is its row size minus 2,
  so \(M\ge n-3\). For \(n\ge23\),
  \(n-1<(3/2)(n-3)<\varphi M\), contradicting (1).

Thus no solution has \(n\ge256\).

## 3. The finite range

Since \(M\ge21\) and \(M\le n-2\), only
\(23\le n\le255\) remain.

The accompanying `verify_adjacent_rows.py` checks every effective pair
\((a,b)\) in these rows. Apart from \((a,b)=(1,1),(2,2)\), the
only pairs with \(0<|U-V|<10n\) are

| \(n\) | \(a\) | \(b\) | \(U-V\) |
|---|---|---|---|
| 23 | 1 | 2 | -208 |
| 24 | 1 | 2 | -229 |

In both exceptional cases the larger coefficient is \(V\), whereas
the smaller coefficient is \(U=n\). Thus
\(t=V-U>U=B\), violating the upper-branch condition.
The pairs with equal effective indices 1 or 2 are excluded exactly as
in Section 2. The program additionally reconstructs every possible
orientation of the original lower indices and confirms that none meets
all necessary conditions.

All computations use Python's arbitrary-precision integers and
`math.comb`. The inequality \(t>\varphi M\) is checked without
floating point by

\[
2t>M\quad\text{and}\quad (2t-M)^2>5M^2.
\]

Together with the analytic lemma, this proves the theorem.

## Scope

This excludes a new infinite family: adjacent upper indices in the
upper branch, with no restriction on their size and no restriction on
the difference between the lower indices. It does not handle adjacent
upper indices in the lower branch, or prove global nonexistence.
