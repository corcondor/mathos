# Recovering missing prime factors from the equation itself

## Scope and notation

The equation is unchanged:

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns \(\ell=1,\ j=i-3\). Put

\[
n=i,\quad A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),\quad G=\gcd(A,X),\quad S=A/G.
\]

The established branch reductions give \(n\ge104\),
\(3n<r<10n/3\), and, for \(n\ge1024\),

\[
r<3n+\frac{3n}{4\log n}.
\tag{1}
\]

The v9 result is \(S\ge13\), with
\(S\mid(n-2)/\gcd(n-2,6)\). We strengthen the invariant to which
the same bound applies. The new divisor need not divide X: the
equation itself recovers prime factors missing from the ordinary gcd.

For every prime \(p\mid A\), write

\[
\alpha_p=v_p(A),\qquad x_p=v_p(X),
\qquad
d_p=\begin{cases}
\max(\alpha_p-3x_p/2,0),&x_p\text{ even},\\
0,&x_p\text{ odd}.
\end{cases}
\]

Define

\[
\boxed{E=\prod_{p\mid A}p^{d_p},\qquad B=A/E.}
\tag{2}
\]

All exponents in (2) are nonnegative integers. The main conclusions
for any solution in this branch are

\[
\boxed{G\mid B\mid A,\qquad B\mid r^3,\qquad
E\mid S\mid\frac{n-2}{\gcd(n-2,6)},}
\tag{3}
\]

\[
\boxed{E\ge13,\qquad \log n<128E,\qquad n<2^{192E}.}
\tag{4}
\]

The proof covers both outer branches \(k=r\) and \(k=A-r\).
There is no restriction on the number of prime divisors of n-2.
It does not solve the whole original equation.

Section 7 also improves the height bound for **every** fixed cofactor,
without a large-prime or small-cofactor restriction:

\[
\boxed{n=wp^a+2\text{ is a solution index}
\Longrightarrow
\log n<128\frac{w}{\gcd(w,6)},\qquad
n<2^{192w/\gcd(w,6)}.}
\tag{4a}
\]

## 1. A polynomial congruence containing more information than the gcd

The binomial identity

\[
r\binom Ar=A\binom{A-1}{r-1}
\]

and the original equation imply \(A\mid r(X+k^2)\).
Since \(k\equiv r\) or \(-r\pmod A\), both branches give

\[
\boxed{A\mid r(X+r^2).}
\tag{5}
\]

Reducing (5) modulo G gives the already known \(G\mid r^3\).
Retaining the whole modulus A is stronger.

### Prime-local recovery lemma

More generally, let A, X, r be positive integers satisfying (5).
Fix \(p\mid A\), and abbreviate
\(\alpha=v_p(A), x=v_p(X), e=v_p(r)\).

If \(3e<\alpha\), then necessarily

\[
\boxed{x=2e,\qquad
\left(\frac r{p^e}\right)^2
\equiv-\frac X{p^{2e}}\pmod{p^{\alpha-3e}}.}
\tag{6}
\]

Indeed, if \(x\ne2e\), the two summands in \(X+r^2\) have
unequal valuations, so

\[
v_p\bigl(r(X+r^2)\bigr)=e+\min(x,2e)\le3e<\alpha,
\]

contradicting (5). When \(x=2e\), divide (5) by \(p^{3e}\)
to obtain the congruence in (6).

In particular, **an odd valuation of X forces the entire p-part of
A into r cubed**, regardless of how much is missing from gcd(A,X).

If x is odd, the same unequal-valuation calculation gives the
slightly stronger explicit bound

\[
\boxed{e\ge\max\!\left(\lceil\alpha/3\rceil,\alpha-x\right).}
\tag{7}
\]

If x is even, (6) gives

\[
e\ge\min\!\left(\lceil\alpha/3\rceil,x/2\right).
\tag{8}
\]

These elementary statements use only (5); there is no use of a
probabilistic model or an asymptotic estimate.

## 2. The recovered divisor and the smaller missing part

For odd x, (7) proves \(p^\alpha\mid r^3\), which is the p-part
of B in (2). For even x, (8) proves

\[
p^{\min(\alpha,3x/2)}\mid r^3,
\]

again exactly the p-part of B. Therefore \(B\mid r^3\).

