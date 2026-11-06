# v14: large noncubic prime exponents must occur in two different factors

Date: 2026-11-06 JST.

The original equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

The right-hand side has squared **indices**. The application in this note
concerns the branch \(\ell=1,\ j=i-3\), including both \(k=r\) and
\(k=A-r\). It does not resolve the original four-variable problem.

## 1. Main result and what is new

For a solution in that branch, put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
g=\gcd(A,r^3),\quad H=A/g,\quad T=r^3/g.
\tag{1}
\]

For a positive integer m define

\[
\operatorname{cf}_3(m)=\prod_p p^{v_p(m)\bmod3},
\qquad S=\{2,3,5,7\}.
\tag{2}
\]

Thus m is uniquely a cube-free positive integer times a positive cube.
S-supported here describes the prime factors of cf3(m), **not** all prime
factors of m. Primes outside S may occur in the cube with any exponent
divisible by 3.

**Two-factor support theorem.** At least two different members of
\(n,n-1,n-2\) must have a prime outside S in their cube-free parts.
Equivalently, there are distinct d,e in {0,1,2} and distinct primes p,q>=11
such that

\[
\boxed{
v_p(n-d)\not\equiv0\pmod3,\qquad
v_q(n-e)\not\equiv0\pmod3.}
\tag{3}
\]

The primes are necessarily distinct because a prime >=11 cannot divide
two integers whose difference is 1 or 2. The theorem gives a distribution
constraint across factors, stronger than a count of primes in their product.

Its primitive-parameter consequence is

\[
\boxed{\#\{p\ge11:\ v_p(HT)\not\equiv0\pmod3\}\ge2.}
\tag{4}
\]

In particular, for **every** prime p>=11 the entire family

\[
\boxed{HT=2^a3^b5^c7^d p^e u^3,
\qquad a,b,c,d,e\ge0,\ u\ge1}
\tag{5}
\]

is excluded. There is no bound on p, u, the exponents, H, or T. This
excludes the displayed pairs (H,T); it does not exclude every T for some
fixed H. The v12 numerical condition H>=21 is unchanged.

The proof uses previously established branch conditions, a complete
Thue calculation, and exact finite arithmetic. The new calculation solves
125 coefficient equations. It reuses the complete 625-equation result
from v13. The values of the extra prime p are never enumerated.

## 2. Previously established inputs

The following necessary conditions apply to the original branch:

\[
6Hr^3=Tn(n-1)(n-2),\qquad H\mid n-2,\qquad \gcd(H,T)=1,
\tag{6}
\]

\[
n\ge104,\qquad 3n<r<10n/3,
\tag{7}
\]

and, when n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{8}
\]

The definitions, primitivity and transfer to both k branches are recorded
in [v11_effective_defect_cf.md](v11_effective_defect_cf.md), Sections 1-2,
and [v10_valuation_recovery.md](v10_valuation_recovery.md), Section 3.
The logarithmic bound is in
[v6_offset_composite.md](v6_offset_composite.md), Section 1. The same
inputs were used and listed in
[v13_uniform_cube_support.md](v13_uniform_cube_support.md), Section 2.

The new theorem is also an auxiliary result for any positive integers
n,r,H,T satisfying (6)-(8). It does not need the enormous binomial
coefficients themselves, the CF height n<2^(192H), the numerical exclusion
H<=20, or a new valuation calculation involving binom(n^2,6n-9).

## 3. Exact classification of two supported cores

First consider all integers n>=3, independently of the original equation.
We classify those for which at least two of cf3(n), cf3(n-1), cf3(n-2) are
S-supported.

### 3.1 The adjacent-pair list from v13

Let N be the complete set of m>=2 such that both cf3(m) and cf3(m-1)
are S-supported. The executed v13 computation gives

\[
\begin{split}
N=\{&2,3,4,5,6,7,8,9,10,15,16,21,25,28,36,49,50,\\
&64,81,126,225,2401,4375,6860\}.
\end{split}
\tag{9}
\]

