# Prime Power Symmetry Problem 74

## Problem

For prime numbers `a,b,c`, decide whether there exists a triple `(a,b,c)` such
that both

```text
a^a + b^b - c^c
a^a - b^b + c^c
```

are prime.

Japanese source:

```text
素数 a,b,c に対して、a^a+b^b-c^c, a^a-b^b+c^c がともに素数となる組 (a,b,c) は存在するか。
```

## MathOS Status

Current general pipeline classification:

```text
domain: number_theory
semantic lift families: none
answer: none
```

This is a missing backend family, not a solved theorem in the current system.

## Certified Reductions

Let

```text
P = a^a + b^b - c^c
Q = a^a - b^b + c^c
d = b^b - c^c
```

Then `P=a^a+d`, `Q=a^a-d`.

Necessary conditions:

1. None of `a,b,c` can be `2`; otherwise parity makes both targets even or one
   target non-positive.
2. Therefore any solution has `a,b,c` odd primes.
3. The primes are pairwise distinct. If `b=c`, then `P=Q=a^a`; if `a=b`, then
   `Q=c^c`; if `a=c`, then `P=b^b`.
4. `a` must be the largest prime. If `max(b,c)>a`, then
   `|b^b-c^c|>a^a-2`, so one of `P,Q` is not a positive prime.
5. Hence any solution must satisfy `b,c<a`.
6. Modulo `a`, `P≡d` and `Q≡-d`, so `PQ≡-d^2 (mod a)`. An earlier version
   incorrectly inferred `a≡1 (mod 4)` here. Primality of `P,Q` does not imply
   that `PQ` is a quadratic residue modulo `a`, so no such restriction follows.
7. Modulo `3`, except for the small value `3` case, `b` and `c` must have the
   same residue modulo `3`; otherwise one of `P,Q` is divisible by `3`.

## Correction to the First Reduction

The first diagnostic incorrectly claimed `a≡1 (mod 4)`.  From
`PQ≡-(b^b-c^c)^2 (mod a)` one cannot infer that `PQ` is a quadratic residue
modulo `a`.  All snapshots that used that gate are withdrawn.  The corrected
backend enumerates every odd prime `a`.

## Independent Computation Snapshot

Backend added:

```text
math_os_prototype/prime_power_symmetry.py
```

Run:

```text
python -B math_os_prototype\prime_power_symmetry.py --limit 500 --sieve-bound 5000
```

Result:

```text
status: no_example_in_bounded_search
search_limit: 500
candidate_a_values: 94
canonical_pairs_checked: 134044
ordered_triples_covered: 268088
rejected_by_modulo_3: 70103
rejected_by_modular_factor: 61741
candidate_triples_after_sieve: 2200
examples: []
audit_sha256: e3332c41fa6345c5c09667aa775b1bc501244073fb225bd2ce35a66cae0ef025
backend: gmpy2.is_prime 2.3.1
```

The `b<c` enumeration is a complete set of representatives under the symmetry
that swaps `b` and `c`; `ordered_triples_covered` restores both orderings.

## Collaborator Report

On 2026-07-21, the problem author reported that an independent collaborator
found no example with `a<=2000`.  The collaborator's program, exact search
domain, and run log have not yet been imported, so this is recorded as an
external result rather than a MathOS-verified bound.  The critical audit
question is whether all odd primes `a` were searched, without the invalid
`a≡1 (mod 4)` gate described above.

## C1-C5 Congruence Sieve Snapshot (2026-07-22)

The corrected structural gates are fixed as:

```text
C1: none of a,b,c equals 2
C2: a,b,c are odd primes
C3: a,b,c are pairwise distinct
C4: a is the largest variable
C5: b<a and c<a
```

The computation then quotients by the `S2` action swapping `b,c` and removes a
candidate only when one target has a certified prime divisor in the sieve.

Run:

```text
python -B math_os_prototype\prime_power_symmetry.py \
  --limit 2000 --sieve-bound 20000 --sieve-only
```

Result:

```text
candidate_a_values: 302
canonical S2 representatives: 4,545,100
ordered triples covered: 9,090,200
rejected modulo 3: 2,304,726
rejected by another prime p<=20,000: 2,181,648
survivors after p<=100: 265,381
survivors after p<=500: 147,115
survivors after p<=1,000: 120,220
survivors after p<=5,000: 79,352
survivors after p<=20,000: 58,726
exact primality checks: 0
audit_sha256: 273349639eb3424739386d176c47211e3bc92335c50204da7d3a5fbaa5ec686f
```

Thus the congruence stage alone rejects about `98.71%` of the C1-C5 canonical
search space.  The remaining `58,726` triples are not solutions; they are only
triples for which neither target has a prime divisor at most `20,000`.

## MathOS IR Connection

`PrimePowerSymmetricPrimalityIR` is now lifted by coefficient-vector structure:

```text
(target_1 + target_2)/2 = SelfPower(a)
(target_1 - target_2)/2 = SelfPower(b) - SelfPower(c)
```

Term order, whitespace, and LaTeX braces are parameters.  The resulting
LiftCertificate uses family
`elementary_number_theory.prime_power_symmetric_primality` and connects to a
bounded-evidence backend.  The backend explicitly leaves the unbounded
existence question unresolved.

## Interpretation

This is not yet a complete solution.  The corrected MathOS computation proves
only a bounded software-assisted statement through `a=500`; the collaborator
report extends the observed bound to `a=2000` pending reproduction.  A final
proof of non-existence or a constructive example is still missing.

Next backend target:

```text
PrimePowerSymmetricPrimalityIR
  -> parity gate
  -> largest-variable gate
  -> residue analysis modulo a (no unproved Legendre-symbol gate)
  -> modulo-3 gate
  -> modular sieve
  -> probable-prime / proof-prime checker
```
