# Affine and rate graph backend PDCA (2026-08-10)

## Objective

Close the largest public-benchmark backend gap without adding problem ids,
expected answers, or per-question solution templates.  The implementation adds
two reusable executable structures.

1. An affine state action `x -> a*x+b`, composed from proportional and absolute
   events and inverted by rational Gaussian elimination.
2. A typed rate graph, where units are sorts and `per` is a morphism.  Products,
   quotients, labelled coproducts, and inverse-rate observations are accepted
   only when dimensions and labels match.

Mixed named comparisons such as `A = 1.6B`, `C = A-7`, and observations of a
vertex, sum, or difference are lowered to the same affine equation backend.

## Anti-memorization checks

- The solvers receive only problem text, never benchmark id or expected answer.
- Numeric perturbation tests keep the same certificate while changing the
  computed value.
- Independent object labels must contract before addition.
- Endpoint observations cannot be reused as unrestricted arithmetic leaves.
- Unsupported temporal, comparison, capacity, and piecewise relations abstain
  instead of being forced through the rate graph.

The first rate-graph draft exposed 16 wrong answers in GSM8K.  The cause was not
missing data: dimension equality alone could not preserve object labels or the
role of an endpoint.  Labelled contraction and an observation gate reduced the
new operator to 9/9 correct GSM8K answers.

## Fixed 3,574-case result

Protocol and manifest are unchanged: manifest `996fd351...`, eight workers,
12-second case timeout, no live retrieval, no external tools, and surface
morphisms disabled.

| Metric | Before | After | Delta |
|---|---:|---:|---:|
| Exact | 816 | 840 | +24 |
| Exact rate | 22.8316% | 23.5031% | +0.6715 points |
| Answered | 1,171 | 1,199 | +28 |
| Answer precision | 69.6840% | 70.0584% | +0.3744 points |
| Wrong | 355 | 359 | +4 |
| Held-out exact | 572 | 584 | +12 |
| Morphism-to-backend gap | 2,209 | 2,179 | -30 |
| Correct-to-wrong regressions | 0 | 0 | 0 |

Case-level comparison found 24 newly correct cases and no prior correct case
that became incorrect.  The four additional wrong answers are newly answered
cases, so precision improved but the verifier still needs stronger semantic
gates.

## Remaining contract gaps (superseded audit)

The post-change unresolved audit contains 2,734 cases.  The largest
`morphism_to_backend_gap` groups are:

1. affine system / elimination / observation: 1,258;
2. finite-domain filtering and observation: 476;
3. new typed-semantic lowering required: 221;
4. geometric constraints / invariants / measure: 121;
5. symbolic relation / elimination: 84;
6. matrix-vector observation: 15;
7. calculus observation: 4.

This first contract audit was too coarse.  In particular, generic observation
phrases such as `how many` and `total` caused heterogeneous unresolved problems
to be counted as affine.  The corrected audit and follow-up clause compiler are
recorded in `docs/clause_affine_graph_pdca_2026-08-10.md`.  The figure 1,258
must not be used as an estimate of executable affine work.

## Verification

- Focused affine/rate tests: 48/48.
- Full suite: 48 modules passed in the parallel 180-second run; two heavy
  modules hit that local timeout, then both passed separately (4/4 and 5/5).
- Total discovered tests: 441, with no assertion failures.
- Benchmark artifact:
  `artifacts/public_benchmark_frozen_3574_after_periodic_affine_v3_20260810.json`.
- Gap audit artifact:
  `artifacts/backend_gap_contract_audit_after_periodic_affine_v3_20260810.json`.
