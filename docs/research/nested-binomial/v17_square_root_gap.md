# v17: exact classification at the square-root boundary

Date: 2026-11-06 JST. Written reductions and a complete exact-integer
certificate; no new Lean execution, DeepSeek API call, complete CAS
integral-point solver, or external peer review is claimed.

## 1. Scope and conclusions

Retain the **squared-index** equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
 =\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

and the branch \(\ell=1,j=i-3\), including both \(k=r\) and \(k=A-r\).
Set

\[
n=i,\quad A=\binom n3,\quad r=\min(k,A-k),\quad t=r-3n,
\]

\[
M=\gcd(n,3)\gcd(n-1,6),\qquad Q=\frac{n(n-1)}M.
\]

The earlier necessary conditions are

\[
n\ge104,\quad M\in\{1,2,3,6\},\quad Q\mid r^3,
\quad 3n<r<10n/3.
\tag{1}
\]

They are established in `v6_offset_composite.md` and
`v6_common_divisor.md`. The v16 lower-gap proof is the sole additional
written input to the new reduction below.

**Theorem A (necessary-condition classification).** Under (1),

\[
\boxed{t^2\ge9n.}
\tag{2}
\]

Equality holds for exactly the following 13 values of \(s\), with
\(n=s^2\) and \(r=3s(s+1)\):

\[
\boxed{s\in\{13,19,25,28,37,55,73,82,109,163,217,325,649\}.}
\tag{3}
\]

This is a classification of the stated necessary conditions, not of
solutions to the original binomial equation.

**Theorem B (original equation).** None of the 26 original k branches
from (3) satisfies the original equation. Consequently every original
solution in this branch must satisfy

\[
\boxed{r>3n+3\sqrt n.}
\tag{4}
\]

**Theorem C (residual size).** Define the positive integer from v16

\[
h=\frac{M\{(9t^2+27t+27)n+t^3\}}{n(n-1)}.
\tag{5}
\]

Under (1), one has \(h>81M\). This integer gap is sharp for (1):
\(n=421201=649^2\), \(r=1265550=3\cdot649\cdot650\) has \(M=6\)
and \(h=487=81M+1\). That pair has \(\delta=6\) and is not an original
solution.

**Theorem D (stronger original-equation consequences).** Original
solutions in this branch also satisfy

\[
\boxed{h\ge93M,\qquad t+3>\sqrt{31n/3}.}
\tag{4a}
\]

Theorem A is proved by the finite, exhaustively certified reduction
below. Theorem B can be checked directly by the saved 26 congruence
witnesses, independently of the v16 exclusion \(\delta\le12\).

## 2. What is inherited from the v16 integer separation

Put

\[
D=9t^2+27t+27,\quad P=h+MD,\quad x=2hn-P,
\quad u=t+3.
\]

The earlier proof establishes, solely from (1),

\[
t\ge4,\quad h\in\mathbb Z_{>0},\quad h<4Mt,
\quad h<\frac{28Mu^2}{3n},
\tag{6}
\]

\[
x^2=P^2+4hMt^3,
\quad q=P+\frac{2h}{9}(t-3)-\frac{2h^2}{729M},
\]

\[
x>q>\frac{17M}{3}u^2>0,
\tag{7}
\]

and, for \(R=x^2-q^2\),

\[
R<24Mhu+\frac{28h^2}{27}+\frac{8h^3u}{6561M}.
\tag{8}
\]

All sign checks and exact polynomial expansions for (6)-(8) are in
`v16_lower_gap.md`. No logarithmic upper bound, fixed H, Pell
enumeration, or prime cutoff is needed for them.

The positive residual is

\[
J=\frac{729M}{2}(x-q)
=729M(hn-P)-81Mh(t-3)+h^2\in\mathbb Z_{>0}.
\tag{9}
\]

Its stronger divisibility, not used in v16, is central here.

## 3. Only twelve possible reduced denominators

Write

\[
g=\gcd(h,81M),\qquad h=ga,\qquad81M=gb,
\qquad\gcd(a,b)=1.
\tag{10}
\]

Thus \(h/(81M)=a/b\) in lowest terms and

\[
b\mid486,\qquad
b\in\{1,2,3,6,9,18,27,54,81,162,243,486\}.
\tag{11}
\]

Indeed each possible \(81M\) is a divisor of 486. Expanding (9) gives

\[
J=h^2+81M\{h(9n-t-6)-81M(t^2+3t+3)\}.
\]

