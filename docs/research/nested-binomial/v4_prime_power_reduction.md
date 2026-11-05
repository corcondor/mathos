# New cubic divisibility and prime-power valuation restrictions

These statements concern the original squared-index equation

\[
L:=\binom AB=X+Y,\qquad
A=\binom ij,\ B=\binom{k}{\ell},\
X=\binom{i^2}{j^2},\ Y=\binom{k^2}{\ell^2}.
\]

Set \(r=\min(B,A-B)\). The main result in Sections 1--2 holds for
**arbitrary first upper index \(i\)**, not only prime powers. This note
does not claim that the full equation has been solved. The p-adic
experiments are separate from the proofs below.

We work after the previously established endpoint exclusions, so
\(1\le j\le i-2\), \(1\le\ell\le k-1\), and \(1<B<A\).
The unconditional divisibilities in Section 1 in fact require only
the corresponding interior binomial arguments.

## 1. A primitive-denominator divisibility for all four indices

Put

\[
q=\frac{i}{\gcd(i,j)}.
\]

Then

\[
\boxed{q\mid A,\qquad q^2\mid X.} \tag{1}
\]

Indeed, write \(i=gq,j=gu\), where \(\gcd(q,u)=1\). The standard
binomial identities give

\[
uA=q\binom{i-1}{j-1},\qquad
u^2X=q^2\binom{i^2-1}{j^2-1}.
\]

Coprimality allows the factors \(u,u^2\) to be cancelled in the
corresponding divisibilities, proving (1).

Also

\[
rL=A\binom{A-1}{r-1},
\]

so \(q\mid rL\). Since \(q\mid X\), the original equation implies

\[
\boxed{q\mid rY.} \tag{2}
\]

Equivalently, \(q/\gcd(q,r)\mid Y\). This statement needs neither a
height bound nor the restriction \(\ell=1\).

## 2. A polynomial height for every solution with ell = 1

If \(\ell=1\), then \(Y=B^2\). Since \(B=r\) or \(B=A-r\), and
\(q\mid A\), one has \(B^2\equiv r^2\pmod q\). Equation (2) gives

\[
\boxed{\frac{i}{\gcd(i,j)}\mid r^3.} \tag{3}
\]

An equivalent form is \(i\mid jr^3\).

The already proved exclusion of \(M\le20\) means that \(j\ge21\)
for a remaining solution with \(\ell=1\). If \(i\ge2j\), then

\[
A\ge\binom{2j}{j},
\]

and Section 4 of `sharp_q_bounds.md` gives \(r<2j\). Hence (3) yields

\[
i\le\gcd(i,j)r^3<8\gcd(i,j)j^3\le8j^4.
\]

If instead \(i<2j\), the same upper bound is immediate. Therefore,
in both branches of the outer binomial coefficient,

\[
\boxed{\ell=1\quad\Longrightarrow\quad
i<8\gcd(i,j)j^3\le8j^4.} \tag{4}
\]

In particular,

\[
\boxed{\ell=1,\ \gcd(i,j)=1\quad\Longrightarrow\quad i<8j^3.}
\tag{5}
\]

This replaces the earlier exponential upper-index bound by a polynomial
bound on this entire family. It does not bound \(j\) itself.

For each fixed \(j,r\), equation (3) also means that \(i\) must be a
divisor of the explicit integer \(jr^3\), not an arbitrary integer up
to the height. In the branch \(i\ge2j\), the possible values of \(r\)
are confined to \(j+2\le r<2j\), with the stronger previously proved
lower bound \(r>\varphi j\).

## 3. A large prime factor of i must occur exactly cubed

Assume \(\ell=1\), \(i\ge2j\), and let \(p>j\) be a prime divisor
of \(i\). Write

\[
i=p^a w,\qquad p\nmid w.
\]

By (3), \(p\mid r\); since \(r<2j<2p\), this forces

