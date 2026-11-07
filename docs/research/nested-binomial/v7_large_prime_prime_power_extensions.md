# Large-prime branch: cubic-exponent exclusion and prime-power digit blocks

## Scope and conclusions

The original equation is unchanged:
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
In the surviving lower \(\ell=1\) branch with a prime \(p>j\) dividing \(i\),
the preceding notes prove
\[
i=jp^3,\qquad k=p,\qquad j\text{ odd},\qquad
j+2\le p<2j,\qquad j\ge101,\quad p\ge103.
\tag{1}
\]
Set
\[
A=\binom{jp^3}{j},\quad X=\binom{j^2p^6}{j^2},\quad
L=\binom Ap,\quad N=\Phi_3(p)=p^2+p+1.
\]
The equation in this branch is \(L=X+p^2\). We use the v6 bound
\[
\frac p2<j<\frac{10p}{19}.
\tag{2}
\]

There are two new results.

1. If \(N=7q^a\), with \(q\ne3,7\) prime and \(a\ge1\), every
   surviving solution must satisfy \(q\mid42j^2+p-1\). This extends the
   v6 digit obstruction from exponent one to every positive exponent.
   The modulus is **q**, not \(q^a\).
2. Let \(t\ge2\) and suppose \(c=t^2+t+1\) is prime and
   \(c\equiv4\) or \(7\pmod9\). The equation
   \[
   x^2+x+1=cy^3,\qquad x\in\mathbb Z,\quad y\in\mathbb Z_{>0},
   \]
   has only \((x,y)=(t,1),(-t-1,1)\). In particular, no value
   \(\Phi_3(p)=cq^a\) with \(3\mid a\), \(a>0\), is possible for
   **any** prime \(q\), including \(q=c\).

The second result applies, for example, to \(c=7,13,31,43\), obtained
from \(t=2,3,5,6\). It invokes the proved Thomas--Mignotte theorem on
simplest cubic Thue equations, cited precisely in Section 2. The algebraic
reduction is proved here. There is no unbounded search and no assumed
upper bound on the variables.

The v6 exclusion of \(N=7q\), combined with these results, leaves within
the form \(N=7q^a\) only exponents \(a\ge2\) with \(3\nmid a\), still
subject to the digit condition and all earlier necessary conditions.
Neither this residual form nor the whole original equation is solved.
These notes are not Lean formalizations.

## 1. The digit obstruction for every exponent in N=7q^a

Assume
\[
N=7q^a,\quad q\ne3,7\text{ prime},\quad a\ge1,
\quad D=q^a.
\tag{3}
\]
Every prime divisor of \(\Phi_3(p)\) other than 3 is 1 modulo 3,
as proved in v6. Hence \(q\ge13\). The bounds (2) imply
\[
\boxed{D<j^2<2D.}
\tag{4}
\]
For the first inequality use
\(p^2/4>(p^2+p+1)/7\), equivalent to
\(3p^2-4p-4>0\). For the second use
\(100p^2/361<2(p^2+p+1)/7\), since \(700<722\).

### 1.1 The outer binomial is zero modulo q

The exact centered product is
\[
A=\prod_{m=1}^j\left(1+\frac{j(p^3-1)}m\right),
\qquad p^3-1=7D(p-1).
\tag{5}
\]

If \(a=2s+1\), (4) gives \(j<\sqrt{2q}\,q^s<q^{s+1}\).
Thus \(v_q(m)\le s\) for \(1\le m\le j\), and every correction
in (5) has q-adic valuation at least \(s+1\). Therefore
\[
A\equiv1\pmod{q^{s+1}}.
\]
Also \(p^2<7q^{2s+1}<q^{2s+2}\), so \(1<p<q^{s+1}\).
Lucas' theorem then gives \(L\equiv0\pmod q\): the lowest \(s+1\)
base-q digits of the top A are those of 1, and those of the bottom p
cannot fit them.