Consequently \(g^2\mid J\), and the positive integer

\[
\boxed{j=J/g^2
=a^2+ab(9n-t-6)-b^2(t^2+3t+3)}
\tag{12}
\]

satisfies

\[
\boxed{j\equiv a^2\pmod b.}
\tag{13}
\]

The auxiliary residual j in this note is distinct from the original
binomial index \(j=i-3\); equation (12) defines it locally. In code it
is the residual field `j`, while the original binomial lower index is
always supplied explicitly as \((n-3)^2\).

### A uniform upper bound for the residual

From (7) and (9),

\[
R=(x-q)(x+q)>\frac{68J u^2}{2187}.
\]

Use (8), and then \(h/u<4M\), to get

\[
\begin{aligned}
J
&<\frac{2187}{68}
 \left(\frac{24Mh}{u}+\frac{28h^2}{27u^2}
       +\frac{8h^3}{6561Mu}\right)\\
&<\frac{61560}{17}M^2+\frac8{51}h^2.
\end{aligned}
\]

Dividing by \(g^2\), and using \(M/g=b/81\), yields

\[
\boxed{0<j<\frac{216a^2+760b^2}{1377},
\qquad j\equiv a^2\pmod b.}
\tag{14}
\]

Every comparison is strict where needed. The positive j values are
therefore exactly covered by

\[
j=j_0+qb,\quad q\ge0,\quad
j\le\left\lfloor\frac{216a^2+760b^2-1}{1377}\right\rfloor,
\]

where \(j_0\) is the least positive integer congruent to \(a^2\bmod b\).

### Polynomial heights for a fixed reduced numerator

Using \(J\ge g^2\) in the same estimates, now retaining \(u\ge7\),

\[
g^2u<\frac{13122}{17}Mh+\frac{81}{17}h^2+
\frac{2}{51M}h^3.
\]

Thus

\[
\boxed{t+3<\frac{27a(2a^2+3ab+6b^2)}{17b},}
\tag{15}
\]

and (6) gives

\[
\boxed{n<\frac{84a(2a^2+3ab+6b^2)^2}{289b}.}
\tag{16}
\]

These are uniform in all n and all prime factors. For fixed a, there
are only twelve possible b, and n has a bound of degree five in a.
This does not bound a itself, and it is not an improvement of the
previous global first-index counting theorem by itself.

## 4. Exact quadratic reconstruction, in both directions

For a fixed \((a,b,j)\) satisfying (11)-(14), define

\[
\begin{aligned}
\mathcal A&=jb^2,\\
\mathcal B&=j(3b^2+2ab)-2ab(a^2+3b^2),\\
\mathcal C&=j(3b^2+3ab-2a^2+j)
-a(9b^3+21ab^2+3a^2b-a^3).
\end{aligned}
\tag{17}
\]

Every original necessary-condition pair must give

\[
\boxed{\mathcal A t^2+\mathcal B t+\mathcal C=0,}
\tag{18}
\]

followed by

\[
\boxed{
n=\frac{b^2(t^2+3t+3)+ab(t+6)-a^2+j}{9ab}.
}
\tag{19}
\]

To check the derivation without division ambiguities, let N denote
the numerator of (19). Direct polynomial multiplication gives

\[
N^2-\{9ab+b^2(t^2+3t+3)\}N-ab^3t^3
=\mathcal A t^2+\mathcal B t+\mathcal C.
\tag{20}
\]

Since \(N=9abn\), the left side equals

\[
ab^2\{81a n(n-1)-b(9(t^2+3t+3)n+t^3)\}.
\]

This is precisely (5), using \(h/(81M)=a/b\).

Conversely, suppose (18)-(19) give integers \(n\ge104\), \(t\ge4\)
with \(3t<n\). Compute the actual
\(M=\gcd(n,3)\gcd(n-1,6)\), and require \(b\mid81M\).
Then \(h=81Ma/b\) is a positive integer, and (20) proves (5).
The cubic division identity from v16 shows

\[
\frac{r^3}{Q}=27M(n+t+1)+h\in\mathbb Z,
\qquad r=3n+t.
\]

Thus the original necessary conditions (1) are recovered. The full
binomial equation is an additional condition and is not implied by
this converse.

For the discriminant computation set

\[
\begin{aligned}
F(a,b,j)={}&4a^6+24a^4b^2-12a^4j+36a^2b^4
 +60a^2b^2j\\
&+12a^2j^2-3b^2j^2-4j^3.
\end{aligned}
\tag{21}
\]

