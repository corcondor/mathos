# Complete exclusion when the first index minus two is a prime power

## Theorem and proof structure

For the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

the entire family

\[
\boxed{\ell=1,\qquad j=i-3,\qquad
i=P^a+2,\quad P\text{ prime},\quad a\ge1}
\tag{1}
\]

has no solution. Both outer branches are included.

The proof combines the v7 exact valuation classification with the
full v6 common divisor. Their interaction produces a positive integer
quotient in a short, fixed interval. The logarithmic gap then gives
an absolute height bound. A unit congruence also bounds the prime base.
The resulting finite remainder consists of 2,903 explicit integers,
each certified to lie strictly between two consecutive cubes.

The bound defining this finite remainder is proved below. No interval
of possible values of \(r\) is enumerated, and no assumption about the
distribution of Wieferich primes is used. This theorem does not settle
all composite values of \(i-2\), every offset, or the original equation.

## 1. Established inputs and the remaining cases

Write

\[
z=P^a,\quad n=z+2=i,\quad A=\binom n3,\quad
r=\min(k,A-k),\quad d=v_P(r).
\]

The following inputs were proved in the earlier notes:

\[
3n<r<10n/3, \tag{2}
\]

\[
Q:=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3,
\tag{3}
\]

and, when \(n\ge1024\),

\[
r<3n+\frac{3n}{4\log n}. \tag{4}
\]

These are respectively in `v5_offset_three_structure.md`,
`v6_common_divisor.md`, and `v6_offset_composite.md`.
The v7 shifted-power classification gives the following complete
list of necessary cases after its explicit small-index exclusions:

| Prime base | Necessary exponent and valuation |
|---|---|
| \(P\ge7\) | \(a=3d\), \(d\ge1\) |
| \(P=2\) | \(a=3h\), \(d=h+1\), \(h\ge5\) |
| \(P=5\) | \(a=3d-1\), \(a\ge8\) |

The case \(P=3\) is completely excluded by the companion
`v8_shifted_base_three.md`. In that case the exact valuation is
\(d=(a-1)/2\), and (3) bounds the exponent by 9; the single
remaining value \(3^9+2=5\cdot31\cdot127\) is squarefree and
contradicts (2). Its small-exponent coverage is recorded there.

For the three rows of the table, define

\[
K=P^{3d-a}=
\begin{cases}
1,&P\ge7,\\
8,&P=2,\\
5,&P=5.
\end{cases} \tag{5}
\]

In every remaining case, \(z>320\): the minimum powers in the
three rows are \(7^3\), \(2^{15}\), and \(5^8\).

## 2. A common divisor becomes an integer quotient

Put

\[
Q'=\frac{n(n-1)}6.
\]

This is an integer in all three rows. Since \(P\ne3\), the
integer \(z=P^a\) is nonzero modulo 3, so \(n\) is 0 or 1
modulo 3. Hence 3 divides \(n(n-1)\), and 2 always does.

For odd \(P\ne3\), the index \(n\) is odd. If \(n\) is 0
modulo 3, the two gcds in (3) are 3 and 2. If it is 1 modulo 3,
they are 1 and 6. Thus \(Q=Q'\), and \(P\nmid Q'\), because
\(n\equiv2\) and \(n-1\equiv1\pmod P\).

