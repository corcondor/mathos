# A uniform exact height bound for every remaining solution

## Statement

Consider the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

at valid nonnegative integer arguments, and set

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2},
\quad M=\max(j,\ell),\quad t=A-B,\quad r=\min(B,t).
\]

**Theorem.** Every solution with \(M\ge21\) satisfies

\[
\boxed{A<H_M:=\frac{(M^2)!}{(M!)^{2M}}<e^{M^2}.} \tag{1}
\]

In particular,

\[
i,k<e^{M^2},\qquad
 i<j\,e^{M^2/j},\qquad k<\ell\,e^{M^2/\ell}. \tag{2}
\]

The upper bound \(H_M\) is an exactly computable rational number; for the integer \(A\), it means \(A\le\lceil H_M\rceil-1\). A simpler, slightly weaker integral bound is \(A,i,k<3^{M^2}\). The earlier independently verified exclusion of \(M\le20\) means that (1) applies to every remaining candidate for the original equation. The theorem does not bound \(M\) itself, and therefore does not settle existence for unrestricted indices.

## 1. Established lemmas used

The elementary boundary reductions give

\[
1\le j\le i-2,\quad 1\le\ell\le k-1,\quad 1<B<A,
\quad r\ge j+2,\quad t\ge M+2. \tag{3}
\]

For \(m\ge1\), write

\[
Q_m(n)=\frac{\binom{n^2}{m^2}}{\binom nm^{2m}},\qquad
q_m=\frac{(m!)^{2m}}{(m^2)!}.
\]

The ratio proof in `sharp_q_ratio_proof.md` / `sharp_q_bounds.md` establishes:

\[
Q_m(n)\ge q_m\quad(n\ge m+1), \tag{4}
\]

\[
Q_m(n)<16\quad(n\ge m+2). \tag{5}
\]

For \(m=1\), both \(Q_m\) and \(q_m\) equal 1. For \(m\ge2\), (4) follows from strict decrease of \(Q_m\) and its limit \(q_m\).

The same ratio analysis establishes the following large-\(A\) consequence for \(M\ge21\):

\[
A\ge\binom{2M}{M}\quad\Longrightarrow\quad r<2M. \tag{6}
\]

Finally the elementary product estimate in `proof_reduction.md` gives

\[
\left|\frac{Q_m(n)}{q_m}-1\right|\le\frac{3m^3}{n}
\qquad(n\ge2m^3). \tag{7}
\]

The proof below uses precisely these statements.

## 2. Auxiliary estimates

### 2.1 The limiting ratio has a simple exponential lower bound

Robbins's factorial bounds give

\[
q_m>
 e^{-m^2}(2\pi)^{m-1/2}m^{m-1}e^{-1/(12m^2)}
>e^{-m^2}. \tag{8}
\]

To check the last inequality uniformly, its extra factor is at least
\(\sqrt{2\pi}\,e^{-1/12}>1\): use \(\pi>3\) and
\(e^{1/6}<1/(1-1/6)=6/5\). Thus

\[
\boxed{\frac1{q_m}<e^{m^2}.} \tag{9}
\]

### 2.2 Monotonicity of the limiting factorial ratio

The sequence \(q_m\) is strictly decreasing. Its exact successive ratio is

\[
\frac{q_{m+1}}{q_m}
=\frac{(m+1)^{2m+2}(m!)^2}
{\prod_{a=1}^{2m+1}(m^2+a)}
<\frac{(1+1/m)^{4m+2}}{4^m}, \tag{9a}
\]

using \(m!\le((m+1)/2)^m\) by the arithmetic-geometric mean inequality. For \(m\ge4\), the last expression is less than \(e^5/4^m<243/256<1\). For \(m=3\), it is less than 1 by \(4^{11}<3^{14}\). The first two comparisons follow from \(q_1=1\), \(q_2=2/3\), \(q_3=9/70\). In particular,

\[
j\le M\quad\Longrightarrow\quad \frac1{q_j}\le H_M. \tag{9b}
\]

