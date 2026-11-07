# A golden-ratio lower bound for the nested binomial equation

## Scope and notation

The equation throughout is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

with all binomial coefficients at valid nonnegative integer arguments. The right side uses squared arguments, not squared values. Set

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2},
\quad t=A-B,\quad r=\min(B,t),\quad M=\max(j,\ell).
\]

The established elementary boundary reduction gives
\(1\le j<i\), \(1\le\ell<k\), \(1<B<A\),
\(r\ge j+2\), and \(t\ge M+2\).
The present deductions are uniform in all the parameters; they do not depend on a finite computational exclusion range.

Write

\[
\phi=\frac{1+\sqrt5}{2},\qquad
h(p)=-p\log p-(1-p)\log(1-p).
\]

## 1. The external entropy inequality

Boppana's entropy inequality states

\[
\boxed{h(p^2)\ge\phi p\,h(p)\quad(0\le p\le1).} \tag{1}
\]

Equality holds precisely at \(p=0,1/\phi,1\). A primary source giving an elementary calculus proof is Ravi B. Boppana, *A Useful Inequality for the Binary Entropy Function* (2023), arXiv:2301.09664.

A 2026 generalization by Boon Suan Ho, *A generalization of Boppana's entropy inequality*, arXiv:2601.19327, includes (1) as Proposition 1 and supplies a Lean formalization of a more general power inequality. Only the established square case (1) is needed below. The finite-binomial deductions below are derived here; they are not asserted to be statements quoted from those papers.

## 2. A finite-binomial inequality, with the error factors included

**Theorem.** For all integers \(1\le m<n\),

\[
\boxed{\binom{n^2}{m^2}>\binom nm^{\phi m}.} \tag{2}
\]

The proof needs precise prefactors rather than just leading entropy asymptotics.

### 2.1 Entropy estimates

For \(0<a<N\), put \(p=a/N\). Robbins's factorial bounds imply

\[
\frac{e^{Nh(p)}}{\sqrt{8Np(1-p)}}
\le\binom Na
<\frac{e^{Nh(p)}}{\sqrt{2\pi Np(1-p)}}. \tag{3}
\]

Here is a check of the constants. Write

\[
v!=\sqrt{2\pi v}(v/e)^v e^{\rho_v},\qquad
\frac1{12v+1}<\rho_v<\frac1{12v}.
\]

For the upper bound, \(N>a\) gives
\(\rho_N<1/(12N)<1/(12a+1)<\rho_a\). Hence
\(\rho_N-\rho_a-\rho_{N-a}<0\), proving the strict upper estimate in (3).

For the lower bound, the loss in the exponential is at most

\[
f=\frac1{12a}+\frac1{12(N-a)}-\frac1{12N+1}.
\]

If \(N\ge3\), then \(f<1/10\): when both lower arguments are at least 2, \(f<1/12\); otherwise take \(a=1\), \(b=N-a\ge2\), obtaining

\[
f=\frac1{12}+\frac{13}{12b(12b+13)}
\le\frac{29}{296}<\frac1{10}.
\]

Since \(2\pi e^{1/5}<8\), the lower estimate follows. The remaining case \(N=2,a=1\) is equality in the stated lower estimate. Thus (3) holds for every case used here.

### 2.2 Transfer of (1) to exact binomial coefficients

For \(m=1\), (2) is simply \(n^2>n^\phi\), since \(n\ge2\) and \(\phi<2\).

Suppose \(m\ge2\), and put

\[
p=\frac mn,\qquad u=m(1-p).
\]

Since \(n\ge m+1\),

\[
u\ge\frac m{m+1}\ge\frac23,
\qquad 2\pi u>4.
\]

By (1) and (3),

\[
\binom{n^2}{m^2}
\ge\frac{e^{n^2h(p^2)}}{\sqrt{8m^2(1-p^2)}}
>\frac{e^{\phi mn h(p)}}{\sqrt8\,m},
\]

whereas

\[
\binom nm^{\phi m}
<\frac{e^{\phi mn h(p)}}{(2\pi u)^{\phi m/2}}.
\]

Consequently

\[
\frac{\binom{n^2}{m^2}}{\binom nm^{\phi m}}
>\frac{(2\pi u)^{\phi m/2}}{\sqrt8\,m}
>\frac{2^{3m/2}}{\sqrt8\,m}\ge1. \tag{4}
\]

The second strict inequality uses \(2\pi u>4\) and \(\phi>3/2\). The last inequality holds at \(m=2\), and its left side increases with \(m\): the successive ratio is \(2^{3/2}m/(m+1)>1\). This proves (2).

## 3. Consequences for the original equation

Applying (2) twice gives

\[
X>A^{\phi j},\qquad Y>B^{\phi\ell}. \tag{5}
\]

### 3.1 The smaller outer index

Since

\[
A^{\phi j}<X<X+Y=\binom Ar\le\frac{A^r}{r!},
\]

we obtain the quantitative necessary condition

\[
\boxed{(r-\phi j)\log A>\log(r!).} \tag{6}
\]

