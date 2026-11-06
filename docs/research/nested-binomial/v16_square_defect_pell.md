# v16: the exact quadratic defect, a uniform Pell reduction, and delta >= 13

Date: 2026-11-06 JST.

## 1. Scope and results

The original equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

We work only in the branch ell=1, j=i-3, with both choices of k.
Put

\[
n=i,\quad A=\binom n3,\quad B=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),
\]

\[
M=\gcd(n,3)\gcd(n-1,6)\in\{1,2,3,6\},\qquad
Q=\frac{n(n-1)}M.
\]

Define the **exact quadratic defect**

\[
\boxed{\delta=\frac Q{\gcd(Q,r^2)}.}
\tag{1}
\]

It is the reduced denominator of r^2/Q. Unlike the cube-root divisor
kappa used in v15, delta discards cube factors already absorbed by r^2.
The new results are

\[
\boxed{\delta\mid r,\qquad \delta^3\mid Q,\qquad \delta\mid\kappa,}
\tag{2}
\]

\[
\boxed{\log n<28\delta,\qquad n<2^{42\delta},}
\tag{3}
\]

and, by a complete finite Pell reduction,

\[
\boxed{\delta\ge13.}
\tag{4}
\]

Thus kappa>=13 as well. More precisely, for the two coprime normalized
factors of Q, at least one of their cube-root divisors is >=5. Indeed,
two coprime positive integers both <=4 have product at most 12.
Consequently there is an integer t>=5 with t^3 dividing n or n-1.
This t need not be prime; the assertion is not that a prime >=5 must
occur to exponent at least 3.

We also give a uniform complete reduction for every fixed delta, and
an explicit polynomial bound for the number of Pell points needed
when delta is bounded. The full four-variable equation, the whole
offset-three branch, and unbounded delta remain unresolved.

## 2. Inherited branch inputs

The proof uses

\[
n\ge104,\qquad 3n<r<10n/3,\qquad Q\mid r^3,
\tag{5}
\]

and, for n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{6}
\]

These are recorded in [v6_offset_composite.md](v6_offset_composite.md)
and [v6_common_divisor.md](v6_common_divisor.md). The height calculation
below adapts the integer-separation argument in
[v15_cube_height.md](v15_cube_height.md), using the actual denominator.
It does not use a bound on the primitive defect H, a finite prime-support
classification, or the v14 complete Thue computations. The delta=1
part reproves the v15 quadratic-divisor exclusion within a slightly
smaller proved height; it does not assume that exclusion as an input.

## 3. Exact local structure and a reversible parametrization

Let alpha=v_p(Q), e=v_p(r), and d_p=v_p(delta). By (1),

\[
d_p=\max(\alpha-2e,0).
\tag{7}
\]

Because alpha<=3e, whenever d_p>0 we have d_p<=e and 3d_p<=alpha.
This proves delta|r, delta^3|Q, and delta|kappa prime by prime.

Put

\[
K=\frac{\delta r^2}{Q}=\frac{r^2}{\gcd(Q,r^2)}.
\]

The standard gcd reduction gives

\[
\boxed{K\in\mathbb Z_{>0},\qquad\gcd(K,\delta)=1.}
\tag{8}
\]

There is also the following exact description of all positive pairs
(Q,r) with Q|r^3:

\[
\boxed{Q=\delta^3 a b^2,\qquad
r=\delta a b u,\qquad
a\text{ squarefree},\quad\gcd(\delta,a u)=1.}
\tag{9}
\]

Here b and u are arbitrary positive integers subject to the displayed
conditions. In particular b may share primes with delta or a. These
a,b are not the two squarefree factors in v15's cube-remainder
decomposition; only a is required to be squarefree in (9).

To prove (9), write Q/delta^3=a b^2 using the unique squarefree/square
decomposition. At a prime dividing delta, equation (7) gives

\[
v_p(Q/\delta^3)=\alpha-3(\alpha-2e)
=2(e-d_p),
\]

so that prime does not divide a. Its exponent in delta*b is exactly e.
At a prime not dividing delta, alpha<=2e, hence the exponent in a*b
is ceil(alpha/2)<=e. Thus delta*a*b divides r and u is an integer;
the exact exponents at primes dividing delta show gcd(delta,u)=1.

