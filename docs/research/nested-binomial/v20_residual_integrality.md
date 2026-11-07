# v20: residual reconstruction, exact gcd, and 2/3-adic cube classes

2026-11-07 JST. Written proof and exact arithmetic certificates; no new
Lean or DeepSeek execution. This supplements the original squared-index
equation, in the branch ell=1, j=i-3, for both choices of k.

## 1. The integer reconstruction supplies stronger necessary conditions

Retain the v17/v19 variables a,b,rho,n,t, with a,b,rho positive,
gcd(a,b)=1, b|486, and n,t integers. Put

\[
q(t)=t^2+3t+3.
\]

The two exact defining equations are

\[
81a n(n-1)=b\{9nq(t)+t^3\},                                      \tag{1}
\]
\[
\rho=a^2+ab(9n-t-6)-b^2q(t).                                    \tag{2}
\]

These equations, including the integrality of n,t, are stronger than just
the sextic square equation y²=F(a,b,rho). The following conclusions do not
use a bound on a, n, t, or rho.

**Theorem 1.** Equations (1)–(2), with gcd(a,b)=1, imply

\[
\boxed{\gcd(a,\rho)=\gcd(a,3),}                                \tag{3}
\]
\[
\boxed{\rho\equiv a^2\pmod3,\qquad
3\mid a\Longrightarrow \rho\equiv6\pmod9,}                     \tag{4}
\]
\[
\boxed{\rho\bmod9\in\{1,4,6,7\}.}                           \tag{5}
\]

In particular, combining (5) with the already established rho>=11 gives

\[
\boxed{\rho\ge13.}                                             \tag{6}
\]

This improvement does not extend the earlier finite rho search: the
unbounded congruence excludes 11 and 12 immediately.

**Proof of the gcd statement.** Let g=gcd(a,rho). Equation (2) and
gcd(g,b)=1 give g|q(t). Reducing (1) modulo g then gives g|t³.
The exact polynomial Bezout identity

\[
(2t^2-3t+3)q(t)-(2t+3)t^3=9                                   \tag{7}
\]

shows g|9. If 3|t, then q(t)=3 mod9, while if 3 does not divide t
then 3 does not divide t³. Hence

\[
\gcd(t^3,q(t))=\gcd(t,3)\in\{1,3\},
\]

and g divides 3. If 3|a, coprimality gives 3∤b; (1) modulo 3 forces
3|t. In (2), both the a² term and ab(9n-t-6) are divisible by 9,
while q(t)=3 mod9 and b²=1 mod3. Thus rho=−3b²=6 mod9. Consequently
3 divides g exactly once, proving (3). If 3∤a, g=1.

**Proof of the congruences.** If 3∤b, (1) modulo 3 gives 3|t, and
(2) gives rho=a² mod3. If 3|b, the same congruence follows directly
from (2), and gcd(a,b)=1 forces a to be a unit modulo 3. Thus 3∤a
always gives rho=1 mod3, whose mod9 classes are 1,4,7. The case
3|a was just shown to give the sole class 6. QED.

The hypotheses b|486, n>=104, and positivity are not needed for (3)–(5)
beyond making gcd(a,rho) unambiguous; the equations and coprimality suffice.
The application (6) uses the original-branch result rho>=11 from v19.

### A uniform parity condition

If b is odd, (1) modulo 2 gives t=n mod2, since q(t)=1 mod2 and
n(n-1) is even. Equation (2) then gives rho=a+1 mod2. If b is even,
coprimality makes a odd and (2) makes rho odd. Therefore

\[
\boxed{\rho\equiv a+b\pmod2.}                                 \tag{8}
\]

This also uses no numerical cutoff.

## 2. Saturating the residual square condition

The existing sextic is

\[
F=4a^6+(24b^2-12\rho)a^4
 +(36b^4+60b^2\rho+12\rho^2)a^2-3b^2\rho^2-4\rho^3.
\]

For a chosen signed square root y, the exact t reconstruction is

\[
t=\frac{2a(a^2+3b^2)-\rho(3b+2a)+y}{2b\rho}.                  \tag{9}
\]

Set

\[
N=b^2q(t)+ab(t+6)-a^2+\rho,\qquad n=N/(9ab).
\]

The two polynomial identities

