# Complete exclusion of the mixed family i = 2 P^a + 2

## Theorem and scope

For the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

there is no solution in the entire family

\[
\boxed{\ell=1,\qquad j=i-3,\qquad i=2P^a+2,
\qquad P\text{ prime},\quad a\ge1.}
\tag{1}
\]

Both outer branches are included. This extends the v8 complete exclusion
of i=P^a+2 to a family for which i-2 generally has two different prime
factors. It does not classify all composite i-2 or solve the whole
four-variable equation.

For P=2 the theorem follows from v8. The base P=3 is reduced to six
explicit squarefree factorizations. For P>=5, exact valuations leave
three types, an integer quotient gives n<2^192, and a normalized unit
congruence bounds the remaining prime bases. The final remainder is
exactly 2,592 explicit integers, each strictly between adjacent cubes.
All bounds used to define that remainder are proved here.

## 1. Established input and notation

Put

\[
q=P^a,\quad n=2q+2,\quad A=\binom n3,\quad
r=\min(k,A-k),\quad L=\binom Ar,
\]

\[
X=\binom{n^2}{6n-9},\qquad Y=k^2.
\]

The equality defining X uses binomial symmetry. The earlier complete
small-j theorem and endpoint reductions give n>=104 and L=X+Y for
every remaining solution. The two possible values of k are r and A-r.

The v5 gap, v6 common divisor, and v6 logarithmic refinement give

\[
3n<r<10n/3,\qquad
Q:=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3,
\tag{2}
\]

and, when n>=1024,

\[
r<3n+\frac{3n}{4\log n}<\frac{25n}{8}.
\tag{3}
\]

We also use the v6 theorem excluding every case where n-1 is
squarefree. These inputs are proved respectively in
`v5_offset_three_structure.md`, `v6_common_divisor.md`, and
`v6_offset_composite.md`.

## 2. The small prime bases

### 2.1 Base two

When P=2, one has n=2^(a+1)+2. This is already excluded by
`v8_shifted_prime_power_completion.md` for every positive a.

### 2.2 Base three: exact valuations

Now let P=3. Exponents a<=3 give n<=103 and are already excluded.
For a=4,5, the integers n-1 are respectively the primes 163 and 487,
so the squarefree n-1 theorem applies. Assume henceforth a>=6.

Write

\[
\alpha=a-1,\quad \rho=3^\alpha=q/3,\qquad
A=\rho T,\quad T=2(q+1)(2q+1).
\]

Since n>=1460, (3) is available. Its lower and upper bounds give

\[
18<r/\rho<\frac{75}{4}(1+1/q)<19.
\tag{4}
\]

Thus r=18 rho+u with 0<u<rho. In particular d=v_3(r)<alpha,
and both possible values of k have valuation d.

The lower alpha base-three digits of A-1 are all 2. Separating
those digits in Legendre's formula therefore gives

\[
v_3(L)=\alpha-d+v_3\binom{T-1}{18}.
\tag{5}
\]

Among T-m for 1<=m<=18, the multiples of 3 occur at
m=2,5,8,11,14,17. Their valuations, in that order, are

\[
a+1,\quad1,\quad1,\quad2,\quad1,\quad1.
\]

Indeed T-2=2q(2q+3) has valuation a+1; each other listed factor
differs from it by 3,6,9,12,15. Since v_3(18!)=8,

\[
v_3\binom{T-1}{18}=a-1=\alpha,
\qquad v_3(L)=2\alpha-d.
\tag{6}
\]

For X, split into q-blocks:

\[
n^2=q(4q+8)+4,\qquad 6n-9=12q+3,
\qquad n^2-(6n-9)=q(4q-4)+1.
\]

The lower blocks contribute v_3 C(4,3)=0. Consequently

\[
v_3(X)=v_3\binom{4q+8}{12}=a-2=\alpha-1.
\tag{7}
\]

To see the middle evaluation directly, the numerator factors are
4q+t for -3<=t<=8. Their total 3-adic valuation is a+3,
coming from t=-3,0,3,6. Subtracting v_3(12!)=5 gives a-2.

The equation L=X+Y, with v_3(Y)=2d, now forces