The exponent of p in G is \(\min(\alpha,x)\). It is at most
the exponent in B: for even x use \(3x/2\ge x\), and for odd x
B contains \(p^\alpha\). This proves \(G\mid B\mid A\).
Consequently \(E=A/B\mid A/G=S\), establishing (3).

For example, if a prime contributes \(p^b\) to the old defect S,
then the new defect can remove it completely. A large old S need
not mean that a large new E remains. Only primes for which
\(x_p\) is even and \(3x_p<2\alpha_p\) can remain in E.

## 3. Why the v8 height bound and v9 certificates apply unchanged

The following general transfer statement is useful. Suppose C is
any positive integer such that

\[
G\mid C\mid A,\qquad C\mid r^3,
\qquad H=A/C.
\tag{9}
\]

Then \(H\mid S\mid n-2\), and

\[
U=r^3/C\in\mathbb Z_{>0},\qquad
162H<U<229H,
\qquad6Hr^3=Un(n-1)(n-2).
\tag{10}
\]

The v8 integer-separation argument uses only this integral quotient,
the binomial expression for A, and the upper gap (1). It gives
\(\log n<128H\), hence \(n<2^{192H}\).
In particular it does **not** use \(C\mid X\).

For clarity, if \(\log n\ge128H\), the exact estimates in
`v8_gcd_defect_height.md` give

\[
162H<U<162H
\left(1+\frac1{512H}\right)^3
\left(1+\frac1{2^{18}H}\right)<162H+1,
\]

contradicting integrality. All estimates and the rational endpoint
constant remain the same when H replaces S.

The complete v9 continued-fraction calculation excludes every
integer point with

\[
1\le H\le12,\quad162H<U<229H,\quad
6Hr^3=U(n^3-3n^2+2n),
\]

\[
n\ge104,\quad n<2^{192H},\quad3n<r<10n/3,
\quad H\mid n-2.
\]

Its proof and its two implementations deliberately do not recompute
the actual gcd. Thus it proves \(H\ge13\) under (9).
Apply this with \(C=B,H=E\) to obtain (4). No new CF prefix,
curve computation, or completeness assumption is required.

The reused finite result comprises all 5,214 curves for H=1,...,12;
the primary verifier and separate reproduction both returned no
surviving point. The actual v9 outputs and complete certificates
remain in the previous version's files.

## 4. A further recovery from local square obstructions

Call p critical when \(d_p>0\). Write

\[
x_p=2t_p,\qquad\alpha_p=3t_p+d_p.
\]

For a critical prime, (5) gives the exact alternatives

\[
\boxed{
\begin{array}{ll}
v_p(r)=t_p,&
(r/p^{t_p})^2\equiv-X/p^{2t_p}\pmod{p^{d_p}},\\[3pt]
v_p(r)\ge t_p+d_p.&
\end{array}}
\tag{11}
\]

To prove completeness, values \(e<t_p\) give valuation
\(3e<\alpha_p\) in (5), impossible. Values \(e>t_p\) give
valuation \(e+2t_p\), so \(e\ge t_p+d_p\). The equality
case is precisely the first congruence in (11).

If the unit \(-X/p^{2t_p}\) is not a square modulo \(p^{d_p}\),
the first alternative is impossible. The second puts all of
\(p^{\alpha_p}\) into \(r^3\). Hence define

\[
E_{\rm sq}=
\prod_{\substack{p\text{ critical}\\
-X/p^{x_p}\text{ is a square mod }p^{d_p}}}p^{d_p},
\qquad B_{\rm sq}=A/E_{\rm sq}.
\tag{12}
\]

Then

\[
\boxed{G\mid B\mid B_{\rm sq}\mid A,\quad
B_{\rm sq}\mid r^3,\quad E_{\rm sq}\mid E,\quad
E_{\rm sq}\ge13,\quad\log n<128E_{\rm sq}.}
\tag{13}
\]

For odd p, the unit-square test modulo \(p^d\) is equivalent to
the test modulo p. A nonzero root lifts uniquely at each step:
in \((z+c p^h)^2\), the coefficient \(2z\) is invertible
modulo p. For p=2, a unit is a square modulo \(2^d\) exactly
when it is 1 modulo 2 for d=1, 1 modulo 4 for d=2, or 1 modulo 8
for d>=3. The last sufficiency follows by adjusting an odd root
by \(2^{h-1}\) to toggle the next square digit. These are finite,
exact local tests; there is no numerical tolerance.

