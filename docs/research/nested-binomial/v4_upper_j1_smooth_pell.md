# Upper branch with j = 1: three consecutive smooth integers and a Pell reduction

The equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

Throughout this note, assume \(j=1\) and the upper branch. Thus

\[
B=\binom{k}{\ell},\qquad A=i=B+t,\qquad
0<t\le B,\qquad
\binom{B+t}{t}=(B+t)^2+\binom{k^2}{\ell^2}. \tag{1}
\]

We use the previous complete exclusion of \(M\le20\), so
\(\ell=M\ge21\). The earlier endpoint reduction gives
\(k\ge\ell+2\) and \(t\ge\ell+2\). The proved large-height lemma
from `sharp_q_bounds.md`, Section 4, says

\[
A\ge\binom{2\ell}{\ell}\quad\Longrightarrow\quad t<2\ell. \tag{2}
\]

## 1. A new uniform necessary condition

**Theorem.** Every solution of (1) satisfies

\[
\boxed{P^+\bigl((k-1)k(k+1)\bigr)\le2\ell.} \tag{3}
\]

In words: each of the three consecutive integers \(k-1,k,k+1\)
must have no prime factor larger than \(2\ell\).
This strengthens the previous \(\ell^2\)-smoothness restriction on
the long interval \(k-\ell+1,\ldots,k\), for the two integers
\(k-1,k\), and adds a restriction on \(k+1\).

**Proof.** If \(k<2\ell\), all three positive integers are at most
\(2\ell\), so there is nothing to prove. Suppose \(k\ge2\ell\).
Then \(A>B\ge\binom{2\ell}{\ell}\), and (2) gives

\[
\ell+2\le t<2\ell. \tag{4}
\]

Let \(p>2\ell\) be a prime dividing \((k-1)k(k+1)\). In particular
\(p>t+1\), \(p>\ell+1\), and \(\ell!,t!\) are invertible modulo \(p\).
Put \(Y=\binom{k^2}{\ell^2}\). We first show \(p\mid Y\).

If \(p\mid k\), use

\[
\ell^2Y=k^2\binom{k^2-1}{\ell^2-1};
\]

the factor \(\ell^2\) is prime to \(p\). If \(p\mid k-1\) or
\(p\mid k+1\), use instead

\[
\ell^2(\ell^2-1)Y
=k^2(k^2-1)\binom{k^2-2}{\ell^2-2}.
\]

Here \(\ell^2(\ell^2-1)=\ell^2(\ell-1)(\ell+1)\) is prime to \(p\).
Thus \(p\mid Y\) in all three cases.

Because \(p>\ell\), the polynomial formula for \(\binom{k}{\ell}\)
is valid modulo \(p\). If \(k\equiv0\) or \(1\pmod p\), it gives
\(B\equiv0\pmod p\). Hence \(A\equiv t\pmod p\), and because
\(p>t\),

\[
\binom At\equiv\binom tt=1\pmod p.
\]

Equation (1) then implies \(t^2\equiv1\pmod p\), which is impossible:
the prime \(p\) would divide \(t-1\) or \(t+1\), both strictly between
0 and \(p\) by (4).

If \(k\equiv-1\pmod p\), then

\[
B\equiv\binom{-1}{\ell}=(-1)^\ell\pmod p.
\]

For even \(\ell\), \(A\equiv t+1\) and
\(\binom At\equiv t+1\), so (1) implies
\(t(t+1)\equiv0\pmod p\), again impossible.
For odd \(\ell\), \(A\equiv t-1\) and
\(\binom At\equiv0\), so (1) implies
\((t-1)^2\equiv0\pmod p\), also impossible. This proves (3). \(\square\)

**Corollary.** There is no upper-branch solution with \(j=1\),
\(k\) prime, and \(2\ell<k\). More generally, any prime factor of
\(k-1,k,k+1\) larger than \(2\ell\) excludes the entire candidate.

## 2. Replacing a scan of k with Pell equations

Fix \(\ell\), and put \(S=\{p:p\text{ is prime},\ p\le2\ell\}\).
By (3), write

\[
k^2-1=d y^2,
\]

where \(d>1\) is squarefree and all prime factors of \(d\) and \(y\)
belong to \(S\). Thus every remaining \(k\) is an x-coordinate of
one of the finitely many Pell equations

\[
\boxed{k^2-dy^2=1,\qquad d\mid\prod_{p\in S}p,\quad d>1.} \tag{5}
\]

There are exactly \(2^{|S|}-1\) possible values of \(d\). For each,
the positive solutions are powers of its fundamental positive solution.
The additional requirement that \(k\) itself is \(S\)-smooth can be
checked immediately on each generated solution.

The existing exact height theorem gives

\[
\binom{k}{\ell}=B<A<H_\ell
:=\frac{(\ell^2)!}{(\ell!)^{2\ell}}. \tag{6}
\]

Consequently the Pell process is stopped at an exactly computed bound
\(K_\ell\), the largest integer satisfying
\(\binom{K_\ell}{\ell}<H_\ell\). Fundamental solutions already
exceeding \(K_\ell\) are discarded by stopping their increasing
continued-fraction convergents once the x-coordinate exceeds this bound.
This does not require computing an enormous fundamental solution in full.

Finally, for each retained \(k\), use

\[
\ell+2\le t<\begin{cases}
2\ell,& k\ge2\ell,\\
10\ell,& k<2\ell,
\end{cases}
\quad t\le B,
\]

and the original equation (1). Modular contradictions are sufficient to
reject candidates; any modular survivor must be checked exactly.

The implementation `v4_upper_j1_pell.py` uses only integer arithmetic.
It generates Pell candidates rather than iterating through all integers
up to \(K_\ell\).

## 3. Status

The complete Pell calculation was run for every \(21\le\ell\le40\).
It produced 213,756 candidates, each rejected by an explicit Lucas-theorem
congruence witness. There were no survivors. Thus this entire range is
excluded for unbounded \(i,k\) under the earlier proved height bounds.
The generator did not scan integers up to the height limit: for example,
\(K_{40}=16,502,522,521,700,867\).

The independent verifier `v4_upper_j1_pell_verify.py` reconstructs all
candidates using the different Pell equation
\((2k-1)^2-4k(k-1)=1\), a separate squarefree-product order, and a
different Lucas implementation. It confirmed exact coverage and all
213,756 congruence contradictions. The certificate file is
`v4_upper_j1_pell_certificates.json` (SHA256
`128e778e9a5c6de11e697c8b4ed7e697d201b1345e90cf260cce0d2b5c534d51`);
the machine-readable verification report is
`v4_upper_j1_pell_verification.json`.

Theorem (3) is uniform in unbounded \(k,\ell\). The Pell reduction is
complete for each fixed \(\ell\), subject to the explicitly cited
previous height theorem. Neither statement supplies an absolute bound on
\(\ell\), so they do not solve the entire original equation.

No use of a primitive-divisor theorem is needed for the bounded algorithm
above. An optional stronger structural observation is possible using
primitive divisors of Lucas sequences, but it must not be silently treated
as an independently verified premise of this implementation.
