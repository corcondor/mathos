# v17: the quadratic defect meets the n^2+2 neighbor

Date: 2026-11-06 JST. These are written deductions and exact Python
certificates. They are not new Lean verification or a DeepSeek API run.
Existing successful formal proof bodies and fixed goal contracts are
unchanged.

## 1. Scope and inputs

Keep the original squared-index equation, only in the branch ell=1,
j=i-3. Write

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
M=\gcd(n,3)\gcd(n-1,6),\quad Q=\frac{n(n-1)}M,
\]

\[
Q_0=\frac n{\gcd(n,3)},\quad
Q_1=\frac{n-1}{\gcd(n-1,6)},\quad Q=Q_0Q_1,
\quad\delta=\frac Q{\gcd(Q,r^2)}.
\]

The established inputs are n>=104, M in {1,2,3,6}, coprimality of
Q0,Q1, Q|r^3, 3n<r<10n/3, delta^3|Q, delta>=13, and

\[
t:=r-3n\ge4,\qquad t+3>n^{3/5}/64.
\tag{1}
\]

Here t>=4 already follows from n/gcd(n,3)|t^3 and n>=104; its use
does not require the more difficult three-fifths estimate. The latter
is the written v16 lower-gap theorem. The cofactor calculation below
also uses the written v15 n^2+2-neighbor congruence and divisor transfer.

Let p be any prime divisor of N=n^2+2 and put w=N/p. Write epsilon=0
for k=r and epsilon=1 for k=A-r. If p<=6n-9, then n<6w.
If p>6n-9, v15 gives the integer

\[
z=\frac{(r-\varepsilon)^2-6n+8}{p},\qquad
8w<z<100w/9,
\tag{2}
\]

and, with

\[
c_0=2z-(8+\varepsilon^2)w,\qquad
c_1=3z-(2+\varepsilon^2)w,
\tag{3}
\]

\[
c_i\equiv wr(r-2\varepsilon)\pmod{Q_i},\qquad
Q_i\mid c_i^3.
\tag{4}
\]

For epsilon=0 one also has Q_i^2|c_i^3. No coprimality of p and w is
assumed. Formula (2) follows from A=1 and
binom(n^2,6n-9)=8-6n modulo p; denominators are p-units since p>6n-9.

## 2. The exact defect gives stronger divisor transfer

Put delta_i=Q_i/gcd(Q_i,r^2). Since Q0,Q1 are coprime,

\[
\delta_0\delta_1=\delta.
\]

If epsilon=0, (4) directly gives

\[
\boxed{Q_i/\delta_i\mid c_i}.
\tag{5}
\]

Indeed gcd(Q_i,r^2) divides both Q_i and wr^2, so it divides c_i.
If epsilon=1, square (4). Every prime power dividing gcd(Q_i,r^2)
also divides r^2(r-2)^2, and consequently c_i^2. Thus

\[
\boxed{Q_i/\delta_i\mid c_i^2}.
\tag{6}
\]

This argument is valid at every prime, including 2 and 3. It does not
cancel w or r-2. Multiplying the coprime i=0,1 divisors gives

\[
\boxed{
\begin{array}{ll}
Q/\delta\mid c_0c_1,&k=r,\\
Q/\delta\mid(c_0c_1)^2,&k=A-r.
\end{array}}
\tag{7}
\]

Since delta^3|Q, these also give delta^2|c0*c1 in the small branch,
and delta|c0*c1 in the complementary branch. In the latter assertion,
delta^2 divides the square (c0*c1)^2, so delta divides c0*c1 prime by
prime. These forced factors are coprime to the old H because
v16 proves gcd(delta,H)=1. No new numerical lower bound on H follows
from this observation.

### Uniform bounds depending on the actual delta

For epsilon=0, (2)-(3) give

\[
c_0<128w/9,\quad c_1<94w/3,
\quad c_0c_1<\frac{12032}{27}w^2.
\]

Thus (7) implies

\[
n(n-1)=MQ<\frac{24064}{9}\delta w^2
<52^2\delta w^2.
\]

For epsilon=1, instead

\[
c_0<119w/9,\quad c_1<91w/3,
\quad c_0c_1<\frac{10829}{27}w^2,
\]

so

\[
n(n-1)<6\left(\frac{10829}{27}\right)^2\delta w^4
<983^2\delta w^4.
\]

The p<=6n-9 case has n<6w and satisfies the following bounds too.
For every prime divisor p of n^2+2, therefore,