### 2.3 A lower bound for the proposed height

The elementary factorial estimates

\[
n!\le e\sqrt n\,(n/e)^n,\qquad n!>(n/e)^n
\]

follow from integral estimates for \(\log n!\). For the first, concavity of \(\log\) gives
\(\log n!\le\int_1^n\log x\,dx+(\log n)/2\); the second follows from monotonicity of \(\log\).

They imply

\[
q_M<\bigl(M e^{2-M}\bigr)^M<e^{-M^2/2}
\quad(M\ge21), \tag{9c}
\]

because \(\log M+2<M/2\) in that range. This last inequality holds at \(M=21\), using \(\log21<4\), and its right-minus-left difference is increasing for \(M>2\). Thus

\[
\boxed{H_M>e^{M^2/2}\quad(M\ge21).} \tag{9d}
\]

### 2.4 A factorial ratio needed in the equal-degree case

For every integer \(j\ge11\),

\[
\boxed{T_j=q_j(2j)!<\frac14.} \tag{10}
\]

This has a short analytic proof with no finite scan. Applying the factorial bounds from §2.3, and \((2j)!\le(2j)^{2j}\), yields

\[
T_j<\bigl(4j^3e^{2-j}\bigr)^j. \tag{11}
\]

The function \(4x^3e^{2-x}\) strictly decreases for \(x>3\). At \(x=11\),

\[
4\cdot11^3e^{-9}=\frac{5324}{e^9}<\frac45,
\]

because \(e>8/3\) and

\[
(8/3)^9>6655=\frac54\,5324.
\]

The latter is the exact integer comparison
\(134217728>6655\cdot19683=130990365\).
Therefore

\[
T_j<(4/5)^j\le(4/5)^{11}<\frac14,
\]

proving (10).

## 3. Assume a solution exceeds the proposed bound

Suppose for contradiction that

\[
M\ge21,\qquad A\ge H_M>e^{M^2/2}. \tag{12}
\]

Since \(M/2>\log4\),

\[
A>e^{M^2/2}>4^M>\binom{2M}{M}.
\]

Thus (6) forces

\[
r<2M. \tag{13}
\]

We now cover all possible solutions.

### 3.1 The maximum lower index is \(j=M\)

By (4),

\[
q_M A^{2M}\le X<X+Y=\binom Ar\le\frac{A^r}{r!}.
\]

Therefore

\[
A^{2M-r}<\frac1{q_Mr!}<\frac1{q_M}=H_M.
\]

But \(2M-r\) is a positive integer, so \(A\le A^{2M-r}<H_M\), contradicting (12).

### 3.2 The maximum lower index is \(\ell=M>j\), and \(t\le B\)

Here \(r=t<2M\) and \(B=A-t\ge A/2\). Hence

\[
q_M(A/2)^{2M}\le q_MB^{2M}\le Y
<\binom At\le\frac{A^t}{t!}.
\]

This implies

\[
A^{2M-t}<\frac{4^M}{q_Mt!}. \tag{14}
\]

Since \(t\ge M+2\), one has \(t!\ge(M+2)!>4^M\). The last inequality holds for every integer \(M\ge1\): its initial value is \(3!>4\), and its successive factorial multiplier is \(M+3\ge4\).

Using this fact in (14) gives

\[
A\le A^{2M-t}<\frac1{q_M}=H_M,
\]

again a contradiction.

### 3.3 The maximum lower index is \(\ell=M>j\), and \(B\le t\)

Now \(B=r<2M\). If \(k\ge M+2\), then

\[
B=\binom kM\ge\binom{M+2}{2}>2M,
\]

a contradiction. Therefore

\[
k=M+1,\qquad B=M+1=:b. \tag{15}
\]

The fixed second summand becomes

\[
Y=\binom{b^2}{(b-1)^2}=\binom{b^2}{2b-1}<b^{4b}. \tag{16}
\]

For every \(M\ge21\),

\[
\log(M+1)<\frac M5. \tag{17}
\]

