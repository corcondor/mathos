# Prime first upper index in the large-gap lower branch

We retain the squared-index equation and the notation

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2},
\qquad \binom AB=X+Y.
\]

This note concerns the lower branch with \(j>\ell\) and
\(B\ge3j\). The previous complete certificate excludes
\(M=j\le20\), so only \(j\ge21\) need be considered here.
For \(j\ge100\), the structural reduction in Section 6 of
`lower_branch_reduction.md` says that a solution must have
\(i-j\in\{2,3\}\). Section 7 of that same note proves
the necessary bands
\(i-j=2\Rightarrow B\ge4j+5\) and
\(i-j=3\Rightarrow3j<B<4j\).
These reductions are prerequisites, not proved again here.

The proved gap bounds give \(B<10j\) in general and \(B<5j\)
when \(j\ge800\). Also \(1\le\ell\le k-2\).

## Theorem

There is no solution in the lower branch with

\[
\boxed{j>\ell,\qquad B\ge3j,\qquad i\text{ prime}.}
\]

Equivalently, every solution in the specified branch must have
composite first upper index \(i\).

The analytic argument in Sections 1--4 excludes all primes
\(i=p\ge2^{14}=16384\). It also excludes \(\ell=1\) for every
prime \(p\) with \(j=p-d\ge100\), without the threshold 16384.
Section 5 records an exact modular certificate for the remaining
finite interval of primes when \(j\ge100\). Section 6 treats
\(21\le j\le99\) using the cubic height, including every offset
\(i-j\ge2\). Both finite candidate sets are independently
enumerated and verified.

## 1. The elementary congruences

Because \(1\le j<p\),

\[
A=pa,\qquad
a\equiv
\begin{cases}
-1/2&d=2,\\
1/3&d=3
\end{cases}\pmod p.
\tag{1}
\]

Also \(X=\binom{p^2}{j^2}\equiv0\pmod p\), since
\(p\nmid j\). All uses of Lucas's congruence below follow by
comparing coefficients in \((1+z)^p\equiv1+z^p\pmod p\).

### The entire case ell=1

Here \(B=k\) and \(Y=B^2\). If \(p\nmid B\), Lucas gives
\(\binom AB\equiv0\pmod p\), while \(X+Y\not\equiv0\).

If \(p\mid B\), write \(B=mp\). From \(B<10j<10p\)
we have \(1\le m\le9\). The least nonnegative residue \(a_0\)
of \(a\) in (1) is \((p-1)/2\) when \(d=2\); when \(d=3\),
it is the inverse of 3, at least \((p+1)/3\). Since \(p\ge103\),
in both cases \(9<a_0<p\). Thus

\[
\binom A{mp}\equiv\binom{a_0}m\not\equiv0\pmod p,
\]

whereas \(X+Y\equiv0\). This excludes \(\ell=1\) throughout
the claimed range.

## 2. Effective second lower index at least three

Now assume \(p\ge16384\), so \(B<5j<5p\), and put
\(e=\min(\ell,k-\ell)\). If \(e\ge3\), then

\[
B\ge\binom k3=\frac{k(k-1)(k-2)}6.
\]

We claim \(k^2<p\). Otherwise \(k\ge\sqrt p\ge128\),
and \((k-1)(k-2)>k^2/2\), so

\[
B>k^3/12\ge(128/12)p>5p,
\]

a contradiction. Thus \(k^2<p\). Every prime factor of
\(B=\binom{k}{\ell}\) is at most \(k<p\), and
\(Y=\binom{k^2}{\ell^2}\not\equiv0\pmod p\), since all its
factorials have arguments less than \(p\). Again Lucas gives
\(\binom AB\equiv0\pmod p\), contradicting \(X+Y\not\equiv0\).

## 3. Effective second lower index two: quantization from Lucas

Only \(e=2\) remains, so

\[
B=\binom k2,\qquad \ell\in\{2,k-2\}.
\]

The bound \(B<5p\) implies

\[
k<\sqrt{10p}+1,\qquad k^2<11p<p^2.
\tag{2}
\]

In particular \(k<p\), so \(p\nmid B\). Consequently
\(Y\equiv0\pmod p\). Write