\[
\boxed{2d=a-2,\qquad a\text{ even}.}
\tag{8}
\]

If 2d<alpha-1, equality of valuations would require 2alpha=3d,
contradicting that strict inequality. If 2d>alpha-1, the right
side has valuation alpha-1, whereas 2alpha-d>alpha because
d<alpha. Only equality of the two right-side valuations remains,
which is exactly (8).

### 2.3 Base three: the exponent is at most twelve

Here n is even and n=2 modulo 3, so Q=n(n-1), which is prime to 3.
Write r=3^d v. The divisibility in (2) implies Q|v^3, and hence

\[
n(n-1)\le v^3<\frac{1000n^3}{27\,3^{3d}}.
\]

Divide the resulting bound on 3^(3d) by q=3^a and use (8):

\[
3^{(a-6)/2}
<\frac{2000}{27}\frac{(2q+2)^2}{(2q)(2q+1)}.
\tag{9}
\]

For z>320,

\[
\frac{(z+2)^2}{z(z+1)}
=1+\frac{3z+4}{z(z+1)}<1+4/z<81/80.
\tag{10}
\]

Since 2q>=1458, (9) gives

\[
3^{(a-6)/2}<75<81.
\]

Thus a is one of 6,8,10,12. All these cases have squarefree n-1:

| a | n-1 = 2*3^a+1 |
|---:|---|
| 4 | 163 |
| 5 | 487 |
| 6 | 1459 |
| 8 | 11 * 1193 |
| 10 | 17 * 6947 |
| 12 | 353 * 3011 |

Every displayed factor is prime and all factors in each row are
distinct; the companion checker verifies this by deterministic trial
division. The squarefree n-1 theorem excludes every row. This
completes the base-three branch for all positive exponents.

## 3. Every remaining base at least five has a fixed outer block

Assume now P>=5. If q<=50, then n<=102 and the small-j theorem
already applies. Otherwise q>50, and (2) gives

\[
6<r/q<\frac{20}{3}+\frac{20}{3q}<7.
\tag{11}
\]

We have

\[
A=qT,\qquad T=\frac{2(q+1)(2q+1)}3,
\qquad v_P(A)=a.
\]

Thus r=6q+u with 0<u<q, d=v_P(r)<a, and both k branches
have valuation d. Separating the low a digits gives

\[
\boxed{v_P(L)=a-d+\delta_P,\qquad
\delta_P:=v_P\binom{T-1}{6}.}
\tag{12}
\]

### 3.1 The two exact valuation tables

For 1<=m<=6,

\[
T-m=\frac{4q^2+6q+2-3m}{3}.
\]

The six constant numerators 2-3m are

\[
-1,-4,-7,-10,-13,-16.
\]

For P=7 and P=13 the corresponding factor has valuation exactly
one, since q>50 already forces a>=2 at these primes. For P=5,
the single factor of 5 in the numerator cancels the single factor
in 6!. All other primes P>=5 have neither occurrence. Therefore

\[
\boxed{\delta_P=
\begin{cases}1,&P=7,13,\\0,&P=5,11\text{ or }P\ge17.
\end{cases}}
\tag{13}
\]

The same q-block decomposition used in Section 2 gives

\[
v_P(X)=v_P\binom{4q+8}{12}.
\]

In the numerator offsets -3 through 8, P=5 sees offsets 0 and 5,
P=7 sees 0 and 7, and P=11 or P>=13 sees only 0.
Subtracting the valuation of 12! gives

\[
\boxed{v_P(X)=
\begin{cases}a-1,&P=5,11,\\a,&P=7,13\text{ or }P\ge17.
\end{cases}}
\tag{14}
\]

At P=5,7,11,13, the assumption q>50 ensures a>=2, so the
nonzero multiple offsets have exactly one factor of P. For larger
primes the formula is valid even for a=1.

### 3.2 Consequences of the valuation balance

Equations (12)-(14), together with v_P(Y)=2d, imply

| Base | Necessary relation |
|---|---|
| P>=17 | a=3d |
| P=7,13 | a+1=3d |
| P=5,11 | a=3d, or the exceptional pair (a,d)=(2,1) |

