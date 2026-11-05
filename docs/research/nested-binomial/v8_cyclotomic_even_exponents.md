# Cyclotomic cofactor seven: even exponents, residue restrictions, and exact valuations

## Scope and results

The original squared-index equation remains
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
This note continues the surviving large-prime branch
\[
i=jp^3,\quad k=p,\quad \ell=1,\quad j\text{ odd},\quad
j\ge101,\quad p\ge103,\quad \frac p2<j<\frac{10p}{19},
\tag{1}
\]
where p is prime. Write
\[
A=\binom{jp^3}{j},\quad X=\binom{j^2p^6}{j^2},\quad
L=\binom Ap,\quad N=\Phi_3(p)=p^2+p+1.
\]
The equation becomes \(L=X+p^2\).

We focus on \(N=7q^a\), where q is prime. The preceding notes already
exclude \(q=3,7\), exponent \(a=1\), and all positive exponents
divisible by 3. They also prove
\[
q\mid42j^2+p-1.
\tag{2}
\]

**New conclusions in this note.**

- All positive exponents divisible by 4 are excluded.
- If \(a=2s\) is even, necessarily
  \[
  \boxed{s\text{ odd},\qquad q\equiv7\pmod{12},\qquad
  p\equiv149\pmod{168}.}
  \tag{3}
  \]
- In the even-exponent case, \(q^s\mid L\). More precisely, except
  possibly at \(q=151,211\),
  \[
  \boxed{v_q(L)=v_q(X+p^2)=s.}
  \tag{4}
  \]
  An exact formula covering those two primes is given below as well.
- For any exponent, every \(q\equiv1\pmod{12}\) must satisfy the
  explicit test
  \[
  \boxed{(-3)^{(q-1)/4}\equiv42^{(q-1)/2}\pmod q.}
  \tag{5}
  \]
  This excludes \(q=13\) and \(q=37\) for every positive exponent.

These are uniform proofs, without a chosen bound on p, q, or a.
The even-exponent argument uses only factorization in the Eisenstein
integers and small-modulus arithmetic; it does not invoke a new external
completeness theorem. The external Thomas--Mignotte theorem from v7
is needed only when combining this note with the earlier exclusion of
exponents divisible by 3.

The whole large-prime branch is still unresolved. Within \(N=7q^a\),
the remaining even exponents are restricted to \(a\equiv2,10\pmod{12}\).
The remaining odd exponents satisfy \(a\ge5\) and \(3\nmid a\).
All remaining cases must satisfy the earlier real and p-adic conditions
as well as those recorded here. No new Lean formalization is claimed.

## 1. An arithmetic theorem for seven times a square

**Theorem.** If p is a prime greater than 3 and y is a positive integer
such that
\[
p^2+p+1=7y^2,
\tag{6}
\]
then
\[
\boxed{y\equiv3\pmod4,\quad p\equiv2\pmod7,\quad
p\equiv149\pmod{168}.}
\tag{7}
\]

The integer y need not be prime or a prime power; it may be divisible
by 7. The primality of p is used to exclude divisibility by 2 and 3.

### 1.1 All conjugates and units in the square factorization

Let \(\omega^2+\omega+1=0\). As proved in the v7 note,
\(R=\mathbb Z[\omega]\) is a norm-Euclidean unique factorization
domain, with
\[
\operatorname N(r+t\omega)=r^2-rt+t^2,
\qquad R^\times=\{\pm1,\pm\omega,\pm\omega^2\}.
\]
For any integer p, the 3-adic valuation of \(p^2+p+1\) is either
0 or 1. In (6), this valuation must be even. Consequently
\(3\nmid p^2+p+1\), and \(p-\omega\) and \(p-\omega^2\)
are coprime in R: any common prime divides their difference, of norm 3.

The rational prime 7 factors as
\[
7=(2-\omega)(2-\omega^2).
\]
Its two prime factors are nonassociate. Coprimality and conjugation
ensure that exactly one lies in each of \(p-\omega,p-\omega^2\).
Their exponents in the product are \(1+2v_7(y)\); all other prime
exponents are even. After choosing the conjugate if necessary,
unique factorization therefore gives
\[
z=\varepsilon(2-\omega)(r+t\omega)^2,
\quad z\in\{p-\omega,\ (p+1)+\omega\}.
\tag{8}
\]
All cube roots of unity are squares of units, so they can be absorbed
into \(r+t\omega\). We may and do take \(\varepsilon\in\{1,-1\}\).
Taking norms gives
\[
y=r^2-rt+t^2.
\tag{9}
\]

