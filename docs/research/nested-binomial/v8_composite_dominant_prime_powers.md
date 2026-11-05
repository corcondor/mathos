# Offset three: uniform classification of a dominant prime-power factor

## Scope and main results

The equation is still

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note treats \(\ell=1,j=i-3\), with

\[
n=i=wp^a+2,\qquad p\text{ prime},\quad p>6w,\quad a\ge1.
\tag{1}
\]

The integer \(w\ge1\) is unrestricted. In particular the results
are uniform in the cofactor, rather than a check of a chosen list of
cofactors. The inequality \(p>6w\) implies \(p\ge7\) and
\(p\nmid w\), so \(a=v_p(n-2)\).

**Theorem A: cofactors divisible by three.** If \(3\mid w\), a
solution necessarily satisfies

\[
\boxed{a=2,\qquad 6w<p<31\eta w,
\qquad n<961\eta^2w^3+2,}
\tag{2}
\]

where \(\eta=1\) for even \(w\), and \(\eta=2\) for odd \(w\).
Thus every fixed cofactor divisible by three has an explicit cubic
upper bound for the first index, and only exponent two survives.

**Theorem B: the other cofactors.** If \(3\nmid w\), put
\(r=\min(k,\binom n3-k)\) and \(e=v_p(r)\). A solution must
satisfy exactly one of the following two alternatives:

\[
\boxed{a=3e}
\qquad\text{or}\qquad
\boxed{a+1=3e,\quad6w<p<9w,\quad p+w\equiv0\pmod3.}
\tag{3}
\]

In particular, for every cofactor in (1),

\[
\boxed{a\not\equiv1\pmod3.}
\tag{4}
\]

Theorem A does not claim that all its finitely many possibilities
for a fixed \(w\) have been checked. The full cofactor-three family
has separately been excluded by the v7 cofactor-three result and the
v8 completion of the shifted base-three branch.

## 1. Inputs and notation

Put

\[
q=p^a,\quad A=\binom n3=qT,
\qquad T=\frac{w(wq+1)(wq+2)}6,
\]

\[
r=\min(k,A-k),\quad L=\binom Ar,\quad
X=\binom{n^2}{6n-9},\quad Y=k^2.
\]

Both \(k=r\) and \(k=A-r\) are included. The established offset-three
results give

\[
n\ge104,\qquad L=X+Y,\qquad 3n<r<10n/3,
\tag{5}
\]

\[
Q=\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3.
\tag{6}
\]

For \(n\ge1024\), the logarithmic gap implies

\[
r<3n+\frac{3n}{4\log n}<\frac{25n}{8}.
\tag{7}
\]

Finally, `v7_offset_dominant_prime.md` excludes all \(a=1\)
under (1). We may therefore assume \(a\ge2\) throughout the new
argument. The earlier common-divisor and gap proofs are in
`v6_common_divisor.md` and `v6_offset_composite.md`.

## 2. The common prime power and the outer digit block

The valuation calculation from the v7 dominant-prime note gives

\[
\boxed{v_p(A)=v_p(X)=a.}
\tag{8}
\]

For completeness, the squared-index binomial splits into base-\(p\)
blocks as

\[
n^2=q(qw^2+4w)+4,\quad 6n-9=6wq+3,
\quad n^2-(6n-9)=q(qw^2-2w)+1.
\]

Legendre's formula gives
\(v_p(X)=v_p\binom{qw^2+4w}{6w}=a\): the denominator
\((6w)!\) is prime to \(p\), and exactly the numerator's central
factor \(qw^2\) is divisible by \(p\).

Write

\[
s=\lfloor r/q\rfloor.
\]

Since \(q\ge p^2\ge49\), the broad gap in (5) implies

\[
3w\le s<r/q<\frac{10w}{3}+\frac{20}{3q}<p
\tag{9}
\]

when \(q\nmid r\). The upper bound \(r/q<p\) also holds when
\(q\mid r\); then the non-strict relation \(s=r/q\) replaces the
middle strict relation. In either case, \(3w\le s<p\).

If \(q\nmid r\), set \(e=v_p(r)<a\). The lower \(a\) digits
of \(A-1=qT-1\) are all \(p-1\), and the upper block of \(r-1\)
is \(s\). Consequently

\[
v_p\binom{A-1}{r-1}=v_p\binom{T-1}{s},
\]

\[
\boxed{v_p(L)=a-e+v_p\binom{T-1}{s},\qquad v_p(Y)=2e.}
\tag{10}
\]

These are exact digit-block identities. If instead \(r=qs\),
the corresponding identity is

\[
v_p(L)=v_p\binom Ts.
\tag{11}
\]

## 3. A uniform bound when 3 divides w

