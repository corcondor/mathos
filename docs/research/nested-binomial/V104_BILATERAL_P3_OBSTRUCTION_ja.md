# v104 — 2-sided p³ obstruction: finitely many prime factors, not a brute-force bound

**2026-11-12**. This is a rigorous *written mathematical proof* and a reproducible exact-integer certificate for the fixed branch
\[
j=1,\qquad k=p\ge5\ \text{prime},\qquad \ell=p-1.
\]
The original squared-index nested-binomial equation is then
\[
\boxed{\binom{i}{p}=i^2+R_p,\quad R_p=\binom{p^2}{2p-1}.}\tag{104.1}
\]
We combine v100's real-root crossing, v101's \(i<p^3\), and v102's mod-\(p^2\) harmonic recovery. We do **not** claim the unrestricted four-variable equation is solved.

## 1. Universal third p-adic digit (all primes p≥5)

Write \(i=pq+r\), \(0\le r<p\), and
\[
H_r=\sum_{j=1}^r\frac1j,\qquad J_r=\sum_{j=1}^r\frac1{j^2}.
\]
Denominators are units modulo \(p\). Wolstenholme's congruence
\(H_{p-1}\equiv0\pmod{p^2}\) and \(J_{p-1}\equiv0\pmod p\) imply
\[
\binom{pq}{p}\equiv q\pmod{p^3}.
\]
For \(q\ge1\), use the exact quotient
\[
\frac{\binom{pq+r}{p}}{\binom{pq}p}
=\prod_{j=1}^r\frac{pq+j}{p(q-1)+j}
=\prod_{j=1}^r\left(1+\frac p{p(q-1)+j}\right).
\]
Expanding the product in \(\mathbb Z_{(p)}\) to order \(p^2\) yields
\[
\boxed{\binom{pq+r}{p}\equiv
q\Bigl[1+pH_r+\frac{p^2}{2}
(H_r^2-(2q-1)J_r)\Bigr]\pmod{p^3}.}\tag{104.2}
\]
The case \(q=0\) is immediate. Independently,
\[
(2p-1)R_p=p^2\binom{p^2-1}{2p-2},\qquad
\binom{p^2-1}{2p-2}\equiv1\pmod p
\]
by Lucas, so
\[
\boxed{R_p\equiv-p^2\pmod{p^3}.}\tag{104.3}
\]

The mod-\(p^2\) condition for (104.1) is precisely v102's
\[
\boxed{q\equiv r^2[1+p(2r-H_r)]\pmod{p^2}.}\tag{104.4}
\]
By v101's \(i<p^3\), \(0\le q<p^2\); thus q is **the unique canonical representative** of this residue class.

## 2. The LOW edge: an effective universal bound on p in terms of r

Take fixed \(r\ge1\), \(r<p\). Put
\[
a=r^2,\quad H=H_r,\quad J=J_r,\quad L=\operatorname{lcm}(1,\ldots,r),
\]
\[
B=a(2r-H)=U/V>0,\qquad \gcd(U,V)=1,\quad V\mid L,
\]
\[
\boxed{M_r=
1-a^2-a(2r-H)^2+\frac a2[H^2-(2a-1)J].}\tag{104.5}
\]
For every prime \(p>\max(U,a)\), the exact unique integer \(q\in[0,p^2)\) from (104.4) has the rational representation
\[
\boxed{q=a+pB+\frac tV p^2,\qquad
0\le t<V,\quad U+tp\equiv0\pmod V.}\tag{104.6}
\]
This is equality of *rational expressions* for the integer q, not an approximation. Substituting into (104.2) and subtracting \(i^2+R_p\) gives the exact necessary condition
\[
\frac{\binom{i}{p}-i^2-R_p}{p^2}
\equiv M_r+\frac tV\pmod p.
\]
Thus an exact solution requires
\[
\boxed{p\mid N_r(t):=2L^2\left(M_r+\frac tV\right)\in\mathbb Z.}\tag{104.7}
\]
Each \(N_r(t)\) is **nonzero**. For \(r\ge2\), \(H\le r\), \(0<J<2\) imply
\[
1-\frac32r^4\ge M_r>-7r^4,
\]
so \(M_r<-1\), \(0\le t/V<1\), and
\[
0<|N_r(t)|<14r^4L^2.
\]
At r=1, \(M_1=-1\) and \(N_1(0)=-2\). Since \(U\le2r^3L\), the previously omitted \(p\le\max(U,a)\) are also strictly bounded by the same expression. Therefore every putative solution with \(r\ge2\) satisfies the **effective, all-prime theorem**
\[
\boxed{p<14r^4\operatorname{lcm}(1,\ldots,r)^2.}\tag{104.8}
\]
At r=1 the congruence already gives a contradiction for every p≥5.

