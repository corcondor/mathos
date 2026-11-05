# Expanding the completely excluded L1 band to 8j/3 <= b <= 4j

## Setting

The original squared-index equation is retained:

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns the lower-branch type L1, for which the earlier
classification proves

\[
k=B=\ell+1=b,\qquad \ell>j,\qquad b\le A/2,
\quad A=\binom ij,\quad X=\binom{i^2}{j^2},
\quad Y_b=\binom{b^2}{2b-1}.
\]

Earlier reductions give

\[
b\ge22,\qquad i-j\ge4,\qquad A>b^3/4,
\qquad X<16A^{2j}.
\]

They also prove that the ratio
\(\binom{A}{b}/(X+Y_b)\) is strictly increasing as a function
of the real upper index i on the valid interval whenever \(b\ge2j\).
These results are in `lower_branch_reduction.md` and
`sharp_q_bounds.md`. The band \(3j\le b\le4j\) was completely
excluded in `v4_lower_l1_band.md`.

**Completed theorem.** There is no L1 solution with

\[
\boxed{8j/3\le b\le4j.}
\]

The new analytic work below reduces the adjoining band
\(8j/3\le b\le3j\) to a fixed, explicitly bounded finite set.
All 355,759 candidates in that set have exact modular contradictions,
and the independent verifier has passed. Combining this with the
previous complete \(3j\le b\le4j\) exclusion proves the theorem.

## 1. A fourth-degree height bound

If \(b\ge8j/3\), then

\[
\boxed{A<b^4.} \tag{1}
\]

Suppose otherwise. Let \(L=\binom Ab\). Since \(A\ge b^4\),
the product inequality gives

\[
L>\frac{A^b}{2b!}.
\]

The inequality \(b-2j\ge b/4\) therefore implies

\[
\frac XL<\frac{32b!}{A^{b-2j}}
\le\frac{32b!}{b^b}
\le32\,2^{-\lfloor b/2\rfloor}\le\frac1{64}.
\]

The already proved direct comparison
\(\binom{b^3}{b}/Y_b>b-1\) does not require \(b\ge3j\);
its proof involves only b. As \(A\ge b^4\ge b^3\), it gives
\(Y_b/L<1/(b-1)\le1/21\). Thus \(X+Y_b<L\), a contradiction.
This proves (1).

More generally, the same proof gives \(A<b^s\) whenever
\(s\ge3\) and \(b-2j\ge b/s\); only s=4 is needed here.

## 2. A uniform offset bound in the new band

Assume \(8j/3\le b\le3j\). Then \(b\ge22\) implies
\(j\ge8\), and (1) gives \(A<81j^4\).

At j=8,

\[
\binom{23}{15}=490314>331776=81\cdot8^4.
\]

Also \(\binom{j+15}{15}/j^4\) strictly increases for integers
j>=8. Indeed the numerator of its successive ratio minus one is

\[
(j+16)j^4-(j+1)^5
=11j^4-10j^3-10j^2-5j-1>0.
\]

For j>=8 the sum of the four negative terms is less than
\(2j^4\), which explicitly verifies the last sign.

Consequently \(i-j\ge15\) would force
\(A\ge\binom{j+15}{15}>81j^4\ge b^4\), a contradiction.
Together with the earlier offset lower bound,

\[
\boxed{4\le i-j\le14.} \tag{2}
\]

## 3. Analytic exclusion of every j>=1024

Fix j>=1024 and \(8j/3\le b\le3j\), and put

\[
i_0=j+4,\quad A_0=\binom{j+4}{4},\quad
N=(j+4)^2,\quad q=8j+16,\quad
X_0=\binom Nq,
\]

\[
a=8j/3,\qquad s=\lceil a\rceil.
\]

We will show that \(\binom{A_0}{b}>X_0+Y_b\). The monotonicity
in i recalled above then excludes all \(i\ge j+4\).

### 3.1 Comparing with X

We have \(A_0>j^4/24\), \(s\le3j\), and
\(s(s-1)/(2A_0)<108/j^2<1/2\). Thus

\[
\binom{A_0}{s}>\frac{A_0^s}{2s!}.
\]

The elementary integral estimate for the logarithm of a factorial gives

\[
\log(s!)\le\int_1^s\log x\,dx+\log s
=s\log s-s+1+\log s,
\]

so \(s!\le e s(s/e)^s\). Since
\(x\log(eA_0/x)\) increases for \(0<x<A_0\), and a<=s,

