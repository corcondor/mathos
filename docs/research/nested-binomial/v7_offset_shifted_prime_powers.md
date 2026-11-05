# Offset three: prime powers shifted by two

## Theorem and scope

We keep the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

In this note \(\ell=1\), \(j=i-3\), and \(i=P^a+2\), where
\(P\) is prime and \(a\ge1\). Put

\[
z=P^a,\quad n=z+2,\quad A=\binom n3,\quad
B=k,\quad r=\min(B,A-B),\quad L=\binom Ar,
\]

\[
X=\binom{n^2}{6n-9},\qquad Y=B^2.
\]

Both choices \(B=r\) and \(B=A-r\) are included throughout.

**Shifted prime-power theorem.** For any solution in this family,
\(d=v_P(r)\) satisfies the following necessary conditions:

| Base \(P\) | Necessary exponent condition |
|---|---|
| \(P\ge7\) | \(a=3d\) |
| \(P=2\) | \(a+3=3d\), hence \(a=3h\), \(d=h+1\), \(h\ge5\) |
| \(P=3\) | \(a-1=2d\), with odd \(a\ge9\) |
| \(P=5\) | \(a+1=3d\), with \(a\ge8\) |

For \(P\ge7\), write \(v=r/P^d\) and \(u=r-3P^a\). Then

\[
\boxed{(9v)^3\equiv(-1)^u120\pmod P.} \tag{1}
\]

Consequently every \(n=P^a+2\) with \(P\ge7\) and
\(a\not\equiv0\pmod3\) is excluded. All \(n=13^a+2\) and
\(n=19^a+2\) are excluded, for every positive exponent.

For \(P=3\) there is the additional necessary condition

\[
\boxed{r/3^d\equiv 2\text{ or }7\pmod9.} \tag{2}
\]

There is also a uniform obstruction involving the factors of \(P^a+1\):

**Plus-Wieferich consequence.** If a solution has first index
\(n=b^a+2\), for \(b=2,3,5\), then there exists an odd prime
\(q\mid b^a+1\) satisfying

\[
b^{q-1}\equiv1\pmod{q^2},
\]

and lying outside the following explicitly checked finite set:

| Base \(b\) | The required prime lies outside |
|---|---|
| 2 | \(\{1093,3511\}\) |
| 3 | \(\{11,1006003\}\) |
| 5 | \(\{20771,40487\}\) |

These are unconditional necessary conditions. No claim is made that
these finite sets contain all primes with the displayed congruence,
or that the original equation is now completely solved. The proof
uses exact valuations, the previously proved real gap, and elementary
lifting of prime divisibility; no conjecture about Wieferich primes is
assumed. The new arguments in this note have not been formalized in Lean.

## 1. Previously established input

The complete exclusion for \(\ell=1,j\le100\) and the v5 offset-three
gap give

\[
n\ge104,\qquad 3n<r<10n/3. \tag{3}
\]

The v6 common-divisor theorem gives

\[
\frac n{\gcd(n,3)}\,
\frac{n-1}{\gcd(n-1,6)}\mid r^3. \tag{4}
\]

In particular, if \(n/\gcd(n,3)\) is squarefree, there is no solution.
For an integer \(t\ge1\), define

\[
c_3(t)=\prod_{q\mid t}q^{\lceil v_q(t)/3\rceil}.
\]

Thus \(t\mid r^3\) is equivalent to \(c_3(t)\mid r\).
We also use the v6 logarithmic gap

\[
n\ge1024\quad\Longrightarrow\quad
r<3n+\frac{3n}{4\log n}. \tag{5}
\]

These inputs are proved in `v5_offset_three_structure.md` and
`v6_offset_composite.md`; the small-index result is recorded in the
v4 research notes. We do not introduce an arbitrary numerical cutoff.

## 2. Exact valuation of the inner right-hand binomial

Here

\[
N=n^2=z^2+4z+4,\qquad m=6n-9=6z+3,
\]

so, on splitting base-\(P\) digits after the bottom \(a\) positions,

\[
N=z(z+4)+4,\qquad m=6z+3,\qquad
N-m=z(z-2)+1.
\]

Since \(z\ge102\), the bottom blocks are 4, 3 and 1. There is
no borrow from the upper block when subtracting 3 from 4. Legendre's
factorial-valuation formula therefore gives the exact identity

\[
v_P X=v_P\binom43+v_P\binom{z+4}{6}. \tag{6}
\]

