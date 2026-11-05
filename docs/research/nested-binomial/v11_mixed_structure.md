# A second local obstruction from the factor n-3

## Scope and connection to the mixed-factor remainder

We retain the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

Throughout this note, \(\ell=1\) and \(j=i-3\). Put

\[
n=i,\qquad A=\binom n3,\qquad
X=\binom{n^2}{(n-3)^2}=\binom{n^2}{6n-9},
\qquad r=\min(k,A-k),\qquad L=\binom Ar=X+k^2.
\tag{1}
\]

Both branches \(k=r\) and \(k=A-r\) are included. Previously
proved inputs, in `v5_offset_three_structure.md`,
`v6_common_divisor.md`, and `v6_offset_composite.md`, are

\[
n\ge104,\qquad 3n<r<10n/3,
\qquad
Q_0:=\frac n{\gcd(n,3)}\mid r^3,\qquad
Q_1:=\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{2}
\]

For \(n\ge1024\), the sharper previously proved inequality gives

\[
r<3n+\frac{3n}{4\log n}<\frac{25n}{8},
\tag{3}
\]

because \(\log n>6\). The lower cutoff in (2) comes from the
complete earlier exclusion of \(\ell=1,j\le100\), not from a
new search bound.

The v10 mixed-prime reduction constrains the factors of \(A\),
with its remaining deficit supported on \(n-2\). The present
note adds information from the neighboring integer \(A-1\):

\[
\boxed{A-1=\frac{(n-3)(n^2+2)}6.}
\tag{4}
\]

Consequently the new restrictions apply even when \(n-2\) has
several prime factors and the v10 simultaneous congruences alone
leave a candidate. They are additional necessary conditions on
that same unsolved branch, not a replacement equation.

The main new results are:

\[
\boxed{
n=wp^a+3,\quad p\ge7,\quad p\equiv3\pmod4
\quad\Longrightarrow\quad
n<\frac{4000}{3}w^3+1
}
\tag{5}
\]

for any hypothetical solution, and the complete exclusions

\[
\boxed{
n=wp^a+3,\quad
w\in\{1,2,3,4\},\quad p\ge7,\quad p\equiv3\pmod4
\quad\Longrightarrow\quad\text{no solution}.
}
\tag{6}
\]

Here \(a\ge1\), and no coprimality assumption on \(w,p\) is
needed in (5). Sections 4-6 also exclude the exceptional bases
\(2,3\) for every one of the four cofactors. The combined result is

\[
\boxed{
n=wp^a+3,\quad w\in\{1,2,3,4\},\quad
p=2\ \text{or}\ p\equiv3\pmod4
\quad\Longrightarrow\quad\text{no solution}.
}
\tag{7}
\]

All conclusions concern (1). They do not assert nonexistence for
all offsets, all \(\ell\), or the unrestricted original equation.

## 1. A prime power in n-3 forces r into two residue classes

Let \(n=wq+3\), where \(q=p^a\), \(w,a\ge1\),
\(p\ge7\), and \(p\equiv3\pmod4\). First suppose

\[
q>6w.
\tag{8}
\]

For a solution, \(n\ge104\). These conditions imply \(q>9\):
if \(w\ge2\), then \(q>12\); if \(w=1\), then
\(q=n-3\ge101\). As \(q-6w\) is a positive integer,

\[
6wq+9<q^2.
\tag{9}
\]

Use the exact rational product

\[
X=\binom{w^2q^2+6wq+9}{w^2q^2}
=\prod_{h=1}^{6wq+9}
\left(1+\frac{w^2q^2}{h}\right).
\tag{10}
\]

Since every \(h\) is smaller than \(q^2=p^{2a}\),
\(v_p(h)\le2a-1\). Each correction \(w^2q^2/h\) therefore
has p-adic valuation at least one, including when \(p\mid w\).
Equivalently, after cancelling the p-part of its denominator,
the correction has numerator divisible by p and denominator
coprime to p. Multiplying these congruences in (10) gives

\[
\boxed{X\equiv1\pmod p.}
\tag{11}
\]

The congruence \(z^2\equiv-1\pmod p\) has no solution for
\(p\equiv3\pmod4\): a nonzero solution would imply
\(z^{p-1}=(-1)^{(p-1)/2}=-1\pmod p\), contradicting Fermat's
theorem. Thus \(L=X+k^2\) is a p-adic unit, independently of
which branch gives k.

Identity (4) becomes

\[
A-1=\frac{wq(w^2q^2+6wq+11)}6.
\tag{12}
\]