The exact multiplication in (8) is
\[
(2-\omega)(r+t\omega)^2=C-F\omega,
\tag{10}
\]
where
\[
C=2r^2+2rt-3t^2,\qquad
F=r^2-6rt+2t^2=(r-3t)^2-7t^2.
\]
Since the coefficient of \(\omega\) in z is \(\pm1\), we have
\(F=\pm1\). The value \(-1\) is impossible modulo 7: it would
make \((r-3t)^2\equiv-1\pmod7\). Thus
\[
\boxed{F=1.}
\tag{11}
\]

Modulo 3, (11) is \(r^2-t^2\equiv1\). If \(3\nmid t\), this
would require \(r^2\equiv2\pmod3\), which is impossible. Hence
\(3\mid t\), \(r^2\equiv1\pmod3\), and \(C\equiv2\pmod3\).

For \(z=p-\omega\), the coefficient in (10) forces
\(\varepsilon=1\) and \(p=C\). For \(z=(p+1)+\omega\), it forces
\(\varepsilon=-1\) and \(p=-C-1\equiv0\pmod3\). The second case
is incompatible with p being prime greater than 3. Therefore the
factorization has the definite form
\[
\boxed{p-\omega=(2-\omega)(r+t\omega)^2,\quad p=C,\quad F=1.}
\tag{12}
\]

### 1.2 Parity gives the obstruction

Since p is odd and \(C\equiv t^2\pmod2\), t is odd. Equation (11)
modulo 2 then makes r odd. Reducing (11) modulo 8 gives
\[
3-6rt\equiv1\pmod8,
\qquad rt\equiv3\pmod4.
\]
Using (9),
\[
y=r^2-rt+t^2\equiv1-3+1\equiv3\pmod4.
\tag{13}
\]
This is the main new obstruction.

Eliminating \(r^2\) from C with (11) gives
\[
p=C=7t(2r-t)+2,
\]
so \(p\equiv2\pmod7\). We already have \(p\equiv2\pmod3\).
Since y is odd, (6) gives \(p^2+p+1\equiv7\pmod8\). Among odd
residues p modulo 8, only \(p\equiv5\) satisfies this. The three
congruences combine to \(p\equiv149\pmod{168}\), proving (7).

### 1.3 Consequences for the exponent and the second prime

If \(\Phi_3(p)=7q^{2s}\), apply the theorem with \(y=q^s\).
Equation (13) forces q to be 3 modulo 4 and s to be odd. Every prime
\(q\ne3\) dividing \(\Phi_3(p)\) is 1 modulo 3, so
\(q\equiv7\pmod{12}\). In particular, \(4\mid a\) is impossible.
Combining with v7's \(3\nmid a\) gives \(a\equiv2,10\pmod{12}\)
for every remaining even exponent.

## 2. A higher q-adic order for the outer binomial

Assume \(N=7q^{2s}\), \(q\ne3,7\). Put \(u=q^s\).
The v7 argument gives
\[
u<j<\sqrt2u,\qquad 2u+1<p<3u,
\qquad q\mid42j^2+p-1.
\tag{14}
\]
In particular, \(q\nmid j\): otherwise \(p\equiv1\pmod q\)
would contradict \(p^2+p+1\equiv0\pmod q\) with \(q\ne3\).
We also have \(q\nmid p(p-1)\).

In the centered product
\[
A=\prod_{m=1}^j\left(1+\frac{j(p^3-1)}m\right),
\qquad p^3-1=7u^2(p-1),
\]
the only index divisible by u is \(m=u\), because \(u<j<2u\).
Its correction is \(7j(p-1)u\), of valuation exactly s. Every
other correction has valuation at least \(s+1\). Thus
\[
\boxed{A\equiv1+7j(p-1)u\pmod{q^{s+1}},\qquad v_q(A-1)=s.}
\tag{15}
\]
Define the positive integer
\[
H=(A-1)/u.
\]
Then \(H\equiv7j(p-1)\pmod q\). From
\[
\binom Ap=
\frac{A(A-1)}{p(p-1)}\binom{A-2}{p-2},
\]
we obtain \(q^s\mid L\). There is also an exact valuation formula.
The low s base-q digits of \(A-2=uH-1\) are all \(q-1\), while
\(p-2\) has upper u-block 2 by (14). The low block creates no
borrow. Legendre's formula therefore gives
\[
v_q\binom{A-2}{p-2}=v_q\binom{H-1}{2}.
\]
Consequently
\[
\boxed{v_q(L)=s+v_q(H-1)+v_q(H-2).}
\tag{16}
\]
Lucas' theorem in the same blocks gives a low-block factor
\((-1)^{p-2u-2}=-1\), since p is odd. Thus the normalized residue is
\[
\boxed{
\frac L{q^s}\equiv
-\frac{H(H-1)(H-2)}{2p(p-1)}\pmod q.
}
\tag{17}
\]
All denominators in (17) are units modulo q.

