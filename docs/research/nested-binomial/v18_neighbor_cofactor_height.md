# v18: prime-power congruences and polynomial heights for both cofactor branches

Date: 2026-11-07 JST. These are written deductions and exact arithmetic
checks. They are not new Lean proofs, DeepSeek API work, or an external
peer review. Existing formal proofs and fixed goals are unchanged.

## 1. Scope and inherited inputs

Retain the original squared-index equation, only in the branch
ell=1, j=i-3, with both choices k=r and k=A-r. Put

\[
n=i,\quad A=\binom n3,\quad N=n^2+2,\quad m=6n-9,
\quad r=\min(k,A-k),\quad t=r-3n,\quad u=t+3,
\]
\[
g=\gcd(n,3),\quad d=\gcd(n-1,6),\quad M=gd,\quad
Q_0=n/g,\quad Q_1=(n-1)/d,\quad Q=Q_0Q_1.
\]

Also write \(\delta=Q/\gcd(Q,r^2)\), the intrinsic defect from v16.

The previously proved necessary conditions used here are

\[
n\ge104,\quad 3n<r<10n/3,\quad Q\mid r^3,\quad
t\ge4,\quad M\le6.
\tag{1}
\]

The v16 bound u>n^(3/5)/64 is used only for the old-gap corollaries.
The sharper v18 bound

\[
\boxed{u>n^{7/11}/96}
\tag{2}
\]

from [v18_residual_gap.md](v18_residual_gap.md) is used for the new
numerical heights. That theorem has the same old necessary conditions
(1), and introduces no prime-support or bounded-defect assumption.

Use epsilon=0 for k=r and epsilon=1 for k=A-r. Define

\[
S_\varepsilon=(r-\varepsilon)^2-6n+8,\qquad
T_\varepsilon=S_\varepsilon-9N
=6n(t-\varepsilon-1)+(t-\varepsilon)^2-10.
\tag{3}
\]

## 2. The right general domain is a common divisor, not just a prime

Let q be **any positive divisor of gcd(N,S_epsilon)**, and set

\[
w=N/q,\qquad z=S_\varepsilon/q,\qquad J=z-9w=T_\varepsilon/q.
\tag{4}
\]

No primality of q is assumed. Since t>=4, (3) gives T_epsilon>0.
The coarse interval also gives S_epsilon<100N/9. Therefore

\[
\boxed{J\ge1,\quad 9w<z<100w/9,\quad 0<J/w<19/9.}
\tag{5}
\]

Put

\[
\begin{array}{c|cc}
\varepsilon&c_0&c_1\\ \hline
0&10w+2J&25w+3J\\
1&9w+2J&24w+3J.
\end{array}
\tag{6}
\]

The integer identity w(r-epsilon)^2=zN+6wn-8w implies

\[
c_i\equiv wr(r-2\varepsilon)\pmod{Q_i}\quad(i=0,1).
\tag{7}
\]

Consequently

\[
\boxed{Q_i\mid c_i^3,\quad\text{and if }\varepsilon=0,\quad
Q_i^2\mid c_i^3.}
\tag{8}
\]

The proof is the same prime-by-prime transfer as v15: if alpha=v_p(Q_i),
then v_p(r)>=ceil(alpha/3). In the small branch,
v_p(c_i)>=min(alpha,2ceil(alpha/3))>=ceil(2alpha/3).
No cancellation of w or assumption gcd(w,Q_i)=1 occurs.

Thus every cofactor argument based solely on (5)-(8), including the
v15 polynomial bounds and v17 adaptive-defect bounds, applies to every
q in (4), even if q<=m or q is composite.

### A canonical, relatively prime pair of parameters

Take the largest admissible common divisor

\[
G=\gcd(N,S_\varepsilon)=\gcd(N,T_\varepsilon).
\]

Then w=N/G and J=T_epsilon/G satisfy

\[
\boxed{\gcd(w,J)=1.}
\tag{9}
\]

These are the denominator and numerator of the positive rational
difference S_epsilon/N-9 in lowest terms. The resulting fixed-J
heights below are therefore independent of a choice of prime factor.

For this canonical pair, linear combinations in (6) give the useful
constant gcd restrictions

\[
\boxed{
\gcd(c_0,c_1)\mid20\quad(\varepsilon=0),\qquad
\gcd(c_0,c_1)\mid21\quad(\varepsilon=1).
}
\tag{10}
\]

