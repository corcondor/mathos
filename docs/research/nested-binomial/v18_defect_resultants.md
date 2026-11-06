# v18: local quadratic obstructions become factors of polynomials in the exact defect

Date: 2026-11-07 JST. Written proofs and exact integer checks.
No new Lean execution, DeepSeek API execution, or complete CAS solver is claimed.

## 1. Scope and inherited inputs

Keep the original squared-index equation, only in the branch ell=1, j=i-3.
Write n=i, A=binom(n,3), r=min(k,A-k), m=6n-9 and

\[
M=\gcd(n,3)\gcd(n-1,6),\quad Q=n(n-1)/M,\quad
\delta=Q/\gcd(Q,r^2),\quad C=M\delta,\quad K=\delta r^2/Q.
\]

Here C is an auxiliary coefficient, not the notation for a binomial coefficient.
The v16 exact-defect theorem supplies

\[
K\in\mathbb Z_{>0},\quad \gcd(K,\delta)=1,\quad
Cr^2=Kn(n-1),\quad
9C<K<\frac{10400}{927}C<\frac{45}{4}C,\quad M\le6.
\tag{1}
\]

Both original branches k=r and k=A-r are retained, with n>=104.
All conclusions below are necessary conditions for original solutions.
They are not unconditional assertions about all integers n.

For the negative neighbors retain

\[
\mathcal C(n)=\{c\in\{2,3,5,6,7,8,10,11,12,13,14,15\}:
6\mid(c+2)n-3c\},
\]

\[
N_c=n^2-c,\qquad a_c=((c+2)n-3c)/6,\qquad
A-a_c=(n-3)N_c/6.
\tag{2}
\]

Let L=lcm(1,...,m), and for a prime p let j_p=floor(log_p(m)).
Define the v17 excess and its square-root divisor by

\[
R_c=\prod_{p\ge17}p^{\max(v_p(N_c)-j_p,0)},\qquad
T_c=\prod_{p\ge17}p^{\lceil\max(v_p(N_c)-j_p,0)/2\rceil}.
\tag{3}
\]

v17 proves R_c|k^2, hence T_c|k. Primes in different N_c are distinct
in this range, and all are coprime to Q and delta. Set R=product R_c.

## 2. Small branch: the whole excess product divides K

If k=r, then

\[
\boxed{R\mid K,\qquad R<68\delta.}
\tag{4}
\]

Indeed R|r^2 and gcd(R,Q)=1 give R|delta*r^2/Q=K.
The numerical bound is

\[
K<\frac{10400}{927}M\delta\le\frac{62400}{927}\delta<68\delta.
\]

This exact divisibility connects the simultaneous v17 excess condition
to the *actual* defect delta, rather than just to the size of n.
It can be used together with the v17 bound R<(225n)^(2/3).
No upper bound on delta follows from (4) alone.

## 3. Complementary branch: explicit norm factors

If k=A-r, then for every admissible c,

\[
\boxed{T_c\mid E_c(C,K),}
\tag{5}
\]

where

\[
D_c(C,K)=(36K-Cc(c+8))^2-C^2c(5c+4)^2,
\]

\[
g_c=\gcd(1296,72c(c+8),c(c-1)(c-4)^2),\qquad
E_c=D_c/g_c.
\tag{6}
\]

The division in (6) is coefficientwise over the integers. Every prime
factor of g_c is 2 or 3, since g_c divides 1296.

### Proof without cancellation of a possible nonunit

Put q=T_c. From q|k and q|N_c, the identity (2) gives
r=A=a_c modulo q; the denominator 6 is a unit modulo q.
Combining this with (1) and n^2=c modulo q yields

\[
q\mid U_c n+V_c,
\]

\[
U_c=6Cc(c+2)-36K,\qquad
V_c=c\{36K-C(c^2+13c+4)\}.
\tag{7}
\]

The exact polynomial identity behind (7) is

\[
36Kn(n-1)-C\{(c+2)n-3c\}^2
=\{36K-C(c+2)^2\}(n^2-c)+U_cn+V_c.
\]

Next,

\[
V_c^2-cU_c^2=c(c-1)D_c.
\tag{8}
\]

Multiplying (7) by U_cn-V_c and using n^2=c modulo q proves
q|c(c-1)D_c. All prime factors of q are at least 17, whereas
2<=c<=15 and 1<=c-1<=14. Thus gcd(q,c(c-1)g_c)=1,
which proves (5). No cancellation of K, delta or a possible zero
residue is required.

Every c in this list is nonsquare. Consequently D_c cannot vanish:
D_c=0 would make sqrt(c)=(36K-Cc(c+8))/(C(5c+4)) rational.
Therefore E_c is a nonzero explicit integer.

The primitive quadratic forms are:

| c | E_c(C,K) |
|---:|---|
| 2 | 162K²−180CK+C² |
| 3 | 216K²−396CK+C² |
| 5 | 324K²−1170CK+5C² |
| 6 | 54K²−252CK+5C² |
| 7 | 24K²−140CK+7C² |
| 8 | 81K²−576CK+56C² |
| 10 | 2K²−20CK+5C² |
| 11 | 648K²−7524CK+2695C² |
| 12 | 27K²−360CK+176C² |
| 13 | 12K²−182CK+117C² |
| 14 | 162K²−2772CK+2275C² |
| 15 | 216K²−4140CK+4235C² |

Thus for a fixed pair (delta,K), the allowable prime support of every
negative excess is obtained by factoring twelve explicit quadratic
integers, independently of the magnitude of n.

### Stronger version with the shorter LCM from v18