Here are the equal-valuation cases explicitly. If v_P(X)=a
and delta_P=0, then 2d=a would make the left valuation a-d
less than a, which is impossible; the remaining possibilities force
a=3d. If delta_P=1, the case 2d=a can only have a=2,d=1,
which still satisfies a+1=3d; the unequal case again gives that
relation. If v_P(X)=a-1 and delta_P=0, the case 2d>a-1
forces d=1 and a=2. The equality 2d=a-1 requires a<=3,
so its only possibility is a=3,d=1, already in a=3d.
The other case gives a=3d directly.

All small exceptional exponents can now be removed:

- P=5,a=2 and P=7,a=2 were already in n<=103.
- P=11,a=2 gives n=244 and
  Q=n(n-1)/3=2^2*3^4*61. Therefore Q|r^3 requires
  1098=2*3^2*61 to divide r. But r<10n/3<1098.
- P=5,a=3 gives n-1=251, prime.
- P=11,a=3 gives n-1=2663, prime.

The last two are excluded by the squarefree n-1 theorem. We have
therefore obtained the following complete list of remaining types:

| Base | Exponents | d | K=P^(3d-a) |
|---|---|---|---:|
| P>=17 | a>=3, a=0 modulo 3 | a/3 | 1 |
| P=5,11 | a>=6, a=0 modulo 3 | a/3 | 1 |
| P=7 | a>=5, a=2 modulo 3 | (a+1)/3 | 7 |
| P=13 | a>=2, a=2 modulo 3 | (a+1)/3 | 13 |

In all four rows, z=2q>320. The smallest possibility is z=338
at P=13,a=2.

## 4. A stronger common divisor keeps the height bound at 2^192

Since P!=3, n is even and n=0 or 1 modulo 3. The common divisor
in (2) is therefore exactly

\[
\boxed{Q=\frac{n(n-1)}3,\qquad \gcd(Q,P)=1.}
\tag{15}
\]

Write r=P^d v. Cancelling the P-power from Q|r^3 gives a
positive integer quotient

\[
\boxed{t=\frac{3v^3}{n(n-1)}\in\mathbb Z_{>0},\qquad
3v^3=t(2P^a+2)(2P^a+1).}
\tag{16}
\]

The factor 3 in (15), instead of 6, is useful here. With z=2q
and K from the preceding table,

\[
Kt=\frac{3r^3}{q n(n-1)}
=\frac{6r^3}{z n(n-1)}.
\tag{17}
\]

Using (2), (10), and z>320 gives

\[
\boxed{162<Kt<225.}
\tag{18}
\]

Thus the complete possible integer ranges are

| K | Possible t |
|---:|---|
| 1 | 163,...,224 |
| 7 | 24,...,32 |
| 13 | 13,...,17 |

If log n>=128, then z=n-2>2^20, and (3), (10), (17) give

\[
162<Kt<162(513/512)^3(1+2^{-18})<163.
\]

This is impossible because Kt is an integer. The final strict
comparison is the exact rational inequality

\[
162(513/512)^3(1+2^{-18})
=\frac{2866676543645265}{17592186044416}<163.
\]

Consequently

\[
\boxed{n<e^{128}<2^{192}.}
\tag{19}
\]

As in v8, the latter inequality follows from e<11/4 and
(11/4)^2<8. No numerical search cutoff has been introduced.

## 5. A normalized unit bounds every other prime base

We now restrict to the ordinary rows K=1: P>=17, or P=5,11
with a>=6. At these bases, v_P(X)>2d, whereas v_P(L)=2d.

Splitting the product for C(A-1,r-1) at q,2q,...,6q gives

\[
\frac{L}{P^{a-d}}
\equiv\frac{(-1)^{r-7}T}{v}\binom{T-1}{6}\pmod P.
\tag{20}
\]

Every other factor is -1 modulo P. The exact rational value at
T=2/3 is

\[
\frac{\prod_{m=1}^6(2/3-m)}{6!}=\frac{728}{6561}.
\tag{21}
\]

Thus C(T-1,6)=728/6561 modulo P. At P=5, evaluating this
polynomial requires accounting for the denominator 6!: the difference
from its value at 2/3 has valuation at least a-v_5(6!)=a-1>=1.
For all other ordinary bases 6! is a unit. Hence (21) is valid
modulo every prime used in (20).

