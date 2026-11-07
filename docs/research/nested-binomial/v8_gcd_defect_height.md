# A logarithmic lower bound for the missing part of the full binomial gcd

## Scope and theorem

We keep the original squared-index equation and restrict to
ell=1, j=i-3. Put

\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),\quad G=\gcd(A,X),\quad S=A/G.
\]

Every remaining solution has n>=104. The integer S measures the
part of A not contained in the common divisor G. This note proves
the necessary conditions

\[
\boxed{S\mid n-2,\qquad \log n<128S,\qquad n<2^{192S}.}
\tag{1}
\]

Thus a bounded missing part of the gcd implies an explicit finite
height bound, for general composite n as well as for prime-power
subfamilies. In particular,

\[
A\mid X\quad\Longrightarrow\quad n<e^{128}<2^{192}
\tag{2}
\]

for any solution. This is not a complete exclusion of all integers
in those bounds and does not solve the whole original equation.

## 1. Two integral quotients

The previously proved full-gcd theorem gives G|r^3. Hence

\[
T=r^3/G\in\mathbb Z_{>0},\qquad T=S\,r^3/A.
\tag{3}
\]

The v6 explicit common divisor is

\[
Q=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid G.
\]

Write c=gcd(n,3)gcd(n-1,6). Since c|6,

\[
A/Q=(n-2)c/6
\]

is an integer divisor of n-2: multiplying it by 6/c gives n-2.
As Q|G|A, the integer S=A/G divides A/Q. This proves S|n-2.

The gap 3n<r and the strict inequality A<n^3/6 yield

\[
\boxed{T>162S.}
\tag{4}
\]

The issue is now the distance from T to the next integer above
162S, rather than just the size of G or r separately.

## 2. A contradiction if log n is at least 128S

Suppose log n>=128S. Since S>=1, this implies n>=1024, so the
proved logarithmic upper gap applies:

\[
r<3n\left(1+\frac1{4\log n}\right)
\le3n\left(1+\frac1{512S}\right).
\tag{5}
\]

We will also use n>2^20 S. Indeed, e>2 and log n>=128S imply
n>=e^(128S)>2^(128S). For positive integral S, the elementary
induction 2^(S-1)>=S, together with 128S>20+S-1, gives
2^(128S)>2^20 S.

For n>=10, a direct rational comparison shows

\[
\frac{n^2}{(n-1)(n-2)}<1+\frac4n.
\tag{6}
\]

Clearing positive denominators reduces (6) to
n^2-10n+8>0, which holds at n=10 and increases thereafter.
Consequently n>2^20 S gives

\[
\frac{n^2}{(n-1)(n-2)}<1+\frac1{2^{18}S}.
\tag{7}
\]

Combining (3), (5), and (7),

\[
T<162S\left(1+\frac1{512S}\right)^3
             \left(1+\frac1{2^{18}S}\right).
\tag{8}
\]

Let

\[
F(x)=(1+x/512)^3(1+x/2^{18}).
\]

All four nonconstant coefficients of F are positive. Since S>=1,
termwise comparison of the polynomial gives

\[
S\bigl(F(1/S)-1\bigr)\le F(1)-1.
\tag{9}
\]

The exact rational inequality used in the shifted-power proof is

\[
162F(1)=\frac{2866676543645265}{17592186044416}<163.
\tag{10}
\]

Therefore (8)-(10) imply

\[
T<162S+162(F(1)-1)<162S+1.
\]

This and (4) place the integer T strictly between the consecutive
integers 162S and 162S+1. The contradiction proves log n<128S.
Finally e<11/4 and (11/4)^2<8 give e^(128S)<2^(192S), proving (1).

## 3. Interpretation and verification scope

Equivalently, every hypothetical solution in this branch must have

\[
\boxed{\gcd\!\left(\binom n3,\binom{n^2}{6n-9}\right)
<\frac{128}{\log n}\binom n3.}
\tag{11}
\]

For sufficiently large n, the two binomial coefficients therefore
cannot share almost all of A. The missing factor S must grow at
least logarithmically with n and must divide n-2.

This uses the same integer-separation mechanism that completes the
shifted prime-power family, but applies to every n in the
offset-three branch. It does not give an upper bound on S independent
of n, and does not claim that every bounded-S remainder has been
checked.

The divisibility G|r^3 was already kernel-checked in v6_formal.
The rational constant in (10) is separately checked in v8_formal.
The whole logarithmic theorem in this note is a written mathematical
proof and is not asserted to be Lean-formalized.

An independent mathematical audit by the composite-family reviewer
passed on 2026-11-05. It checked the divisor chain, the integral
quotient, both ratio estimates, the positive-coefficient argument,
and the strict endpoint contradiction. This was an AI-assisted
independent audit, not external peer review.
