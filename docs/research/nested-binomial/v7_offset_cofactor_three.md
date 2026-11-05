# Offset three: complete exclusion of 3 p^a + 2 for p other than 3

## Theorem and scope

For the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

the following entire infinite family is impossible:

\[
\boxed{\ell=1,\qquad j=i-3,\qquad
i=3p^a+2,\quad p\text{ prime},\quad p\ne3,\quad a\ge1.}
\tag{1}
\]

Both branches of the outer binomial are included. The excluded
base \(p=3\) is exactly the separate shifted-power family
\(i=3^{a+1}+2\), for which `v7_offset_shifted_prime_powers.md`
gives necessary conditions; that family is not claimed to be
completely excluded.

The proof below reduces an unbounded family to 40 primes and 16
additional prime-exponent pairs. These finite remainders are derived
from proved bounds, and are all eliminated by short factorizations
of explicit divisors. There is no scan of the original equation.

## 1. Notation and established inputs

Write

\[
q=p^a,\quad n=3q+2,\quad
A=\binom n3=qT,\qquad T=\frac{(3q+2)(3q+1)}2,
\]

\[
r=\min(k,A-k),\quad L=\binom Ar,\quad
X=\binom{n^2}{6n-9},\quad Y=k^2.
\]

The prior small-index theorem and offset-three gap give

\[
n\ge104,\qquad 3n<r<10n/3.
\tag{2}
\]

The common-divisor theorem in `v6_common_divisor.md` gives

\[
\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{3}
\]

Since \(n\equiv2\pmod3\), (3) in particular implies

\[
\boxed{H:=\frac{n(n-1)}2\mid r^3.}
\tag{4}
\]

For odd \(p\), \(H\) is exactly the divisor in (3); for \(p=2\),
it is half that divisor. In all large cases used below,
\(\gcd(H,p)=1\): for \(p\ge5\), reduce \(n,n-1\) modulo \(p\);
for \(p=2\), \(a\ge2\) makes \(n/2=3\cdot2^{a-1}+1\) odd.

We also use the proved logarithmic gap in `v6_offset_composite.md`:

\[
n\ge1024\quad\Longrightarrow\quad
r<3n+\frac{3n}{4\log n}<\frac{25n}{8}.
\tag{5}
\]

The last inequality follows from \(\log1024>6\).
Previously, squarefree \(n/\gcd(n,3)\) was completely excluded.

## 2. Removing the small first indices

For \(p\ge19\), all exponents \(a=1\) are excluded by
`v7_offset_dominant_prime.md`, because \(n-2=3p\) and \(p>18\).
Every \(a\ge2\) in this range has \(n\ge1085\).

For \(p\in\{2,5,7,11,13,17\}\), the values with
\(104\le n<1024\) are exactly the following eight:

| p | a | n | Factorization of n |
|---:|---:|---:|---|
| 2 | 6 | 194 | 2 * 97 |
| 2 | 7 | 386 | 2 * 193 |
| 2 | 8 | 770 | 2 * 5 * 7 * 11 |
| 5 | 3 | 377 | 13 * 29 |
| 7 | 2 | 149 | prime |
| 11 | 2 | 365 | 5 * 73 |
| 13 | 2 | 509 | prime |
| 17 | 2 | 869 | 11 * 79 |

They are squarefree, and \(3\nmid n\), so all are already
excluded. Values below 104 are covered by the earlier small-index
theorem. Hence it remains to consider \(n\ge1024\), or \(q\ge341\).

From (2) and (5),

\[
9q+6<r<\frac{25(3q+2)}8<10q.
\tag{6}
\]

The final inequality holds for \(q>10\). Thus
\(r=9q+u\), with \(6<u<q\). In particular

\[
d:=v_p(r)<a=v_p(A),\qquad v_p(Y)=2d
\tag{7}
\]

for either \(k=r\) or \(k=A-r\).

## 3. Exact valuation of X

The digit blocks are

\[
n^2=q(9q+12)+4,\qquad 6n-9=18q+3,
\qquad n^2-(6n-9)=q(9q-6)+1.
\]

Legendre's formula, separating terms at \(p^a=q\), gives

\[
v_p(X)=v_p\binom43+v_p\binom{9q+12}{18}.
\tag{8}
\]

In the second numerator product, the offsets from \(9q\) run
from \(-5\) through 12. Because \(q\ge341\) and \(p\ne3\),
each nonzero offset has valuation below \(a\), and the central
factor has valuation \(a\). Therefore

\[
v_p\binom{9q+12}{18}
=a-v_p\left(6\binom{18}{6}\right).
\]

Here

\[
6\binom{18}{6}=2^3\,3^2\,7\,13\,17.
\]

Since \(v_p\binom43=2\) for \(p=2\) and is zero otherwise,

\[
\boxed{v_p(X)=
\begin{cases}
a,&p=5,11\text{ or }p\ge19,\\
a-1,&p=2,7,13,17.
\end{cases}}
\tag{9}
\]

## 4. Exact valuation of the outer binomial

The bottom \(a\) base-\(p\) digits of \(A-1=qT-1\) are all
\(p-1\). By (6), the corresponding upper block of \(r-1\) is
9. Another application of Legendre's formula gives

\[
v_p\binom{A-1}{r-1}=v_p\binom{T-1}{9}.
\tag{10}
\]

Now

\[
T-1=\frac{9q(q+1)}2.
\]