\[
k^2=mp+s,\qquad 0\le s<p.
\]

If \(\ell=2\), use \(Y=\binom{k^2}4\). If \(\ell=k-2\),
use \(Y=\binom{k^2}{4k-4}\). In either case the lower argument
\(q\) is less than \(p\), by (2), so Lucas says that \(Y\equiv0\)
requires \(s<q\). Therefore

\[
0\le s<4k,
\qquad B=\frac{mp}{2}+\frac{s-k}{2}.
\]

Since \(p\ge16384\), (2) gives
\(3k/2<5\sqrt p\) and \(k/2<2\sqrt p\). We obtain

\[
\boxed{\frac{mp}{2}-2\sqrt p<B<\frac{mp}{2}+5\sqrt p.}
\tag{3}
\]

This locates \(B\) in narrow intervals around half-integer multiples
of \(p\). The actual magnitude required by the equation lies between
two of those intervals, as proved next.

We will also use \(Y<X\). Indeed, the lower argument \(q\) just
chosen is less than \(p\), while

\[
X=\binom{p^2}{q_d},\qquad
q_2=4p-4,\quad q_3=6p-9,
\]

and \(q<q_d<p^2/2\). Increasing the upper argument from
\(k^2<p^2\), followed by unimodality in the lower argument, gives
\(Y<X\).

## 4. Explicit size comparisons, with errors

For real \(x>0\), write

\[
F_N(x)=x(\log(N/x)+1).
\]

For integers \(1\le u<N\), the product formula and the standard
Stirling bounds give

\[
\log\binom Nu\le F_N(u),
\]

\[
\log\binom Nu\ge F_N(u)-\tfrac12\log(2\pi u)
-\frac1{12u}-\frac{u(u-1)}{2(N-u+1)}.
\tag{4}
\]

For the product term in the second inequality, use
\(\log(1-z)\ge-z/(1-z)\). No asymptotic error is omitted.
In what follows \(L=\binom AB\), and all bounds apply for
\(p\ge16384\).

### Case d=2, m at most 8

By (3), \(B<4p+5\sqrt p\). Since
\(A=p(p-1)/2<p^2/2\), concavity of \(F_{p^2/2}\) yields

\[
\log L\le4p(\log(p/8)+1)+5\sqrt p\log p.
\]

On the other hand, applying (4) to \(X\), and using
\(q_2=4p-4\), gives

\[
\log X\ge4p(\log(p/4)+1)-5\log p-12.
\]

For clarity, the losses are bounded by \(4\log p\) from replacing
\(q_2\) by \(4p\), less than \(\tfrac12\log p+2\) from the
square-root factor, less than 1 from the Stirling remainder, and less
than 9 from the product term. Hence

\[
\log X-\log L>
g_2(p):=\frac83p-5\sqrt p\log p-5\log p-12>0.
\tag{5}
\]

Here we used \(\log2>2/3\). Thus \(L<X\), impossible.

### Case d=2, m at least 9