Because \(p\nmid6\), it follows that \(q\mid A-1\).
The choose-pair identity

\[
r(r-1)L=A(A-1)\binom{A-2}{r-2}
\tag{13}
\]

therefore gives \(q\mid r(r-1)\), since \(p\nmid L\).
Consecutive integers are coprime, so the whole prime power lies
in one of them:

\[
\boxed{r\equiv0\ \text{or}\ 1\pmod q.}
\tag{14}
\]

The assumptions in (2) ensure \(r\ge2\) and \(r\le A\),
so every binomial in (13) is in its ordinary integer range.
No Lucas-type valuation formula for the outer binomial is needed.

## 2. A short coefficient range and a cubic cofactor bound

Write

\[
r=mq+\delta,\qquad\delta\in\{0,1\}.
\tag{15}
\]

The strict lower gap in (2) gives \(r>3wq+9\), hence
\(m\ge3w+1\). For the upper endpoint,
\(mq<10wq/3+10\). The complete rounding argument yields

\[
\boxed{3w+1\le m\le\lfloor10w/3\rfloor.}
\tag{16}
\]

Here it is essential to use both \(q>6w\) and \(n\ge104\).
Indeed, if m exceeded the displayed floor, then

\[
\left(\lfloor10w/3\rfloor+1-10w/3\right)q<10.
\tag{17}
\]

The coefficient in parentheses is respectively \(1,2/3,1/3\)
when \(w\equiv0,1,2\pmod3\). Each alternative is impossible:

| Residue of w | Lower bound for q |
|---|---|
| \(w\equiv0\pmod3\) | \(w\ge3\), hence \(q>18>10\) |
| \(w\equiv1\pmod3\) | For \(w=1\), \(q\ge101\); otherwise \(q>24>15\) |
| \(w\equiv2\pmod3\) | For \(w=2\), \(q\ge51\); otherwise \(q>30\) |

Now combine the two common divisors in (2) with the linear
identities

\[
wr-mn=w\delta-3m,
\qquad wr-m(n-1)=w\delta-2m.
\tag{18}
\]

They imply the simultaneous, exact restrictions

\[
\boxed{
Q_0\mid(3m-w\delta)^3,
\qquad Q_1\mid(2m-w\delta)^3.
}
\tag{19}
\]

No cancellation of w modulo either divisor is used here: first
multiply \(r^3\) by \(w^3\), then apply (18).
Both quantities being cubed are positive by (16). Let
\(g=\gcd(n,3)\) and \(d=\gcd(n-1,6)\). Since consecutive
integers cannot both be divisible by 3, \(gd\le6\).
Consequently

\[
\begin{aligned}
n(n-1)
&=gd\,Q_0Q_1\\
&\le6\bigl[(3m-w\delta)(2m-w\delta)\bigr]^3\\
&\le6\left(10w\cdot\frac{20w}{3}\right)^3
=\left(\frac{4000}{3}w^3\right)^2.
\end{aligned}
\tag{20}
\]

Since \((n-1)^2<n(n-1)\), this proves (5) when (8) holds.
If \(q\le6w\), then
\(n\le6w^2+3<4000w^3/3+1\) already, for every \(w\ge1\).
Thus (5) holds for every w and every exponent, without (8).

### Consequence for every exact prime-power factor of n-3

Let \(p\ge7\), \(p\equiv3\pmod4\), divide \(n-3\).
Take \(q=p^{v_p(n-3)}\) and \(w=(n-3)/q\). Then (5) gives

\[
\boxed{
w>\left(\frac{3(n-1)}{4000}\right)^{1/3},
\qquad
q^3<\frac{4000(n-3)^3}{3(n-1)}.
}
\tag{21}
\]

In particular, \(q<12n^{2/3}\). This power-scale restriction
is on prime powers in \(n-3\); the v10 logarithmic complementary
factor bound concerned \(n-2\). Both must hold at a remaining
solution index. This distinction between the two shifts matters.

## 3. Complete exclusion of the first four cofactors

Assume \(w\in\{1,2,3,4\}\). If \(q\le6w\), then
\(n\le6w^2+3\le99\), contradicting (2). Thus (14)-(19)
apply. The following case analysis is finite because (16) proves
the complete list of m, not because an upper bound on n was
chosen for a search.

### 3.1 The cofactors w=1 and w=2

For w=1, (16) requires \(4\le m\le3\); for w=2 it requires
\(7\le m\le6\). Both intervals are empty.

### 3.2 The cofactor w=3

