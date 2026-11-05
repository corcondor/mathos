# Cyclotomic cofactor seven: auxiliary-ring obstructions and completion of the three residual small bases

## Scope and results

The original equation is the squared-index equation
\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
We continue the residual branch
\[
i=jp^3,\quad k=p,\quad\ell=1,\qquad
p\ge103\text{ prime},\quad j\ge101\text{ odd},\quad
p/2<j<10p/19,
\]
with
\[
\Phi_3(p)=p^2+p+1=7q^a,
\quad q\ne3,7\text{ prime},\quad a\ge1.
\tag{1}
\]
The preceding notes prove that q=1 modulo 3 and that
\[
q\mid42j^2+p-1,\qquad q^a<j^2<2q^a.
\tag{2}
\]
The v8 arithmetic theorem gives, for even a=2s, that s is odd,
q=7 modulo 12, and p=2 modulo 7. In particular 4 does not divide a.

The new results are:

1. **The exclusion of 3|a in this prime-p branch has an elementary
   proof in the four-element field R/(2).** The Thomas--Mignotte
   theorem is not needed for this restricted conclusion.
2. If the primary trace is defined by
   \[
   4q=B^2+27m^2,\quad m>0,\quad B\equiv2\pmod3,
   \tag{3}
   \]
   every solution of (1), with p any prime greater than 3, must have
   \[
   \boxed{B\text{ odd},\qquad m\text{ odd},\qquad5\nmid B.}
   \tag{4}
   \]
   Thus the prime shape q=b^2+27u^2, with u nonzero, is excluded for
   **every positive exponent**, as is the shape (3) with 5|B.
3. A new modulo-seven test constrains the primary trace and q:
   \[
   \boxed{
   \begin{array}{ll}
   p\equiv2\pmod7:&B^2\equiv(q+1)^2\pmod7,\\
   p\equiv4\pmod7:&
   B\equiv3+5q\text{ or }5+3q\pmod7.
   \end{array}}
   \tag{5}
   \]
   The second branch necessarily has odd a; exact orientation and
   exponent conditions are proved below.
4. **The three v9 residual bases q=19,31,67 are all excluded for
   every exponent in the original branch.** The first uses only the
   auxiliary moduli 5 and 11; the other two follow from (4).
5. Consequently all 21 possible prime bases through 211 are now
   excluded. The same uniform shape theorem excludes 223 and 229,
   giving **q>=241** for every surviving exponent. The previous
   first possible even base 367 has B=35 and is also excluded.
   Applying the same filters to379 and439 gives **q>=463** in
   the even-exponent branch.

These lower bounds are consequences of uniform obstructions and
complete existing exponent periods, not scans to a chosen exponent.
The whole cyclotomic branch and the original four-variable equation
remain unsolved.

## 1. Exact primary factorization and orientation

Write R=Z[omega], with omega^2+omega+1=0. Its norm is
N(x+y omega)=x^2-xy+y^2. The norm-Euclidean argument, unique
factorization, and exact primary normalization are proved in v7 and
v9. We record all the choices needed here.

Because p>3 is prime and q=1 modulo 3, equation (1) forces p=2
modulo 3. The factors p-omega and p-omega^2 are coprime: a common
prime divides their difference, whose norm is 3, but 3 does not
divide their norms. Thus precisely one of the conjugate primes
over q divides p-omega. Choose that prime and its unique associate
\[
\pi=x+y\omega\equiv1\pmod{3R},\qquad N(\pi)=q.
\tag{6}
\]
In particular x=1 modulo 3 and y=0 modulo 3. If
r=p modulo q, its orientation is characterized by
\[
x+yr\equiv0\pmod q.
\tag{7}
\]
The two orientations have the same trace B=2x-y, and y=+/-3m
with m>0. This gives (3). The representation with that trace and
positive m is unique, as shown in v9.

Since 7 divides Phi_3(p), p=2 or4 modulo 7. The exact factorizations
from v9 are
\[
\boxed{p-\omega=\gamma_h\pi^a,\qquad
\gamma_2=2-\omega,\quad\gamma_4=-1+2\omega,
\quad h=p\bmod7.}
\tag{8}
\]
For h=4, gamma_4=(3+omega)omega. There is no unspecified unit:
division by 2-omega gives residue 1 modulo 3R in the first case;
division by 3+omega gives residue omega in the second. Since pi=1
modulo 3R, the unit is exactly 1 or omega respectively.