Its valuation is \(a\) for odd \(p\ne3\), and \(a-1\) for
\(p=2\). In either case the corresponding prime power is greater
than 8. Hence \(\binom{T-2}{8}\) is a \(p\)-adic unit: the lower
digits of \(T-2=(T-1)-1\) are all \(p-1\) through all positions
occupied by 8. Using
\(\binom{T-1}{9}=(T-1)\binom{T-2}{8}/9\) gives

\[
v_p\binom{T-1}{9}=
\begin{cases}a,&p\ge5,\\a-1,&p=2.\end{cases}
\]

Finally \(rL=A\binom{A-1}{r-1}\) proves

\[
\boxed{v_p(L)=
\begin{cases}2a-d,&p\ge5,\\2a-1-d,&p=2.\end{cases}}
\tag{11}
\]

## 5. Comparing the valuations forces cancellation

If two integer summands have unequal \(p\)-adic valuations, their
sum has the smaller valuation. Apply this to \(L=X+Y\), using
(7), (9), and (11).

For \(p=5,11\) or \(p\ge19\), if \(2d<a\), equality would
give \(2a-d=2d\), or \(d=2a/3\), inconsistent with \(2d<a\).
If \(2d>a\), it would give \(d=a\), inconsistent with (7).
Thus \(2d=a\).

For \(p=7,13,17\), if \(2d<a-1\), equality similarly gives
\(d=2a/3\), which is impossible. If \(2d>a-1\), it gives
\(d=a+1\), also impossible. Thus \(2d=a-1\).

For \(p=2\), the first unequal case would give
\(3d=2a-1\), incompatible with \(2d<a-1\); the second would
give \(d=a\), again impossible. Thus \(2d=a-1\).

Consequently every remaining candidate satisfies

| Primes | Exponent parity | Exact valuation d = v_p(r) |
|---|---|---|
| 5, 11, and all p >= 19 | a even | a/2 |
| 2, 7, 13, 17 | a odd | (a-1)/2 |

## 6. A uniform numerical bound makes the remainder finite

By (4) and \(\gcd(H,p)=1\), \(H\mid(r/p^d)^3\). Thus

\[
p^{3d-a}
<\frac{2000}{27}\frac{(3q+2)^2}{q(3q+1)}<223
\qquad(q\ge341).
\tag{12}
\]

The first inequality uses \(r<10n/3\). For the second, clearing
positive denominators leaves

\[
63q^2-17979q-8000>0.
\]

At \(q=341\) this is \(1186864>0\), and its derivative
\(126q-17979\) is positive for \(q\ge341\).

For \(p\ge19\), the even exponent therefore satisfies
\(p^{a/2}<223\). Since \(19^2>223\), necessarily

\[
a=2,\qquad19\le p<223.
\tag{13}
\]

There are exactly 40 primes in this interval.

For the six smaller bases, (12), parity, and \(3p^a+2\ge1024\)
leave exactly the following 16 pairs:

| p | Remaining a |
|---:|---|
| 2 | 9, 11, 13, 15, 17 |
| 5 | 4, 6 |
| 7 | 3, 5, 7 |
| 11 | 4 |
| 13 | 3, 5, 7 |
| 17 | 3, 5 |

For example, the powers to bound are \(p^{a/2}\) in the first
row of the preceding parity table and \(p^{(a-3)/2}\) in the
second. This proves completeness of the finite remainder.

## 7. Explicit squarefree-divisor certificates close every case

If a squarefree positive integer \(D\) divides \(H\), then
\(H\mid(r/p^d)^3\) implies \(D\mid r/p^d\). Consequently

\[
\boxed{D\mid H,\quad D\text{ squarefree},\quad
3p^dD\ge10n\quad\Longrightarrow\quad\text{contradiction}.}
\tag{14}
\]

This requires only a factorization of \(D\) into distinct primes,
an integer divisibility check, and an integer inequality.

For the 40 primes in (13), we can use an even simpler bound:
(6) gives \(r/p<10p\). Take \(D=\operatorname{rad}(n)\),
the product of its distinct prime factors, except for \(p=71\).
All 39 such divisors satisfy \(D>10p\). For \(p=71\), use

\[
n=15125=5^3\,11^2,\qquad
D=(n-1)/2=7562=2\cdot19\cdot199>710.
\]

For the 16 small-base pairs, take \(D=\operatorname{rad}(n)\)
for odd \(p\), and \(D=\operatorname{rad}(n)/2\) for \(p=2\).
They all satisfy (14). The certificate records their full
factorizations and inequalities, rather than assuming primality
from a probabilistic test.

`v7_offset_cofactor_three_checks.py` generates the 56 certificates
and then verifies them independently. The verifier reconstructs the
complete domains from (12)-(13), checks every claimed prime by
deterministic trial division, checks that the listed distinct primes
multiply to \(D\), and checks \(D\mid H\) and the relevant strict
upper-gap contradiction. It also checks all eight small-index
factorizations in Section 2 and the constants in the companion
dominant-prime proof.

This completes the proof of (1).

## 8. Reproduction and verification scope

Run

    python3 v7_offset_cofactor_three_checks.py

The generated artifacts are `v7_offset_cofactor_three_certificates.json`
and `v7_offset_cofactor_three_verification.json`. The script additionally
checks representative instances of the valuation identities using
Legendre sums; these checks corroborate Sections 3-4 and are not a
substitute for their uniform proofs.

This is a complete exclusion of the stated infinite family, not a
complete solution of every offset-three case or of the full original
equation. The new proof has not been formalized in Lean.
