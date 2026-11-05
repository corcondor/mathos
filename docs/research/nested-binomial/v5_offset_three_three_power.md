# Complete exclusion of powers of three in the ell=1, offset-three family

## Theorem and inputs

There is no solution of the original squared-index equation with

\[
\boxed{i=3^a,\qquad j=i-3,\qquad \ell=1,\qquad a\ge1.}
\]

Both outer branches, B=r and B=A-r, are included. We use the notation

\[
n=i,\quad A=\binom n3,\quad B=k,\quad
r=\min(B,A-B),\quad L=\binom Ar,
\]

\[
X=\binom{n^2}{6n-9},\qquad Y=B^2.
\]

The previous complete ell=1,j<=100 exclusion, together with the proofs
in `v5_offset_three_structure.md`, gives the following necessary facts:

\[
n\ge104,\qquad X<L<2X,\qquad 3n<r<10n/3. \tag{1}
\]

For n=3^a, write d=v_3(r). The valuation calculation in Section 5.3
of that note proves

\[
2a-2=3d.
\]

Thus every remaining candidate has

\[
a=3h+1,\qquad h\ge2,\qquad d=2h. \tag{2}
\]

This note proves a sharper size bound, then uses normalized units
modulo 9 to eliminate all exponents in (2). The only finite table
contains six integers when a=7; it is derived explicitly below.

## 1. A sharper upper bound when n>=2^15

We claim that for all n>=2^15 in this ell=1, offset-three family,

\[
\boxed{r<28n/9.} \tag{3}
\]

Put b=ceil(28n/9). The previously established estimates A>n^3/7
and b<7n/2 give A>b^2. In particular b<=A/2. The elementary
product bound and the factorial integral estimate give

\[
\binom Ab>
\frac{A^b}{2b!}\ge\frac{(eA/b)^b}{2eb}.
\]

Since 9b<=28n+8, we have A/b>n^2/20. Clearing denominators,
the latter comparison follows from

\[
4n^2-196n+120>0,
\]

which holds for n>=49. Using 8/3<e<3, we obtain

\[
\binom Ab>
\frac{(2n^2/15)^b}{6b}
\ge\frac{(2n^2/15)^{28n/9}}{6b}. \tag{4}
\]

As proved in the structure note, X<(n/2)^(6n). Also b<13n/4,
so 12b<39n. Consequently

\[
\frac{\binom Ab}{2X}>
\frac{\left[64(2/15)^{28/9}n^{2/9}\right]^n}{39n}. \tag{5}
\]

The bracket is increasing in n and is greater than 6/5 at n=2^15.
Raising the comparison to the ninth power and clearing denominators
reduces it exactly to

\[
2^{103}-3^{37}5^{19}
=1552720879039172862272697908633>0.
\]

The structure note proves (6/5)^n/(42n)>1 for every n>=104;
hence (5) is greater than 1. It follows that C(A,b)>2X. The
inequality L<2X and monotonicity of C(A,r) for r<=A/2 now imply
r<b, and therefore (3).

For exponents in (2), every a>=10 gives n>=3^10=59049>2^15.
Thus (3) applies to all remaining exponents except a=7.

## 2. Normalized products modulo 9

Write

\[
\alpha=a-1=3h,\qquad q=3^\alpha=n/3,\qquad
A=qT,\qquad T=\frac{(n-1)(n-2)}2.
\]

The broad gap in (1) permits us to write

\[
r=9q+u,\qquad 0<u<q.
\]

In this section assume in addition that

\[
0<u<q/3. \tag{6}
\]

This is exactly the conclusion of (3), since 3n=9q and 28n/9=28q/3.

Let S=T-1. A direct calculation gives

\[
S=\frac{n(n-3)}2=3^{\alpha+2}w,\qquad
w=\frac{3^\alpha-1}{2}\equiv4\pmod9. \tag{7}
\]

All congruences of rational units below are in the ring of rational
numbers whose denominator is coprime to 3, followed by reduction
modulo 9. Thus any displayed denominator v with 3 not dividing v
means its multiplicative inverse modulo 9.

### 2.1 Separate the factors divisible by q

Use the exact product

\[
\binom{A-1}{r-1}=
\prod_{m=1}^{r-1}\frac{A-m}{m}.
\]

The indices divisible by q are precisely q,2q,...,9q. Their product
is

\[
H=\prod_{s=1}^9\frac{T-s}{s}=\binom{T-1}{9}=\binom S9.
\]

By (7),

\[
\frac{H}{3^\alpha}=w\binom{S-1}{8}\equiv4\pmod9. \tag{8}
\]

Indeed C(S-1,8)=prod_{m=1}^8 (S-m)/m. After the eight minus
signs cancel, each factor is 1-S/m. Since v_3(S)=alpha+2 and
v_3(m)<=1, every such factor is 1 modulo 9. This proves both
v_3(H)=alpha and the normalized congruence (8).