## 3. The HIGH edge: a different but equally explicit bound

Let \(s=p-r\ge1\); thus \(r=p-s\). Set
\[
a=s^2,\qquad H=H_{s-1},\qquad J=J_{s-1},
\quad L=\operatorname{lcm}(1,\ldots,s-1)
\]
with \(L=1\) at \(s=1\). Wolstenholme implies
\[
H_{p-s}\equiv H+pJ\pmod{p^2},\qquad
J_{p-s}\equiv-J\pmod p.
\]
Define
\[
B=-aH-2s(a+1)=U/V<0,\quad V\mid L,
\]
\[
\boxed{M_s^-=B(H+2s)+
\frac a2[H^2+(2a+1)J]-(a+1)^2+1.}\tag{104.9}
\]
For \(p>\max(|U|,a)\), the unique \(q\in[0,p^2)\) from (104.4) equals
\[
\boxed{q=a+pB+\frac tV p^2,\quad
1\le t\le V,\quad U+tp\equiv0\pmod V.}\tag{104.10}
\]
Using the full \(p^3\) expansion (104.2), one obtains
\[
\frac{\binom{i}p-i^2-R_p}{p^2}\equiv M_s^-+\frac tV\pmod p.
\]
Thus an exact solution requires
\[
\boxed{p\mid N_s^-(t)=2L^2\left(M_s^-+\frac tV\right)\in\mathbb Z.}\tag{104.11}
\]
Because \(H<s\), \(J<2\),
\[
-18s^4\le M_s^-<-\frac52s^4-5s^2<-1.
\]
Hence all \(N_s^-(t)\ne0\), \(|N_s^-(t)|<40s^4L^2\), and the omitted small \(p\le|U|\) also satisfy this upper bound. Consequently
\[
\boxed{p<40s^4\operatorname{lcm}(1,\ldots,s-1)^2.}\tag{104.12}
\]

Combining both sides with \(m=\min(r,p-r)\ge1\),
\[
\boxed{p<40m^4\operatorname{lcm}(1,\ldots,m)^2.}\tag{104.13}
\]
This is an **effective all-prime p-adic bound** requiring neither irrationality exponent \(\mu(e)\), PNT nor analytic root asymptotics. The classical elementary lcm bound \(L_m\le4^m\) already yields a logarithmic exclusion band \(m\gg\log p\). Using PNT \(L_m=e^{(1+o(1))m}\) recovers \(m\ge(\frac12-o(1))\log p\), but the prime cutoff (104.13) is entirely elementary.

## 4. Two universal REAL inequalities for the finitely many exceptional primes

The symbolic \(p^3\) conditions make each fixed distance a **finite and provably exhaustive list of primes**. Those remaining primes are settled using mod \(p^4/p^5\), plus two archimedean inequalities avoiding prohibitively large binomial coefficients.

**Lower real barrier.** For all primes \(p\ge1000\) and \(i\le3p^3/5\),
\[
\boxed{\binom{i}p<R_p.}\tag{104.14}
\]
To prove, put \(D=p^2-2p+2\), \(\lambda=D/p^2\). Using \(i\ge p\) (otherwise the LHS vanishes) and product bounds,
\[
\frac{R_p}{\binom{i}p}\ge
\frac{D^{2p-1}p!}{(2p-1)!\,i^p}
=\left(\frac Di\right)^p
\frac{D^{p-1}}{\prod_{j=p+1}^{2p-1}j}.
\]
AM–GM bounds the denominator product by \((3p/2)^{p-1}\). Since \(i\le3p^3/5\), \(\lambda\ge499/500\),
\[
\frac{R_p}{\binom{i}p}\ge
\frac{3}{2\lambda p}\left(\frac{10\lambda^2}{9}\right)^p
>\frac3{2p}\left(\frac{11}{10}\right)^p>1.
\]
The last inequality holds for all \(p\ge1000\), since \((11/10)^{1000}>1000\) by the first three binomial terms, and \((11/10)^p/p\) thereafter increases.

