# v19 supplement: eliminating the canonical common divisor against the exact defect

Date: 2026-11-07 JST. This is a new written deduction and an exact
polynomial certificate. It is not a Lean proof, a DeepSeek run, or a
classification of the original four-variable equation.

## 1. Inputs and what is added

The original right-hand side is `binom(i^2,j^2)+binom(k^2,ell^2)`.
Keep the inherited branch `ell=1, j=i-3`, and put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
M=\gcd(n,3)\gcd(n-1,6),\quad Q=n(n-1)/M.
\]

The exact defect and its numerator, from `v16_square_defect_pell.md`, are

\[
\delta=Q/\gcd(Q,r^2),\quad C=M\delta,\quad K=\delta r^2/Q.
\]

They satisfy

\[
Cr^2=Kn(n-1),\quad \gcd(K,\delta)=1,\quad
9<K/C<10400/927<45/4,\quad C\le6\delta.
\tag{1}
\]

We use `n>=104`, `3n<r<10n/3`, and, only in Section 5,
`r-3n>3 sqrt(n)` from v17. Define epsilon=0 for `k=r`, and epsilon=1
for `k=A-r`. The canonical variables from v18 are

\[
N=n^2+2,\quad T_\epsilon=(r-\epsilon)^2-9n^2-6n-10>0,
\]
\[
G=\gcd(N,T_\epsilon),\qquad w=N/G,\qquad J=T_\epsilon/G.
\tag{2}
\]

In particular, `gcd(w,J)=1`. Set

\[
g=\gcd(C,K),\qquad c=C/g,\qquad h=K/g.
\tag{3}
\]

Thus `g` divides `M` (because `gcd(K,delta)=1`), `g<=M<=6`,
`gcd(c,h)=1`, `c<=6 delta`, and

\[
cr^2=hn(n-1),\qquad 9<h/c<45/4.
\]

The letter `h` here is this **primitive quadratic numerator**, not the
different residual integer called `h` in v17. None of the results below
uses that older residual variable.

The new bridge is

\[
\boxed{G\mid E_0(c,h)=2(3h^2-4ch+68c^2)\quad(k=r),}
\tag{4}
\]

\[
\boxed{G\mid E_1(c,h)=3(12h^4-16ch^3+404c^2h^2
                         -1752c^3h+7803c^4)\quad(k=A-r).}
\tag{5}
\]

These restrictions apply to **the entire common divisor**, with all
its prime-power multiplicities. They require no large-prime or
repeated-prime hypothesis. They concern `n^2+2`, unlike the conditional
`n^2+1` bounds in v18's earlier resultant note. For each fixed exact
defect family `(M,delta,K)`, (4)-(5) confine the prime support and the
exponents of `G` to a fixed, explicitly factorable integer.

Consequently,

\[
\boxed{G<2^{15}\delta^2\quad(k=r),\qquad
       G<2^{30}\delta^4\quad(k=A-r).}
\tag{6}
\]

This gives new **joint** polynomial heights, without a cutoff on delta
or J:

\[
\boxed{n^2<2^{18}\delta^3J\quad(k=r),\qquad
       n^2<2^{33}\delta^5J\quad(k=A-r),}
\tag{7}
\]

and independently, using the square-root gap,

\[
\boxed{n^3<2^{22}\delta^4J^2\quad(k=r),\qquad
       n^3<2^{52}\delta^8J^2\quad(k=A-r).}
\tag{8}
\]

These do not bound delta or J above. Their purpose is to connect two
previously distinct sets of parameters and give a new finite
reconstruction when both parameters are fixed.

## 2. The actual elimination ideals and their integral certificates

Use the polynomial ring `QQ[r,n,h,c]`, with the displayed variable order
for lexicographic elimination. Define

\[
F=cr^2-hn(n-1),\quad N=n^2+2,\quad
B_\epsilon=(r-\epsilon)^2-6n+8,
\]
\[
I_\epsilon=\langle F,N,B_\epsilon\rangle.
\]

SymPy actually computes

\[
I_0\cap\mathbb Q[c,h]=\langle 3h^2-4ch+68c^2\rangle,
\]
\[
I_1\cap\mathbb Q[c,h]=\langle
12h^4-16ch^3+404c^2h^2-1752c^3h+7803c^4\rangle.
\tag{9}
\]