Equation (16) leaves only \(m=10\), so \(r=10q+\delta\).
Here \(Q_0=q+1\), and hence

\[
q+1\mid(10-\delta)^3.
\tag{22}
\]

If \(\delta=1\), this says the even integer q+1 divides
\(9^3=729\), impossible.

If \(\delta=0\), it gives \(q+1\mid1000\). Also
\(Q_1=3q+2\): this is odd and is not divisible by 3, so
\(\gcd(n-1,6)=1\). From \(3r-10Q_1=-20\),

\[
3q+2\mid20^3=8000.
\tag{23}
\]

As an odd divisor of 8000, it must equal \(5^b\) with
\(0\le b\le3\). Its residue 2 modulo 3 forces b odd,
so b=1 or b=3. These give q=1 or q=41, respectively.
The first violates \(n\ge104\); the second violates
\(q+1=42\mid1000\). This excludes w=3.

### 3.3 The cofactor w=4

Equation (16) leaves only \(m=13\), so \(r=13q+\delta\).
Since \(p\ge7\), q is odd and is not divisible by 3. Thus
\(n=4q+3\) is coprime to 3 and \(n\equiv7\pmod8\).
In particular \(Q_0=n\).

If \(\delta=0\), (19) gives \(n\mid39^3\). Since
\(3\nmid n\), this forces \(n=13^b\), \(0\le b\le3\).
But such a number is 1 modulo 4, whereas n is 3 modulo 4.

If \(\delta=1\), (19) gives

\[
n\mid35^3,\qquad Q_1\mid22^3.
\tag{24}
\]

Write \(n=5^b7^c\), where \(0\le b,c\le3\).
The residue \(n\equiv3\pmod4\) forces c odd, so \(7\mid n\).
Let \(d=\gcd(n-1,6)\). We have \(d\in\{2,6\}\).
Also \(v_2(n-1)=1\), because \(n\equiv7\pmod8\), so
\(Q_1=(n-1)/d\) is odd. Equation (24) therefore forces

\[
Q_1=11^e,\quad0\le e\le3,\qquad n=1+d11^e.
\tag{25}
\]

For d=2, the residues of \(1+2\cdot11^e\) modulo 7, for
e=0,1,2,3, are 3,2,5,3. None is zero, contradicting \(7\mid n\).

For d=6, the same divisibility requires \(11^e=4^e\equiv1\pmod7\),
which leaves e=0 or e=3. These give n=7 or n=7987.
The first is below 104. The second is 2 modulo 5, hence b=0
in \(n=5^b7^c\); but then \(n\le7^3=343\), also impossible.
This completes the proof of (6).

The finite divisibility argument does not require testing whether
any of its intermediate q values is a prime power. It excludes
the larger set allowed by the displayed necessary conditions.

## 4. The special base 3 when n-3 is a pure prime power

Let \(q=3^a\) and \(n=q+3\). If \(a\le4\), then
\(j=q\le81\), already excluded. Thus suppose a>=5.
The product (10), now with w=1, has

\[
6q+9<9q=3^{a+2}.
\]

Every denominator h has \(v_3(h)\le a+1\), so each
correction \(q^2/h\) has valuation at least a-1. Therefore

\[
X\equiv1\pmod{3^{a-1}},\qquad3\nmid L=X+k^2.
\tag{26}
\]

Here

\[
v_3(A-1)=a-1,\qquad3\nmid A,
\]

because \(A-1=q(q^2+6q+11)/6\) and the expression in
parentheses is 2 modulo 3. Identity (13) now gives

\[
\frac q3\mid r(r-1),\qquad
r\equiv0\ \text{or}\ 1\pmod{q/3}.
\tag{27}
\]

Put \(M=q/3\ge81\). Since \(r>3q+9=9M+9\), the next
possible value allowed by (27) is at least \(10M\). Thus

\[
r\ge\frac{10q}{3}.
\tag{28}
\]

If \(a\ge7\), then \(n\ge2190>1024\), so (3) applies.
Its upper bound contradicts (28), since

\[
\frac{10q}{3}-\frac{25(q+3)}8=\frac{5q-225}{24}>0.
\tag{29}
\]

The only boundary exponents are a=5,6, and both are excluded
using the already proved divisors in (2):

| a | n | Exact divisor obstruction |
|---:|---:|---|
| 5 | 246 | \(Q_0=82\) is squarefree, so \(82\mid r\); the interval \((738,820)\) has no such multiple. |
| 6 | 732 | \(Q_0=244=2^2\cdot61\), \(Q_1=731=17\cdot43\); hence \(122\cdot731=89182\mid r\), whereas \(r<2440\). |