**Upper real barrier.** For all odd primes \(p\ge64\) and \(3p^3/4\le i<p^3\),
\[
\boxed{\binom{i}p>2R_p>R_p+i^2.}\tag{104.15}
\]
Indeed
\[
\frac{\binom ip}{R_p}\ge
\left(\frac{i-p+1}{p^3}\right)^p
\prod_{j=p+1}^{2p-1}\frac jp
>\left(\frac{37}{50}\right)^p2^{(p-1)/2}>2.
\]
Pair factors \(j\) and \(3p-j\) to bound the product \(>2^{(p-1)/2}\), and use Bernoulli on
\(\frac{37}{50}(1+238/2500)^{(p-1)/2}>2\).
Finally \(R_p\ge\binom{p^2}{p}\ge p^p>p^6>i^2\).

Thus **no original solution** can have \(i/p^3\le3/5\) at \(p\ge1000\), or \(i/p^3\ge3/4\) at \(p\ge64\).

## 5. Full exact finite-factor certificate, NOT an arbitrary prime scan

The verifier [v104_bilateral_p3_certificate.py](v104_bilateral_p3_certificate.py) does NOT pick an experimental upper bound on p. For each distance \(d\), it constructs the *finitely many integers* \(N_d(t)\) from (104.7)/(104.11), factors every one of them completely by exact integer division, and checks all small primes at or below the **proved** bound \(\max(|U|,d^2)\). Each surviving p³-compatible exception has the unique i from the already proved mod-\(p^2\) formula. The only remaining steps are exact modular binomial certificates mod \(p^4\), rarely mod \(p^5\), or the two universal inequalities (104.14)–(104.15). In particular huge exceptional prime p=43,933,129 at r=7 is excluded by \(2i<p^3\) and (104.14) (indeed already the weaker p≥64, i<p³/2 lemma); no enormous binomial expansion.

For \(1\le d\le10\) the p³-compatible prime exceptions are:

| distance | low edge r=d | high edge r=p−d |
|---:|---|---|
| 1 | none | 5 |
| 2 | 5, 53 | 11, 41 |
| 3 | 7, 433 | 5, 2131 |
| 4 | 5, 2039 | 7, 11, 29, 2749 |
| 5 | 29, 137, 241, 423847 | 23 |
| 6 | 59 | 29 |
| 7 | 11, 1279, 43933129 | 139 |
| 8 | 127, 229 | 12037 |
| 9 | 11, 31, 31466713, 2737611311 | none |
| 10 | 231799, 10947653, 1718780009 | 101, 113, 1139321, 1377499 |

All **40** instances are discharged by the exact modular/real certificates. For the sole example (p,r)=(31,9), p⁴ vanishes but
\[
\frac{\binom ip-i^2-R_p}{p^4}\equiv19\pmod{31},
\]
so mod \(p^5\) gives the contradiction. In all other modular cases p⁴ already suffices. No large prime not in this table can survive, by (104.7)/(104.11) and complete factorization of the finite N list.

**New completed infinite-family theorem:**
\[
\boxed{\forall p\ge5\ {\rm prime},\
\forall i\ge p,\quad
1\le \min(i\bmod p,p-(i\bmod p))\le10
\Longrightarrow
\binom ip\ne i^2+\binom{p^2}{2p-1}.}\tag{104.16}
\]
Combined with v101's \(p\mid i\) exclusion and v100's small k=2,3, it rules out all residue classes when p≤19 and the 20 edge classes for any arbitrarily large p.

**Strict scope and research implication:** This is *not* an unrestricted solution for k=p; middle classes 11≤r≤p−11 are still possible in principle for p≥23. Even less does it solve the original four-variable equation. The genuinely new gain over v102 is a completely **elementary effective** p-in-terms-of-residue bound plus systematic finite-factor elimination, not merely an asymptotic irrationality-measure estimate. The continuous real-root curve becomes useful only for a small number of factored exceptional primes.

### Verification status

The source implements exact integer finite-factor certificates and modular binomial arithmetic, with no unbounded i enumeration. The analytical inequalities and p³ expansion above are written proofs, not Lean-kernel proofs. Any CI PASS must be checked in the Actions log; no claim of full Lean final goals.
