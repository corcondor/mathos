# Complete exclusion of the upper branch with ell=k-2

## Theorem

For valid nonnegative binomial arguments, the equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

has **no solution** satisfying

\[
\boxed{\ell=k-2,\qquad
\frac12\binom ij\le\binom{k}{\ell}<\binom ij.}
\]

The proof combines an analytic reduction valid at unbounded parameter
sizes with exact finite certificates. The finite coverage follows from
proved bounds, not an experimental cutoff. This theorem does not settle
the entire original equation, and this whole theorem is not claimed to
have been formalized in Lean.

## 1. Reduction to two cases

Put

\[
A=\binom ij,\quad B=\frac{k(k-1)}2,\quad t=A-B,
\quad L=\binom At,\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{4k-4}.
\]

The upper branch is \(0<t\le B\). We use the already proved
small-index exclusion \(M=\max(j,\ell)\le20\), boundary
exclusions, and the ordering theorem for effective lower indices
\(d=\min(j,i-j)\), \(e=\min(\ell,k-\ell)\).

Here \(e=2\). Equal effective indices are impossible; effective
index 1 on the first side must be \(j=1\), since \(j=i-1\) is
already excluded. If \(d\ge3\), the opposite-ordering and adjacent-top
exclusions give \(i+2\le k\). Thus the only remaining possibilities
are

1. \(j=1\), or
2. \(d\ge3\) and \(i+2\le k\).

In both cases \(M=k-2\), \(k\ge23\), \(t\ge k\), and
\(t<10(k-2)\); for \(k\ge802\), \(t<5(k-2)\).
The source proofs are `upper_order_and_prime_support.md`,
`sharp_q_bounds.md`, and the earlier certified small-M result indexed
in `PROGRESS_v3_ja.md`.

## 2. The unbounded part is excluded analytically

For \(k\ge802\), set

\[
P=\prod_{s=1}^{\lfloor k/2\rfloor}(B+s).
\]

Retain the full powers of primes greater than \(5k\), denoting this
part by \(P_{>5k}\). The outer numerator contains every \(B+s\),
and the numerator of \(Y\) contains the distinct multiples
\(2(B+s)=k^2-k+2s\). Neither denominator contains a prime greater
than \(5k\). Therefore

\[
P_{>5k}\mid\gcd(L,Y)\mid X. \tag{1}
\]

Explicit prime-sum estimates then give

\[
\log P_{>5k}>
\frac{k-1}{2}\log\frac{k-1}{10}
-\frac{23k}{4}-2k^{2/3}. \tag{2}
\]

The complete proof, including prime-power multiplicities, is in
`v4_upper_complement_two.md`. Exact rational comparisons recorded in
`v4_upper_complement_two_sharper_bounds.md` compare (2) with
\(X<k^4\) when \(j=1\), and with
\(X<16k^{4i}\), \(i<(11/6)k^{2/3}+2\), when \(d\ge3\).
They imply

\[
\boxed{j=1\Longrightarrow k<2^{20},\qquad
d\ge3\Longrightarrow k<2^{22}.} \tag{3}
\]

The analytic argument and its constants were independently audited.

## 3. Exact finite certificate for j=1

Here \(i=A=B+t\) and \(X=A^2\). Since \(A<k^2\) and
\(Y>k^4\), any solution must have

\[
Y<\binom{B+t}{t}<2Y.
\]

For each of the **1,048,553** integers \(23\le k<2^{20}\), the
generator certifies endpoints for the strictly increasing outer
binomial using exact integer logarithm intervals. It then supplies a
Lucas congruence contradiction for each integer t between the
endpoints. At small k the whole necessary t interval is checked.

The complete run produced **5,455,320** congruence witnesses, all
using primes at most **19**, with **zero survivors**. The binary
certificate includes every consecutive k and every retained t.

The independent verifier uses a different fixed-point precision
\(2^{52}\), 28 atanh terms with individually propagated upper and
lower intervals, separate binomial enclosures, an integer-only square
root, and Pascal-row Lucas digits. The generator instead uses
\(2^{56}\), 24 terms with a proved global error bound, and factorial
tables. The verifier recalculated every endpoint and every witness,
checked complete coverage, and passed.

Files:

- Proof of the interval arithmetic and certificate format:
  `v4_upper_complement_two_j1_certification.md`.
- Generator: `v4_upper_complement_two_j1.cpp`.
- Independent verifier: `v4_upper_complement_two_j1_verify.cpp`.
- Complete certificate: `v4_upper_complement_two_j1.bin`.
- Execution and verification reports: `v4_upper_complement_two_j1_report.json`
  and `v4_upper_complement_two_j1_verification.json`.

Certificate SHA256:
`ab4a1f4400ca9c4545a175db31b212deca4121d09603ab6e5a5b7f3a75260fcf`.
Its uncompressed size is 13,843,764 bytes. The enclosing ZIP compresses
the certificate; a duplicate gzip file is not required in the bundle.

## 4. Exact finite certificate for effective index d>=3

The bound in (3), together with \(A<B+10(k-2)\), gives

\[
A\le8,796,128,673,762,
\qquad i\le37,512.
\]

For each admissible \(A=\binom id\), the small-gap inequality permits
only a short interval of triangular numbers \(B=k(k-1)/2\).
Both actual lower indices \(j=d\) and \(j=i-d\) are retained.

There are **350,164** complete finite candidates. Of these,
**350,011** are excluded by Lucas residues. The remaining **153**
are excluded by p-adic valuations: for a prime at most 7, exactly one
of \(v_p(L),v_p(X),v_p(Y)\) is smallest, contradicting
\(L-X-Y=0\).

The independent verifier changes the enumeration order, reconstructs
the triangular interval by integer binary searches, checks residues
with `math.comb` on base-p digits, and verifies valuations using
Kummer carries rather than the generator's Legendre floor sums.
Every candidate was covered exactly once, with no unresolved case.

Files:

- Detailed proof and coverage explanation:
  `v4_upper_complement_two_dge3.md`.
- Generator and independent verifier modes:
  `v4_upper_complement_two_dge3.py`, with helper dependency
  `v4_lower_l1_single_top.py`.
- Certificates and verification report:
  `v4_upper_complement_two_dge3_certificates.json` and
  `v4_upper_complement_two_dge3_verification.json`.

Certificate SHA256:
`719f8090b51407e6bf7a8f9ad54b76489cb70fbfacb55843d47c243fd572910f`.

Together, Sections 1–4 exclude all cases in the stated theorem.

## Reproduction

```bash
g++ -O3 -std=c++17 v4_upper_complement_two_j1.cpp -o v4_upper_complement_two_j1
./v4_upper_complement_two_j1
g++ -O3 -std=c++17 v4_upper_complement_two_j1_verify.cpp -o v4_upper_complement_two_j1_verify
./v4_upper_complement_two_j1_verify
python3 v4_upper_complement_two_dge3.py generate
python3 v4_upper_complement_two_dge3.py verify
```

The analytic inequalities depend on the explicitly cited primary
prime-sum estimates of Rosser–Schoenfeld and Dusart; the interval
certificate uses Robbins' explicit factorial remainder. Their exact
statements and references are recorded in the component proof notes.
