# v20 appendix: the intrinsic-defect height improves to 24 bits per unit

Date: 2026-11-07 JST. This is a written proof with exact rational checks.
No new Lean execution or DeepSeek API call is claimed. This appendix
does not edit the parent proof `v20_sharper_defect_height.md`; that
proof's global `log n<17 delta` remains valid independently.

## 1. Theorem and inherited inputs

Retain the original squared-index equation and the branch
`ell=1, j=i-3`. Set

\[
n=i,\quad A=\binom n3,\quad B=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),\quad t=r-3n,
\]

\[
M=\gcd(n,3)\gcd(n-1,6),\quad Q=n(n-1)/M,\quad
\delta=Q/\gcd(Q,r^2),\quad C=M\delta,\quad K=\delta r^2/Q.
\]

The inherited necessary conditions are

\[
n\ge104,\quad 3n<r<10n/3,\quad
B<\binom A r<2B,
\]
\[
Cr^2=Kn(n-1),\quad C,K\in\mathbb Z_{>0},\quad
C\le6\delta,\quad \delta\ge25.
\tag{1}
\]

The last lower bound is the already completed v19 exclusion; it is not
derived from the theorem about to be proved. Both original choices of
k are included in (1).

**Theorem.** Every original solution in this branch satisfies

\[
\boxed{n<2^{24\delta}.}
\tag{2}
\]

The proof also gives the sharper upper logarithmic gap

\[
\boxed{t<\frac{231n}{500\log n}\qquad(n\ge2^{600}).}
\tag{3}
\]

The proof splits at `2^600`, but performs no enumeration up to that
number. The entire lower range follows from `600=24*25` and the
previously proved delta>=25. All logarithms below are natural.

## 2. A rational lower bound for log 2

Let

\[
\lambda=\frac{693147}{10^6},\qquad \alpha=\frac{231}{500}.
\]

The integral identity

\[
\log2=2\int_0^{1/3}\frac{du}{1-u^2}
\]

and the first six terms of the positive geometric series imply

\[
\log2>
2\sum_{j=0}^{5}\frac1{(2j+1)3^{2j+1}}
=\lambda+\frac{335369}{4546773000000}>\lambda.
\tag{4}
\]

This is an exact rational lower bound, not a rounded numerical value
substituted into an inequality. We also use the elementary bounds
`8/3<e<3` and `log2<7/10`, proved by the exponential series in the
parent note and in `v20_logarithmic_gap.md`.

Put `N0=2^600`, `L=log n`, and `x=alpha/L`. If n>=N0, then

\[
L>600\lambda=\frac{2079441}{5000},\qquad
0<x<\frac{\alpha}{600\lambda}=\frac{110}{99021}<\frac1{100}.
\tag{5}
\]

The exact positive margin used in the binomial comparison is

\[
3\lambda-\frac{519}{250}
-3\left(\frac{110}{99021}\right)-\frac1{10000}
=\frac{276387}{33007000000}>0.
\tag{6}
\]

For `3<=y<=3+x`, `(8/3)^3>6(3+1/100)` gives `log(6y)<3`.
Likewise `(8/3)^4>48` gives `log48<4`.

## 3. Proof of the upper gap

Let `a=(3+x)n` and `b=ceil(a)`. Then `b<4n`. In the present range,

\[
A>n^3/7>16n^2>b^2,
\]

so b<A/2. The elementary product inequality and the factorial integral
bound give

\[
\prod_{j=0}^{b-1}(1-j/A)
\ge1-\frac{b(b-1)}{2A}>\frac12,
\qquad b!\le eb(b/e)^b,
\]

\[
\binom A b>\frac{(eA/b)^b}{2eb}
\ge\frac{(eA/a)^a}{2eb}.
\tag{7}
\]

The last comparison uses the increasing function
`y log(eA/y)` for `0<y<A`; it changes only the numerator and retains
the denominator `2eb`. It is valid whether or not a is integral.

As in the parent proof, the following lower and upper logarithmic
estimates hold:

\[
\log A>3\log n-\log6-4/n,
\qquad B<(en/6)^{6n}.
\tag{8}
\]

For completeness, the first uses
`A>(n^3/6)(1-3/n)` and
`log(1-3/n)>-3/(n-3)>=-4/n` for n>=12. The second follows from
`log(s!)>=s log s-s+1` and monotonicity of `y log(en^2/y)` between
`6n-9` and `6n<n^2`. All these ranges hold for n>=N0.