\[
\boxed{
\begin{array}{ll}
n<52\sqrt\delta\,w+1,&k=r,\\
n<983\sqrt\delta\,w^2+1,&k=A-r.
\end{array}}
\tag{8}
\]

Equivalently, using n>=104,

\[
\boxed{
\begin{array}{ll}
p<53\sqrt\delta\,n,&k=r,\\
p<32\delta^{1/4}n^{3/2},&k=A-r.
\end{array}}
\tag{9}
\]

For the first constant, 52(n^2+2)<53n(n-1) is equivalent to
n^2-53n-104>0. For the second, use n^2+2<(101/100)n^2,
n-1>(99/100)n, and 983*10201/9900<32^2.

The constants are convenient and not asserted optimal. These are
adaptive improvements when delta is sufficiently small, not new
unconditional exponents for all possible delta. The previous v15
bounds p<40n^(4/3) and p<28n^(5/3) remain available; one may take the
minimum. No bound for every full exact prime-power divisor is asserted.

## 3. A second integer parameter and a polynomial height

Still suppose p>6n-9 and put

\[
J=z-9w.
\]

From (2),

\[
Jp=6n(t-\varepsilon-1)+(t-\varepsilon)^2-10.
\tag{10}
\]

The right side is positive for n>=104,t>=4 in either branch. Hence

\[
\boxed{J\in\mathbb Z_{>0},\qquad9w<z<100w/9.}
\tag{11}
\]

The divisor coefficients now have the simple form

\[
\begin{array}{c|cc|c}
&c_0&c_1&\text{gcd restriction}\\\hline
\varepsilon=0&10w+2J&25w+3J&\gcd(c_0,c_1)\mid4J\\
\varepsilon=1&9w+2J&24w+3J&\gcd(c_0,c_1)\mid7J
\end{array}
\tag{12}
\]

Indeed 5c0-2c1=4J in the first case and 8c0-3c1=7J in the second.

### A uniform bound for fixed J in the small branch

Let epsilon=0 and D=6n(t-1)+t^2-10=J N/w. The exact identity

\[
\begin{aligned}
7nD-18(t+3)N
={}&(t-4)\{24n^2+n(7t+22)\}\\
&+6(n-6)(t+3)>0
\end{aligned}
\tag{13}
\]

proves

\[
t+3<\frac7{18}\frac{Jn}{w}.
\]

Together with (1),

\[
\boxed{w<\frac{224}{9}J n^{2/5}.}
\tag{14}
\]

The v15 small-branch cofactor theorem supplies n-1<240w^(3/2).
Since n-1>(99/100)n, it follows that

\[
w>\left(\frac{33}{8000}\right)^{2/3}n^{2/3}.
\]

Combining with (14),

\[
n^{4/15}<\frac{224}{9}
\left(\frac{8000}{33}\right)^{2/3}J<1024J.
\]

The last comparison is exact after cubing. We have proved

\[
\boxed{n^4<2^{150}J^{15},\qquad w^2<2^{40}J^5
\quad(k=r,\ p>6n-9).}
\tag{15}
\]

For the second bound, n^(2/5)<2^15 J^(3/2) and
(224/9)*2^15<2^20. Thus a fixed J gives a polynomial, rather than
exponential, height bound. J itself is not bounded here, and the
entire small branch is not thereby finite.

The complementary branch has the valid comparison

\[
t+3<\frac35\frac{Jn}{w},\qquad
w<\frac{192}{5}J n^{2/5}.
\tag{16}
\]

Its proof expands 3nD-5(t+3)N, with
D=6n(t-2)+(t-1)^2-10, as

\[
(t-4)\{13n^2+3n(t+2)-10\}+n^2-3n-70>0.
\]

The weaker v15 complementary cofactor exponent does not turn (16)
into the unconditional fixed-J bound (15). Applying (15) to both
branches would be incorrect.

## 4. Complete cofactor exclusion w<=64

We also execute a complete finite reduction in w. It is uniform in n;
there is no arbitrary upper search bound on n.

### Large-p case: enumerate divisors of small explicit integers

For a fixed w<=64, (11) leaves the finite range

\[
9w+1\le z\le\left\lfloor\frac{100w-1}{9}\right\rfloor.
\]

For each epsilon define c0,c1 by (3). The v15 transfer (4) implies
n/gcd(n,3)|c0^3. Hence all possible n occur among the numbers

\[
n=g d,\quad g\in\{1,3\},\quad d\mid c_0^3,
\quad \gcd(n,3)=g.
\]

In the small branch the stronger Q0^2|c0^3 lets one use