For epsilon=0 use 5c0-2c1=4J and 3c0-2c1=-20w.
Their gcd is 4*gcd(J,5), which divides 20.
For epsilon=1 use 8c0-3c1=7J and 3c0-2c1=-21w.
Their gcd is 7*gcd(J,3), which divides 21.
These assertions use (9); for a non-reduced q the larger common
factor gcd(w,J) must not be discarded.

### The canonical numerator shares only fixed small factors with delta

For the canonical choice q=G, the following restrictions couple the new
numerator to the old intrinsic defect:

\[
\boxed{
\gcd(\delta,J)\mid25\quad(k=r),\qquad
\gcd(\delta,J)\mid72\quad(k=A-r).
}
\tag{10a}
\]

The deduction was proposed by the root researcher and independently
checked here, including the exceptional primes 2,3,5.

To prove it, fix a prime with \(D=v_p(\delta)>0\), and set
\(\alpha=v_p(Q), E=v_p(r)\). The exact defect formula gives
\(\alpha=D+2E\), \(E\ge D\), and \(\alpha\ge3D\).

For p>=5, either n or n-1 is divisible by p^(3D), and N is a p-unit.
In the small branch,

\[
T_0=r^2-9n^2-6n-10
\equiv
\begin{cases}-10,&p\mid n,\\-25,&p\mid n-1\end{cases}
\pmod{p^{2D}}.
\]

Only p=5 can divide both delta and J. If p|n, its valuation in T0 is
exactly 1. If p|n-1 and D>=2, it is exactly 2; D=1 already bounds the
common valuation by 1. Since G is a p-unit, the same holds for J.
In the complementary branch, T1 is congruent to -9 or -24 modulo
p^D, so no p>=5 divides both delta and J.

At p=2, if n is even then v2(n)=alpha>=3D. The small-branch T0 and N
both have valuation exactly 1, so that factor cancels in J=T0/G.
The complementary T1 is odd. If n is odd,
v2(n-1)=alpha+1>=3D+1. T0 is odd. For T1, when D>=3, r is a multiple
of 8 and

\[
T_1=r(r-2)-24-24(n-1)-9(n-1)^2
\]

has valuation exactly 3. For D<=2 the common valuation is already at
most 2. Hence the possible common 2-part divides 8.

At p=3, either v3(n)=alpha+1>=3D+1 or
v3(n-1)=alpha+1>=3D+1. T0 is a 3-unit in both cases.
For T1 with 3|n, the competing valuations are E from r(r-2) and 2
from -9. If E=2 then D<=2; otherwise the smaller valuation is at most
2. Since N is a 3-unit, the common valuation in J is at most 2.
For n=1 mod3, v3(N)=1; if E>=2, v3(T1)=1 also, so G removes it.
If E=1, D<=1 already. This proves (10a).

In particular, for every prime p>=7 dividing delta, p does not divide
the canonical numerator J in either branch. The lemma does not impose
an upper bound on delta or J separately.

## 3. A positive integer from the complementary branch

Assume epsilon=1. Equation (8) makes

\[
a_0=\frac{g c_0^3}{n},\qquad
a_1=\frac{d c_1^3}{n-1}
\]

positive integers. Since c0 and c1 have leading coefficients 9 and 24
in w, cancel their leading cubes with 512 and 27. Write

\[
F_1=512c_0^3-27c_1^3
=7J(15552w^2+5400wJ+481J^2).
\tag{11}
\]

The new integer is

\[
\boxed{
E_1=512d a_0-27g a_1
=\frac{M\{nF_1-512c_0^3\}}{n(n-1)}\in\mathbb Z.
}
\tag{12}
\]

It is strictly positive. To check this uniformly, put v=J/w.
From t>=4 and (3),

\[
nv\ge\frac{n(12n-1)}{n^2+2}>11,
\tag{13}
\]

where the last inequality is n^2-n-22>0. Also v<19/9, so

\[
\frac{nF_1}{w^3}>108864\cdot11
>\frac{512\cdot119^3}{9^3}
>\frac{512c_0^3}{w^3}.
\tag{14}
\]

The middle positive difference is exactly 10179008/729.
No q>m condition is needed for this positivity argument.

