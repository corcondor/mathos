# v13: exact parity-normalized descent of the auxiliary cubic

Date: 2026-11-06 JST. This is an unformalized mathematical note about
the auxiliary cubic, not an equivalence with the original binomial equation.

## Exact allocation theorem

Assume n,H,T are positive integers, n>=3, gcd(H,T)=1, and H|n-2.
For positive rational q, define

\[
\rho(q)=\prod_p p^{v_p(q)\bmod3},
\]

where each exponent is chosen from {0,1,2}, including for negative
valuations. Thus q=rho(q)*lambda^3 for a unique positive rational lambda.

Let epsilon=0 if n is odd and epsilon=1 if n is even. Define

\[
(f_0,f_1,f_2)=
\begin{cases}
(n,n-1,n-2),&\varepsilon=0,\\
(n/2,n-1,(n-2)/2),&\varepsilon=1,
\end{cases}
\qquad
D_\varepsilon=\rho\!\left(\frac{6H}{4^\varepsilon T}\right).
\]

The three f_i are positive and pairwise coprime. For odd n, the possible
gcd of n and n-2 divides 2 and is odd. For even n, n/2 and (n-2)/2 are
consecutive, while n-1 is twice either of them plus or minus 1.

If a positive integer r satisfies

\[
6Hr^3=Tn(n-1)(n-2),
\tag{1}
\]

then f_0*f_1*f_2=(6H/(4^epsilon*T))*r^3. The unique decompositions
f_i=d_i*a_i^3 therefore satisfy

\[
\gcd(d_i,d_j)=1\quad(i\ne j),\qquad d_0d_1d_2=D_\varepsilon.
\tag{2}
\]

Each d_i is positive and cube-free. Each prime-power factor of
D_epsilon is placed wholly into exactly one slot; there are
3^omega(D_epsilon) allocations before further restrictions, not three
independent choices of arbitrary supported coefficients.

The two simultaneous equations become:

| Parity | Cubic equations | Extra condition |
|---|---|---|
| Odd | d0*a0^3-d1*a1^3=1; d1*a1^3-d2*a2^3=1 | d0*a0^3 odd; H divides d2*a2^3 |
| Even | d0*a0^3-d2*a2^3=1; d1*a1^3-2*d2*a2^3=1 | H divides 2*d2*a2^3 |

All a_i must be positive integers. Zero coordinates are not admitted.

## Converse, including integrality

Conversely take a coefficient allocation (2) and positive bases satisfying
the relevant two equations and extra conditions. Reconstruct n from f_0
(twice f_0 in the even case). Write

\[
\frac{6H}{4^\varepsilon T}=D_\varepsilon\lambda^3.
\]

Then r=a0*a1*a2/lambda is positive rational and satisfies (1). In fact it
is automatically an integer. Since H|n-2,

\[
r^3=\frac{Tn(n-1)((n-2)/H)}6.
\]

The denominator of this rational cube divides 6. If r=a/b is reduced,
b^3 divides 6, hence b=1. Finally A/r^3=H/T, where A=binom(n,3), and
gcd(H,T)=1 recover H=A/gcd(A,r^3) and T=r^3/gcd(A,r^3).
Thus the descent is exact for the primitive auxiliary system.
The original binomial equality imposes additional conditions.

## Forced allocations at primes dividing H

If p>=5 and p^h exactly divides H, then p divides n-2 and divides neither
n nor n-1 nor T. Consequently

\[
v_p(f_2)=h+3v_p(r).
\]

When h is not divisible by 3, the corresponding prime-power factor of
D_epsilon is forced into d_2. At the exceptional primes:

- If 3^h exactly divides H, h>0, then v3(f2)=h+1+3*v3(r). The residue
  exponent is (h+1) mod 3.
- If 2^h exactly divides H, h>=2, then n=2 mod 4 and
  v2(f2)=h-1+3*v2(r). The residue exponent is (h-1) mod 3.
- If v2(H)=1, T is odd, D1 is odd, and v2(f0*f2)=3*v2(r)>=1;
  in particular r is even. The even normalized factor may be f0 or f2.
- For odd n, H is odd and any factor 2 in D0 must go into d1.
- For even n, f1 is odd, so any factor 2 in D1 goes into d0 or d2.

A prime whose adjusted exponent is 0 mod 3 disappears from D_epsilon;
its divisibility requirement in H|n-2 still constrains the cube bases.

## A uniform prime-support obstruction

At least two of d0,d1,d2 must exceed 1. Therefore

\[
\boxed{\omega(D_\varepsilon)\ge2.}
\tag{3}
\]

For odd n, two coefficients equal to 1 would give distinct positive
cubes differing by 1 or 2, impossible because the smallest gap is 7.

For even n, d0=d2=1 would give consecutive positive cubes. If d0=d1=1,
then (1,a0^3,a1^3) is a nonconstant arithmetic progression of rational
cubes with nonzero center. If d1=d2=1, the same holds for
(-1,a2^3,a1^3). Both contradict the classical theorem of Legendre:
the only rational three-term progressions of cubes are constant or
proportional to (-1,0,1). See [G], Section 2 and Corollary 3.
The zero-centered exception does not occur here, because every a_i>0.

For m=omega(D)>=1, at most 3^m-3 allocations remain after discarding the
three allocations putting all prime factors into a single slot.

### An unbounded illustration

Take H=6*a^3 and T=(10*a+1)^3 for a>=1, a not congruent to 2 mod 3.
Then gcd(H,T)=1 and

\[
162<\frac{T}{H}=\frac{(10+1/a)^3}{6}\le\frac{1331}{6}<229.
\]

Any n with H|n-2 is even, but

\[
D_1=\rho\!\left(9\left(\frac a{10a+1}\right)^3\right)=9,
\]

contradicting (3). This rules out these pairs (H,T) with arbitrarily
large H. It does not rule out every possible T for each of those H.
The stronger T-support result of [v13_uniform_cube_support.md](v13_uniform_cube_support.md)
already contains this illustrative family.

## Why a bare congruence sieve is insufficient

The unsplit equation (1) always has n=2,r=0 modulo every modulus, also
compatible with H|n-2. A congruence alone cannot distinguish these
residues from large positive integers. The positivity restrictions and
global results on cubic equations are necessary ingredients here.

A useful auxiliary-point control is (n,r,H,T)=(169,546,167,34398). It
satisfies (1), primitive gcd conditions, H|n-2, n>=104, 3n<r<10n/3,
and 162H<T<229H. Its odd cores are (169,21,167), so (3) properly retains
it. This tuple is not asserted to solve the original binomial equation;
other existing necessary conditions may exclude it.

## Status and reference

The argument was independently audited by another AI checker, including
the converse, exceptional primes, positivity, and the zero-centered
exception in the classical theorem. Small numerical consistency checks
were used only as checks, not as a proof for all n. No Lean execution or
3-Selmer-group computation was performed in this version.

[G] E. Gonzalez-Jimenez, *Three cubes in arithmetic progression over
quadratic fields*, Archiv der Mathematik 95 (2010), 233-241,
Section 2 and Corollary 3.
https://arxiv.org/html/0909.0227v1