## 5. Simultaneous restrictions on all critical primes

Define the least positive integer whose cube is divisible by B:

\[
F=c_3(B)=\prod_{p\mid B}p^{\lceil v_p(B)/3\rceil}.
\]

Equation (3) gives \(F\mid r\). Write \(r=Fu\).
At a critical prime p, the exponent of p in F is exactly t_p.
Define the unit modulo \(p^{d_p}\)

\[
\lambda_p\equiv
\frac{X}{p^{2t_p}}
\left(\frac F{p^{t_p}}\right)^{-2}
\pmod{p^{d_p}}.
\]

Substituting r=Fu in (5), cancelling the p-unit and the factor
\(p^{3t_p}\), gives

\[
u(u^2+\lambda_p)\equiv0\pmod{p^{d_p}}.
\]

Since \(\lambda_p\) is a unit, the two factors cannot both be
divisible by p. Consequently

\[
\boxed{u\equiv0\pmod{p^{d_p}}
\quad\text{or}\quad
u^2\equiv-\lambda_p\pmod{p^{d_p}}.}
\tag{14}
\]

For odd p, the quadratic has at most two roots at every prime-power
precision. For p=2 it has at most four: for any two odd roots z,y,
the product (z-y)(z+y) is divisible by \(2^d\), while one of its
two factors has 2-adic valuation exactly one. Thus
\(y\equiv z\) or \(-z\pmod{2^{d-1}}\), giving at most four
possibilities modulo \(2^d\). The d=1 case is immediate.

The Chinese remainder theorem therefore places u in at most

\[
\boxed{3^{\omega_{\rm odd}(E)}
\times\begin{cases}1,&2\nmid E,\\5,&2\mid E\end{cases}}
\tag{15}
\]

residue classes modulo E. This treats the prime factors
simultaneously. Here \(\omega_{\rm odd}\) counts distinct odd
prime factors; for E=1 the single congruence class is understood.

Moreover \(F^3\ge B\), so (10) gives

\[
\boxed{u^3\le r^3/B<229E,\qquad u<(229E)^{1/3}.}
\tag{16}
\]

Thus the residue classes need only be intersected with a short
interval depending on E, rather than an interval proportional to n.
The conclusion is a necessary-condition reduction, not a claim that
every such intersection is empty.

### The deficit remaining after the zero-root choices

At a critical prime, (14) makes u either a p-unit or divisible by
the whole \(p^{d_p}\). In the first case \(v_p(r)=t_p\), and
the exponent of p in \(A/\gcd(A,r^3)\) is d_p. In the second,
the exponent is zero. Noncritical primes already divide r cubed
to their full exponent in A. Therefore

\[
\boxed{\frac A{\gcd(A,r^3)}=\frac E{\gcd(E,u)}.}
\tag{17}
\]

Since \(G\mid\gcd(A,r^3)\), the transfer in Section 3 applies
once more:

\[
\boxed{
\frac E{\gcd(E,u)}\ge13,
\qquad\log n<128\frac E{\gcd(E,u)}.
}
\tag{18}
\]

This additional test prevents the factors assigned to the zero
classes in (14) from being counted as remaining obstructions.
If Z is their product, then Z=gcd(E,u), Z divides u, and (16)
also gives \(Z^2<229(E/Z)\).

## 6. Fixed cofactors: only a short list of small exponents can remain

Write \(n=wp^a+2\), with \(p\nmid w\) and \(p^a>4w\).
Use the v9 definitions

\[
D_w=\binom{6w}{2w}/\gcd\!\left(\binom{6w}{2w},6\right),
\qquad c_w=w/\gcd(w,6),\qquad b=v_p(D_w).
\]

The v9 exact formula says \(v_p(S)=b\), and the p-free part
of S divides c_w. Set \(\alpha=v_p(A)\), so

\[
\alpha=a-\mathbf1_{p=3}.
\]

If b=0, p contributes nothing to E. If b>0, the equality
\(\min(\alpha,v_p(X))=\alpha-b\) forces

\[
v_p(X)=\alpha-b.
\]

By (2), p contributes to E if and only if

\[
\boxed{\alpha\in\{b,b+2,b+4,\ldots,3b-2\}.}
\tag{19}
\]

In that event its exact exponent in E is

\[
\boxed{v_p(E)=\frac{3b-\alpha}{2}.}
\tag{20}
\]