We use both coordinates of (8). For a pair (c,d) representing
c+d omega, multiplication is
\[
(c,d)(x,y)=(cx-dy,\ cy+dx-dy).
\tag{9}
\]
Equality (8) requires its two coordinates to be exactly (p,-1).
The v9 trace test reduced the equality modulo the conjugate prime
above q. We now also reduce it modulo the independent rational
primes 2,5,7 and, in one case,11.

## 2. Reduction modulo 2: exponent and prime-shape obstructions

The polynomial z^2+z+1 is irreducible over F_2, so R/(2) is the
field F_4. Its nonzero elements are 1,omega,omega^2, all with cube1.
Since N(pi)=q is odd, pi is nonzero in this field.

For odd p,
\[
p-\omega=1+\omega=\omega^2\quad\text{in }R/(2),
\]
whereas gamma_2=omega and gamma_4=1. Thus (8) requires
\[
\boxed{
\pi^a=\omega\text{ if }h=2,\qquad
\pi^a=\omega^2\text{ if }h=4.
}
\tag{10}
\]

If 3|a, the left side is 1, a contradiction. Hence
\[
\boxed{3\nmid a.}
\tag{11}
\]
This proof uses the prime-p assumptions only to ensure p is odd and
p=2 modulo 3, which was needed for the exact units in (8).
It does not invoke a Thue-equation theorem.

If m is even, then y=+/-3m is even. The odd norm forces x odd,
so pi=1 modulo 2R. Equation (10) is then impossible for every a.
Therefore m is odd, and (3) shows B is odd as well.

In particular, if
\[
q=b^2+27u^2\quad(u\ne0)
\tag{12}
\]
is prime, choose the sign of b so that B=2b is 2 modulo 3.
This is possible because 3 does not divide b. Then (3) holds with
m=2|u|, so this entire prime shape is excluded. Examples include
31,43,109,127,157,223,229. This statement does not assert that
infinitely many primes have the shape (12).

For later finite tests, (10) also gives the complete small table:

| pi modulo 2R | h=2 requires | h=4 requires |
|---|---|---|
| 1 | impossible | impossible |
| omega | a=1 modulo 3 | a=2 modulo 3 |
| omega^2 | a=2 modulo 3 | a=1 modulo 3 |

### Scope of the removed external dependency

The v7 Thomas--Mignotte argument proves a stronger statement for
all integers x in x^2+x+1=7y^3. That statement and its dependency
remain unchanged. The elementary argument above proves the
specific exclusion needed here, namely 3|a with p a prime greater
than3 in (1). Hence all v8/v9 cyclotomic period tables can now use
(11) instead of the external theorem in this restricted branch.

## 3. Reduction modulo 5: every trace divisible by 5 is excluded

Assume 5|B. From B=2x-y we get y=2x modulo5. Because q is prime
and q=1 modulo3, q is not5; the norm is nonzero modulo5. Thus
\[
q=x^2-xy+y^2=3x^2\equiv2\text{ or }3\pmod5,
\qquad x\ne0\pmod5.
\tag{13}
\]
The characteristic identity pi^2-B pi+q=0 gives
\[
\pi^2=-q\quad\text{in }R/(5).
\tag{14}
\]
Using (9) and y=2x,
\[
\gamma_2\pi=(4x,0),\qquad
\gamma_4\pi=(0,x)\quad\text{in }R/(5).
\tag{15}
\]

If a=2s+1 is odd, (14)-(15) show that in the h=2 branch the
omega-coordinate of gamma_2 pi^a is0. It cannot equal -1.
In the h=4 branch its constant coordinate is0, forcing5|p.
This would make p=5, impossible because Phi_3(5)=31 is not
divisible by7. Thus every odd exponent is excluded.

If a=2s is even, the v8 arithmetic theorem forces h=2. The
omega-coordinate of gamma_2 pi^a is then -(-q)^s modulo5.
Equation (8) forces (-q)^s=1. By (13), -q is2 or3 modulo5,
both of multiplicative order4. Therefore4|s and8|a, contrary to
the v8 exclusion of4|a. This excludes all even exponents too.

We have proved
\[
\boxed{5\nmid B}
\tag{16}
\]
for every solution of (1) with p prime greater than3. This is a
uniform exclusion with no bounds on q or a.