Thus E1>=1. Dropping the subtracted positive term in (12) yields

\[
1\le E_1<\frac{M F_1}{n-1}\le\frac{6F_1}{n-1},
\]

and hence the new gap-sensitive cofactor inequality

\[
\boxed{n-1<6F_1
=42J(15552w^2+5400wJ+481J^2).}
\tag{15}
\]

Since J/w<19/9,

\[
\boxed{
n-1<C_1Jw^2,\qquad C_1=\frac{32994542}{27}.
}
\tag{16}
\]

This is a bound involving J as well as w; it does not uniformly improve
the older constant in n<20000w^3+1 when J is allowed to grow with w.
Its purpose is the new fixed-J height and the connection with the gap.

## 4. A second positive integer strengthens the small branch

Assume epsilon=0. The stronger part of (8) now makes

\[
b_0=\frac{g^2c_0^3}{n^2},\qquad
b_1=\frac{d^2c_1^3}{(n-1)^2}
\]

positive integers. Cancel leading cubes using 125 and 8:

\[
F_0=125c_0^3-8c_1^3
=J(30000w^2+9600wJ+784J^2).
\tag{17}
\]

The integer difference is

\[
\boxed{
E_0=125d^2b_0-8g^2b_1
=\frac{M^2\{n^2F_0-125c_0^3(2n-1)\}}{n^2(n-1)^2}.
}
\tag{18}
\]

To prove positivity, again set v=J/w. Equation (3) and t>=4 give

\[
nv\ge\frac{n(18n+6)}{n^2+2}>17.
\tag{19}
\]

After division by w^3, the numerator in braces in (18) is

\[
\begin{aligned}
&(784n^2-2000n+1000)v^3\\
&+(9600n^2-30000n+15000)v^2\\
&+(30000n^2-150000n+75000)v-250000n+125000.
\end{aligned}
\tag{20}
\]

All three displayed coefficients of positive powers of v are positive
for n>=104. Keeping only the linear term and using v>17/n gives a
strict lower bound

\[
260000n-2425000+\frac{1275000}{n}>0.
\tag{21}
\]

Thus E0>=1. Dropping the subtracted positive term in (18) gives

\[
\boxed{(n-1)^2<36F_0
=36J(30000w^2+9600wJ+784J^2).}
\tag{22}
\]

In particular,

\[
\boxed{
(n-1)^2<C_0Jw^2,\qquad C_0=\frac{17418496}{9}.
}
\tag{23}
\]

The constant follows from
30000+9600*(19/9)+784*(19/9)^2=4354624/81.

## 5. Polynomial heights for both branches

### A short square-root height and the first canonical numerator

The v17 necessary-condition theorem gives \(t\ge3\sqrt n\), without
requiring the original-binomial exclusion of the equality cases.
In the small branch,

\[
T_0=6n(t-1)+t^2-10
\ge18n^{3/2}+3n-10>18n^{3/2}.
\]

Since w/J=N/T0 and n>=104,
\(N<(5001/5000)n^2\) and \(2<\sqrt n/5\). Therefore

\[
\frac{c_0}{J}=\frac{10N}{T_0}+2
<\left(\frac{1667}{3000}+\frac15\right)\sqrt n
<\frac{19}{25}\sqrt n.
\]

The nonzero integer \(g^2c_0^3/n^2\) gives

\[
n^2\le g^2c_0^3\le9c_0^3
<9(19/25)^3J^3n^{3/2}<4J^3n^{3/2}.
\]

Hence

\[
\boxed{n<16J^6\quad(k=r).}
\tag{23a}
\]

In particular, \(n\ge104\) forces

\[
\boxed{J\ge2\quad(k=r).}
\tag{23b}
\]

This holds for every admissible q in (4), including the canonical
choice q=G. It needs neither the new 7/11 bound nor a fresh finite
enumeration. The previous v17 square-root theorem is its input.

### Higher exponents give smaller asymptotic heights

The exact positive comparisons from v17 give, for every q in (4),

\[
\begin{array}{ll}
u<\dfrac7{18}\dfrac{Jn}{w},&\varepsilon=0,\\[4pt]
u<\dfrac35\dfrac{Jn}{w},&\varepsilon=1.
\end{array}
\tag{24}
\]

Their proof uses only w*T_epsilon=J*N and t>=4,n>=104.
It does not require q to be prime or q>m.

