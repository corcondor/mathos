# Two sharper bounds for the squared-index binomial ratio

For an integer \(m\ge1\) and real \(n\ge m+1\), interpret the binomial coefficients by their falling-factorial polynomials and put

\[
Q_m(n)=\frac{\binom{n^2}{m^2}}{\binom nm^{2m}}.
\]

All factors are positive in this range. The following statements are proved below:

1. For \(m\ge2\), \(Q_m(n)\) is strictly decreasing for real \(n\ge m+1\). For \(m=1\), it is identically 1.
2. Uniformly for integers \(m\ge1\), \(n\ge m+2\), one has \(Q_m(n)<16\).

The second statement is an analytic bound; its proof does not require checking a finite numerical table of values of \(m\).

## 1. Monotonicity

Logarithmic differentiation gives

\[
\frac{d}{dn}\log Q_m(n)
=2\left(n\sum_{s=0}^{m^2-1}\frac1{n^2-s}
          -m\sum_{h=0}^{m-1}\frac1{n-h}\right).
\tag{1}
\]

Write \(s=mh+r\), where \(0\le h,r<m\). For each pair \((h,r)\), put \(a=n-h\), \(b=n-r\). Since \(m\le n-1\),

\[
\begin{aligned}
&\frac{n}{n^2-mh-r}+\frac{n}{n^2-mr-h}\\
&\quad\le \frac{n}{(n-1)a+b}+\frac{n}{(n-1)b+a}
\le\frac1a+\frac1b.
\end{aligned}
\tag{2}
\]

For the last inequality, its two sides have the common positive factor \(a+b\). It is equivalent to

\[
((n-1)a+b)((n-1)b+a)\ge n^2ab,
\]

whose difference is exactly \((n-1)(a-b)^2\). Summing (2) over all \((h,r)\) proves that the expression in parentheses in (1) is nonpositive. If \(m\ge2\), at least one pair has \(h\ne r\), so the inequality is strict. For \(m=1\), direct evaluation gives \(Q_1(n)=1\).

Consequently,

\[
Q_m(n)\le Q_m(m+2)\qquad(n\ge m+2).
\tag{3}
\]

## 2. A uniform constant for an offset of at least two

Put \(x=m+1\ge2\), \(N=(x+1)^2\), and \(K=4x\). Complementing the numerator's lower index gives

\[
Q_m(m+2)=\frac{\binom NK}{[x(x+1)/2]^{2x-2}}.
\tag{4}
\]

For \(0\le z<1\), \(\log(1-z)\le-z-z^2/2\). Therefore

\[
\binom NK\le\frac{N^K}{K!}
\exp\left(-\frac{K(K-1)}{2N}
-\frac{K(K-1)(2K-1)}{12N^2}\right).
\tag{5}
\]

Use the standard strict Stirling lower bound

\[
K!>\sqrt{2\pi K}(K/e)^K
\tag{6}
\]

(which also follows from the Robbins bound used in `proof_reduction.md`). Substituting into (4) yields

\[
Q_m(m+2)<\frac{x^{7/2}}{4\sqrt{8\pi}}
\left(\frac{e^4}{64}\right)^x
\left(1+\frac1x\right)^{6x+2}
\exp\left(-\frac{2x(4x-1)}{(x+1)^2}
-\frac{x(4x-1)(8x-1)}{3(x+1)^4}\right).
\tag{7}
\]

The inequality

\[
\log(1+1/x)\le\frac1x-\frac1{2x^2}+\frac1{3x^3}
\]

and the identity

\[
\frac{2x(4x-1)}{(x+1)^2}=8-\frac{18}{x+1}+\frac{10}{(x+1)^2}
\]

show that the logarithm of (7) is at most

\[
\frac72\log x-(6\log2-4)x-\log(4\sqrt{8\pi})-2+R(x),
\tag{8}
\]

where

\[
R(x)=-\frac1x+\frac1{x^2}+\frac2{3x^3}
+\frac{18}{x+1}-\frac{10}{(x+1)^2}
-\frac{x(4x-1)(8x-1)}{3(x+1)^4}.
\]

For every real \(x\ge2\),

\[
R(x)\le\frac{33}{4x}.
\tag{9}
\]