Assume \(3\mid w\). Then \(w\ge3,p\ge19,q\ge361\), so
\(n\ge1085\), and (7) applies. Also \(n\equiv2\pmod3\), giving

\[
Q=\frac{n(n-1)}\eta,
\qquad \eta=\begin{cases}1,&w\text{ even},\\2,&w\text{ odd}.
\end{cases}
\tag{12}
\]

The integer \(Q\) is prime to \(p\). For any \(b\ge0\) such
that \(p^b\mid r\), (6) gives \(Q\mid(r/p^b)^3\). Combining
this with (7) yields

\[
p^{3b-a}
<\eta\left(\frac{25}{8}\right)^3\frac{n^2}{q(n-1)}
=\eta w\left(\frac{25}{8}\right)^3
\frac{(t+2)^2}{t(t+1)},\qquad t=wq.
\tag{13}
\]

For every \(t\ge1083\),

\[
\left(\frac{25}{8}\right)^3\frac{(t+2)^2}{t(t+1)}<31.
\tag{14}
\]

After clearing denominators, (14) is
\(247t^2-46628t-62500>0\). This polynomial is positive at
1083, and its derivative \(494t-46628\) is positive thereafter.
Thus (13) gives the useful uniform inequality

\[
\boxed{p^{3b-a}<31\eta w\le62w.}
\tag{15}
\]

If \(q\mid r\), take \(b=a\). Then (15) gives \(q^2<62w\),
whereas

\[
q^2\ge p^2>36w^2\ge108w.
\]

This contradiction proves \(q\nmid r\), without any assumption
that the interval for \(r/q\) has width less than one.

## 4. The valuation balance proves Theorem A

Still assuming \(3\mid w\), set \(c=w/3\). The exact identity

\[
T-c=\frac{w^2}{2}q(1+cq)
\tag{16}
\]

shows \(v_p(T-c)=a\). By (9),
\(1\le c\le s<p\), so among the factors \(T-1,\ldots,T-s\)
only \(T-c\) is divisible by \(p\). Since \(s!\) is a unit,

\[
v_p\binom{T-1}{s}=a.
\]

Writing \(e=v_p(r)<a\), equations (8) and (10) become

\[
v_p(L)=2a-e,\qquad v_p(X)=a,\qquad v_p(Y)=2e.
\tag{17}
\]

If \(2e<a\), equality \(L=X+Y\) would require
\(2a-e=2e\), inconsistent with \(2e<a\). If \(2e>a\),
it would require \(e=a\), inconsistent with \(e<a\).
Therefore

\[
2e=a.
\tag{18}
\]

Taking \(b=e\) in (15) now gives

\[
p^{a/2}<31\eta w\le62w.
\]

If the even exponent \(a\) were at least four, the left side
would be at least \(p^2>36w^2\ge108w\). Consequently \(a=2\),
and \(p<31\eta w\). Substituting \(n=wp^2+2\) proves the
cubic height bound in (2).

## 5. Other cofactors: at most one extra p in the outer block

Assume now \(3\nmid w\). Since \(0<w<p\), there is a unique
\(h\) with

\[
1\le h<p,\qquad 3h=w+\tau p,\qquad \tau\in\{1,2\}.
\tag{19}
\]

The expansion

\[
T-h=-\frac{\tau p}{3}+\frac{w^2}{2}q+
\frac{w^3}{6}q^2
\tag{20}
\]

shows \(v_p(T-h)=1\), because \(a\ge2\). This is the only
residue class at which \(T\) minus an integer in \([0,p-1]\)
is divisible by \(p\).

First suppose \(q\mid r\). Then (11), (9), and (20) show
\(v_p(L)\le1\). But \(v_p(X)=a\ge2\), and both possible
values of \(k\) are divisible by \(q\), so \(v_p(Y)\ge2a\).
It follows that \(v_p(X+Y)=a\), a contradiction. Hence
\(q\nmid r\) in this case also.

For \(e=v_p(r)<a\), let

\[
\delta=v_p\binom{T-1}{s}
=\begin{cases}1,&h\le s,\\0,&h>s.\end{cases}
\tag{21}
\]

Thus

\[
v_p(L)=a+\delta-e,\quad v_p(X)=a,\quad v_p(Y)=2e.
\tag{22}
\]

If \(\delta=0\), the unequal-valuation case \(2e<a\) gives
\(a=3e\). The case \(2e>a\) would give \(e=0\), which is
inconsistent with its inequality; the equal case \(2e=a\)
would require \(a-e\ge a\), also impossible. Therefore
\(a=3e\).

