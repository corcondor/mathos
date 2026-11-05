# Lower ell=1: one real candidate per large prime, and a fifth-order harmonic test

## Scope and status

This note continues the **original squared-index equation**

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

It concerns only the lower branch with ell=1 and a prime p>j dividing i.
The exact reductions proved in `v4_ell_one_large_prime_strengthening.md`
already give

\[
i=jp^3,\qquad k=p,\qquad j\text{ odd},\qquad j+2\le p<2j.
\tag{1}
\]

Put

\[
A=\binom{jp^3}{j},\qquad
X=\binom{j^2p^6}{j^2},\qquad
L=\binom Ap.
\]

The remaining equation is L=X+p². We prove two new uniform necessary
conditions:

1. For every prime p>=23, at most **one integer j** can satisfy the
   equation. It lies in an explicit real interval of length less than
   1/(9 p log p), with no upper bound imposed on p.
2. That j must satisfy an explicit harmonic congruence modulo p^5,
   strengthening the previous congruence modulo p².

These are written mathematical proofs. They are not a proof that this
whole branch is empty, and they have not been formalized in Lean.
The primes below 23 fall inside the already excluded range j<=100.

## 1. An explicit narrow interval

For real x>0 define

\[
\begin{split}
G(x,p)={}&px(1+3\log p)-x^2(1+6\log p)\\
&-(p+\tfrac12)\log p+p
-\frac p2\log(2\pi x)+\log x.
\end{split}
\tag{2}
\]

**Theorem.** For p>=23 there is a unique root xi_p of G(x,p)=0 in
(p/2,p). If (1) is a solution of L=X+p², then

\[
\boxed{\quad
\xi_p-\frac1{9p\log p}<j<\xi_p.
\quad}
\tag{3}
\]

In particular the only possible integer is ceil(xi_p)-1, and it still
has to pass every other necessary condition. An interval of this width
often contains no integer at all.

### 1.1 Exact error control

Write

\[
\log(n!)=(n+\tfrac12)\log n-n+\tfrac12\log(2\pi)+\rho_n,
\qquad
\frac1{12n+1}<\rho_n<\frac1{12n}.
\tag{4}
\]

These are Robbins' rigorous factorial bounds, not an unbounded
asymptotic approximation. Define

\[
E(n,m)=\sum_{h=0}^{m-1}\log(1-h/n).
\]

For 1<=m<=n, the inequality -log(1-t)<=t/(1-t) gives

\[
0\le-E(n,m)\le\frac{m(m-1)}{2(n-m+1)}.
\tag{5}
\]

Let E_A=E(jp³,j), E_X=E(j²p^6,j²), E_L=E(A,p), and set
D=log L-log X. Applying (4) to j!, (j²)!, p!, and using the numerator
product for each binomial coefficient gives the exact identity

\[
D=G(j,p)-\rho_p-p\rho_j+\rho_{j^2}
       +pE_A+E_L-E_X.
\tag{6}
\]

We now prove the deliberately simple uniform bound

\[
\boxed{G(j,p)-\tfrac14<D<G(j,p)}
\qquad(p\ge23,\ p/2<j<p).
\tag{7}
\]

First, binom(n,m)>=(n/m)^m, so A>=p^(3j)>=p^6. Equations (4)-(5)
give

\[
\begin{gathered}
\rho_p<\frac1{12p},\qquad p\rho_j<\frac16,\\
-pE_A<\frac{p(j-1)}{2(p^3-1)}
      <\frac1{2(p-1)},\qquad
-E_L<\frac1{p^4}.
\end{gathered}
\]

Dropping the two positive terms rho_(j²) and -E_X in (6), the total
negative error is therefore less than

\[
\frac1{276}+\frac16+\frac1{44}+\frac1{23^4}<\frac14.
\]

This proves the left side of (7). For the right side, the only positive
terms obey

\[
\rho_{j^2}-E_X
<\frac1{3p^2}+\frac1{p^4}<\frac1{13},
\]

whereas

\[
p\rho_j>\frac{p}{12j+1}>\frac1{13}.
\]

All remaining error terms in (6) are nonpositive, so D<G(j,p).

If L=X+p², then X>=p^(6j²) and

\[
0<D=\log(1+p^2/X)<p^2/X<p^{-4}.
\]

Together with (7), this proves

\[
\boxed{0<G(j,p)<\frac14+p^{-4}<\frac13.}
\tag{8}
\]