Here is an explicit algebraic check. The numerator of
\(33/(4x)-R(x)\), over the positive denominator \(12x^3(x+1)^4\), is

\[
P(x)=23x^6-144x^5+206x^4+244x^3+15x^2-44x-8.
\]

With \(y=x-2\ge0\), this becomes

\[
P(x)=23y^6+132y^5+y^2(146y^2-188y+423)+2432y+2076>0,
\]

because the quadratic's discriminant is \(188^2-4\cdot146\cdot423<0\).

Also,

\[
6\log2-4>\frac{19}{120}.
\tag{10}
\]

For an entirely rational check of the constant, the first four terms of
\(\log2=2\sum_{r\ge0}((2r+1)3^{2r+1})^{-1}\) sum to
\(53056/76545>499/720\), which implies (10).

Thus (8) and (9) bound \(Q_m(m+2)\) above by

\[
h(x)=\frac{e^{-2}}{4\sqrt{8\pi}}x^{7/2}
\exp\left(-\frac{19x}{120}+\frac{33}{4x}\right).
\tag{11}
\]

Its logarithmic derivative has the sign of
\(-19x^2+420x-990\). Hence its global maximum on \([2,\infty)\) occurs either at \(x=2\) or at

\[
x_+=\frac{210+\sqrt{25290}}{19}\in(19,20).
\]

At the first point, \(h(2)=e^{217/120}/\sqrt\pi<e^2<9\). At the second, the function \(x^{7/2}e^{-19x/120}\) is increasing throughout \([19,20]\), so

\[
h(x_+)\le2000\sqrt{\frac5{2\pi}}\exp(-1079/228)<16.
\tag{12}
\]

The last numerical constant can also be checked without floating-point evaluation. Use \(\pi>31/10\) and

\[
e^{1079/228}>e^{4+73/100}
>\left(\frac{19}{7}\right)^4\frac{1037}{500}
>\frac{225}{2}.
\]

Indeed \(e>19/7\), and the first six terms of the exponential series at \(73/100\) exceed \(1037/500\). Thus the middle expression of (12) is less than
\(800/(9\sqrt{31})<16\), the last inequality following by squaring: \(640000<642816\).

Combining (3), (11), and (12) proves

\[
\boxed{Q_m(n)<16\quad(m\ge1,\ n\ge m+2).}
\tag{13}
\]

## 3. Immediate consequences for the nested-binomial equation

Use the notation \(A,B,X,Y,M,r,t\) of `proof_reduction.md`, with the necessary conditions already established there. If \(r\ge5M\), then \(\ell=k-1\) is impossible, since it would give \(B=\ell+1\le M+1<r\). We already know \(j\le i-2\). Thus (13) applies to both summands, giving

\[
X+Y<16A^{2j}+16B^{2\ell}\le32A^{2M}.
\tag{14}
\]

### 3.1 A gap of ten times the largest lower index is impossible for \(M\ge21\)

Assume \(r\ge10M\). As in the earlier proof, \(A\ge20M\), \(A\ge M^2/2\), and

\[
\binom Ar\ge\frac{(A/(5M))^{10M}}{20M+1}.
\]

Dividing by (14), the ratio is greater than or equal to

\[
\frac{q^M}{32(20M+1)},\qquad q=\frac{A^8}{5^{10}M^{10}}.
\]

The two lower bounds on \(A\), split at \(M=40\), give

\[
q\ge\max\left\{\frac{65536}{25M^2},\frac{M^6}{256\cdot5^{10}}\right\}
\ge\frac{1024}{625}.
\]

One has \((1024/625)^{21}>32(20\cdot21+1)\); this is a single exact integer comparison. The inequality is preserved as \(M\) increases, because \(1024/625>(20(M+1)+1)/(20M+1)\) for \(M\ge21\). Hence the left side of the original equation would exceed its right side. Therefore

\[
\boxed{r<10M\quad\text{for every solution with }M\ge21.}
\tag{15}
\]

Together with the previously verified exclusion \(M\le20\), this is a necessary condition on every remaining candidate.

### 3.2 A stronger conditional bound

If \(M\ge21\) and \(A\ge M^3/6\), then

\[
\boxed{r<5M.}
\tag{16}
\]