This excludes every exponent for the base 3.

## 5. The special base 2 when n-3 is a pure prime power

Let \(q=2^a\) and \(n=q+3\). If \(a\le6\), then
\(j=q\le64\), already excluded. Suppose a>=7.
The product (10) with w=1 has

\[
6q+9<8q=2^{a+3}.
\]

Every denominator h has \(v_2(h)\le a+2\), so

\[
X\equiv1\pmod{2^{a-2}},\qquad X\equiv1\pmod4.
\tag{30}
\]

Because a square is 0 or 1 modulo 4, \(L=X+k^2\) is 1 or 2
modulo 4, and \(v_2(L)\le1\). At the same time,

\[
v_2(A-1)=a-1,\qquad A\text{ is odd},
\]

by (12), because \(q^2+6q+11\) is odd. Thus (13) implies

\[
\frac q4\mid r(r-1),\qquad
r\equiv0\ \text{or}\ 1\pmod{q/4}.
\tag{31}
\]

Put \(M=q/4\ge32\). The lower gap is
\(r>3q+9=12M+9\), so (31) forces

\[
r\ge\frac{13q}{4}.
\tag{32}
\]

If \(a\ge10\), then \(n\ge1027\), and (3) contradicts
(32), because

\[
\frac{13q}{4}-\frac{25(q+3)}8=\frac{q-75}{8}>0.
\tag{33}
\]

The three boundary values a=7,8,9 give

\[
n=131,\quad259=7\cdot37,\quad515=5\cdot103.
\]

Each n is squarefree and coprime to 3. Therefore \(Q_0=n\)
divides r, which is incompatible with \(3n<r<10n/3\).
This excludes every exponent for the base 2 when w=1.

## 6. Completing the bases 2 and 3 for all four cofactors

Some cases follow directly from the pure-power results just proved:
\(2\cdot2^a=2^{a+1}\), \(4\cdot2^a=2^{a+2}\), and
\(3\cdot3^a=3^{a+1}\). It remains to consider \((p,w)=(3,2),
(2,3),(3,4)\). A short common-divisor lemma handles the latter
two cases together.

### 6.1 A common-divisor obstruction at coefficient 37

Suppose

\[
n=12M+3,\qquad r=37M+\delta,\qquad
M\ge1,\quad\delta\in\{0,1\}.
\tag{34}
\]

Then \(Q_0=4M+1\) and \(Q_1=6M+1\), with
\(3Q_0-2Q_1=1\). In particular they are coprime and both
exceed 1. The identities

\[
4r-37Q_0=4\delta-37,\qquad
6r-37Q_1=6\delta-37
\]

and (2) give

\[
Q_0\mid(37-4\delta)^3,\qquad
Q_1\mid(37-6\delta)^3.
\tag{35}
\]

If \(\delta=0\), both divisors are nontrivial powers of 37,
contradicting their coprimality. If \(\delta=1\), then
\(Q_0\mid33^3\) and \(Q_1\mid31^3\). Since Q1>1, it
must equal \(31^c\) for c=1,2,3. The complete list is

| c | \(M=(31^c-1)/6\) | \(Q_0=4M+1\) | \(33^3\bmod Q_0\) |
|---:|---:|---:|---:|
| 1 | 5 | 21 | 6 |
| 2 | 160 | 641 | 41 |
| 3 | 4965 | 19861 | 16076 |

None satisfies \(Q_0\mid33^3\). Thus (34) is incompatible
with the common divisors (2), for every M>=1.

### 6.2 The case p=3,w=2

Let \(q=3^a\), \(n=2q+3\). The earlier small-j theorem
leaves only a>=4. The product (10) has
\(12q+9<27q\), so each correction has 3-adic valuation
at least a-2. Therefore \(X\equiv1\pmod3\) and \(3\nmid L\).
Equation (12) has \(v_3(A-1)=a-1\), so (13) gives

\[
r\equiv0\ \text{or}\ 1\pmod M,\qquad M=q/3.
\]

Since \(M\ge27\) and \(r>3n=18M+9\), it follows that
\(r\ge19M=19q/3\). If a>=6, then n>=1461 and (3) applies;
the contradiction is

\[
\frac{19q}{3}-\frac{25(2q+3)}8
=\frac{2q-225}{24}>0.
\tag{36}
\]

