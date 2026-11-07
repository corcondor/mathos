# v15: a genuine cube divisor is necessary in the adjacent factors

Date: 2026-11-06 JST.

## 1. Statement and scope

The original equation has squared indices:

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns the existing branch \(\ell=1,\ j=i-3\), including
both outer choices of k. Write

\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),
\]

\[
g=\gcd(n,3),\quad d_0=\gcd(n-1,6),\quad
M=gd_0,\quad Q=\frac n g\frac{n-1}{d_0}.
\tag{1}
\]

**New necessary condition.** Every solution in this branch satisfies

\[
\boxed{Q\nmid r^2.}
\tag{2}
\]

The established input \(Q\mid r^3\) therefore implies the stronger local
description

\[
\boxed{\exists p\text{ prime}:\quad
2v_p(r)<v_p(Q)\le3v_p(r).}
\tag{3}
\]

In particular, some prime has

\[
\boxed{v_p(Q)=3\quad\text{or}\quad v_p(Q)\ge5.}
\tag{4}
\]

Thus every Q whose prime exponents belong to \(\{0,1,2,4\}\) is excluded.
This includes every cube-free Q. It follows in particular that n and n-1
cannot both be cube-free: **a prime cube must divide n or n-1**.

The proof is a uniform reduction to 25 ordinary Pell families, a proven
height bound, and exact finite checks against the original equation.
It neither extends a chosen support set nor enumerates large primes.
It does not solve the unrestricted original equation or the remaining
branch cases.

## 2. Previously established inputs

The proof uses only

\[
n\ge104,\qquad 3n<r<10n/3,
\tag{5}
\]

and, when \(n\ge1024\),

\[
r<3n+\frac{3n}{4\log n}.
\tag{6}
\]

The cube-divisibility input \(Q\mid r^3\), from
`v6_common_divisor.md`, is needed only for the consequences (3)-(4).
The inequality (6), \(\mathrm e<3\), and \(\mathrm e^2<8\) are established
in the existing v6 analysis and subsequent height reductions.

The finite exclusion of (2) does not use H<=20 certificates, a bound on
H, a v14 Thue calculation, factorization of the enormous binomial X,
or any rank/Selmer computation. It is a separate restriction on the
remaining branch after v14.

## 3. An integer coefficient creates a height bound

Assume for a contradiction that \(Q\mid r^2\), and put

\[
L=r^2/Q\in\mathbb Z_{>0}.
\]

Since gcd(n,n-1)=1, the factors g and d_0 in (1) are coprime and

\[
M\in\{1,2,3,6\},\qquad
\boxed{Mr^2=Ln(n-1).}
\tag{7}
\]

The strict lower bound in (5) gives

\[
\frac LM=\frac{r^2}{n(n-1)}>\frac{9n}{n-1}>9,
\]

so L>=9M+1. In particular, L/M>=55/6 for all four M.

If n>=1024 and log(n)>=30, (6) yields

\[
\left(\frac rn\right)^2<
\left(3+\frac3{4\cdot30}\right)^2=
\left(\frac{121}{40}\right)^2.
\]

But (7) gives

\[
\left(\frac rn\right)^2
=\frac LM\left(1-\frac1n\right)
\ge\frac{55}{6}\frac{1023}{1024}.
\]

The difference between this last lower bound and (121/40)^2 is exactly
363/51200>0, a contradiction. Thus n>=1024 implies log(n)<30.
The smaller n are already below the resulting bound. Since e^2<8,

\[
\boxed{n<\mathrm e^{30}<2^{45}=35184372088832.}
\tag{8}
\]

This is a consequence of Q|r^2, not an experimental search cutoff.

The upper inequality in (5), together with n>=104, gives

\[
\frac LM<\frac{100}{9}\frac n{n-1}
\le\frac{10400}{927}.
\]

Consequently all possible pairs are exactly contained in these ranges:

| M | Possible L |
|---:|---|
| 1 | 10, 11 |
| 2 | 19, 20, 21, 22 |
| 3 | 28, 29, 30, 31, 32, 33 |
| 6 | 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67 |

There are 25 pairs. They are a covering list; some pairs need not
actually occur for a valid n and r.

## 4. Ordinary Pell equations cover every candidate

For each pair (M,L), write