### 1.2 The interval is shorter than one integer spacing

For x>p/2 and p>2,

\[
\frac{\partial G}{\partial x}
=p(1+3\log p)-2x(1+6\log p)-\frac{p/2-1}{x}
<-3p\log p.
\tag{9}
\]

Thus G is strictly decreasing on (p/2,p). To check that it crosses
zero, observe that G(p,p)<0 and

\[
G(p/2,p)
=\frac{p^2}{4}-(\tfrac32p-\tfrac12)\log p
-\frac p2\log\pi+p-\log2.
\tag{10}
\]

Call the expression in (10) F(p). The elementary bounds
log 23<7/2, log pi<3/2, log 2<1 give F(23)>18 and F'(23)>5.
Moreover

\[
F''(p)=\frac12-\frac3{2p}-\frac1{2p^2}>0\qquad(p\ge23).
\]

Consequently F(p)>0 throughout the desired range. The unique root
xi_p therefore exists. The mean value theorem, (8), and (9) give

\[
3p\log p\,(\xi_p-j)<G(j,p)<\frac13,
\]

which is exactly (3).

The width in (3) tends to zero. This is a reduction for all primes,
not a statement obtained by checking a finite box of (i,j,k,ell).

For orientation only, solving the leading terms of (2) gives

\[
\xi_p=
\frac{p(1+3\log p)}{1+6\log p}
-\frac12+O\!\left(\frac1{\log p}\right)
=\frac p2+\frac{p}{12\log p+2}
-\frac12+O\!\left(\frac1{\log p}\right).
\]

The proof and any exclusion should use (2)-(9), not this asymptotic
orientation formula.

## 2. A necessary congruence modulo p^5

Write

\[
H=H_{j-1},\quad H_2=\sum_{h=1}^{j-1}\frac1{h^2},\quad
K=H_{p-1},\quad K_2=\sum_{h=1}^{p-1}\frac1{h^2}.
\]

All these denominators are coprime to p. Rational congruences below
therefore mean ordinary congruences after modular inversion.
The earlier proof already shows H=0 (mod p), K=0 (mod p²), and

\[
jH\equiv-p\pmod{p^2}.
\tag{11}
\]

**Proposition.** Every solution in (1) satisfies

\[
\boxed{
jH+K+\frac{p^3}{2}\bigl(j^2H_2+K_2\bigr)
\equiv-p\pmod{p^5}.
}
\tag{12}
\]

In particular

\[
\boxed{jH+K\equiv-p\pmod{p^3}.}
\tag{13}
\]

### Proof

The sign of the following product is positive because j is odd:

\[
a_0:=A/p^3
=\prod_{h=1}^{j-1}(1-jp^3/h).
\]

Keeping the linear and quadratic terms yields

\[
a_0\equiv
1-jp^3H+\frac{j^2p^6}{2}(H^2-H_2)
\pmod{p^9}.
\tag{14}
\]

Since H is divisible by p, a_0=1 (mod p^4). Also

\[
\frac L{p^2}
=a_0\prod_{h=1}^{p-1}(1-A/h)
\equiv a_0-Aa_0K+\frac{A^2a_0}{2}(K^2-K_2)
\pmod{p^9}.
\tag{15}
\]

For reduction modulo p^8, the term H² in (14) disappears because
p² divides H², and the term K² in (15) disappears because p^4
divides K². Since A=p³a_0, a_0=1 (mod p^4), and p² divides K,
replacing Aa_0 by p³ and A²a_0 by p^6 in the relevant terms
does not change their residues modulo p^8. Therefore

\[
\frac L{p^2}\equiv
1-p^3(jH+K)-\frac{p^6}{2}(j^2H_2+K_2)
\pmod{p^8}.
\tag{16}
\]

On the other side,

\[
\frac X{p^6}
=\prod_{h=1}^{j^2-1}(1-j^2p^6/h)
\equiv1\pmod{p^5}.
\tag{17}
\]

Indeed h<j²<p², so v_p(h)<=1, making every correction in (17)
divisible by p^5. Again j² is odd, so the product sign is positive.
Dividing L=X+p² by p², (17) makes its right side congruent to
1+p^4 modulo p^8. Comparing with (16) and dividing by p³ proves
(12). Reduction modulo p³ proves (13).

## 3. A precise connection with current harmonic-number research

The 2025-online / 2026-volume paper by Carofiglio, Cherubini, and
Gambini studies

