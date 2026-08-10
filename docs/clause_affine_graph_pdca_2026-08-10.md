# Clause affine graph PDCA (2026-08-10)

## Correction to the previous audit

The earlier claim that 1,258 morphism gaps were one affine family was false.
The audit assigned contracts from broad surface markers, so unrelated generic
CAS failures were merged into one bucket.  The corrected audit no longer
treats `how many` or `number of` as evidence of a finite-domain contract and
separates comparison, rate, aggregate, state, and percentage obligations.

Current morphism-to-backend counts after the change are:

- typed semantic lowering still unknown: 508;
- typed rate contraction: 358;
- aggregate/coproduct observation: 332;
- symbolic elimination: 223;
- state/event flow: 164;
- comparison affine graph: 156;
- geometry: 149;
- percentage affine state: 128;
- finite domain: 127.

These remain triage labels, not proofs that every item in a bucket has one
solver contract.

## Implemented structure

Elliptical comparison clauses are compiled to rational affine edges
`A = q*B+c`.  Surface nouns and names are alpha-renamed graph vertices.  The
same executor handles additive comparison, multiplicative comparison, direct
projection, and coproduct total observation.

Safety gates require every numeric premise before the query to be consumed by
the graph.  Pronouns and unit words cannot become entity vertices.  Stories
with several named time states are rejected until time-indexed vertices are
available.

No benchmark id, expected answer, or numeric answer appears in the solver.
Tests include alpha-renaming and numeric perturbation.

## Benchmark result

Using the unchanged 3,574-case manifest (`996fd351...`):

| Metric | Prior | Current | Delta |
|---|---:|---:|---:|
| Exact | 840 | 850 | +10 |
| Exact rate | 23.5031% | 23.7829% | +0.2798 points |
| Answered | 1,199 | 1,209 | +10 |
| Answer precision | 70.0584% | 70.3060% | +0.2476 points |
| Wrong | 359 | 359 | 0 |
| Morphism-to-backend gap | 2,179 | 2,171 | -8 |

The first frozen run exposed four subject/object errors.  Those cases were then
used to repair the grammar, so the final `850` result is a regression result,
not a clean held-out claim.  A new independently frozen corpus is required for
an unbiased generalization estimate.

Artifacts:

- `artifacts/public_benchmark_frozen_regression_3574_after_subject_edges_v7_20260810.json`
- `artifacts/backend_gap_contract_audit_after_subject_edges_v8_20260810.json`
