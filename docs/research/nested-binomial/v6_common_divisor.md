# A second common divisor and complete exclusion when i-1 is squarefree

## Scope

The original equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns ell=1 and j=i-3. Write

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
L=\binom Ar,\quad X=\binom{n^2}{(n-3)^2},\quad Y=k^2.
\]

Both outer branches k=r and k=A-r are included. Previous endpoint
and small-index results, and v5_offset_three_structure.md, give

\[
n\ge104,\qquad 3n<r<10n/3,\qquad L=X+Y.
\tag{1}
\]

The new conclusion is uniform:

\[
\boxed{\ell=1,\quad j=i-3,\quad i-1\text{ squarefree}
\quad\Longrightarrow\quad\text{no solution}.}
\tag{2}
\]

The proof has one small residual calculation, n=250, derived by
divisibility and a list of exponents at most three. No arbitrary
upper-index search bound is used.

## 1. Any common divisor of A and X divides r cubed

More generally, if D divides both A and X and C(A,k)=X+k^2, then

\[
\boxed{D\mid r^3.}
\tag{3}
\]

Indeed A divides r C(A,r), by the identity
r C(A,r)=A C(A-1,r-1). Hence D divides r(X+k^2), so D divides
r k^2. Since k=r or k=A-r and D divides A, we have k=+/-r
modulo D, proving (3).

In particular the condition can use D=gcd(A,X); it is not limited
to the previously used divisor n/gcd(n,3).

## 2. A new divisor coming from n-1

Set

\[
q_0=\frac n{\gcd(n,3)},\qquad
q_1=\frac{n-1}{\gcd(n-1,6)}.
\]

The previous proof gives q_0|A and q_0^2|X. We now prove
q_1|A and q_1|X.

The first assertion follows immediately from
6A=n(n-1)(n-2): since n-1 divides 6A,
(n-1)/gcd(n-1,6) divides A.

For the second, put t=n-1, N=n^2=(t+1)^2, and
m=(n-3)^2=(t-2)^2. The choose-pair identity is

\[
\binom N2\binom{N-2}{m-2}=\binom m2\binom Nm.
\tag{4}
\]

First,

\[
\binom N2
=t\,\frac{(t+1)^2(t+2)}2
\]

is divisible by t; the displayed half-factor is an integer, since
either t+1 or t+2 is even. Second,

\[
\binom m2-6
=\frac t2\left(t^3-8t^2+23t-28\right).
\tag{5}
\]

The bracket in (5) is even for every integer t, because
t^3+23t is even and its remaining terms are even. Thus
C(m,2)=6 modulo t. Equation (4) implies t|6X, and therefore
q_1|X.

The integers q_0 and q_1 are coprime, being divisors of consecutive
integers n and n-1. Consequently

\[
\boxed{
Q:=\frac n{\gcd(n,3)}
   \frac{n-1}{\gcd(n-1,6)}
\ \mid A,\qquad Q\mid X,\qquad Q\mid r^3.
}
\tag{6}
\]

The additional factor has size comparable to n; it can impose
substantially more divisibility than q_0 alone.

## 3. Squarefree n-1 leaves only four short cases

Suppose n-1 is squarefree. Define

\[
d=\gcd(n-1,6)\in\{1,2,3,6\},\qquad
s=\frac{n-1}{d},
\]

and

\[
c=c_3(q_0):=\prod_{p\mid q_0}p^{\lceil v_p(q_0)/3\rceil}.
\]

Because s is squarefree, (6) implies s|r. Also c|r. The integers
c and s are coprime, because c|n and s|n-1.

Write r=ts. Then c|t, and the strict interval in (1) gives

\[
3d+\frac3s<t<\frac{10d}3+\frac{10}{3s}.
\tag{7}
\]

Since n>=104 and d<=6, one has s>17. The entire integer list
permitted by (7) is therefore

| d | Possible t |
|---:|---|
| 1 | none |
| 2 | none |
| 3 | 10 |
| 6 | 19 or 20 |

We now eliminate the last three entries.

### 3.1 d=3 and t=10

In this case n is even and n=1 modulo 3, so q_0=n.
Since c_3(n)|10, the prime factorization of n must have the form

\[
n=2^a5^b,\qquad 1\le a\le3,\qquad0\le b\le3.
\tag{8}
\]

The congruence n=1 modulo 3 says that a+b is even.
If b<=1 then n<=40, contradicting n>=104.
If b=2, the parity condition forces a=2 and n=100, also too small.
If b=3 then a=1 or 3, leaving only

\[
n=250\quad\text{or}\quad n=1000.
\]

But 1000-1=999 is divisible by 9, contrary to squarefreeness.

For n=250 we have

\[
s=83,\quad r=830,\quad
A=\binom{250}3=2573000=83\cdot31000,
\qquad31000\equiv41\pmod{83}.
\]

Lucas' theorem gives

\[
L=\binom{83\cdot31000}{83\cdot10}
\equiv\binom{31000}{10}
\equiv\binom{41}{10}\not\equiv0\pmod{83}.
\tag{9}
\]

The final binomial is nonzero modulo 83 because every factor in
its numerator and denominator is smaller than 83.
On the other hand 83|X by (6). Both k=r and k=A-r are divisible
by 83, so 83|Y. Thus L=X+Y contradicts (9).

### 3.2 d=6 and t=19

Again n=1 modulo 3, so q_0=n. The condition c_3(n)|19 forces

\[
n=19^a,\qquad1\le a\le3.
\]

Since 19=1 modulo 9, every such n has 9|n-1. This contradicts
the assumption that n-1 is squarefree.

### 3.3 d=6 and t=20

Here n is odd. The condition c_3(n)|20 permits only the primes
2 and 5 in n, and oddness removes 2. Hence

\[
n=5^b,\qquad1\le b\le3.
\]

But 5=1 modulo 4, so every such n has 4|n-1, again a contradiction.

All cases have been eliminated, proving (2).

## 4. Consequences and verification scope

Together with the previous v5 theorem, a hypothetical solution in
this offset-three family must satisfy both:

- n/gcd(n,3) has a repeated prime factor;
- n-1 has a repeated prime factor.

This does not exclude every such pair of adjacent integers.
The full original equation remains unsolved.

The general common-divisor implication (3) is formalized in the
v6 Lean source. The new choose-pair divisibility argument and the
squarefree n-1 case analysis are written mathematical proofs;
no full Lean formalization of (2) is claimed.

The author of v6_offset_composite.md independently audited (4)-(9),
the integrality in (5), the coprimality step, all interval endpoints,
and the exponent cases, and found no correction necessary.
The small companion script performs an exact check of the exceptional
n=250 calculation and several sample common-divisor identities; those
samples do not replace the uniform proof above.
