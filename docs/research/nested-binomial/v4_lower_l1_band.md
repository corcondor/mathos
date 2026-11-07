# Complete exclusion of the L1 band 3j <= b <= 4j

## Statement

For the original equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

there is no solution in the previously classified lower-branch type L1
with

\[
\boxed{k=\ell+1=B=b,\quad \ell>j,\quad B\le A/2,
       \quad 3j\le b\le4j.}
\]

This is an exclusion of a parameter band with no initial upper bound on
any index. Its proof consists of a uniform height argument followed by
exact modular certificates for the finite set forced by that argument.

## 1. Deriving the finite region

The already proved results in `lower_branch_reduction.md` give

\[
b\ge22,\qquad i-j\ge4,\qquad
\frac{b^3}{4}<A=\binom ij<b^3
\]

under \(b\ge3j\). Since \(b\le4j\), one has \(j\ge6\), and

\[
\frac{j^4}{24}<\binom{j+4}{4}\le A<b^3\le64j^3.
\]

Consequently

\[
\boxed{6\le j\le1535.} \tag{1}
\]

There is also a small, uniform bound on the upper-minus-lower offset:

\[
\boxed{4\le i-j\le11.} \tag{2}
\]

To prove the upper bound, note that
\(\binom{18}{12}=18564>64\cdot6^3=13824\).
The quantity \(\binom{j+12}{12}/j^3\) strictly increases at every
integer \(j\ge6\), because the numerator of its successive ratio
minus 1, after clearing the positive denominator, is

\[
(j+13)j^3-(j+1)^4=9j^3-6j^2-4j-1>0.
\]

For an explicit positive-coefficient check, put \(u=j-6\ge0\); the
last polynomial becomes

\[
9u^3+156u^2+896u+1703>0.
\]

Thus \(i\ge j+12\) would imply
\(A\ge\binom{j+12}{12}>64j^3\ge b^3\), a contradiction.

The complete remaining set is therefore the integer triples satisfying

\[
6\le j\le1535,\quad j+4\le i\le j+11,\quad
\max(22,3j)\le b\le4j,\quad b^3<4\binom ij<4b^3.
\tag{3}
\]

The last condition means exactly \(b^3/4<A<b^3\).
This list has **542,642 triples**, distributed among **1,475 pairs**
\((j,i)\). The number is a result of exact enumeration of (3), not a
chosen search cutoff.

## 2. Certificate rule

For every triple in (3), the certificate supplies a prime \(p\) such
that

\[
\binom{\binom ij}{b}
\not\equiv
\binom{i^2}{j^2}+\binom{b^2}{2b-1}\pmod p.
\tag{4}
\]

Each inequality (4) excludes that triple. Binomial residues are computed
with Lucas's theorem, so their large integer values do not need to be
materialized. The generator uses factorial tables and modular inverses
for the base-p digits. The independent verifier instead uses exact
`math.comb` on every pair of digits.

The generator enumerates \((j,i)\) first and derives the allowed
\(b\)-interval from exact integer cube roots. The verifier enumerates
\(b\) first, derives its complete \(j\)-interval, and then uses the
proved offset bound (2) to find every allowed \(i\). It requires the
two complete candidate sets to coincide without missing or duplicate
entries. Every supplied modulus is checked to be prime, and every
congruence contradiction is recomputed.

No unexcluded candidate is silently treated as impossible.

## 3. Reproduction and status

```bash
python3 v4_lower_l1_band.py generate
python3 v4_lower_l1_band.py verify
```

The script imports the exact Lucas routines from
`v4_lower_l1_single_top.py`; both files must be in the same directory.
The certificate and verifier report are
`v4_lower_l1_band_certificates.json` and
`v4_lower_l1_band_verification.json`.

The executed independent verifier reported **542,642 excluded triples,
zero unresolved triples**, and a largest obstruction prime of **73**.
The certificate SHA256 is
`b82380617732a85c4f92bddaff67ba9c6c1690f02f2e04da49dd3c3586b8dd03`.

The proof uses ordinary written mathematics plus exact integer
certificate verification. It is not claimed to have been formalized
in Lean. The conclusion excludes the specified entire band; it does
not settle the remaining L1 regions \(b<3j\) and \(b>4j\), nor the
other branches of the original equation.
