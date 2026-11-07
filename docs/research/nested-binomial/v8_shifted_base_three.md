# Complete exclusion of the shifted powers of three

## Theorem

For the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

there is no solution in the entire family

\[
\boxed{\ell=1,\qquad j=i-3,\qquad i=3^a+2,\quad a\ge1.}
\tag{1}
\]

Both outer branches are included. Combining this result with the v7
cofactor-three theorem also proves

\[
\boxed{\ell=1,\qquad j=i-3,\qquad
i=3p^a+2,\quad p\text{ prime},\quad a\ge1
\quad\Longrightarrow\quad\text{no solution}.}
\tag{2}
\]

In (2), the case \(p=3\) is now included. The v7 theorem had excluded
only \(p\ne3\). This closes the remaining prime base in that family.
It does not solve every offset-three case or the original equation.

## 1. Inputs already proved

Set

\[
z=3^a,\quad n=z+2,\quad A=\binom n3,\quad
r=\min(k,A-k).
\]

The v5 gap and v6 common-divisor theorem give

\[
3n<r<10n/3,\qquad
Q:=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{3}
\]

`v7_offset_shifted_prime_powers.md`, Section 4, proves that any
remaining solution with \(n=3^a+2\) must satisfy

\[
\boxed{a\ge9\text{ odd},\qquad d:=v_3(r)=(a-1)/2.}
\tag{4}
\]

The coverage of the earlier exponents in that proof is explicit:
\(a\le4\) gives \(j\le100\); \(a=5\) is excluded by a forced
divisor 4270 of \(r\) at \(n=245\); \(a=6,7\) give squarefree
\(n=731,2189\); and the valuation balance excludes all even
\(a\ge8\). Thus (4) leaves no unverified small-exponent case.

## 2. The common divisor forces a finite exponent bound

Since \(n=3^a+2\) is odd and \(n\equiv2\pmod3\), we have

\[
Q=\frac{n(n-1)}2,\qquad \gcd(Q,3)=1.
\]

Write \(r=3^dv\). From \(Q\mid r^3\) and coprimality,
\(Q\mid v^3\), hence \(Q\le v^3\). Applying the strict upper
gap in (3) gives

\[
\frac{n(n-1)}2
\le\left(\frac r{3^d}\right)^3
<\frac{1000n^3}{27\,3^{3d}}.
\]

Therefore

\[
3^{3d}<\frac{2000n^2}{27(n-1)}.
\]

Substitute \(2d=a-1\), \(z=3^a\), and divide by \(z\):

\[
\boxed{
3^{(a-3)/2}
<\frac{2000}{27}\frac{(z+2)^2}{z(z+1)}.
} \tag{5}
\]

For \(z>320\), an elementary rational bound gives

\[
\frac{(z+2)^2}{z(z+1)}
=1+\frac{3z+4}{z(z+1)}
<1+\frac4z
<\frac{81}{80}.
\]

Here \(z\ge3^9>320\). Thus (5) implies

\[
\boxed{3^{(a-3)/2}<\frac{2000}{27}\frac{81}{80}=75<81.}
\tag{6}
\]

Every odd \(a\ge11\) would make the left side at least
\(3^4=81\), which is impossible. In view of (4), only \(a=9\)
remains. The bound on the exponent is proved, rather than imposed
as a search cutoff.

## 3. The single remaining exponent

For \(a=9\),

\[
n=3^9+2=19685=5\cdot31\cdot127.
\]

The three factors are distinct primes, so \(n\) is squarefree and
\(3\nmid n\). Formula (3) implies \(n\mid r^3\), hence
\(n\mid r\). But the strict interval

\[
3n<r<10n/3
\]

contains no multiple of \(n\). This excludes \(a=9\) and completes
the proof of (1).

For (2), the v7 cofactor-three theorem already covers every prime
\(p\ne3\). When \(p=3\), the first index is
\(3\cdot3^a+2=3^{a+1}+2\), covered by (1).

## Verification and audit

`v8_shifted_base_three_checks.py` verifies the exact factorization,
the primality of its three factors by deterministic trial division,
the rational inequalities and constants in (5)-(6), and the
small-exponent coverage stated above. The proof uses no assumption
about Wieferich primes, and no prime or exponent scan is needed.
The new proof has not been formalized in Lean.

The composite-family peer reviewer independently audited the full
argument and reported PASS on 2026-11-05, including the cancellation
of the 3-power from \(Q\mid r^3\), the strict exponent bound, the
single exceptional factorization, and the completion of the case
\(p=3\) in the v7 cofactor-three theorem.