If \(a=2s\), where \(s\ge1\), put \(u=q^s\). Inequality (4)
gives \(j<\sqrt2u<q^{s+1}\), and (5) gives
\[
A\equiv1\pmod u.
\]
The equality \(p^2+p+1=7u^2\) implies
\[
\boxed{2u+1<p<3u.}
\tag{6}
\]
The upper bound follows from \(p^2<7u^2<9u^2\). If the lower bound
failed, then
\[
7u^2=p^2+p+1\le4u^2+6u+3<7u^2,
\]
where the last strict inequality holds for \(u\ge3\) because
\(3u^2-6u-3=3((u-1)^2-2)>0\).
Consequently \(p\bmod u\) lies between 2 and \(u-1\), whereas
\(A\bmod u=1\). Lucas again gives \(L\equiv0\pmod q\).

Thus in both parity cases
\[
\boxed{L\equiv0\pmod q.}
\tag{7}
\]

### 1.2 The first nontrivial digit of X

Write \(n=j^2\). Since \(D<n<2D\), the bottom n of X has low a
base-q digits equal to those of \(n-D\), its digit at position a is 1,
and all higher digits are zero. The exact identity
\[
np^6=n+14nD(p-1)+49nD^2(p-1)^2
\tag{8}
\]
shows that the top and bottom have identical low a digits. The top digit
at position a is congruent to \(1+14n(p-1)\) modulo q. Lucas therefore
gives
\[
\boxed{X\equiv1+14j^2(p-1)\pmod q.}
\tag{9}
\]
Combining (7), (9), and \(L=X+p^2\) yields
\[
14j^2(p-1)+p^2+1\equiv0\pmod q.
\]
Use \(p^2+p+1\equiv0\pmod q\), multiply by \(p+2\), and use
\((p-1)(p+2)\equiv-3\pmod q\). This gives
\[
\boxed{q\mid42j^2+p-1.}
\tag{10}
\]

For \(a=1\), v6 could bound the quotient in (10) and force an exact
quadratic equation. For \(a>1\), this proof yields only modulus q;
it does not justify replacing q by \(q^a\) or reusing that exact
quadratic equation.

## 2. The external Thue theorem used below

The precise theorem required is:

> For every integer \(n>3\), the integral solutions of
> \[
> U^3-(n-1)U^2V-(n+2)UV^2-V^3=\pm1
> \]
> are exactly
> \[
> (U,V)=(\pm1,0),(0,\pm1),(\pm1,\mp1).
> \]

The theorem was completed by:

- M. Mignotte, **Verification of a Conjecture of E. Thomas**,
  *Journal of Number Theory* 44(2) (1993), 172--177.
  DOI: <https://doi.org/10.1006/jnth.1993.1043>.
  Publisher record and abstract:
  <https://www.sciencedirect.com/science/article/pii/S0022314X83710437>.

The publisher abstract explicitly states the displayed family and the
conclusion for \(n>3\). The trivial solution set is also explicitly
listed in the primary predecessor:

- E. Thomas, **Complete solutions to a family of cubic Diophantine
  equations**, *Journal of Number Theory* 34(2) (1990), 235--250.
  DOI: <https://doi.org/10.1016/0022-314X(90)90154-J>.
  Publisher record and abstract:
  <https://www.sciencedirect.com/science/article/pii/0022314X9090154J>.

Primary publisher search records were retrieved on 2026-11-05. Direct
fetching of the Mignotte publisher page returned HTTP 403, while both
search engines returned its abstract. We rely on that stated theorem,
not on a new verification of its full proof. For a readable independent
research presentation with the exact statement, see A. Hoshi's 2012
slides, pp. concerning the Thomas and Mignotte theorems:
<https://mathweb.sc.niigata-u.ac.jp/~hoshi/Rikkyo2012-hoshi.pdf>.

The argument below uses \(n=3t+1\ge7\). Its certificate checks the
reduction and the six listed solutions; it does **not** reprove the
Thomas--Mignotte theorem or claim that checking six points proves its
completeness.

## 3. A uniform cubic-exponent exclusion

**Theorem.** Suppose \(t\ge2\), \(c=t^2+t+1\) is prime, and
\(c\equiv4\) or \(7\pmod9\). If
\[
x^2+x+1=cy^3,\qquad x\in\mathbb Z,\quad y>0,
\tag{11}
\]
then \(y=1\) and \(x=t\) or \(x=-t-1\).

