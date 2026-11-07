# Four or five consecutive common divisors give polynomial height bounds

## Scope

The equation remains

$$
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
$$

This note concerns ell=1, but is not restricted to j=i-3.
Put n=i, d=i-j, A=C(n,d), X=C(n^2,(n-d)^2), and
r=min(k,A-k). Earlier complete small-j results give j>=101
for every remaining solution. The appendix of
prime_first_ell_one.md shows that d>=4 implies r<3n,
in either outer branch.

**New height bounds.** Every solution with ell=1 satisfies

$$
\boxed{d\ge7\ \Longrightarrow\ n<172d^{36},}
$$

and, more strongly,

$$
\boxed{d\ge9\ \Longrightarrow\ n<27d^{35}.}
$$

Thus every fixed offset d>=7 has an explicit finite upper bound
for the first index. These bounds are large. They do not mean
that the entire finite remainder has been checked or excluded.
The proof is uniform and uses no numerical search for solutions.

## 1. A divisibility fact about consecutive integers

For h positive consecutive integers n,n-1,...,n-h+1, write

$$
P_h(n)=\prod_{s=0}^{h-1}(n-s),\qquad
L_h(n)=\operatorname{lcm}(n,n-1,\ldots,n-h+1).
$$

Then

$$
\boxed{P_h(n)\mid (h-1)!\,L_h(n).}
\tag{1}
$$

To prove this, fix a prime p. For each p^a, the number of
multiples of p^a in an interval of h integers is at most
floor((h-1)/p^a)+1. If there is at least one, its contribution
to v_p(P_h)-v_p(L_h) is that number minus one. Summing gives

$$
v_p(P_h)-v_p(L_h)
\le\sum_{a\ge1}\left\lfloor\frac{h-1}{p^a}\right\rfloor
=v_p((h-1)!).
$$

This proves (1) at every prime.

## 2. An explicit common divisor of A and X

Assume

$$
h\ge1,\qquad d\ge2h-1,\qquad j=n-d\ge h.
$$

For 0<=s<h, define

$$
u_s=s^2+1,\qquad
M_{d,s}=\prod_{b=0}^{s^2}\bigl((d-s)^2-b\bigr),
$$

$$
M_h(d)=\prod_{s=0}^{h-1}M_{d,s},\qquad
K_h(d)=(h-1)!\,M_h(d).
$$

All these integers are positive under the displayed assumptions.
Define

$$
\boxed{
D_h(n,d)=
\frac{P_h(n)}{\gcd(P_h(n),K_h(d))}.
}
\tag{2}
$$

We prove

$$
\boxed{D_h(n,d)\mid A,\qquad D_h(n,d)\mid X.}
\tag{3}
$$

### 2.1 The ordinary inner binomial

The subset-selection identity gives

$$
P_h(n)\binom{n-h}{d-h}
=(d)_h\binom nd,
\qquad (d)_h=\prod_{s=0}^{h-1}(d-s).
$$

Hence P_h divides (d)_h A. Each M_{d,s} contains the factor
(d-s)^2, so (d)_h divides M_h(d), and therefore

$$
P_h(n)\mid K_h(d)A.
\tag{4}
$$

### 2.2 The squared-index binomial

Put N=n^2 and m=(n-d)^2. For each s, the assumptions ensure
u_s<=m<=N, so the falling-factorial selection identity applies:

$$
(N)_{u_s}\binom{N-u_s}{m-u_s}
=(m)_{u_s}\binom Nm.
\tag{5}
$$

The left factor (N)_{u_s} includes N-s^2=(n-s)(n+s).
Consequently

$$
n-s\mid (m)_{u_s}X.
$$

Modulo n-s, m=(n-d)^2 is congruent to (d-s)^2. Therefore

$$
n-s\mid M_{d,s}X.
\tag{6}
$$

Since M_{d,s} divides M_h(d), every n-s divides M_h(d)X.
Thus L_h(n) divides M_h(d)X. Applying (1) yields

$$
P_h(n)\mid K_h(d)X.
\tag{7}
$$

Cancelling gcd(P_h,K_h) in (4) and (7) proves (3).

This uses several factors n-s at once. It extends the
n and n-1 common-divisor method beyond the offset-three branch.

## 3. The original equation turns (3) into a height bound

For any common divisor D of A and X, the equation
C(A,r)=X+k^2 gives

$$
D\mid r^3.
\tag{8}
$$

Indeed r C(A,r)=A C(A-1,r-1), so D divides r k^2.
Since k is r or A-r, k is congruent to plus or minus r modulo D.

Combining (2), (3), (8), and r<3n gives

$$
\boxed{
\frac{P_h(n)}{K_h(d)}
\le D_h(n,d)
\le r^3<27n^3.
}
\tag{9}
$$

For h>=2, every factor in M_h is at most d^2 and at least
one is strictly smaller. Hence

$$
K_h(d)<(h-1)!\,d^{E_h},\qquad
E_h=2\sum_{s=0}^{h-1}(s^2+1)
=2h+\frac{h(h-1)(2h-1)}3.
\tag{10}
$$

### 3.1 Four factors: d>=7

Take h=4. Then E_4=36 and K_4<6d^36.
Because j>=101 and d>=7, n>=108. The product inequality
product(1-x_s)>=1-sum(x_s), for 0<=x_s<=1, implies

$$
P_4(n)
=n^4\prod_{s=1}^3(1-s/n)
\ge n^4(1-6/n)
\ge\frac{17}{18}n^4.
$$

Inserting this in (9) gives

$$
\frac{17n^4}{108d^{36}}<27n^3,
\qquad
n<\frac{2916}{17}d^{36}<172d^{36}.
$$

### 3.2 Five factors: d>=9

Take h=5. Then E_5=70 and K_5<24d^70.
Now n>=110 and

$$
P_5(n)\ge n^5(1-10/n)\ge\frac{10}{11}n^5.
$$

Equation (9) becomes

$$
n^2<\frac{3564}{5}d^{70}<729d^{70}.
$$

Taking positive square roots proves n<27d^35.

## 4. Meaning and verification

For d>=9, the second theorem can be read as

$$
d>(n/27)^{1/35}.
$$

Apart from the separately retained offsets3 through8, a
hypothetical ell=1 solution cannot keep i-j below this
power-scale bound. This is a rigorous, but numerically weak,
height restriction. It does not bound d independently of n,
does not address ell>1, and does not settle the original equation.

The small accompanying exact checker compares (1), (3)-(7)
against direct integer binomial coefficients on explicitly
listed sample parameters, including nontrivial common divisors.
It also verifies the rational constants in the height bounds.
Those samples check the formulas; the universal proof is above.

No new Lean formalization is asserted in this note.

Independent mathematical audits by both the composite-family agent and
the shifted-prime-powers agent passed on 2026-11-05. They checked the
consecutive-integer valuation argument, the selection identities,
cancellation, and both explicit height constants. This is AI-assisted
independent checking, not external peer review.
