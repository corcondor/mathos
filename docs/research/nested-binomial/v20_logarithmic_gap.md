# v20: a logarithmic lower gap, smaller canonical heights, and complementary J > 8

Date: 2026-11-07 JST. This note gives written proofs with exact rational
checks. It does not claim new Lean verification or a DeepSeek API run.
The original equation and the accepted formal proof files are unchanged.

## 1. Scope and results

Retain the squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

In the inherited branch `ell=1, j=i-3`, set

\[
n=i,\quad A=\binom n3,\quad m=6n-9,\quad
B=\binom{n^2}{m},\quad r=\min(k,A-k),\quad t=r-3n.
\]

Both `k=r` and `k=A-r` are included. The earlier results give
`n>=104`, `3n<r<10n/3`, and, for n>=1024,
`t<3n/(4 log n)`. All logarithms below are natural.

The new lower bounds use the **original equality**, through

\[
L:=\binom A r=B+k^2>B.
\tag{1}
\]

They are

\[
\boxed{t>\frac{2n}{5\log n}\qquad(n\ge1024),}
\tag{2}
\]

\[
\boxed{t>\frac{9n}{20\log n}\qquad(n\ge32768).}
\tag{3}
\]

Unlike the earlier power lower bounds derived from cube divisibility
alone, these estimates explicitly use (1). Combined with the inherited
upper bound, they confine the gap to constant multiples of `n/log n`.

For epsilon=0 in the small branch and epsilon=1 in the complementary
branch, use the canonical variables

\[
N=n^2+2,\quad T_\epsilon=(r-\epsilon)^2-9n^2-6n-10>0,
\]
\[
G=\gcd(N,T_\epsilon),\qquad w=N/G,\qquad J=T_\epsilon/G.
\tag{4}
\]

In both branches, the new consequences are

\[
\boxed{w<\frac7{16}J\log n\quad(n\ge1024),\qquad
       w<\frac38J\log n\quad(n\ge32768).}
\tag{5}
\]

Combining these with the integer differences already proved in v18
gives global heights

\[
\boxed{n<2^{12}J^{3/2}(1+\log J)\quad(k=r),}
\tag{6}
\]

\[
\boxed{n<2^{25}J^3(1+\log J)^2\quad(k=A-r).}
\tag{7}
\]

The small-branch extension to the low-n range uses the established
`J>=17` from v19. The complementary bound requires only J>=1.
These improve the previous fixed-J exponents `33/14` and `11`, with
their large constants. They leave J unbounded.

Finally, using the inherited canonical `w>=65` and just one cubic
divisibility, we prove without an n or delta scan that

\[
\boxed{J\ge9\qquad(k=A-r).}
\tag{8}
\]

A separate v20 finite divisor certificate may strengthen (8). Its
extra finite exclusions are not needed for any theorem in this note.

## 2. Elementary logarithmic estimates for the two binomial coefficients

For every positive integer s, integration of the increasing function
log x gives

\[
s\log s-s+1\le\log(s!)
\le s\log s-s+1+\log s.
\tag{9}
\]

For the upper inequality, use
`log((s-1)!)<=integral_1^s log x dx`, then add log s. Thus there is
no untracked Stirling error term in this argument.

Since `A<n^3/6` and `r>3n`, (9) yields

\[
\log L<r\log(eA/r)<(3n+t)D,
\qquad D=2\log n+1-\log18<2\log n.
\tag{10}
\]

Here D is positive for n>=1024. The last strict inequality follows
from `e<3<18`.

For the lower binomial coefficient, each of its m numerator factors
is at least `n^2-m+1`. Formula (9) therefore gives

\[
\log B\ge
m\left(1+\log\frac{n^2-m+1}{m}\right)-1-\log m.
\tag{11}
\]

The following are uniform inequalities for n>=1024:

\[
\frac{n^2-6n+10}{6n-9}>\frac{n-5}{6},\qquad
\log(1-5/n)>-\frac5{n-5},\qquad
\frac{5(6n-9)}{n-5}<31.
\tag{12}
\]

The first difference after multiplication by `6(6n-9)` is `3n+15>0`.
The middle estimate follows by integrating `1/(1-x)` on `[0,5/n]`.
The last is equivalent to n>110. Substitution into (11), followed by
`m<6n`, proves