Indeed m=alpha*x^3, m-1=beta*y^3 with coprime S-supported cube-free
coefficients, so alpha*x^3-beta*y^3=1. Every prime of S is absent or
occurs to exponent 1 or 2 in exactly one coefficient. All 5^4=625 ordered
pairs were completely solved. The saved full data are
[v13_thue_support_results.json](v13_thue_support_results.json), with
its GP input, raw output and verifier. We reuse that calculation rather
than claiming to have run the 1250 v13 solver calls again in v14.

### 3.2 Complete coverage of the three factor pairs

If some two factors have S-supported cores, the following cases exhaust
all possibilities.

| Pair with supported cores | Necessary set for n | Reason |
|---|---|---|
| n and n-1 | N | The adjacent-pair classification |
| n-1 and n-2 | N+1 | Apply the classification to m=n-1 |
| n and n-2, with n even | 2N | Divide both numbers by 2 |
| n and n-2, with n odd | M | The new odd gap-2 equations below |

In the even endpoint case, n/2 and (n-2)/2 are consecutive positive
integers. Dividing by 2 leaves every prime valuation outside S unchanged,
so both cores remain S-supported. Conversely, multiplying an adjacent
pair by 2 preserves this support condition. The ordinary binomial
symmetry is not needed for this step.

In the odd endpoint case, gcd(n,n-2)=1 and both numbers are odd. Write

\[
n=\alpha x^3,\qquad n-2=\beta y^3,\qquad
\alpha x^3-\beta y^3=2,
\tag{10}
\]

where alpha,beta are coprime cube-free integers supported on {3,5,7}
and x,y are positive odd integers. There are exactly 5^3=125 ordered
coefficient pairs. A large prime in the remaining middle factor does not
occur in these coefficients.

### 3.3 Complete gap-2 calculation

For every one of the 125 coefficient pairs the executed program called
PARI/GP 2.17.4 using

```gp
thue(thueinit(alpha*x^3-beta, 1), 2)
```

and also solved the monic equation

\[
U^3-\alpha^2\beta y^3=2\alpha^2,\qquad U=\alpha x.
\tag{11}
\]

Transformed solutions were retained exactly when alpha divides U. The
complete signed integer solution sets, after this conversion, agreed in
all 125 cases. Every returned solution was checked by exact substitution.
There were 250 solver calls and 13 signed solutions in total across the
125 direct equations. The process returned exit code 0 and empty stderr.

PARI's official documentation [P] states that `thue` returns all integer
solutions and that `thueinit` with flag 1 gives an unconditional result.
The input format permits nonmonic and reducible polynomials. No upper
bound for x,y,n was supplied. The pair (alpha,beta)=(1,1), for which the
polynomial is reducible, was included explicitly.

Positive odd x,y give exactly

\[
\boxed{M=\{3,5,7,9,27,245\}.}
\tag{12}
\]

The 125 complete records, GP input and raw outputs are saved in
[v14_gap2_results.json](v14_gap2_results.json),
[v14_gap2_results.gp](v14_gap2_results.gp),
[v14_gap2_results.stdout](v14_gap2_results.stdout), and
[v14_gap2_results.stderr](v14_gap2_results.stderr).

Two encodings share the same PARI backend. They are not independent
implementations of a complete Thue solver. Completeness depends on PARI's
documented complete algorithm and its implementation; substitution alone
cannot show that no solution was omitted. Bennett's RHS-1 uniqueness
theorem used for a separate v13 cardinality result is **not** used for
the RHS-2 calculation.

### 3.4 The 57 indices and a sharp bound of 13720

The exact set of n>=3 with two S-supported cores is

\[
\mathcal U=\bigl(N\cup(N+1)\cup2N\cup M\bigr)\cap[3,\infty).
\tag{13}
\]

The union before restricting n>=3 has 58 elements, including n=2. The
valid set has **57** elements, and its maximum is **13720**. Thus under
this particular two-core support condition there is a sharp upper bound
on n. It is a consequence of complete equations, not a chosen search
cutoff. Sharpness is witnessed by

\[
13720=5\cdot14^3,\qquad13718=2\cdot19^3.
\tag{14}
\]

Each of the 57 listed indices has its three exact cube-free cores and
the corresponding pair witnesses recorded in
[v14_pair_support_results.json](v14_pair_support_results.json).
The verifier checks the converse as well: every listed index really has
at least two S-supported cores. The example (14) satisfies this auxiliary
support condition, not the original binomial equation.