\[
ML=s^2d,\qquad d\text{ positive and square-free}.
\]

Set x=2n-1. Equation (7) becomes

\[
(2Mr)^2=s^2d(x^2-1).
\]

First s divides 2Mr, because s^2 divides its square. Put v=2Mr/s.
Then v^2=d(x^2-1). Square-freeness of d implies d|v. Therefore

\[
\boxed{x^2-dy^2=1,\qquad y=\frac{2Mr}{sd}\in\mathbb Z_{>0}.}
\tag{9}
\]

The inverse formulas are

\[
\boxed{n=\frac{x+1}{2},\qquad r=\frac{sdy}{2M}.}
\tag{10}
\]

Thus oddness of x and divisibility 2M|sdy are checked when reconstructing
the indices. The actual value gcd(n,3)gcd(n-1,6)=M must also be checked.
If d=1, the equation (x-y)(x+y)=1 has only x=1,y=0 in nonnegative
integers, hence no candidate. All actual 25 pairs here have d>1.

There are 13 distinct d values. Their least positive Pell solutions are:

| d | Fundamental x | Fundamental y |
|---:|---:|---:|
| 6 | 5 | 2 |
| 10 | 19 | 6 |
| 11 | 10 | 3 |
| 21 | 55 | 12 |
| 38 | 37 | 6 |
| 42 | 13 | 2 |
| 87 | 28 | 3 |
| 93 | 12151 | 1260 |
| 330 | 109 | 6 |
| 354 | 258065 | 13716 |
| 366 | 907925 | 47458 |
| 390 | 79 | 4 |
| 402 | 401 | 20 |

The generator certifies minimality directly: for every integer y from
1 through the reported y, it uses integer square root to check whether
1+d*y^2 is a square, and stops at the first one. The largest such check
ends at y=47458. No complete CAS solver or continued-fraction completeness
claim is needed for these fundamental solutions.

### Why the recurrence is complete

Let epsilon=u+v*sqrt(d)>1 be the least positive solution in the table.
Any other positive solution eta=x+y*sqrt(d) has norm 1. Choose k>=0
such that epsilon^k<=eta<epsilon^(k+1). The quotient eta/epsilon^k
still has integer coefficients, because epsilon^(-1)=u-v*sqrt(d).
Its norm is 1 and it lies in [1,epsilon). If it were strictly larger
than 1, its integer sqrt(d)-coefficient would be positive and smaller
than v, contradicting the checked minimality of v. Thus the quotient
is 1 and eta=epsilon^k.

All positive solutions are therefore generated by

\[
x_{k+1}=u x_k+d v y_k,\qquad
y_{k+1}=v x_k+u y_k.
\tag{11}
\]

Both coordinates strictly increase. The height (8) is equivalent to
x<2^46-1, so the first point at or beyond that threshold certifies the
end of each finite list. The norm identities, complete recurrences,
reconstruction conditions, and first excluded point are all recorded.

## 5. Exact finite exclusion

The executed generator finds these counts:

| Stage | Count |
|---|---:|
| Pell points below the proven height, summed over 25 pairs | 188 |
| Integer n,r under (10) | 160 |
| n>=104 | 140 |
| Actual M matches the coefficient M | 66 |
| Strict interval 3n<r<10n/3 | 62 |
| Still allowed by the rational logarithmic upper bound | 11 |
| Original branch equations, both k choices | 22 |
| Surviving original equations | 0 |

For the logarithmic comparisons choose an integer J with 3^J<n.
Since e<3, log(n)>J and (6) gives the strict rational bound
r<3n+3n/(4J). All comparisons are made by integer cross-multiplication.
No floating-point logarithms are used.

The eleven remaining pairs and the witness primes are:

| n | r | Prime for k=r | Prime for k=A-r |
|---:|---:|---:|---:|
| 169 | 546 | 5 | 3 |
| 243 | 792 | 5 | 2 |
| 361 | 1140 | 7 | 7 |
| 784 | 2436 | 5 | 5 |
| 1369 | 4218 | 5 | 5 |
| 3025 | 9240 | 13 | 13 |
| 11881 | 35970 | 7 | 7 |
| 332668 | 1016316 | 5 | 11 |
| 2589895 | 7841295 | 2 | 13 |
| 564585121 | 1709366340 | 7 | 7 |
| 123076966375 | 372634020825 | 2 | 7 |

