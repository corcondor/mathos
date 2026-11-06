# v17: simultaneous prime-power restrictions from quadratic neighbors

Date: 2026-11-06 JST. Written deductions with exact integer certificates.
No new Lean execution, DeepSeek API call, or external peer review is claimed.
Existing formal proof bodies and frozen goal contracts are unchanged.

## 1. Scope and notation

Retain the squared-index equation and the branch `ell=1, j=i-3`.
Put

\[
n=i,\quad A=\binom n3,\quad m=6n-9,\quad
B=\binom{n^2}{m},\quad r=\min(k,A-k),
\]

\[
M=\gcd(n,3)\gcd(n-1,6),\qquad Q=\frac{n(n-1)}M.
\]

The previously proved inputs are

\[
n\ge104,\quad 3n<r<10n/3<m,\quad Q\mid r^3,\quad
\binom Ar=B+k^2,\quad k\in\{r,A-r\}.
\tag{1}
\]

For the non-square offsets define

\[
\mathcal C=\{2,3,5,6,7,8,10,11,12,13,14,15\},
\qquad
\mathcal C(n)=\{c\in\mathcal C:6\mid(c+2)n-3c\}.
\]

For each admissible c set

\[
N_c=n^2-c,\qquad a_c=\frac{(c+2)n-3c}{6}.
\]

The exact identity and size bounds are

\[
A-a_c=\frac{(n-3)N_c}{6},\qquad0<a_c<r<m.
\tag{2}
\]

The possible sets C(n), according to n modulo 6, are:

| n mod 6 | C(n) |
|---|---|
| 0 | 2, 6, 8, 10, 12, 14 |
| 1 or 5 | 7, 10, 13 |
| 2 or 4 | 10 |
| 3 | 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15 |

## 2. Generalized large repeated-prime theorem

**Theorem 1.** For any c in C(n) and any prime p, the conditions

\[
e=v_p(N_c)\ge2,\qquad p^2>m
\tag{3}
\]

force

\[
\boxed{k=A-r,\qquad e=3,\qquad v_p(r-a_c)=1.}
\tag{4}
\]

In particular, in the small branch k=r, every repeated prime divisor
of every N_c in the applicable row satisfies p^2<=m.

### 2.1 Valuation transfer

We use the elementary exact formula from v16. If
0<=b<s<=U, p^e exactly divides U-b, and p^e>s, then

\[
v_p\binom Us=e-v_p\left(\frac{s!}{b!(s-b-1)!}\right).
\tag{5}
\]

This follows by comparing the numerator factors U-j with b-j for
j != b. Every nonzero |b-j| is smaller than p^e, so its valuation is
unchanged. The factorial quotient is an integer, equal to both
s*C(s-1,b) and (s-b)*C(s,b).

Under (3), p>=29, p>c, and p cannot divide n-3, since otherwise it
would divide 9-c, a nonzero integer of absolute value at most 7.
Thus v_p(A-a_c)=e. Applying (5) to both binomials gives

\[
v_p(B)=e-F,\qquad v_p\binom Ar=e-G,
\tag{6}
\]

where

\[
F=\left\lfloor\frac mp\right\rfloor-
  \left\lfloor\frac{m-c-1}{p}\right\rfloor\in\{0,1\},
\]

\[
G=\left\lfloor\frac rp\right\rfloor-
  \left\lfloor\frac{a_c}p\right\rfloor-
  \left\lfloor\frac{r-a_c-1}p\right\rfloor\in\{0,1\}.
\tag{7}
\]

### 2.2 Complete exception analysis

If F=1, some t with 0<=t<=c satisfies p|(m-t). Combining this with
p|N_c yields

\[
p\mid D_{c,t}:=(9+t)^2-36c.
\tag{8}
\]

All 118 constants, including odd t, must be retained. None is zero,
because c is not a square. Their prime divisors >=29, together with
the boundary primes 29,31,37, give the following complete table:

