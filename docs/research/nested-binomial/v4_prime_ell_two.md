# Prime first upper index, ell = 2, and i >= 2j

## Statement and prerequisites

For the original squared-index nested-binomial equation, there is no solution
in the lower branch `B <= A/2` with `ell = 2`, `i = p` prime, and `p >= 2j`.

The proof below excludes all `p >= 1,000,000` uniformly. The smaller range is
reduced to an explicitly finite set by the same necessary congruences and is
covered by `v4_prime_ell_two_finite.py` and its certificate/verifier report.
The previously certified `max(j,ell) <= 20` handles `j <= 20`.

For the remaining cases `j >= 21`, hence `p >= 43`, put

\[
A=\binom pj,\quad B=\binom k2,\quad
X=\binom{p^2}{j^2},\quad Y=\binom{k^2}{4}.
\]

The theorem is:

\[
\boxed{\ell=2,\ i=p\text{ prime},\ p\ge2j,\ B\le A/2
\quad\Longrightarrow\quad\text{no solution}.}
\]

In the lower branch `r=B`. Since `A>=C(2j,j)`, the proved height-gap lemma
in `sharp_q_bounds.md`, Section 4, gives

\[
0<B<2j\le p. \tag{1}
\]

## 1. A small finite set of residue types

Write `A=pu`. The product formula gives

\[
u\equiv(-1)^{j-1}j^{-1}\pmod p,
\qquad p^2\mid X.
\]

Since `0<B<p`, the identity `B*C(A,B)=A*C(A-1,B-1)` shows that the
left side has valuation exactly one at `p`. Thus `p|Y`. From
`B=k(k-1)/2<p` we have `k+1<p`. Hence `p` cannot divide `k^2` or
`k^2-1`. Because `24` is invertible modulo `p`,

\[
k^2=mp+c,\qquad c\in\{2,3\},\quad m\in\{1,2\}. \tag{2}
\]

Indeed `k^2<2p+k<3p`, while `m=0` would give `k^2=2` or `3`.

Normalize the equation by dividing by `p` and reducing modulo `p`.
Set `epsilon=(-1)^(j+B-2)`. Then

\[
\frac{1}{p}\binom AB\equiv\frac{\varepsilon}{jB},
\qquad
\frac Yp\equiv
\begin{cases}-m/12,&c=2,\\m/4,&c=3.\end{cases}
\pmod p.
\]

As `2B=mp+c-k`, and `(c-k)(c+k) == c(c-1) (mod p)`, this implies

\[
\boxed{
\begin{array}{ll}
c=2:&mj\equiv-12\varepsilon(k+2)\pmod p,\\
c=3:&3mj\equiv4\varepsilon(k+3)\pmod p.
\end{array}} \tag{3}
\]

For each `(k,m,c)`, these conditions leave at most two residues for `j`
between `1` and `p-1`. They will also force useful real locations of `j/p`.

## 2. Entropy estimates with certified constants

Let `H(x)=-x log(x)-(1-x)log(1-x)`. For `0<K<N`,

\[
\frac{e^{NH(K/N)}}{N+1}\le\binom NK\le e^{NH(K/N)}. \tag{4}
\]

For the upper bound, take the `K`th term in the binomial distribution with
parameter `K/N`. For the lower bound, that term is a mode and at least
`1/(N+1)` of the sum, which is one. The usual adjacent-term ratio proves
the mode assertion directly. Also `H` increases on `(0,1/2)`.

The rational inequalities used below are

\[
H(17/50)<13/20,\quad H(64/625)>33/100,
\quad H(49/100)>69/100,\quad H(1/4)<57/100. \tag{5}
\]

`v4_entropy_constants.py` verifies (5) with rational log enclosures. For
`z>0`, put `u=(z-1)/(z+1)`. Truncating
`log(z)=2 sum_(n>=0) u^(2n+1)/(2n+1)` after `N` terms has absolute error
at most `2|u|^(2N+1)/((2N+1)(1-u^2))`. The checker uses this exact
rational error bound, not floating-point values.

## 3. Uniform exclusion for p >= 1,000,000

### 3.1 m=1, c=2

Here `k^2=p+2<2p`, so `k<p/500`. Thus
`u=12(k+2)<p/40`. Equation (3) says `j` is either `u` or `p-u`.
The condition `j<=p/2` forces `j=u<p/40`.
But `B=(p+2-k)/2>499p/1000`, and (1) requires
`j>B/2>499p/2000`. Contradiction.

### 3.2 m=1, c=3

Again `k<p/500`, and `v=4(k+3)<p/100`.
By (1), `499p/2000<j<=p/2`. Equation (3) now forces

\[
p-v\le3j\le p+v,
\qquad 8/25<j/p<17/50. \tag{6}
\]

The only possible multiple of `p` in `3j=hp+/-v` is `h=1`, since
`0.7485p<3j<=1.5p` and `v<0.01p`.

By (4)--(6), and `B<p/2`,

\[
\binom AB\le A^B<e^{(13/40)p^2},
\qquad
X>\frac{e^{(33/100)p^2}}{p^2+1}.
\]

Since `log(p^2+1)<2log(p+1)<2p<p^2/200` for `p>400`, the second
quantity exceeds the first. Thus `L<X`, which contradicts `L=X+Y`.

### 3.3 m=2, either c: congruences already suffice

Now `k^2=2p+c<3p`, whence `k<p/50` and

\[
B=p+(c-k)/2>99p/100,
\qquad 49/100<j/p\le1/2. \tag{7}
\]

If `c=2`, cancellation of 2 in (3) gives
`j == +/-6(k+2) (mod p)`. Put `u=6(k+2)<p/5`. Then `j` is
either `u` or `p-u`, incompatible with `0.49p<j<=0.5p`.

If `c=3`, cancellation of 2 in (3) gives
`3j == +/-2(k+3) (mod p)`. Put `v=2(k+3)<p/20`.
But `1.47p<3j<=1.5p`, so its residue modulo `p` is between
`0.47p` and `0.5p`. It cannot be either `v` or `p-v`.

Thus both subcases are impossible using only (3) and (7).

This excludes every residue type for all primes above the threshold.

## 4. Finite range and verification scope

For `43<=p<1,000,000`, (2) gives `k<=1414`. Enumerate `m=1,2`,
`c=2,3`, let `p=(k^2-c)/m` when integral, test primality, and use (3)
to enumerate at most two candidates for `j`. Retain only the previously
proved necessary ranges and parity sign. Every retained candidate is
tested by an exact modular witness for the ORIGINAL equation.

The finite certificate report records its exact count and independent
verification. The theorem in this note is a written analytic proof plus
an integer certificate; it has not been formalized in Lean.