Dividing L=X+Y by P^(2d), the normalized right side is v^2
modulo P, for both k=r and k=A-r. As T=2/3 modulo P, (20)
therefore yields

\[
\boxed{(27v)^3\equiv\pm1456\pmod P.}
\tag{22}
\]

On the other hand, (16) reduced modulo P gives 3v^3=2t modulo P.
Combining this with (22) and cancelling 2 gives

\[
\boxed{P\mid6561t-728\quad\text{or}\quad P\mid6561t+728.}
\tag{23}
\]

Both integers are positive, and 163<=t<=224. Therefore every
ordinary prime base satisfies

\[
\boxed{P\le6561\cdot224+728=1470392.}
\tag{24}
\]

Factoring the 124 specified integers in (23), and retaining primes
P>=5 other than 7 and 13, gives 241 prime-quotient pairs with
163 distinct prime bases. Their maximum is 1436131. The independent
verifier reconstructs the same list by sieving all primes through
the proved bound (24), rather than trusting those factorizations.

## 6. Complete finite certificates

Equation (16) requires the following integer to be a cube:

\[
\boxed{V(P,a,t)=\frac{t(2P^a+2)(2P^a+1)}3=v^3.}
\tag{25}
\]

The complete finite domain is defined as follows:

1. Ordinary bases: use (23), 163<=t<=224, a=0 modulo 3,
   a>=6 for P=5,11 and a>=3 for P>=17, with 2P^a+2<2^192.
2. P=7: use a=5,8,...,68 and t=24,...,32.
3. P=13: use a=2,5,...,50 and t=13,...,17.

The endpoints in the last two rows are checked by exact integer powers.
The counts are

| Type | Number of triples (P,a,t) |
|---|---:|
| Ordinary bases | 2309 |
| P=7 | 198 |
| P=13 | 85 |
| Total | 2592 |

There are 1018 distinct pairs (P,a). For every one of the 2592
triples, the accompanying certificate supplies a nonnegative integer m
such that

\[
\boxed{m^3<V(P,a,t)<(m+1)^3.}
\tag{26}
\]

Thus none of the required values is a cube. This contradicts (25)
for every P>=5 case. Sections 2.1-2.3 already excluded P=2,3,
which proves (1) for all primes and all positive exponents.

## 7. Verification, reproducibility, and limits

Run the standard-library script

    python3 v9_cofactor_two_checks.py

It creates `v9_cofactor_two_certificates.json` and
`v9_cofactor_two_verification.json`.

The generator factors the integers in (23) and computes lower integer
cube roots by exact binary search. The verifier independently sieves
all primes up to (24), reconstructs all exponents and quotient ranges,
and checks that the serialized certificate has exactly that domain,
without omissions or duplicates. It checks (26) by direct integer
cubing, without a cube-root algorithm. All 2592 rows pass.

The script also checks every small exceptional factorization, the
exact constants, and representative valuation and normalized-unit
identities using Legendre's formula and a separate factorial-unit
recursion. Those representative checks support the written uniform
proof; they are not used to extrapolate an infinite theorem from a scan.

The finite arithmetic has not been Lean-formalized by this script.
Any subsequent formalization must distinguish the finite row checks
from the analytic, valuation, and domain-completeness reductions.
The original four-variable equation is still unresolved.

Two independent mathematical audits passed on 2026-11-05. The root
reviewer and the gcd-structure reviewer each checked the whole proof,
including the base-three digit block and valuations, every small
exception, the factor 3 in (15), the denominator-5 issue in (21),
the prime bound, and the complete exponent endpoints. Neither found
a mathematical correction necessary.

The gcd-structure reviewer also independently reconstructed the entire
finite domain with a prime sieve and the equivalent condition
(6561t)^2-728^2=0 modulo P, then used a Newton integer cube-root
algorithm to verify every serialized witness. This reproduced all
2592=2309+198+85 noncube values, the 241 ordinary prime-quotient
pairs, all 163 ordinary prime bases, and the maximum 1436131.
These independent AI audits are not external peer review.