For \(P=2\), the index \(n=2^a+2\) has exactly one factor
of 2. The product of the two gcds in (3) is 3, so \(Q=2Q'\)
and \(Q'\) is odd. Therefore, in every case,

\[
\boxed{Q'\mid r^3,\qquad\gcd(Q',P)=1.} \tag{6}
\]

Write \(r=P^dv\). Cancelling the prime power from (6) gives
\(Q'\mid v^3\). We obtain a positive integer

\[
\boxed{t=\frac{v^3}{Q'}\in\mathbb Z_{>0},\qquad
6v^3=t(P^a+2)(P^a+1).} \tag{7}
\]

This quotient is the key additional information. Its integrality
will interact with the upper gap, not merely its magnitude.

## 3. A fixed, short list of possible quotients

Since \(P^{3d}=Kz\), equation (7) gives

\[
t=\frac{6r^3}{Kz n(n-1)}. \tag{8}
\]

The elementary ratio

\[
E(z):=\frac{n^2}{z(n-1)}
=\frac{(z+2)^2}{z(z+1)}
=1+\frac{3z+4}{z(z+1)}
\]

satisfies

\[
1<E(z)<1+\frac4z<\frac{81}{80}, \tag{9}
\]

because \(z>320\). Apply the two bounds in (2) to (8). They give

\[
\frac{162}{K}<t<\frac{2000}{9K}E(z)<\frac{225}{K}.
\]

Since \(t\) is an integer, its complete possible ranges are

| Base | \(K\) | Possible integers \(t\) |
|---|---:|---|
| \(P\ge7\) | 1 | \(163,164,\ldots,224\) |
| \(P=2\) | 8 | \(21,22,\ldots,28\) |
| \(P=5\) | 5 | \(33,34,\ldots,44\) |

## 4. An absolute height bound from the logarithmic gap

Suppose, for a contradiction, that \(\log n\ge128\). In
particular \(n\ge1024\), so (4) gives

\[
r<3n\left(1+\frac1{4\log n}\right)
\le3n\frac{513}{512}.
\]

Also \(e>2\), so \(z=n-2>2^{128}-2>2^{20}\). Hence (9)
gives \(E(z)<1+2^{-18}\), and (8) yields

\[
t<\frac{162}{K}\left(\frac{513}{512}\right)^3
\left(1+2^{-18}\right)<\frac{163}{K}. \tag{10}
\]

The last strict inequality is the exact rational calculation

\[
162\left(\frac{513}{512}\right)^3(1+2^{-18})
=\frac{2866676543645265}{17592186044416}<163;
\]

after clearing denominators its positive margin is
\(849781594543\). But, for each \(K\in\{1,5,8\}\), the
open interval

\[
\left(\frac{162}{K},\frac{163}{K}\right)
\]

contains no integer. This contradicts the lower bound for \(t\).
We have therefore proved

\[
\boxed{n<e^{128}<2^{192}.} \tag{11}
\]

The second bound uses only \(e<11/4\) and
\((11/4)^2=121/16<8\). For a short proof of the first numerical
bound, the factorial series gives
\(e<65/24+1/100<11/4\), bounding the tail from \(1/5!\)
by a geometric series with ratio \(1/6\). Thus
\(e^{128}=(e^2)^{64}<8^{64}=2^{192}\).

This is a uniform height bound for every prime base in the table.
It is not a chosen computational stopping point.

## 5. Bounding the prime base when P is at least seven

The v7 normalized-unit argument proves, for \(P\ge7\),

\[
(9v)^3\equiv\pm120\pmod P. \tag{12}
\]

On the other hand, reducing (7) modulo \(P\) gives
\(6v^3\equiv2t\pmod P\), or \(3v^3\equiv t\pmod P\).
Combining this with (12) yields

\[
243t\equiv\pm120\pmod P,
\qquad
\boxed{P\mid81t-40\quad\text{or}\quad P\mid81t+40.}
\tag{13}
\]

The integers on the right are positive, because \(t\ge163\).
The upper bound \(t\le224\) therefore implies

\[
\boxed{P\le81\cdot224+40=18184.} \tag{14}
\]

More precisely, only the prime factors at least seven of the 124
explicit integers \(81t\pm40\), for \(163\le t\le224\),
can occur. Keeping the association between \(P\) and \(t\)
gives 204 prime-quotient pairs, with 119 distinct prime bases.
The largest candidate prime is 17293. These counts are checked
independently by the two domain-construction methods below.

## 6. The complete finite remainder and its cube certificates

Equation (7) requires

\[
\boxed{V(P,a,t):=\frac{t(P^a+2)(P^a+1)}6=v^3.} \tag{15}
\]

All factors and divisions in (15) are exact integers. The finite
domain is now determined entirely by proved necessary conditions:

1. For \(P\ge7\), use (13), \(163\le t\le224\), and
   positive exponents \(a\equiv0\pmod3\) satisfying
   \(P^a+2<2^{192}\).
2. For \(P=2\), use \(a=15,18,\ldots,189\) and
   \(21\le t\le28\).
3. For \(P=5\), use \(a=8,11,\ldots,80\) and
   \(33\le t\le44\). The endpoint is verified by
   \(5^{80}+2<2^{192}\le5^{83}+2\).

The certificate contains the following counts:

| Bases | Prime-exponent pairs | Quotient tests |
|---|---:|---:|
| \(P\ge7\) | 840 | 2131 |
| \(P=2\) | 59 | 472 |
| \(P=5\) | 25 | 300 |
| Total | 924 | 2903 |

For **every** one of these 2903 triples, the file
`v8_shifted_prime_power_completion_certificates.json` supplies a
nonnegative integer \(m\) with

\[
\boxed{m^3<V(P,a,t)<(m+1)^3.} \tag{16}
\]

Thus none of the required values is a cube. Equations (15) and
(16) contradict one another, completing the proof for every
\(P\ne3\). The companion proof for \(P=3\) completes (1).

The certificate does not require a numerical approximation to a
cube root. Each row is verified by two integer cube evaluations
and comparisons after forming the exact value in (15).

### Independent completeness and verification checks

The standard-library Python checker follows two separate methods:

- The generator factors each \(81t\pm40\) by trial division and
  constructs the domain from those factors. It computes each integer
  \(m\) by binary integer cube-root search.
- The verifier independently sieves **all** primes through 18184,
  tests (13), and reconstructs the exponents and quotient ranges.
  It checks that the certificate contains exactly this set of triples,
  with neither missing cases nor duplicate rows. It then checks
  (16) directly, without using a cube-root algorithm.

The exact rational constants in the proof and the endpoints of the
small-base exponent ranges are checked as well. No probabilistic
primality tests, floating-point bounds, or enumeration of an interval
of \(r\) is used.

To reproduce the certificate and verification report, run

    python v8_shifted_prime_power_completion_checks.py

The report is
`v8_shifted_prime_power_completion_verification.json`.
All 2903 strict neighboring-cube certificates and both independently
constructed domains pass.

## 7. Consequences and formalization scope

Any remaining offset-three solution with \(\ell=1\) must have
at least two distinct prime factors in \(i-2\), since every
prime-power value of \(i-2\) has now been excluded.

Combining with `v7_offset_cofactor_three.md` also excludes
\(i=3P^a+2\) for every prime \(P\): that note covers
\(P\ne3\), and the companion base-three theorem covers \(P=3\).

The previous plus-Wieferich necessary conditions for the shifted
powers of 2, 3 and 5 are now superseded by complete exclusions of
those families. Nothing about the global existence or nonexistence
of further Wieferich primes is inferred.

The composite-family reviewer independently checked the quotient,
height and prime-base reductions and independently reproduced the
complete finite calculation on 2026-11-05. The reviewer obtained the
same 204 prime-quotient pairs, 119 prime bases, and 2131+472+300
noncube values, and reported PASS.

Root's independent full mathematical audit also passed on 2026-11-05,
covering the cancellation from the common divisor, both outer branches,
the three values of \(K\), both finite bounds, the normalized-unit
congruence, and the complete domain of triples \((P,a,t)\). The peer
reviewer then audited both finalized v8 notes in full, confirmed the
displayed rational constants and counts, and reported PASS again.

The written analytic and valuation reductions are not asserted here
to be fully formalized in Lean. Any separate formal verification of
the finite arithmetic certificate must state its own scope and does
not, by itself, formalize those preceding reductions.
