# Further structural reductions in the lower branch

## Setting and prerequisites

The equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

Write \(A=\binom ij\), \(B=\binom{k}{\ell}\),
\(X=\binom{i^2}{j^2}\), \(Y=\binom{k^2}{\ell^2}\),
\(M=\max(j,\ell)\), \(t=A-B\), and \(r=\min(B,t)\).
The lower branch is \(B\le t\), equivalently \(B\le A/2\).

We use the previously proved boundary conditions, exclusion of \(M\le20\),
and the analytic results in `sharp_q_bounds.md`:

\[
1\le j\le i-2,\quad 1\le\ell\le k-1,\quad
B\ge j+2,\quad B\ge k\ge\ell+1,
\]

\[
M\ge21,\qquad r<10M,
\qquad M\ge800\Longrightarrow r<5M,
\]

\[
Q_m(n):=\frac{\binom{n^2}{m^2}}{\binom nm^{2m}}<16
\quad(n\ge m+2).
\]

The ratio \(Q_m(n)\) is nonincreasing in real \(n\ge m+1\), strictly
decreasing for \(m\ge2\), with limit
\(q_m=(m!)^{2m}/(m^2)!\).

In particular, every remaining solution has \(B\ge M+1\ge22\).
The earlier classification gives two lower-branch types:

- L1: \(\ell>j\), \(k=\ell+1=B=:b\).
- L2: \(j>\ell\), \(M=j\), \(k\ge\ell+2\), \(B<10j\).

All new conclusions below are uniform implications and do not enlarge the
previous finite numerical search range.

## 1. A universal upper envelope for the second summand

**Lemma.** If \(B=\binom{k}{\ell}>1\), with \(1\le\ell<k\), then

\[
\boxed{\binom{k^2}{\ell^2}\le Z(B):=\binom{B^2}{2B-1}.}
\tag{1}
\]

The bound is attained at \((k,\ell)=(B,B-1)\).

**Proof.** If \(\ell=k-1\), this is equality. If \(\ell=1\), then
\(k=B\), and \(Y=B^2\le\binom{B^2}{2B-1}\), since the smallest interior
coefficient in row \(B^2\) is \(B^2\).

For \(2\le\ell\le k-2\), we have \(B\ge\binom k2\) and \(B\ge k\), so
\(k^2\le3B\). If \(k\ge5\), then \(B\ge10\), and

\[
Y\le2^{k^2}\le8^B,
\qquad
Z(B)\ge\left(\frac{B^2}{2B-1}\right)^{2B-1}
>\left(\frac B2\right)^{2B-1}\ge8^B.
\]

For the last inequality, use \(B/2\ge4\) and \(4B-2\ge3B\).
The only smaller interior case is \(k=4,\ell=2,B=6\); here
\(Z(B)=\binom{36}{11}>\binom{36}{4}>\binom{16}{4}=Y\).
This proves (1). \(\square\)

## 2. A cubic height whenever \(B\ge3j\)

**Theorem.** Every remaining solution satisfying \(B\ge3j\) has

\[
\boxed{A<B^3.} \tag{2}
\]

This implication is valid in either branch, though it is informative
primarily in the lower branch.

**Proof.** Suppose \(A\ge B^3\). The product bound for the outer coefficient gives

\[
L:=\binom AB
=\frac{A^B}{B!}\prod_{h=0}^{B-1}(1-h/A)
>\frac{A^B}{2B!}.
\]

Since \(X<16A^{2j}\) and \(B-2j\ge B/3\),

\[
\frac XL<\frac{32B!}{A^{B-2j}}
\le\frac{32B!}{B^B}
\le32\,2^{-\lfloor B/2\rfloor}\le\frac1{64}.
\tag{3}
\]

The penultimate inequality bounds the first \(\lfloor B/2\rfloor\)
factors of \(B!\) by \(B/2\), and all other factors by \(B\).

On the other hand, direct products give

\[
\frac{\binom{B^3}{B}}{Z(B)}
>\frac{(B^3-B)^B(2B-1)!}{B!B^{4B-2}}
>B(1-B^{-2})^B\ge B-1.
\]

Here \((2B-1)!/B!>B^{B-1}\), and the final step is Bernoulli's inequality.
By (1) and monotonicity in the upper argument,

\[
\frac YL<\frac1{B-1}\le\frac1{21}.
\tag{4}
\]

Equations (3)-(4) give \((X+Y)/L<1\), a contradiction. \(\square\)

For type L2, (2) in particular gives

\[
B\ge3j\Longrightarrow A<1000j^3;
\qquad
j\ge800\Longrightarrow A<125j^3.
\tag{5}
\]

## 3. A cubic lower height and a forbidden offset in type L1

For L1, \(k=B=b=\ell+1\) and \(Y=Z(b)\).

**Theorem.** Every L1 solution satisfies

\[
\boxed{A>\frac{b^3}{4},\qquad i-j\ge4.} \tag{6}
\]

**Proof.** If \(A\le b^3/4\), then \(L\le(b^3/4)^b/b!\), whereas

\[
Y=\binom{b^2}{2b-1}
>\frac{(b-1)^{4b-2}}{(2b-1)!}.
\]