Of the 57 valid indices, 39 are below the already necessary n>=104.
The remaining 18 are exactly

\[
\begin{split}
\{&126,127,128,162,225,226,245,252,450,2401,2402,\\
&4375,4376,4802,6860,6861,8750,13720\}.
\end{split}
\tag{15}
\]

The new odd-endpoint set adds 27 and 245 to the union of the first three
families; 245 is the only additional index at or above 104.

## 4. All eighteen branch candidates are impossible

For each candidate define

\[
D=\frac{A}{\gcd(A,n-2)},\qquad
F=\prod_{p\mid D}p^{\lceil v_p(D)/3\rceil}.
\tag{16}
\]

Equation (6) says Hr^3=TA. Since H divides n-2, we obtain
A | (n-2)r^3. Cancelling gcd(A,n-2) gives D | r^3, and hence F | r.
In detail, if d0=gcd(A,n-2), the integers A/d0 and (n-2)/d0 are coprime,
so Euclid's lemma justifies the cancellation.

The smallest possible multiple of F strictly above 3n is

\[
r_0=F\left(\left\lfloor\frac{3n}{F}\right\rfloor+1\right).
\tag{17}
\]

For n>=1024 choose an integer L>0 with 3^L<n. Since e<3, log(n)>L.
Consequently (8) implies the strict rational bound

\[
r<3n+\frac{3n}{4L}.
\tag{18}
\]

The table uses the smaller of (18) and 10n/3 when applicable. Every
comparison uses exact integers after clearing denominators.

| n | F | r_0 | Required strict upper bound r < |
|---:|---:|---:|---:|
| 126 | 105 | 420 | 420 |
| 127 | 2667 | 2667 | 1270/3 |
| 128 | 508 | 508 | 1280/3 |
| 162 | 483 | 966 | 540 |
| 225 | 420 | 840 | 750 |
| 226 | 1695 | 1695 | 2260/3 |
| 245 | 4270 | 4270 | 2450/3 |
| 252 | 10542 | 10542 | 840 |
| 450 | 6735 | 6735 | 1500 |
| 2401 | 980 | 7840 | 29841/4 |
| 2402 | 58849 | 58849 | 104487/14 |
| 4375 | 1575 | 14175 | 54375/4 |
| 4376 | 191450 | 191450 | 95178/7 |
| 4802 | 235249 | 235249 | 29841/2 |
| 6860 | 1330 | 21280 | 169785/8 |
| 6861 | 160090 | 160090 | 679239/32 |
| 8750 | 1531075 | 1531075 | 433125/16 |
| 13720 | 320110 | 320110 | 169785/4 |

All 18 satisfy r_0 >= the strict upper bound, contradicting the existence
of r. At n=126 equality with 420 also contradicts the strict upper bound.
For n=245 specifically, D=29890=2*5*7^2*61 and F=4270, already larger
than 2450/3. The logarithmic bounds use L=7 or 8 and certified powers
3^7=2187 or 3^8=6561.

This rules out every n having two S-supported cores and proves (3),
subject to the stated previous inputs and the complete solver results.

## 5. Primitive H,T, and all possible extra primes at once

For p>=11 write h=v_p(H), t=v_p(T), e=v_p(r), and
m=v_p(n(n-1)(n-2)). Taking valuations in (6) gives

\[
h+3e=t+m,\qquad m\equiv h-t\pmod3.
\tag{19}
\]

Primitivity gcd(H,T)=1 implies min(h,t)=0. Therefore

\[
\boxed{m\not\equiv0\pmod3
\quad\Longleftrightarrow\quad v_p(HT)=h+t\not\equiv0\pmod3.}
\tag{20}
\]

The coprimality condition matters: without it h-t and h+t can have
different zero/nonzero status modulo 3. Since p divides at most one of
n,n-1,n-2, the two distinct primes from (3) give (4). Formula (5) has at
most one prime outside S with nonzero exponent modulo 3, so (4) excludes
it for every p and every exponent.

For clarity, let

\[
\omega_{S^c}^{(3)}(m)=\#\{p\notin S:\ 3\nmid v_p(m)\}.
\]

The new and old conclusions together are