One can check the block identity directly by summing
\(\lfloor N/P^t\rfloor-\lfloor m/P^t\rfloor-
\lfloor(N-m)/P^t\rfloor\): terms with \(t\le a\) give
\(v_P\binom43\), and terms with \(t>a\) give the other binomial.

Using

\[
\binom{z+4}{6}
=\frac{(z-1)z(z+1)(z+2)(z+3)(z+4)}{720},
\]

we obtain

\[
\boxed{
v_P X=
\begin{cases}
a,&P\ge7,\\
a+1,&P=2,\\
a-1,&P=3\text{ or }5.
\end{cases}} \tag{7}
\]

For example, when \(P=2\), the six numerator factors have total
valuation \(a+3\), the denominator has valuation 4, and
\(v_2\binom43=2\). When \(P=3\), the numerator has valuation
\(a+1\) and the denominator has valuation 2. The bounds on \(a\)
needed for these counts follow from \(z+2\ge104\).

## 3. The outer binomial, for bases other than three

For \(P\ne3\), write

\[
A=zT,\qquad T=\frac{(z+1)(z+2)}6.
\]

This is an integer prime to \(P\). From (3),

\[
r=3z+u,\qquad 6<u<z/3+20/3<z.
\]

In particular \(d=v_P(r)<a\). If \(A=P^aT\) and
\(r=3P^a+u\), with \(0<u<P^a\), the bottom \(a\) digits of
\(A-1\) are all \(P-1\). Counting borrows, or separating the
indices divisible by \(P^a\) in the binomial product, gives

\[
v_P\binom{A-1}{r-1}=v_P\binom{T-1}{3}. \tag{8}
\]

The relevant factors are

\[
T-1=\frac{(z-1)(z+4)}6,\quad
T-2=\frac{(z-2)(z+5)}6,\quad
T-3=\frac{z^2+3z-16}{6}.
\]

They show

\[
v_P\binom{T-1}{3}=
\begin{cases}
0,&P\ge7,\\
3,&P=2,\\
1,&P=5.
\end{cases} \tag{9}
\]

For \(P=2\), the three numerator factors have valuations 1, 0, 3,
and division by 6 removes one power of 2. For \(P=5\), only
\(T-2\) is divisible by 5, and its valuation is exactly 1.

Both possible \(B\) have valuation \(d\), because \(d<a=v_P(A)\).
Thus

\[
v_P L=a-d+v_P\binom{T-1}{3},\qquad v_PY=2d. \tag{10}
\]

### 3.1 Bases at least seven

If \(2d<a\), (7) and (10) imply \(a-d=2d\), so \(a=3d\).
If \(2d>a\), they imply \(a-d=a\), forcing \(d=0\), a
contradiction. If \(2d=a\), the right-hand side has valuation at
least \(a\), while \(a-d<a\), again impossible. This proves
\(a=3d\) in all cases.

For the unit congruence, separate the three factors with indices
\(z,2z,3z\) in

\[
\binom{A-1}{r-1}=\prod_{t=1}^{r-1}\frac{A-t}{t}.
\]

All other factors are \(-1\) modulo \(P\); their number is
\(r-4\). Also \(T\equiv1/3\pmod P\). With \(v=r/P^d\),

\[
\frac{L}{P^{a-d}}
\equiv\frac{(-1)^rT}{v}\binom{T-1}{3}
\equiv\frac{(-1)^{r+1}40}{243v}\pmod P.
\]

Because \(v_PX=a=3d>2d\), the normalized right-hand side is
\(v^2\) modulo \(P\), in either outer branch. Multiplication by
\(729v\) gives

\[
(9v)^3\equiv(-1)^{r+1}120=(-1)^u120\pmod P,
\]

where the sign identity uses the fact that \(3z\) is odd.
Since \(-1\) itself is a cube, the sign cannot rescue a noncubic
120. Direct modular calculation shows that 120 is not a cube modulo
13 or modulo 19, proving their complete exclusions.

### 3.2 Base two

Here \(a\ge7\), \(v_2X=a+1\), and \(v_2L=a+3-d\).
If \(2d<a+1\), valuation comparison gives \(a+3=3d\).
If \(2d>a+1\), it gives \(d=2\), contradicting \(2d>a+1\)
and \(a\ge7\). If \(2d=a+1\), it would require

\[
(a+5)/2=v_2L\ge a+1,
\]

which forces \(a\le3\), again impossible.
Thus \(a=3h\), \(d=h+1\), initially with \(h\ge3\).
For \(h=3,4\), respectively,

