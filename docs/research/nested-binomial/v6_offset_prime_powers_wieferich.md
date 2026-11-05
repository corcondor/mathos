# Offset three: powers of 2 and 5 require Wieferich prime factors

## Statement and scope

We retain the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

In this note ell=1 and j=i-3. Set

\[
n=i,\quad A=\binom n3,\quad
r=\min(k,A-k),\quad
X=\binom{n^2}{(n-3)^2}.
\]

Both outer branches k=r and k=A-r are included.

**Theorem.** If a solution has n=2^a, then there exists an odd prime
q dividing 2^a-1 that satisfies

\[
\boxed{2^{q-1}\equiv1\pmod{q^2}.}
\tag{1}
\]

If a solution has n=5^a, then there exists an odd prime q dividing
5^a-1 that satisfies

\[
\boxed{5^{q-1}\equiv1\pmod{q^2}.}
\tag{2}
\]

Such q are called base-2 and base-5 Wieferich primes, respectively.
The theorem is an unconditional **necessary condition**. It does
not assert that these primes do not exist, and it does not finish
either prime-power branch. Equivalently, it completely excludes
every exponent for which n-1 has no corresponding Wieferich prime
factor. No abc conjecture or unproved distribution assertion is
assumed.

In fact Section 6 proves the stronger conclusions

\[
\boxed{
\begin{aligned}
n=2^a&:\quad q\notin\{1093,3511\},\\
n=5^a&:\quad q\notin\{20771,40487\}.
\end{aligned}}
\tag{2a}
\]

These are exclusions of explicit finite sets, without assuming
that those sets exhaust the Wieferich primes.

We prove stronger quantitative restrictions below, which require
the product of the exceptional prime-power contributions to grow
exponentially with the exponent a.

## 1. Inputs and the new divisor of n-1

The preceding results give, for every remaining candidate,

\[
n\ge104,\qquad
3n<r<10n/3,\qquad
\frac n{\gcd(n,3)}\mid r^3.
\tag{3}
\]

The exact prime-power valuation calculations in
v5_offset_three_structure.md give

\[
n=2^a:\quad a=3h,\ h\ge3,\quad v_2(r)=h+1;
\tag{4}
\]

\[
n=5^a:\quad a=3d-1,\ d\ge2,\quad v_5(r)=d.
\tag{5}
\]

The new common-divisor argument also gives

\[
\boxed{D:=\frac{n-1}{\gcd(n-1,6)}\mid r^3.}
\tag{6}
\]

For completeness, (6) can be proved directly. Put t=n-1,
N=n^2, m=(n-3)^2. The pair-selection identity is

\[
\binom Nm\binom m2=\binom N2\binom{N-2}{m-2}.
\]

We have t|C(N,2), and

\[
\binom m2-6
=\frac{t(t^3-8t^2+23t-28)}2
\]

is divisible by t, since the polynomial in parentheses is even
for every integer t. Thus t|6X, so D|X. Also t|6A, hence D|A.
Using

\[
r\binom Ar=A\binom{A-1}{r-1},
\]

the original equation gives D|r k^2. Since k is r or A-r and
D|A, this implies D|r^3. In particular,

\[
R:=\operatorname{rad}(D)\mid r.
\tag{7}
\]

Here rad means the product of the distinct prime divisors.

## 2. The required elementary lifting lemma

Let q be an odd prime and let z=1+q^e c, where e>=1 and q does
not divide c. The binomial expansion gives

\[
v_q(z^q-1)=e+1.
\tag{8}
\]

Indeed, the linear term has valuation e+1. For 2<=j<=q-1,
the j-th term has valuation at least 1+je>=e+2, and the last
term has valuation qe>=e+2. Therefore no cancellation changes
the valuation of the linear term.

If q does not divide u, the same expansion gives
v_q(z^u-1)=e. Factoring an arbitrary positive exponent into its
q-power part and a q-coprime part, then iterating (8), proves

\[
\boxed{v_q(z^s-1)=v_q(z-1)+v_q(s).}
\tag{9}
\]

Now let b be coprime to q and let f=ord_q(b). If q|b^a-1,
then f|a and f|(q-1), so q does not divide f. Define

\[
e_q:=v_q(b^f-1).
\]

Equation (9) gives

\[
\boxed{
v_q(b^a-1)=e_q+v_q(a),\qquad
v_q(b^{q-1}-1)=e_q.
}
\tag{10}
\]

Thus e_q>=2 is exactly the Wieferich condition. If q is not
Wieferich, the repeated occurrences of q in b^a-1 are completely
accounted for by the q-part of a.

## 3. Isolating the exceptional multiplicities

For b in {2,5}, define

\[
W_b(a)=
\prod_{\substack{q\mid b^a-1\\q\ {\rm odd\ prime}}}
q^{\,e_q-1},
\qquad e_q=v_q(b^{\operatorname{ord}_q(b)}-1).
\tag{11}
\]

All exponents are nonnegative. In particular,

\[
W_b(a)=1
\quad\Longleftrightarrow\quad
b^a-1\text{ has no odd base-}b\text{ Wieferich prime factor}.
\tag{12}
\]

