# Large-prime branch: a cyclotomic obstruction and exclusion of Phi_3(p)=7q

## Scope and inputs

The original equation remains
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
In the lower ell=1 branch with a prime p>j dividing i, the earlier
proofs give
\[
i=jp^3,\quad k=p,\quad j\text{ odd},\quad j+2\le p<2j.
\tag{1}
\]
The previous complete ell=1,j<=100 exclusion implies j>=101 and
p>=103 for every remaining solution. Put
\[
A=\binom{jp^3}{j},\quad X=\binom{j^2p^6}{j^2},
\quad L=\binom Ap,\quad N=\Phi_3(p)=p^2+p+1.
\]
The equation is L=X+p². We use G(j,p)>0 from
v5_large_prime_localization.md.

**New conclusions.**
Every prime-power factor q^(v_q(N)) is at most j². Equivalently,
N has at least two distinct prime divisors other than3.
Moreover, the entire additional class N=7q, with q prime, is
impossible. Its proof reduces all p to17 explicitly listed integers,
none of which satisfies a necessary quadratic equation.

No upper bound on p is assumed in advance. These results do not
classify the whole original equation and are not Lean formalizations.

## 1. An explicit bound from the real localization

Write the previously proved function as
\[
\begin{aligned}
G(x,p)={}&x[p(1+3\log p)-x(1+6\log p)]\\
&+p-(p+\tfrac12)\log p-\tfrac p2\log(2\pi x)+\log x.
\end{aligned}
\]
For p>=23 and x>p/2, the second line is negative: x>1,
log(2pi x)>log x, and log p>1. Hence G(j,p)>0 implies
\[
\boxed{
\frac p2<j<
p\frac{1+3\log p}{1+6\log p}
=p\left(\frac12+\frac1{12\log p+2}\right)
<\frac{10p}{19}.}
\tag{2}
\]
The final inequality uses log p>3; for example e<11/4 and
(11/4)^3<23 prove that bound. In particular
\[
j^2<\frac{100p^2}{361}<\frac{p^2}{3}.
\tag{3}
\]

## 2. A prime-power factor of Phi_3(p) cannot exceed j²

**Theorem.** Every solution in (1) satisfies
\[
\boxed{q^{v_q(N)}\le j^2\quad\text{for every prime }q.}
\tag{4}
\]

Suppose D=q^a divides N and D>j². Write N=cD. Since j>p/2,
\[
0<c<4(p^2+p+1)/p^2<5 \qquad(p\ge23).
\]
The integer N is odd, so c=1 or3.

Every prime divisor q!=3 of N is1 modulo3: p³=1 modulo q, but
p=1 modulo q would imply q divides3, so p has order3 modulo q.
Also v_3(N)<=1, because if p=1+3u then
N=3(1+3u+3u²), and otherwise3 does not divide N.
Thus q=3 cannot give D>j², and q>=7.

Put h=floor(a/2)+1. Since j²<q^a, one has
j<q^ceil(a/2), so every 1<=m<=j obeys
v_q(m)<=ceil(a/2)-1. The exact product
\[
A=\prod_{m=1}^j\left(1+\frac{j(p^3-1)}m\right)
\tag{5}
\]
has every correction divisible by q^h in the q-adic sense:
\[
v_q(j(p^3-1)/m)\ge a-\lceil a/2\rceil+1=h.
\]
Consequently
\[
\boxed{A\equiv1\pmod{q^h}.}
\tag{6}
\]
Furthermore p²<N=cq^a<=3q^a, while
q^(2h)>=q^(a+1)>3q^a. Therefore p<q^h.

It follows that q divides L=C(A,p). This follows either from Lucas,
or directly from
\[
\binom Ap=\frac{A(A-1)}{p(p-1)}\binom{A-2}{p-2}:
\]
q does not divide p, v_q(p-1)<h, and v_q(A-1)>=h.

