# v16: a simultaneous family of quadratic-neighbor obstructions

Date: 2026-11-06 JST.

This is a written proof with exact supporting checks. It is not a new
Lean proof or a DeepSeek API result. No existing formal proof body is
changed. The original four-variable equation remains unresolved.

## 1. Scope and main statement

Keep the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

and restrict to the established branch ell=1, j=i-3. Write

\[
n=i,\quad A=\binom n3,\quad m=6n-9,\quad
B=\binom{n^2}{m},\quad r=\min(k,A-k).
\]

Both k=r and k=A-r are included. The branch inputs from
`v6_offset_composite.md` are

\[
n\ge104,\qquad 3n<r<10n/3,\qquad
Q=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{1}
\]

For n>=1024 the existing logarithmic refinement is

\[
r<3n+\frac{3n}{4\log n}.
\tag{2}
\]

Let P+(u) denote the largest prime divisor of a positive integer u>1.

**Theorem.** Let c be any integer with 0<=c<=16 such that

\[
\boxed{6\mid(c+2)n-3c.}
\tag{3}
\]

Then every solution in the branch satisfies

\[
\boxed{P^+(n^2-c)<r<10n/3.}
\tag{4}
\]

For n>=1024, (2) gives the sharper upper bound

\[
\boxed{P^+(n^2-c)<3n+\frac{3n}{4\log n}.}
\tag{5}
\]

The most useful uniform specialization is **c=10**, for which (3)
holds for every integer n. Consequently

\[
\boxed{P^+(n^2-10)<r}
\tag{6}
\]

is necessary throughout the branch, with no residue restriction on n,
no upper bound on n or H, and no enumeration of primes.

The proof of P+(n^2-c)<=r uses only the size bounds in (1) and the
original equation. The strict inequality in (4) additionally uses
Q|r^3. These are bounds on **prime divisors**, not on their full exact
prime powers. A separate prime-power theorem would require additional
argument. Such an argument, with its own complete exceptional-case
analysis, is given in [v16_repeated_neighbor_primes.md](v16_repeated_neighbor_primes.md).

## 2. A small residue for the outer upper index

Under (3) define the integer

\[
a=\frac{(c+2)n-3c}{6}.
\tag{7}
\]

Because n>=104 and 0<=c<=16, this expression increases with c and

\[
0<n/3\le a\le3n-8<r.
\tag{8}
\]

The exact polynomial identity is

\[
\boxed{A-a=\frac{(n-3)(n^2-c)}6.}
\tag{9}
\]

For c=10 it becomes the particularly simple identity

\[
A-(2n-5)=\frac{(n-3)(n^2-10)}6.
\tag{10}
\]

Suppose p is a prime divisor of n^2-c with p>r. Then p>3n>3, so 6
is invertible modulo p. Equations (8)-(9) show that A mod p=a and
0<a<r<p. Therefore

\[
\binom Ar\equiv\binom ar=0\pmod p.
\tag{11}
\]

One can obtain (11) directly from the falling-factorial formula,
since r! is a p-unit and one numerator factor is A-a.

Also k is not divisible by p in either branch: for k=r it is the
integer 0<r<p; for k=A-r its residue is a-r, strictly between -p and 0.

## 3. The inner binomial also vanishes, including primes below m

We must prove

\[
\boxed{B\equiv0\pmod p}
\tag{12}
\]

under p>r. It is not enough to assume p>m, because r<m. The narrow
possible exception for r<p<=m is removed below.

As p>r>3n, we have m=6n-9<2p. Also c<p and n^2 mod p=c. Lucas'
formula gives a zero residue whenever the low base-p digit of m is
greater than c. If p>m, that digit is m>c, proving (12).

If p<=m, the low digit is m-p. The only way it can fail to exceed c
is

\[
p=m-t=6n-9-t,\qquad0\le t\le c\le16.
\tag{13}
\]

Since p and m are odd, t is even. From p|n^2-c and 6n=0+9+t modulo p,

\[
p\mid D_{c,t}:=(9+t)^2-36c.
\tag{14}
\]

But t even implies D_(c,t)=1 modulo 4, so this integer is nonzero.
The bounds 0<=t<=c<=16 give

\[
-495=81-36\cdot16\le D_{c,t}
\le(c-9)^2\le81.
\tag{15}
\]

Meanwhile (13) and n>=104 give

\[
p\ge6n-25\ge599>|D_{c,t}|.
\]

This contradicts (14). Thus the exceptional interval contains no such
prime, and (12) holds for every p>r.