There are only b possible values of alpha. In particular,
\(b=1\) leaves only \(\alpha=1\); all larger exponents of
that prime recover completely. This is substantially stronger than
retaining \(p^b\) in S at every exponent.

At all other primes E divides S, whose p-free part divides c_w.
Thus

\[
\boxed{E\mid c_w p^{v_p(E)}.}
\tag{21}
\]

If \(c_w\le12\), (4) and (21) force \(v_p(E)>0\).
Therefore p must divide the fixed integer D_w, and its exponent
must belong to (19). This gives a finite prime/exponent list,
with the complementary small-power range \(p^a\le4w\).

### A polynomial bound for every cofactor with c_w<=12

The v9 floor-sum argument gives
\(p^{v_p\binom{6w}{2w}}\le6w\). Hence, when b>0,

\[
p^b\le\begin{cases}3w,&p=2,\\2w,&p=3,\\6w,&p\ge5.\end{cases}
\]

Using \(\alpha\le3b-2\) from (19),

\[
p^a\le\begin{cases}
(3w)^3/4,&p=2,\\
(2w)^3/3,&p=3,\\
(6w)^3/p^2\le216w^3/25,&p\ge5.
\end{cases}
\]

The largest constant is 216/25. The small-power range obeys
\(n\le4w^2+2\le216w^4/25+2\). Therefore

\[
\boxed{
c_w\le12,\quad n=wp^a+2\text{ is a solution index}
\quad\Longrightarrow\quad
n\le\frac{216}{25}w^4+2<9w^4+2.
}
\tag{22}
\]

This also covers a prescribed w divisible by p: write
\(w=p^h w_0\), apply the result to \(w_0p^{a+h}+2\), and
use \(w_0\le w\) and \(c_{w_0}\le c_w\). The latter follows
because multiplication by a prime power increases gcd(w,6) by no
more than the factor by which w increases.

There are exactly thirty positive cofactors satisfying c_w<=12:

\[
1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,21,22,24,
27,30,33,36,42,48,54,60,66,72.
\]

The list is finite because w<=6c_w<=72; testing those 72 elementary
gcd values gives exactly the displayed list. This note proves the
reduction and bound, not the emptiness of every resulting finite list.

## 7. A linear-in-cofactor height bound for every prime base

The same argument gives a stronger general result than merely
the small-cofactor conclusion (22). Let w be any positive integer,
p any prime, and a>=1. A solution index n=wp^a+2 necessarily satisfies

\[
\boxed{\log n<128c_w,\qquad n<2^{192c_w},
\qquad c_w=w/\gcd(w,6).}
\tag{23}
\]

There is no hypothesis c_w<=12 or p>6w in (23).

First assume p does not divide w and put q=p^a. If q>4w and
p contributes nothing to E, (21) gives E|c_w, and (4) immediately
gives log n<128c_w.

If q>4w and p does contribute to E, the finite exponent list (19)
still applies: its proof never assumed c_w<=12. The three
prime-base estimates preceding (22) therefore give

\[
n\le216w^4/25+2<16w^4.
\tag{24}
\]

The last strict inequality is equivalent to 184w^4-50>0,
which follows from w>=1. If instead q<=4w, then
\(n\le4w^2+2<16w^4\), so the same simpler bound holds.
For either of these cases,

\[
\log n<4\log2+4\log w
<4+4(w-1)=4w\le24c_w<128c_w.
\tag{25}
\]

Here log2<1 follows from e>2, and log w<=w-1 follows, for example,
by integrating 1/t<=1 from 1 to w. Also w/gcd(w,6)=c_w and
gcd(w,6)<=6 justify 4w<=24c_w.

If a prescribed w is divisible by p, normalize w=p^h w_0
as after (22), apply the result to w_0 and exponent a+h, and use
c_(w_0)<=c_w. This proves the logarithmic claim for all w,p,a.
The already established elementary comparison e^2<8 gives
e^(128c_w)<2^(192c_w), completing (23).

Thus the v9 height coefficient 768w^2/gcd(w,6) can be replaced
by 128w/gcd(w,6), uniformly for all prime bases and all exponents.

### Every exact prime-power factor has a logarithmically large complement

For a general solution index, put N=n-2. Choose any prime p|N,
take the exact prime-power factor q=p^v_p(N), and let w=N/q.
Equation (23) gives

