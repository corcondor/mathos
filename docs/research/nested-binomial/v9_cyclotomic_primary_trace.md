# Cyclotomic cofactor seven: a primary-trace obstruction for every exponent

## Scope and new conclusions

The original equation remains
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
This note continues the large-prime branch
\[
i=jp^3,\quad k=p,\quad\ell=1,\quad p\text{ prime},\quad
j\text{ odd},\quad j\ge101,\quad p\ge103,\quad
\frac p2<j<\frac{10p}{19}.
\tag{1}
\]
Write
\[
A=\binom{jp^3}{j},\quad X=\binom{j^2p^6}{j^2},\quad
L=\binom Ap,\qquad p^2+p+1=7q^a,
\tag{2}
\]
where q is prime. The earlier notes exclude q=3,7 and give
\[
q\equiv1\pmod3,\quad q\ge13,\quad
q\mid42j^2+p-1,\quad q^a<j^2<2q^a.
\tag{3}
\]
They also exclude a=1, all multiples of 3, and all multiples of 4.
For even a, v8 proves q=7 modulo 12 and p=2 modulo 7.

The new results are:

1. An exact, exponent-dependent congruence involving the **primary trace**
   B of q. With r=p modulo q,
   \[
   \boxed{
   B^a\equiv
   \begin{cases}
   (2r+1)/(r+3),&p\equiv2\pmod7,\\
   (r+2)/(r-2),&p\equiv4\pmod7.
   \end{cases}}
   \tag{4}
   \]
   Here B is the unique integer with
   \[
   \boxed{4q=B^2+27m^2\text{ for some }m>0,\qquad B\equiv2\pmod3.}
   \tag{5}
   \]
   The existence and uniqueness needed in (5) follow from the Eisenstein
   factorization proved below. They are not assumptions about q.
2. If q is prime, q is not 7, and **4q=1+27m^2**, then
   \(p^2+p+1=7q^a\) itself has no solution with p prime greater than 3
   and a positive. This unbounded family includes q=61,331,547.
3. In the original branch (1), among the 21 possible prime bases
   \(13\le q\le211\), only **q=19,31,67** survive the new finite-field
   tests. Their exponents must be odd and satisfy
   \[
   \begin{array}{c|c|c|c}
   q&p\bmod q&p\bmod7&\text{necessary exponent condition}\\\hline
   19&11&4&a\equiv1\pmod6,\quad a\ge7\\
   31&5&4&a\equiv9\pmod{10},\quad3\nmid a,\quad a\ge19\\
   67&37&2&a\equiv21\pmod{22},\quad3\nmid a,\quad a\ge43.
   \end{array}
   \tag{6}
   \]
   This is a complete exclusion of every exponent for the other 18
   bases, not a scan up to a chosen exponent.
4. For every remaining even exponent a=2s, **q>=367**. In particular
   the two v8 valuation exceptions q=151,211 have been completely
   removed; the exact valuation in every surviving even case is
   \[
   \boxed{v_q(L)=v_q(X+p^2)=s.}
   \tag{7}
   \]
5. For odd a=2s+1, the outer valuation improves from q|L to
   \[
   \boxed{v_q(L)=v_q(A-1)\ge s+1,}
   \tag{8}
   \]
   with an explicit leading harmonic residue and a smaller binomial
   expression for X modulo q^(s+1).

No result here solves the full large-prime branch or the original
four-variable equation. No new Lean formalization is claimed.

## 1. Primary normalization fixes the units completely

Let \(\omega^2+\omega+1=0\) and work in
\(R=\mathbb Z[\omega]\). Its norm is
\(N(x+y\omega)=x^2-xy+y^2\). The norm-Euclidean proof, unique
factorization, and six units were given in v7.

Every prime q=1 modulo 3 splits as q=pi times its conjugate, with
N(pi)=q. The quotient R/(3) has nine elements, exactly six of them
units. The residues of \(\pm1,\pm\omega,\pm\omega^2\) are precisely
those six units. Consequently there is exactly one associate of
each prime factor for which
\[
\pi\equiv1\pmod{3R}.
\tag{9}
\]
Both pi and its conjugate satisfy (9). Write pi=x+y omega and define
\[
B=\pi+\bar\pi=2x-y.
\]
Then x=1 modulo 3, y=0 modulo 3, and
\[
4q=B^2+3y^2=B^2+27m^2,\qquad B\equiv2\pmod3.
\]
The integer m is nonzero, since a rational integer cannot have prime
norm q. Changing to the conjugate changes the sign of m and leaves
B fixed. Unique factorization shows that these are the only two
normalized prime factors of norm q, proving (5).

