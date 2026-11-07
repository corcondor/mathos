# Exact finite certificate for j=1, ell=k-2 in the upper branch

The analytic common-prime-product theorem and its sharper bound reduce
this family to \(23\le k<2^{20}\). Put
\(m=k-2\), \(B=k(k-1)/2\), \(A=B+t\), \(N=k^2\), and \(q=4k-4\).
Earlier necessary bounds give

\[
\max(k,\lfloor\varphi m\rfloor+1)\le t\le
\min\bigl(B,c_km-1\bigr),\qquad
c_k=\begin{cases}10&k<802,\\5&k\ge802.\end{cases}
\]

Here \(\lfloor\varphi m\rfloor=(m+\lfloor\sqrt{5m^2}\rfloor)//2\),
so these endpoints are exact integers.

Write \(L(t)=\binom{B+t}{t}\) and \(Y=\binom Nq\).
Since \(A\le2B<N\), and
\(Y\ge\binom N3>N^2\) for every \(k\ge23\), a solution must have

\[
Y<L(t)=Y+A^2<2Y. \tag{1}
\]

The function \(L(t)\) strictly increases on the positive integers,
because \(L(t+1)/L(t)=(B+t+1)/(t+1)>1\). Thus two verified
endpoints with \(L(a)<Y\) and \(L(b)>2Y\) exclude all
\(t\le a\) and \(t\ge b\). Only the integers strictly between
the endpoints need a congruence check.

The C++ generator uses floating point to propose endpoints. That has no
logical role: every proposed endpoint is checked by the integer bounds
below, and moved outward until certified. For \(k<1024\), every integer
in the necessary interval is retained without using logarithms.

## 1. Exact integer logarithm intervals

Set \(Q=2^{56}\). For \(0\le z\le1/3\),

\[
2\operatorname{atanh}z
=2\sum_{a=0}^{23}\frac{z^{2a+1}}{2a+1}+R,
\quad 0\le R\le\frac9{196\cdot3^{49}}<\frac1Q.
\]

In the code `logseries`, set
\(r=\lfloor Qz\rfloor\), \(s=\lfloor r^2/Q\rfloor\),
\(p_0=r\), and \(p_{a+1}=\lfloor p_as/Q\rfloor\).
All these values divided by \(Q\) are lower bounds for the
corresponding powers. The normalized error of \(s\) is less than
\(2/Q\). Induction gives

\[
0\le z^{2a+1}-p_a/Q\le(1+4a)/Q.
\]

Therefore each rounded term
\(\lfloor p_a/(2a+1)\rfloor/Q\) has error less than \(3/Q\).
After multiplying the sum by 2 and including the tail, its total error
is less than \(145/Q\), hence certainly less than \(256/Q\).

For an integer \(n\ge1\), let \(e=\lfloor\log_2 n\rfloor\),
\(u=2^e\). Then

\[
\log n=e\log2+2\operatorname{atanh}\frac{n-u}{n+u},
\]

where both atanh arguments (including \(1/3\) for \(\log2\))
are at most \(1/3\). Thus `logint(n)` returns exact integers
\(l_n,h_n\) such that

\[
l_n\le Q\log n\le h_n,
\qquad h_n-l_n=256(e+1).
\tag{2}
\]

No floating point operation occurs in (2).

## 2. A binomial ratio interval without subtracting enormous factorials

Robbins' factorial remainder satisfies, for positive integers \(r\),

\[
\log r!=(r+1/2)\log r-r+\tfrac12\log(2\pi)+\rho_r,
\qquad \frac1{12r+1}<\rho_r<\frac1{12r}.
\tag{3}
\]

For \(1\le r<n\), put

\[
a(n,r)=\frac{r(r-1)}{2n},\qquad
b(n,r)=\frac{r(r-1)(2r-1)}{12n(n-r+1)}.
\]

The elementary series for \(\log(1-x)\) gives

\[
-a(n,r)-b(n,r)\le
E(n,r):=\sum_{s=0}^{r-1}\log(1-s/n)\le-a(n,r).
\tag{4}
\]

Indeed the remainder after \(-x\) is between
\(-x^2/[2(1-u)]\) and zero whenever \(0\le x\le u<1\),
and one takes \(u=(r-1)/n\), then sums the squares.

Consequently, if \(D=\log L(t)-\log Y\) and

\[
F=t\log A-(t+1/2)\log t+t-q\log N+(q+1/2)\log q-q
-a(A,t)+a(N,q),
\]

then

\[
F+\frac1{12q+1}-\frac1{12t}-b(A,t)
<D<
F+\frac1{12q}-\frac1{12t+1}+b(N,q).\tag{5}
\]

The generator evaluates the two sides of (5) in units of \(1/(2Q)\),
using (2) with the appropriate rounding direction for every logarithm
and exact floor/ceiling division for each rational term. Thus its
returned integers satisfy `lo <= 2Q*D <= hi`.

If `hi < 0`, this certifies \(L(t)<Y\). If
`lo > 2*LOG2_HI`, this certifies \(L(t)>2Y\). The constant
`LOG2_HI` is the rigorously proved upper bound for \(Q\log2\).

All integer intermediates fit the stated C++ types. The largest product
in a rational numerator is \(r(r-1)(2r-1)Q\), with
\(r<5\cdot2^{20}\) for \(k\ge802\), and \(r<8020\) otherwise.
It is less than \(2(5\cdot2^{20})^3 2^{56}=250\cdot2^{116}<2^{124}\),
well below the unsigned 128-bit limit. The remaining denominators,
logarithm products, and sums are smaller. Binomial inputs are below
\(2^{40}\). Integer square root is corrected with exact integer
comparisons after its floating point proposal.

## 3. Lucas congruence witnesses and binary format

For each remaining integer \(t\), the generator finds a prime
\(p<1000\) for which

\[
\binom{B+t}{t}\not\equiv (B+t)^2+\binom{k^2}{4k-4}\pmod p.
\tag{6}
\]

Both binomials are evaluated by Lucas' theorem. The candidate is
excluded only after such a witness has been found; any survivor causes
the generator to stop with a nonzero exit code.

The certificate begins with the seven ASCII bytes `V4J1CP2` followed by a
null byte (eight bytes in total). Three little-endian unsigned 32-bit words give the first k,
exclusive last k, and the small-k cutoff. For each consecutive k, two
more words give endpoints `lo, hi`; the following `hi-lo-1` bytes give
the zero-based indices of the witness primes in the increasing list of
primes below 1000. There are no gaps in k coverage.

An independent verifier must check the endpoints (or that they coincide
with the necessary interval boundary), every congruence witness, and
that the file ends at exactly the specified position.

## Primary reference for (3)

H. Robbins, *A Remark on Stirling's Formula*, American Mathematical
Monthly 62 (1955), 26–29, DOI https://doi.org/10.2307/2308012 .
Author's article available at
https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf .

## Status

The complete generator run covered all 1,048,553 integers
\(23\le k<2^{20}\) and produced 5,455,320 Lucas witnesses using
primes at most 19, with zero survivors. The independent verifier
`v4_upper_complement_two_j1_verify.cpp` recalculated every endpoint and
every witness using different interval arithmetic and a different
Lucas implementation; it passed. Its report is
`v4_upper_complement_two_j1_verification.json`.

The full upper \(\ell=k-2\) theorem, including the separate
effective-index \(d\ge3\) certificate, is assembled in
`v4_upper_complement_two_complete.md`.