Then

\[
\mathcal B^2-4\mathcal A\mathcal C=b^2F.
\]

A rational t therefore requires \(F\ge0\) to be an integer square.
For \(y=\sqrt F\), both possible roots are

\[
\boxed{
t=\frac{2a(a^2+3b^2)-j(3b+2a)\ \pm y}{2bj}.
}
\tag{22}
\]

All denominators here are positive. Both signs, including any repeated
root only once, are checked in the certificate.

## 5. The square-root region has a complete finite coefficient domain

Assume additionally \(t\le3\sqrt n\), and write \(s=\sqrt n\), which
need not be an integer at this stage. The right side of (5) divided
by M increases with t>0 for fixed n. At \(t=3s\) it is exactly

\[
\frac hM\le81+\frac{108}{s-1}<93,
\tag{23}
\]

because \(n\ge104\) implies \(s>10\). Therefore

\[
\boxed{27a<31b.}
\tag{24}
\]

This is a restriction on a ratio with only the twelve denominators
in (11), so it is a complete finite domain, with no arbitrary n
cutoff. Equations (14), (22), and (19) exhaust it.

The executed certificate gives:

| Stage | Count |
|---|---:|
| Coprime coefficient pairs (a,b), b dividing 486, 27a<31b | 557 |
| Positive residuals satisfying (14) | 94,710 |
| Square reduced discriminants | 272 |
| Reconstructed integer t at least 4 | 30 |
| Reconstructed integer n at least 104 | 13 |
| Actual denominator and strict coarse interval | 13 |
| Pairs with t^2<9n | 0 |
| Pairs with t^2=9n | 13 |
| Original k branches excluded by modular witnesses | 26 |

No filter \(t^2\le9n\) is imposed during reconstruction: all 13
necessary pairs in the larger coefficient domain (24) already have
equality. Thus the strict region is empty and Theorem A follows.
The full per-residual disposition string, every square discriminant,
both roots, all thirty integer-t records, and all thirteen necessary
pairs are stored in `v17_square_root_gap_results.json`.

## 6. Independent elementary classification of equality

If \(t^2=9n\), then 3 divides t and \(s=t/3\) is an integer;
\(n=s^2\) and \(r=3s(s+1)\). For a square n one has

\[
M=3\gcd(s-1,2).
\]

Indeed the factor 3 comes either from \(\gcd(s^2,3)\) or from
\(\gcd(s^2-1,6)\), and the factor 2 occurs exactly when s is odd.
Furthermore

\[
\frac{Mr^3}{n(n-1)}=\frac{27M s(s+1)^2}{s-1},
\]

so

\[
Q\mid r^3
\iff s-1\mid108M
\iff s-1\mid324\gcd(s-1,2).
\tag{25}
\]

Here \(s(s+1)^2\equiv4\pmod{s-1}\), so the equivalence is exact.
If s is even, its odd predecessor divides 324, hence is a power of 3
with exponent from 0 to 4. If s is odd, its even predecessor divides
648, so it is \(2^\alpha3^\beta\) with \(1\le\alpha\le3\),
\(0\le\beta\le4\). Imposing \(n\ge104\), equivalently \(s\ge11\),
gives exactly the list (3). The coarse interval is automatic because
\(s>9\).

The thirteen pairs and their actual reduced defects are:

| s | n | r | delta=Q/gcd(Q,r^2) |
|---:|---:|---:|---:|
| 13 | 169 | 546 | 1 |
| 19 | 361 | 1140 | 1 |
| 25 | 625 | 1950 | 2 |
| 28 | 784 | 2436 | 1 |
| 37 | 1369 | 4218 | 1 |
| 55 | 3025 | 9240 | 1 |
| 73 | 5329 | 16206 | 2 |
| 82 | 6724 | 20418 | 3 |
| 109 | 11881 | 35970 | 1 |
| 163 | 26569 | 80196 | 3 |
| 217 | 47089 | 141918 | 2 |
| 325 | 105625 | 317850 | 3 |
| 649 | 421201 | 1265550 | 6 |

Thus the previous \(\delta\ge13\) theorem would exclude all of them.
For an independent route to Theorem B, this certificate also evaluates
the original binomial residues directly. For both k=r and k=A-r,
a prime at most 13 witnesses

\[
\binom Ak\not\equiv\binom{n^2}{(n-3)^2}+k^2\pmod p.
\]