\[
n=514=2\cdot257,\qquad
n=4098=2\cdot3\cdot683.
\]

In each case \(n/\gcd(n,3)\) is squarefree, so (4) and the gap
exclude it. Hence \(h\ge5\).

### 3.3 Base five

Now \(a\ge3\), \(v_5X=a-1\), and \(v_5L=a+1-d\).
If \(2d<a-1\), the equation gives \(a+1=3d\); its inequality
then forces \(a>5\). If \(2d>a-1\), it gives \(d=2\) and
therefore \(a<5\). If \(2d=a-1\), it requires

\[
(a+3)/2\ge a-1,
\]

so \(a\le5\). Thus every \(a\ge6\) has
\(a+1=3d\), and the first permitted exponent is 8.
The three smaller exponents are excluded because

\[
5^3+2=127,\quad 5^4+2=3\cdot11\cdot19,\quad
5^5+2=53\cdot59,
\]

each giving squarefree \(n/\gcd(n,3)\).

## 4. Base three: a cancellation case and its unit restriction

Here \(a\ge5\). For \(a=5\), \(n=245\), and the two
coprime factors in (4) are 245 and 122. Hence

\[
c_3(245)c_3(122)=35\cdot122=4270\mid r,
\]

which contradicts \(r<10n/3\). For \(a=6\),
\(n=731=17\cdot43\) is squarefree. We may therefore assume
\(a\ge7\).

Put \(\alpha=a-1\), \(q_0=3^\alpha=z/3\), and

\[
A=q_0T,\qquad T=\frac{(z+1)(z+2)}2.
\]

Since \(n\ge1024\) and \(\log n>6\), (5) gives

\[
r<25n/8=25(z+2)/8<10z/3=10q_0.
\]

The last inequality holds already for \(z>30\). Together with
\(r>3n=9q_0+6\), this gives

\[
r=9q_0+u,\quad 6<u<q_0,\quad d=v_3(r)<\alpha.
\]

Now

\[
T-1=\frac{z(z+3)}2,
\qquad v_3(T-1)=a+1=\alpha+2.
\]

As \(\binom{T-2}{8}\) is a 3-adic unit,

\[
v_3\binom{T-1}{9}=\alpha.
\]

The same block calculation as (8), with nine upper factors, yields

\[
v_3L=2\alpha-d,\quad v_3X=\alpha,\quad v_3Y=2d. \tag{11}
\]

If \(2d<\alpha\), valuation equality would give
\(2\alpha=3d\), inconsistent with \(2d<\alpha\). If
\(2d>\alpha\), it gives \(d=\alpha\), also impossible.
Therefore

\[
2d=\alpha=a-1.
\]

This is the cancellation case: the two right-hand summands have
equal valuation and must cancel further. In particular \(a\) is odd.
The remaining small exponent \(a=7\) gives
\(n=2189=11\cdot199\), already excluded by squarefreeness.
Thus \(a\ge9\).

For completeness, cancellation imposes a nontrivial unit condition.
We prove

\[
\frac{X}{3^{a-1}}\equiv-4\pmod9. \tag{12}
\]

All rational congruences in this paragraph have denominators prime
to 3 after the stated powers of 3 are removed. The exact identity

\[
X=F(z)\binom{z(z+4)}{6z},
\quad
F(z)=\frac{N(N-1)(N-2)(N-3)}{m(m-1)(m-2)(N-m)}
\]

has \(F(z)\equiv4\pmod9\) for \(a\ge3\). To see this,
cancel the factor 3 in \(N-1=(z+1)(z+3)\) against that in
\(m=3(2z+1)\), and reduce the remaining unit factors modulo 9.

For any positive integers \(M\ge K\), the unit quotient

\[
\frac{\binom{3M}{3K}}{\binom MK}
=\prod_{\substack{1\le t<3K\\3\nmid t}}
\left(1-\frac{3M}{t}\right)
\equiv1\pmod9. \tag{13}
\]

Pair the terms \(t=3s+1,3s+2\): their inverses sum to 0
modulo 3, so their product is 1 modulo 9. Applying (13)
successively to \(M=z+4,K=6\) and its scaled versions gives

\[
\binom{z(z+4)}{6z}\bigg/\binom{z+4}{6}\equiv1\pmod9.
\]

The remaining normalized binomial is

\[
\frac1{3^{a-1}}\binom{z+4}{6}
=\frac{(z-1)(z+1)(z+2)(1+z/3)(z+4)}{80}
\equiv-1\pmod9.
\]