\[
\boxed{r=p.} \tag{6}
\]

Because \(j<p\), the product formula for the inner binomial gives

\[
v_p(A)=a,\qquad
\frac{A}{p^a}\equiv w(-1)^{j-1}j^{-1}\pmod p.
\tag{7}
\]

Also \(j^2<p^2\le p^{2a}\), so
\(\binom{i^2-1}{j^2-1}\) is a p-adic unit: the bottom \(2a\) base-p
digits of \(i^2-1\) are all \(p-1\). Thus

\[
v_p(X)=2a. \tag{8}
\]

The identity

\[
\binom A p=\frac A p\binom{A-1}{p-1}
\]

has a p-adic unit as its last factor, with residue 1. Hence
\(v_p(L)=a-1\).

If \(a=1\), both \(X\) and \(B^2\) are divisible by \(p^2\),
whereas \(L\) is not even divisible by p. This is impossible.
If \(a\ge2\), then \(B=p\) or \(B=A-p\) has valuation 1, so
\(v_p(X+B^2)=2\). Therefore

\[
\boxed{a=3.} \tag{9}
\]

Dividing the original equation by \(p^2\), and reducing modulo p,
gives \(A/p^3\equiv1\pmod p\). By (7),

\[
\boxed{
v_p(i)=3,\qquad
\frac{i}{p^3}\equiv(-1)^{j-1}j\pmod p,
\qquad p=r.
} \tag{10}
\]

In particular there can be at most one prime divisor of i greater than
j. Any such prime occurs with exponent exactly 3, lies in
\(j+2\le p<2j\), and satisfies (10). Every i having a prime divisor
greater than j with a different exponent is excluded in this branch.

## 4. Prime powers: a cube-exponent restriction and a cubic residue

Assume \(\ell=1\). Let \(i=p^a\), \(0<j<i\), and write

\[
j=p^b u,\quad p\nmid u,\qquad c=a-b>0.
\]

Then

\[
v_p(A)=c,\qquad v_p(X)=2c,\qquad
\frac A{p^c}\equiv(-1)^{j-1}u^{-1}\pmod p.
\tag{11}
\]

Suppose in addition that \(r<p^c\), and write \(r=p^d v\),
\(p\nmid v\). Then \(d<c\). The bottom c base-p digits of A are
zero, so \(\binom{A-1}{r-1}\) is a p-adic unit, with residue
\((-1)^{r-1}\). Consequently

\[
v_p\binom Ar=c-d.
\]

In either outer branch, \(v_p(B)=d\), and therefore
\(v_p(X+B^2)=2d\). Equality forces

\[
\boxed{c=3d.} \tag{12}
\]

Comparing the normalized units modulo p gives

\[
\boxed{u v^3\equiv(-1)^{j+r}\pmod p.} \tag{13}
\]

These two restrictions follow from valuations and normalized residues,
not from a numerical search.

The premise \(r<p^c\) is guaranteed by \(2j\le p^c\), because this
implies \(i\ge2j\) and hence \(r<2j\). In particular, if p does not
divide j and \(j\le i/2\), then

\[
\boxed{a\equiv0\pmod3,\qquad v_p(r)=a/3.} \tag{14}
\]

Thus all prime-power exponents not divisible by 3 are eliminated in
that subfamily. For example, all \(i=p^2\), \(p\nmid j\),
\(j\le p^2/2\), \(\ell=1\) are excluded.

For an odd prime \(p\equiv1\pmod3\), (13) also requires u to be a
nonzero cubic residue modulo p, because \(\pm1\) are cubes. If u
fails that residue condition, the whole corresponding family is
excluded.

### 4.1 All prime powers whose base prime exceeds j

Combining (10) with \(i=p^a\) proves

\[
\boxed{i=p^a,\quad p>j,\quad\ell=1\quad\Longrightarrow
\text{no solution}.} \tag{15}
\]