\[
\begin{aligned}
&(2b\rho t-2a(a^2+3b^2)+\rho(3b+2a))^2-F\\
&\quad=4\rho P,
\end{aligned}                                                  \tag{10}
\]
\[
P=N^2-(9ab+b^2q(t))N-ab^3t^3                                  \tag{11}
\]

show that a residual square reconstructs (1) over the rationals, since
P=ab² times the left-minus-right side of (1). They do not prove n,t
are integers. This is exactly the distinction used in Theorem 1.

There is also an explicit saturation identity

\[
P=\rho N+aS,                                                   \tag{12}
\]
\[
S=a^3-a^2b(2t+3)-21ab^2-a\rho-b^3(6t+9)+b\rho(t-3).
\]

If t is an integer and rho=a² modb, N/b is an integer. Since P=0
and gcd(a,b)=1, (12) proves

\[
\frac a{\gcd(a,\rho)}\mid N/b.
\]

Consequently, after imposing (3),

\[
\boxed{n\in\frac1{9\gcd(a,3)}\mathbb Z\subseteq\frac1{27}\mathbb Z.}
\tag{13}
\]

This reduces the remaining denominator check to powers of 3. It is not
a sufficient condition for integer n. For example the residual point
(a,b,rho)=(373,2,13573) gives t=3363 and n=21299/3, despite satisfying
(3)–(5). The checker records both signs and exact rational reconstruction.

### Genuine extra restrictions on the sextic input

The following explicit positive-Z residual squares satisfy gcd(a,b)=1,
b|486, 27a>=31b, rho>=13, rho=a² modb,
1377rho<216a²+760b², and the old whole-fiber mod5 restriction. They
illustrate why equations (1)–(2) must retain integrality.

| (a,b,rho) | y | Positive t branch | Reconstructed n | New rejection |
|---|---:|---:|---:|---|
| (31,1,124) | 48732 | 405 | 19683/31 | gcd(a,rho)=31, violating (3) |
| (84,1,477) | 1067913 | 2277 | 64009/9 | rho=0 mod9, violating (5) |

These are auxiliary residual points, not former solutions of the original
equation. No claim is made that they satisfy every other v19 inequality.

## 3. Restrictions on the actual positive cube covers

Use the v19 normalization

\[
Z=(a^2-b^2-\rho)/b>0,\quad D=9a^2-b^2,
\quad L=D-3bZ,
\]
\[
U=(y/b-L)/2>0,\quad V=(y/b+L)/2>0,
\quad UV=bZ^3,\quad V-U=L.                                    \tag{14}
\]

Positivity of Z comes from the inherited v17 gap; it is not a new result.
Write U=alpha*u³, V=beta*v³ with positive cube-free alpha,beta. The
v19 cover condition alpha*beta*b²=gamma³ permits three formal exponent
pairs at each prime in bD. The following local restrictions remove
entire coefficient choices uniformly in a.

### Reconstruction restricts t and Z at 3

Write b=2^e 3^d, e in {0,1}, 0<=d<=5. If 3∤t, the factor
9nq(t)+t³ in (1) is a 3-adic unit. The right side has valuation d,
whereas the left side, for integer n, is divisible by 3⁴. Thus

\[
d\le3\Longrightarrow3\mid t.                                 \tag{15}
\]

The exact rearrangement of (2) is

\[
Z=b(t+1)(t+2)+a(t+6-9n).                                      \tag{16}
\]

It follows that

\[
\begin{cases}
Z\equiv-b\pmod3,& d=0,\\
3\mid Z,&1\le d\le3.
\end{cases}                                                    \tag{17}
\]

For d=0, (14) also forces (U,V)=(2,1) mod3.
If b is odd, t=n mod2 in (16) gives 2|Z.

### Complete table of allowed 3-adic cube-core exponents

Let i=v3(alpha), j=v3(beta); i,j are in {0,1,2}.

| d=v3(b) | Formal v19 pairs | Allowed v20 pairs |
|---:|---|---|
| 0 | (0,0), because 3∤bD | (0,0) |
| 1 | (0,1),(1,0),(2,2) | same three, with 3|Z |
| 2 | (0,2),(1,1),(2,0) | **(0,2),(2,0)** |
| 3 | (0,0),(1,2),(2,1) | **(1,2),(2,1)** |
| 4 | (0,1),(1,0),(2,2) | **(2,2)** |
| 5 | (0,2),(1,1),(2,0) | **(0,2),(2,0)** |

