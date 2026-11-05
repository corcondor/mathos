# Offset three with ell=1: a strict gap, squarefree exclusion, and prime powers

## Setting and previously proved input

We retain the original squared-index equation. In this note

\[
i=n,\qquad j=n-3,\qquad \ell=1,\qquad
A=\binom n3,\quad B=k,\quad r=\min(B,A-B),
\]

\[
L=\binom Ar,\qquad
X=\binom{n^2}{6n-9},\qquad Y=B^2.
\]

Both outer branches are included: B=r and B=A-r.
The v4 complete exclusion of ell=1,j<=100 implies n>=104 for
every remaining solution. The endpoint reductions give 1<B<A
and r<=A/2. The Lean-checked divisibility lemma gives

\[
\boxed{q:=\frac n{\gcd(n,3)}\mid r^3.} \tag{1}
\]

No new finite cutoff is imposed on n in the main results below.

## 1. The second summand is smaller than X

For n>=104, 3<=6n-9<=n^2/2. Thus

\[
X\ge\binom{n^2}{3}>\binom n3^2=A^2>Y.
\]

For the middle comparison, cancel n^2 and compare
6(n^2-1)(n^2-2) with (n-1)^2(n-2)^2; each quadratic on the
left is already larger than its counterpart on the right.
Consequently every solution must have

\[
\boxed{X<L<2X.} \tag{2}
\]

## 2. A lower gap: r>3n

We prove the slightly stronger standalone inequality

\[
\boxed{\binom{\binom n3}{3n}<\binom{n^2}{6n-9}
\quad(n\ge64).} \tag{3}
\]

Put b=3n and N=n^2. Product bounds and AM--GM give

\[
\frac{\binom Ab}{\binom N{2b}}
\le\left(\frac{A(3b+1)}{2(N-2b+1)^2}\right)^b
=Q_n^{3n},
\]

where Q_n=A(9n+1)/(2(n^2-6n+1)^2). For n>=64,
Q_n<7/8. After clearing positive denominators this is equivalent
to positivity of

\[
6n^4-400n^3+1536n^2-512n+42.
\]

Writing n=64+u makes it

\[
6u^4+1136u^3+72192u^2+1572352u+2064426>0.
\]

The remaining ratio of binomials in row N satisfies

\[
\frac{\binom N{6n}}{\binom N{6n-9}}
\le\left(\frac{N}{6n-8}\right)^9
\le(n/5)^9.
\]

Therefore the ratio in (3) is smaller than
f(n)=(7/8)^(3n)(n/5)^9. At n=64,

\[
f(64)<\frac{3^{24}}{2^{18}5^9}
=\frac{282429536481}{512000000000}<1,
\]

using (7/8)^8<3/8. Moreover

\[
\frac{f(n+1)}{f(n)}
=\frac{343}{512}(1+1/n)^9
\le\frac{343}{512}\frac1{1-9/n}
\le\frac{343}{440}<1.
\]

The bound (1+x)^9<=1/(1-9x) for 0<=9x<1 follows by
bounding each binomial coefficient by 9 to the corresponding power.
This proves (3). Monotonicity of C(A,r) up to A/2, together with
(2), now proves r>3n for every remaining solution.

## 3. An upper gap: r<10n/3

Let b=ceil(10n/3), n>=104. We will prove

\[
\binom Ab>2X. \tag{4}
\]

First A>n^3/7 and b<7n/2, hence A>b^2, because 4n>343.
The elementary product inequality gives

\[
\binom Ab
=\frac{A^b}{b!}\prod_{s=0}^{b-1}(1-s/A)
>\frac{A^b}{2b!}.
\]

The integral comparison for log(b!) yields
b!<=e b(b/e)^b. Also A/b>n^2/22: since 3b<=10n+2,
this follows from n^2-35n+22>0. Using 8/3<e<3,

\[
\binom Ab>
\frac{(4n^2/33)^b}{6b}
\ge\frac{(4n^2/33)^{10n/3}}{6b}.
\tag{5}
\]

Write m=6n-9. The usual factorial integral bound gives
C(n^2,m)<(e n^2/m)^m. Since m>=11n/2 and e<11/4,

\[
X<(n/2)^{6n}. \tag{6}
\]

Combining (5)--(6), and 12b<42n, gives

\[
\frac{\binom Ab}{2X}>
\frac{\left[64(4/33)^{10/3}n^{2/3}\right]^n}{42n}.
\tag{7}
\]

The bracket is greater than 6/5 for n>=104. Cubing and clearing
denominators reduces the check at n=104 to the positive integer

\[
125\cdot2^{38}\cdot104^2-216\cdot33^{10}
=40813869371167016>0.
\]

Finally (6/5)^n/(42n)>1 for n>=104: it is increasing there,
and (6/5)^100>2^20>42*104, using (6/5)^5>2.
This proves (4). Since b<=A/2, (2) and monotonicity imply r<b,
and therefore r<10n/3.

The numerical bounds on e used above follow from its positive
factorial series. For example e>8/3, while
e<65/24+1/100<11/4, by summing through 1/4! and bounding the
remaining tail geometrically.

Together with Section 2, we have the uniform theorem

\[
\boxed{\ell=1,\quad j=i-3\quad\Longrightarrow\quad
3i<r<\frac{10i}{3}.} \tag{8}
\]

The small n values are already impossible by the earlier full j<=100
theorem; there is no unverified numerical remainder in (8).

## 4. Complete exclusion when q is squarefree

