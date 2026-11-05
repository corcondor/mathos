# A stronger restriction on large prime factors when ell=1

Throughout this note the original equation is

\[
\binom{A}{B}=X+B^2,\qquad
A=\binom ij,\quad X=\binom{i^2}{j^2},\quad B=k,
\]

and \(r=\min(B,A-B)\). The previous endpoint and size reductions
give \(j+2\le r\), and, if \(i\ge2j\), \(r<2j\).
The independently proved denominator lemma gives

\[
q:=i/\gcd(i,j)\mid r^3.
\tag{1}
\]

All congruences between rational products below are in the localization
of the integers at p: after cancellation their denominators are coprime
to p. The normalized binomial coefficients on the left are integers,
so those congruences also have their ordinary integer meaning. The
harmonic congruence in Section 3 uses modular inverses of its
denominators, which are all less than p.

## 1. The only possible shape if p>j divides i

Suppose \(i\ge2j\) and a prime \(p>j\) divides i. Since
\(p\nmid j\), (1) gives \(p\mid r\). The inequalities
\(j+2\le r<2j<2p\) force \(r=p\).

Let \(g=\gcd(i,j)\). Equation (1) now says \(i/g\mid p^3\),
so \(i=g p^a\) for some \(1\le a\le3\); here \(p\nmid g\).
The product identities for the two inner coefficients give

\[
v_p(A)=a,\qquad v_p(X)=2a.
\]

Indeed j<p, j²<p², and each noninitial factor of
\(\binom{i^2}{j^2}=i^2/j^2\prod_{h=1}^{j^2-1}(i^2-h)/h\)
is a p-adic unit. Similarly
\(v_p\binom Ap=a-1\).

If a=1, the latter is zero while both X and B² are divisible by p²,
a contradiction. If a>=2, then \(v_p(B^2)=2\), in both the
lower case B=p and the upper case B=A−p, whereas \(v_p(X)=2a>2\).
Thus \(a-1=2\), so a=3.

Modulo p, normalization by p² in the original equation gives

\[
\frac{\binom Ap}{p^2}\equiv
\frac{g(-1)^{j-1}}j\equiv1\pmod p.
\tag{2}
\]

Here p is odd: p=2 would imply j=1 and contradict r=p>=j+2.
Write \(j=gu\). Then (2) implies
\(u\equiv(-1)^{j-1}\pmod p\). But
\(1\le u\le j\le p-2\). Hence the sign is positive and u=1.
Consequently

\[
\boxed{i=j p^3,\qquad j\text{ odd},\qquad r=p,
\qquad j+2\le p<2j.}
\tag{3}
\]

This is only a necessary condition; it does not exclude the lower
branch.

## 2. The upper branch is impossible at the next precision

Assume the upper case \(B=A-p\). From (3),

\[
a_0:=A/p^3
=\prod_{h=1}^{j-1}\left(1-\frac{jp^3}{h}\right)
\equiv1\pmod{p^3}.
\tag{4}
\]

The sign in this identity is positive because j is odd, and h<p
in every factor. Likewise, p is odd and every h in 1,...,p−1 is a
p-adic unit, so

\[
\frac{\binom Ap}{p^2}
=a_0\prod_{h=1}^{p-1}\left(1-\frac A h\right)
\equiv1\pmod{p^3}.
\tag{5}
\]

But \(v_p(X)=6\), hence \(X/p^2\equiv0\pmod{p^3}\), while

\[
\frac{(A-p)^2}{p^2}
=(p^2a_0-1)^2\equiv1-2p^2\pmod{p^3}.
\tag{6}
\]

Dividing the original equation by p² and comparing (5) with (6)
would give \(2p^2\equiv0\pmod{p^3}\), or p|2, impossible.
Thus no solution with i>=2j in the upper ell=1 branch can have a
prime divisor of i greater than j.

If i<2j and p>j divides i, then i=p, since 2p>2j>i.
The earlier complete exclusion of prime i with ell=1 applies
(`prime_first_ell_one.md`). Therefore the final uniform conclusion is

\[
\boxed{\ell=1,\quad B\ge A/2
\quad\Longrightarrow\quad P^+(i)\le j.}
\tag{7}
\]

Here \(P^+(i)\) denotes the largest prime divisor of i. The result
is a necessary condition on any hypothetical solution, not an
exclusion of the entire upper branch.

## 3. An optional stronger condition in the lower branch

For completeness, the same products also give an explicit harmonic
congruence in the remaining lower case (3):

\[
\boxed{jH_{j-1}\equiv-p\pmod{p^2},\qquad
H_m=\sum_{h=1}^{m}\frac1h.}
\tag{8}
\]

Here j is odd and j+2<=p<2j, so j>=3 and p>=5. We include the
short proof to specify the exact strength of the condition.

First, \(H_{p-1}\equiv0\pmod{p^2}\). Pairing h and p−h gives
\(1/h+1/(p-h)\equiv-p/h^2\pmod{p^2}\). The half sum of
\(1/h^2\) vanishes modulo p: twice that half sum equals the full
sum modulo p, and the full sum is \(\sum_{h=1}^{p-1}h^2\equiv0\pmod p\)
because inversion permutes the nonzero residues and p>=5. This
proves the claimed harmonic congruence without an external theorem.

Expanding (4) one order further and then the product in (5) gives

\[
a_0\equiv1-jp^3H_{j-1}\pmod{p^6},\qquad
\frac{\binom Ap}{p^2}\equiv a_0\pmod{p^5}.
\]

For the second congruence the linear term A H_(p−1) is divisible by
p⁵, and all higher products by p⁶. Also

\[
\frac X{p^6}
=\prod_{h=1}^{j^2-1}\left(1-\frac{j^2p^6}{h}\right)
\equiv1\pmod p,
\]

as j²<p² and j² is odd. The lower equation, divided by p² and
reduced modulo p⁵, is therefore

\[
1-jp^3H_{j-1}\equiv1+p^4\pmod{p^5},
\]

which is exactly (8). Harmonic zeros and these higher congruences
are genuine additional restrictions; this note makes no claim that
(8) is impossible for all p and j.

## Verification status

This is a written exact p-adic proof, building on the earlier endpoint,
size, prime-i, and cubic-divisibility lemmas. No Lean formalization of
this strengthening or of the harmonic calculation is claimed.