| c | Primes requiring a residue check |
|---:|---|
| 2 | 29, 31, 37 |
| 3 | 29, 31, 37 |
| 5 | 29, 31, 37, 59 |
| 6 | 29, 31, 37, 47 |
| 7 | 29, 31, 37, 83, 131 |
| 8 | 29, 31, 37, 47, 167 |
| 10 | 29, 31, 37, 41, 71, 191, 239 |
| 11 | 29, 31, 37, 107, 227 |
| 12 | 29, 31, 37, 59, 71, 83, 263, 311 |
| 13 | 29, 31, 37, 43, 53, 107, 179, 347 |
| 14 | 29, 31, 37, 43, 47, 67, 101, 383 |
| 15 | 29, 31, 37, 43, 53, 71, 179, 251, 419 |

This is 69 pairs (c,p), using 25 distinct primes. Hypothesis (3) gives

\[
104\le n\le\left\lfloor\frac{p^2+8}{6}\right\rfloor<p^2.
\tag{9}
\]

For each pair, all roots of n^2=c modulo p^2 are obtained by the
unique Hensel lift from each root x modulo p:

\[
n=x+pz,\qquad
z\equiv-\frac{x^2-c}{p}(2x)^{-1}\pmod p.
\tag{10}
\]

The inverse exists since p>c>0. The accompanying certificate compares
these roots with a second computation over every residue modulo p^2.
After (9) and the integrality condition on a_c, exactly four triples
remain:

| c | p | n | Q | Least F_3 with Q dividing F_3^3 |
|---:|---:|---:|---:|---:|
| 7 | 37 | 157 | 4082 | 4082 |
| 10 | 71 | 275 | 37675 | 7535 |
| 10 | 191 | 5382 | 9653514 | 9653514 |
| 13 | 43 | 149 | 11026 | 11026 |

Here F_3=product over q of q^ceil(v_q(Q)/3), so Q|r^3 forces F_3|r.
In every row F_3>10n/3, contradicting (1). Thus every genuine solution
under (3) has p>=41 and F=0. The exception check is over the entire
domain forced by the written argument; it is not a chosen search
cutoff in n.

### 2.3 Exponent and branch

If G=0, both binomials in (6) have valuation e>=2. Their difference
k^2 then forces p|k. For k=r the integer defining G is
r*C(r-1,a_c), so G>=1. For k=A-r, (2) gives p|(r-a_c), and the same
integer is (r-a_c)*C(r,a_c), again giving G>=1. Contradiction.

Hence G=1 and the two binomials have unequal valuations. Consequently

\[
e-1=2v_p(k).
\tag{11}
\]

Both r and r-a_c are positive and smaller than p^2. In the complement
branch, v_p(k)=v_p(r-a_c), since A-a_c has valuation at least 2.
Thus v_p(k)<=1 in either branch. Equation (11), together with e>=2,
forces e=3 and v_p(k)=1.

If k=r, then p|r, while p is coprime to Q: p>c and p>c-1 prohibit
p from dividing n or n-1. Therefore Q|(r/p)^3. This implies

\[
p^3<\frac{1000M}{27}\frac{n^2}{n-1}<225n.
\tag{12}
\]

The last constant follows from M<=6, n>=104 and
208000/927<225. But

\[
p^3>p(6n-9)\ge41(6n-9)>225n
\]

for n>=104, a contradiction. This proves (4).

## 3. A simultaneous limit: at most four such primes across all c

Let P be the product of all primes satisfying (3) for at least one
c in C(n), with the empty product equal to 1. A prime p>=29 cannot
divide two distinct N_c, because it would divide their nonzero
difference, whose absolute value is at most 13. Theorem 1 gives

\[
P\mid k,\qquad\gcd(P,Q)=1.
\tag{13}
\]

Also Q divides A. Indeed A/Q=M(n-2)/6, and the values of M for
n mod 6 = 0,1,2,3,4,5 are respectively 3,6,1,6,3,2, which make
this expression integral. Since k is r or A-r, Q|r^3 implies Q|k^3.
Cancelling the primes in P gives Q|(k/P)^3. Thus