Write `f(y)=y(1-log(6y))`. Subtracting the logarithm of 2B from
the lower bound (7), and using `2xL=2alpha=231/250`, gives

\[
\log\frac{\binom A b}{2B}
>n\left\{3\log2-\frac{519}{250}+f(3+x)-f(3)\right\}
-4(3+x)-\log(4eb).
\tag{9}
\]

Since `f'(y)=-log(6y)>-3`, (4)-(6) make the expression in braces
greater than `1/10000`. Also `4(3+x)<13` and `4eb<48n`. Therefore
the right-hand side of (9) is greater than

\[
q(n)=n/10000-13-\log(48n).
\]

This function increases for n>10000. At N0, the bounds
`log N0=600log2<420` and `log48<4` give

\[
q(N_0)>2^{600}/10000-437>0.
\]

Thus `binom(A,b)>2B`. The original solution has `binom(A,r)<2B`,
with `r<=A/2`, so monotonicity of the binomial row gives `r<b`.
For integer r, `r<ceil(a)` implies `r<a`, including integral a.
This proves (3), with no lost endpoint and for both k branches.

## 4. The height for n >= 2^600

Because r>3n and `Cr^2=Kn(n-1)`, the integer K-9C is positive.
It is therefore at least 1. Using (3),

\[
\begin{aligned}
\frac LC
&\le L\left(\frac KC-9\right)\\
&=L\left(\frac{r^2}{n(n-1)}-9\right)\\
&<\frac{(6\alpha+\alpha^2/L)n+9L}{n-1}.
\end{aligned}
\tag{10}
\]

The finite-n corrections are retained explicitly. First, (5) gives

\[
\frac{\alpha^2}{L}<\frac{\alpha^2}{600\lambda}
<\frac{257}{500000}.
\tag{11}
\]

The margin in the last comparison is exactly
`12799/16503500000`. Second,

\[
9L<\frac n{10^6},\qquad
\frac n{n-1}<\frac{1000001}{1000000}.
\tag{12}
\]

For the first inequality, `log n/n` decreases for n>e and
`log N0<420`; the sufficient endpoint comparison is
`2^600>9*420*10^6`. The second follows directly from n>1000001.
Both are exact integer comparisons.

Combine (10)-(12) with `C<=6delta`. This proves, **in this high-n
range**,

\[
L<\beta\delta,
\qquad
\beta=
6\left(6\alpha+\frac{257}{500000}+\frac1{10^6}\right)
\frac{1000001}{1000000}
=\frac{1663510663509}{10^{11}}.
\tag{13}
\]

The required comparison is exact:

\[
24\lambda-\beta=\frac{42136491}{10^{11}}>0.
\]

Since lambda<log2, (13) implies `log n<24delta log2`, and hence
`n<2^(24delta)` whenever n>=N0. No cancellation of C or K modulo
another integer is used; the sole discrete step is K-9C>=1.

## 5. The entire lower range and the global conclusion

If n<N0, the inherited delta>=25 gives directly

\[
n<2^{600}\le2^{24\delta}.
\]

Together with Section 4, this proves (2) for all original solutions
in the branch. The auxiliary bound `log n<beta delta` in (13) is
**not** asserted for this lower range. The parent note's global
`log n<17delta` is a separate, already proved statement.

Relative to the old binary height `2^(42delta)`, the new height uses
24 instead of 42 bits per unit of delta. This reduces that certified
exponent domain by `18/42=3/7`. It is not a measured runtime improvement,
and it does not bound delta above. The already saved finite certificates
for delta<=24 retain their original domains; none is rewritten here.

## 6. Verification and dependencies

Run

```sh
python v20_binary_height_24.py
```

The checker uses the Python standard library only. It checks the six
integral-series terms, all rational margins, the logarithmic expansion
in (9) as a polynomial identity with formal log symbols, the
finite-n identity in (10) after clearing denominators, and the large
threshold comparisons as exact integers. Its report is
`v20_binary_height_24.json`.

The universal arguments are the written integral inequalities,
monotonicity proofs, binomial-row comparison, and two-range split.
Finite numerical samples are not used to prove them. Mathematical
inputs are the recorded offset-three reductions, the exact-defect
definition, and v19's complete delta<=24 exclusion. This appendix
does not solve the unbounded-defect branch or the full original
four-variable equation.