**Proof.** If d>=2, coprimality gives 3∤a and
v3(L)=v3(9a²-b²-3bZ)=2 exactly. Put f=v3(Z). Then
v3(U)+v3(V)=d+3f. For d=2,3, (17) gives f>=1, so the sum is >4.
For d=4 it equals 4 when f=0, and is >4 otherwise. For d=5 it is
always >4. If the sum is >4, the valuations must be unequal, with
minimum exactly 2, since v3(V-U)=2. Hence the pair is
(2,d+3f-2) or its reverse. If the sum is 4, both valuations are 2.
Reduction modulo 3 proves every row for all f, without an exponent cutoff.
For d=1 we retain the formal alternatives rather than claim more than
has been proved. QED.

### Prime 2

If b is even, a is odd and L is odd. Therefore U,V have opposite
parity; their valuations are 0 and 1+3v2(Z). The allowed cube-core
pairs at 2 are exactly among

\[
\boxed{(v_2(\alpha),v_2(\beta))\in\{(0,1),(1,0)\}.}           \tag{18}
\]

The formal pair (2,2) is excluded. If b is odd and a is even, 2∤bD
and the pair is (0,0). If a,b are both odd, the three formal pairs
(0,0),(1,2),(2,1) are retained; (16) gives 2|Z and U,V are both even.
No assertion is made that every retained pair is realized globally.

### Uniform count of remaining coefficient types

Let s be the number of prime divisors of D at least 5. Set

\[
N_2=\begin{cases}2&b\text{ even},\\3&a,b\text{ odd},\\1&a\text{ even},b\text{ odd},\end{cases}
\quad
(N_3(0),\ldots,N_3(5))=(1,3,2,2,1,2).
\]

Every original residual point belongs to one of at most

\[
\boxed{N_2N_3(d)\,3^s}                                         \tag{19}
\]

coefficient covers. For example, b=162 reduces the two small-prime
choices from 9 to 2, for every admissible a; b=18,54,486 reduces
them from 9 to 4. Primes at least 5 still need their own local/global
analysis, and a remains unbounded.

## 4. The common factor has a quantitative bound

For g0=gcd(U,V), the normalization alone implies

\[
\boxed{g_0^2\mid D^3,\qquad \gcd(g_0,a)=1.}                   \tag{20}
\]

Indeed g0|L and g0²|bZ³. For a prime p, write m=vp(g0), e=vp(b),
f=vp(Z). If vp(D)>=m, then 2m<=3vp(D). Otherwise, from
D=L+3bZ, vp(D)=vp(3)+e+f, and
2m<=e+3f<=3(vp(3)+e+f). This proves the divisibility prime by prime.
Finally gcd(a,D)=gcd(a,b²)=1. In this b|486 family one also has
gcd(g0,b)|9: there is no common factor 2 when b is even, and d>=2
has v3(g0)<=2 by the previous proof.

## 5. Verification and limitations

The accompanying generator checks the integer polynomial identities,
complete mod9/mod2 residue tables for (4)–(8), the q(t)=3 mod9 step of
the gcd proof, and the finite small-prime core choices. The all-primes
statement (3) is proved by the Bezout identity and valuation argument,
not by extrapolating a finite gcd table. The independent verifier uses
standard Python only, reconstructs
the residue tables directly, and uses exact polynomial coefficient
arithmetic rather than importing the producer. The exponent proof in
Section 3 is symbolic in f; a bounded exponent sample is not its proof.

The sample residual points are reconstructed in both signs with exact
fractions. Additional samples from the existing v19 Pell certificate
exercise the conditions on actual integer n,t inputs, but are not
solutions of the binomial equation. The general proof does not depend on
their number or height.

The new exclusion rho>=13 and congruence/gcd restrictions arise from
integer reconstruction, not from declaring the sextic fiber locally
empty. They are consistent with the v19 theorem that only mod5 can
exclude a whole unrestricted sextic fiber by a mod-prime test alone.
This work does not solve the unbounded residual family, complete a
Selmer computation, or solve the original four-variable equation.