\[
d\mid\prod_{q\mid c_0}q^{\lfloor3v_q(c_0)/2\rfloor}
\]

instead. Test n>=104 and the second transfer Q1|c1^3 (or Q1^2|c1^3).
Finally require w|n^2+2, p=(n^2+2)/w>6n-9, and

\[
(r-\varepsilon)^2=zp+6n-8.
\]

This covers every possible original solution with w<=64 and large p.
We deliberately do not require p to be prime in the finite calculation:
a larger necessary set is excluded, without any primality dependency.

The exact reduction gives:

| Stage | Count |
|---|---:|
| (w,z,epsilon) coefficient families | 8,712 |
| Generated (g,d) divisor points | 590,028 |
| n>=104 and actual gcd(n,3)=g | 350,188 |
| Second divisor condition | 1,260 |
| w divides n^2+2 | 20 |
| p=(n^2+2)/w>6n-9 | 11 |
| zp+6n-8 is a square | **0** |

Every last case has an explicit consecutive-square witness. With
S=zp+6n-8 and a=floor(sqrt(S)), each row satisfies a^2<S<(a+1)^2:

| w | z | epsilon | n | p | S | a |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 22 | 1 | 676 | 228489 | 5030806 | 2242 |
| 6 | 61 | 1 | 136 | 3083 | 188871 | 434 |
| 6 | 66 | 1 | 676 | 76163 | 5030806 | 2242 |
| 17 | 158 | 1 | 163 | 1563 | 247924 | 497 |
| 17 | 188 | 0 | 160 | 1506 | 284080 | 532 |
| 18 | 172 | 1 | 364 | 7361 | 1268268 | 1126 |
| 22 | 225 | 1 | 784 | 27939 | 6290971 | 2508 |
| 33 | 323 | 1 | 349 | 3691 | 1194279 | 1092 |
| 33 | 355 | 0 | 223 | 1507 | 536315 | 732 |
| 33 | 361 | 1 | 289 | 2531 | 915417 | 956 |
| 41 | 394 | 0 | 276 | 1858 | 733700 | 856 |

The largest generated n is 1,816,487,208. This is a derived divisor
candidate, not a scan endpoint and not an original solution.

### Small-p case: the theoretical bound n<384

If p<=6n-9 and w<=64, then n<6w<=384. For each integer
104<=n<=383, factor Q and set F=product q^ceil(v_q(Q)/3).
The equivalence Q|r^3 iff F|r completely enumerates r in the strict
interval 3n<r<10n/3. Exactly four pairs remain:

| n | r | delta |
|---:|---:|---:|
| 169 | 546 | 1 |
| 243 | 792 | 1 |
| 250 | 830 | 5 |
| 361 | 1140 | 1 |

Each contradicts the proved v16 delta>=13. This is an exhaustive
check over the range derived from w<=64, not an extrapolation.

Consequently every prime divisor p of n^2+2 in either branch obeys

\[
\boxed{\frac{n^2+2}{p}>64,\qquad
P^+(n^2+2)<\frac{n^2+2}{64}.}
\tag{17}
\]

Because the cofactor is an integer, the equivalent cofactor statement
is w>=65, and the sharper convenient upper bound is

\[
\boxed{\frac{n^2+2}{p}\ge65,\qquad
P^+(n^2+2)\le\frac{n^2+2}{65}.}
\tag{18}
\]

This extends the v15 w=1 exclusion to a whole cofactor range. For
large n the older polynomial prime bounds may be stronger; (17) is
used together with them, not in place of them.

## 5. Reproduction and verification boundaries

`v17_neighbor_defect_checks.py` uses only Python's standard library.
It checks the exact rational constants, polynomial coefficient
identities, local divisor-transfer consistency cases, the complete
large-p divisor families and square witnesses, and every small-p
index in the theoretically bounded range. It writes a compressed
full certificate and a readable summary. Factorizations, all 8,712
family count records, all 1,260 second-divisor candidates, all final
square witnesses, and all small-index records are retained.

The generic theorems in Sections 2-3 rest on the written proofs.
Finite local consistency samples do not prove them by extrapolation.
The finite calculation in Section 4 is complete because of the
explicit cofactor range and divisor reduction proved before it.
The prime factors of c0 are small and checked directly; no external
CAS or primality oracle is required. No original solution is found.

The full four-variable equation, the whole offset-three branch,
unbounded delta, and unbounded J remain unresolved. No new Lean or
DeepSeek execution is claimed. The old H>=21 and global candidate
count O(sqrt(X) log X) are unchanged.