Conversely, (9) gives

\[
\frac{r^3}{Q}=a^2 b u^3\in\mathbb Z,
\quad
\gcd(Q,r^2)=\delta^2 a b^2\gcd(\delta,a u^2)
=\delta^2 a b^2.
\]

Consequently (1) holds exactly, and K=a u^2. This proves both directions.

In particular the height bound in (3) can be much stronger than
log(n)<28*kappa. Extra cube factors absorbed by r^2 cannot be counted
toward delta.

### Connection to the original primitive defect H

Let H=A/gcd(A,r^3), the primitive defect from the earlier analysis.
The new denominator satisfies

\[
\boxed{\gcd(\delta,H)=1,\qquad \delta^3\mid A/H.}
\tag{9a}
\]

Indeed, every prime p dividing delta satisfies v_p(A)=v_p(Q):

- For p>=5, p divides n or n-1, so it does not divide n-2; the
  denominators 6 and M are p-units, giving equality.
- For p=3, divisibility of Q forces p to divide n or n-1. Both A
  and Q remove exactly one factor 3 from n(n-1), and n-2 is a 3-unit.
- For p=2 and n odd, both A and Q have exponent v_2(n-1)-1.
- For p=2 and n even, M is odd. Since p divides delta and delta^3|Q,
  we have v_2(n)=v_2(Q)>=3, hence v_2(n-2)=1. Dividing A by 6
  therefore leaves v_2(A)=v_2(n)=v_2(Q).

By Q|r^3, these equal exponents are fully absorbed by gcd(A,r^3),
so p does not divide H. This proves gcd(delta,H)=1. Equations (2)
and the same equality of exponents show delta^3 divides both A and
r^3, hence divides gcd(A,r^3)=A/H. This bridge does not impose a
new upper bound on H or prove that all remaining pairs (delta,H)
are impossible.

## 4. Height controlled by the actual denominator

The lower bound on r gives

\[
K=M\delta\frac{r^2}{n(n-1)}>9M\delta.
\tag{10}
\]

Suppose log(n)>=28*delta. Since e>2 and delta>=1,

\[
n\ge e^{28\delta}>2^{28\delta}>8192\delta+1.
\]

In particular (6) applies. Put eta=3/(4 log(n))<=3/(112 delta).
Exactly as in v15,

\[
\begin{aligned}
K-9M\delta
&<M\delta(6\eta+\eta^2)
+\frac{M\delta}{n-1}(9+6\eta+\eta^2)\\
&<6\left(\frac9{56}+\frac9{12544}\right)
+\frac6{8192}\left(9+\frac9{56}+\frac9{12544}\right)\\
&=\frac{50111163}{51380224}<1.
\end{aligned}
\tag{11}
\]

This contradicts K and 9M*delta being integers, proving log(n)<28*delta.
The elementary inequality e^2<8 then yields n<2^(42*delta).
The positive integer K-9M*delta is also coprime to delta by (8).
No extra lower gap is claimed merely from this coprimality.

## 5. A complete Pell reduction for every fixed delta

Set C=M*delta. Equations (5) and (8) give

\[
\boxed{C r^2=K n(n-1),\qquad
\gcd(K,\delta)=1,\qquad
9C<K<\frac{10400C}{927}.}
\tag{12}
\]

The final inequality uses r<10n/3 and n/(n-1)<=104/103.
It is strict. Thus the last possible integer K is
floor((10400*C-1)/927), while the first is 9*C+1.

For each allowed triple (delta,M,K), write

\[
CK=s^2 d,\qquad d\text{ positive and squarefree}.
\]

With x=2n-1, multiplying (12) by 4C gives

\[
(2Cr)^2=s^2d(x^2-1).
\]

Since s^2 divides the left square, s|2Cr. Squarefreeness of d then
implies d|(2Cr/s). Hence

\[
\boxed{x^2-dy^2=1,\qquad
n=\frac{x+1}{2},\qquad r=\frac{sdy}{2C}.}
\tag{13}
\]

All reconstructions are checked for integer n,r, the actual M and delta,
cube divisibility, and the original interval conditions. If d=1,
(x-y)(x+y)=1 has no positive-y integer solution and that family is empty.