For completeness, the part of Lucas' formula used here follows by
writing N in base p and expanding
(1+x)^N=product_j (1+x^(p^j))^(N_j) modulo p. Comparing coefficients
gives binom(N,M)=product_j binom(N_j,M_j) modulo p. If one lower digit
exceeds its upper digit, that product is zero.

## 4. Contradiction in both branches and the endpoint p=r

Equations (11)-(12) and the original equation imply

\[
0\equiv0+k^2\pmod p,
\]

contradicting the nonzero residue of k proved in Section 2. Therefore
every prime divisor of n^2-c is at most r.

To make the bound strict, suppose r itself were prime. Since r>3n,
every prime factor of Q divides n(n-1) and is strictly smaller than r.
Thus gcd(Q,r)=1. But Q|r^3 and Q>=n(n-1)/6>1, a contradiction.
Consequently r is not prime, and no prime divisor can equal r.

The endpoint exclusion uses the old common-divisor condition; it does
not incorrectly apply the r<p digit argument when r=p.

## 5. Exact residue classification and simultaneous conditions

Condition (3) depends only on n modulo 6. The full classification is:

| n mod 6 | All c in 0..16 satisfying (3) |
|---:|---|
| 0 | 0,2,4,6,8,10,12,14,16 |
| 1 | 1,4,7,10,13,16 |
| 2 | 4,10,16 |
| 3 | 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 |
| 4 | 4,10,16 |
| 5 | 1,4,7,10,13,16 |

If c is a square (0,1,4,9,16), the size restriction follows already
from n^2-c=(n-sqrt(c))(n+sqrt(c)); all prime divisors are <=n+4<r.
Thus the genuinely additional quadratic conditions supplied here are:

| n mod 6 | Nonsquare c whose n^2-c must satisfy P+(n^2-c)<r |
|---:|---|
| 0 | 2,6,8,10,12,14 |
| 1 or 5 | 7,10,13 |
| 2 or 4 | 10 |
| 3 | 2,3,5,6,7,8,10,11,12,13,14,15 |

These conditions hold simultaneously for each candidate n in its row.
In particular the c=10 condition is present in every row. They impose
additional factorization restrictions, not a proof that no integer can
satisfy all of them.

For any listed c and any prime p|n^2-c, put w=(n^2-c)/p. From p<10n/3,

\[
3n-10w<3c/n<1.
\]

Both 3n and 10w are integers, so

\[
\boxed{3n\le10w.}
\tag{16}
\]

This gives a linear cofactor bound, again for any prime divisor.
For c=10 it follows, for example, that
(n^2-10)/gcd(n^2-10,6) must be composite: if this quotient were a
prime p, its cofactor w would be <=6, contradicting (16) and n>=104.
No assertion about infinitude of prime values of any polynomial is made.

## 6. A separate positive neighbor: n^2+1 for n=3 modulo 6

When n=3 modulo 6, put a=(n+3)/6. The same identity with c=-1 gives

\[
A-a=\frac{(n-3)(n^2+1)}6.
\]

Suppose a prime p|n^2+1 satisfies p>m. Then 0<a<r<p and the outer
binomial is zero modulo p, while

\[
B\equiv\binom{-1}{m}=(-1)^m=-1\pmod p.
\]

The original equation requires k^2=1 modulo p. In the two branches,
k is congruent to r or -(r-a). Both positive integers r and r-a lie
strictly between 1 and p-1, by n>=104 and r<10n/3<m-1. Neither can
be congruent to 1 or -1 modulo p, a contradiction. Therefore

\[
\boxed{P^+(n^2+1)\le6n-9\qquad(n=3\pmod6).}
\tag{17}
\]

This argument deliberately requires p>m. It does not claim the
stronger P+(n^2+1)<r. For n odd, n^2+1 is automatically even, but
(17) additionally excludes (n^2+1)/2 being prime in this residue class:
the latter quotient is greater than 6n-9 for n>=104.

## 7. Supporting checks and limits

`v16_quadratic_neighbors_checks.py` checks the six residue classes,
all 81 parity-compatible constants D_(c,t), the exact polynomial
identity, and modular obstructions for explicit small samples. Selected
samples are also checked by constructing the actual binomial integers.
The script records the note and source hashes in its JSON output.

The finite samples are consistency checks of the written uniform proof;
they are not a finite-range proof, and they are not solutions of the
original equation. The scope remains ell=1,j=i-3 with both k choices.
No new Lean execution, DeepSeek API call, complete CAS solver, or
external peer review is claimed.