\[
\binom{A_0}{s}
>\frac1{2es}\left(\frac{eA_0}{s}\right)^s
>\frac1{18j}\left(\frac{e j^3}{64}\right)^{8j/3}. \tag{3}
\]

Here we used e<3 and s<=3j. For X, the elementary factorial
lower bound \(q!\ge(q/e)^q\) gives

\[
X_0\le\left(\frac{eN}{q}\right)^q.
\]

Moreover,

\[
\frac Nq
=\frac j8\frac{(1+4/j)^2}{1+2/j}
<\frac j8 e^{8/j}.
\]

Because j>=1024>128 and e<8, this implies

\[
X_0
<\left(\frac{ej}{8}\right)^{8j+16}e^{64+128/j}
<e^{65}j^{16}\left(\frac{ej}{8}\right)^{8j}. \tag{4}
\]

Combining (3)--(4), and using monotonicity of the binomial row
between s and b<=A_0/2, gives

\[
\frac{\binom{A_0}{b}}{X_0}
>\frac{(256/e^{16/3})^j}{18e^{65}j^{17}}
>\frac{e^{j/5}}{18e^{65}j^{17}}>2. \tag{5}
\]

For clarity, the exact constants in the last two steps are justified
as follows. The first three positive atanh terms give
\(\log2>693/1000\), so
\(\log256-16/3=8\log2-16/3>1/5\).
The function \(j/5-17\log j\) increases for j>85.
At j=1024, use \(\log1024<7\) and \(\log36<4\) to obtain

\[
\frac{1024}{5}-65-17\log1024-\log36
>\frac{1024}{5}-65-119-4=\frac{84}{5}>0.
\]

The bound \(\log2<7/10\) follows from the first five terms of
the exponential series, whose sum at 7/10 is
\(482921/240000>2\). The bound \(\log36<4\) follows from
\(e>8/3\). No numerical logarithm approximation is used in (5).

### 3.2 Comparing with Y

For j>=1024>648,

\[
A_0>j^4/24>27j^3\ge b^3.
\]

The same b-only product comparison used in Section 1 gives

\[
\frac{Y_b}{\binom{A_0}{b}}<\frac1{b-1}\le\frac1{21}.
\]

Together with (5), the two right-side summands have total less than
the left side. The monotonicity in i excludes every larger i too.
Therefore

\[
\boxed{8j/3\le b\le3j\quad\Longrightarrow\quad j\le1023}
\tag{6}
\]

for any hypothetical L1 solution.

## 4. The remaining exact finite set

Equations (1), (2), and (6), together with the earlier lower height,
show that every remaining candidate is among the triples

\[
\boxed{
8\le j\le1023,\quad j+4\le i\le j+14,\quad
\max(22,\lceil8j/3\rceil)\le b\le3j,
\quad b^3<4\binom ij,quad \binom ij<b^4.
}
\tag{7}
\]

All bounds here are proved, not chosen experimental cutoffs.
The script `v5_l1_expanded_band.py` generates a modular or p-adic
contradiction for each triple and has an independent verifier.
The generator lists j and the offset first; the verifier lists b first.
Lucas digits are evaluated by factorial tables in one implementation
and direct small binomial values in the other. Valuations, when needed,
are evaluated by Legendre floor sums and independently by Kummer carries.

## 5. Completed finite verification

The set (7) has **355,759** triples. Every triple has an ordinary
Lucas congruence contradiction; no valuation fallback was needed.
The independent b-first verifier covered every candidate exactly once,
reported zero unresolved cases, and used a largest witness prime of 73.

The certificate is `v5_l1_expanded_band_certificates.json`; its SHA256 is

`cddf422267205ffafd2e3472940048abf71a87500e1c0382163e746f2fe2c943`.

The execution report is `v5_l1_expanded_band_verification.json`.
Reproduction:

```sh
python3 v5_l1_expanded_band.py generate
python3 v5_l1_expanded_band.py verify
```

The script imports the existing exact Lucas and integer-root helpers
from `v4_lower_l1_single_top.py`, and the optional valuation helpers
from `v4_upper_complement_two_dge3.py`.

Together with the previously certified band in `v4_lower_l1_band.md`,
this proves the entire stated interval \(8j/3\le b\le4j\) has no
solution for arbitrary original indices.

This argument and its finite certificates are not claimed to have
been formalized in Lean. No general exclusion is claimed outside
the stated band.