\[
\mathcal J_p=\{n\ge1:v_p(H_n)\ge1\}
\]

using the exact p-adic recursion

\[
H_{pn+b}\equiv H_n/p+H_b\pmod p
\qquad(0\le b<p).
\tag{18}
\]

In the usual rooted tree, n has a child pn+b precisely when the
corresponding harmonic congruence holds. Our previous condition (11)
has the following exact interpretation:

\[
\boxed{
jH_{j-1}\equiv-p\pmod{p^2}
\quad\Longleftrightarrow\quad
j-1\in\mathcal J_p\ \text{and}\ p(j-1)+j\in\mathcal J_p.
}
\tag{19}
\]

To prove this, put n=j-1. If (11) holds, then H_n=0 (mod p),
H_n/p=-1/j (mod p), and H_j=1/j (mod p); apply (18).
Conversely, membership of both n and pn+j gives
H_n+pH_j=0 (mod p²). As H_j=H_n+1/j and H_n=0 (mod p), this
reduces to H_n=-p/j (mod p²).

Thus our surviving candidate must occupy a specified edge of the
harmonic-zero tree: the base-p digits of the child are the consecutive
integers j-1 and j. The new condition (12) is stronger still.

One immediate exclusion is worth spelling out. A *harmonic prime* is
a prime for which

\[
\mathcal J_p=\{p-1,p^2-p,p^2-1\}.
\]

Every harmonic prime is impossible in (1), because (19) would require
0<j-1<p-1 to belong to that set. This excludes a structurally defined
class of primes without imposing a numerical bound. The cited paper
does not prove that every prime is harmonic, and no such assertion is
being used.

This connection does **not** prove that the original binomial equation
is a known open problem. Nor does the paper establish that the
specific edges in (19) never occur. It provides a precise link to
modern p-adic harmonic-number algorithms; any claimed exclusion
still needs a proved argument or an explicitly bounded certificate.

## 4. What the reduction achieves, and what remains

In this whole large-prime subfamily, any hypothetical solution must
pass the following sequence, for an otherwise unbounded prime p:

1. Locate the unique real zero xi_p of the explicit function (2).
2. Check whether its interval in (3) contains an integer j. There is
   at most one; j must also be odd and satisfy the earlier size bounds.
3. Check the explicit harmonic congruence (12).
4. If it passes, the original exact equality still requires proof or
   disproof. Necessary conditions are not sufficient conditions.

The remaining obstacle is not four-variable exhaustive search in this
subfamily: the reductions leave at most one candidate for each prime.
There is still no proved finite upper bound for p, and no argument here
excludes that last candidate for every prime.

## 5. Audit and computational verification

The root agent independently audited the exact identity (6), the
error estimates leading to (7), the existence and derivative proof
for (3), and the product expansion leading to (12), and found no gap.
The companion `v5_large_prime_localization_checks.py` supplies a small
numerical sanity report rather than a large search:

- It encloses each logarithm by exact rational series bounds, including
  a Machin-formula enclosure of pi, and uses these intervals to locate
  the last integer with G(j,p)>0 for several representative primes.
- It compares the expression in (12) with the exact integer residual
  -(L-X-p²)/p^5 modulo p^5 at three nontrivial harmonic-zero examples.
  These are identity checks, not new claims of an unbounded exclusion.

The checks are additional verification of the calculations. The
theorems above rest on the displayed proofs, not on the chosen sample
values. No Lean formalization of this note is claimed.

## References

- Herbert Robbins, *A Remark on Stirling's Formula*, American
  Mathematical Monthly 62 (1955), 26-29, DOI 10.2307/2308012.
  Primary-paper scan:
  https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf
- Leonardo Carofiglio, Giacomo Cherubini, Alessandro Gambini,
  *On Eswarathasan-Levine and Boyd's conjectures for harmonic numbers*,
  Bulletin of the Australian Mathematical Society 113 (2026), 15-25;
  published online 20 June 2025, DOI 10.1017/S0004972725100154,
  arXiv:2503.15714. Primary article:
  https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-eswarathasanlevine-and-boyds-conjectures-for-harmonic-numbers/AADD00C255BBC1535F9F6DD8FFD4893A
  Primary PDF:
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AADD00C255BBC1535F9F6DD8FFD4893A/S0004972725100154a.pdf/on_eswarathasanlevine_and_boyds_conjectures_for_harmonic_numbers.pdf
