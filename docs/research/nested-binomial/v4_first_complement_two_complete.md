# Complete exclusion of j=i-2, for both outer branches

## Theorem

For valid nonnegative binomial arguments, the original squared-index
equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

has **no solution with \(j=i-2\)**. There is no bound on the
original four indices in this statement, and neither outer branch
is omitted.

This theorem combines ordinary mathematical proofs with exact finite
certificates whose complete ranges follow from proved inequalities.
The theorem as a whole is not asserted to be Lean-formalized. The
separate Lean file proves the universal divisibility lemmas, with its
scope recorded in `v4_formal/README.md`.

## 1. Partition of all cases

Let

\[
A=\binom i2,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{4i-4},\quad Y=\binom{k^2}{\ell^2}.
\]

The earlier endpoint arguments exclude \(j=0\), \(\ell=0\),
\(\ell=k\), and noninterior outer arguments. Thus it suffices
to consider \(1\le\ell\le k-1\), \(1<B<A\).

The prior first-summand bound gives \(r\ge j+2=i\), where
\(r=\min(B,A-B)\le A/2\). Thus \(A\ge2i\), and
\(A=i(i-1)/2\) forces \(i\ge5\). In particular the effective
first index is indeed \(\min(i-2,2)=2\); no tiny-index exception
is hidden in the later effective-index partition.

If \(\ell=1\), both outer branches are excluded by Section 2 below.
Suppose \(\ell\ge2\). The branches are

- lower: \(B\le A/2\);
- upper: \(A-B\le B\).

They cover all possibilities, with harmless overlap at \(A=2B\).

In the lower branch, the previously proved classification of
\(\ell>j\) requires \(i-j\ge4\), contrary to \(i-j=2\).
The case \(\ell=j\) was also already excluded. Consequently
\(2\le\ell<j\), so the small-M result gives \(j\ge21\) and
\(i\ge23\). This is exactly the scope of Section 3 below.

In the upper branch, \(\ell=k-1\) is impossible: then
\(B=\ell+1\le M+1\), whereas the previous gap lower bound gives
\(t=A-B\ge M+2\), contradicting \(t\le B\). Thus the
effective index \(e=\min(\ell,k-\ell)\) is at least 2.
Since the effective first index is 2, the prior equal-effective-index
theorem excludes \(e=2\). The remaining \(e\ge3\) upper cases
are excluded by Section 4.

The prior dependencies are `proof_reduction.md`,
`lower_branch_reduction.md`, `equal_effective_upper.md`,
`sharp_q_bounds.md`, and the complete small-M certificate indexed
in `PROGRESS_v3_ja.md`.

## 2. ell=1 in both branches

The analytic common-prime-product argument in
`v4_upper_first_complement_two.md` proves
\(i<2^{20}\). It retains the large-prime part of

\[
P=\prod_{s=0}^{\lfloor i/2\rfloor-1}(A-s).
\]

This part divides both the outer binomial and X, so it must divide
\(Y=k^2\). Beyond the stated cutoff its proved size exceeds Y.

The complete finite verification, described in
`v4_upper_complement_two_l1_certification.md`, uses exact endpoints
for

\[
X<\binom Ar<2X,\qquad r=\min(k,A-k).
\]

At each retained r it checks both \(k=r\) and \(k=A-r\).
The verified extended certificate covers every
\(23\le i<2^{21}\), which contains the entire required range
\(i<2^{20}\). Its extension is also used in Section 3.

It contains 15,103,216 branch records. Eight pairs coincide when
\(r=A/2\), giving 15,103,208 distinct equations. Every equation
has a Lucas congruence contradiction using a prime at most 23.
The independent verifier recalculates every endpoint with a different
integer interval method and every congruence via Pascal-row digits.

Certificate: `v4_upper_complement_two_l1_extended.bin`.
SHA256:
`5ec127d0e32ca1a43a7789e8115a8d8a7d10a784cace6830e02cf7f169fef144`.

## 3. Lower branch with ell>=2

The proof in `v4_first_complement_two_lower.md` shows

\[
\boxed{i<2^{21}.}
\]

For \(i\ge802\), one has \(B<5i\) and
\(k<\sqrt{10i}+1\). Thus the same common-prime part of P,
which must divide Y, eventually exceeds
\(Y<16(5i)^{2k}\). The explicit inequality for \(i\ge2^{21}\)
is

\[
\log P_{>5i}-\log Y
>\frac{79i}{320}-\frac{2219}{200}>0.
\]

Also \(X>Y\) for \(i\ge1024\), giving
\(X<\binom AB<2X\). The extended certificate of Section 2
therefore supplies the necessary B window. At \(i<1024\), its
full necessary range is retained and no such comparison is assumed.

The finite check enumerates every representation
\(B=\binom{k}{\ell}\) with effective lower index at least 2
up to the proved maximum \(5(2^{21}-3)-1\). There are 10,492
oriented representations and 5,244 distinct binomial values in this
auxiliary set. The window intersections, with \(2\le\ell<i-2\),
leave **150,663** candidates. All have congruence contradictions,
with primes at most **67**.

The independent verifier enumerates representations with k first
instead of the effective index first, uses direct binomial values,
visits every integer inside each certified window instead of binary
searching the representable values, and recomputes the Lucas residues
with a separate implementation. It checks all 2,097,129 first indices
in the finite range, finds no missing or duplicate candidate, and passes.

Files: `v4_first_complement_two_lower.py`,
`v4_first_complement_two_lower_certificates.json`, and
`v4_first_complement_two_lower_verification.json`.
Certificate SHA256:
`aa2ec4edc8bc0347d8cd9d5f326b114730133deb0cf09b9ee994e75b29bebf0a`.
The separate endpoint-verifier pass for the matching extended binary
is a necessary part of this certificate chain.

## 4. Upper branch with effective index e>=3

The analytic proof in `v4_upper_first_complement_two.md` gives

\[
\boxed{i<2^{22}.}
\]

Here the upper ordering theorem gives \(k<i\), and
\(\binom k3\le B<A<i^2\) forces
\(k<(11/6)i^{2/3}+2\). The large-prime part of P grows too fast
to divide \(Y<16i^{4k}\) past the cutoff.

The proof and full finite coverage are described in
`v4_upper_first_complement_two_ege3.md`. There are **350,544**
candidates, both actual orientations \(\ell=e\) and
\(\ell=k-e\) included. Of these, 350,352 have ordinary Lucas
congruence contradictions; **192** require a p-adic valuation
comparison. The latter have exactly one smallest valuation among
the three terms, which is incompatible with an equality of their sum.

The independent verification changes the enumeration and triangular
interval construction, verifies residues by direct digit binomials,
and verifies valuations via Kummer carries instead of Legendre
factorial sums. It passes with no unresolved case.

Certificate: `v4_upper_first_complement_two_ege3_certificates.json`.
SHA256:
`774acdba55f880684e4006bad38f7fac6bb3b16198eeab30d0fec2141e187560`.

Sections 1--4 cover every valid case with j=i-2, proving the theorem.
Together with the earlier endpoint results, every possible solution
of the original equation therefore satisfies

\[
\boxed{1\le j\le i-3.}
\]

This does not determine whether solutions exist among those remaining
indices.

## Reproduction of the new finite parts

Keep all files from the bundle in one directory, and do not disable
Python or C++ assertions. The extended binary is included directly.

```sh
g++ -O3 -std=c++17 v4_upper_complement_two_l1_verify.cpp -o v4_upper_complement_two_l1_verify
./v4_upper_complement_two_l1_verify v4_upper_complement_two_l1_extended.bin v4_upper_complement_two_l1_extended_verification.json
python3 v4_first_complement_two_lower.py verify
python3 v4_upper_first_complement_two_ege3.py verify
```

To regenerate the extended binary, compile
`v4_upper_complement_two_l1.cpp` and run it with arguments
`2097152 v4_upper_complement_two_l1_extended`.
