# Offset three: a logarithmic gap and bounded repeated-prime defect

## Scope and inputs

This note retains the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

We restrict to ell=1 and j=i-3, and put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
X=\binom{n^2}{6n-9},\quad L=\binom Ar.
\]

Both choices k=r and k=A-r are included. The previous exact reductions
and the proof in v5_offset_three_structure.md give

\[
n\ge104,\quad X<L<2X,\quad 3n<r<10n/3,
\qquad q:=n/\gcd(n,3)\mid r^3.
\tag{1}
\]

The new statements below are uniform in the unbounded integer n.
They do not prove nonexistence for every composite n.

## 1. A logarithmic upper gap

**Theorem.** Every solution in this family with n>=1024 satisfies

\[
\boxed{3n<r<3n+\frac{3n}{4\log n}.}
\tag{2}
\]

Here and throughout, log is the natural logarithm.

### Proof

Set x=3/(4 log n), a=(3+x)n, and b=ceil(a). Since n>=1024 and
e<3, one has log n>6, hence 0<x<1/8. Thus

\[
b<7n/2,\qquad A>4n^3/25>b^2.
\]

The estimate A>4n^3/25 follows from n^2-75n+50>0, valid already
for n>=75. The estimate 4n^3/25>b^2 follows from
4n/25>49/4 in the present range.

The elementary product inequality
product(1-t_s)>=1-sum(t_s), for 0<=t_s<=1, gives

\[
\binom Ab>\frac{A^b}{2b!}.
\]

The integral bound on log(b!) gives b!<=e b(b/e)^b, so

\[
\binom Ab>\frac{(eA/b)^b}{2eb}.
\]

The function y log(eA/y) is increasing for 0<y<A, since its
derivative is log(A/y)>0. Therefore b>=a, b<A, and e<3 imply

\[
\binom Ab
>\frac{(eA/a)^a}{21n}
>\frac{\bigl(4e n^2/[25(3+x)]\bigr)^{(3+x)n}}{21n}.
\tag{3}
\]

Let N=n^2 and m=6n-9. The inequality C(N,m)<(eN/m)^m,
together with monotonicity of y log(eN/y) for y<N, yields

\[
X<\left(\frac{en}{6}\right)^{6n},
\tag{4}
\]

because m<6n<N. Combining (3) and (4),

\[
\log\frac{\binom Ab}{2X}
>
n\left\{\frac32+(3+x)[1-\log(25(3+x)/4)]-6(1-\log6)\right\}
-\log(42n).
\tag{5}
\]

Write f(y)=y[1-log(25y/4)]. Its derivative is -log(25y/4).
Since 0<x<1/8 and log(625/32)<3,

\[
f(3+x)-f(3)>-3x>-\frac38.
\tag{6}
\]

Also

\[
\frac32+f(3)-6(1-\log6)
=3\log(48/25)-\frac32>\frac9{20}.
\tag{7}
\]

Consequently the expression in braces in (5) is greater than
9/20-3/8=3/40. Thus

\[
\log\frac{\binom Ab}{2X}>\frac{3n}{40}-\log(42n)>0.
\tag{8}
\]

For the last strict inequality, the function 3n/40-log(42n)
increases for n>40/3. At n=1024, e^(3*1024/40)>e^17>2^17>42*1024.
This proves C(A,b)>2X. Since b<A/2 and r<=A/2, equation (1)
and monotonicity of the binomial row force r<b. As r is an integer,
r<ceil(a) implies r<a, completing (2).

All numerical constants above can be established by exact rational
inequalities:

- e<68/25 follows by summing through 1/4! and bounding the tail
  by 1/100: e<65/24+1/100=1631/600<68/25.
- log(48/25)>13/20 follows from
  (68/25)^13<(48/25)^20.
- e>65/24>27/10 and (27/10)^3>625/32 imply log(625/32)<3.
- log 1024>6 follows from e<3 and 3^6<1024.

The accompanying exact checks verify the displayed rational
comparisons after clearing denominators. No asymptotic remainder or
floating-point inequality is used.

## 2. The minimal divisor whose cube is a multiple of q