\[
\log B>
(6n-9)(1+\log n-\log6)-32-\log(6n).
\tag{13}
\]

Subtract `3nD` from (13). The leading terms simplify exactly:

\[
\boxed{\log B-3nD>
3(1-\log2)n-10\log n+8\log6-41.}
\tag{14}
\]

Equation (1) and (10) imply that `tD` exceeds the expression on the
right of (14). The proof has retained the original positive `k^2`
term by using the valid consequence `L>B`; it has not replaced the
original equality by a different squared-binomial equation.

## 3. Uniform thresholds for the lower gap

We use the exact elementary estimates

\[
\log2<7/10,\qquad \log2<25/36,\qquad \log6>3/2.
\tag{15}
\]

The first two follow from positive truncated exponential series:

\[
\sum_{a=0}^{3}\frac{(7/10)^a}{a!}-2=\frac{13}{6000}>0,
\]
\[
\sum_{a=0}^{4}\frac{(25/36)^a}{a!}-2
=\frac{43441}{40310784}>0.
\]

Also `e<3`, whence `e^3<27<36=6^2`, proving the last inequality.
The bounds `8/3<e<3` used in this note follow directly from the
exponential series (for the upper bound compare its tail with a
geometric series).

Using the first and third bounds of (15), (14) is greater than

\[
\frac9{10}n-10\log n-29.
\]

The function `n/10-10 log n-29` increases for n>=1024. At 1024,
`log1024=10log2<7`, and its value is greater than

\[
1024/10-70-29=17/5>0.
\]

Consequently `tD>4n/5`. Because `D<2log n`, this proves (2).

Use instead `log2<25/36` in (14). Its right-hand side is greater than

\[
\frac{11}{12}n-10\log n-29.
\]

The difference from `9n/10` is `n/60-10log n-29`, an increasing
function for n>=32768. At that threshold, `log32768=15log2<21/2`,
so the difference is greater than

\[
32768/60-105-29=6182/15>0.
\]

Thus `tD>9n/10` in this entire range, which proves (3).
These threshold arguments are monotonic real inequalities, not
extrapolations from finitely many tested n.

## 4. The canonical denominator grows at most logarithmically

For n>=1024, (2) implies t>5. We may therefore discard a strictly
positive term in

\[
T_1=6n(t-2)+(t-1)^2-10>6n(t-2).
\tag{16}
\]

Moreover `T0>T1`, so a lower bound for T1 applies to both branches.
The function `log n/n` decreases for n>e. From (2) and
`log1024<7`,

\[
T_1>
\left(\frac{12}{5}-\frac{12\log n}{n}\right)
\frac{n^2}{\log n}
>\frac{2967}{1280}\frac{n^2}{\log n}
\qquad(n\ge1024).
\tag{17}
\]

Similarly, (3) and `log32768<21/2` give

\[
T_1>\frac{220869}{81920}\frac{n^2}{\log n}
\qquad(n\ge32768).
\tag{18}
\]

For every n>=104, `N<(5001/5000)n^2`, because n^2>10000.
Use `w/J=N/T_epsilon` to obtain the exact coefficient comparisons

\[
\frac{w}{J\log n}<\frac{53344}{123625}<\frac7{16},
\qquad
\frac{w}{J\log n}<\frac{3414016}{9202875}<\frac38
\]

at the corresponding thresholds. This proves (5). No primality
assumption on G or w, and no upper bound on delta or J, is used.

## 5. New fixed-J heights

The positive integer differences in Sections 3-4 of
`v18_neighbor_cofactor_height.md` give, in their respective branches,

\[
n-1<42J(15552w^2+5400wJ+481J^2)\quad(k=A-r),
\tag{19}
\]

\[
(n-1)^2<36J(30000w^2+9600wJ+784J^2)\quad(k=r).
\tag{20}
\]

For n>=32768, substituting `w<(3/8)Jlog n` yields

\[
\boxed{n-1<42J^3P_1(\log n),\qquad
P_1(x)=2187x^2+2025x+481,}\tag{21}
\]

\[
\boxed{(n-1)^2<J^3P_0(\log n),\qquad
P_0(x)=151875x^2+129600x+28224.}\tag{22}
\]

The branches in (21)-(22) are complementary and small, respectively.
These explicit inequalities are often stronger filters than the
simplified heights (6)-(7).

