# Prime first upper index: a global reduction of the lower branch

We use the original equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

and write \(A=\binom ij\), \(B=\binom{k}{\ell}\),
\(X=\binom{i^2}{j^2}\), \(Y=\binom{k^2}{\ell^2}\),
\(t=A-B\), \(r=\min(B,t)\).

All conclusions below combine proved uniform reductions with explicitly
verified finite remainders. They do not claim global nonexistence of the
original equation. No proof assistant has been executed.

## 1. No prime first upper index in L2 with \(B\ge3j\)

**Theorem.** A solution satisfying

\[
B\le A-B,\qquad j>\ell,\qquad B\ge3j
\]

cannot have prime \(i\).

**Proof.** The previous \(M\le20\) certificate permits us to assume
\(M=j\ge21\). Write \(i=p\) prime and \(d=p-j\ge2\).

For \(j\ge100\), Section 6 of lower_branch_reduction.md proves
\(d\in\{2,3\}\). For these offsets, the uniform proof in
prime_upper_index_large_gap.md excludes \(\ell=1\) for all such primes,
and excludes all \(\ell\ge2\) for \(p\ge16384\).
The remaining \(\ell\ge2\), \(p<16384\) candidates have the necessary
bands

\[
\begin{array}{c|c}
d=2 & 4j+5\le B<(5\text{ if }j\ge800\text{ else }10)j\\
d=3 & 3j<B<4j
\end{array},
\qquad 2B\le A.
\]

The exact finite certificate verifies all 295,411 candidates in these
bands, with none unresolved:

| Offset | Candidates excluded |
|---|---:|
| \(d=2\) | 141,865 |
| \(d=3\) | 153,546 |

All witnesses are congruence contradictions at primes at most 71.
The generator enumerates \(k\) first and uses an exact recurrence for
\(\binom{k}{e}\), \(e=\min(\ell,k-\ell)\). The verifier instead enumerates
\(e\) first, determines \(k\) intervals by exact binomial binary searches,
and recomputes each Lucas residue with exact math.comb on the base-prime
digits. It separately checks primality, completeness, duplicates, and
extraneous rows.

For \(21\le j\le99\), we do not assume \(d\in\{2,3\}\).
Section 2 of lower_branch_reduction.md gives

\[
A<B^3<(10j)^3=1000j^3.
\]

Thus the strictly increasing function \(\binom pj\) gives a proved
finite range for \(p\), with all offsets \(d\ge2\) included.
There are 93 admissible pairs \((j,p)\), with largest \(p=103\).
For each pair we include \(\ell=1\), and for \(\ell\ge2\) use
\(\binom{k}{2}\le B<10j\) to bound \(k\).
The known offset bands are applied where valid:

- \(d=2\) implies \(B\ge4j+5\);
- \(d=3\) implies \(B\ge3j+1\);
- \(j\ge30,\ d\ge3\) implies \(B<4j\).

All 13,458 candidates are excluded, using prime witnesses at most 17.
This includes 11,819 candidates with \(\ell=1\) and 1,639 with
\(\ell\ge2\). The independently implemented verifier obtains its prime
range from the separately checked inequality
\(\binom{2j}{j}>1000j^3\) for each of the 79 integers \(21\le j\le99\),
then uses an effective-index-first enumeration.
There are no unresolved candidates.

These cases exhaust all \(j\), proving the theorem. \(\square\)

The two finite checks can be reproduced by

    python finite_prime_outer_exclusion.py verify
    python finite_small_j_prime_exclusion.py verify

Their certificate and report filenames have the respective prefixes
finite_prime_outer_ and finite_small_j_prime_.

## 2. A uniform exclusion of \(\ell=1,\ i=p\) in both branches

For completeness, the short uniform argument used in the further
reduction is given here. This argument was developed independently in
the companion analysis.

Suppose \(\ell=1\), \(i=p\) prime. We may assume \(j\ge21\), hence
\(p\ge23\), \(j\le p-2\), and \(r<10j<10p\).
Then \(B=k\), \(Y=B^2\), and

\[
A=pa,\qquad a\equiv\frac{(-1)^{j-1}}j\pmod p,\qquad X\equiv0\pmod p.
\]

If \(p\nmid B\), Lucas gives \(\binom AB\equiv0\pmod p\), whereas
\(X+B^2\not\equiv0\). Thus \(p\mid B\), and consequently \(p\mid r\).
Write \(r=mp\), \(1\le m\le9\).
Let \(a_0\in\{1,\ldots,p-1\}\) be the residue of \(a\). Lucas now gives

\[
0\equiv\binom Ar\equiv\binom{a_0}m\pmod p,
\qquad\text{so }a_0<m.
\]

The value \(a_0=1\) is impossible: it would give
\(j\equiv(-1)^{j-1}\pmod p\), forcing \(j=1\) or \(j=p-1\),
both excluded. Thus \(a_0\ge2\).
There is an integer \(1\le h\le a_0-1\) with