For a positive integer z define

\[
c_3(z)=\prod_{p\mid z}p^{\lceil v_p(z)/3\rceil}.
\]

This is the least positive integer, in the divisibility ordering,
whose cube is divisible by z. More explicitly,

\[
z\mid u^3\quad\Longleftrightarrow\quad c_3(z)\mid u.
\tag{9}
\]

Define the positive integer

\[
\boxed{R=\frac{n}{c_3(n/\gcd(n,3))}.}
\tag{10}
\]

It is an integer because c_3(q) divides q and q divides n.
Equation (1) and (9) show that c_3(q) divides r and n, hence
also r-3n. The latter is positive. Therefore

\[
r-3n\ge c_3(q)=n/R.
\tag{11}
\]

Combining (11) with (2) gives the new necessary condition

\[
\boxed{\frac43\log n<R,\qquad n<e^{3R/4}\qquad(n\ge1024).}
\tag{12}
\]

For every fixed upper bound on R, this yields a proved finite
upper bound on n. The quantity c_3(q) retains repeated prime powers
and is generally stronger than rad(q).

Even without the new logarithmic bound, (1) and (11) exclude R<=3.
For example n=4m with m squarefree and gcd(m,6)=1 has R=2 and
is therefore impossible for every m. This conclusion requires no
new finite certificate.

## 3. Complete finite reduction when R<=12

Suppose R<=12. If n>=1024, (12) implies n<e^9<8192. The final
comparison follows from e<68/25 and (68/25)^9<8192.
If n<1024, the same integer upper bound is automatic. Thus

\[
\boxed{104\le n\le8191}
\tag{13}
\]

contains every remaining possibility with R<=12.

Put c=c_3(q), so n=cR. Since c divides r, write

\[
r=c(3R+t).
\]

The strict gap 3n<r<10n/3 is exactly

\[
\boxed{t\ge1,\qquad3t<R.}
\tag{14}
\]

For R<=12 there are at most three such t. Values R<=3 allow none.
For each pair (n,t), only k=r and k=A-r remain.

Consequently (13)-(14), together with the definition of R, are a
complete finite remainder, derived from uniform inequalities.
There is no arbitrarily chosen upper-index search cutoff.

The exact modular certificate and its independently ordered verifier
are implemented in v6_offset_composite_checks.py. The generator
enumerates n first, while the verifier enumerates R,c first and
checks the original inequalities. The generator uses factorial-table
Lucas residues; the verifier uses direct small binomial coefficients
for each Lucas digit. Every prime witness is checked.

The completed independent verification excludes all **2,180** pairs
(n,r), hence all **4,360** branch equations. Every witness prime is
at most **17**, and there are no unresolved cases. Thus

\[
\boxed{\ell=1,\quad j=i-3,\quad
i/c_3(i/\gcd(i,3))\le12
\quad\Longrightarrow\quad\text{no solution}.}
\tag{15}
\]

The certificate SHA-256 is

5744085478ff7608b832f6e1e1bc1391aab921c9332f60b3984fb68f20b77cad.

The full report is v6_offset_composite_verification.json. Regenerate
and verify with:

    python3 v6_offset_composite_checks.py all

## 4. Interpreting R

For primes other than 3, a factor p^a in n contributes
p^(a-ceil(a/3)) to R. For 3^a exactly dividing n, it contributes
3^(a-ceil((a-1)/3)).

In particular, R<=12 includes the following cases with nontrivial
repeated prime factors:

- n=4m, with m squarefree and odd;
- n=8m,16m, with m squarefree and odd;
- n=32m, with m squarefree and gcd(m,6)=1;
- n=25m, with m squarefree and gcd(m,15)=1;
- n=49m, with m squarefree and gcd(m,21)=1;
- n=121m, with m squarefree and gcd(m,33)=1;
- n=100m, with m squarefree and gcd(m,30)=1;
- n=36m,72m,144m, with m squarefree and gcd(m,6)=1;
- n=27m, with m squarefree and 3 not dividing m.