Because p is prime greater than 3 and the right side of (2) is 1
modulo 3, necessarily p=2 modulo 3. Also
\[
7=(2-\omega)(3+\omega).
\]
The factors p-omega and p-omega^2 are coprime: a common prime would
divide their difference, whose norm is 3, but 3 does not divide
p^2+p+1. Thus all q-factors of p-omega lie above one of the two
primes over q. Choose pi in that orientation.

If p=2 modulo 7, the factor 2-omega divides p-omega, and
\[
\gamma=\frac{p-\omega}{2-\omega}
\]
is an Eisenstein integer of norm q^a. It is a unit times pi^a.
Modulo 3R, both numerator and denominator equal omega^2, so
gamma=1. Since pi=1 modulo 3R, the unit is exactly 1. Therefore
\[
\boxed{p-\omega=(2-\omega)\pi^a.}
\tag{10}
\]

If p=4 modulo 7, use the other factor:
\[
\gamma=\frac{p-\omega}{3+\omega}.
\]
The numerator is omega^2 modulo 3R and the denominator is omega.
Thus gamma=omega modulo 3R, fixing the unit exactly as omega:
\[
\boxed{p-\omega=(3+\omega)\omega\pi^a.}
\tag{11}
\]
In particular no unspecified unit or sign remains in (10)-(11).

## 2. Reduction at the conjugate prime gives the trace condition

Reduce (10) or (11) modulo bar(pi). The residue field has q elements.
Since the conjugate of p-omega is divisible by bar(pi), in this field
\[
\omega^2=r,\qquad\omega=r^2,\qquad r=p\bmod q,
\qquad r^2+r+1=0.
\]
Also pi=B modulo bar(pi). Hence (10) gives
\[
B^a=\frac{r-r^2}{2-r^2}
=\frac{2r+1}{r+3}=:T_1(r).
\]
Equation (11) gives
\[
r^2B^a=\frac{r-r^2}{3+r^2},
\qquad
B^a=\frac{r+2}{r-2}=:T_2(r).
\]
This proves (4). All denominators are nonzero: r=-3 or r=2 would
make q divide 7, which is excluded.

The original binomial equation imposes, independently,
\[
\boxed{\left(\frac{(1-r)/42}{q}\right)=1,}
\tag{12}
\]
where the symbol denotes the quadratic character. Indeed (3) says
j^2=(1-r)/42 modulo q, and q does not divide j. If q divided j,
(3) would force r=1, contradicting r^2+r+1=0 for q not 3.

The combination of (4), (12), and the exponent restrictions is a
uniform test involving only q and the residue class of a.

### 2.1 A cubic-reciprocity consequence

There is also a faster, weaker filter that avoids computing the full
multiplicative order of B: **B is a cube modulo q**.

To see this, use cubic reciprocity on the coprime primary primes
pi and bar(pi). It gives
\[
\left(\frac{\pi}{\bar\pi}\right)_3
=\left(\frac{\bar\pi}{\pi}\right)_3.
\]
Complex conjugation sends one symbol to the conjugate of the other.
An element of {1,omega,omega^2} equal to its conjugate must be 1.
Thus pi modulo bar(pi), which is B, is a cube. Consequently (4)
requires T1 or T2 to be a cube, with the choice determined by p mod 7.

The external theorem used in this paragraph is the classical cubic
reciprocity law in J.S. Milne, *Class Field Theory*, version 4.03
(2020), Chapter VIII, Example 5.13, printed page 249, PDF page index
257. It applies to any relatively prime Eisenstein integers that are
each congruent to plus or minus 1 modulo 3R; it therefore includes
the conjugate prime pair of equal norm used here.

Author-hosted source, directly checked on 2026-11-05:
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>.

This source is an external theorem dependency for the **universal
cubic filter**. The exact trace congruence, the B=-1 family below,
and the explicit finite power-period certificates do not require
that reciprocity law: their checks use (10)-(11) and exact powers.

## 3. An unbounded family with trace minus one

**Theorem.** Suppose q is a prime different from 7 and
\[
4q=1+27m^2\quad(m>0).
\]
There are no primes p>3 and positive a satisfying
\(p^2+p+1=7q^a\).

Here (5) forces B=-1. If a is even, (4) requires T1=1 or T2=1.
The first implies r=2, forcing q=7; the second implies 4=0 modulo q.
Both are impossible.