All 26 witnesses are recorded. Twenty-four have both binomial residues
zero; the two branches for n=5329 have inner residue 3 modulo 5,
and are checked by their complete residues instead. This proves (4).

For Theorem C, the subdomain a<=b is contained in (24). It consists of
486 coefficient pairs, 80,274 residuals, 199 square discriminants,
and seventeen integer t>=4, but gives no integer n>=104. Thus h>81M.
The last row of the table attains h=81M+1, as claimed.

### Stronger consequences of the same complete domain

The computation did not impose \(t^2\le9n\) as a reconstruction filter.
It exhausted **all** necessary pairs with \(h/M<93\), since that is exactly
\(27a<31b\). They are the thirteen pairs just excluded by the original
binomial congruences. Hence every original solution must have

\[
\boxed{h\ge93M.}
\tag{25a}
\]

There is no additional enumeration in this deduction. Together with
\(h<4Mt\), it gives \(93<4t\), so \(t\ge24\) and \(u=t+3\ge27\).
Suppose for a contradiction that \(u^2\le31n/3\). The exact expansion is

\[
\begin{aligned}
&(9t^2+27t+27)n+t^3-93n(n-1)\\
&=(9u^2n-93n^2)+u^3+(120-27u)n-9u^2+27u-27\\
&\le n\left(120-\frac{50u}{3}\right)-9u^2+27u-27<0.
\end{aligned}
\tag{25b}
\]

The first upper bound uses \(9u^2n\le93n^2\) and
\(u^3\le31un/3\). The final expression is negative because
\(u\ge27\), \(n>0\), and \(u^2-3u+3>0\).
On the other hand, (5) and (25a) make its first line nonnegative.
This contradiction proves

\[
\boxed{t+3>\sqrt{31n/3}.}
\tag{25c}
\]

The combined necessary lower bound is therefore

\[
\boxed{t>\max\left(3\sqrt n,\sqrt{31n/3}-3\right).}
\tag{25d}
\]

## 7. Elliptic-curve interpretation and the singular exception

The new residual equation is also an explicit family of cubic curves.
Given a square \(F=y^2\), put

\[
X=4a^2-b^2-4j,\qquad Y=4y.
\]

Exact multiplication of polynomials gives

\[
\boxed{
Y^2=X^3-3b^2(72a^2+b^2)X
+2b^2(648a^4+180a^2b^2-b^4).
}
\tag{26}
\]

The Weierstrass discriminant is

\[
\boxed{-995328a^2b^4(3a-b)^3(3a+b)^3.}
\tag{27}
\]

For positive coprime a,b the only singular pair is (a,b)=(1,3).
It is not discarded: the finite arithmetic procedure (17)-(22) works
there as well. In this case

\[
F(1,3,j)=(j+8)^2(49-4j).
\]

The allowed positive residuals are j=1,4, neither of which gives a
square. Thus it contributes no integer pair.

Conversely, a cubic point from (26) is used only if X recovers an
integer j by \(j=(4a^2-b^2-X)/4\), Y is divisible by 4, the residual
conditions (14) hold, and (22)-(19) pass all original integrality and
interval checks. The cubic equation alone is not equivalent to the
original binomial equation.

This geometric description was not used to invoke a complete elliptic
curve solver. The finite coefficient and residual bounds already
prove completeness of the executed exact checks.

## 8. Reproduction and remaining scope

Run in the directory containing the note and code:

```sh
python3 v17_square_root_gap.py --output reproduced_v17_square_root_gap.json
```

The code uses only the Python standard library. It checks five
polynomial coefficient identities, all finite residual values and
both reconstruction roots, the elementary equality classification,
and the actual original-binomial Lucas witnesses. Source and note
SHA-256 values are saved in the report.

The proof is not obtained by extrapolating a finite scan in n. The
finite domain (11), (14), (24) was proved to contain every point in
the claimed region. The larger four-variable problem and the full
offset-three branch remain unsolved.

The exponent 3/5 from v16 is unchanged. Combined with that result,
original solutions must obey all three

\[
r-3n>3\sqrt n,\qquad
r-3n+3>\sqrt{31n/3},\qquad
r-3n+3>n^{3/5}/64.
\]

The new square-root inequality has the sharp necessary-condition
boundary (3); the 3/5 inequality eventually dominates it for large n.
This work neither improves the global O(sqrt(X) log(X)) first-index
count nor completes the separate DeepSeek/Lean fixed goals.