If \(\delta=1\), the case \(2e<a\) gives \(a+1=3e\).
The case \(2e>a\) would force \(e=1\), contradicting
\(a\ge2\). If \(2e=a\), (22) and \(v_p(X+Y)\ge a\)
give \(a/2+1\ge a\), hence \(a=2,e=1\). This too satisfies
\(a+1=3e\).

It remains to restrict where \(\delta=1\) can occur. If
\(\tau=2\) in (19), then

\[
h=\frac{w+2p}{3}>\frac{13w}{3}
>\frac{10w}{3}+\frac{20}{3q}>s,
\]

using \(q\ge49\). Thus \(\delta=1\) requires \(\tau=1\),
which is \(p+w\equiv0\pmod3\). Moreover \(h\le s\) implies

\[
p<9w+20/q<9w+1.
\]

Since \(p\) is prime, it cannot equal \(9w\). Therefore
\(p<9w\), proving every assertion in (3).

When \(6w<p<8w\) and \(p+w\equiv0\pmod3\), one has
\(h<3w\le s\); in this subrange the second alternative is
mandatory. If \(p\ge9w\) or \(p+w\not\equiv0\pmod3\),
the first alternative is mandatory.

## 6. An additional quadratic congruence in Theorem A

The finite remainder in (2) has a further explicit obstruction.
Put \(B=\binom{6w}{2w}\). Since \(p>6w\), \(B\) is a
\(p\)-adic unit. Every solution in Theorem A must satisfy

\[
\boxed{\left(B\frac rp\right)^2\equiv2wB\pmod p.}
\tag{23}
\]

In particular \(2w\binom{6w}{2w}\) must be a nonzero quadratic
residue modulo \(p\).

Here is a proof of the normalized residue needed for (23). With
\(M=qw^2+4w\), \(K=6w\), and \(N=n^2,m=6n-9\), the exact
identity

\[
X=\frac{N(N-1)(N-2)(N-3)}{m(m-1)(m-2)(N-m)}
\binom{qM}{qK}
\]

has prefactor congruent to 4 modulo \(p\). Also

\[
\binom{pU}{pV}/\binom UV\equiv1\pmod p
\]

as a \(p\)-adic unit: in the binomial product, the factors with
indices divisible by \(p\) give \(\binom UV\), and each remaining
factor \((p(U-V)+t)/t\) is congruent to 1. Repeating this identity
\(a\) times reduces \(\binom{qM}{qK}\) to \(\binom MK\).
Removing its central factor \(qw^2\) gives

\[
\frac1q\binom MK
\equiv-\frac{w^2(2w-1)!(4w)!}{(6w)!}
=-\frac{w}{2B}\pmod p.
\]

Consequently

\[
X/p^a\equiv-2w/B\pmod p.
\tag{24}
\]

Theorem A gives \(a=2,e=1\), so \(v_p(L)=3\), and the
equation divided by \(p^2\) reduces to
\((r/p)^2\equiv2w/B\pmod p\). Both branches have the same
normalized square because \(p^2\mid A\). This proves (23).

## 7. Interpretation for general composite n

For \(n\equiv2\pmod3\), let \(p^a\) be the exact power of a
prime \(p\) in \(n-2\). If

\[
p^{a+1}>6(n-2),
\]

then \(p>6w\) for \(w=(n-2)/p^a\). In particular \(p\ge7\),
so \(3\mid w\), and Theorem A applies. Thus the exponent must
be exactly two, with

\[
6(n-2)<p^3<31\eta(n-2),
\]

where \(\eta=1\) for even \(n\) and \(\eta=2\) for odd \(n\).
This applies to every prime factor of \(n-2\), without fixing a
cofactor in advance. In particular,

\[
\boxed{p^{v_p(n-2)+1}<31\eta(n-2)\quad\text{for every }p\mid n-2}
\]

is necessary when \(n\equiv2\pmod3\). An exponent other than two
must satisfy the sharper inequality
\(p^{v_p(n-2)+1}\le6(n-2)\).

## 8. Verification and limits

`v8_composite_dominant_prime_powers_checks.py` checks the exact
constant in (14), the valuation blocks and normalized residue on
representative parameters, and the arithmetic in the conversion to
the general-index formulation. Its report is
`v8_composite_dominant_prime_powers_verification.json`.

These finite checks corroborate the identities. The unbounded
claims follow from the written proofs, not extrapolation from a
scan. No complete exclusion is claimed for every cofactor or for
the original equation, and no new Lean formalization is claimed.

An independent reviewer audited the entire proof, including both
ways of excluding q|r, the exceptional a=2 cancellation in Theorem B,
the normalized residue, and the general-index reformulation. The
review found no gap. A separate execution of the checker, with
report writes disabled, also passed all 29 identity examples.