Combining (24) with the new bound (2) gives

\[
\boxed{
w<\frac{112}{3}J n^{4/11}\quad(\varepsilon=0),\qquad
w<\frac{288}{5}J n^{4/11}\quad(\varepsilon=1).
}
\tag{25}
\]

Since (103/104)n<=n-1, (23) and (25) imply

\[
n^{14/11}
<
\underbrace{C_0(104/103)^2(112/3)^2}_{2363270191120384/859329<2^{32}}
J^3.
\]

Likewise, (16) and (25) imply

\[
n^{3/11}
<
\underbrace{C_1(104/103)(288/5)^2}_{10541360234496/2575<2^{32}}
J^3.
\]

Therefore

\[
\boxed{
\begin{array}{c|cc}
&\text{height of }n&\text{height of }w\\ \hline
k=r&n^{14}<2^{352}J^{33}&w^7<2^{101}J^{13}\\
k=A-r&n^3<2^{352}J^{33}&w<2^{49}J^5.
\end{array}
}
\tag{26}
\]

For the small-branch w bound, raise (25) to the seventh power and use
(n^14)^(2/11), obtaining
w^7<(112/3)^7*2^64*J^13<2^101*J^13.
For the complementary branch, cubing (25) gives
w^3<(288/5)^3*2^128*J^15<2^146*J^15<2^147*J^15.

Thus any fixed canonical numerator J in (9) now gives an explicit
polynomial height in **both** branches. The exponents for n are
33/14 and 11, respectively. J itself remains unbounded.

### Corollaries independent of the new 7/11 estimate

Keeping only the v16 bound u>n^(3/5)/64 in (24) gives

\[
w<(224/9)J n^{2/5}\quad(\varepsilon=0),\qquad
w<(192/5)J n^{2/5}\quad(\varepsilon=1).
\]

The same positive integers prove the separately useful bounds

\[
\boxed{
\begin{array}{c|cc}
k=r&n^6<2^{155}J^{15}&w<2^{15}J^2\\
k=A-r&n<2^{155}J^{15}&w<2^{68}J^7.
\end{array}
}
\tag{27}
\]

The relevant rational constants are
9453080764481536/7733961<2^31 and
14055146979328/7725<2^31. These older-gap consequences do not depend
on the new residual proof.

## 6. A congruence that includes all exact prime powers of n^2+2

Let L_m=lcm(1,...,m), and define

\[
\boxed{W=\gcd(N,3L_m)=\gcd(N,6L_m),\qquad R=N/W.}
\tag{28}
\]

The two gcds agree because v_2(N)<=1 and m>=615, so L_m already
contains the full 2-primary part of N.

For every original solution in the stated branch,

\[
\boxed{R\mid S_\varepsilon,\qquad \gcd(R,Q)=1.}
\tag{29}
\]

In particular R is always an admissible q in (4), so all the preceding
cofactor, J-height, and adaptive-defect conclusions apply to W.

### Proof of the full-power congruence

For a prime p put e=v_p(N) and a=floor(log_p m), defined by
p^a<=m<p^(a+1). The elementary identity
j*C(N,j)=N*C(N-1,j-1) shows that, for 1<=j<=m,

\[
p^{\max(e-a,0)}\mid\binom Nj.
\]

The exact alternating Pascal identity

\[
\binom{N-2}{m}
=\sum_{j=0}^m(-1)^{m-j}(m-j+1)\binom Nj
\]

therefore gives

\[
B=\binom{N-2}{m}\equiv-(m+1)=8-6n
\pmod{p^{\max(e-a,0)}}.
\tag{30}
\]

Next A-1=(n-3)N/6, so v_p(A-1)>=e-v_p(6).
Using C(A,r)=C(A-1,r)+C(A-1,r-1), both lower indices lie between 1
and m. Hence

\[
\binom Ar\equiv0
\pmod{p^{\max(e-a-v_p(6),0)}}.
\tag{31}
\]

Modulo the same prime power, A=1 and
k^2=(r-epsilon)^2. The original equation now yields the corresponding
prime-power part of (29). Multiplication over all primes gives
R=N/gcd(N,6L_m) dividing S_epsilon. This uses no inversion of a
p-divisible factorial.