In particular,

\[
\boxed{r>\phi j,\qquad r\ge\lfloor\phi j\rfloor+1.} \tag{7}
\]

Equation (6) can be stronger than the simpler bound (7), especially when \(r\) is the first integer above \(\phi j\).

### 3.2 The complementary gap

We claim, without assuming either outer branch, that

\[
\boxed{t>\phi\ell.} \tag{8}
\]

Suppose instead \(t\le\phi\ell\). For \(\ell\le3\), this already contradicts \(t\ge\ell+2\). Thus \(\ell\ge4\) and \(t\ge6\).

Every interior binomial coefficient satisfies \(B=\binom{k}{\ell}\ge k\ge\ell+1\). Therefore

\[
\frac AB=1+\frac tB<1+\phi=\phi^2.
\]

For every integer \(t\ge6\),

\[
t!>\phi^{2t}. \tag{9}
\]

Indeed, at \(t=6\), \(\phi^{12}=144\phi+89<377<720=6!\); the induction step follows because \(t+1\ge7>\phi^2\).

It follows that

\[
\binom At\le\frac{A^t}{t!}
< B^t\frac{\phi^{2t}}{t!}
<B^t\le B^{\phi\ell}<Y,
\]

contradicting \(\binom At=X+Y\). This proves (8).

Since \(t\ge r>\phi j\), (8) also yields

\[
\boxed{t>\phi M,\qquad t\ge\lfloor\phi M\rfloor+1.} \tag{10}
\]

The following quantitative inequality is valid as well:

\[
\boxed{(t-\phi\ell)\log B>
\log(t!)-t\log\left(1+\frac tB\right).} \tag{11}
\]

It follows directly from \(\binom At>Y>B^{\phi\ell}\) and \(\binom At\le A^t/t!\).

Combining (7) and (10) with the previously proved \(r<12M\) gives

\[
\phi j<r<12M,\qquad t>\phi M.
\]

In the upper branch \(t\le B\), this becomes

\[
\boxed{\phi M<t<12M.} \tag{12}
\]

Any independently proved sharper upper bound for \(r\) can replace \(12M\) in this conclusion.

## 4. The coefficient is best possible for the binomial lemma

The coefficient \(\phi\) in (2) cannot be replaced by a larger universal constant. To see this, take integers \(n\to\infty\), \(m=\lfloor n/\phi\rfloor\), and write \(p=m/n\to p_0=1/\phi\).

Stirling's formula gives

\[
\log\binom{n^2}{m^2}=n^2h(p^2)+O(\log n),
\]

\[
m\log\binom nm=pn^2h(p)+O(n\log n).
\]

Thus

\[
\frac{\log\binom{n^2}{m^2}}
{m\log\binom nm}
\longrightarrow
\frac{h(p_0^2)}{p_0h(p_0)}
=\frac1{p_0}=\phi,
\]

using \(p_0^2=1-p_0\) and entropy symmetry. Any constant larger than \(\phi\) would fail for all sufficiently large members of this sequence. This sharpness concerns the standalone binomial comparison (2); it does not show that actual solutions of the nested equation approach the bound.

## 5. An infinite diagonal subclass is eliminated

The prior complete verification excludes \(\max(j,\ell)\le20\). Together with the previous uniform bound \(r<12M\), it also eliminates **every case \(j=\ell\)**, even when this common index is arbitrarily large.

It remains to consider \(j=\ell=M\ge21\). In the lower branch, \(B<12M\). If \(k\ge M+2\), then

\[
B\ge\binom{M+2}{2}>12M,
\]

since \((M+2)(M+1)-24M=M^2-21M+2>0\) for \(M\ge21\). Therefore \(k=M+1\) and \(B=M+1\), contradicting \(r=B\ge M+2\).

In the upper branch, \(k=M+1\) is impossible because \(t\ge M+2>B\). Hence \(k\ge M+2\). Since \(A>B\) and the lower indices agree, \(i>k\), and Pascal's identity yields

\[
t=\binom iM-\binom kM
\ge\binom{k}{M-1}
\ge\binom{M+2}{3}\ge12M.
\]

The last inequality already holds for \(M\ge7\). This contradicts \(t=r<12M\). Thus the diagonal subclass is excluded in full. This conclusion explicitly uses the earlier certified finite-range theorem for the small common indices.

## Primary references

1. Ravi B. Boppana, *A Useful Inequality for the Binary Entropy Function*, 2023. https://arxiv.org/abs/2301.09664 ; PDF https://arxiv.org/pdf/2301.09664 .
2. Boon Suan Ho, *A generalization of Boppana's entropy inequality*, 2026. https://arxiv.org/abs/2601.19327 ; full text https://arxiv.org/html/2601.19327v1 . The author's linked formalization is https://github.com/boonsuan/entropy-inequality . No Lean execution is claimed for the present work.
3. Herbert Robbins, *A Remark on Stirling's Formula*, American Mathematical Monthly 62(1), 1955, pp. 26–29. https://doi.org/10.2307/2308012 ; primary paper scan https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf .
