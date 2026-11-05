# Exact certificates for j=i-2, ell=1, in both outer branches

**Completed theorem.** The original squared-index equation has no
solution with \(j=i-2\) and \(\ell=1\), in either outer branch.
The analytic cutoff and the independently verified finite certificates
below prove this for unbounded original parameters.

## Scope and size interval

Put \(n=i\), \(j=n-2\),

\[
A=\frac{n(n-1)}2,\qquad
X=\binom{n^2}{4n-4},\qquad
r=\min(k,A-k).
\]

For \(\ell=1\), the two branches have

\[
k=r,\ Y=r^2\quad\text{or}\quad
k=A-r,\ Y=(A-r)^2.
\]

The analytic theorem in `v4_upper_first_complement_two.md` proves
\(23\le n<2^{20}\). In either branch, \(Y<A^2<n^4<X\),
so a solution must satisfy

\[
X< L(r):=\binom Ar <2X. \tag{1}
\]

The necessary interval retained in the certificate is

\[
\max\bigl(n,\lfloor\varphi(n-2)\rfloor+1\bigr)
\le r\le
\min\bigl(\lfloor A/2\rfloor,c_n(n-2)-1\bigr),
\]

where \(c_n=10\) for \(n<802\) and \(c_n=5\) otherwise.
The binomial \(L(r)\) strictly increases throughout this interval.

## Exact endpoint verification

The generator `v4_upper_complement_two_l1.cpp` is an adaptation of the
already verified interval method in
`v4_upper_complement_two_j1_certification.md`. Here the outer top
\(A=n(n-1)/2\) is fixed while r varies. The comparison is

\[
D(r)=\log\binom Ar-\log\binom{n^2}{4n-4}.
\]

The exact integer bounds for this difference use the same factorial
remainder and numerator correction formulas as before, with
\(t=r\), \(N=n^2\), and \(q=4n-4\). They give integers
`loD, hiD` with

\[
\texttt{loD}\le 2Q D(r)\le\texttt{hiD},\qquad Q=2^{56}.
\]

An endpoint with `hiD<0` proves \(L(r)<X\); an endpoint with
`loD>2*LOG2_HI` proves \(L(r)>2X\). Only the integers strictly
between the two certified endpoints remain. For \(n<1024\), the
entire necessary interval is retained. Floating point is used only to
propose endpoints; all logical comparisons use exact integers.

The optional extended run reaches \(n<2^{21}\), so the same
certified intervals can support a separate argument with
\(\ell\ge2\), once \(Y<X\) has independently been proved.
This extension remains within the integer type bounds: the largest
numerator is at most

\[
2(5\cdot2^{21})^3 Q=250\cdot2^{119}<2^{127}.
\]

All other integer intermediates are smaller. The endpoint calculation
depends only on \(A,X,r\); it is reusable whenever a separate
family has the same A and X and a positive summand \(Y<X\).

## Congruence certificates

For every retained r, two prime witnesses are recorded, proving
respectively

\[
\binom Ar\not\equiv\binom{n^2}{4n-4}+r^2\pmod{p_0},
\]

\[
\binom Ar\not\equiv\binom{n^2}{4n-4}+(A-r)^2\pmod{p_1}.
\]

The generator uses Lucas' theorem with factorial and inverse tables.
Every recorded prime is below 1000. No candidate is accepted merely
because it passed a size approximation.

## Binary schema

The first eight bytes are the seven ASCII characters `V4JC2L1` and a
null byte. Three little-endian unsigned 32-bit integers give the first
n, exclusive last n, and small-n cutoff. Each consecutive n then has
two unsigned 32-bit endpoints `lo, hi`, followed by two bytes for each
\(r=\texttt{lo}+1,\ldots,\texttt{hi}-1\). The first byte gives
the lower-branch witness and the second the upper-branch witness, as
zero-based indices in the increasing prime list below 1000.

Thus a reader extracting only the certified intervals can skip exactly
\(2(\texttt{hi}-\texttt{lo}-1)\) bytes after each endpoint pair.
The list contains every n in order, with no omitted values.

## Executed runs

The base run through \(n<2^{20}\) covered **1,048,553** values of n
and produced **10,908,912** branch witnesses, with no survivors.

The extended run through \(n<2^{21}\) covered **2,097,129** values
of n and produced **15,103,216** branch witnesses, with no survivors.
Its certificate is `v4_upper_complement_two_l1_extended.bin`, and its
execution report is
`v4_upper_complement_two_l1_extended_report.json`.

The independent verifier uses the separately implemented interval and
Pascal-digit method from the preceding upper \(\ell=k-2\) verifier.
It completed successfully for the entire extended file: every one of
the 2,097,129 parameter values, both endpoint inequalities when needed,
and all 15,103,216 branch records were verified. Eight small central
cases have \(r=A-r\), so there are 15,103,208 distinct equations;
the duplicate branch records are harmless and checked explicitly.
The largest witness prime was 23. The verifier uses only integer
arithmetic, 28-term interval-propagated logarithms at precision
\(2^{52}\), and Pascal-row Lucas digits.

The verifier source is `v4_upper_complement_two_l1_verify.cpp`, and the
complete report is
`v4_upper_complement_two_l1_extended_verification.json`.
The extended certificate SHA256 is
`5ec127d0e32ca1a43a7789e8115a8d8a7d10a784cace6830e02cf7f169fef144`.
Its uncompressed size is 31,880,268 bytes. The enclosing ZIP compresses
the certificate; no duplicate gzip file is needed. No Lean formalization
of this complete theorem is claimed.

## Reproduction

```bash
g++ -O3 -std=c++17 v4_upper_complement_two_l1.cpp -o v4_upper_complement_two_l1
./v4_upper_complement_two_l1 2097152 v4_upper_complement_two_l1_extended
g++ -O3 -std=c++17 v4_upper_complement_two_l1_verify.cpp -o v4_upper_complement_two_l1_verify
./v4_upper_complement_two_l1_verify v4_upper_complement_two_l1_extended.bin v4_upper_complement_two_l1_extended_verification.json
```

The full \(\ell=1\) theorem uses only n below \(2^{20}\). Extra
certified intervals above that cutoff do not themselves exclude cases
with \(\ell\ge2\); those require their own coverage and modular or
p-adic certificates.