These are eliminations of modular necessary conditions: at an original
integer solution, `G` divides each generator, rather than `N=0` as an
integer. A rational Gröbner basis may divide by 2 or 3. Therefore (9)
alone is **not** permission to discard those factors modulo G. The
integer identities below, checked coefficient by coefficient by a
second implementation, establish the exact multiples (4)-(5).

### Small branch: a quadratic norm, without an unnecessary square

Put `a=h+6c`, `b=2h-8c`. Then

\[
L_0=an+b=F-cB_0+hN,
\]

\[
E_0=b^2+2a^2=a^2N-(an-b)L_0.
\tag{10}
\]

All coefficients are integers. Thus `G|F,N,B0` implies `G|E0`.
This is stronger than merely taking the two raw resultants: those
return `E0^2`, because the first elimination squares a linear condition.
The direct identity removes this artificial square and preserves the
prime-power multiplicities relevant to G.

### Complementary branch: a quartic norm

Now put

\[
a=h+6c,\quad b=2h-9c,\quad L_1=2cr+an+b=F-cB_1+hN,
\]
\[
U=4ch+2ab=4h^2+10ch-108c^2,
\]
\[
V=b^2+8ch-2a^2=2h^2-52ch+9c^2.
\]

An exact identity is

\[
Un+V=4cF+(4ch-a^2)N-(2cr-an-b)L_1.
\tag{11}
\]

Consequently

\[
E_1=V^2+2U^2=U^2N-(Un-V)(Un+V).
\tag{12}
\]

This proves (5) without cancelling c, h, 2, 3, U, V, or any residue
that may be a nonunit modulo G. Expanding (12) gives precisely the
quartic in (5). The two raw resultants also give E1 in this branch.

Both norms are positive in our domain. For E0, `a=h+6c>0`.
For E1, `U/c^2=4(h/c)^2+10(h/c)-108>306>0` by (1).
They therefore provide genuine finite divisor lists, not a vacuous
divisibility by zero.

### Saturation and the exceptional residue issue

The producer also computes the Rabinowitsch ideal with
`1-s*c*h*n*(n-1)` and eliminates s. Over QQ the resulting saturated
ideal is unchanged in both branches, as checked by reductions in both
directions. Its dimension is still positive while c and h vary; no
global finite set of original solutions follows.

More significantly, **rational saturation is not used to cancel any
factor modulo G**. A positive integer c can vanish in a residue field,
so the rational open chart `c!=0` is not automatically an allowed
modular cancellation. Equations (10)-(12) avoid this issue entirely.
Primitivity in (3) is ordinary integer gcd reduction, not a rational
Bezout variable pretending to encode coprimality.

## 3. Exact size bounds for the common divisor

Write `x=h/c`, so `9<x<45/4`. In the small branch,

\[
E_0/c^2=2(3x^2-4x+68)<6443/8.
\]

This polynomial is increasing on the stated interval. Since `c<=6 delta`,

\[
E_0<(57987/2)\delta^2<2^{15}\delta^2.
\tag{13}
\]

In the other branch, `U/c^2=4x^2+10x-108` is positive and increasing,
and `V/c^2=2x^2-52x+9` is negative and decreasing throughout the interval.
Thus `(V/c^2)^2+2(U/c^2)^2` is increasing. Its value at `x=45/4` is

\[
\frac{40062681}{64}.
\]

It follows that

\[
E_1<\frac{3245077161}{4}\delta^4<2^{30}\delta^4.
\tag{14}
\]

Because G is a positive divisor of the corresponding positive E,
(13)-(14) prove (6).

## 4. Divisor reconstruction and the quadratic-in-n heights

Let `a=h-9c`. By (1), a is a **positive integer**, hence `a>=1`.
Substitute `cr^2=hn(n-1)` into `T_epsilon=JG`.

In the small branch, the exact equation is

\[
\boxed{a n^2-(h+6c)n-c(JG+10)=0.}
\tag{15}
\]

In the complementary branch, write

\[
L(n)=a n^2-(h+6c)n-c(JG+9).
\]

Then

\[
\boxed{L(n)=2cr>0,\qquad
 L(n)^2-4ch\,n(n-1)=0.}
\tag{16}
\]

