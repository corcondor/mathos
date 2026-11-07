# Upper branch with ell = k-2: a common large-prime divisor bound

## Scope

We retain the squared-index equation and write

\[
A=\binom ij,\quad B=\binom{k}{k-2}=\frac{k(k-1)}2,
\quad t=A-B,\quad L=\binom At,
\quad X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{4k-4}.
\]

Assume the upper branch \(0<t\le B\). The previously proved small-M,
endpoint, equal-effective-index, and opposite-ordering results imply that
every remaining candidate has \(k\ge23\) and is one of the following:

1. \(j=1\), so \(X=A^2\), or
2. \(d=\min(j,i-j)\ge3\) and \(i<k\).

Indeed effective index 2 is already excluded; effective index 1 cannot
mean \(j=i-1\) by the endpoint exclusion. In both remaining cases
\(M=k-2\). Thus \(t\ge M+2=k\), and if \(k\ge802\),

\[
t<5(k-2)<5k. \tag{1}
\]

## 1. A shared numerator product

Put

\[
h=\lfloor k/2\rfloor,
\qquad N=B+h=\lfloor k^2/2\rfloor,
\qquad P=\prod_{s=1}^{h}(B+s).
\]

For this section assume \(k\ge802\). Let \(P_{>5k}\) be the product of the prime powers in \(P\) belonging
to primes larger than \(5k\). Then

\[
\boxed{P_{>5k}\mid\gcd(L,Y),\quad\text{hence } P_{>5k}\mid X.} \tag{2}
\]

**Proof.** The numerator of \(L=\binom{B+t}{t}\) contains every
\(B+s\), since \(h<t\), and its denominator \(t!\) has no prime
above \(5k\) by (1). The numerator of \(Y\) contains the distinct
integers

\[
2(B+s)=k^2-k+2s\quad(1\le s\le h),
\]

because these lie between \(k^2-(4k-4)+1\) and \(k^2\).
Its denominator \((4k-4)!\) also has no prime above \(5k\), and the
factor 2 does not affect any such prime valuation. Thus the full prime
powers in \(P_{>5k}\) divide both binomial coefficients. Since
\(L-Y=X\), they divide \(X\) as well. \(\square\)

## 2. Explicit lower bound for the common factor

The following published inequalities are used, with deliberately rounded
constants:

\[
\theta(x)<1.001x,\qquad
\psi(x)-\theta(x)<1.001\sqrt{x}+1.8x^{1/3}\quad(x>0). \tag{3}
\]

They follow from Dusart, *Estimates of some functions over primes without
R.H.*, arXiv:1002.0442, Propositions 3.2 and 5.1, which give respectively
\(1.00007\sqrt{x}+1.78x^{1/3}\) and
\(\theta(x)<(1+1/36260)x\).

Also,

\[
S(x):=\sum_{p\le x}\frac{\log p}{p-1}<\log x\quad(x\ge319). \tag{4}
\]

For completeness, (4) follows from Rosser--Schoenfeld (1962), Theorem 6,
inequality (3.22):
\(\sum_{p\le x}\log p/p<\log x+E+1/(2\log x)\), together with
their identity \(E=-\gamma-\sum_p\log p/[p(p-1)]\).
Adding the partial sum of the latter prime series gives
\(S(x)<\log x-\gamma+1/(2\log x)<\log x\), because
\(\gamma>1/2\) and \(\log319>1\).

For each prime \(p\le5k\), counting multiples of \(p^a\) in an
interval of length \(h\) gives

\[
v_p(P)\le\frac{h}{p-1}+\lfloor\log_pN\rfloor.
\]

Therefore, since \(N<(5k)^2\),

\[
\begin{aligned}
\log P_{>5k}
&\ge h\log B-hS(5k)-\sum_{p\le5k}\lfloor\log_pN\rfloor\log p\\
&>h\log\frac{B}{5k}
 -\theta(5k)-\bigl(\psi(N)-\theta(N)\bigr).
\end{aligned}
\]

