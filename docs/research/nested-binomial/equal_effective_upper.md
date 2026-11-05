# Equal effective lower indices are excluded in the upper branch

Consider the squared-argument equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

Write \(A=\binom ij\), \(B=\binom{k}{\ell}\),
\(X=\binom{i^2}{j^2}\), \(Y=\binom{k^2}{\ell^2}\),
\(t=A-B\), and \(M=\max(j,\ell)\).
The upper branch means \(0<t\le B\).

The established prerequisites are:

\[
1\le j\le i-2,\quad 1\le\ell\le k-2,\quad
M\ge21,\quad M+2\le t<10M.
\]

Here \(\ell=k-1\) is excluded in this branch by
\(t\ge M+2>B=k\), and \(M\le20\) was excluded by the prior
complete certificate. The previously proved exclusions of \(j=\ell\)
and \(i-j=k-\ell\) are also used.

## Theorem

There is no solution in the upper branch with

\[
\boxed{\min(j,i-j)=\min(\ell,k-\ell).}
\]

This covers both choices of orientation of each inner binomial coefficient.
It strengthens the previous separate exclusions of equal lower indices
and equal complements.

## 1. A common effective index of at least three

Let the common effective index be \(d\). Then
\(A=\binom id>B=\binom kd\), hence \(i>k\ge2d\).
If \(d\ge3\), then \(M\le i-d\), so \(i\ge24\), and Pascal's identity gives

\[
t\ge\binom{i-1}{d-1}\ge\binom{i-1}{2}>10i>10M.
\]

The middle inequality uses \(2\le d-1\le(i-1)/2\). The strict numerical
inequality holds at \(i=24\) and thereafter: its difference from \(10i\)
is \((i^2-23i+2)/2>0\). This contradicts the gap bound.

For \(d=1\), the endpoint exclusions in this branch force \(j=\ell=1\),
already impossible. Thus only \(d=2\) remains.

## 2. The four orientations for effective index two

The cases \((j,\ell)=(2,2)\) and \((j,\ell)=(i-2,k-2)\) were already
excluded. The crossed cases are handled below.

### 2.1 First lower index large: \(j=i-2,\ \ell=2\)

Put \(i=n\), \(k=n-s\), with \(n\ge23\), \(s\ge1\), and \(k\ge4\).
Then

\[
A=\frac{n(n-1)}2,\qquad
t=\frac{s(2n-s-1)}2,\qquad
X=\binom{n^2}{4n-4},\qquad Y=\binom{k^2}{4}.
\]

For \(n\ge23\), unimodality gives \(Y<X\).
If \(s\le4\), then
\(t\le4n-10<4n-4\le n^2/2\), whence
\(\binom At<\binom{n^2}{4n-4}=X\).

For \(s\ge5\) and \(n\ge256\), the exact analytic comparison proved
in Section 3.1 of `continuation_arithmetic.md` applies unchanged:

\[
\binom At\ge\binom A{5n-15}>2\binom{n^2}{4n-4}=2X>X+Y.
\]

That comparison used only the displayed formulas for \(A,t,X\) and
the upper-branch condition \(t\le A/2\); its final use of the other
summand needs only \(Y<X\), which was checked here.
Consequently the proved remaining interval is \(23\le n\le255\).

### 2.2 Second lower index large: \(j=2,\ \ell=k-2\)

Put \(k=n\), \(i=n+s\). Now \(n\ge23\), and

\[
A=\frac{(n+s)(n+s-1)}2,\quad
B=\frac{n(n-1)}2,\quad
t=sn+\frac{s(s-1)}2,
\]

\[
X=\binom{(n+s)^2}{4},\qquad Y=\binom{n^2}{4n-4}.
\]

Since \(sn\le t<10(n-2)\), we have \(1\le s\le9\).
Also \(t\le B\) implies \(A\le2B<n^2\).

Set \(N=n^2\) and \(q=4n-4\). If \(s\le3\), then
\(t\le3n+3<q\le N/2\), so \(\binom At<Y\).

If \(s=4\), then \(t=q+10\), and
\(A=(n+4)(n+3)/2<(2/3)N\) for every \(n\ge23\).
The product formulas give

\[
\frac{\binom A{q+10}}{\binom Nq}
\le\left(\frac AN\right)^q
\left(\frac A{q+1}\right)^{10}
<\left(\frac23\right)^{4n-4}n^{10}<1.
\]

The last inequality holds at \(n=23\) by the exact comparison
\(2^{88}23^{10}<3^{88}\). It persists as \(n\) increases because its
successive ratio is at most \(16\cdot24^{10}/(81\cdot23^{10})<1\).
Both integer comparisons are also checked by the accompanying script.

Finally suppose \(s\ge5\) and \(n\ge160\). Let

\[
A_0=\frac{(n+5)(n+4)}2,\qquad t_0=5n+10.
\]

Since \(A\ge A_0\), \(t\ge t_0\), and \(t\le A/2\),
\(\binom At\ge\binom{A_0}{t_0}\).
The elementary inequality \(\log(1-u)\ge-u/(1-u)\) gives

\[
\binom{A_0}{t_0}
\ge\frac{A_0^{t_0}}{t_0!}
\exp\!\left(-\frac{t_0(t_0-1)}{2(A_0-t_0+1)}\right).
\]

The exponent loss is

\[
\frac{(5n+10)(5n+9)}{n^2-n+2}<26
\quad(n\ge160),
\]

because the difference after clearing denominators is
\(n^2-121n-38>0\).
Using \(t_0-q=n+14\), \(t_0!/q!\le t_0^{n+14}\),
\(A_0/N>1/2\), and \(A_0/t_0>n/10\), we obtain

\[
\frac{\binom{A_0}{t_0}}{Y}
> e^{-26}2^{-4n+4}\left(\frac n{10}\right)^{n+14}
=e^{-26}2^{60}\left(\frac n{160}\right)^{n+14}>2.
\]

For the last step use \(e<3\) and the exact comparison \(2^{59}>3^{26}\).
Moreover, since \(s\le9\) and \(n\ge23\),

\[
Y\ge\binom{n^2}{8}
\ge\left(\frac{n^2}{8}\right)^8
>(n+9)^8>X.
\]

Thus \(\binom At>2Y>X+Y\), again a contradiction.
The proved remaining interval in this crossed orientation is
\(23\le n\le159\), \(1\le s\le9\).

## 3. Exact finite remainder

`verify_equal_effective_upper.py` enumerates precisely the finite intervals
just proved, retaining the necessary conditions
\(M+2\le t<10M\) and \(t\le B\). It evaluates both sides using exact
Python integers.

| Crossed orientation | Candidates | Left smaller | Left larger | Equalities |
|---|---:|---:|---:|---:|
| \(j=i-2,\ \ell=2\) | 2076 | 946 | 1130 | 0 |
| \(j=2,\ \ell=k-2\) | 1197 | 548 | 649 | 0 |

The executed output is `verification_equal_effective_upper.json`.
Combining the analytic ranges, these finite remainders, and the established
prerequisites proves the theorem for all upper indices, with no remaining
cutoff assumption.

## Scope

This is a new exclusion of an infinite parameter family. It does not
exclude all upper-branch solutions and does not settle the original
equation. The proof is written mathematics plus exact finite verification;
it has not been formalized in Lean.