\[
\omega_{S^c}^{(3)}(H)+\omega_{S^c}^{(3)}(T)\ge2,
\qquad \omega_{S^c}^{(3)}(T)\ge1.
\tag{21}
\]

The second inequality also follows directly from (3): at least one of
the two affected factors is n or n-1. A prime >=11 dividing it cannot
divide H, because H | n-2, so its nonzero exponent class must come from T.

Two useful consequences refine the allocation:

- If cf3(H) is S-supported, cf3(T) must contain at least two distinct
  primes >=11.
- If cf3(T) has exactly one such prime p, it must occur in n or n-1, and
  cf3(H) must contain a different such prime q in n-2.

The theorem does **not** force two large noncubic primes into T in every
case. Conversely, having two primes in HT is only a necessary condition:
placing all of them in the same consecutive factor still violates (3).

## 6. The general reduction behind the calculation

For any fixed finite prime set S containing 2 and 3, define N_S by the
complete adjacent equations alpha*x^3-beta*y^3=1 with coprime S-supported
cube-free coefficients. Define M_S by the odd equations with RHS 2 and
coefficients supported on S without 2. The exact two-supported-core set
is always

\[
\bigl(N_S\cup(N_S+1)\cup2N_S\cup M_S\bigr)\cap[3,\infty).
\tag{22}
\]

There are 5^|S| adjacent coefficient equations and 5^(|S|-1) odd
gap-2 equations. The only reducible coefficient case is (1,1), which
has no positive solution for RHS 1 or 2; all other equations are genuine
irreducible cubic Thue equations. Thus both lists are finite and
effectively computable. The number and size of prime factors in the
remaining third factor never enter these fixed coefficient sets.

This supplies a structural way to handle arbitrary additional primes.
For S={2,3,5,7}, the two complete lists and the subsequent exclusion of
all original-branch candidates were actually computed here. No new
general theorem on the uniqueness of RHS-2 Thue solutions is asserted.

## 7. Reproduction, evidence, and limits

Run in this directory with a PARI/GP executable available:

```sh
python3 v14_thue_gap_verifier.py --gp /absolute/path/to/gp --primes 3 5 7 --rhs 2 --odd-bases --output reproduced_gap2.json
python3 v14_pair_support_verifier.py --adjacent v13_thue_support_results.json --odd-gap reproduced_gap2.json --output reproduced_pairs.json
python3 v14_independent_audit.py --gap1 v13_thue_support_results.json --gap2 reproduced_gap2.json --output reproduced_audit.json
```

The first script writes the GP input and both raw output streams beside
its JSON, retaining all 125 records. The second independently enumerates
all cube-free coefficients, checks both encodings, the exact union, every
pair witness, and all 18 final exclusions. The third was separately
written and audits coefficient coverage, exact substitutions, the actual
250 flag-1 GP calls, raw stdout/JSON equality, output hashes, and the 18
interval contradictions. Both final auditors were executed using the
published filenames and returned PASS.

The saved solver source and raw gap-2 results are byte-identical copies
of the executed scratch artifacts under versioned filenames. The two
audit JSON files were regenerated with the published filenames. Hashes,
counts, provenance and prior dependencies are in
[v14_manifest.json](v14_manifest.json). The PARI executable is the same
pinned 2.17.4 installation recorded in
[v13_pari_environment.json](v13_pari_environment.json).

The mathematical cases and the primitive support transfer were also
checked by separate AI collaborators. This is not external peer review.
No new Lean execution, DeepSeek API call, or Selmer-group computation was
performed. This workspace has no available authenticated DeepSeek binding
or the prior Lean runtime; existing Lean proof bodies and fixed DeepSeek
goals were not edited. The evidence is a written reduction plus a
documented complete CAS calculation and exact finite audits, not kernel
verification of the full proof.

The remaining original-branch possibilities include large noncubic
primes in at least two consecutive factors. The new theorem supplies
neither a bound on those primes nor an upper bound on n for that
remaining family. The full four-variable equation and the existence
of any concrete solution remain unresolved.

## Reference

[P] PARI/GP official documentation, *Polynomials and power series*,
`thue` and `thueinit`. Retrieved 2026-11-06 JST.
https://pari.math.u-bordeaux.fr/dochtml/html/Polynomials_and_power_series.html#thue