\[
\boxed{\frac{w}{\gcd(w,6)}>\frac{\log n}{128}.}
\tag{26}
\]

Equivalently,

\[
\boxed{
q<\frac{128N}{\gcd(w,6)\log n}
\le\frac{128N}{\log n},\qquad
Q_{\max}(n-2)<\frac{128(n-2)}{\log n}.
}
\tag{27}
\]

This improves the earlier square-root-of-logarithm scale to a
logarithmic scale. For the two displayed bounds with gcd discarded,
the new numerical upper bound is smaller once log n>64/3;
no uniform comparison in the opposite small-log range is asserted.
The exact general height theorem (23) itself improves the earlier
fixed-cofactor coefficient by a factor 6w for every w.

## 8. Verification and formalization boundary

The companion `v10_valuation_recovery_checks.py` uses exact integer
congruences to test the local recovery lemma, including odd x,
both critical alternatives, p=2, and square obstructions at higher
precision. It also checks simultaneous mixed-prime constructions,
the CRT classes, identity (17), and the fixed-cofactor exponent rule.
These finite examples support the uniform written proof; they are
not used to extrapolate it.

The v9 CF computation is reused through the explicitly audited
transfer in Section 3. This note does not claim a new execution of
those 5,214 curves, and does not need a larger range of CF certificates.

### Executed Lean verification of the general recovery core

The v10 source `v10_formal/ValuationRecovery.lean` has been compiled
with Lean 4.35.0 and the pinned mathlib revision, with exit code 0.
The actual run is recorded in `v10_formal/valuation_kernel_check.json`
and `v10_formal/valuation_kernel_check.log`; the recorded source hash
matches the independently reviewed file.
Unlike the earlier finite arithmetic certificates, these are
universally quantified structural theorems. The following mapping
states their actual scope:

| Mathematical statement | Executed Lean theorem |
|---|---|
| (5), from the outer equation, both branches | `original_cubic_divisibility` |
| If \(3e<\alpha\), then \(x=2e\) | `low_cube_valuation_forces_equality` |
| Odd x recovers the full p-part into r cubed | `odd_valuation_recovers_full_cube` |
| Even x recovers exponent \(\min(\alpha,3x/2)\) | `even_valuation_recovers_cube_part` |
| The recovered prime power divides r cubed | `recovered_prime_power_dvd_cube` |
| The last conclusion for the actual outer equation | `original_recovers_prime_power` |
| Critical exponents satisfy \(e=t\) or \(e\ge t+d\) | `critical_exponent_dichotomy` |
| The finite list \(\alpha=b+2t,\ 0\le t<b\) | `critical_exponent_parametrization` |

The prime is assumed prime, X and r are nonzero where valuations
are used, and the original-equation application assumes k<=A.
These hypotheses hold in the branch considered here. The note's
author independently reviewed the Lean statements, their proofs,
and their correspondence to the mathematics and reported PASS.

The Lean source uses no `sorry`, `native_decide`, or added axioms.
The normalized square congruence, the global product B and its
divisor chain, CRT reconstruction, the transfer of the CF exclusion,
the quartic cofactor bound, and the general height bound in Section 7
are written proofs here; they are not
claimed to have been formalized by this Lean source. The original
four-variable equation and the unrestricted mixed-factor branch
remain unresolved.

The fixed-cofactor reviewer independently audited the whole written
note and reported PASS on 2026-11-05, including the odd-valuation
bound, both critical branches, the 2-adic unit-square criterion,
the CRT reconstruction and root counts, identity (17), the CF
transfer, normalization, and the quartic bound. The same reviewer
also checked the correspondence with the executed Lean source.
The root reviewer separately audited the whole note and also
reported PASS, specifically checking the odd-valuation lower bound,
2-adic lifting, CRT zero and unit branches, the actual-deficit
identity (17), and the fact that the v9 verifier does not impose an
unrecorded equality with the original gcd. These are independent
AI audits, not external peer review.

After the main audit, root proposed the further general height
bound in Section 7. The note's author independently checked its
two q>4w alternatives, the small-q case, normalization, and every
constant in (24)-(27), and confirmed the strengthened theorem.
The checker was extended to test the polynomial bound on every
sample with a surviving critical prime, without restricting c_w.
The fixed-cofactor and cyclotomic reviewers also independently
audited the added Section 7 and reported PASS, including w=1,
the normalization, and the exact prime-power-factor consequence.