The checker also records a related useful consequence when5|m,
so pi=x is a nonzero scalar modulo5. For h=2, its omega-coordinate
requires x^a=1. If q=x^2=4 modulo5, x has order4, contradicting
4 not dividing a. For h=4, the condition is2x^a=-1, so x^a=2;
this is impossible when q=x^2=1 modulo5. Consequently
\[
\boxed{5\mid m\Longrightarrow
\begin{cases}
q\equiv1\pmod5,&h=2,\\
q\equiv4\pmod5,&h=4.
\end{cases}}
\tag{17}
\]
Equation (17) is an additional necessary condition, not an
assertion that those remaining cases have solutions.

## 4. Reduction modulo 7: a trace test with exact orientation

There are two ring homomorphisms from R/(7) to F_7, obtained by
sending omega to2 and4. Put
\[
u_2=x+2y,\qquad u_4=x+4y\quad\text{modulo7}.
\]
Since q is not7, both are nonzero, and
\[
u_2u_4=q,\qquad u_2+u_4=B\pmod7.
\tag{18}
\]

For h=2, evaluate (8) at omega=4. Its two nonzero gamma and
target values are both5, so
\[
u_4^a=1.
\]
The order of u_4 divides6. Together with3 not dividing a, this
forces u_4=1 or-1; the latter requires even a. Thus
B=+(q+1) or-(q+1), proving the first part of (5).

For h=4, evaluate at omega=2. The target is2 and gamma_4 is3,
so
\[
u_2^a=3.
\]
The element3 has order6. Therefore a is coprime to6 and is odd.
If a=1 modulo6, u_2=3 and u_4=5q; if a=5 modulo6, u_2=5
and u_4=3q. Their sums give exactly the second part of (5).

These are direct finite-field consequences of the exact
factorization. No reciprocity theorem or new classification
theorem is used.

## 5. Completion of q=19,31,67

The complete v9 periods left only these three bases among all
q=1 modulo3 with13<=q<=211. We now finish them for all exponents.

### 5.1 The bases31 and67

For q=31, the primary representation is
\[
4q=(-4)^2+27\cdot2^2.
\]
It has even m, so Section2 excludes every exponent. The v9
surviving orientation is pi=1+6omega, and indeed both pi and
gamma_4 are1 modulo2R, whereas p-omega=omega^2.

For q=67,
\[
4q=5^2+27\cdot3^2.
\]
The trace is divisible by5, so Section3 excludes every exponent.
In its v9 surviving odd branch the contradiction is especially
short: pi=-2-9omega, gamma_2=2-omega, and
\[
\pi^2\equiv3,\qquad\gamma_2\pi=-13-25\omega\equiv2\pmod{5R}.
\]
Thus gamma_2 pi^a is a scalar modulo5R for every odd a, and
cannot have omega-coordinate -1.

### 5.2 The remaining base19

We give the necessary v9 reductions explicitly. The two roots of
r^2+r+1 modulo19 are7 and11. Condition (2) makes j^2 equal
to8 or7, respectively. The first is a quadratic nonresidue and
the second is a residue, so r=11 is necessary.

The primary trace is B=-7=12 modulo19, with order6 and powers
\[
1,12,11,18,7,8.
\]
The two v9 trace targets at r=11 are3 for h=2 and12 for h=4.
The first is absent from this list, while the second is B^1.
Consequently
\[
h=4,\qquad a\equiv1\pmod6.
\tag{19}
\]
The oriented primary prime is
\[
\pi=-5-3\omega,
\quad -5-3\cdot11\equiv0\pmod{19},
\quad\gamma_4=-1+2\omega.
\]

Modulo5R, pi=2omega. Since a=1 modulo3,
\[
\gamma_4\pi^a
=2^a(-1+2\omega)\omega
=2^a(-2-3\omega).
\]
Its omega-coordinate equals2^(a+1) modulo5. Equality to-1=4
forces a=1 modulo4, since2 has order4 modulo5.

But exact multiplication gives
\[
\gamma_4\pi=11-\omega,\qquad
\pi^4=-185+231\omega\equiv2\pmod{11R}.
\tag{20}
\]
For a=1+4t,
\[
p-\omega=\gamma_4\pi^a
\equiv-2^t\omega\pmod{11R}.
\]
Its constant coordinate forces11|p. The primality of p makes
p=11, contradicting p>=103 in the original branch. In fact (1)
then forces a=1; this is the genuine small arithmetic solution
Phi_3(11)=7*19, not a solution of the residual binomial branch.

