# v13: uniform cube-support descent, independent of the size of H

Date: 2026-11-06 JST. The original equation remains

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

The right-hand side has squared **indices**. This note concerns only
\(\ell=1,\ j=i-3\), including both outside branches \(k=r\) and \(k=A-r\).

## 1. Main result

For this branch put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
C=\gcd(A,r^3),\quad H=A/C,\quad T=r^3/C.
\]

Every remaining solution must satisfy

\[
\boxed{\text{There is a prime }p\ge11\text{ such that }
v_p(T)\not\equiv0\pmod3.}
\tag{V13}
\]

Equivalently, the family

\[
\boxed{T=2^a3^b5^c7^d u^3,
\qquad a,b,c,d\ge0,\quad u\ge1}
\tag{F}
\]

is excluded for **all H**, without an upper bound on H, T, u, or the four
exponents. Primes greater than 7 may occur in u; this is not an assertion
that T itself must be smooth. Removing cubes leaves one of 81 possible
cube classes, and all 81 are excluded together.

This does not exclude a particular H for every possible T. The numerical
bound H>=21 from v12 is unchanged. The full four-variable problem remains
unresolved, and this note provides no solution to the original equation.

## 2. Previously proved inputs

The necessary conditions used here are

\[
6Hr^3=Tn(n-1)(n-2),\qquad H\mid n-2,\qquad \gcd(H,T)=1,
\tag{1}
\]

\[
n\ge104,\qquad 3n<r<10n/3,
\tag{2}
\]

and, when n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{3}
\]

References in this repository:

- [v11_effective_defect_cf.md](v11_effective_defect_cf.md), Sections 1 and 2,
  for the primitive H,T and the transfer of (1)-(2).
- [v10_valuation_recovery.md](v10_valuation_recovery.md), Section 3,
  for H|n-2 and applicability to both k branches.
- [v6_offset_composite.md](v6_offset_composite.md), Section 1, for (3).

We do not use the exponential CF height n<2^(192H) or the numerical
exclusion H<=20 in the new calculation. We do not rerun those old proofs.

## 3. Uniform reduction for an arbitrary fixed prime set

Let S be a finite set of primes containing 2 and 3. Assume

\[
v_p(T)\equiv0\pmod3\qquad\text{for every prime }p\notin S.
\tag{4}
\]

Write cf3(m)=product p^(v_p(m) mod 3) for the positive cube-free part of
a positive integer m. Set

\[
\alpha=\operatorname{cf}_3(n),\qquad
\beta=\operatorname{cf}_3(n-1).
\]

**Uniform support theorem.** The integers alpha and beta are coprime,
cube-free, and all their prime factors belong to S. There are positive
integers x,y such that

\[
n=\alpha x^3,\qquad n-1=\beta y^3,\qquad
\boxed{\alpha x^3-\beta y^3=1.}
\tag{5}
\]

**Proof.** Take p outside S, so p>=5. If p divides n or n-1, it does not
divide n-2; because H|n-2, it does not divide H either. At most one of
n,n-1 is divisible by p. Taking p-adic valuations in (1) gives

\[
3v_p(r)=v_p(T)+v_p(n)+v_p(n-1).
\]

By (4), whichever of the last two terms is nonzero is a multiple of 3.
Consequently p divides neither alpha nor beta. The unique decomposition
of each positive integer into a cube-free part times a positive cube
proves (5). Coprimality follows from gcd(n,n-1)=1. QED.

Notice that neither the value of H nor an upper bound for n appears in
the resulting coefficient set.

## 4. A global bound on the number of possible n

For each p in S, its exponent pair in (alpha,beta) is exactly one of

\[
(0,0),(1,0),(2,0),(0,1),(0,2).
\]

Thus there are exactly 5^|S| ordered coefficient pairs. Each equation (5)
can be completely solved as a cubic Thue equation. If alpha=beta=1, it
has no positive solution, since distinct positive cubes differ by at
least 7. Otherwise the polynomial alpha*z^3-beta is irreducible over Q:
a rational cube beta/alpha would force both cube-free coprime numbers to
be 1.

There is also a stronger **cardinality** statement, by a theorem of
M. A. Bennett [B], Theorem 1.1: for fixed nonzero integers a,b and an
integer m>=3, |a*x^m-b*y^m|=1 has at most one positive integer pair (x,y).
Applying m=3, and pairing (alpha,beta) with (beta,alpha), gives

\[
\boxed{\#\{\text{possible first indices }n\}\le
\frac{5^{|S|}-1}{2}.}
\tag{6}
\]

Each unordered coefficient pair determines at most one n, namely the
larger of its two consecutive cube-weighted integers. The only pair
fixed by swapping is (1,1), which has no positive solution. For
S={2,3,5,7}, (6) bounds the number of n by 312 over the entire unbounded
range, not merely for one fixed n or H.

This is a consequence of an established theorem applied to this problem,
not a claim to have proved Bennett's theorem or a new general Thue theorem.
The computational proof below does not need (6): it obtains complete
solutions for all ordered coefficient pairs directly.

## 5. Complete solution of the 625 coefficient equations

For S={2,3,5,7}, the code generates all 625 pairs, including (1,1), and
executes PARI/GP 2.17.4 with

```gp
thue(thueinit(alpha*x^3-beta, 1), 1)
```

PARI's official documentation [P] states that thue returns all integer
solutions and that thueinit flag 1 certifies the computation without the
Generalized Riemann Hypothesis. Nonmonic and reducible input is allowed.
For irreducible polynomials with real roots, the documentation identifies
the Bilu-Hanrot algorithm. No user-supplied bound for n,x,y is imposed.
This is a complete-solver computation, not an extrapolation from a scan.