For coprimality, primes p>=5 cannot divide both N and n(n-1).
The 2-part of N has been absorbed in W. If 3 divides Q, either
3 divides n, in which case 3 does not divide N, or 9 divides n-1,
in which case v_3(N)=1 and that factor is absorbed in W.
Thus gcd(R,Q)=1.

### Exact scope of the all-power extension

Since N<m^2, **R is either 1 or a power of a single prime**.
Indeed any prime appearing in R has its full exact factor p^e>m;
two different such factors would have product greater than m^2>N.
Thus (29) must not be described as combining many nontrivial excess
prime bases in this particular positive quadratic neighbor.

Its new content beyond the old large-prime congruence is that a
smaller prime with sufficiently high multiplicity is included, with a
precisely controlled loss a+v_p(6). In prime-power form,

\[
p^{\max(e-a-v_p(6),0)}\mid S_\varepsilon.
\tag{32}
\]

For example, in the small branch, the v17 adaptive bound applied to R
is

\[
R<53\sqrt\delta\,n.
\tag{33}
\]

If p>=5, p^e exactly divides N, e>2a, and w_0=N/p^e, then
e=2a+1 (because N<m^2<p^(2a+2)), and (33) gives

\[
\boxed{p<2809\delta\,w_0.}
\tag{34}
\]

This is a condition on an exact prime-power cofactor, valid with no
upper bound on the exponent. It is specific to k=r.
It does not assert that an arbitrary exact prime-power factor is
smaller than the old prime-divisor bounds.

## 7. Existing complete cofactor exclusion transfers without new scanning

The v17 finite certificate excludes w<=64 for **every q in (4)**,
not only for primes q. Its large-q enumeration deliberately imposed no
primality test. It covers every w<=64, every 9w<z<100w/9, every divisor
reconstruction of n from (8), and both original branches; the final
eleven q>m records have nonsquare S.

If q<=m, then N=qw<=mw implies n<6w<=384. The same four necessary
(n,r) pairs in the v17 small-domain record have intrinsic defects
1,1,5,1 and contradict the already proved delta>=13.

Therefore

\[
\boxed{
N/\gcd(N,S_\varepsilon)\ge65,\qquad
\gcd(N,3L_m)\ge65.
}
\tag{35}
\]

This is a logical transfer of the saved complete certificate, not a
new execution of its large enumeration. The first conclusion also
requires the inherited delta>=13 to handle q<=m. The height theorems
(15)-(27) do not use delta>=13 or this certificate.

For all admissible q, the inherited bounds also remain

\[
\begin{array}{ll}
n<240w^{3/2}+1,\quad n<52\sqrt\delta\,w+1,&k=r,\\
n<20000w^3+1,\quad n<983\sqrt\delta\,w^2+1,&k=A-r.
\end{array}
\tag{36}
\]

The prime-free proofs use only (5)-(8). Some coarse bounds for R are
automatic in parts of the small-prime range; no universal asymptotic
improvement for all n or all prime powers is asserted merely by
rewriting them with R.

## 8. Verification and limitations

The accompanying exact Python checks expand the polynomial identities,
verify the rational margins, and check both positive-integer
constructions on necessary-condition samples. Full binomial integer
values are used in selected finite examples of (30)-(31), including
nontrivial small-prime powers. These numerical examples support the
written all-prime proof and do not replace it.

The saved v17 cofactor certificate's hashes and complete domain are
checked for the logical reuse in Section 7; no claim of a fresh full
v17 rerun is made. The v18 7/11 height proof is a separate dependency
and receives a separate mathematical review.

Before the short argument (23a) was found, a complete auxiliary
calculation of the small-branch J=1 case was executed from
\(w^7<2^{101}\). It covers w=1,...,22051 and gives 902,288 divisor
generation points, 499,970 normalized n, 763 second-divisor candidates,
and no integer q=(n^2+2)/w. The maximum generated n was 217,588,146.
That is a derived divisor point, not an n cutoff. A full losslessly
compressed record was generated in the scratch audit workspace.
This auxiliary computation is not needed for (23a)-(23b); the short
universal proof is the published basis of J>=2.

No original solution was found. The canonical numerator J is not
bounded, the entire branch is not proved finite, and the original
four-variable equation remains unsolved. The old H>=21 and candidate
count O(sqrt(X) log X) are unchanged.