### 3.1 Coprimality and the cube factorization

Let \(\omega^2+\omega+1=0\) and work in the Eisenstein integers
\(R=\mathbb Z[\omega]\), with norm
\[
\operatorname N(r+s\omega)=r^2-rs+s^2.
\]
For completeness, this ring is Euclidean for the norm. In the quotient
field, round both coordinates in the basis \(1,\omega\) to nearest
integers. The error has coordinates of absolute value at most \(1/2\),
so its norm is at most \(3/4<1\). The division algorithm follows,
and hence R has unique factorization. Its units are
\(\{\pm1,\pm\omega,\pm\omega^2\}\), as follows directly by solving
\(r^2-rs+s^2=1\).

For every integer x, the 3-adic valuation of \(x^2+x+1\) is either 0
or 1. Indeed, if \(x=1+3h\), it equals
\(3(1+3h+3h^2)\), and otherwise it is nonzero modulo 3. Since
\(c\ne3\), (11) therefore implies
\[
3\nmid x^2+x+1,\qquad 3\nmid y.
\tag{12}
\]
The two factors \(x-\omega\) and \(x-\omega^2\) are coprime in R:
a common prime would divide their difference \(\omega-\omega^2\),
whose norm is 3, contradicting (12).

Set \(\alpha=t-\omega\). Its norm is the rational prime c, so
\(\alpha\) and \(\bar\alpha=t-\omega^2\) are prime elements.
They are nonassociate: a common prime would divide
\(\omega-\omega^2\), but \(c>3\).

In the factorization
\[
(x-\omega)(x-\omega^2)=c y^3,
\]
coprimality puts each prime element entirely on one side. Every prime
valuation other than those above c is a multiple of 3; at the two
primes above c the valuations are 1 modulo 3. The two primes
\(\alpha,\bar\alpha\) cannot both occur in the same factor: if both
divided \(x-\omega\), conjugation would make both divide
\(x-\omega^2\) too, contradicting coprimality. Therefore exactly one
occurs in each factor. After taking the conjugate if necessary, unique
factorization gives
\[
z=\varepsilon\alpha\beta^3,
\qquad
z\in\{x-\omega,\ x-\omega^2=(x+1)+\omega\},
\tag{13}
\]
where \(\beta\in R\) and \(\varepsilon\) is a unit. Absorb a minus
sign into \(\beta^3\), so \(\varepsilon\in\{1,\omega,\omega^2\}\).
The coefficient of \(\omega\) in z is either \(-1\) or \(+1\).

This step does not assume \(\gcd(c,y)=1\). If \(c\mid y\), the
valuation at the selected prime above c is \(1+3v_c(y)\); the
\(3v_c(y)\) part goes into \(\beta^3\).

### 3.2 Two unit choices are impossible modulo c

Write \(\beta=r+s\omega\). Then
\[
\beta^3=P+Q\omega,
\quad P=r^3-3rs^2+s^3,
\quad Q=3r^2s-3rs^2.
\tag{14}
\]
Multiplication by \(\alpha=t-\omega\) yields
\[
\alpha\beta^3=C+D\omega,
\quad C=tP+Q,\quad D=(t+1)Q-P.
\tag{15}
\]
The \(\omega\) coefficients for the three choices of \(\varepsilon\)
are, respectively,
\[
\begin{array}{c|ccc}
\varepsilon&1&\omega&\omega^2\\\hline
\omega\text{ coefficient}&D&C-D&-C.
\end{array}
\tag{16}
\]

Modulo c, t has order exactly 3: \(t^3\equiv1\), while \(t\not\equiv1\)
because \(c>t+1\). Also \(3\mid c-1\) but \(9\nmid c-1\), by the
hypothesis on c. Thus t is not a cube modulo c. If \(t=u^3\), Fermat's
theorem would give \(t^{(c-1)/3}=1\), contrary to t having order 3
and \(3\nmid(c-1)/3\). The same argument applies to \(t^2\);
and \(t+1\equiv-t^2\) is not a cube either, since \(-1=(-1)^3\).