Since \((2b-1)!/b!<(2b)^{b-1}\), this yields

\[
\frac YL>
\frac{2^{b+1}}b(1-1/b)^{4b-2}
>\frac{2^{b+1}}{243b}>1.
\tag{7}
\]

For the middle inequality, \(\log(1-x)\ge-x/(1-x)\) gives
\((4b-2)\log(1-1/b)>-5\) for \(b\ge22\), and \(e<3\).
The last inequality holds at \(b=22\) and increases thereafter.
Thus \(L<Y\), impossible.

For the offset conclusion, put \(d=i-j\). We already know \(d\ge2\).
Since \(\ell>j\), \(b\ge j+2\). If \(d=2\),
\(A\le\binom b2\le\binom{b+1}{3}\); if \(d=3\),
\(A\le\binom{b+1}{3}\). But

\[
\binom{b+1}{3}=\frac{b^3-b}{6}<\frac{b^3}{4},
\]

contradicting the first conclusion. \(\square\)

Combining with (2), L1 and \(b\ge3j\) imply

\[
\boxed{\frac{b^3}{4}<A<b^3,\qquad j^4<24b^3.}
\tag{8}
\]

Indeed \(i\ge j+4\) gives \(A\ge\binom{j+4}{4}>j^4/24\).

## 4. Exactly one real crossing in L1 when \(b\ge2j\)

This statement concerns real \(i\) only to describe the shape of the
integer problem; the original domain remains integer.

**Theorem.** Fix integers \(b\ge22\) and \(1\le j\le b/2\).
Extend binomial coefficients at real upper arguments by their falling-factorial
polynomials. On the interval \(i\ge j+2\), \(A=\binom ij\ge2b\), the equation

\[
\binom Ab=\binom{i^2}{j^2}+Z(b)
\]

has exactly one real root. In particular, each such pair \((b,j)\) permits
at most one integer \(i\).

**Proof.** Write \(X=\binom{i^2}{j^2}\) and \(Y=Z(b)\). The ratio of the
two sides is

\[
R(i)=\frac{\binom Ab}{X+Y}
=\frac{\binom Ab}{A^b}
\frac{A^{b-2j}}{Q_j(i)(1+Y/X)}.
\tag{9}
\]

As \(i\) increases, \(A\) and \(X\) strictly increase;
\(\binom Ab/A^b=(1/b!)\prod_{h=0}^{b-1}(1-h/A)\) strictly increases;
\(A^{b-2j}\) is nondecreasing; \(Q_j(i)\) is nonincreasing; and
\(1+Y/X\) strictly decreases. Thus \(R(i)\) strictly increases.

At the interval's left endpoint,

\[
A=\max\{\binom{j+2}{2},2b\}<b^3/4,
\]

using \(j\le b/2\) and \(b\ge22\). The proof of (7), which is also valid
for real \(A\ge2b\), gives \(R<1\) there.

If \(b>2j\), then \(R(i)\to\infty\).
If \(b=2j\), then \(j\ge11\), and

\[
R(i)\longrightarrow\frac1{q_j(2j)!}>4,
\]

by the factorial-ratio estimate in `global_height_bound.md`.
Continuity and strict monotonicity prove the assertion. \(\square\)

This shows why a single uniform sign comparison cannot eliminate the
entire L1 range \(b\ge2j\): a real crossing exists for every allowed pair.
The remaining issue there is whether that unique root can be an integer.

## 5. A logarithmic restriction in the same L1 range

**Theorem.** In L1 with \(b\ge2j\), put

\[
s=\lceil6\log(2b)\rceil.
\]

Then

\[
\boxed{\min(j,i-j)<s.} \tag{10}
\]

**Proof.** It suffices to exclude \(j\ge s\) and \(i\ge j+s\).
These inequalities imply

\[
A\ge\binom{j+s}{j}\ge\binom{2s}{s}\ge2^s
\ge(2b)^{6\log2}>(2b)^4.
\]

Put \(L_0=\log(2b)\), \(u=js/(j+s)\). The previously proved entropy
estimate and ratio monotonicity give

\[
Q_j(i)\le(8u e^{-u})^j
\le\left(\frac{3L_0}{b^3}\right)^j,
\]

because \(u\ge s/2\ge3L_0>1\).
Since \(2j\le b\le A/2\) and \(A>4j^2\),

\[
L:=\binom Ab\ge\binom A{2j}>\frac{A^{2j}}{2(2j)!}.
\]

Consequently

\[
\frac XL<2(2j)!Q_j(i)
\le2\left(\frac{12j^2L_0}{b^3}\right)^j
\le2\left(\frac{3\log(2b)}b\right)^j<\frac35.
\]

For the last step, \(3\log(2b)/b\) decreases for \(b\ge22\), and
its value there is less than \(12/22=6/11\), since \(\log44<4\).
Also \(j\ge s\ge2\), and \(2(6/11)^2=72/121<3/5\).

Meanwhile

\[
Y\le\frac{b^{4b-2}}{(2b-1)!}\le b^{3b-2},
\qquad L\ge(A/b)^b>b^{3b},
\]

