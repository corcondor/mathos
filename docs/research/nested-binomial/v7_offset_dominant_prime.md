# Offset three: excluding a dominant prime factor of n-2

## Scope and prior inputs

We retain the squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

and restrict to \(\ell=1,j=i-3\). Put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
X=\binom{n^2}{6n-9}.
\]

Both \(k=r\) and \(k=A-r\) are included. The previous notes prove

\[
n\ge104,\qquad 3n<r<10n/3,
\]

\[
Q=\frac n{g}\frac{n-1}{d_0}\mid r^3,
\qquad g=\gcd(n,3),\quad d_0=\gcd(n-1,6),\quad gd_0\mid6.
\tag{1}
\]

They also exclude every \(n\) for which \(n/g\) is squarefree.
For any common divisor \(D\mid A,X\), the original equation implies
\(D\mid r^3\). These inputs are in `v5_offset_three_structure.md`
and `v6_common_divisor.md`.

**Theorem.** No solution in this family has

\[
\boxed{n-2=wp,\qquad p\text{ prime},\quad p>6w.}
\tag{2}
\]

Equivalently, writing \(P^+(m)\) for the greatest prime factor of
\(m>1\), every remaining solution must satisfy

\[
\boxed{P^+(n-2)^2\le6(n-2).}
\tag{3}
\]

## 1. A prime-power divisor shared by A and X

More generally let \(n=wp^a+2\), with \(p\) prime and \(p>6w\).
Write \(q=p^a\). Then \(p\ge7\), \(p\nmid w\), and

\[
v_p(A)=a.
\tag{4}
\]

For the squared-index binomial, split base-\(p\) digits after the
bottom \(a\) positions:

\[
n^2=q(qw^2+4w)+4,\quad 6n-9=6wq+3,
\quad n^2-(6n-9)=q(qw^2-2w)+1.
\]

There is no borrow between these blocks, and the bottom block
\(\binom43\) is a \(p\)-adic unit. Legendre's factorial-valuation
formula gives

\[
v_p(X)=v_p\binom{qw^2+4w}{6w}=a.
\tag{5}
\]

Indeed, in the last numerator product the offsets from \(qw^2\)
range from \(-2w+1\) to \(4w\). Only the central factor is
divisible by \(p\), and its valuation is \(a\); the denominator
\((6w)!\) is prime to \(p\).

The common-divisor lemma now implies
\(p^{\lceil a/3\rceil}\mid r\). Moreover \(p\nmid Q\), since
\(n\equiv2\pmod p\) and \(n-1\equiv1\pmod p\).
If \(s=\lceil a/3\rceil\), (1) consequently implies

\[
Q\mid(r/p^s)^3.
\]

Using \(Q\ge n(n-1)/6\) and the upper gap gives

\[
p^{3s}<\frac{2000}{9}\frac{n^2}{n-1}.
\tag{6}
\]

## 2. All sufficiently large primes when a is 1 modulo 3

Suppose \(a\equiv1\pmod3\). Since \(3s=a+2\), (6) becomes

\[
\frac{p^2}{w+2/p^a}
<\frac{2000}{9}\frac n{n-1}
\le\frac{208000}{927}.
\tag{7}
\]

On the other hand, \(w\le(p-1)/6\) and \(a\ge1\) give

\[
\frac{p^2}{w+2/p^a}
\ge\frac{6p^3}{p^2-p+12}.
\tag{8}
\]

The last function is strictly increasing for positive real \(p\):
its derivative has the sign of
\(p^2(p^2-2p+36)>0\). At \(p=37\), its value is

\[
\frac{50653}{224}>\frac{208000}{927}.
\]

Thus we have also proved the uniform extension

\[
\boxed{p\ge37,\quad p>6w,\quad a\equiv1\pmod3
\quad\Longrightarrow\quad\text{no solution}.}
\tag{9}
\]

## 3. Completing a=1

For (2) we set \(a=1\). It remains only to consider \(p\le31\).
If \(p\le23\), then \(w\le3\), so \(n=wp+2\le71\), already
excluded. For \(p=29,31\), the conditions \(p>6w\) and
\(n\ge104\) leave precisely

| p | w | n | n/gcd(n,3) |
|---:|---:|---:|---:|
| 29 | 4 | 118 | 118 = 2 * 59 |
| 31 | 4 | 126 | 42 = 2 * 3 * 7 |
| 31 | 5 | 157 | 157, prime |

The last column is squarefree in every case, so all are excluded
by the earlier squarefree theorem. This proves (2).

Finally, if a prime \(p\mid n-2\) satisfies \(p^2>6(n-2)\),
putting \(w=(n-2)/p\) gives \(p>6w\), contradicting (2).
This proves (3). Notice that \(p>6w\) itself forces
\(v_p(n-2)=1\); there is no missing higher-power case in this
equivalence.

## 4. Verification and limits

The exact rational comparisons and the three residual factorizations
are checked by `v7_offset_cofactor_three_checks.py`. The argument is
a uniform divisibility proof, followed by three explicitly derived
integers, and does not scan a chosen interval of first indices.
It concerns only \(\ell=1,j=i-3\), and does not solve the full
original equation. No Lean formalization is claimed here.