Put \(w=r+t^2s\). Expanding and using \(t^2+t+1\equiv0\pmod c\)
in (15) gives
\[
\boxed{
C\equiv t w^3,\qquad C-D\equiv(t+1)w^3\pmod c.}
\tag{17}
\]
If \(\varepsilon=\omega\), its coefficient \(C-D=\pm1\) would
make \(t+1\) a cube modulo c. If \(\varepsilon=\omega^2\), its
coefficient \(-C=\pm1\) would make t a cube modulo c. In each case
w is necessarily nonzero, so division by \(w^3\) is valid. Both cases
are impossible. Therefore
\[
\boxed{\varepsilon=1,\qquad D=\pm1.}
\tag{18}
\]

### 3.3 The remaining coefficient is a solved Thue equation

Define the standard simplest cubic form
\[
F_m(U,V)=U^3-mU^2V-(m+3)UV^2-V^3.
\]
Equations (14)--(15) give the exact identity
\[
\begin{aligned}
-D&=r^3-3(t+1)r^2s+3trs^2+s^3\\
&=F_{3t}(s,-r).
\end{aligned}
\tag{19}
\]
Hence \(F_{3t}(s,-r)=\pm1\). Apply the theorem in Section 2 with
\(n=3t+1>3\). Its only possible pairs give
\[
(r,s)\in
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\tag{20}
\]
Every such pair has \(\operatorname N(\beta)=r^2-rs+s^2=1\).
Taking norms in (13) and comparing with (11) gives
\[
c y^3=c\operatorname N(\beta)^3=c,
\]
so \(y=1\). Finally
\[
x^2+x+1-c=(x-t)(x+t+1)=0,
\]
and the two claimed values of x follow. Both satisfy (11). This proves
the theorem.

## 4. Consequences for the original branch

If \(\Phi_3(p)=cq^a\), with c satisfying Section 3 and \(a=3b>0\),
take \(y=q^b\ge2\). The theorem forces \(y=1\), a contradiction.
Therefore
\[
\boxed{
\Phi_3(p)\ne cq^{3b}
\quad(b\ge1,\ q\text{ prime}),
\quad c=t^2+t+1\text{ prime},\ c\equiv4,7\pmod9.}
\tag{21}
\]
This arithmetic exclusion is independent of j and even of the primality
of p. It rules out the whole specified cyclotomic pattern before any
large binomial is formed.

| t | c | c mod 9 | Excluded pattern |
|---:|---:|---:|---|
| 2 | 7 | 7 | \(\Phi_3(p)=7q^{3b}\) |
| 3 | 13 | 4 | \(\Phi_3(p)=13q^{3b}\) |
| 5 | 31 | 4 | \(\Phi_3(p)=31q^{3b}\) |
| 6 | 43 | 7 | \(\Phi_3(p)=43q^{3b}\) |

For \(c=7\), v6 already excludes exponent 1, and Section 1 supplies
an additional necessary congruence for every remaining exponent.
The forms \(7q^2\), \(7q^4\), \(7q^5\), and the corresponding higher
exponents not divisible by 3 are **not** excluded by this note.
The prime cofactor condition in Section 3 is essential to this proof:
for composite c, different prime factors may choose different conjugate
sides, and (13) need not hold with \(\alpha=t-\omega\).

## Verification status

The companion exact Python certificate checks the polynomial identities,
unit transforms, reduction to the stated Thue family, the six transformed
trivial solutions, and complete residue tables for the four displayed
cofactors. These checks audit the reduction; the completeness theorem
for the Thue equation remains the explicitly cited external input.
Root independent mathematical audit passed on 2026-11-05, including
the odd/even digit blocks, coefficient reductions, unit analysis,
factorization with \(c\mid y\) allowed, and the external theorem's
parameter substitution. The companion script passed all 11 groups of
exact checks, including 48 structured generic digit cases.
A second independent mathematical and certificate audit by the
prime-powers agent also passed on 2026-11-05. That audit independently
re-expanded both coefficient congruences, checked the \(c\mid y\) and
conjugation cases, and separately retrieved the publisher theorem
statement and the Hoshi presentation. No correction was required.