Every equation is also solved through the monic transformation

\[
U^3-\alpha^2\beta y^3=\alpha^2,\qquad U=\alpha x.
\tag{7}
\]

We retain the transformed solutions with alpha|U and compare the entire
signed integer solution sets. They agree for every one of the 625 pairs.
Every returned pair is re-substituted using Python integer arithmetic.
These are two encodings using the **same PARI backend**, not independent
implementations of a complete Thue solver. Completeness depends on PARI's
documented algorithm and implementation; substitution checks alone cannot
certify absence of omitted solutions.

The complete positive n list is

\[
\begin{split}
\{&2,3,4,5,6,7,8,9,10,15,16,21,25,28,36,49,50,\\
  &64,81,126,225,2401,4375,6860\}.
\end{split}
\tag{8}
\]

Of these 24 values, 19 are less than the prior cutoff 104. The five
remaining values are dealt with below. The value n=2 belongs to this
intermediate adjacent-integer calculation, not to the auxiliary cubic
problem n>=3 or the original remaining branch n>=104.

Full inputs, raw stdout, and all returned integer pairs are saved in
[v13_thue_support_results.gp](v13_thue_support_results.gp),
[v13_thue_support_results.stdout](v13_thue_support_results.stdout), and
[v13_thue_support_results.json](v13_thue_support_results.json).

## 6. Five small exact contradictions finish the infinite family

For a candidate n set

\[
D_n=\frac{A}{\gcd(A,n-2)},\qquad
F_n=\prod_{p\mid D_n}p^{\lceil v_p(D_n)/3\rceil}.
\tag{9}
\]

From H*r^3=T*A and H|n-2, we have A|(n-2)*r^3. Cancelling the gcd
implies D_n|r^3. Prime by prime this implies F_n|r.
The least admissible multiple of F_n above 3n is therefore

\[
r_{\min}=F_n\left(\left\lfloor\frac{3n}{F_n}\right\rfloor+1\right).
\tag{10}
\]

The following exact bounds contradict (2) or (3):

| n | D_n | F_n | r_min | Required strict upper bound |
|---:|---:|---:|---:|---:|
|126|2625|105|420|r<420|
|225|8400|420|840|r<750|
|2401|960400|980|7840|r<29841/4 = 7460.25|
|4375|3189375|1575|14175|r<54375/4 = 13593.75|
|6860|23526370|1330|21280|r<169785/8 = 21223.125|

The final three rational upper bounds use log(n)>7,7,8 respectively.
These follow exactly from e<3, 3^7=2187<2401,4375, and
3^8=6561<6860. All comparisons in the verifier use integer arithmetic
after clearing denominators. In particular equality at r=420 is rejected
because the upper inequality is strict.

Thus every n in (8) is excluded from the branch. This proves (V13),
subject to the stated previous inputs and the complete PARI computation.
The proof never evaluates the enormous original binomial coefficients.

## 7. Smaller support checks

The same executed calculation with S={2,3} returned n={2,3,4,9}; with
S={2,3,5}, it returned n={2,3,4,5,6,9,10,16,25,81,6860}.
These are consistency checks and earlier checkpoints. The full 625-pair
data already subsume them, so they are not required for the final theorem.

## 8. Reproduction and audit boundary

With a PARI/GP executable on the local system, run:

```sh
python3 v13_thue_support_verifier.py --gp /absolute/path/to/gp --primes 2 3 5 7 --output reproduced.json
python3 v13_branch_filter.py --input reproduced.json --output reproduced_branch_filter.json
python3 v13_encoding_audit.py --inputs reproduced.json --source v13_thue_support_verifier.py --output reproduced_encoding_audit.json
```

The first program executes 1250 solver calls: two encodings per equation.
The second program independently enumerates all 81 possible cores and
their coprime pairs, checks every returned point and all five final
contradictions. It does not independently reimplement the complete solver.
The source hashes, full output hashes and environment record are retained.

A separate AI checker audited coefficient-set coverage using an independent
enumeration, signed solutions, the monic transformation, hashes, and the
Bennett counting argument. This is not external peer review.

No new Lean execution was performed: the current workspace has neither
the saved Lean runtime nor the previous authenticated DeepSeek binding.
The existing Lean proof bodies and frozen DeepSeek goals were not changed.
This work is an unformalized mathematical reduction plus a complete CAS
calculation and exact finite verification. It is not a computation of a
3-Selmer group, a full isogeny descent, or the solution of the original
four-variable equation.

## 9. Next structural boundary

The unresolved classes contain at least one prime p>=11 in cf3(T).
The mere number or size of those primes is not bounded by this note.
Adding primes mechanically multiplies the coefficient set by 5; a further
general theorem should constrain their allocations or solve parametrized
coefficient families. The global uniqueness statement (6), together with
the exact three-factor descent in [v13_exact_three_factor_descent.md](v13_exact_three_factor_descent.md),
is available for that next step.

## References

[B] M. A. Bennett, *Rational approximation to algebraic numbers of small
height: the Diophantine equation |ax^n-by^n|=1*, J. reine angew. Math. 535
(2001), 1-49, Theorem 1.1.
https://personal.math.ubc.ca/~bennett/B-Crelle2.pdf

[P] PARI/GP official documentation, *Polynomials and power series*, thue
and thueinit. Retrieved 2026-11-06 JST.
https://pari.math.u-bordeaux.fr/dochtml/html/Polynomials_and_power_series.html#thue