The squarefree cases and n=9m with m squarefree and 3 not dividing m
were already excluded in v5. The list above illustrates the
additional families; the invariant condition R<=12 is the precise
statement and does not depend on this illustrative classification.

## 5. Combining the two consecutive common divisors

The companion v6_common_divisor.md strengthens q|r^3 to

\[
Q=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{16}
\]

The factors of Q are coprime. Put

\[
g=\gcd(n,3),\quad d=\gcd(n-1,6),\quad
c_1=c_3(n/g),\quad c_2=c_3((n-1)/d),
\]

\[
R=n/c_1,\qquad S=(n-1)/c_2.
\]

Equation (16) implies c_1 c_2|r. Since r<10n/3,

\[
\boxed{n-1<\frac{10}{3}RS.}
\tag{17}
\]

Also c_1^3>=n/g. Cubing c_1 c_2<10n/3 and substituting
c_2=(n-1)/S gives

\[
\frac{(n-1)^3}{n^2}<\frac{1000g}{27}S^3.
\]

The left side is n-3+3/n-1/n^2>n-3. Therefore

\[
\boxed{n<3+\frac{1000g}{27}S^3.}
\tag{18}
\]

Thus a fixed upper bound on the repeated-prime defect of n-1
also gives a proved finite bound on n. The logarithmic theorem
(12) and its complete R<=12 exclusion do not depend on (16).

## 6. At least one adjacent integer has a large square divisor

Let U^2 and V^2 be the largest square divisors of n and n-1.
For every positive integer z, rad(z)>=z/W^2, where W^2 is its
largest square divisor. This follows prime by prime from
2 floor(a/2)>=a-1. Further,

\[
c_1\ge\operatorname{rad}(n/g)\ge\frac{\operatorname{rad}(n)}g,
\quad
c_2\ge\operatorname{rad}((n-1)/d)\ge
\frac{\operatorname{rad}(n-1)}d.
\]

Consequently R<=g U^2 and S<=d V^2. Since g|3, d|6, and
gcd(g,d)=1, their product divides 6. Combining this with (17),

\[
\boxed{n-1<20U^2V^2.}
\tag{19}
\]

In particular D=max(U,V) satisfies

\[
\boxed{D^2\mid n\ \hbox{or}\ D^2\mid n-1,\qquad n<20D^4+1.}
\tag{20}
\]

Thus n or n-1 must have a square divisor larger than
sqrt((n-1)/20). This is a necessary condition for every solution
in the offset-three family, regardless of the number or size of
the prime factors of n.

### Polynomial sparsity of possible first indices

Let T(X) be the number of integers n<=X that can occur as the first
index of a solution in this family. This counts indices, not the
number of quadruples. Equations (19)-(20) imply

\[
\boxed{T(X)=O(X^{3/4}).}
\tag{21}
\]

Here is an elementary counting proof. Each possible n has an
integer D<=sqrt(X) such that n=0 or1 modulo D^2 and n<=20D^4;
the last non-strict inequality follows from (20) and integrality.
For a fixed D, the number of such n is at most

\[
2\min(X/D^2,20D^2)+2.
\]

Summing this upper bound and splitting at Y=(X/20)^(1/4),
the contribution from D<=Y is bounded by

\[
40\sum_{D\le Y}D^2+2Y=O(Y^3)=O(X^{3/4}),
\]

and the contribution from D>Y is bounded by

\[
2X\sum_{D>Y}D^{-2}+2\sqrt X=O(X/Y)+O(\sqrt X)
=O(X^{3/4}).
\]

Overcounting an n that has multiple witnesses only increases the
upper bound. No assumption about the independence of consecutive
integers, prime distribution, or unproved probability model is used.
In particular the admissible first indices have natural density zero.

## 7. Verification scope and limits

The author of v6_offset_prime_powers_wieferich.md independently
audited Sections 1--4 and both finite enumeration domains and
reported that all analytic constants, endpoint choices, and
coverage checks passed. Sections 5--6 are separate algebraic
consequences of the companion common-divisor theorem.

This note does not claim that all R are bounded, that every
remaining composite n has been excluded, or that the whole original
equation has been solved. The proofs here have not been formalized
in Lean.