This proves the all-exponent exclusion of q=19.

## 6. Consequences for the remaining bases

The 18 v9 exclusions plus Section5 exclude all21 possible bases
13<=q<=211. No new external theorem is required to reuse those
period tables: their restriction3 not dividing a now follows from
Section2. The quadratic, exact trace, and v8 even-exponent
conditions are unchanged.

The only further primes q=1 modulo3 below241 are223 and229.
They have the uniform excluded forms
\[
223=14^2+27,\qquad229=11^2+27\cdot2^2.
\]
Thus every remaining base satisfies q>=241.

In the even branch, v9 had excluded all17 possible prime bases
below367. For367, (3) has B=35 and m=3, so Section3 excludes it
for all exponents. Two direct consequences of the same new filters
also apply:
\[
4\cdot379=29^2+27\cdot5^2,\qquad
4\cdot439=(-28)^2+27\cdot6^2.
\]
For379, m is divisible by5 and q=4 modulo5. Equation (17) rules
out h=2, which every even exponent requires. For439, m is even,
so Section2 excludes all exponents.

The even branch requires q=7 modulo12. Between367 and463 the
only other integers in that residue class are
\[
391=17\cdot23,\quad403=13\cdot31,\quad415=5\cdot83,
\quad427=7\cdot61,\quad451=11\cdot41.
\]
All are composite. Therefore **q>=463** in the even branch.
This is a direct application of the already proved uniform filters,
with no new exponent search. We do not assert that241 or463
actually survives all other tests, much less that it gives a solution.

## 7. Verification and dependency boundary

The companion Python checker verifies the entire relevant rings
modulo2,5,7, the new finite-field implications, every concrete
primary representation, both conjugate orientations, the q19
trace and quadratic tables, and the exact multiplication in (20).
Its second implementation uses two-by-two matrices instead of
pair multiplication to verify powers and all finite records.
These finite identities support the uniform written arguments;
they are not extrapolations from an exponent cutoff.

The frozen v9 21-base and17-base period records are rechecked with
the new elementary3|a exclusion substituted for the previous
external dependency. Only the original scopes of those records
are used. No whole-equation classification is claimed.

The finite calculations in
[v10_formal/CyclotomicFilters.lean](v10_formal/CyclotomicFilters.lean)
were actually run with Lean4.35.0 and finished with exit code0.
They include the complete residue rings, the trace-zero filters,
the modulo-seven implications, and the complete120-period
certificate for the two q19 auxiliary moduli. Source and verbatim
output hashes are recorded in
[v10_formal/cyclotomic_kernel_check.json](v10_formal/cyclotomic_kernel_check.json).
The factorization, unit normalization, unbounded exponent
deductions, and original binomial reductions are not thereby
claimed to be Lean-formalized. No sorry, native_decide, or custom
axioms are used.

The new argument uses no new external classification theorem and
no cubic reciprocity. The v7 theorem for arbitrary integer x keeps
its Thomas--Mignotte dependency; this note only removes that
dependency from the prime-p cyclotomic branch considered here.

Three independent AI mathematical audits passed on2026-11-05.
The root reviewer checked the full written argument, including
the exact unit normalization and the scope of the v8 arithmetic
theorem for every prime p>3. The recovery reviewer independently
checked the full proof and Lean statement correspondence, then
reconstructed every finite record by polynomial convolution
reduced by omega^2+omega+1, direct norm-lattice enumeration,
unit cycles, and explicit square sets. All6 modulo-two records,
48 modulo-five records,72 modulo-seven records, the complete120
q19 residues and10 surviving records, and all39 previous period
tables agreed with the saved report. That independent execution
finished with exit code0.

The small-cofactor reviewer separately audited the mathematics,
checking code, and Lean correspondence, and reran the checking
program while capturing its output without modifying the report;
every saved field agreed. This reviewer supplied the immediate
379/439 consequence. The recovery reviewer then independently
checked those two prime representations, the modulo-five condition,
all seven intervening numbers in the modulo-twelve class, and the
five displayed composite factorizations. The strengthened bound463
therefore adds no new exponent search or external dependency.

After adding those final numerical examples, both the Python
checks and the Lean source were run again successfully. These
internal AI audits are not external peer review. The Lean boundary
remains the explicit finite arithmetic stated above.