\[
a_0j=hp+(-1)^{j-1},
\qquad
j\le\frac{(a_0-1)p+1}{a_0}.
\]

Since \(m\ge a_0+1\),

\[
r-5j\ge
\frac{\bigl((a_0-2)^2+1\bigr)p-5}{a_0}>0.
\]

If \(p-j\ge3\), the already proved offset-specific bound
\(r<5j\) from sharp_q_bounds.md contradicts this.
If \(p-j=2\), then \(a_0=(p-1)/2\ge11>m\), also impossible.
Thus

\[
\boxed{\ell=1,\ i\text{ prime is impossible in either branch}.}
\]

## 3. All larger effective second indices are excluded

**Theorem.** In the lower branch \(B\le A-B\), if \(j>\ell\) and
\(i=p\) is prime, a remaining solution must satisfy

\[
\boxed{
\ell\in\{2,k-2\},\quad
B=\binom{k}{2}<3j,\quad
p-j\ge4,\quad
p\le k^2<6j+\sqrt{6j}+1.
}
\tag{1}
\]

**Proof.** By Sections 1 and 2, it suffices to consider \(B<3j\) and
\(\ell\ge2\). Since \(k-\ell\ge2\),

\[
\binom{k}{2}\le B<3j.
\]

As \(j\ge21\), this implies \(k<j<p\). In particular \(p\nmid B\).
Since \(p\mid A\) and \(X\equiv0\pmod p\), Lucas forces \(p\mid Y\).
If \(k^2<p\), all factorials in \(Y=\binom{k^2}{\ell^2}\) would be
invertible modulo \(p\), a contradiction. Hence \(p\le k^2\).

Put \(e=\min(\ell,k-\ell)\). Suppose \(e\ge3\). Then

\[
\binom{k}{3}\le B<3j<3p\le3k^2,
\]

so

\[
(k-1)(k-2)<18k,\qquad k^2-21k+2<0.
\]

For every integer \(k\ge21\), the latter polynomial is positive
(it equals 2 at 21 and increases). Therefore \(k\le20\), and
\(p\le k^2\le400\).

This leaves exactly the following finite set of necessary candidates:

\[
\begin{gathered}
p\le400\text{ prime},\quad
21\le j\le p-2,\quad 6\le k\le20,\quad 3\le\ell\le k-3,\\
p\le k^2,\qquad
j+2\le B=\binom{k}{\ell}<3j,\qquad
2B\le A=\binom pj.
\end{gathered}
\]

The exact certificate excludes all 9,078 candidates, with none
unresolved. The distribution by effective second lower index is

| \(e\) | Candidates excluded |
|---|---:|
| 3 | 8,448 |
| 4 | 616 |
| 5 | 14 |

No candidates meet the conditions with \(e\ge6\).
All witness moduli are primes at most 23. The generator enumerates
\((k,\ell,p,j)\); the independent verifier enumerates \((p,j,e,k)\),
handles the binomial symmetry explicitly, and recomputes all modular
values by a second Lucas implementation.

Thus \(e=2\), so \(\ell=2\) or \(k-2\).
The previously proved offset comparisons give \(B>4j+4\) at offset
2 and \(B>3j\) at offset 3, both incompatible with \(B<3j\).
Hence \(p-j\ge4\).
Finally

\[
k(k-1)<6j,\qquad k<\sqrt{6j}+1,
\]

and consequently \(p\le k^2<6j+k<6j+\sqrt{6j}+1\).
This proves (1). \(\square\)

The final finite check can be reproduced by

    python finite_prime_effective_index.py verify

The certificate and report are
finite_prime_effective_index_certificates.json and
finite_prime_effective_index_verification.json.

## 4. An additional congruence when \(\ell=2\)

In the remaining subcase \(\ell=2\), the condition \(p\mid Y\) reads

\[
p\mid k^2(k^2-1)(k^2-2)(k^2-3).
\]

Here \(k<j\le p-4\), so \(p\) divides none of \(k,k-1,k+1\).
Therefore

\[
\boxed{k^2\equiv2\text{ or }3\pmod p.}
\]

This is a necessary condition only. Neither this subcase nor
\(\ell=k-2\) has been excluded for every unbounded \(p\).

## Verification limits

The three finite verifiers were actually executed and passed, with
295,411, 13,458, and 9,078 excluded candidates respectively.
Their ranges follow from the preceding analytic arguments; they are not
arbitrary numerical cutoffs. The verifiers establish the finite
congruence exclusions, while the written proofs establish why those
finite ranges suffice for the stated theorems.

The original equation remains unsolved globally. In particular, the
triangular second-binomial family in (1), the other lower-branch type,
and upper-branch families remain to be settled.