To prove this, assume \(r\ge5M\), use (14), and apply the same central-binomial estimate with \(s=5M\). The ratio of the left-side lower bound to the right-side upper bound is at least

\[
\frac{q_5^M}{32(10M+1)},\qquad
q_5=\left(\frac25\right)^5\frac{A^3}{M^5}
\ge\frac{4M^4}{84375}>9\quad(M\ge21).
\]

Since \(9^{21}>32(10\cdot21+1)\), and the exponential subsequently grows faster than the linear denominator, this is a contradiction.

The premise \(A\ge M^3/6\) holds, in particular, whenever a variable attaining the maximum lower index \(M\) has upper index at least \(M+3\): its binomial coefficient is at least \(\binom{M+3}{3}>M^3/6\), and \(A>B\) if that term is the second one.

These consequences are reductions, not a proof of global nonexistence.

### 3.3 Further offset bounds

For \(M\ge21\), the same argument gives the following table. An offset condition means that at least one of the terms with lower index \(M\) has its upper index at least \(M+d\).

| Offset condition | Sufficient bound on \(A\) | Necessary gap bound |
|---|---|---|
| \(d\ge3\) | \(A\ge\binom{M+3}{3}\) | \(r<5M\) |
| \(d\ge4\) | \(A\ge\binom{M+4}{4}\) | \(r<4M\) |
| \(d\ge5\) | \(A\ge\binom{M+5}{5}\) | \(r<3M\) |

For the second row, assume \(r\ge4M\). The quotient of the central-binomial lower bound by (14) is at least

\[
\frac{q_4^M}{32(8M+1)},\qquad
q_4=\frac{A^2}{16M^4}\ge\frac{M^4}{9216}>21.
\]

This exceeds 1 for \(M\ge21\). For the third row, assume \(r\ge3M\). Again \(\ell=k-1\) is impossible, so (14) applies. The quotient is at least

\[
\frac{q_3^M}{32(6M+1)},\qquad
q_3=\frac{8A}{27M^3}
\ge\frac{8\binom{M+5}{5}}{27M^3}>2.
\]

To check the last bound uniformly, the function \(\binom{x+5}{5}/x^3\) increases for \(x\ge21\): its logarithmic derivative is
\(\sum_{h=1}^5 1/(x+h)-3/x\ge5/(x+5)-3/x>0\).
At \(M=21\), \(q_3\ge526240/250047>2\). Finally
\(2^{21}>32(6\cdot21+1)\), and the exponential-to-linear comparison persists for larger \(M\).

### 3.4 An unconditional bound for sufficiently large \(M\)

For every solution with \(M\ge800\),

\[
\boxed{r<5M.}
\tag{17}
\]

If \(r\ge5M\), the endpoint \(\ell=k-1\) is excluded, and \(A\ge M^2/2\) as before. In the proof of (16) this gives the weaker but sufficient estimate

\[
q_5\ge\frac{4M}{3125}\ge\frac{128}{125}.
\]

The exact comparison \((128/125)^{800}>32(10\cdot800+1)\) proves the base case, and the same exponential-to-linear comparison proves it for all larger \(M\).

## 4. A much smaller height when the gap is at least \(2M\)

The following estimate also follows from the ratio monotonicity and does not need the constant 16:

\[
\boxed{M\ge21,\quad A\ge\binom{2M}{M}\quad\Longrightarrow\quad r<2M.}
\tag{18}
\]

Thus a candidate with \(r\ge2M\) must have \(A<\binom{2M}{M}<4^M\).

### 4.1 A uniform upper bound on both squared-index terms

The entropy argument in the earlier proof, specialized to \(n=2m\), gives

\[
Q_m(2m)\le(4m)^m e^{-m^2/2}.
\tag{19}
\]

Consider any \(1\le m\le M\), \(n>m\), and \(D=\binom nm\le A\). If \(n\ge2m\), monotonicity gives

\[
\binom{n^2}{m^2}\le (4m)^m e^{-m^2/2}A^{2m}
\le (4M)^M e^{-M^2/2}A^{2M}.
\tag{20}
\]

For the last inequality, the logarithm
\(f(x)=x\log(4x)-x^2/2+2x\log A\) increases on \([1,M]\):

\[
f'(x)=\log(4x)+1-x+2\log A>0,
\]