Using \(\sqrt N<0.71k\), \(N^{1/3}\le k^{2/3}\), and (3),

\[
\theta(5k)+\psi(N)-\theta(N)
<\frac{23}{4}k+2k^{2/3}.
\]

As \(B/(5k)=(k-1)/10\), we obtain, for \(k\ge802\),

\[
\boxed{
\log P_{>5k}
>\frac{k-1}{2}\log\frac{k-1}{10}
-\frac{23}{4}k-2k^{2/3}.
} \tag{5}
\]

Here the replacement \(h\ge(k-1)/2\) is legitimate because
\(\log((k-1)/10)>0\).

For the threshold comparisons below, the simpler consequence

\[
\log P_{>5k}
>\frac{k-1}{2}\log k-7k+\frac54-2k^{2/3} \tag{6}
\]

is convenient. It follows from \((k-1)/10>k/11\) and
\(\log11<5/2\).

## 3. The case j=1 has k < 2^21

Since \(A\le2B<k^2\), we have \(X=A^2<k^4\).
Suppose \(k\ge2^{21}\). Then \(k^{2/3}\le k/128\) and
\(\log k>29/2\): for example
\(\log2>2(1/3+1/81)=56/81\), so
\(21\log2>392/27>29/2\).
Subtracting \(4\log k\) from (6) gives

\[
\begin{aligned}
\log P_{>5k}-4\log k
&>\frac{k-9}{2}\log k-7k+\frac54-2k^{2/3}\\
&>\frac{15}{64}k-64>0.
\end{aligned}
\]

Thus \(P_{>5k}>X\), contradicting the divisibility (2). Therefore

\[
\boxed{j=1,\ \ell=k-2,\ t\le B\quad\Longrightarrow\quad k<2^{21}.} \tag{7}
\]

## 4. Every remaining d>=3 case has k < 2^24

Here \(\binom i3\le\binom id=A\le2B<k^2\), so

\[
(i-2)^3<6k^2,\qquad i<2k^{2/3}+2.
\]

The proved ratio bound \(X<16A^{2j}\), with \(j<i\), yields

\[
\log X<\log16+(8k^{2/3}+8)\log k. \tag{8}
\]

Suppose \(k\ge2^{24}\). Then \(k^{2/3}\le k/256\),
\(\log k>16\), and \(\log16<3\). Subtracting (8) from (6) gives

\[
\begin{aligned}
\log P_{>5k}-\log X
&>\left(\frac{15k}{32}-\frac{17}{2}\right)\log k
 -\frac{897k}{128}+\frac54-\log16\\
&>\frac{63k}{128}-\frac{551}{4}>0.
\end{aligned}
\]

This again contradicts (2). Hence

\[
\boxed{d\ge3,\ \ell=k-2,\ t\le B\quad\Longrightarrow\quad k<2^{24}.} \tag{9}
\]

For this remaining finite part, \(i<131074\). Because \(A\) and \(B\)
differ by less than \(10(k-2)\), only a bounded number of triangular
numbers immediately below any fixed \(A\) need be considered.

## 5. Current status

The analytic bounds (7) and (9) are the proved output of this note.
The subsequent finite exclusion is now complete and independently
verified; the assembled theorem excluding the entire upper
\(\ell=k-2\) family is in `v4_upper_complement_two_complete.md`.
This note supplies the analytic part of that proof.

An independently checked sharpening is recorded separately in
`v4_upper_complement_two_sharper_bounds.md`: its thresholds are
\(k<2^{20}\) for \(j=1\) and \(k<2^{22}\) for \(d\ge3\).

### Primary references checked

- J. B. Rosser and L. Schoenfeld, *Approximate formulas for some functions
  of prime numbers*, Illinois Journal of Mathematics 6 (1962), 64--94,
  Theorem 6, p.70; DOI https://doi.org/10.1215/ijm/1255631807 .
  PDF https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf .
- P. Dusart, *Estimates of some functions over primes without R.H.*, 2010,
  https://arxiv.org/pdf/1002.0442 , Propositions 3.2 and 5.1.