### Certifying the fundamental units

Every positive Pell solution satisfies gcd(x,y)=1 and

\[
0<\frac xy-\sqrt d
=\frac1{y^2(x/y+\sqrt d)}<\frac1{2y^2}.
\tag{14}
\]

Legendre's convergent criterion therefore applies: x/y is a convergent
of the ordinary continued fraction of sqrt(d). The exact theorem is
documented as `Real.exists_rat_eq_convergent` in the official
[mathlib DiophantineApproximation documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/Basic.html).
This use of 1/2 is justified by the new exact Pell identity (14).
It does not substitute 1/2 for the separate 3/2 approximation constant
in the older cubic-curve analysis.

The certificate records every partial quotient through the first
norm-one convergent, and the norm of every such convergent. These
sequences encode all earlier numerators and denominators without loss
through their usual recurrence. Each quotient is certified by integer
inequalities for the corresponding quadratic surd. Every earlier norm
is checked to differ from 1. Convergent denominators do not decrease
and strictly increase after the initial possible equality, so the first
norm-one convergent has minimal positive y among all Pell solutions.

### Why powers exhaust the positive solutions

Let epsilon=u+v*sqrt(d)>1 denote the certified minimal positive unit.
For any positive solution eta=x+y*sqrt(d), choose k>=0 with
epsilon^k<=eta<epsilon^(k+1). The quotient eta/epsilon^k has integer
coefficients, since epsilon^(-1)=u-v*sqrt(d), and norm 1. It lies in
[1,epsilon). If larger than 1, its positive sqrt(d)-coefficient would
be smaller than v, contradicting minimality. Thus eta=epsilon^k.

For reference, the corresponding general theorem is
`Pell.IsFundamental.eq_pow_of_nonneg` in the official
[mathlib Pell documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Pell.html).
These are references to established mathematics, not a new Lean run.

Thus the recurrence

\[
x_{k+1}=u x_k+d v y_k,\qquad y_{k+1}=v x_k+u y_k
\tag{15}
\]

generates every positive solution. Both coordinates strictly increase.
The first point with x>=2^(42*delta+1)-1 certifies completion of the
height range n<2^(42*delta).

## 6. A general candidate bound in the defect parameter

For a fixed M, the open coefficient interval in (12) contains fewer
than (2057/927)*M*delta integers. Summing M=1,2,3,6 gives fewer than
(8228/309)*delta<27*delta coefficient families, even before imposing
gcd(K,delta)=1. Hence there are at most 27*delta-1 families.

Every positive norm-one unit has
epsilon>=2+sqrt(3)>2^(3/2). If its k-th power satisfies the height,

\[
2^{3k/2}<\epsilon^k=x_k+\sqrt{x_k^2-1}
<2x_k<2^{42\delta+2}.
\]

Thus 3k<84*delta+4 and k<=28*delta+1. Consequently, for each fixed
delta, there are at most

\[
\boxed{(27\delta-1)(28\delta+1)}
\tag{16}
\]

Pell points to reconstruct. For all 1<=delta<=D together the count is
at most

\[
\boxed{126D(D+1)(2D+1)-\frac{D(D+1)}2-D.}
\tag{17}
\]

This is a bound on candidate points, not a claim that all of them occur
or satisfy the original equation. It makes the bounded-defect reduction
uniform in the original index n and all its prime factors. It is not a
bound on the arithmetic bit complexity of finding fundamental units,
nor a bound on unbounded delta.

## 7. Executed complete exclusion for delta=1,...,12

The executed certificate has the following exact totals.

| Stage | Count |
|---|---:|
| Coefficient triples (delta,M,K) | 1,223 |
| Square-discriminant families, with no positive Pell point | 8 |
| Distinct nonsquare radicands | 570 |
| All Pell points below the proved rational height | 34,010 |
| Integer n,r after reconstruction | 24,114 |
| n>=104 | 23,920 |
| Actual M and delta match | 9,324 |
| Q divides r^3 | 1,929 |
| Strict coarse interval | 1,762 |
| Strict rational logarithmic interval | 123 |
| Both original k branches | 246 |
| Branches excluded by an exact modular witness | 246 |
| Survivors | 0 |

The counts by exact defect are:

| delta | Coefficient triples | Final n,r pairs | Original branches excluded |
|---:|---:|---:|---:|
| 1 | 25 | 11 | 22 |
| 2 | 26 | 8 | 16 |
| 3 | 52 | 23 | 46 |
| 4 | 53 | 5 | 10 |
| 5 | 107 | 10 | 20 |
| 6 | 54 | 12 | 24 |
| 7 | 160 | 7 | 14 |
| 8 | 107 | 4 | 8 |
| 9 | 159 | 20 | 40 |
| 10 | 107 | 5 | 10 |
| 11 | 266 | 7 | 14 |
| 12 | 107 | 11 | 22 |

For n>=1024, an integer J with 3^J<n gives log(n)>J, since e<3.
The strict rational necessary bound r<3n+3n/(4J) is then checked by
integer cross-multiplication. The binomial witnesses use Lucas' formula,
which follows by expanding (1+t)^N modulo p using (1+t)^p=1+t^p.
No enormous binomial integer is constructed.

All 246 witnesses use primes at most 23. In 242 of them both binomials
vanish modulo p and k^2 does not. The four exceptions are equally direct
contradictions; their residues (left,B,k^2,right) are:

| delta | n | r | Branch | p | Residues |
|---:|---:|---:|---|---:|---|
| 2 | 5329 | 16206 | k=r | 5 | (0,3,1,4) |
| 2 | 5329 | 16206 | k=A-r | 5 | (0,3,4,2) |
| 3 | 9801 | 30030 | k=r | 13 | (6,0,0,0) |
| 3 | 9801 | 30030 | k=A-r | 13 | (6,0,1,1) |

The largest candidate n has 150 decimal digits. These are candidates in
a rational necessary superset, not solutions of the original equation.
For delta=1 the final 11 pairs agree exactly with the v15 certificate,
including the control (169,546). The earlier v15 initial count was 188
Pell points under 2^45; this calculation has 181 for delta=1 under the
newly proved smaller bound 2^42. The identical final candidate set is
checked explicitly; the differing initial heights must not be conflated.

This proves (4) from the inherited inputs, the displayed mathematical
reduction, and the exact finite certificate. A separately written
[auditor](v16_square_defect_independent_audit.py) was executed and
reconstructed all coefficient triples, minimal units, recurrence points,
disposition strings, endpoint records, and original-index modular
witnesses. All counts agree, including the four nonvanishing-pattern
exceptions. See the [audit report](v16_square_defect_independent_audit.json)
and [verification scope](v16_square_defect_independent_audit_note.md).

## 8. Files and reproduction

From the research directory:

```sh
python3 v16_square_defect_pell.py --limit 12 --output reproduced_v16_square_defect.json --v15-certificate v15_pell_square_divisor_results.json
python3 v16_square_defect_independent_audit.py --input reproduced_v16_square_defect.json --generator v16_square_defect_pell.py --v15 v15_pell_square_divisor_results.json --output reproduced_v16_pell_audit.json
```

The source is [v16_square_defect_pell.py](v16_square_defect_pell.py).
The full output is stored losslessly as
[v16_square_defect_pell_results.json.gz](v16_square_defect_pell_results.json.gz).
The [readable summary](v16_square_defect_pell_summary.json) records both
the compressed and uncompressed sizes and SHA-256 hashes. To audit the
saved output directly, decompress it with `gzip -dc` to
`reproduced_v16_square_defect.json`, then run the second command above.
It includes:

- All 570 exact continued-fraction quotient and norm sequences through
  the first norm-one solution; the maximum sequence length is 70.
- All 1,223 family records, their first omitted point, and a disposition
  character for every Pell point. The characters encode why each point
  is rejected or identify the retained modular-witness stage.
- All 123 final candidate pairs and all 246 original-equation witnesses.
- Source and v15 control-certificate hashes, counts and the empty
  surviving set.

The Python computation uses only standard-library exact integer
arithmetic. The generic height, Legendre criterion and unit-descent
arguments are mathematical prerequisites to interpreting the finite
certificate as complete. No new Lean execution, DeepSeek API call,
complete CAS solver, Selmer calculation or external peer review is
claimed here. Existing formal proof bodies and fixed goals are unchanged.
