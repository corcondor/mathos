# v16: repeated large primes in n^2-10 have a forced exponent and branch

Date: 2026-11-06 JST.

This is a written theorem and exact arithmetic certificate. The root
derived the valuation argument with an initial p>279 hypothesis; a
separate collaborator independently checked it and extended it by
complete small-prime residue certificates. No new Lean execution,
DeepSeek API call, complete CAS solver, or external peer review is
claimed. Existing formal proof bodies are unchanged.

## 1. Statement and scope

Retain the original squared-index equation in the branch ell=1,j=i-3.
Set

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
m=6n-9,\quad B=\binom{n^2}{m},\quad a=2n-5,
\]

\[
M=\gcd(n,3)\gcd(n-1,6),\qquad Q=\frac{n(n-1)}M.
\]

Use the established conditions

\[
n\ge104,\quad3n<r<10n/3,\quad
M\in\{1,2,3,6\},\quad Q\mid r^3,
\quad\binom Ar=B+k^2.
\tag{1}
\]

**Theorem.** Let p be any prime such that

\[
\boxed{e=v_p(n^2-10)\ge2,\qquad p^2>6n-9.}
\tag{2}
\]

Every solution satisfying (1)-(2) must lie in the complementary branch,
and must satisfy

\[
\boxed{k=A-r,\qquad e=3,\qquad v_p(r-2n+5)=1.}
\tag{3}
\]

In particular, in the small branch k=r every repeated prime factor
of n^2-10 satisfies p^2<=6n-9. In either branch, a repeated prime
above sqrt(6n-9) cannot have exponent 2 or any exponent >=4.
The conclusion is about exact valuations under (2); it is not a
bound for all exact prime powers without that hypothesis.

No fixed numerical lower cutoff on p is needed in the final theorem.
The small-prime certificates in Section 3 remove it completely.

## 2. An exact factorial valuation transfer

We use the following elementary lemma. Suppose
0<=b<s<=U, p^e exactly divides U-b, and p^e>s. Then

\[
\boxed{v_p\binom Us
=e-v_p\!\left(\frac{s!}{b!(s-b-1)!}\right).}
\tag{4}
\]

Indeed the numerator product for binom(U,s) contains U-b with
valuation e. Every other factor U-j has valuation v_p(b-j)<e,
because 0<|b-j|<s<p^e. Summing those valuations gives
e+v_p(b!)+v_p((s-b-1)!), and subtracting v_p(s!) proves (4).
The displayed factorial quotient is an integer; it equals both
s*binom(s-1,b) and (s-b)*binom(s,b).

Under (2), p^e>=p^2>m>r>a. In particular p>=29. The identity

\[
A-a=\frac{(n-3)(n^2-10)}6
\tag{5}
\]

shows v_p(A-a)=e: p>3, and p cannot divide n-3 because n^2-10
would then be -1 modulo p. Apply (4) twice to obtain

\[
v_p(B)=e-F,\qquad v_p\binom Ar=e-G,
\tag{6}
\]

where

\[
F=v_p\!\left(\frac{m!}{10!(m-11)!}\right),\qquad
G=v_p\!\left(\frac{r!}{a!(r-a-1)!}\right).
\tag{7}
\]

Since p^2>m>r and p>10,

\[
F=\left\lfloor\frac mp\right\rfloor
 -\left\lfloor\frac{m-11}p\right\rfloor,\quad
G=\left\lfloor\frac rp\right\rfloor
 -\left\lfloor\frac ap\right\rfloor
 -\left\lfloor\frac{r-a-1}p\right\rfloor.
\tag{8}
\]

Thus F,G belong to {0,1}. The statement for G follows by writing
the two remainders of a and r-a-1; their sum plus 1 is less than 2p.

## 3. Complete removal of the small-prime exceptions

F can be nonzero only if p divides m-t for some integer 0<=t<=10.
Combining this with p|n^2-10 gives

\[
p\mid(9+t)^2-360.
\tag{9}
\]

All eleven constants must be retained. Here p divides m-t, and
need not equal it, so no parity restriction on t is valid in (9).
Their values, for t=0 through 10, are

\[
-279,-260,-239,-216,-191,-164,-135,-104,-71,-36,1.
\]

Their prime divisors >=29 are exactly

\[
\{31,41,71,191,239\}.
\tag{10}
\]

We also treat p=29,37 so that every remaining prime is at least 41.
Condition p^2>6n-9 gives