### Complementary branch

The function `(n-1)/P1(log n)` increases when `log n>=2`. Indeed its
derivative has positive numerator
`P1(log n)-(1-1/n)P1'(log n)`; already

\[
P_1(x)-P_1'(x)=2187x^2-2349x-1544>0\quad(x\ge2).
\]

Put `s=log J>=0` and

\[
H_1=2^{25}J^3(1+s)^2.
\]

Since `log(1+s)<=s` and `log2<7/10`,

\[
\log H_1<35/2+5s\le(35/2)(1+s).
\]

The coefficients of P1 are positive, so
`P1(log H1)<P1(35/2)(1+s)^2`. Also
`H1-1>=(2^25-1)J^3(1+s)^2`. Finally,

\[
42P_1(35/2)=59277729/2<2^{25}-1.
\]

Thus the ratio at H1 is greater than `42J^3`, and monotonicity
contradicts (21) if n>=H1. The low range n<32768 satisfies n<H1
automatically. This proves the global bound (7).

### Small branch

Likewise `(n-1)^2/P0(log n)` increases for `log n>=2`, since

\[
2P_0(x)-P_0'(x)=303750x^2-44550x-73152>0\quad(x\ge2).
\]

Put

\[
H_0=2^{12}J^{3/2}(1+s).
\]

Then `log H0<42/5+(5/2)s<=(42/5)(1+s)`. The exact comparison is

\[
P_0(42/5)=11833164<(2^{12}-1)^2=16769025.
\]

It follows that the ratio at H0 exceeds J^3, contradicting (22) if
n>=H0. For the global statement, use the established `J>=17`:
then H0>32768, so the low-n range also satisfies n<H0. This proves
(6). This last use of v19 is explicit; a low-n branch is not silently
discarded.

## 6. A proof without enumeration that complementary J <= 8 is impossible

Assume the complementary branch and `1<=J<=8`. The inherited canonical
bound is w>=65. The v17 square-root gap implies
`T1>17n^(3/2)` for n>=104, hence

\[
w<\frac{5001}{85000}J\sqrt n.
\tag{23}
\]

If n<1024, the right side is less than 16, contradicting w>=65.
For `1024<=n<=32768`, the first bound in (5) gives

\[
w<\frac7{16}\cdot8\cdot\frac{21}{2}=147/4<65.
\]

Thus n>32768 and the second bound in (5) applies.

The first complementary cubic divisibility in v18 is

\[
\frac n{\gcd(n,3)}\mid(9w+2J)^3.
\]

Since its right side is positive,

\[
n\le3(9w+2J)^3\le3(9w+16)^3.
\]

It follows that

\[
w<3\log n\le3\log\{3(9w+16)^3\}.
\tag{24}
\]

However, the difference

\[
f(w)=w-3\log\{3(9w+16)^3\}
\]

has derivative `1-81/(9w+16)>0` for w>=65. Its value at 65 is
positive. For an entirely rational check of that endpoint, use

\[
e^{65/3}>e^{21}>(8/3)^{21}>3\cdot601^3;
\]

the last inequality is exactly `8^21>3^22*601^3`, checked as integers.
Therefore f(w)>0 throughout w>=65, contradicting (24).
This proves (8) for **all** possible n, delta, and primitive defects H.

## 7. Inputs, checks, and scope

The new analytic gap uses only (1), `n>=1024`, and the inherited
`r>3n`; it does not require the residual elliptic-curve calculations.
The cofactor estimates use the definitions in (4). The near-optimal
fixed-J heights additionally use the written positive integer
differences from v18. The short complementary exclusion uses the
canonical w>=65, the earlier square-root bound for its low-n portion,
and one complementary cubic divisibility. The small global height
uses v19's already established J>=17.

`v20_logarithmic_gap_checks.py` verifies the finite rational constants,
the polynomial substitutions, positivity certificates at the derivative
thresholds, and the endpoint integer comparison. The general proofs
are the written integral and monotonicity arguments above. These
checks do not purport to be a scan proving the universal inequalities.

The power lower gaps from v16-v18 remain valid for their weaker
necessary-condition systems; (2)-(3) make essential additional use of
the original binomial equality. No original solution is found and
neither the offset-three branch nor the full four-variable equation
is solved by this note.