### 2.2 Compute all remaining units, retaining the needed precision

For every index m not divisible by q,

\[
\frac{A-m}{m}=-(1-A/m).
\]

There are (r-1)-9=r-10 such indices, so their total sign is (-1)^r.
If v_3(m)<=alpha-2, then A/m is divisible by 9 and the unit
1-A/m is 1 modulo 9. Only v_3(m)=alpha-1 can contribute.

The latter indices have the form m=(q/3)s with 3 not dividing s.
Condition (6) says that the possible values of s are exactly

\[
1\le s\le27,\qquad 3\nmid s.
\]

There are 18 such values: nine are 1 modulo 3, and nine are 2
modulo 3. As T=1 modulo 9, their unit factors are

\[
1-3T/s\equiv
\begin{cases}
7\pmod9,&s=1\pmod3,\\
4\pmod9,&s=2\pmod3.
\end{cases}
\]

Their full product is 7^9 4^9=28^9=1 modulo 9. Combining
this with (8) proves

\[
\boxed{
\frac{1}{3^\alpha}\binom{A-1}{r-1}
\equiv4(-1)^r\pmod9.} \tag{9}
\]

The high valuation is removed only from the explicitly separated
factor H. All other factors are already 3-adic units. Thus reducing
them modulo 9 before multiplying by H/3^alpha loses no precision;
no unproved cancellation through a factor divisible by 3 is used.

### 2.3 The equation would make a unit cube equal to +/-4

Write v=r/3^d, so 3 does not divide v. By (2), alpha=3h and d=2h.
Using L=(A/r) C(A-1,r-1), equation (9) gives

\[
\frac{L}{3^{2d}}
=\frac{T}{v}\frac{\binom{A-1}{r-1}}{3^\alpha}
\equiv\frac{4(-1)^r}{v}\pmod9, \tag{10}
\]

because 2alpha-d=2d and T=1 modulo 9.

On the other side, v_3(X)=2a-2=6h. After division by 3^(2d),
X still has valuation 2h>=4 and hence contributes 0 modulo 9.
If B=r, then Y/3^(2d)=v^2. If B=A-r, then

\[
\frac{B}{3^d}=3^hT-v\equiv-v\pmod9,
\]

since h>=2, so its square also gives v^2 modulo 9. Consequently
the equation forces

\[
\boxed{v^3\equiv4(-1)^r\pmod9.} \tag{11}
\]

But the only cubes of units modulo 9 are 1 and -1, whereas the
right side of (11) is 4 or -4. This is impossible.

Thus every remaining exponent a>=10 is excluded.

## 3. The six possibilities at a=7

It remains to check a=7, n=2187. Here alpha=6, q=729,
d=4, and the broad gap in (1) gives

\[
r=81v,\qquad 81<v<90,\qquad 3\nmid v.
\]

Therefore

\[
v\in\{82,83,85,86,88,89\}.
\]

The factor H and normalized value (8) are unchanged. The unit
factors with v_3(m)=alpha-1 are indexed by

\[
1\le s\le\left\lfloor\frac{r-1}{q/3}\right\rfloor,
\qquad 3\nmid s.
\]

For v=82,83 the upper endpoint is 27, giving unit product U=1.
For v=85,86 it is 28, giving the extra factor 7 and U=7.
For v=88,89 it is 29, giving two extra factors 7 and 4 and U=1.
Thus the two sides of the original equation, divided by 3^(2d),
would have to satisfy

\[
4(-1)^v Uv^{-1}\equiv v^2\pmod9.
\]

The exact residue table is

| v | r | U modulo 9 | L/3^(2d) modulo 9 | (X+Y)/3^(2d) modulo 9 |
|---:|---:|---:|---:|---:|
| 82 | 6642 | 1 | 4 | 1 |
| 83 | 6723 | 1 | 7 | 4 |
| 85 | 6885 | 7 | 2 | 7 |
| 86 | 6966 | 7 | 2 | 7 |
| 88 | 7128 | 1 | 7 | 4 |
| 89 | 7209 | 1 | 4 | 1 |

No row agrees. This completes the theorem for every a.

## Verification status and scope

The proof above is exact and finite where it uses a table. It does
not rely on an unbounded numerical search, a floating-point comparison,
or a claim that all cases of the original equation have been solved.
The new argument is not yet formalized in Lean. Its inputs include the
previous complete exclusion for ell=1,j<=100 and the analytic and
valuation results explicitly stated in the companion structure note.

The root proof reviewer and the independent `v5_l1_gap` reviewer both
checked the complete proof and reported no correction needed. The latter
also checked the six final rows directly with exact integer binomials.
`v5_offset_three_checks.py` reproduces the rows by exact `math.comb`, by
stripping the factors of 3 from each factor in the binomial product, and
by the explicit block formula above. Its compact result is recorded in
`v5_offset_three_verification.json`.