For b=2, the integer 2^a-1 is odd, so (10) gives

\[
\boxed{
\frac{2^a-1}{\operatorname{rad}(2^a-1)}
\mid a\,W_2(a).
}
\tag{13}
\]

For b=5, one additionally has

\[
v_2(5^a-1)=2+v_2(a).
\tag{14}
\]

To see this, when a is odd the quotient
(5^a-1)/(5-1) is a sum of an odd number of odd terms. Each
doubling of a multiplies 5^a-1 by 5^a+1, whose 2-adic valuation
is one because 5^a=1 modulo 4. This proves (14).
Combining it with (10) at the odd primes gives

\[
\boxed{
\frac{5^a-1}{\operatorname{rad}(5^a-1)}
\mid 2a\,W_5(a).
}
\tag{15}
\]

In (13) and (15) the quotient of the left side by W_b(a) is
not merely bounded: it is explicitly a divisor of a or 2a.

## 4. Powers of two

By (4), write n=2^(3h), h>=3. We first observe that

\[
\operatorname{rad}(D)=\operatorname{rad}(n-1).
\tag{16}
\]

The integer n-1 is odd, so only removal of a factor 3 from n-1
could affect its radical. If 3|n-1, then h is even. Applying
(10) with q=3, b=2 and ord_3(2)=2 gives

\[
v_3(n-1)=1+v_3(3h)=2+v_3(h)\ge2.
\]

Dividing by gcd(n-1,6)=3 therefore leaves a factor 3, proving
(16).

Because (16) is odd and (4) gives the exact 2-adic valuation of
r, equations (7), (13) imply

\[
r\ge2^{h+1}\operatorname{rad}(n-1)
\ge \frac{2^{h+1}(n-1)}{3h\,W_2(3h)}.
\]

Combining this with r<10n/3 yields the quantitative obstruction

\[
\boxed{
W_2(3h)>
\frac{2^{h+1}}{10h}\bigl(1-2^{-3h}\bigr).
}
\tag{17}
\]

For h>=5, the right side is greater than one: at h=5 it is
(64/50)(1-1/32768)>1, and both 2^(h+1)/h and 1-2^(-3h)
increase thereafter. Therefore W_2(3h)>1 for every such
h, proving the necessary Wieferich condition in this range.

The remaining h=3,4 are excluded directly from (6) and (4):

| h | n | D | rad(D) | A necessary divisor of r |
|---:|---:|---:|---:|---:|
| 3 | 512 | 511=7*73 | 511 | 16*511=8176 |
| 4 | 4096 | 1365=3*5*7*13 | 1365 | 32*1365=43680 |

In both rows the final entry is greater than 10n/3. Smaller
exponents, and exponents not divisible by three, were already
excluded by the stated inputs. This completes the proof of (1).

## 5. Powers of five

By (5), a=3d-1, d>=2; in particular 3 does not divide a.
From (14), n-1 has at least two factors of 2, so division by
gcd(n-1,6) never removes the prime 2 from its radical.

If a is odd, 3 does not divide n-1. If a is even, (10) gives
v_3(5^a-1)=1+v_3(a)=1. Define

\[
\epsilon_a=
\begin{cases}
1,&a\text{ odd},\\
3,&a\text{ even}.
\end{cases}
\]

It follows that

\[
R=\operatorname{rad}(D)
=\frac{\operatorname{rad}(n-1)}{\epsilon_a}.
\tag{18}
\]

Since R is prime to 5, equations (5), (7), (15), (18) imply

\[
r\ge5^d R
\ge\frac{5^d(n-1)}{2a\epsilon_a W_5(a)}.
\]

Using r<10n/3, we obtain

\[
\boxed{
W_5(a)>
\frac{3\cdot5^{(a+1)/3}}{20a\epsilon_a}
\bigl(1-5^{-a}\bigr).
}
\tag{19}
\]

For every allowed a>=11, even the weaker right side
5^((a+1)/3)(1-5^(-a))/(20a) is greater than one. This holds at
a=11 because 625(1-5^(-11))>220. When a increases by three,
the factor 5^((a+1)/3)/a increases by 5a/(a+3)>1.
Thus W_5(a)>1 for all these exponents.

The only remaining allowed exponents are a=5,8. To handle
them, use c_3(z)=product q^ceil(v_q(z)/3), so z|r^3 implies
c_3(z)|r. Equation (6) gives the following exact exclusions.

| a | n | D | c_3(D) | A necessary divisor of r |
|---:|---:|---|---:|---:|
| 5 | 3125 | 1562=2*11*71 | 1562 | 25*1562=39050 |
| 8 | 390625 | 65104=2^4*13*313 | 16276 | 125*16276=2034500 |

The final entry exceeds 10n/3 in both rows. This proves (2)
for all exponents, with no unexamined finite range.

## 6. Two explicit Wieferich primes cannot suffice in either base

The following four primes have the exact multiplicative orders
and multiplicities shown here:

| Base b | q | ord_q(b) | v_q(b^ord_q(b)-1) |
|---:|---:|---:|---:|
| 2 | 1093 | 364 | 2 |
| 2 | 3511 | 1755 | 2 |
| 5 | 20771 | 10385 | 2 |
| 5 | 40487 | 40486 | 2 |

The table is verified by finite exact arithmetic: primality of
the four listed integers, the order tests at every prime divisor
of the proposed order, and modular exponentiation modulo q^2
and q^3. It does not rely on a search claim about all primes.

Suppose a solution with n=2^(3h) had no base-2 Wieferich prime
factors outside {1093,3511}. The preceding theorem requires at
least one of these primes to occur. Since their orders must
divide 3h, this forces h>=364. On the other hand, their exact
multiplicities in the table give

\[
W_2(3h)\le1093\cdot3511=3837523.
\]

For h>=32, the lower bound (17), using
1-2^(-3h)>1/2, is already greater than

\[
\frac{2^{33}}{640}>3837523.
\]

The function 2^(h+1)/h increases here, so the contradiction
holds for every h>=364. This proves the base-2 assertion in
(2a).

Similarly, if the only base-5 Wieferich factors of 5^a-1 were
20771 and 40487, at least one would occur, forcing a>=10385.
The table gives

\[
W_5(a)\le20771\cdot40487=840955477.
\]

For allowed exponents a>=59, equation (19), together with
epsilon_a<=3 and 1-5^(-a)>1/2, already gives a lower bound
greater than

\[
\frac{5^{20}}{40\cdot59}>840955477.
\]

The bound increases along a=3d-1. This contradicts a>=10385
and proves the base-5 assertion in (2a).

More generally, the same calculation can rule out any proposed
finite collection of exceptional factors when its multiplicity
product is too small at the first exponent allowed by their
orders. The assertions here concern exactly the displayed
sets; no statement about current completeness of known
Wieferich-prime lists is needed.

## 7. A general fixed-prime version

The same mechanism is not limited to bases two and five.
Let P>=7 be an odd prime, n=P^a, and assume the necessary
valuation class a=3d, v_P(r)=d from the v5 proof.
Define W_P(a) by (11), with b=P, and put

\[
C_P=2^{v_2(P^2-1)-2}.
\]

The elementary 2-adic lifting argument gives

\[
\frac{P^a-1}{\operatorname{rad}(P^a-1)}
\mid C_P\,a\,W_P(a).
\tag{20}
\]

For odd a, its 2-part follows from v_2(P^a-1)=v_2(P-1).
For even a, repeated doubling gives
v_2(P^a-1)=v_2(P^2-1)+v_2(a)-1. These imply (20);
the odd-prime parts follow from (10).

Passing from rad(n-1) to rad(D) loses at most a factor six.
Thus a solution would force

\[
\boxed{
W_P(3d)>
\frac{P^d}{60C_Pd}\bigl(1-P^{-3d}\bigr).
}
\tag{21}
\]

For each fixed P, this tends to infinity with d. Hence every
sufficiently large exponent in this branch requires an odd
base-P Wieferich prime factor of P^(3d)-1, and in fact requires
an exponentially growing product of exceptional contributions.
No uniform claim about the distribution or nonexistence of
such primes is made.

## 8. Meaning, checks and references

These proofs show that ordinary repeated factors arising from
the exponent a cannot suffice in the remaining large prime
powers. Additional repeated factors arising from the Wieferich
condition are necessary. Equations (17), (19), (21) quantify
how large their combined contribution must be.

The proof is ordinary exact mathematics, not a Lean formalization.
It uses the previously proved gap and prime-power valuation
classes, and the new n-1 divisor, whose short proof is included.
It does not invoke an abc conjecture, a probabilistic model,
or a finite search claimed to cover unbounded exponents.

The accompanying script v6_offset_prime_powers_checks.py
checks the four explicit divisor exclusions, the lifting
identities on a stated small set of examples, and exact
Wieferich examples. These checks are consistency checks of
the formulas; the universal statements are proved above.

For the standard definition of base-b Wieferich primes, see
Yuchen Ding, "Non-Wieferich primes under the abc conjecture",
C. R. Acad. Sci. Paris, Ser. I 357 (2019), 483–486,
DOI 10.1016/j.crma.2019.05.007, Introduction:
https://www.numdam.org/item/CRMATH_2019__357_6_483_0.pdf

The cited paper's distribution results assume abc. No such
result or assumption is used in the deductions of this note.

### Independent audit status

The v6_offset_composite reviewer independently audited the
self-contained lifting proof, all valuation and radical
identities, both quantitative bounds, the four small-exponent
exclusions, and the general fixed-prime extension; that audit
passed without mathematical correction.

The same reviewer separately audited Section 6 after it was
added. Primality, exact orders, and the multiplicity two were
checked independently, including all proper divisors of the
proposed orders. The two finite-set upper bounds and the
corresponding lower-bound contradictions passed. In particular,
the extra multiplicity caused by q dividing a is already
accounted for outside W and does not invalidate the displayed
finite-set product bounds.

The root reviewer also checked the main necessary-condition
mechanism. The companion exact verification script completed
successfully; its output is v6_offset_prime_powers_verification.json.
