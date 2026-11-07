# Shared prime factors for j=i-2

**Completed exclusions.** Together with the independently verified
finite certificates described in Section 5, this note proves that
there is no upper-branch solution with \(j=i-2\), for any valid
\(\ell\). It also excludes \(j=i-2,\ell=1\) in the lower branch.

## Scope

Consider the squared-index equation, and suppose \(j=i-2\).
Write \(n=i\) and

\[
A=\binom n2=\frac{n(n-1)}2,\quad
B=\binom{k}{\ell},\quad r=\min(B,A-B),
\]

\[
L=\binom Ar,\qquad X=\binom{n^2}{4n-4},\qquad
Y=\binom{k^2}{\ell^2}.
\]

This note proves analytic cutoffs for two scopes:

1. **Both outer branches with \(\ell=1\):** \(n<2^{20}\).
2. **The upper branch with effective index
   \(e=\min(\ell,k-\ell)\ge3\):** \(n<2^{22}\).

For the upper branch, these cover all remaining possibilities:
effective index 2 is excluded by the previous equal-effective-index
theorem, and effective index 1 must mean \(\ell=1\), because the
upper branch excludes \(\ell=k-1\).

The earlier small-index exclusion gives \(n\ge23\). In the first
scope \(M=\max(j,\ell)=n-2\) directly. In the second scope the
upper opposite-ordering theorem gives \(k<n\), hence again
\(M=n-2\). Therefore the previous uniform bounds give

\[
n\le r<10(n-2),\qquad
n\ge802\Longrightarrow r<5(n-2)<5n. \tag{1}
\]

The stronger golden-ratio lower bound \(r>\varphi(n-2)\) is also
available. These statements use `sharp_q_bounds.md` and
`entropy_phi_reduction.md`; they hold in both outer branches whenever
\(M=n-2\).

## 1. A numerator product shared by L and X

Assume \(n\ge802\). Put

\[
h=\lfloor n/2\rfloor,
\qquad P=\prod_{s=0}^{h-1}(A-s),
\]

and retain the full powers of primes greater than \(5n\), calling
the result \(P_{>5n}\). Since \(r\ge n>h\), the numerator of
\(L=\binom Ar\) contains every factor of P. Its denominator
\(r!\) contains no prime greater than \(5n\).

For \(0\le s<h\), the numerator of X contains the distinct integers

\[
2(A-s)=n^2-n-2s,
\]

because each lies between \(n^2-(4n-4)+1\) and \(n^2\).
The denominator \((4n-4)!\) has no prime greater than \(5n\).
Multiplication by 2 changes no such valuation. Consequently

\[
\boxed{P_{>5n}\mid\gcd(L,X)\mid Y.} \tag{2}
\]

This retains full prime powers, including multiplicities from distinct
factors of P; it is not merely a statement about squarefree radicals.

## 2. Lower bound for the common prime part

All factors of P are at most \(A<n^2/2\), and

\[
A-h+1>\frac{n(n-2)}2.
\]

The same interval valuation count and explicit prime-sum estimates
used in `v4_upper_complement_two.md` therefore give

\[
\boxed{
\log P_{>5n}>
\frac{n-1}{2}\log\frac{n-2}{10}
-\frac{23n}{4}-2n^{2/3}.
} \tag{3}
\]

For clarity, for each prime \(p\le5n\), the count of multiples in
an interval of length h implies
\(v_p(P)\le h/(p-1)+\lfloor\log_p A\rfloor\).
One then uses
\(\sum_{p\le5n}\log p/(p-1)<\log(5n)\) and

\[
\sum_{p\le5n}\lfloor\log_p A\rfloor\log p
=\theta(5n)+\psi(A)-\theta(A)
<\frac{23n}{4}+2n^{2/3}.
\]

The equality holds because \(5n<A<(5n)^2\) for \(n\ge802\).
The cited prime-sum estimates, their domains, and primary references
are those already checked in the preceding common-prime note.

For \(n\ge4\),
\(\log(1-2/n)>-2/(n-2)\ge-4/n\). Thus (3) implies

