# Upper branch, j=1: repeated large prime factors of k

We keep the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

Here j=1 and we are in the upper outer branch. Set

\[
B=\binom{k}{\ell},\quad A=i=B+t,\quad
Y=\binom{k^2}{\ell^2},\quad L=\binom{B+t}{t}.
\]

The equation is L=(B+t)^2+Y. Earlier results exclude ell<=40 in
this branch. The general gap bound gives t>=ell+2. Whenever
k>=2ell, we also have A>=C(2ell,ell), so the proved central-height
bound gives

\[
\boxed{\ell+2\le t<2\ell.} \tag{1}
\]

## 1. A large repeated prime factor has one exact possibility

Let p>ell be a prime and let a=v_p(k)>=2. In particular
k>=p^2>2ell, so (1) applies. Since ell<p and ell^2<p^2,

\[
v_p(B)=a,\qquad v_p(Y)=2a.
\tag{2}
\]

For the second equality, use
Y=(k^2/ell^2) product_(h=1)^(ell^2-1) (k^2-h)/h. Each h has
v_p(h)<=1<2a, so every product factor is a p-adic unit. The first
equality follows from the same product for B with h<ell<p.

Since p^2 divides B and t<2ell<2p, every factor 1+B/h for
1<=h<=t is 1 modulo p, including h=p if it occurs. Therefore
L=1 (mod p). The equation then yields t^2=1 (mod p). Combining
this with ell+2<=t<2ell, p>ell, leaves only

\[
t=p-1\quad\hbox{or}\quad t=p+1.
\tag{3}
\]

The possibilities t=1 and t=2p-1 are outside (1).

If t=p-1, all h in 1,...,t are prime to p, so

\[
L=\prod_{h=1}^{t}(1+B/h)\equiv1\pmod{p^a}.
\]

But A=B+p-1 satisfies v_p(A^2-1)=1: A+1=B+p has valuation
one, whereas A-1=B+p-2 is a unit. Since v_p(Y)=2a,
v_p(A^2+Y-1)=1. This contradicts a>=2.

If t=p+1, separate the factor h=p:

\[
L=(1+B/p)U,\qquad U\equiv1\pmod{p^a}.
\]

It follows that v_p(L-1)=a-1. On the right, A=B+p+1 gives
v_p(A^2+Y-1)=1. Thus a=2. Reducing (L-1)/p modulo p now gives

\[
\frac B{p^2}\equiv2\pmod p.
\]

Write k=p^2 w with p not dividing w. The product formula for B
shows B/p^2 = w(-1)^(ell-1)/ell (mod p). We have therefore proved

\[
\boxed{
v_p(k)\ge2,\ p>\ell
\ \Longrightarrow\ 
v_p(k)=2,\quad t=p+1,\quad
\frac{k}{p^2}\equiv2(-1)^{\ell-1}\ell\pmod p.
} \tag{4}
\]

All divisions in these congruences have denominators prime to p.

## 2. Uniform exclusions and a restriction on general k

For every solution in this branch:

- No prime p>ell can divide k to exponent three or more.
- At most one prime p>ell can have p^2 dividing k, because (4)
  determines p=t-1.
- There is no solution with k=p^a, p>ell, a>=2.

For the last statement, (4) gives a=2 and w=1, so
2ell = +1 or -1 (mod p). Since 0<ell<p, this forces
2ell=p-1 or p+1. But t=p+1<2ell from (1), a contradiction.

There is also no solution with k=p prime and p>=2ell. Indeed
(1) gives 1<t<p-1. Now B has valuation one, and t<p, so Lucas'
theorem still gives L=1 (mod p), whereas Y=0 (mod p). Hence
t^2=1 (mod p), impossible for this t.

These conclusions leave untouched primes ell<p<2ell with k=p,
prime powers with base p<=ell, and the remaining composite values
of k. They do not settle the entire upper j=1 branch. This note is
an ordinary written proof, not a Lean formalization.

The proof was independently audited by the author of
`v5_large_prime_localization.md`; all valuation and endpoint checks
passed without correction.