This proves (12). Since \(a-1=2d\) and \(v_3L=3d\), dividing
the equation by \(3^{2d}\) and reducing modulo 9 gives
\(v^2\equiv4\pmod9\), where \(v=r/3^d\). In the branch
\(B=A-r\), the normalized square has the same residue because
\(A/3^d=3^dT\) is divisible by 9. The two roots are 2 and 7,
which proves (2).

## 5. Prime multiplicities in \(b^a+1\)

For \(b=2,3,5\) and each odd prime \(q\mid b^a+1\), let

\[
f_q=\operatorname{ord}_q(b),\qquad
e_q=v_q(b^{f_q}-1),\qquad
W_b^+(a)=\prod_{\substack{q\mid b^a+1\\q\text{ odd}}}q^{e_q-1}.
\]

The order \(f_q\) is even, and

\[
a=(f_q/2)t\quad\text{for an odd positive integer }t.
\tag{14}
\]

Indeed \(b^a=-1\pmod q\) is the unique element of order 2 in
the cyclic subgroup generated by \(b\). In particular no prime
with odd \(f_q\) divides \(b^a+1\).

Elementary lifting gives

\[
v_q(b^a+1)=e_q+v_q(a),\qquad
v_q(b^{q-1}-1)=e_q. \tag{15}
\]

Here is a self-contained justification of the needed lifting rule.
If \(q\) is odd and \(q\mid U-1\), binomial expansion shows
\(v_q(U^q-1)=v_q(U-1)+1\): the first term has that valuation
and every later term has greater valuation. If \(q\nmid s\),
then \((U^s-1)/(U-1)\equiv s\pmod q\), so its valuation is
zero. Factoring an arbitrary exponent into its \(q\)-power and
coprime parts proves the rule. Apply it to \(U=b^{f_q}\),
using \(q\nmid f_q\), \(f_q\mid q-1\), and the factorization
\(b^{2a}-1=(b^a-1)(b^a+1)\); the first factor is a \(q\)-unit.

Consequently \(e_q\ge2\) is precisely the displayed Wieferich
condition, and \(W_b^+(a)>1\) forces at least one such prime.

Put \(D=(b^a+1)/\gcd(b^a+1,6)\). By (4),
\(\operatorname{rad}(D)\mid r\). It is coprime to \(b\), so
the exact valuations already proved give

\[
r\ge b^d\operatorname{rad}(D). \tag{16}
\]

We now make this lower bound quantitative in each of the three bases.

### 5.1 Base two

Write \(a=3h\), \(d=h+1\), with \(h\ge5\). The odd number
\(2^a+1\) satisfies

\[
\frac{2^a+1}{\operatorname{rad}(2^a+1)}\mid aW_2^+(a).
\]

Moreover \(\operatorname{rad}(D)=\operatorname{rad}(2^a+1)\).
If \(a\) is even, 3 does not divide \(2^a+1\); if \(a\) is
odd, lifting gives \(v_3(2^a+1)=1+v_3(a)\ge2\), so dividing
by 3 leaves its radical unchanged. Combining (3) and (16) yields

\[
\boxed{
W_2^+(3h)>
\frac{2^{h+1}}{10h}\frac{2^{3h}+1}{2^{3h}+2}.
} \tag{17}
\]

At \(h=5\) the right side exceeds 1, and both factors are
increasing thereafter. Thus every remaining shifted power of two
requires a base-two Wieferich prime dividing \(2^a+1\).

### 5.2 Base three

Here \(a\ge9\) is odd and \(d=(a-1)/2\). We have
\(v_2(3^a+1)=2\), and no factor of 3. Thus

\[
\frac{3^a+1}{\operatorname{rad}(3^a+1)}\mid 2aW_3^+(a),
\qquad \operatorname{rad}(D)=\operatorname{rad}(3^a+1).
\]

Consequently

\[
\boxed{
W_3^+(a)>
\frac{3^{(a+1)/2}}{20a}\frac{3^a+1}{3^a+2}.
} \tag{18}
\]

The right side exceeds 1 at \(a=9\) and increases as the odd
exponent increases by two. Hence the base-three Wieferich condition
is also necessary.

### 5.3 Base five

Here \(a=3d-1\ge8\). The number \(5^a+1\) has exactly one
factor of 2. If \(a\) is odd, it has exactly one factor of 3,
because \(3\nmid a\); if \(a\) is even, it has no factor of 3.
Put \(\epsilon_a=1\) for even \(a\), and
\(\epsilon_a=3\) for odd \(a\). Then

