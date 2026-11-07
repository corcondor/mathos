# Higher-precision p-adic restriction for all prime-power first indices

## Statement

Consider the original equation with \(\ell=1\):

\[
\binom{\binom ij}{k}=\binom{i^2}{j^2}+k^2.
\]

Write

\[
A=\binom ij,\quad X=\binom{i^2}{j^2},\quad
r=\min(k,A-k),\quad g=\gcd(i,j).
\]

The previously certified cases give j≥21 for any remaining solution.
The boundary reduction gives r≥j+2, and the established large-top
lemma gives r<2j whenever i≥2j. Both possible values k=r and k=A−r
are retained throughout.

**Theorem.** If i is a prime power, every remaining solution satisfies

\[
\boxed{i<2gj+4\sqrt{gj}\,j^2\le2j^2+4j^3.} \tag{1}
\]

In particular,

\[
\boxed{i=p^a,\ \ell=1\quad\Longrightarrow\quad i<4j^3+2j^2.}
\tag{2}
\]

If additionally p does not divide j, the proof also gives

\[
\boxed{i^2<(2j)^5.} \tag{3}
\]

These are uniform height bounds, not an absolute bound on j and not a
proof of global nonexistence.

## 1. The valuation-balanced case

If i<2j, all displayed height bounds are immediate. Assume i≥2j,
so j+2≤r<2j.

Write

\[
i=p^a,\qquad j=p^b u,\quad p\nmid u,\qquad
g=p^b,\quad c=a-b,\quad q=p^c=i/g.
\]

If r≥q, then i=gq≤gr<2gj, proving (1) in this case. Therefore
suppose r<q.

Section 4 of `v4_prime_power_reduction.md` proves, by exact valuation
comparison, that

\[
c=3d,\qquad r=p^d v,\quad p\nmid v.
\tag{4}
\]

Put z=p^d. Thus q=z³, i=gz³, r=zv, and d≥1.
Set

\[
s=\lfloor\log_p(r-1)\rfloor,\qquad
E=\min(2d,3d-s),\qquad Q=p^E.
\tag{5}
\]

Since r<p^(3d), we have s<3d and E≥1.

## 2. Keeping the normalized units to higher precision

All rational congruences below have denominators coprime to p after
the displayed powers of p are cancelled. They can equivalently be
read in the ring of rational numbers with p-coprime denominator.

The exact product formula is

\[
\frac A{p^{3d}}
=\frac{(-1)^{j-1}}u
  \prod_{h=1}^{j-1}\left(1-\frac{p^a}{h}\right).
\tag{6}
\]

Every h<j is also less than r. Hence v_p(h)≤s and
v_p(p^a/h)≥a−s≥3d−s≥E. Every factor in the product is therefore
1 modulo Q, giving

\[
U:=A/p^{3d}\equiv(-1)^{j-1}u^{-1}\pmod Q.
\tag{7}
\]

Similarly,

\[
\frac{\binom Ar}{p^{2d}}
=\frac{(-1)^{r-1}U}{v}
  \prod_{h=1}^{r-1}\left(1-\frac A h\right).
\tag{8}
\]

Here v_p(A/h)≥3d−s≥E. Combining (7)--(8),

\[
\frac{\binom Ar}{p^{2d}}
\equiv\frac{(-1)^{j+r}}{uv}\pmod Q.
\tag{9}
\]

The first right-side term has v_p(X)=6d, so X/p^(2d) vanishes
modulo Q, because E≤2d. If k=r, then k²/p^(2d)=v². If k=A−r,
then

\[
k^2/p^{2d}=(p^{2d}U-v)^2\equiv v^2\pmod Q.
\]

Consequently the original equation forces the higher-precision
unit condition

\[
\boxed{u v^3\equiv(-1)^{j+r}\pmod Q.} \tag{10}
\]

The modulus has a useful lower bound. Since p^s≤r−1<r=zv,

\[
p^{3d-s}>\frac{z^3}{r}=\frac{z^2}{v},
\qquad p^{2d}=z^2\ge\frac{z^2}{v}.
\]

Taking the minimum gives

\[
\boxed{Q\ge\frac{z^2}{v}=\frac qr.} \tag{11}
\]

## 3. The congruence gives a cubic height in j

We first exclude the exceptional unit value uv³=1. It would force
u=v=1, so j=p^b and r=p^d. Since j<r, their exponents satisfy d>b,
and therefore r≥pj≥2j. This contradicts r<2j.

Thus uv³≥2. A positive integer at least 2 that is congruent to either
1 or −1 modulo Q must satisfy

\[
Q\le uv^3+1=\frac{u r^3}{q}+1.
\tag{12}
\]

Combining (11) and (12), and multiplying by qr, yields

\[
\boxed{q^2\le u r^4+qr.} \tag{13}
\]

The positive root of T²−rT−ur⁴ is less than r+sqrt(u)r².
One can verify this without approximation: substitution of the
latter quantity gives sqrt(u)r³>0, while the quadratic is increasing
after its positive root. Hence

\[
q<r+\sqrt u\,r^2.
\]

Multiplying by g, using gu=j, and then r<2j,

\[
i<gr+\sqrt{gj}\,r^2
 <2gj+4\sqrt{gj}\,j^2
 \le2j^2+4j^3.
\]

This proves (1)--(2), including the previously separated cases.

## 4. A stronger degree bound when p does not divide j

Here g=1 and u=j. In the case i≥2j, we necessarily have r<q=i,
so the valuation-balanced analysis applies. Suppose z≥v⁵. Then
by (11),

\[
Q\ge z^2/v\ge zv^4.
\]

But j≤r−2=zv−2 implies

\[
jv^3+1\le zv^4-2v^3+1<zv^4.
\]

This contradicts (12). Thus z<v⁵, and

\[
i^2=z^6<z^5v^5=r^5<(2j)^5.
\]

For i<2j, (3) is immediate. This proves the coprime assertion.

## Verification status

The written argument was independently checked by a second AI agent.
The exact product congruence is also compared with direct integer
binomial coefficients by `v4_prime_power_verify.py` on its stated
finite ranges. Neither this note nor that Python check is asserted
to be a Lean formalization. The cubic-divisibility theorem used in
the companion reduction note has separately passed Lean kernel checking;
the exact formalized scope is recorded in `v4_formal/README.md`.