For a=1 this is the already established prime-index theorem. For
a≥2, \(i\ge2j\), so (10) forces a=3 and
\(1\equiv(-1)^{j-1}j\pmod p\). Since \(0<j<p\), this gives
j=1 or j=p−1. The first lies in the already excluded small-M range;
the second contradicts \(r=p\ge j+2\).

## 5. Consequence for the lower branch with ell > 1

Equation (2) also yields a useful restriction without setting ell=1.
If \(B\le A/2\), then r=B, so

\[
\boxed{\frac{i}{\gcd(i,j)}\mid B Y.} \tag{16}
\]

Every prime divisor of \(B Y\) is at most \(k^2\). Prime factors
removed by \(\gcd(i,j)\) are at most j. Therefore

\[
\boxed{P^+(i)\le\max(j,k^2).} \tag{17}
\]

In the previously classified branch \(j>\ell\ge2\), one has
\(k(k-1)<20j\) and k<j, so (17) gives \(P^+(i)<21j\).
If additionally \(i-j\ge3\), then \(B<5j\), yielding
\(k(k-1)<10j\) and hence \(P^+(i)<11j\).

## 6. What remains

None of the preceding results bounds j absolutely. The prime-power
valuation restriction (12) assumes \(r<p^{a-v_p(j)}\); when r is
larger, extra carries in the binomial coefficient can change its
valuation, and the assumption must not be omitted. In particular,
prime powers in the complementary region have not been eliminated.

The separate file `v4_prime_power_experiment.py` explores those extra
carry cases at finite prime-power upper indices. Its output is
explicitly exploratory and is not used to prove (1)--(17).

The independent exact-integer consistency checks in
`v4_prime_power_verify.py` verify the divisibility identities and
valuation formulas against direct binomial coefficients on specified
finite ranges. These checks support the written proof but do not
replace its universal arguments.

## 7. Complete fixed-j certificates through j = 100 for ell = 1

The new divisor restriction supports a complete finite procedure for
every fixed \(j\ge21\), covering all first upper indices i and both
possible outer branches.

* If \(i\ge2j\), then \(j+2\le r<2j\), and i must divide \(jr^3\).
  Thus one lists the divisors of \(jr^3\) for each of these finitely
  many r, retaining i≥2j.
* If \(i<2j\), then \(j+2\le i<2j\). The bounds in
  `sharp_q_bounds.md` give r<3j for i−j≥5, r<4j for i−j=4,
  r<5j for i−j=3, and r<10j for i−j=2. The necessary conditions
  i|jr³ and 2r≤A are retained.
* For each resulting triple (i,j,r), the only values of k are r and
  A−r. A prime modulus at which the original equality fails is a
  complete certificate excluding that equation.

`v4_ell_one_divisor_certificate.py` generated and independently
verified these certificates for 21≤j≤100. There are 436,700 triples
and 873,394 distinct branch equations (six triples have A=2r).
Every equation is excluded by a prime at most 17. The largest
possible i in the enumerated divisor set is 788,059,900; this is a
derived bound, not a search cutoff.

The verifier enumerates the large-i cases differently: it takes
g|j, q|r³, i=gq, and checks gcd(i,j)=g. It checks the small-i range
by a direct r-first enumeration. Lucas residues are computed by
factorial tables in the generator and direct small binomial
coefficients in the verifier. The stored report is
`v4_ell_one_divisor_verification.json`, and the certificate SHA256 is

`644b13b32c63650e0cf12cbc9f451cdf07f03796de91d97f695b7d2e2496bdb1`.

Together with the pre-existing complete j≤20 result, this proves

\[
\boxed{\ell=1,\quad j\le100\quad\Longrightarrow\quad
\text{no solution for any valid }i,k.}
\]

This additional finite-j theorem does not assert nonexistence for
j≥101. It is a consequence of a proved structural reduction followed
by exact congruence certificates, not a finite rectangular search in
the four original variables.