Suppose q=n/gcd(n,3) is squarefree. From (1), q|r.

If 3 does not divide n, then q=n, and the open interval
(3n,10n/3) contains no multiple of n. If 3 divides n, then q=n/3,
and that interval is exactly (9q,10q), containing no multiple of q.
Thus

\[
\boxed{\ell=1,\quad j=i-3,\quad
i/\gcd(i,3)\text{ squarefree}
\quad\Longrightarrow\quad\text{no solution}.} \tag{9}
\]

In particular this excludes every squarefree i, and also i=9m when
m is squarefree and 3 does not divide m. Every remaining i must
either be divisible by 27 or have p^2|i for some prime p!=3.

More generally, rad(q)|r-3n, so (8) requires

\[
\boxed{\operatorname{rad}(i/\gcd(i,3))<i/3.} \tag{10}
\]

## 5. Prime powers: exact valuation classification

Suppose n=p^a. Write d=v_p(r). All statements concern a
hypothetical solution, so n>=104 and (8) hold.

We use this elementary block observation. If A=p^alpha T,
r=s p^alpha+u with 0<u<p^alpha, then

\[
v_p\binom{A-1}{r-1}=v_p\binom{T-1}{s}.
\tag{11}
\]

Indeed all bottom alpha base-p digits of A-1 are p-1, so subtracting
r-1 creates no borrow there. The borrows above them are precisely
those for choosing s from T-1. Equivalently, in the product for the
binomial, all factors whose indices are not divisible by p^alpha
are p-adic units and the remaining factors form C(T-1,s).

### 5.1 Primes p>=7

Here alpha=a, T=(n-1)(n-2)/6, r=3n+u with 0<u<n/3,
and d<a. Modulo p, T=1/3; none of T-1,T-2,T-3 vanishes.
Thus C(T-1,3) is a p-adic unit and

\[
v_p(L)=a-d.
\]

Because n^2 is a pure p-power and 6n-9 is not divisible by p,
v_p(X)=2a. Both B=r and B=A-r have valuation d, so the equation
forces a-d=2d. Therefore

\[
\boxed{p\ge7\Longrightarrow a=3d.} \tag{12}
\]

Let v=r/p^d and u=r-3n. Splitting the product in (11) at the
multiples of n and reducing normalized units modulo p gives

\[
\frac{L}{p^{a-d}}
\equiv\frac{T}{v}(-1)^{u-1}\binom{T-1}{3}
\equiv\frac{(-1)^u40}{243v}\pmod p.
\]

The right side of the original equation, normalized by p^(2d),
is v^2 modulo p. Consequently

\[
\boxed{(9v)^3\equiv(-1)^u120\pmod p.} \tag{13}
\]

For p=1 modulo 3, this requires 120 to be a nonzero cubic residue
modulo p. In particular 120 is not a cube modulo 13 or modulo 19.
Thus there is no solution with i=13^a or i=19^a for any positive a.

### 5.2 The primes 2 and 5

Again alpha=a and s=3 in (11).

For p=2, n>=104 forces a>=7. The three factors of C(T-1,3)
have valuations

\[
v_2(T-1)=1,\quad v_2(T-2)=0,\quad v_2(T-3)=3.
\]

After the denominator 6, v_2 C(T-1,3)=3. These valuations follow
from T-1=(n-4)(n+1)/6 and T-3=(n^2-3n-16)/6.
Therefore

\[
\boxed{p=2\Longrightarrow a+3=3d,\quad a=0\pmod3.} \tag{14}
\]

For p=5, n>=104 forces a>=3. T-2=(n-5)(n+2)/6 has valuation
1, and T-1,T-3 are units. Thus

\[
\boxed{p=5\Longrightarrow a+1=3d,\quad a=2\pmod3.} \tag{15}
\]

In both cases v_p(X)=2a and d<a, so the right side has valuation
exactly 2d, justifying the equations.

### 5.3 The prime 3

Here alpha=a-1, q_0=3^(a-1)=n/3, and
T=(n-1)(n-2)/2. The gap (8) gives r=9q_0+u, 0<u<q_0,
so d<alpha and s=9 in (11).

Now

\[
T-1=n(n-3)/2,\qquad v_3(T-1)=a+1.
\]

As C(T-1,9)=(T-1)/9*C(T-2,8), and the latter binomial is a
3-adic unit, v_3 C(T-1,9)=a-1. Also
v_3(X)=2a-2, since v_3(6n-9)=2. Hence

\[
\boxed{p=3\Longrightarrow 2a-2=3d,\quad a=1\pmod3.} \tag{16}
\]

This valuation class is eliminated completely by the higher-precision
argument in `v5_offset_three_three_power.md`.

## 6. Consequences and status

In particular, i=p^2 and i=p^4 are excluded for every prime p
when j=i-3 and ell=1, in either outer branch. The possible p=3,a=4
and p=5,a=2 exceptions in the residue-class table lie in the already
excluded small-j range.

The proof is ordinary exact mathematics using previously established
endpoint, small-j, and divisibility results. No Lean formalization of
the new gap inequalities or the valuation taxonomy is claimed.
These results do not exclude every composite i, every prime-power
class, or every ell>1 offset-three family.

Both the root proof reviewer and the independent `v5_l1_gap` reviewer
checked this note and reported no correction needed. The exact constants,
cubic residue examples, and the companion note's six residual cases are
reproducibly checked by `v5_offset_three_checks.py`; its result is recorded
in `v5_offset_three_verification.json`.
