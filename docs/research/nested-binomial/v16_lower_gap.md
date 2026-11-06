# v16: a uniform three-fifths lower bound for the offset

Date: 2026-11-06 JST. Written proof; no new Lean, DeepSeek API, or CAS
complete-solver execution is claimed.

## 1. Scope and theorem

Retain the original squared-index binomial equation and the branch
ell=1, j=i-3, including both k=r and k=A-r. Put

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad
g=\gcd(n,3),\quad d=\gcd(n-1,6),\quad M=gd,
\]

\[
Q=\frac{n(n-1)}M.
\]

The established branch inputs are

\[
n\ge104,\quad 3n<r<10n/3,\quad M\in\{1,2,3,6\},\quad Q\mid r^3.
\tag{1}
\]

They are recorded in the existing `v6_offset_composite.md` and
`v6_common_divisor.md`. No logarithmic upper bound, v14 Thue result,
v15 Pell exclusion, or bound on the primitive defect H is needed here.

Set t=r-3n. Then every solution in this branch satisfies

\[
\boxed{n^3<2^{30}(t+3)^5.}
\tag{2}
\]

Equivalently,

\[
\boxed{r-3n+3>\frac{n^{3/5}}{64}.}
\tag{3}
\]

The proof actually gives the smaller exact coefficient

\[
n^3<\frac{124567589888}{153}(t+3)^5<2^{30}(t+3)^5.
\tag{4}
\]

The constant 64 is chosen for a simple statement, not asserted optimal.
This is a lower bound for the distance from 3n. It does not improve the
v15 O(sqrt(X) log X) counting theorem by itself, and does not exclude
the entire branch.

## 2. The first integer separation

Since r>3n and r<10n/3, the integer t satisfies

\[
1\le t<n/3.
\]

Also n/g divides r^3 and n, so n/g divides t^3. Thus
t^3>=n/g>=104/3>27, giving

\[
t\ge4,\qquad u:=t+3\ge7.
\tag{5}
\]

Define

\[
D=9t^2+27t+27.
\]

The exact polynomial identity

\[
r^3=(27n+27t+27)n(n-1)+Dn+t^3
\tag{6}
\]

and Q|r^3 show that

\[
\boxed{h=\frac{M(Dn+t^3)}{n(n-1)}\in\mathbb Z_{>0}.}
\tag{7}
\]

In particular,

\[
hn^2-(h+MD)n-Mt^3=0.
\tag{8}
\]

Two elementary upper bounds on h will be used. First,

\[
\frac{h}{Mt}
=\frac{9t+27+27/t+t^2/n}{n-1}
<\frac{28n/9+54}{n-1}<4.
\tag{9}
\]

The first strict inequality uses t<n/3; the second follows from
8n/9-58>0 when n>=104. Hence h<4Mt.

Next, n-1>=3t because n and t are integers and n>3t. Therefore

\[
\begin{aligned}
\frac{hn}{M}
&=D+\frac{D+t^3}{n-1}\\
&\le D+\frac{D+t^3}{3t}\\
&=\frac{28}{3}t^2+30t+36+\frac9t\\
&<\frac{28}{3}(t+3)^2.
\end{aligned}
\tag{10}
\]

The last difference is 26t+48-9/t>0. In particular,

\[
\boxed{h<\frac{28M u^2}{3n}.}
\tag{11}
\]

For comparison, merely using h>=1 in (7) gives an O(sqrt(n)) lower
bound for t. The second integer separation below gives the exponent
3/5 instead.

## 3. A rational quadratic approximation to an integer square root

Let P=h+MD. Equation (8) gives the integer

\[
x=2hn-P>0,\qquad x^2=P^2+4hMt^3.
\tag{12}
\]

Positivity follows from hn=P+Mt^3/n>P. Define the following rational
quadratic polynomial in t:

\[
q=P+\frac{2h}{9}(t-3)-\frac{2h^2}{729M}.
\tag{13}
\]

Its leading coefficients were chosen so that the cubic and quadratic
terms cancel in the difference of squares. Exact expansion gives

\[
\begin{aligned}
R:=x^2-q^2
={}&24Mht+36Mh+\frac{28h^2}{27}
 +\frac{8h^3t}{6561M}
 +\frac{4h^3}{2187M}
 -\frac{4h^4}{531441M^2}.
\end{aligned}
\tag{14}
\]

