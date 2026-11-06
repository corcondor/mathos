# Neighbor-prime obstruction and uniform polynomial cofactor bounds

v15, 2026-11-06 JST. This is a written
mathematical argument with exact arithmetic checks, not a new Lean proof.
No existing repository proof body is changed.

## 1. Scope and inherited inputs

Consider the original equation only in the branch ell=1, j=n-3. Put

\[
A=\binom n3,\quad X=\binom{n^2}{6n-9},\quad
r=\min(k,A-k),\quad L=\binom Ar=X+k^2.
\]

Use the established necessary conditions

\[
n\ge104,\qquad3n<r<10n/3,
\]

\[
Q_0:=\frac n{\gcd(n,3)}\mid r^3,\qquad
Q_1:=\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{1}
\]

The optional logarithmic result also uses, for n>=1024,

\[
r<3n+\frac{3n}{4\log n}.
\tag{2}
\]

Write epsilon=0 for k=r and epsilon=1 for k=A-r. The analysis below
explicitly includes both choices. The new polynomial factor is n^2+2,
which appeared in v11's factorization but was not the factor constrained
by its n-3 prime-power argument.

## 2. An exact congruence at every sufficiently large neighbor prime

Let p be any prime divisor of n^2+2 such that

\[
p>6n-9.
\tag{3}
\]

Set m=6n-9. Since m<p, every denominator of the ordinary factorial
formula for binom(n^2,m) is a p-unit. As n^2=-2 modulo p,

\[
X\equiv\binom{-2}{m}=(-1)^m(m+1)=8-6n\pmod p,
\tag{4}
\]

because m is odd. This is an exact congruence, with no truncation or
asymptotic approximation.

The factorization

\[
A-1=\frac{(n-3)(n^2+2)}6
\]

shows A=1 modulo p. Here p>6n-9 and n>=104 imply p>3. Also
r<10n/3<6n-9<p and r>1. Thus r(r-1) is a p-unit. The choose-pair
identity

\[
r(r-1)L=A(A-1)\binom{A-2}{r-2}
\]

forces p|L. Since k equals r or A-r, we have k^2=(r-epsilon)^2
modulo p. Combining this with (4) gives

\[
\boxed{(r-\varepsilon)^2\equiv6n-8\pmod p.}
\tag{5}
\]

In particular, 6n-8 is a nonzero quadratic residue modulo p. Its
nonzeroness follows from p>6n-9: if p divided 6n-8 then necessarily
p=6n-8, which is even and greater than 2. Equivalently the Legendre
symbol ( (6n-8)/p ) must be +1. This is a new uniform obstruction for
arbitrary prime divisors satisfying (3).

## 3. A bounded coefficient and two simultaneous divisor relations

For any prime p|n^2+2 let

\[
w=\frac{n^2+2}{p}.
\]

No assumption gcd(p,w)=1 is made. If p<=6n-9, then

\[
n^2<n^2+2=wp\le w(6n-9)<6wn,
\]

so n<6w. Suppose henceforth that (3) holds, and define the integer

\[
z=\frac{(r-\varepsilon)^2-6n+8}{p}.
\tag{6}
\]

Because r is an integer strictly above 3n, r-epsilon>=3n. Consequently

\[
(r-\varepsilon)^2-6n+8
\ge9n^2-6n+8>8(n^2+2).
\]

The last inequality is n^2-6n-8>0, valid for n>=104. At the other end,
r-epsilon<=r<10n/3 gives

\[
(r-\varepsilon)^2-6n+8<\frac{100}{9}(n^2+2).
\]

Therefore

\[
\boxed{8w<z<\frac{100w}{9}.}
\tag{7}
\]

Multiplying (6) by w yields the exact identity

\[
w(r-\varepsilon)^2=z(n^2+2)+6wn-8w.
\tag{8}
\]

Define positive integers

\[
c_0=2z-(8+\varepsilon^2)w,\qquad
c_1=3z-(2+\varepsilon^2)w.
\tag{9}
\]

They are positive by (7), since c0>7w and c1>21w. Reducing (8)
modulo Q0, where n=0, and Q1, where n=1, gives respectively

\[
c_i\equiv wr(r-2\varepsilon)\pmod{Q_i}\quad(i=0,1).
\]

Using Q_i|r^3 from (1), we obtain

\[
\boxed{Q_0\mid c_0^3,\qquad Q_1\mid c_1^3.}
\tag{10}
\]

If epsilon=0, the stronger conclusions hold:

\[
\boxed{Q_0^2\mid c_0^3,\qquad Q_1^2\mid c_1^3.}
\tag{11}
\]

To justify (11), fix a prime power p^a|Q_i. Then v_p(r)>=ceil(a/3).
The congruence c_i=wr^2 modulo p^a implies
v_p(c_i)>=min(2ceil(a/3),a)>=ceil(2a/3). Thus p^(2a)|c_i^3.
This argument allows p|w and needs no cancellation of w.

## 4. Uniform polynomial cofactor bounds

Set g=gcd(n,3), d=gcd(n-1,6). Then gd<=6 and
n(n-1)=gd Q0 Q1.

### 4.1 The complementary branch k=A-r

Here epsilon=1, and (7) gives

\[
c_0<\frac{119}{9}w,\qquad c_1<\frac{91}{3}w.
\]

By (10),

\[
n(n-1)\le6(c_0c_1)^3
<6\left(\frac{10829}{27}\right)^3w^6
<20000^2w^6.
\]

The last constant comparison is exact:

\[
6(10829/27)^3=\frac{2539773905578}{6561}<20000^2.
\]

Since (n-1)^2<n(n-1), it follows that