\[
\boxed{P^3\le\frac{k^3}{Q}<\frac{n^8}{36(n-1)}
<\frac{n^7}{35}.}
\tag{14}
\]

We used k<A<n^3/6, M<=6, and n>36. If there were at least five
distinct such primes, their squared product would exceed m^5,
and hence

\[
P^3>m^{15/2}>(5n)^{15/2}>n^7/35,
\]

contradicting (14). We conclude

\[
\boxed{\#\{p:\text{(3) holds for some }c\in\mathcal C(n)\}\le4.}
\tag{15}
\]

For any one c, there is at most one such prime: two primes p,q would
give p^3q^3>N_c, since p^2,q^2>m and m^3>n^2>N_c.
Consequently at most four of the applicable quadratic neighbors can
contain such a repeated prime. If n=0 modulo 6, at least two of the
six applicable N_c have no repeated prime above sqrt(m). If n=3
modulo 6, at least eight of the twelve have no such prime. None of
these conclusions asserts that those N_c are squarefree.

## 4. Prime divisors of n and n-1

**Theorem 2.** Every solution under (1) satisfies

\[
\boxed{P^+(n)<3\sqrt n.}
\tag{16}
\]

More precisely, if p|n and p^2>m, then

\[
\boxed{n\equiv2\pmod3,\quad n=pw,\quad
6w<p<9w,\quad p\mid3w^2+2.}
\tag{17}
\]

In particular, for n=0 or 1 modulo 3,

\[
\boxed{P^+(n)^2\le6n-9.}
\tag{18}
\]

### 4.1 The case 3 divides n

Suppose p|n and p^2>m. Then p>=29 and p^2>n, so v_p(n)=1.
Since p|Q, p|r; also p|A, so p|k in either branch. Transfer formula
(5), with U=n^2, b=0 and s=m, gives v_p(B)=2, because p does not
divide m=6n-9.

If 3|n, let a_0=n/3. Identity (2) also holds for c=0, and
v_p(A-a_0)=2. Because p divides both a_0 and r, and r<p^2,
the factorial loss in (5) is exactly 1. Thus v_p(C(A,r))=1,
whereas B+k^2 is divisible by p^2. This is impossible.

### 4.2 The other residue classes

Write n=pw. From p^2>6pw-9 and p>=29, the integer p-6w cannot be
negative: otherwise p(p-6w)<=-p<-9. Equality is also impossible
because p is odd. Thus p>6w. Write r=pR; then

\[
3w<R<10w/3<p.
\tag{19}
\]

Modulo p, A/p is congruent to w/3. When 3 does not divide n, let
b be its representative in [0,p). Lucas' formula gives

\[
\binom Ar\equiv\binom bR\pmod p.
\tag{20}
\]

The right-hand side of the original equation is divisible by p^2,
so (20) must vanish. Hence b<R.

If n=1 modulo 3, p and w have the same nonzero residue modulo 3,
so b=(w+2p)/3>13w/3>R. This is a contradiction. If n=2 modulo 3,
then b=(w+p)/3, and b<R<10w/3 implies p<9w.

To obtain the final congruence in (17), observe that A/p-b is an
integer and

\[
\frac Ap-b=\frac p6(pw^3-3w^2-2).
\tag{21}
\]

Since b<R<p, the factors in the product for C(A/p,R) have exactly
one p-divisible numerator factor, namely A/p-b. Its denominator is
a p-unit. The same valuation is obtained for C(A,pR): in its
factorial valuation, the first base-p level cancels because p divides
A and pR, and all higher levels are those of C(A/p,R). Hence

\[
v_p\binom Ar=v_p\left(\frac Ap-b\right).
\tag{22}
\]

Both B and k^2 are divisible by p^2, so the left side is at least 2.
Equations (21)-(22) force p|3w^2+2, completing (17).

For every prime factor p of n, either p^2<=m<9n, or (17) gives
p^2<9pw=9n. This proves (16).

### 4.3 The preceding integer has the stronger bound in all classes

Every solution under (1) also satisfies

\[
\boxed{P^+(n-1)^2\le6n-9.}
\tag{22a}
\]

Suppose instead p|n-1 and p^2>m. Write n=pw+1. Then p>=29,
v_p(n-1)=1, p|r, p|A and p|k. Just as above,
p(p-6w)>-3 implies p>6w, so 1<=w<p/6. Write r=pu with u<p.

Let alpha=A/p=w(p^2w^2-1)/6. Its residue b in [0,p) is

\[
b=\frac{jp-w}{6},\qquad
1\le j\le6,\qquad j\equiv pw\pmod6.
\]

The bounds on w show 0<b<p, and the congruence on j makes b
integral. Moreover,

\[
\alpha-b=\frac p6(pw^3-j)
\]

has valuation exactly 1, because 1<=j<=6<p. If b>=u, then
C(alpha,u) is a p-unit. If b<u, its valuation is exactly 1, because
u<p and its numerator contains precisely the factor alpha-b that is
divisible by p. The factorial valuation identity used in (22) gives

\[
v_p\binom Ar=v_p\binom\alpha u\in\{0,1\}.
\tag{22b}
\]

In contrast, v_p(B)=2. To see the two carries explicitly, put
N=(pw+1)^2 and m=6pw-3. At the first base-p level, N mod p=1 while
m mod p=p-3. At the second, N mod p^2=2pw+1<m<p^2. Each level
contributes 1 to the factorial floor sum. At the third level,

\[
N\bmod p^3=p^2(w^2\bmod p)+2pw+1\ge p^2>m,
\]

since w is a p-unit. At all subsequent levels the residue is at
least this large, so no further carry occurs. Thus B and k^2 are
both divisible by p^2, contradicting (22b). This proves (22a).

## 5. A binomial congruence with a controlled loss of prime powers

Let p be prime, m>=1, and J= floor(log_p m), defined exactly by
p^J<=m<p^(J+1). If p^e|U and e>J, then for 1<=j<=m,

\[
\boxed{p^{e-J}\mid\binom Uj.}
\tag{23}
\]

Here binomial values outside the usual lower-index range are zero.
For j<=U, the identity
j*C(U,j)=U*C(U-1,j-1) implies a valuation of at least e-v_p(j),
which is at least e-J. This proves (23).

Consequently, if U>=b>=0, p^e|(U-b), and b<s<=m, Vandermonde's
identity gives

\[
\boxed{p^{e-J}\mid\binom Us.}
\tag{24}
\]

Indeed each nonzero summand C(b,s-j)*C(U-b,j) has 1<=j<=s<=m.
These two elementary lemmas require no division by a p-divisible
factor in modular arithmetic.

## 6. The positive neighbor n^2+1 obeys a square-LCM condition

**Theorem 3.** Assume in addition that n=3 modulo 6. Put
L_m=lcm(1,2,...,m). Then

\[
\boxed{n^2+1\mid L_m^2.}
\tag{25}
\]

Equivalently, every prime p with e=v_p(n^2+1) satisfies

\[
\boxed{e\le2\lfloor\log_p m\rfloor.}
\tag{26}
\]

### Proof

Let N=n^2+1 and b=(n+3)/6, an integer. Then

\[
A-b=\frac{(n-3)N}{6},\qquad 0<b<r,
\quad1<r-b<r<m-1.
\tag{27}
\]

If p=2, n is odd and e=1, so (26) is automatic. The prime 3 does
not divide N. For an odd p!=3, suppose e>2J where J=floor(log_p m).
Set s=e-J. Lemma (23) and the exact alternating Pascal identity give

\[
\binom{N-1}{m}=
\sum_{j=0}^m(-1)^{m-j}\binom Nj
\equiv(-1)^m=-1\pmod{p^s}.
\tag{28}
\]

Equation (27) shows p^e|(A-b), even when p=5 also divides n-3.
Lemma (24) gives C(A,r)=0 modulo p^s. The original equation therefore
forces k^2=1 modulo p^s. An odd prime has only the two square roots
1 and -1 modulo any of its powers, because gcd(k-1,k+1) divides 2.

In the small branch this forces r=+/-1 modulo p^s. In the complement
branch it forces r-b=+/-1 modulo p^s, since A=b modulo p^s.
But e>2J implies s>=J+1 and p^s>m, contradicting the strict interval
in (27). This proves (26) and hence (25).

### Consequences

1. The old largest-prime restriction P^+(n^2+1)<=m is recovered when
   J=0. Theorem 3 also controls all prime-power exponents.
2. If p^2|n^2+1 and p^2>m, then necessarily

   \[
   \boxed{v_p(n^2+1)=2,\qquad k^2\equiv1\pmod p.}
   \tag{29}
   \]

   Here J=1 (p>m is already impossible). Equations (28) and (24)
   with e=2 also give the displayed congruence. In the two branches,
   it becomes r=+/-1 or r-b=+/-1 modulo p, respectively.
3. Let p^e exactly divide n^2+1 with odd e=2h+1, and put
   w=(n^2+1)/p^e. For odd p, (26) forces p^(h+1)<=m. Therefore

   \[
   p^{e+1}\le m^2<36(n^2+1),\qquad
   \boxed{p<36w.}
   \tag{30}
   \]

   For p=2 the same final inequality is immediate. Thus p>=36w is
   excluded for every odd exponent, with no numerical cutoff on p
   or on the exponent. This does not assert that the remaining
   prime-power equations have solutions.

## 7. All negative neighbors: simultaneous excess prime powers

Let L_m=lcm(1,...,m). For a positive integer u, let u_[>=17] denote
the factor retaining only primes at least 17. Define

\[
\mathcal R=
\prod_{c\in\mathcal C(n)}
\left(\frac{N_c}{\gcd(N_c,L_m)}\right)_{[\ge17]}.
\tag{31}
\]

**Theorem 4.** Both branches satisfy

\[
\boxed{\mathcal R\mid k^2,\qquad
\gcd(\mathcal R,Q)=1,\qquad
\mathcal R^3 Q^2\mid k^6.}
\tag{32}
\]

In particular, in the small branch,

\[
\boxed{\mathcal R<(225n)^{2/3}.}
\tag{33}
\]

To prove this, let p>=17 divide N_c and write e=v_p(N_c),
J=floor(log_p m). If e>J, apply (24) to the inner binomial with
upper residue c and to the outer binomial with upper residue a_c.
Since p is coprime to 6, (2) supplies the latter congruence. Both
binomials are divisible by p^(e-J), so p^(e-J)|k^2.

No prime p>=17 divides two different N_c, since their differences
are nonzero integers of absolute value at most 13. Thus these
prime-power divisibilities multiply, proving R|k^2. Also p cannot
divide n or n-1, since 0<c<p and 0<c-1<p. Therefore gcd(R,Q)=1.
We already proved Q|k^3. Combining R^3|k^6 with Q^2|k^6 proves
(32). For k=r,

\[
\mathcal R^3\le\frac{r^6}{Q^2}
=\left(\frac{r^3}{Q}\right)^2<(225n)^2,
\]

which gives (33). This is a joint restriction on all 12 possible
quadratics and all prime-power exponents, rather than just the
case p^2>m used in Theorem 1.

## 8. Verification boundary

The accompanying Python file records exact factorizations, all 69
root tables by two methods, the four forced-index exclusions, and
supporting binomial-valuation and congruence checks. The exception
tables in Section 2 exhaust a domain proved finite by (8)-(9).
Other bounded checks are consistency checks of the written universal
arguments; they do not prove them by extrapolation. Sampled inputs
are not asserted to solve the original equation.

Theorems 1-4 retain the offset-three branch. They neither solve that
entire branch nor classify the original four-variable equation. The
valuation and binomial identities here are written proofs, not newly
verified Lean theorem bodies.