because \(A\ge\binom{2M}{M}\ge2^M\) and \(2\log2>1\).

If \(n<2m\), then

\[
\binom{n^2}{m^2}\le\binom{4m^2}{m^2}
\le\binom{4M^2}{M^2}
=Q_M(2M)\binom{2M}{M}^{2M}
\le(4M)^M e^{-M^2/2}A^{2M}.
\tag{21}
\]

The middle inequality can be seen by appending a fixed set of \(M^2-m^2\) new objects to each \(m^2\)-subset of a \(4m^2\)-set. There are enough new objects in a \(4M^2\)-set. Applying (20) or (21) to both original terms gives

\[
X+Y\le2(4M)^M e^{-M^2/2}A^{2M}.
\tag{22}
\]

### 4.2 Contradiction for \(r\ge2M\)

If \(r\ge2M\), unimodality and the product inequality \(\prod(1-z_h)\ge1-\sum z_h\) give

\[
\binom Ar\ge\binom A{2M}
>\frac{A^{2M}}{2(2M)!},
\tag{23}
\]

since \(A\ge2^M\ge4M^2>2M(2M-1)\) for \(M\ge21\).

We need

\[
4(4M)^M(2M)!e^{-M^2/2}<1.
\tag{24}
\]

Pair the factorial's terms and use arithmetic-geometric means:

\[
(2M)!=\prod_{h=1}^M h(2M+1-h)
\le\left(\frac{(M+1)(2M+1)}3\right)^M.
\tag{25}
\]

Thus the left side of (24) is at most \(4b(M)^M\), where

\[
b(x)=\frac{4x(x+1)(2x+1)}3e^{-x/2}.
\]

Its logarithmic derivative is at most \(3/x-1/2<0\) for \(x\ge7\). Also
\(b(21)=26488e^{-21/2}<9/10\). One exact verification of this last inequality uses \(e>8/3\) and
\((8/3)^{21}>(264880/9)^2\). Hence
\(4b(M)^M<4(9/10)^{21}<1\), proving (24). Equations (22) and (23) contradict the original equation. This proves (18).

## 5. A quasipolynomial height for the same branch

For \(M\ge24\), put

\[
s=\left\lceil6\log(2M)\right\rceil.
\]

Then \(s\le M\), and the exponential threshold in (18) can be replaced by

\[
\boxed{A\ge\binom{M+s}{M}\quad\Longrightarrow\quad r<2M.}
\tag{26}
\]

Consequently, \(r\ge2M\) forces

\[
A<\binom{M+s}{s}
\le\left(\frac{e(M+s)}s\right)^s
=\exp\bigl(O((\log M)^2)\bigr).
\tag{27}
\]

All logarithms here are natural. To check \(s\le M\), use \(\log48<4\) at \(M=24\), and the positivity of the derivative of \(x-6\log(2x)\) for \(x\ge24\).

For the proof, set \(u_m=ms/(m+s)\). The same entropy estimate gives

\[
Q_m(m+s)\le(8u_m)^m e^{-m u_m}.
\tag{28}
\]

Suppose \(A\ge\binom{M+s}{M}\). Since \(M\ge s\), this implies \(A\ge2^s\). If \(n\ge m+s\), monotonicity of \(Q_m\) and (28) apply. Moreover

\[
f_s(x)=x\log(8u_x)-xu_x+2x\log A
\]

increases for \(1\le x\le M\), because

\[
f_s'(x)=\log(8u_x)+\frac{s}{x+s}-s+\frac{s^3}{(x+s)^2}+2\log A>0.
\]

Here \(u_x\ge s/(s+1)\ge1/2\) and \(2\log A\ge2s\log2>s\). If \(n<m+s\), subset injection as in (21) gives
\(\binom{n^2}{m^2}\le\binom{(M+s)^2}{M^2}\), and (28) can again be applied at \(m=M\). Therefore, with \(u=Ms/(M+s)\),

\[
X+Y\le2(8ue^{-u})^M A^{2M}.
\tag{29}
\]

Now \(u\ge s/2\ge3L\), where \(L=\log(2M)\). Since \(u e^{-u}\) decreases for \(u\ge1\), equation (25) gives

\[
4(8ue^{-u})^M(2M)!
\le4\left(\frac{L(M+1)(2M+1)}{M^3}\right)^M.
\tag{30}
\]