\[
\boxed{n<20000w^3+1\qquad(k=A-r).}
\tag{12}
\]

### 4.2 The branch k=r

Here epsilon=0, and (7) gives

\[
c_0<\frac{128}{9}w,\qquad c_1<\frac{94}{3}w.
\]

Using (11),

\[
n^2(n-1)^2\le36(c_0c_1)^3
<36\left(\frac{12032}{27}\right)^3w^6
<240^4w^6.
\]

The exact comparison is

\[
36(12032/27)^3=\frac{6967443587072}{2187}<240^4.
\]

Since (n-1)^4<n^2(n-1)^2,

\[
\boxed{n<240w^{3/2}+1\qquad(k=r).}
\tag{13}
\]

The earlier p<=6n-9 case has n<6w, so it satisfies both relevant
bounds as well. Thus (12) is a valid branch-independent bound for
**every prime divisor p of n^2+2**, with no bound on p,w,or n. Bound
(13) holds uniformly for the smaller k branch. In particular,

\[
\boxed{p^3<\frac{20000(n^2+2)^3}{n-1}}
\quad\hbox{and}\quad
\boxed{p<28n^{5/3}}.
\tag{14}
\]

For k=r, the stronger versions are

\[
\boxed{p^3<\frac{57600(n^2+2)^3}{(n-1)^2}}
\quad\hbox{and}\quad
\boxed{p<40n^{4/3}}.
\tag{15}
\]

The clean constants in (14)-(15) follow from n>=104, which gives
n^2+2<(101/100)n^2 and n-1>(99/100)n. The remaining rational
comparisons are
20000(101/100)^3(100/99)<28^3 and
57600(101/100)^3(100/99)^2<40^3.

These are bounds on each **prime divisor**, not on each full exact
prime-power factor of n^2+2. The latter is not proved here.

## 5. Complete exclusion when n^2+2 is prime

Suppose p=n^2+2 is prime, so w=1. It automatically satisfies (3),
since n^2+2-(6n-9)=(n-3)^2+2>0. By (7),

\[
z\in\{9,10,11\}.
\]

As n>=104, p>3. If 3 did not divide n, then n^2+2 would be divisible
by 3. Thus 3|n, implying n^2=0 and 6n=0 modulo 9. Put s=r-epsilon.
Equation (6) then gives

\[
2z\equiv s^2-1\pmod9.
\]

The square residues modulo 9 are {0,1,4,7}, so

\[
z\bmod9\in\{0,3,4,6\}.
\]

Of z=9,10,11, only z=9 remains. But z=9 would give

\[
s^2=9n^2+6n+10=(3n+1)^2+9.
\]

This is strictly between (3n+1)^2 and (3n+2)^2 for n>=2,
contradicting s being an integer. Consequently

\[
\boxed{n^2+2\text{ must be composite}.}
\tag{16}
\]

This excludes the structural class with n^2+2 prime, in both
k branches, without a finite scan, a logarithmic estimate, or use of
the old Q0,Q1 divisibility. It does not assert that infinitely many
integers n have n^2+2 prime.

## 6. Optional logarithmic complementary-cofactor bound

For n>=1024, (2) supplies an additional restriction. If n<=6w+2,
then log n<=log(8w)<w+2<=3w<147w/32. Suppose n>6w+2. Then

\[
n^2+2>w(6n+10),\qquad p>6n+10.
\]

The lower bound for s in Section 3 gives

\[
z\ge9w-\frac{6n+10}{p}>9w-1.
\]

Hence z>=9w. As in Section 5, z=9w would give the same impossible
square s^2=(3n+1)^2+9. Thus z>=9w+1. Put h=log n>6 and x=3/(4h).
Then (2), along with n^2<wp, gives

\[
9w+1\le z<w(3+x)^2,
\qquad1<w\left(\frac9{2h}+\frac9{16h^2}\right).
\]

Multiplying by h and using h>6 yields

\[
\boxed{\log n<\frac{147}{32}w\qquad(n\ge1024).}
\tag{17}
\]

In particular the simpler bound log n<5w is valid. The exact quadratic
inequality also yields h<(9w+3sqrt(9w^2+w))/4 in the n>6w+2 case.
The polynomial bounds (12)-(13) do not depend on this section.

## 7. Status and limitations

The results are written deductions from the listed branch conditions
and the original equation. The congruence, coefficient interval,
divisor transfer, rational constants, and mod-9 obstruction are all
exact. No complete Thue, Pell, or other CAS solver is required here.

The polynomial cofactor bounds and the n^2+2-prime exclusion concern
the same ell=1,j=n-3 branch as v14, including both k choices. They do
not solve the original four-variable equation, and they do not imply
nonexistence for all composite n^2+2. No new Lean run or DeepSeek API
call is claimed by this note.

## 8. Reproduction and review

The inherited inputs are recorded in
[v6_offset_composite.md](v6_offset_composite.md) and
[v6_common_divisor.md](v6_common_divisor.md). The earlier factorization
and n-3 restriction appear in [v11_mixed_structure.md](v11_mixed_structure.md).

From this directory, run:

```sh
python3 v15_neighbor_prime_checks.py
```

The script writes `v15_neighbor_prime_checks.json`, including the
SHA-256 hashes of its source and this note. It checks the exact rational
constants, the mod-9 obstruction, 110 actual binomial congruences,
44,442 local divisor-transfer instances, and 240 polynomial identities.
The finite instances are supporting checks; the universal statements
are proved in Sections 2-6 and are not extrapolated from those instances.

The root and separate AI collaborators independently reviewed the
written deductions, including both branches and the case p dividing w.
This is an internal mathematical review, not external peer review or a
Lean kernel check.