Meanwhile q^a divides p^6-1 and j²<q^a. Thus j²p^6=j² modulo
q^a and Lucas gives
\[
\boxed{X\equiv1\pmod q.}
\tag{7}
\]
Equivalently, in the product
X=product_(m=1)^(j²)(1+j²(p^6-1)/m), every correction has positive
q-adic valuation.

The equation would require p²=-1 modulo q, while p³=1 modulo q.
Multiplication by p gives p=-1 modulo q, so p²=1 modulo q as well.
Hence q divides2, contradicting q>=7. This proves (4).

### Equivalent factor-count consequence

If N has only one prime divisor other than3, then N=q^a or3q^a,
since v_3(N)<=1. Its q-power factor is at least N/3>p²/3>j²,
contrary to (4). Thus
\[
\boxed{\Phi_3(p)\text{ has at least two distinct prime divisors other than3}.}
\tag{8}
\]
Conversely, if two such primes divide N, every full prime-power
factor for q!=3 is at most N/7<p²/4<j²; the factor3 is also below
j². Thus (4) and (8) are equivalent in the proved interval.

This includes genuine prime-power obstructions. For example
Phi_3(313)=3*181², so p=313 is excluded independently of the
location of its unique real candidate.

## 3. Complete exclusion of Phi_3(p)=7q with q prime

Assume
\[
N=p^2+p+1=7q,\qquad q\text{ prime}.
\tag{9}
\]
We work in the actual surviving domain p>=103. The intermediate
bounds below hold already for p>=23.

Here q>p, since N>7p. From (2),
\[
\boxed{q<j^2<2q.}
\tag{10}
\]
Indeed p²/4>N/7 follows from 3p²-4p-4>0, and
100p²/361<2N/7 follows from 700<722.

### 3.1 A quadratic congruence from the shared prime

Since p³-1=7q(p-1), jp³=j modulo q, and j<q. Thus A=1 modulo q.
Since 1<p<q, L=0 modulo q.

For the other inner binomial,
\[
j^2p^6=j^2+14j^2q(p-1)+49j^2q^2(p-1)^2.
\]
By (10), the bottom j² has q-place digit1 and low digit j²-q.
The top has the same low digit. Lucas therefore gives
\[
\boxed{X\equiv1+14j^2(p-1)\pmod q.}
\tag{11}
\]
The equation implies
14j²(p-1)+p²+1=0 modulo q. Use p²+p+1=0 modulo q,
then multiply by p+2 and use (p-1)(p+2)=-3 modulo q.
The result is
\[
\boxed{q\mid42j^2+p-1.}
\tag{12}
\]

### 3.2 Its integer quotient must equal76

Set
\[
t=\frac{42j^2+p-1}{q}
=\frac{294j^2+7p-7}{p^2+p+1}.
\]
From j>p/2,
\[
t-70>
\frac{(7/2)(p^2-18p-22)}{p^2+p+1}>0
\qquad(p\ge23).
\]
Thus the integer t is at least71. From j<10p/19, t<82, because
\[
82(p^2+p+1)-
\left(\frac{29400}{361}p^2+7p-7\right)
=\frac{202}{361}p^2+75p+89>0.
\]
Hence 71<=t<=81.

The numerator 42j²+p-1 is even and q is odd, so t is even.
Every q>3 dividing Phi_3(p) is1 modulo3. Equation (9) implies
p=2 modulo3, and (12) then gives t=1 modulo3.
The only possibility is t=76. Therefore
\[
\boxed{294j^2=76p^2+69p+83.}
\tag{13}
\]

### 3.3 The real bound proves p<19683

Equation (13) requires
\[
j^2/p^2>76/294=38/147.
\tag{14}
\]
If p>=3^9, then log p>=9log3>39/4. The last constant is exact:
e<11/4, while
\[
4^{13}3^{12}-11^{13}=1141689649093>0,
\]
so e^13<3^12 and log3>13/12. The bound e<11/4 follows by
summing the exponential series through1/4! and bounding its
remaining tail by1/100.