If a is odd, it requires T1=-1 or T2=-1. The first gives 3r=-4;
substitution into r^2+r+1=0 makes q divide 13. But q=13 does not
satisfy 4q=1+27m^2. The second gives 2r=0, also impossible for a
nontrivial cube root r modulo an odd prime. This proves the theorem.

The primes 61,331,547 arise from m=3,7,9. The theorem is uniform in
m and a. It does not assert that infinitely many values of the
quadratic expression (1+27m^2)/4 are prime.

## 4. Complete exponent-period certificates for small prime bases

For fixed q let d=ord_q(B), and let M=lcm(d,12). Every expression
B^a depends only on a modulo d. The established restrictions
3 does not divide a and 4 does not divide a depend only on a modulo
12. In addition, if a is even, v8 requires p=2 modulo 7 and q=7
modulo 12.

It therefore suffices to check **one complete period 0<=a<M** for
each of the two roots r of r^2+r+1 and the two choices p=2,4 modulo 7.
This is a proof of coverage for all exponents, rather than an
arbitrary exponent cutoff.

The companion checker performs these finite-field calculations by
successive multiplication. Its independent verifier uses modular
exponentiation, verifies the order by checking its prime divisors,
reconstructs the prime bases with a sieve, and checks the entire
period again. All tables and surviving residues are in
`v9_cyclotomic_primary_trace_verification.json`.

Among all primes q=1 modulo 3 with 13<=q<=211 the complete table is:

| q | B | Outcome after all prior and new necessary conditions |
|---:|---:|---|
| 13 | 5 | excluded |
| 19 | -7 | odd a=1 mod 6; a>=7 |
| 31 | -4 | odd a=9 mod 10, 3 does not divide a; a>=19 |
| 37 | 11 | excluded |
| 43 | 8 | excluded |
| 61 | -1 | excluded |
| 67 | 5 | odd a=21 mod 22, 3 does not divide a; a>=43 |
| 73 | -7 | excluded |
| 79 | 17 | excluded |
| 97 | -19 | excluded |
| 103 | -13 | excluded |
| 109 | 2 | excluded |
| 127 | 20 | excluded |
| 139 | 23 | excluded |
| 151 | -19 | excluded |
| 157 | 14 | excluded |
| 163 | -25 | excluded |
| 181 | -7 | excluded |
| 193 | 23 | excluded |
| 199 | 11 | excluded |
| 211 | -13 | excluded |

The existing quadratic test by itself excludes 13,37,181. The other fifteen
excluded bases are additional exclusions from combining the exact
trace condition with the established restrictions. For the surviving
three bases the root and p modulo 7 are uniquely as in (6).

### 4.1 Removing the two exceptional valuation primes

For q=151 the roots are 32,118. The root 32 violates (12). At r=118,
\[
T_1=128,\quad T_2=126,\qquad
T_1^{50}=32,\quad T_2^{50}=118\pmod{151}.
\]
Neither is a cube. For q=211 the root 196 violates (12), and at r=14,
\[
T_1=101,\quad T_2=142,\qquad
T_1^{70}=T_2^{70}=196\pmod{211}.
\]
Again neither is a cube. This illustrates the shorter reciprocity
filter; the full power-period certificate independently excludes
both primes without using the reciprocity theorem.

The v8 exact valuation formula for even a=2s was
\[
v_q(L)=s+v_q(H-1)+v_q(H-2),\qquad
H=(A-1)/q^s,
\]
with a possible excess above s only at q=151 or211. Since both
prime bases have now been excluded for every exponent, (7) follows
without exceptions.

### 4.2 A stronger lower bound in the even branch

The 17 primes q=7 modulo 12 with 13<=q<367 are
\[
19,31,43,67,79,103,127,139,151,163,199,211,
223,271,283,307,331.
\]
Their complete periods have no compatible even exponent. Thus
q>=367 is necessary for any remaining even case. The first prime
not removed by this certificate, q=367, has
\[
r=83,\quad p\equiv2\pmod7,\quad
a\equiv52\pmod{122},\quad a\equiv2\text{ or }10\pmod{12}.
\]
In particular a>=418 for this specific base. No assertion is made
that q=367 actually gives a solution.

The exclusion of multiples of 3 used in these combined period tables
inherits the Thomas--Mignotte theorem dependency recorded in v7.
The tables themselves use only exact finite arithmetic.

## 5. Odd exponents: exact outer valuation and a harmonic leading term