\[
\log P_{>5n}>
\frac{n-1}{2}\log n-\frac{n-1}{2}\log10
-2-\frac{23n}{4}-2n^{2/3}. \tag{4}
\]

This differs by just one unit from the sharpened estimate in
`v4_upper_complement_two_sharper_bounds.md`.

## 3. ell=1, both outer branches

Here \(B=k\), so \(k<A<n^2\), regardless of the outer branch.
Consequently \(Y=k^2<n^4\).

If \(n\ge2^{20}\), insert the exact inequalities
\(\log2>693/1000\), \(\log10<231/100\), and
\(n^{2/3}<n/100\) into (4), exactly as in the preceding sharper
bound. This gives

\[
\log P_{>5n}-4\log n>
\frac{n-12643}{200}>0.
\]

Then \(P_{>5n}>Y\), contradicting (2). Therefore

\[
\boxed{j=i-2,\ \ell=1\quad\Longrightarrow\quad i<2^{20}.} \tag{5}
\]

This cutoff is valid in both outer branches.

## 4. Upper branch with effective second index at least 3

The upper ordering theorem gives \(k<n\), and

\[
\binom k3\le\binom ke=B<A<n^2.
\]

Hence \((k-2)^3<6n^2\), so
\(k<(11/6)n^{2/3}+2\). The existing binomial ratio bound gives

\[
Y<16B^{2\ell}<16n^{4k},
\qquad
\log Y<\log16+
\left(\frac{22}{3}n^{2/3}+8\right)\log n.
\]

For \(n\ge2^{22}\), the same rational comparison as before,
now using (4), yields

\[
\log P_{>5n}-\log Y>
\frac{269n}{40000}-\frac{33359}{250}>0.
\]

Again (2) is contradicted. Thus

\[
\boxed{j=i-2,\ e\ge3,\ B\ge A/2\quad\Longrightarrow\quad i<2^{22}.}
\tag{6}
\]

## 5. Exact finite completion

The \(\ell=1\) finite part uses the necessary size interval

\[
X<L=X+Y<2X.
\]

Indeed \(Y=k^2<A^2<n^4<X\), since
\(X\ge\binom{n^2}{3}>n^4\). Both outer branches share the same
strictly increasing function \(L(r)=\binom Ar\) for
\(1\le r\le A/2\). Their squared summands are \(r^2\) and
\((A-r)^2\). Thus one set of rigorously certified r intervals
serves both branches; every retained r receives two congruence
witnesses.

The interval proof and execution records are in
`v4_upper_complement_two_l1_certification.md`. Its extended certificate
has been independently verified for all \(23\le n<2^{21}\), more
than the cutoff (5) requires: 15,103,216 branch witness records, zero
unresolved cases, all endpoint inequalities recalculated exactly.

The remaining upper-branch effective-index \(e\ge3\) family was
enumerated completely below the cutoff (6). All **350,544** candidates
were excluded: 350,352 by Lucas congruences and **192** by a unique
smallest p-adic valuation. The independent verifier reconstructed the
full candidate set in a different enumeration order, checked Lucas
digits with a separate method, and verified valuations by Kummer
carries rather than Legendre floor sums.

The generator and verifier are
`v4_upper_first_complement_two_ege3.py`; the certificate and report are
`v4_upper_first_complement_two_ege3_certificates.json` and
`v4_upper_first_complement_two_ege3_verification.json`.
The certificate SHA256 is
`774acdba55f880684e4006bad38f7fac6bb3b16198eeab30d0fec2141e187560`.

Effective index 2 was excluded earlier, effective index 1 in the
upper branch is precisely the \(\ell=1\) case just certified, and
effective indices at least 3 are now certified. Therefore the entire
upper \(j=i-2\) family is empty. The lower \(\ell\ge2\) cases
are handled by the separate argument in
`v4_first_complement_two_lower.md`. The assembled theorem excluding
\(j=i-2\) in all branches is
`v4_first_complement_two_complete.md`.
No Lean formalization of these full exclusion theorems is claimed.