The middle bound in (2) would give
\[
j/p<\frac12+\frac1{119}=\frac{121}{238}.
\]
But
\[
38\cdot238^2-147\cdot121^2=245>0,
\]
so (121/238)²<38/147, contradicting (14). Hence
\[
\boxed{103\le p<19683.}
\tag{15}
\]
This is a proved upper bound, not an arbitrarily chosen search limit.

### 3.4 Exactly17 integers remain

Equation (13) modulo16, using odd p,j, gives p=11 modulo16.
Modulo49 its right side factors as
\[
76p^2+69p+83\equiv27(p-9)(p-32)\pmod{49}.
\]
The two roots differ by23, a unit modulo7. Thus p=9 or32 modulo49.
Together with p=2 modulo3, the Chinese remainder theorem gives
\[
\boxed{p\equiv107\text{ or }1355\pmod{2352}.}
\tag{16}
\]
Within (15), the first class gives9 integers and the second gives8.
For each one put S(p)=(76p²+69p+83)/294. The following table gives
an integer b with b²<S(p)<(b+1)².

| p | b | S(p)-b² | (b+1)²-S(p) |
|---:|---:|---:|---:|
| 107 | 54 | 69 | 40 |
| 1355 | 689 | 216 | 1163 |
| 2459 | 1250 | 1165 | 1336 |
| 3707 | 1884 | 3729 | 40 |
| 4811 | 2446 | 1461 | 3432 |
| 6059 | 3080 | 5065 | 1096 |
| 7163 | 3642 | 957 | 6328 |
| 8411 | 4276 | 5601 | 2952 |
| 9515 | 4837 | 9328 | 347 |
| 10763 | 5472 | 5337 | 5608 |
| 11867 | 6033 | 9616 | 2451 |
| 13115 | 6668 | 4273 | 9064 |
| 14219 | 7229 | 9104 | 5355 |
| 15467 | 7864 | 2409 | 13320 |
| 16571 | 8425 | 7792 | 9059 |
| 17819 | 9059 | 17864 | 255 |
| 18923 | 9621 | 5680 | 13563 |

All entries in the final two columns are positive. Thus no S(p) in
the complete set is a square. Primality tests are unnecessary for
this completion: even the composite p in the residue classes fail.
This contradicts (13) and proves
\[
\boxed{
i=jp^3,\ k=p,\ \ell=1,\quad
p^2+p+1=7q\text{ with }q\text{ prime}
\quad\Longrightarrow\quad\text{no solution}.}
\tag{17}
\]

## 4. Meaning, verification, and remaining scope

The new ingredient is a different prime divisor q of Phi_3(p),
not merely an expansion modulo a higher power of p. Its digits
force the outer binomial to vanish while controlling the
squared-index binomial. In the 7q case, this yields a fixed
quadratic equation; its slope conflicts with the real localization
for large p, leaving the explicit17-case table.

The companion v6_large_prime_cyclotomic_checks.py checks the
complete17-case reduction by separate enumeration methods,
the integer constants, and nontrivial instances of the binomial
residue identities. The report is
v6_large_prime_cyclotomic_verification.json.

Cases such as Phi_3(p)=7q^a with a>=2, or products with other
cofactors, are not excluded by Section3 unless they also fall under
Section2. The full large-prime branch remains unresolved. The
proof does not rely on a heuristic about the randomness of the
harmonic residues, and no new Lean formalization is claimed.

### Audit status

The root agent independently checked the full proof, including the
prime-power valuation argument and factor-count equivalence, the
strict bound j<10p/19, the 7q digit formula, the quotient t=76,
the bound p<3^9, the CRT classes, and coverage of the17-case table.
That audit passed without correction.

The v6_offset_prime_powers agent then independently audited the
entire proof and the checking code/report. The cofactor reduction,
all prime-power precisions, both Lucas residue computations, the
quotient restrictions, the real bound, the CRT calculation, and both
enumerations of the17 candidates passed without correction.