Let a=2s+1, where s>=0. Put
\[
u=q^s,\qquad J=\left\lfloor j/u\right\rfloor,
\qquad H_J=\sum_{h=1}^J\frac1h.
\]
From (3), j<sqrt(2q)u<q^(s+1), so J<q and all denominators
of H_J are q-adic units. In the centered product
\[
A=\prod_{m=1}^j\left(1+\frac{7j(p-1)q^{2s+1}}m\right),
\]
all corrections are divisible by q^(s+1). Modulo q^(s+2), only
indices m=q^s h survive, with 1<=h<=J. Products of two corrections
are divisible by q^(2s+2), which is at least q^(s+2). Consequently
\[
\boxed{
A\equiv1+7j(p-1)q^{s+1}H_J\pmod{q^{s+2}}.
}
\tag{13}
\]

Also p^2<7q^(2s+1)<q^(2s+2), so p<q^(s+1). In
\[
L=\frac{A(A-1)}{p(p-1)}\binom{A-2}{p-2},
\]
the denominator is a q-adic unit. The low s+1 digits of A-2 are
all q-1, and p-2 is smaller than q^(s+1). Legendre's formula
therefore makes the final binomial a q-adic unit. Lucas' theorem
gives its residue (-1)^(p-2)=-1, since p is odd. This proves
\[
\boxed{
v_q(L)=v_q(A-1)\ge s+1,\qquad
\frac L{q^{s+1}}\equiv-\frac{7j}{p}H_J\pmod q.
}
\tag{14}
\]
In particular, if H_J is nonzero modulo q then the exact valuation
is s+1, and the equation forces v_q(X+p^2)=s+1 too.

For the three surviving bases below 212, (3) restricts J respectively
to {4,5,6}, {5,6,7}, and {8,9,10,11}. Direct exact harmonic sums are
nonzero modulo q in every case. Therefore every surviving odd case
with q=19,31,67 has the exact valuation v_q(L)=(a+1)/2.

### 5.1 Reducing the lower index of X

Put n=j^2 and
\[
K=\left\lfloor\frac n{q^{s+1}}\right\rfloor,
\qquad M=\frac{n(p^6-1)}{q^{s+1}}.
\]
The division defining M is exact, and v_q(M)=s. From (3),
\[
q^s\le K<2q^s<j<p.
\]
In the product for X, every index not divisible by q^(s+1)
contributes a factor equal to 1 modulo q^(s+1). The retained factors
are q-adically integral, since their indices are below 2q^(2s+1)
and q>2. Their product is exactly the following binomial:
\[
\boxed{
X\equiv\binom{M+K}{K}\pmod{q^{s+1}}.
}
\tag{15}
\]
Thus every odd-exponent solution must satisfy
\[
\binom{M+K}{K}+p^2\equiv0\pmod{q^{s+1}},
\]
where the new lower index K is smaller than p, rather than j^2.
This necessary condition has not been proved to fail in every
remaining case.

## 6. Verification, dependencies, and remaining work

The exact checker verifies the primary representations, complete
exponent periods, all two-root cases, the B=-1 substitutions, the
examples 61,331,547, the two exceptional-prime eliminations, and the
harmonic residues. Separate generic integer examples check the
odd-exponent digit-block and product-reduction identities.

These finite checks do not prove the unbounded algebraic statements
by extrapolation. The uniform proofs are Sections 1-3 and 5.
The new universal cube-residue corollary uses the cited classical
cubic reciprocity law. Using the earlier exclusion of 3|a in the
period tables retains the v7 external Thue-theorem dependency.
No new Lean formalization or external peer review is claimed.

Two independent AI mathematical audits passed on 2026-11-05. The
root reviewer and the cofactor reviewer each checked the full
uniform proofs, including the exact unit normalization, both
conjugate-prime reductions, the trace-minus-one family, and the
odd-exponent identities with s=0 allowed. Both reviewers also read
the checking code and its report and independently opened the
author-hosted Milne source to confirm the reciprocity hypotheses.

The cofactor reviewer independently reconstructed all 39 period
rows (21 small-base rows, 17 even-base rows, and the q=367 row),
using exact powers and a separate order search. Both roots and both
modulo-seven branches agreed throughout, with the exponent residue
1 retained. The reviewer separately reran all 12 centered-product,
60 outer-digit, and 16 product-compression examples without rewriting
the report. No correction was required in either final audit.
These audits are not external peer review or Lean formalization.
