# A common-prime sieve for the remaining L1 offset-four strip

## Scope

Retain the original squared-index equation in the L1 family, and put

\[
i=n,\quad j=n-4,\quad k=b,\quad\ell=b-1,
\qquad A=\binom n4,
\]

\[
L=\binom Ab,\qquad
X=\binom{n^2}{8n-16},\qquad
Y=\binom{b^2}{2b-1}.
\]

The equation is \(L=X+Y\). The preceding reductions leave the strip

\[
b\ge22,\qquad
\frac52(n-4)\le b<\frac83(n-4).
\tag{1}
\]

In particular \(22<8(n-4)/3\), so the integer \(n\) satisfies
\(\boxed{n\ge13}\). This note gives an additional necessary
congruence condition throughout (1). It does not exclude the strip.

## 1. Exact factors shared by the two binomial numerators

Define

\[
z=n^2-3n+1.
\]

The quartic identity

\[
24A=n(n-1)(n-2)(n-3)=z^2-1
\tag{2}
\]

implies the following. For any positive integer \(u\) such that

\[
u^2\equiv1\pmod{24},\qquad
s:=\frac{u^2-1}{24}<b,
\tag{3}
\]

we have \(0\le s\le b-1\) and

\[
\boxed{24(A-s)=(z-u)(z+u).}
\tag{4}
\]

The number \(A-s\) occurs in the numerator product for \(L\).
Both factors on the right occur in the numerator product for \(X\),
as the following explicit interval check shows.

From (3) and the upper bound in (1),

\[
u^2=24s+1\le24b-23
<64(n-4)-23<64n,
\]

so \(u<8\sqrt n\). For \(n\ge13\),

\[
(3n-1)^2-64n=n(9n-70)+1>0,
\qquad 3n-1<5n-16.
\]

Thus \(u<3n-1<5n-16\), and consequently

\[
\boxed{
n^2-8n+17<z-u<z+u<n^2.
}
\tag{5}
\]

The numerator factors of \(X=\binom{n^2}{8n-16}\) are precisely
the consecutive integers from \(n^2-8n+17\) through \(n^2\).
Equation (5) proves the asserted inclusion.

## 2. A sufficiently large shared prime forces a short residue

Suppose a prime \(p\) satisfies

\[
p>8n-16,
\qquad p\mid(z-u)(z+u)
\tag{6}
\]

for some \(u\) satisfying (3). Since \(n\ge13\), this prime
does not divide 24. Equation (4) therefore gives \(p\mid A-s\).

The upper bound for \(b\) gives

\[
b<\frac83(n-4)<8n-16,
\]

and

\[
2b-1<\frac{16}{3}(n-4)-1<8n-16,
\]

where the difference in the final comparison is
\((8n+19)/3>0\). Hence \(p\) exceeds all three denominator
lengths \(b\), \(8n-16\), and \(2b-1\).

In particular \(p\nmid b!\), so \(p\mid A-s\) implies
\(p\mid L\). By (5), \(p\) divides a numerator factor of
\(X\); since \(p\nmid(8n-16)!\), it also divides \(X\).
The equation \(L=X+Y\) would then force \(p\mid Y\).

Finally, \(p>2b-1\) makes the denominator \((2b-1)!\)
invertible modulo \(p\). Thus

\[
\begin{aligned}
p\mid Y
&\iff p\mid\prod_{h=0}^{2b-2}(b^2-h)\\
&\iff b^2\equiv h\pmod p
\quad\text{for some }0\le h\le2b-2\\
&\iff \boxed{b^2\bmod p\le2b-2}.
\end{aligned}
\tag{7}
\]

The last equivalence uses the least nonnegative residue, and the
fact that \(2b-2<p\).

Therefore the complete sieve statement is

\[
\boxed{
\begin{gathered}
u>0,\quad u^2\equiv1\pmod{24},\quad
(u^2-1)/24<b,\\
p\text{ prime},\quad p>8n-16,\quad
p\mid(z-u)(z+u),\\
b^2\bmod p>2b-2
\quad\Longrightarrow\quad L\ne X+Y.
\end{gathered}}
\tag{8}
\]

## 3. What is proved and what remains open in this approach

Equations (4)--(8) are exact, uniform necessary conditions. No
numerical scan is used in this note.

It has **not** been proved that every pair \((n,b)\) in (1) has
a prime satisfying the rejecting conditions in (8). In particular,
this note supplies neither a uniform existence theorem for a large
prime among the factors \(z\pm u\), nor a proof that one of those
primes must fail (7).

There are only \(O(\sqrt n)\) admissible positive values of \(u\),
and each exposed factor is \(O(n^2)\). Their full product is
therefore at most \(\exp(O(\sqrt n\log n))\). In contrast,
\(b=\Theta(n)\) in (1), and the elementary bounds

\[
\left(\frac{b^2}{2b-1}\right)^{2b-1}
\le\binom{b^2}{2b-1}
\le(b^2)^{2b-1}
\]

show \(Y=\exp(\Theta(n\log n))\). Consequently, the factors
explicitly exposed here do not by themselves yield a contradiction
just by producing a common divisor larger than \(Y\).

The unresolved task is to guarantee a prime with the residue failure
in (8), or to combine these necessary conditions with additional
structure. This note does not claim a complete exclusion or a Lean
formalization.