For fixed positive `(delta,J)`, the inherited interval supplies finitely
many M and K. For each, compute c,h and factor E0 or E1. **Every**
possible G is a positive divisor of that fixed integer. Equation (15)
then supplies a quadratic polynomial for n; (16) supplies a quartic.
Retain only integer `n>=104`, the required positive sign in (16),
integer r, the actual M and delta, `G=gcd(N,T_epsilon)`, and all
remaining inherited conditions. Finally the original binomial equation
must still be checked. In (15) there is at most one positive real n;
in (16) at most four algebraic n need be inspected for each divisor G.

This is a finite algebraic reconstruction for fixed `(delta,J)`, not a
claim that all possible pairs `(delta,J)` have been bounded. It avoids
using the exponential Pell height as its n domain; it also avoids
assuming that the modular eliminant is sufficient for an original
solution.

For explicit heights, (15), `h/c<45/4`, and (6) imply

\[
n^2<\frac{207}{2}\delta n+6\cdot2^{15}\delta^3J+60\delta.
\tag{17}
\]

From (16) and `r<10n/3`, similarly,

\[
n^2<\frac{287}{2}\delta n+6\cdot2^{30}\delta^5J+54\delta.
\tag{18}
\]

For any real positive z and n, `(n-4z)^2>=0` gives
`zn<=n^2/8+2z^2`. Apply this to the linear term in (17) or (18), and
use `delta,J>=1` to absorb the lower powers. The remaining exact
constant comparisons are

\[
\frac87\left(6\cdot2^{15}+60+\frac{207^2}{2}\right)
=\frac{1744740}{7}<2^{18},
\]

\[
\frac87\left(6\cdot2^{30}+54+\frac{287^2}{2}\right)
=\frac{51539937460}{7}<2^{33}.
\]

This proves (7), including the linear terms. The inequalities hold
already for delta>=1; using v19's stronger delta>=25 is unnecessary.

## 5. The square-root and 7/11 gaps give different joint bounds

Let `t=r-3n`. The inherited v17 result is `t>3 sqrt(n)`. Hence

\[
T_0=6n(t-1)+t^2-10>18n^{3/2},
\]

and, for n>=104,

\[
T_1=6n(t-2)+(t-1)^2-10
>18n^{3/2}-3n-6\sqrt n-9>17n^{3/2}.
\]

For the last comparison, `sqrt(n)>10` makes
`n^(3/2)>10n>3n+6 sqrt(n)+9`.
Now `T_epsilon=JG` and (6) imply

\[
18n^{3/2}<2^{15}\delta^2J\quad(\epsilon=0),\qquad
17n^{3/2}<2^{30}\delta^4J\quad(\epsilon=1).
\]

Square these inequalities, and use `18^2>2^8` and `17^2>2^8`.
This proves (8). Neither (7) nor (8) dominates the other for every
relative size of delta and J, so both can be kept as filters.

The stronger v18 input `u=t+3>n^(7/11)/96` also transfers directly.
Here `u>33`, and

\[
T_\epsilon\ge6n(u-5)+(u-4)^2-10>5nu
>\frac5{96}n^{18/11}.
\]

Thus an exact useful form, without another loose power-of-two constant,
is

\[
\boxed{\frac5{96}n^{18/11}<J E_\epsilon(c,h).}
\tag{19}
\]

Raising to the eleventh power turns it into the integer comparison
`5^11*n^18 < 96^11*J^11*E_epsilon^11`. Its scope and remaining free
parameters are the same as above.

## 6. Reproduction and verification limits

Run

```sh
python v19_canonical_defect_elimination_checks.py
python v19_canonical_defect_elimination_verify.py
```

The producer uses SymPy for actual lexicographic Gröbner bases,
resultants, and rational saturation. It exports the integer coefficient
certificates (10)-(12). The verifier uses only the Python standard
library, reconstructs the base polynomials itself, and checks the
integer coefficient identities and rational constant margins without
importing the producer or SymPy. These exact identities, together with
the written inequalities above, are the basis for the quantified
divisibility and height statements.

Optional regression checks on the previously saved 93 Pell candidates
test the new identities against large integers and both canonical
branches. They do not provide the universal proof, and those 93 points
were already excluded from the original equation in v19. No new global
cutoff for n, no complete Mordell--Weil basis, no elliptic discrete
logarithm solver, and no new original solution is asserted.

Inputs: `v16_square_defect_pell.md`, `v17_square_root_gap.md`,
`v18_residual_gap.md`, `v18_neighbor_cofactor_height.md`.
The earlier `v18_defect_resultants.md` is related but its large repeated
prime hypotheses are not inputs to (4)-(19).