\[
\frac{5^a+1}{\operatorname{rad}(5^a+1)}\mid aW_5^+(a),
\qquad
\operatorname{rad}(D)=\frac{\operatorname{rad}(5^a+1)}{2\epsilon_a}.
\]

Therefore

\[
\boxed{
W_5^+(a)>
\frac{3\,5^{(a+1)/3}}{20a\epsilon_a}
\frac{5^a+1}{5^a+2}.
} \tag{19}
\]

For \(a=8\) this exceeds 1 directly. For every permitted
\(a\ge11\), use \(\epsilon_a\le3\): the weaker expression
\(5^{(a+1)/3}(5^a+1)/(20a(5^a+2))\) exceeds 1 at 11 and
increases as the exponent increases by three. This proves the
base-five necessity.

## 6. The finite sets in the theorem cannot suffice

The accompanying exact script verifies primality, multiplicative order,
and \(e_q=2\) for the six explicitly named primes:

| Base \(b\) | Prime \(q\) | \(f_q\) | \(e_q\) |
|---:|---:|---:|---:|
| 2 | 1093 | 364 | 2 |
| 2 | 3511 | 1755 | 2 |
| 3 | 11 | 5 | 2 |
| 3 | 1006003 | 1006002 | 2 |
| 5 | 20771 | 10385 | 2 |
| 5 | 40487 | 40486 | 2 |

Order is certified by \(b^{f_q}=1\pmod q\) and
\(b^{f_q/t}\ne1\pmod q\) for every prime divisor \(t\mid f_q\).
Multiplicity is certified by modular powers modulo \(q^2\) and
\(q^3\). These are finite checks of the named integers, not a claim
about completeness of a prime list.

For base 2, the prime 3511 cannot divide \(2^a+1\), because its
order is odd. If all Wieferich prime factors of \(2^a+1\) were
in the displayed pair, (17) would force 1093 to occur, with
\(W_2^+(a)\le1093\). By (14), \(182\mid a=3h\), hence
\(h\ge182\). But (17) is greater than \(2^h/(10h)\), which
already exceeds 1093 at \(h=18\) and increases thereafter.
This is a contradiction.

For base 3, the order of 11 is odd, so it cannot divide \(3^a+1\).
If all relevant Wieferich primes were in the displayed pair,
(18) would force 1006003 to occur, with
\(W_3^+(a)\le1006003\). Condition (14) then gives
\(503001\mid a\), hence \(a\ge503001\). But the weaker bound
\(3^{(a+1)/2}/(40a)\) already exceeds 1006003 at odd \(a=39\)
and increases through the odd exponents. This is again impossible.

For base 5, the order of 20771 is odd. If the displayed pair
contained all relevant Wieferich primes, (19) would force 40487
to occur, with \(W_5^+(a)\le40487\). Its order gives
\(20243\mid a\), so \(a\ge20243\). The weaker bound
\(5^{(a+1)/3}/(40a)\) already exceeds 40487 at the permitted
exponent \(a=35\) and increases as \(a\) increases by three.
This is the final contradiction.

These arguments prove the finite-set exclusions stated at the start.
They do not assume that further Wieferich primes fail to exist.

## 7. Verification record

`v7_offset_shifted_prime_powers_checks.py` uses exact integers only.
It checks the displayed small factorizations and exclusions, the six
prime/order/multiplicity certificates, the cubic nonresidues, the
integer comparisons used in the Wieferich thresholds, and representative
instances of the valuation and normalized-unit identities. Its output
is `v7_offset_shifted_prime_powers_verification.json`.

The representative identity checks are corroboration of the written
uniform proofs; they do not claim to cover an unbounded domain by
enumeration. The finite exceptional exponents are justified by the
valuation classification and prior small-index theorem, as detailed above.

Root's independent full mathematical audit passed on 2026-11-05,
including all exact inner and outer valuations, the base-three
cancellation case and normalized congruence, the signs in (1),
the radical multiplicities, and every order-based finite-set implication.
The exact checker passed all 38 recorded groups: eight small exceptions,
twelve valuation examples, three normalized-unit examples, two cubic
nonresidues, six prime/order/multiplicity certificates, and seven
integer threshold comparisons.

The composite-family peer reviewer independently audited the same note
and reported PASS on 2026-11-05, specifically confirming the valuation
balances and small-exponent coverage, the base-three scaling quotient
and factor \(F(z)\), the cubic unit sign, and all plus-Wieferich bounds
and order-parity exclusions. No mathematical correction was required.