\[
104\le n\le\left\lfloor\frac{p^2+8}{6}\right\rfloor<p^2.
\tag{11}
\]

The complete roots of n^2=10 modulo p^2 and the resulting possibilities
in (11) are:

| p | Roots in [0,p^2) | Upper bound in (11) | Remaining n |
|---:|---|---:|---|
| 29 | none | 141 | none |
| 31 | 76,885 | 161 | none |
| 37 | 566,803 | 229 | none |
| 41 | 517,1164 | 281 | none |
| 71 | 275,4766 | 841 | 275 |
| 191 | 5382,31099 | 6081 | 5382 |
| 239 | 25535,31586 | 9521 | none |

These are complete residue certificates, not an arbitrary scan over n.
For each root x modulo p, the unique lift x+p*t is obtained by
t=-((x^2-10)/p)*(2x)^(-1) modulo p. The inverse exists because
p>5 and x^2=10 modulo p. The accompanying code independently checks
the full set of residues modulo each of these seven small p^2.

Both remaining n are excluded by the old divisibility and interval:

- n=275 gives Q=37675=5^2*11*137. Hence Q|r^3 forces 7535|r,
  contradicting r<2750/3.
- n=5382 gives n/gcd(n,3)=1794=2*3*13*23, which is squarefree.
  Consequently 1794|r. Since n=3*1794 and r>3n, one has
  r>=10*1794=17940=10n/3, a contradiction.

Therefore any actual solution under (2) has p>=41 and F=0. In
particular

\[
\boxed{v_p(B)=e.}
\tag{12}
\]

## 4. Valuation parity forces e=3

Suppose first that G=0. Then both binom(A,r) and B have valuation e,
so their difference k^2 is divisible by p^e. As e>=2, this forces p|k.

If k=r, then the integer defining G equals r*binom(r-1,a), forcing
G>=1. If k=A-r, (5) shows p|(r-a), while the same integer equals
(r-a)*binom(r,a), again forcing G>=1. Both contradict G=0.

Thus G=1, and the valuations of binom(A,r) and B are unequal. Their
difference has the smaller valuation, giving

\[
\boxed{e-1=2v_p(k).}
\tag{13}
\]

For k=r, the inequality 0<r<p^2 implies v_p(k)<=1. For k=A-r,
write k=(A-a)-(r-a). The first term has valuation e>=2 and
0<r-a<p^2, so

\[
v_p(k)=v_p(r-a)\le1.
\]

Since e>=2 and (13) has an even right side, both branches force

\[
\boxed{e=3,\qquad v_p(k)=1.}
\tag{14}
\]

In the complementary branch, this is exactly v_p(r-2n+5)=1.

## 5. The small branch contradicts the common divisor

If k=r, equation (14) gives p|r. Since p>=41 and p|n^2-10,
p divides neither n nor n-1: otherwise p would divide 10 or 9.
Thus p is coprime to Q. From Q|r^3, cancellation of p^3 gives

\[
Q\mid(r/p)^3.
\]

Using Q=n(n-1)/M and r<10n/3,

\[
p^3<\frac{1000M}{27}\frac{n^2}{n-1}<225n.
\tag{15}
\]

For the last comparison, M<=6 and n>=104 give

\[
\frac{1000M}{27}\frac n{n-1}
\le\frac{208000}{927}<225,
\]

whose positive gap is 575/927. On the other hand, p>=41 and (2) give

\[
p^3>p(6n-9)\ge41(6n-9)=246n-369>225n,
\tag{16}
\]

because n>=104. Equations (15)-(16) contradict each other. The small
branch is impossible, completing (3).

## 6. Verification boundary

`v16_repeated_neighbor_primes_checks.py` verifies all eleven constants
and their exceptional prime factors, the complete seven-prime root
table by two methods, the two old-condition exclusions, the rational
constant, and synthetic plus actual-input valuation identities.
The JSON records source and proof-note hashes.

The small-prime residue certificates in Section 3 exhaust the entire
exceptional domain proved in (10)-(11). Other finite samples are only
consistency checks of the uniform argument. They do not prove the
theorem by extrapolation, and no sampled necessary-condition pair is
asserted to solve the original equation. The initial p>279 argument
and this completed exception analysis were also checked by the root.

The theorem restricts the existing ell=1,j=i-3 branch. It neither
eliminates all complementary-branch cubic factors nor solves the
original four-variable problem.
