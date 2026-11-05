# L1: only offset four in the strip 5j/2 <= b <= 4j

## Scope and completed conclusion

Retain the original equation and the lower-branch type L1:

\[
k=B=\ell+1=b,\quad \ell>j,\quad
A=\binom ij,\quad X=\binom{i^2}{j^2},\quad
Y_b=\binom{b^2}{2b-1},\quad L=\binom Ab.
\]

The previous reductions give b>=22, i-j>=4, A>b³/4, and
\(X<16A^{2j}\). The quotient L/(X+Y_b) strictly increases in i
when b>=2j. The new `v5_l1_expanded_band.md` completely excludes
\(8j/3\le b\le4j\).

This note shows that in the remaining adjoining strip
\(5j/2\le b<8j/3\), every solution must have i-j=4.
The analytic reduction is below; its exact finite completion is
recorded at the end.

Consequently the combined statement is

\[
\boxed{\text{L1},\quad 5j/2\le b\le4j
\quad\Longrightarrow\quad
i=j+4,\quad 5j/2\le b<8j/3.}
\tag{1}
\]

## 1. Fifth-degree height and a finite offset range

Since b>=5j/2, we have b-2j>=b/5. The same product argument as in
Section 1 of `v5_l1_expanded_band.md` proves

\[
\boxed{A<b^5.} \tag{2}
\]

In detail, if A>=b⁵, then L>A^b/(2b!), so
X/L<32b!/b^b<=1/64. Also A>=b³ gives Y_b/L<1/(b-1)<=1/21.
Their sum cannot equal L.

For b<8j/3<3j and b>=22, it is safe to use j>=8. If i-j>=24,
then A>=C(j+24,24). At j=8,

\[
\binom{32}{24}=10518300>7962624=243\cdot8^5.
\]

The quotient C(j+24,24)/j⁵ increases for all integer j>=8, since
the numerator of its successive ratio minus one is

\[
(j+25)j^5-(j+1)^6
=19j^5-15j^4-20j^3-15j^2-6j-1>0.
\]

The negative terms total less than 3j⁵ for j>=8.
Thus i-j>=24 would imply A>243j⁵>=b⁵, contrary to (2).
For the cases being excluded, therefore,

\[
\boxed{5\le i-j\le23.} \tag{3}
\]

## 2. Analytic exclusion of all offsets at least five for j>=1024

Fix j>=1024 and 5j/2<=b<=3j. Let

\[
i_0=j+5,\quad A_0=\binom{j+5}{5},\quad
N=(j+5)^2,\quad q=10j+25,\quad X_0=\binom Nq,
\quad a=5j/2,\quad s=\lceil a\rceil.
\]

We compare the equation at i=i_0. Monotonicity in i will then
exclude every i>=j+5.

As before, A_0>j⁵/120, s<=3j, and the numerator correction in
\(\binom{A_0}{s}\) is larger than 1/2. The elementary bound
s!<=e s(s/e)^s and monotonicity of x log(eA_0/x) give

\[
\binom{A_0}{s}
>\frac1{18j}\left(\frac{ej^4}{300}\right)^{5j/2}.
\tag{4}
\]

For X_0,

\[
\frac Nq
=\frac j{10}\frac{(1+5/j)^2}{1+5/(2j)}
<\frac j{10}e^{10/j}.
\]

Since q=10j+25, j>=1024, and e<10,

\[
X_0\le\left(\frac{eN}{q}\right)^q
<e^{101}j^{25}\left(\frac{ej}{10}\right)^{10j}.
\tag{5}
\]

Combining (4)--(5) yields

\[
\frac{\binom{A_0}{b}}{X_0}
>\frac{K^j}{18e^{101}j^{26}},
\qquad
K=\frac{10^5}{3^{5/2}e^{15/2}}.
\tag{6}
\]

We have log K>3/4>1/2, using only the exact elementary bounds
log10>9/4 and log3<6/5:

\[
\log K=5\log10-\frac52\log3-\frac{15}{2}
>\frac{45}{4}-3-\frac{15}{2}=\frac34.
\]

For completeness, e<11/4 and (11/4)^9<10⁴ prove log10>9/4.
The first inequality follows by summing through 1/4! and bounding
the remaining exponential series by 1/100. The second is the integer
comparison 11⁹<10⁴·4⁹. Also e>8/3 and 8⁶>3¹¹ imply log3<6/5.

The function j/2-26 logj increases for j>=1024. At the starting point,
log1024<7 and log36<4 give

\[
\frac{1024}{2}-101-26\log1024-\log36
>512-101-182-4=225>0.
\]

Thus (6) implies \(\binom{A_0}{b}>2X_0\).

Meanwhile A_0>j⁵/120>27j³>=b³ in this range. The b-only product
comparison gives Y_b/C(A_0,b)<1/(b-1)<=1/21.
The two right-side terms therefore total less than the left side at
i=j+5. Since the ratio L/(X+Y_b) strictly increases thereafter,
all i>=j+5 are excluded.

Hence in the strip 5j/2<=b<8j/3, a solution with i-j>=5 must satisfy

\[
\boxed{j\le1023.} \tag{7}
\]

## 3. Exact finite remainder

Equations (2), (3), (7), and the earlier lower height give the complete
remaining list

\[
8\le j\le1023,\quad j+5\le i\le j+23,
\]

\[
\max(22,\lceil5j/2\rceil)\le b<8j/3,
\qquad b^3<4\binom ij,\qquad \binom ij<b^5.
\tag{8}
\]

`v5_l1_offset_four.py` generates witnesses for exactly this set and
verifies them independently. The generator lists j and the offset
first, deriving b endpoints from integer roots. The verifier lists b
first, uses the integer equivalent 3b<8j and 5j<=2b to reconstruct
the j interval, and tests the original strict height inequalities.
Lucas calculations use separate factorial-table and direct-binomial
implementations. No floating point is used.

## Exact verification result

The complete set (8) contains **224,160** candidates. Every candidate
has a nonzero residue witness modulo a prime at most **71**. There
are no unresolved candidates and no valuation fallback certificates.
The independent verifier passed on all 224,160 candidates; its result
is recorded in `v5_l1_offset_four_verification.json`.

The certificate file SHA-256 is

`cb17bd9580f87aa017150fb33a3694b47d6f6f63a652a6a2e0373420686c98a4`.

Reproduce the generation and the independent verification with

```bash
python3 v5_l1_offset_four.py generate
python3 v5_l1_offset_four.py verify
```

Neither this proof nor its finite verification is claimed to be a
Lean formalization. The remaining offset-four, two-variable equation
is not asserted to have no solutions.