since \((2b-1)!\ge b^b\). Thus \(Y/L<1/b^2<2/5\).
The two summands total less than \(L\), a contradiction. \(\square\)

## 6. Type L2 with \(B\ge3j\): only two offsets survive for \(j\ge100\)

**Theorem.** In L2,

\[
\boxed{j\ge100,\quad B\ge3j\quad\Longrightarrow\quad i-j\in\{2,3\}.}
\tag{11}
\]

**Proof.** Suppose \(i-j\ge4\). Then \(A\ge\binom{j+4}{4}>j^4/24\).
Both original terms have upper-minus-lower offset at least two, so
\(X+Y<32A^{2j}\).
Since \(A\ge2B\ge6j\), the central-binomial product estimate gives

\[
\binom AB\ge\binom A{3j}
\ge\frac{(2A/(3j))^{3j}}{6j+1}.
\]

The ratio to the upper bound on the right side is greater than

\[
\frac{q^j}{32(6j+1)},\qquad
q=\frac{8A}{27j^3}>\frac j{81}>\frac65\quad(j\ge100).
\]

At \(j=100\), \((6/5)^{100}>2^{20}>32\cdot601\), since \((6/5)^5>2\).
The quotient \((6/5)^j/(6j+1)\) increases thereafter. This makes the
left side larger than the right side, a contradiction. \(\square\)

The earlier cubic bound alone would give the weaker threshold 3000;
(11) improves it to 100 without a finite scan.

## 7. Position of \(B\) for offsets 2 and 3

### 7.1 Offset 2

If \(i=j+2\), then

\[
A=\binom{j+2}{2}<(j+2)^2,
\qquad X=\binom{(j+2)^2}{4j+4}.
\]

For \(j\ge21\), \(4j+4\le(j+2)^2/2\).
If \(B\le4j+4\), monotonicity gives
\(\binom AB<\binom{(j+2)^2}{4j+4}=X\).
Therefore

\[
\boxed{i-j=2\quad\Longrightarrow\quad B\ge4j+5.} \tag{12}
\]

### 7.2 Offset 3

Put \(n=j+3\), \(b_0=3j=3n-9\), \(N=n^2\), and \(A=\binom n3\).
For \(j\ge21\), \(b_0\le A/2\), so \(B\le b_0\) would imply

\[
\binom AB\le\binom A{b_0}.
\]

Here \(X=\binom N{6n-9}>\binom N{2b_0}\), because
\(2b_0<6n-9\le N/2\). Elementary product bounds and AM-GM yield

\[
\frac{\binom A{b_0}}{\binom N{2b_0}}
\le
\left(\frac{A(3b_0+1)}{2(N-2b_0+1)^2}\right)^{b_0}<1.
\]

For the last inequality, after clearing positive denominators, it is
enough that

\[
P(n)=3n^4-91n^3+792n^2-2684n+4332>0.
\]

Writing \(u=n-19\ge0\) proves this directly:

\[
P(19+u)=3u^4+137u^3+2103u^2+11167u+6042>0.
\]

Thus \(B\le3j\) is impossible, and

\[
\boxed{i-j=3\quad\Longrightarrow\quad B\ge3j+1.} \tag{13}
\]

There is also a sharper upper bound in L2: if \(j\ge30\) and \(i-j\ge3\),
then \(B<4j\). To prove it, suppose \(B\ge4j\). The same central
comparison now gives a ratio greater than

\[
\frac{q_4^j}{32(8j+1)},\qquad
q_4=\frac{A^2}{16j^4}>\frac{j^2}{576}\ge\frac{25}{16}.
\]

At \(j=30\), \((25/16)^{30}=(5/4)^{60}>2^{15}>32\cdot241\),
using \((5/4)^4>2\), and the quotient grows thereafter.

Combining (11)-(13) with \(B<5j\) for \(j\ge800\), we obtain the
disjoint bands

\[
\boxed{
\begin{array}{c|c}
\text{L2, }j\ge800,\ B\ge3j & \text{necessary range}\\\hline
i-j=3 & 3j<B<4j\\
i-j=2 & 4j+4<B<5j.
\end{array}}
\tag{14}
\]

No other offset is possible in this regime.

## 8. An exact degree-gap bound when \(B<2j\)

In either lower-branch type, \(Q_j(i)\ge q_j\) and
\(\binom AB\le A^B/B!\) give

\[
\boxed{
B<2j\quad\Longrightarrow\quad
A^{2j-B}<\frac{(j^2)!}{(j!)^{2j}B!}.
} \tag{15}
\]

In particular, since \(1/q_j<e^{j^2}\),

\[
i<j\exp\left(\frac{j}{2j-B}\right).
\]

For example, a fixed fractional gap \(B\le(2-\epsilon)j\) forces
\(i<j e^{1/\epsilon}\). This has no arbitrary cutoff on \(i\).

## Status

These results impose polynomial heights, logarithmic offset restrictions,
unique-real-root structure, and disjoint parameter bands on infinite
lower-branch families. They do not prove that the original equation has
no integer solution. In particular, the unique real crossings in Section 4
have not been uniformly proved nonintegral.