### 2.1 Only two primes can raise the order above s

Put \(b=7j(p-1)\pmod q\). From (2) and
\((p-1)^2\equiv-3p\pmod q\),
\[
2b^2+14p+7\equiv0\pmod q.
\tag{18}
\]
If \(H\equiv1\) or 2 modulo q, take the corresponding
\(b\in\{1,2\}\). Eliminating p between (18) and
\(p^2+p+1\equiv0\) gives
\[
q\mid4b^4+147.
\]
For \(b=1\), this integer is the prime 151; for \(b=2\), it is
the prime 211. Hence (16) gives \(v_q(L)=s\) whenever
\(q\notin\{151,211\}\). The original equation identifies this
with \(v_q(X+p^2)\), proving (4).

### 2.2 A shorter exact expression for testing the higher congruence

The condition \(X+p^2\equiv0\pmod{q^s}\) need not be evaluated
by constructing X. Put \(n=j^2\),
\[
K=\left\lfloor\frac n{q^s}\right\rfloor<2q^s,
\qquad M=\frac{n(p^6-1)}{q^s}.
\]
Then
\[
\boxed{X\equiv\binom{M+K}{K}\pmod{q^{s+1}}.}
\tag{19}
\]
Indeed, use the product
\(X=\prod_{h=1}^n(1+n(p^6-1)/h)\). Since
\(v_q(p^6-1)=2s\) and \(q\nmid n\), every factor whose index
is not divisible by \(q^s\) is 1 modulo \(q^{s+1}\).
The retained factors, with \(h=q^sm\), give exactly
\(\prod_{m=1}^K(1+M/m)=\binom{M+K}{K}\).
Every retained factor is q-adically integral: \(v_q(M)=s\)
and \(m<2q^s\) implies \(v_q(m)\le s\).

Thus the modulus and the bottom index in (19) are derived from the
proof. The latter is less than \(2q^s<p\), whereas the original
bottom index is \(j^2\). Equations (17) and (19) give an explicit
additional necessary congruence modulo \(q^{s+1}\); they do not
establish that it always fails.

## 3. A prime-only residue obstruction for all exponents

Assume now \(N=7q^a\) for any \(a\ge1\), and
\(q\equiv1\pmod{12}\). From (2),
\[
42j^2\equiv1-p\pmod q,
\]
with both sides nonzero. Let \(\chi\) be the quadratic character
modulo q. Necessarily \(\chi(1-p)=\chi(42)\).
But \((1-p)^2\equiv-3p\), and \(p^3\equiv1\pmod q\).
Since \((q-1)/4\) is a multiple of 3,
\[
\chi(1-p)
=((1-p)^2)^{(q-1)/4}
\equiv(-3)^{(q-1)/4}\pmod q.
\]
Euler's criterion now gives exactly (5).

For q=13, the two sides of (5) are respectively \(-1,1\).
For q=37, they are respectively \(1,-1\). Thus these two prime
bases are completely excluded, regardless of the exponent. This
finite calculation illustrates a uniform prime-only obstruction;
no completeness claim about the list \(\{13,37\}\) is made.

## 4. What remains open and what was not used

The arithmetic theorem in Section 1 proves a parity obstruction for
the Pell-type equation \(p^2+p+1=7y^2\). It does not classify all of
its solutions with y a prime power. Investigating its Pell orbits did
not yield a proved factorization making every such y composite.
Composite values observed in initial Pell terms are not a proof and
are not used in any conclusion here.

The higher q-adic conditions in Section 2 have not been shown to
contradict the unique real candidate j for every p. The remaining
odd exponents, the allowed even exponents, and more general
factorizations of \(\Phi_3(p)\) therefore still require work.

The companion exact checker verifies the algebraic identities,
the complete small residue tables used above, the two exceptional
prime constants, and structured instances of the digit and product
lemmas. The uniform arguments are the written proofs above, not
extrapolations from those instances.

Two independent AI mathematical audits passed on 2026-11-05: the root
reviewer and the prime-powers reviewer each checked the full proof,
including the unit and conjugation cases with \(7\mid y\) allowed,
the odd low-block sign in (17), both exceptional prime constants, and
the integrality needed in (19). The prime-powers reviewer additionally
tested exact binomials at q=151 and q=211 with upper-block values
producing valuations s, s+1, and s+2. No correction was required in
either final audit.

The companion certificate passed all seven groups of exact structural
checks, including 60 outer-block instances and 16 product reductions.
These AI reviews and finite checks do not constitute Lean formalization
of the unbounded theorems; that status remains as stated above.