For \(M\ge24\), the expression in parentheses is less than

\[
\frac{25}{24}\frac{49}{24}\frac{\log48}{24}
<\frac{1225}{3456}<\frac12.
\]

This uses that \(\log(2M)/M\) decreases in the relevant range. Thus (30) is less than 1. Also
\(A\ge2^s\ge(2M)^{6\log2}>(2M)^4\), so the product lower bound (23) is valid. If \(r\ge2M\), it contradicts (29). This proves (26).

## 6. A uniform height for every upper-branch solution

For \(M\ge21\), every solution in the branch \(t=A-B\le B\) satisfies

\[
\boxed{A<e^{M^2}.}
\tag{31}
\]

First, monotonicity and the leading coefficient limit give

\[
Q_m(n)\ge q_m:=\frac{(m!)^{2m}}{(m^2)!}.
\tag{32}
\]

The Robbins factorial bounds imply the convenient estimate

\[
q_m>e^{-m^2}.
\tag{33}
\]

Indeed they give the stronger lower bound

\[
q_m>e^{-m^2}\frac{(2\pi m)^m}{\sqrt{2\pi}\,m}
\exp\left(-\frac1{12m^2}\right).
\]

The extra factor exceeds 1: \((2\pi m)^m/(\sqrt{2\pi}\,m)\ge\sqrt{2\pi}>2\), while the exponential is greater than \(11/12\).

If \(A<\binom{2M}{M}\), then \(A<4^M<e^{M^2}\) already. Otherwise (18) applies; in the upper branch \(r=t\), so \(t\le2M-1\). Since \(B\ge A/2\), the term with lower index \(M\) contributes at least \(q_M(A/2)^{2M}\) to the right side. On the left,

\[
\binom At\le\binom A{2M-1}\le\frac{A^{2M-1}}{(2M-1)!}.
\]

It follows that

\[
A\le\frac{4^M}{q_M(2M-1)!}<e^{M^2},
\]

using \((2M-1)!\ge4^M\) for \(M\ge3\), which follows immediately by induction from \(5!>4^3\). This proves (31).

The statement is a proved height depending on \(M\). It does not bound \(M\) itself and hence does not settle global existence or nonexistence.

### 6.1 Sharper exact heights away from \(t=2M\)

The upper branch itself excludes \(\ell=k-1\): that endpoint gives \(B=\ell+1\), whereas the previously proved bound \(t\ge M+2\) contradicts \(t\le B\). Hence both terms satisfy the offset-two bound (13), without any extra assumption on \(r\).

For \(t<2M\), (32), \(B\ge A/2\), and \(\binom At\le A^t/t!\) give

\[
\boxed{A^{2M-t}\le\frac{4^M}{q_Mt!}
=\frac{4^M(M^2)!}{(M!)^{2M}t!}.}
\tag{34}
\]

For \(t>2M\), use (14) and \(\binom At\ge(A/t)^t\) to obtain

\[
\boxed{A^{t-2M}<32t^t.}
\tag{35}
\]

These are exact rational/integer inequalities, and can be converted to height bounds using integer root comparisons. They have no preliminary large-\(A\) threshold. For \(t=2M\), use (18) or (26).

## 7. Exclusion of the entire diagonal \(j=\ell\)

Together with the previously independently verified exclusion \(M\le20\), the new gap bound proves

\[
\boxed{\text{There is no solution with }j=\ell.}
\tag{36}
\]

To prove the remaining part, let \(j=\ell=M\ge21\). Since \(B\ge r\ge j+2=M+2\), we cannot have \(k=M+1\). Thus \(k\ge M+2\). Since \(A>B\) and the two binomial coefficients have the same lower index, \(i>k\).

If \(r=B\), then

\[
r=B\ge\binom{M+2}{2}>10M,
\]

contrary to (15). If \(r=t\), Pascal's identity and monotonicity in the upper index give

\[
r=t=\binom iM-\binom kM
\ge\binom{k+1}{M}-\binom kM
=\binom{k}{M-1}
\ge\binom{M+2}{3}>10M.
\]

This is the same contradiction. Both strict numerical inequalities hold for \(M\ge21\). No upper cutoff on \(i,k\) is used.