The independent theorem in [v18_short_lcm.md](v18_short_lcm.md) proves
the same excess divisibility using L_r in place of L_m, in both branches.
Consequently (4) and (5) remain valid after replacing every j_p in (3)
by floor(log_p(r)). In particular the entire stronger excess product
R_r divides K in the small branch, and each stronger square-root
divisor T_{c,r} divides the same nonzero E_c in the complementary branch.
The eliminations and constants above require no changes.

For each individual c, N_c<r^2 implies that its excess over L_r has at
most one prime base: two exact prime powers greater than r would have
product greater than N_c. Different admissible c can still contribute
different primes. The product condition combines those different neighbors.

## 4. Conditional polynomial heights in delta

Suppose at least one admissible negative neighbor has a prime p with

\[
p^2\mid N_c,\qquad p^2>m.
\tag{9}
\]

v17 proves that this is the complementary branch, e=v_p(N_c)=3,
and p<=m. Thus j_p=1, T_c contains p, and p divides E_c(C,K).

For 9<=x<=10400/927, direct exact bounds on the twelve quadratics give

\[
\left|E_c(1,x)\right|
\le\frac{293437045}{10609}<\frac{250000}{9}.
\tag{10}
\]

Here E_c(1,x) means C=1 and K=x. The first bound is the maximum
over all twelve c and the closed interval, attained at its upper endpoint
for c=5. Each quadratic is convex; the maximum absolute value occurs
at an endpoint or at its vertex, so this is a complete rational
calculation, not a grid sample.

As C<=6delta, (5) gives

\[
p\le|E_c(C,K)|<10^6\delta^2.
\]

Together with m<p^2 this proves

\[
\boxed{n<2^{38}\delta^4.}
\tag{11}
\]

For c=10, which is admissible for every n, the sharper exact interval bound

\[
|2x^2-20x+5|<33
\]

gives p<1188delta^2, hence

\[
\boxed{n<2^{18}\delta^4
\quad\text{if }p^2\mid n^2-10,\ p^2>m.}
\tag{12}
\]

The integer margins are checked exactly:
(10^12+9)/6<2^38 and (1188^2+9)/6<2^18.
The extra 9 is harmless for every delta>=1.

These heights are conditional on the existence of a large repeated prime.
If all applicable negative neighbors lack such a prime, (11)-(12)
do not assert a height. In particular, they do not replace
log(n)<28delta by an unconditional polynomial bound.

## 5. Positive neighbor: signed norm factors

Assume n=3 modulo 6 and define

\[
N_+=n^2+1,\qquad S=N_+/\gcd(N_+,L).
\]

The v17 binomial congruence proof gives

\[
S\mid k^2-1,\qquad \gcd(S,6Q)=1.
\tag{13}
\]

For clarity, p=2 has v_2(N_+)=1 and is already absorbed by L;
p=3 does not divide N_+. Every remaining prime is coprime to n(n-1).
The congruence in (13) follows for each p^e from the binomial
divisibility lemma with loss j_p, and multiplies over the primes.

In fact S is 1 or a power of a single odd prime. For any integer
0<N<m^2, two distinct primes with exact powers p^e>m and q^f>m
would have product exceeding N. A prime in N/gcd(N,L) has such
an exact power. Here N_+<m^2.

### Small branch

If k=r, use n^2=-1 and r^2=1 modulo S in (1). This gives

\[
S\mid K(n+1)+C,\qquad
\boxed{S\mid K^2+(K+C)^2<10000\delta^2.}
\tag{14}
\]

The latter divisibility follows by multiplying K n+(K+C) by
K n-(K+C). Its upper bound uses
K/C<45/4 and ((45/4)^2+(49/4)^2)*36<10000.

### Complementary branch

For S>1, there is a unique sign sigma in {+1,-1} with
k=sigma modulo S: an odd prime power has only the two square roots
of one. Put b=(n+3)/6, so A=b modulo S and r=b-sigma modulo S.
Eliminating n as in (7)-(8), now with n^2=-1, gives

\[
\boxed{
\begin{array}{ll}
S\mid648K^2+36CK+25C^2,&k=+1\pmod S,\\
S\mid648K^2+1764CK+1681C^2,&k=-1\pmod S.
\end{array}}
\tag{15}
\]

Indeed the respective linear pairs in n are
(36K-6C,36K+8C) and (36K+18C,36K+80C).
The sums of their squares are four times the two displayed forms;
4 is a unit modulo S. Both forms are positive, and both are
less than 4*10^6 delta^2 by (1).

If p^2|N_+ and p^2>m, v17 gives e=2 and j_p=1, so p|S.
Equations (14)-(15) then imply the additional conditional heights

\[
\boxed{
\begin{array}{ll}
n<2^{24}\delta^4,&k=r,\\
n<2^{42}\delta^4,&k=A-r.
\end{array}}
\tag{16}
\]

Again n=3 modulo 6 and the stated repeated-prime condition are required.
The estimates use (10^8+9)/6<2^24 and ((4*10^6)^2+9)/6<2^42.

## 6. Verification and scope

The standard-library checker verifies the coefficient identities,
all twelve primitive forms and exact extrema, and all numerical
constant margins. It additionally checks the elimination congruences
on finite prime-power residue rings. Those residue examples are
supporting checks; the general proofs above establish the quantified
divisibilities.

This result uses v16_square_defect_pell.md and
v17_quadratic_prime_powers.md, without the new v18 gap theorem.
The shorter-LCM corollary additionally uses v18_short_lcm.md; the
L_m formulation is independent of that new theorem. It therefore
connects the defect and local-prime necessary-condition systems.
It does not find an original solution,
bound all possible delta, or solve either branch.