Now \(B>(9/2)p-2\sqrt p=:b_0\). Formula (4), the bound
\(B<5p\), and \(A=(p^2/2)(1-1/p)\) give the first inequality
below. For the second, integrate
\(F'_{p^2/2}(x)=\log((p^2/2)/x)<\log p\) over
\(b_0\le x\le(9/2)p\):

\[
\log L\ge F_{p^2/2}(b_0)-\log p-35
\ge\frac92p(\log(p/9)+1)-2\sqrt p\log p-\log p-35.
\]

The first constant 35 allows less than 26 for the product term,
less than \(\tfrac12\log p+3\) for the factorial terms, and less
than 6 for replacing \(A\) by \(p^2/2\).
Also \(\log X\le4p(\log(p/4)+1)\). Since
\(9\log3-8\log2-1/2<9/2\), we get

\[
\log L-\log X>
h_2(p):=\tfrac12p\log p-\tfrac92p
-2\sqrt p\log p-\log p-35>1.
\tag{6}
\]

Thus \(L>eX>2X>X+Y\), impossible.

### Case d=3, m at most 6

Here \(B<3p+5\sqrt p\) and \(A<p^3/6\). Consequently

\[
\log L\le3p(\log(p^2/18)+1)+10\sqrt p\log p.
\]

Applying (4) to \(q_3=6p-9\), with product loss less than 20,
gives

\[
\log X\ge6p(\log(p/6)+1)-10\log p-23.
\]

Subtracting, and using \(\log2<7/10\),

\[
\log X-\log L>
g_3(p):=\tfrac9{10}p-10\sqrt p\log p-10\log p-23>0.
\tag{7}
\]

Again \(L<X\).

### Case d=3, m at least 7

Now \(B>(7/2)p-2\sqrt p=:b_0\), and
\(A=(p^3/6)(1-1/p)(1-2/p)\). Apply (4), then integrate
\(F'_{p^3/6}(x)<2\log p\) over
\(b_0\le x\le(7/2)p\), to obtain

\[
\log L\ge F_{p^3/6}(b_0)-\log p-20
\ge\frac72p(\log(p^2/21)+1)
-4\sqrt p\log p-\log p-20.
\]

The product loss is less than 1, the factorial losses are less than
\(\tfrac12\log p+3\), and replacing \(A\) by \(p^3/6\)
loses less than 16.
Also \(\log X\le6p(\log(p/6)+1)\). The elementary bound
\(5/2-6\log6+(7/2)\log21<5\) therefore gives

\[
\log L-\log X>
h_3(p):=p\log p-5p-4\sqrt p\log p-\log p-20>1.
\tag{8}
\]

Thus \(L>2X>X+Y\).

### Verification of the four signs on the entire range

Put \(P=2^{14}\). The elementary estimates
\(2/3<\log2<7/10\) give

\[
\frac{28}{3}<\log P<\frac{49}{5},\qquad\sqrt P=128.
\]

Substitution in the four displayed functions gives the strict bounds

\[
g_2(P)>\frac{112073}{3},\quad
g_3(P)>\frac{10403}{5},\quad
h_2(P)>\frac{2656}{15},\quad
h_3(P)>\frac{989249}{15}.
\]

Their derivatives are positive for \(p\ge P\). This follows by
differentiation, using that \((\log p+2)/\sqrt p\) decreases for
\(p>1\), while \(\log p\) increases. At \(P\), suitable lower
bounds on the four derivatives are respectively

\[
\frac83-\frac{59}{256}-\frac5P,
\quad \frac9{10}-\frac{59}{128}-\frac{10}{P},
\quad \frac23-\frac{59}{640}-\frac1P,
\quad \frac{16}{3}-\frac{59}{320}-\frac1P,
\]

all positive. Thus (5)--(8) hold for all larger real \(p\), in
particular for all primes in the theorem.

The elementary logarithm constants used above require no numerical
approximation: \(\log2>2/3\) follows by convexity of \(1/x\)
on \([1,2]\); \(\log2<7/10\) and \(\log3<11/10\) follow
from finite lower partial sums of the exponential series. These also
give the deliberately loose constants in (6) and (8).

## 5. Exact certificate for the remaining primes when j is at least 100

The remaining primes satisfy \(103\le p<16384\), with
\(j=p-d\ge100\), \(d\in\{2,3\}\), and \(\ell\ge2\).
The prerequisites in `lower_branch_reduction.md` give the exact bands

\[
\begin{array}{ll}
d=2:&4j+5\le B<10j,\quad B<5j\text{ if }j\ge800,\\
d=3:&3j+1\le B<4j,
\end{array}
\qquad 2B\le A.
\]

Also \(\ell<j\), \(k\ge\ell+2\), so the effective index
\(e=\min(\ell,k-\ell)\) is at least 2 and
\(\binom k2\le B\). These facts bound \(k\) and give a complete
finite enumeration, with no experimental upper cutoff on the original
equation.

The files are:

* `finite_prime_outer_exclusion.py`
* `finite_prime_outer_certificates.json`
* `finite_prime_outer_verification.json`

The generator enumerates \(k\) first, builds \(\binom ke\) by its
integer recurrence, and records a prime modulus for each candidate.
The verifier separately enumerates \(e\) first, binary-searches the
exact binomial bounds for \(k\), and checks that the entire candidate
set is covered exactly once. It checks each modular contradiction by
Lucas's formula, using direct integer `math.comb` on the prime-base
digits; the generator used a different factorial-table implementation.
Primality is also checked by trial division in the verifier, separately
from the generator's sieve.

The executed result, reproduced by a separate AI reviewer, is:

| Quantity | Result |
|---|---:|
| Offset 2 candidates | 141,865 |
| Offset 3 candidates | 153,546 |
| Total candidates | 295,411 |
| Candidates with verified modular contradictions | 295,411 |
| Unresolved candidates | 0 |
| Largest witness prime | 71 |

Reproduction command:

```bash
python finite_prime_outer_exclusion.py verify
```

Every recorded modulus is prime, and the left and right sides have
different residues modulo that prime. Thus all candidates in this
proved finite remainder are impossible.

## 6. Exact certificate for all smaller remaining first lower indices

It remains to handle \(21\le j\le99\). The offset-2/3 reduction
does not apply here, so every offset \(p-j\ge2\) must be retained.
Section 2 of `lower_branch_reduction.md` proves, from \(B\ge3j\),

\[
A<B^3<1000j^3.
\tag{9}
\]

For each fixed \(j\) in this finite interval,
\(\binom pj\) strictly increases with \(p\). Thus (9) gives a
proved finite upper bound on the prime \(p\), rather than an
experimental search cutoff. The independent verifier checks the
exact integer inequality

\[
\binom{2j}{j}>1000j^3
\]

for every \(21\le j\le99\). Consequently it is enough to inspect
\(j+2\le p<2j\), retaining only primes satisfying
\(\binom pj<1000j^3\).

The files are:

* `finite_small_j_prime_exclusion.py`
* `finite_small_j_prime_certificates.json`
* `finite_small_j_prime_verification.json`

The candidate interval for \(B\) starts with
\(3j\le B<10j\) and \(2B\le A\). The proved sharper bounds
are also imposed where applicable: offset 2 requires \(B\ge4j+5\),
offset 3 requires \(B\ge3j+1\), and offset at least 3 with
\(j\ge30\) requires \(B<4j\). Every \(\ell=1\) case is
included. For \(\ell\ge2\), both original lower-index
orientations are included, subject to \(\ell<j\) and
\(k\ge\ell+2\).

The generator increases \(p\) until the monotone bound (9) first
fails, then enumerates the original \(k,\ell\). The verifier uses
the independently checked central-binomial bound \(p<2j\), then
enumerates effective lower indices first and reconstructs both
orientations. It checks the same certificate by the independent
direct-digit implementation of Lucas's formula. It also checks there
are no duplicate, missing, or extraneous certificate entries.

The executed result, reproduced by a separate AI reviewer, is:

| Quantity | Result |
|---|---:|
| Prime-index pairs \((j,p)\) surviving the proved height | 93 |
| Largest surviving prime upper index | 103 |
| Candidates with \(\ell=1\) | 11,819 |
| Candidates with \(\ell\ge2\) | 1,639 |
| Total candidates | 13,458 |
| Verified modular contradictions | 13,458 |
| Unresolved candidates | 0 |
| Largest witness prime | 17 |

Reproduction command:

```bash
python finite_small_j_prime_exclusion.py verify
```

This completes the interval \(21\le j\le99\), without presuming
an offset bound. Together with the earlier \(M\le20\) exclusion,
it removes the condition \(j\ge100\) from the final theorem.

## 7. Scope

The congruence and analytic cases cover \(\ell=1\), effective
second lower index at least 3, and effective second lower index 2.
They prove exclusion for every prime \(p\ge16384\) remaining after
the offset-2/3 reduction, with no upper cutoff. The exact certificate
in Section 5 covers all smaller primes in that reduced family;
Section 6 covers the smaller \(j\) where the offset reduction was
not available. Together with the earlier \(M\le20\) certificate,
these prove the theorem for the whole specified family. The proof is written
mathematics plus exact modular certificate verification; it has not
been formalized in Lean. It does not exclude prime \(i\) in other
branches or prove global nonexistence of the original equation.