For every one of these 22 witnesses, the original equation fails in the
particularly simple way

\[
\binom Ar\equiv X\equiv0\pmod p,
\qquad k^2\not\equiv0\pmod p.
\tag{12}
\]

The symmetry binom(A,k)=binom(A,r) applies to both k choices. For each
zero in (12), the JSON records a single base-p digit where the lower
binomial index has a larger digit than the upper index. Lucas' formula
then makes that binomial coefficient zero modulo p. Lucas' formula itself
follows by expanding (1+t)^N modulo p, using (1+t)^p=1+t^p, and comparing
base-p digit coefficients. Thus each witness can be checked from two
digit inequalities and p not dividing k; huge binomial integers are
never constructed.

The pair (n,r)=(169,546) is deliberately retained as a control. It has
M=6, L=63, Q=4732 and passes the coarse necessary bounds. The original
equation, rather than a mistaken removal by those bounds, excludes it
in both branches. Likewise n=243 has Q=9801=3^4*11^2, illustrating why
the result is stronger than just the cube-free-Q case.

This completes the finite contradiction under Q|r^2 and proves (2),
subject to the stated existing branch inputs and verification boundary.

## 6. Exact prime-exponent consequences and the primes 2 and 3

Combine Q not dividing r^2 with Q dividing r^3. At some prime p,
letting alpha=v_p(Q) and e=v_p(r), we have 2e<alpha<=3e.
Necessarily e>=1. If e=1 then alpha=3. If e>=2 then alpha>=5.
This proves (3)-(4); alpha=4 cannot witness the failure of Q|r^2.

The adjacent factors n and n-1 are coprime, so a cube dividing Q comes
from only one of them. The cancellation in the definition of Q must
not be omitted:

| Prime and location | Its exponent in Q |
|---|---|
| p>=5, dividing either n or n-1 | Its full exponent in that factor |
| p=2, n even | v_2(n) |
| p=2, n odd | v_2(n-1)-1 |
| p=3, dividing n | v_3(n)-1 |
| p=3, dividing n-1 | v_3(n-1)-1 |
| p=3, n=2 mod 3 | 0 |

For example, a witness at p=3 forces an exponent 4 or at least 6 in n
or n-1. A witness at p=2 on the n-1 side has the same shifted condition.
The broad conclusion that a prime cube divides n or n-1 is always valid.
The stronger exclusion is precisely that all exponents of Q cannot lie
in {0,1,2,4}; one should not substitute the exponents of n(n-1) without
accounting for the displayed cancellations.

The result combines with v14: at least two different factors among
n,n-1,n-2 must contain large primes with exponents nonzero modulo 3,
and independently Q must have the exponent obstruction (3). The prime
in (3) can be 2 or 3, or one of the v14 primes. No additional count of
distinct large primes is asserted.

## 7. Files, reproduction, and verification boundary

Run:

```sh
python3 v15_pell_square_divisor.py --output reproduced_pell.json
python3 v15_pell_independent_audit.py --input reproduced_pell.json --generator v15_pell_square_divisor.py --output reproduced_pell_audit.json
```

The executed source and output are `v15_pell_square_divisor.py` and
`v15_pell_square_divisor_results.json`. The output contains source hash,
all fundamental solutions, all 25 complete recurrence lists, endpoint
certificates, every candidate disposition, and the 22 modular witnesses.

The finite algorithm uses only Python standard-library exact integer
and rational arithmetic. A separately written auditor was executed and
returned PASS: [v15_pell_independent_audit.py](v15_pell_independent_audit.py)
and [its JSON report](v15_pell_independent_audit.json).
It computes the fundamental units by continued fractions and
also checks their minimality directly, generates the points by a
second-order recurrence, reconstructs all 25 families and 66 candidates,
and verifies every modular witness using factorial-table Lucas digits
at the actual k and the original squared index (n-3)^2. It separately
validates the single-digit zero certificates. The source/result hashes,
all counts, no survivors, and maximum witness prime 13 agree.

The elementary written reduction was also reviewed independently by
another AI collaborator. No new Lean run, DeepSeek call, external CAS
complete-solving claim, or modification of existing formal proof bodies
is made. These are written proofs and independently implemented exact
finite checks, not external peer review or kernel verification.