All parts of this identity can be checked by multiplication of
polynomials with integer coefficients.

### Positivity and lower size of q

Using h<4Mt from (9) and dropping positive terms from (13),

\[
q>M\left[\left(9-\frac{32}{729}\right)t^2+27t+27\right].
\]

Consequently

\[
\begin{aligned}
q-\frac{17M}{3}(t+3)^2
&>\frac M{729}\left(2398t^2-5103t-17496\right)\\
&=\frac M{729}\left(2398(t-4)^2+14081(t-4)+460\right)>0.
\end{aligned}
\tag{15}
\]

The last inequality uses t>=4. Thus q>17M u^2/3>0.

### Positivity of R

The potentially negative final term in (14) combines with its cubic
coefficient term as

\[
\frac{8h^3t}{6561M}-\frac{4h^4}{531441M^2}
=\frac{4h^3}{531441M^2}(162Mt-h)>0,
\]

by h<4Mt. All the remaining terms in (14) are positive. Hence R>0,
so x>q>0.

## 4. The fixed denominator forces a second integer gap

Because x-P=2(hn-P) is an even integer, (13) gives

\[
x-q=\frac{2}{729M}
\left(729M(hn-P)-81Mh(t-3)+h^2\right).
\tag{16}
\]

The parenthesized expression is a positive integer, since x>q. Thus

\[
x-q\ge\frac{2}{729M}.
\]

Using (15),

\[
\boxed{R=(x-q)(x+q)>
\frac{4q}{729M}>
\frac{68u^2}{2187}.}
\tag{17}
\]

On the other hand, substitute t=u-3 in (14) and drop only negative
terms to obtain

\[
R<24Mhu+\frac{28h^2}{27}+\frac{8h^3u}{6561M}.
\]

Divide by h^3*u/M, which is positive. Since M<=6, h>=1, u>=7,

\[
\begin{aligned}
\frac{MR}{h^3u}
&<\frac{24M^2}{h^2}+\frac{28M}{27hu}+\frac8{6561}\\
&\le864+\frac89+\frac8{6561}
=\frac{5674544}{6561}.
\end{aligned}
\tag{18}
\]

Combining (17)-(18) and cancelling u>0 gives

\[
\boxed{u<\frac{1418636}{51}\frac{h^3}{M}.}
\tag{19}
\]

Finally, use (11) and M^2<=36:

\[
\begin{aligned}
n^3
&<\frac{1418636}{51}\left(\frac{28}{3}\right)^3M^2u^5\\
&\le\frac{124567589888}{153}u^5
<2^{30}u^5.
\end{aligned}
\tag{20}
\]

The positive difference in the last constant comparison is exactly

\[
2^{30}-\frac{124567589888}{153}
=\frac{39714909184}{153}>0.
\]

This proves (2)-(4) for the entire branch, under (1).

## 5. Verification and meaning

The universal conclusion is the written algebraic proof above.
Finite integer checks are supplementary and do not supply an
unproved completeness assumption. `v16_lower_gap_checks.py` was executed
and returned PASS. Its Laurent-polynomial coefficient arithmetic checks
five exact identities, and rational arithmetic checks all displayed
constants. A consistency check for 104<=n<=100000 found 45 first indices
and 48 pairs passing the exact necessary divisibility and coarse
interval conditions; every proof inequality held on all 48 pairs.
Those examples are not solutions of the original binomial equation.

Reproduce these checks with:

```sh
python3 v16_lower_gap_checks.py --limit 100000 --output reproduced_lower_gap_checks.json
```

The source and proof-note hashes are recorded in
`v16_lower_gap_checks.json`. No claim that checking the 48 pairs proves
the universal theorem is made.

Combined with the existing logarithmic upper bound, the admissible
offset lies in

\[
\max\left(3,\frac{n^{3/5}}{64}-3\right)<r-3n
<\frac{3n}{4\log n}\qquad(n\ge1024).
\]

The inequalities are compatible for arbitrarily large real n. This
theorem therefore neither establishes a global finite upper bound
on n nor solves the original four-variable problem. It excludes an
explicit region close to r=3n uniformly in all prime factors and H.