The boundary exponents a=4,5 give n=165,489 and
\(Q_0=55,163\), respectively. These Q0 are squarefree, so
\(Q_0\mid r\), whereas \(3n<r<10n/3\) is the open interval
\((9Q_0,10Q_0)\). Both are impossible.

### 6.3 The case p=2,w=3

Let \(q=2^a\), \(n=3q+3\). The small-j theorem leaves only
a>=6. In (10), \(18q+9<32q\), so each correction has 2-adic
valuation at least a-4. Thus \(X\equiv1\pmod4\) and
\(v_2(L)\le1\). Also \(v_2(A-1)=a-1\), so (13) gives

\[
r\equiv0\ \text{or}\ 1\pmod M,\qquad M=q/4,
\qquad n=12M+3.
\tag{37}
\]

For a>=9, n>=1539 and M>=128. Combining (2) and (3),

\[
36M+9<r<\frac{75M}{2}+\frac{75}{8}<38M.
\tag{38}
\]

Among the residue classes in (37), this leaves only
\(r=37M+\delta\), \(\delta\in\{0,1\}\), excluded by
Section 6.1. The boundary exponents a=6,7,8 give
n=195,387,771 and \(Q_0=65,129,257\), all squarefree.
Again the interval \((9Q_0,10Q_0)\) contains no multiple of Q0.

### 6.4 The case p=3,w=4

Let \(q=3^a\), \(n=4q+3\). The small-j theorem leaves only
a>=3. In (10), \(24q+9<27q\), so each correction has 3-adic
valuation at least a-2. Hence \(X\equiv1\pmod3\),
\(3\nmid L\), and \(v_3(A-1)=a-1\). The resulting classes are

\[
r\equiv0\ \text{or}\ 1\pmod M,\qquad M=q/3,
\qquad n=12M+3.
\tag{39}
\]

For a>=6, n>=2919 and M>=243, so (38) holds and the same
coefficient-37 obstruction applies. The boundary exponents
a=3,4 give n=111,327 and squarefree \(Q_0=37,109\).
The last boundary exponent a=5 gives n=975,

\[
Q_0=325=5^2\cdot13,\qquad Q_1=487.
\]

Their cube divisibility in (2) forces \(65\cdot487=31655\mid r\),
contradicting \(r<3250\). This completes (7), including every
cofactor w=1,2,3,4 for p=2 and every prime p congruent to 3 modulo 4.

## 7. Verification, novelty, and limits

The new ingredients are the factorization of A-1 in (4), the
unit condition on L obtained from (10), and the use of (13) to
restrict r modulo a prime power from n-3. The old divisors from
n and n-1 then turn this residue information into (19), a cubic
cofactor bound, and complete infinite-family exclusions. The
argument does not assume that n-2 is a prime power.

The companion `v11_mixed_structure_checks.py` reproduces the
small finite divisor cases and boundary cases with exact integer
arithmetic. It also compares the local congruence (11) against
independently computed base-p binomial residues on a specified
set of samples, including samples with p dividing w; verifies
the coefficient-range endpoints; and checks the exact constants
in (20), (29), and (33). These sample checks support the written
uniform proofs. They are not a search cutoff or an extrapolation
to untested values.

The fixed-cofactor reviewer independently audited Sections 1-6
and reported PASS on 2026-11-05, including both exceptional
prime bases, both k branches, the full rounding argument in
(16), the general cubic height constant, all w=3,4 cases, the
coefficient-37 obstruction, and the exceptional-base extensions.
This is an independent AI audit, not external peer review.

The root reviewer independently audited the completed Sections 1-6 and
also reported PASS on 2026-11-05. That review checked the unit-product
argument without a coprimality assumption on w, all strict interval
endpoints, the exceptional-base cutoff exponents and boundary factorizations,
the coefficient-37 divisor argument, and the scope of the all-w height
bound versus the four-cofactor complete exclusion. The exact checker
returned PASS on 4,681 structured odd-prime local examples (including
60 with p dividing w), 9,362 coefficient-endpoint checks, and every
finite divisor and exceptional-boundary case derived in the proof.

The local-square reviewer separately audited the full note and checker,
reported PASS, and reproduced the checker's complete saved result. That
third review explicitly included p dividing w, the coefficient-37 lemma,
and every exceptional-base cofactor case. These three reviews were
independent AI audits within the research session.

No Lean execution of the new statements in this note is claimed
here. Previously executed Lean results in v5, v6, and v10 cover
their stated divisibility cores, not the entire new argument.
The admissible cases with larger cofactors, the prime bases
\(p\equiv1\pmod4\), and the general original four-variable
equation remain unresolved by this note.