For example, the initial case follows from \(\log22<4<21/5\), while the derivative of \(M/5-\log(M+1)\) is positive for \(M>4\). Thus

\[
Y<b^{4b}<e^{4M(M+1)/5}<e^{M^2}<A^2. \tag{18}
\]

We will also use

\[
17b^b<e^{M^2/2}<A. \tag{19}
\]

Indeed,

\[
\log(17b^b)<3+\frac{M(M+1)}5<\frac{M^2}{2}
\]

for \(M\ge21\); \(\log17<3\) follows from \(e>8/3\).

There are three cases according to the outer lower index \(b\) relative to \(2j\).

#### Case \(b>2j\)

Since \(j\le i-2\), (5) applies to \(X\), and (18) gives

\[
X+Y<16A^{2j}+A^2\le17A^{2j}.
\]

On the other hand,

\[
\binom Ab\ge(A/b)^b.
\]

The original equation consequently forces

\[
A^{b-2j}<17b^b.
\]

The exponent is a positive integer, so \(A<17b^b<A\) by (19), a contradiction.

#### Case \(b<2j\)

Using (4),

\[
q_jA^{2j}\le X<\binom Ab\le A^b/b!.
\]

Hence

\[
A^{2j-b}<\frac1{q_jb!}<\frac1{q_j}\le H_M,
\]

where the last step uses (9b). This again contradicts (12), since \(2j-b\) is a positive integer.

#### Case \(b=2j\)

In this case \(M=2j-1\ge21\), so \(j\ge11\). Because \(A=\binom ij\le i^j\), assumption (12) gives

\[
i\ge A^{1/j}>e^{(2j-1)^2/(2j)}>e^{2j-2}>6j^3. \tag{20}
\]

The last inequality holds at \(j=11\), since \(e^{20}>2^{20}>6\cdot11^3\), and the logarithmic derivative of \(e^{2j-2}/(6j^3)\) is \(2-3/j>0\).

From (7), \(Q_j(i)<(3/2)q_j\). With (10), this implies

\[
X<\frac32q_jA^b<\frac{3A^b}{8b!}. \tag{21}
\]

Also, (19) ensures \(A>b^2\). The elementary product bound \(\prod_h(1-z_h)\ge1-\sum_hz_h\), applied to the outer binomial coefficient, gives

\[
\binom Ab
=\frac{A^b}{b!}\prod_{h=0}^{b-1}\left(1-\frac hA\right)
>\frac{A^b}{2b!}. \tag{22}
\]

Subtracting (21) from (22),

\[
\binom Ab-X>\frac{A^b}{8b!}>A^2>Y. \tag{23}
\]

For the middle inequality, note that \(8b!<17b^b<A\) by (19), and \(b\ge22\), so \(A^{b-2}\ge A>8b!\). Equation (23) contradicts the original equation.

All cases contradict (12), proving \(A<H_M\). Combining this with (9) proves the full statement (1).

## 4. Bounds for the original upper indices

For every interior binomial coefficient, \(i\le A\) and \(k\le B<A\), which proves the first bounds in (2).

The product comparison

\[
\binom ij\ge(i/j)^j,
\qquad
\binom{k}{\ell}\ge(k/\ell)^\ell
\]

then gives the sharper coordinate statements in (2). In particular, whichever lower index equals \(M\) has its corresponding upper index less than \(M e^M\).

## 5. Logical status and references

This is an unconditional implication for any solution with \(M\ge21\). Its analytic ingredients are the already proved ratio estimates and the large-\(A\) theorem (6); all additional estimates and cases are proved above. The only use of the earlier finite computation is to know that a solution, if any, must have \(M\ge21\). No computation over four integer variables is part of the new height argument.

For the factorial bounds underlying (8), see Herbert Robbins, *A Remark on Stirling's Formula*, American Mathematical Monthly 62(1), 1955, pp. 26–29, https://doi.org/10.2307/2308012 . The elementary bounds in §2.3 follow from the explicitly given integral argument and do not require a numerical factorial check.
