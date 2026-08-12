# AlphaGeometry 2 reverse engineering and fixed benchmark

> Historical research reference only. The current MORTRA core has no AlphaGeometry,
> AlphaGeometry2, DDAR, adapter, executor, or environment-variable runtime dependency.

Date: 2026-08-10

## Scope

This iteration had two separate objectives.

1. Reproduce the reusable, non-LLM parts of AlphaGeometry 2's search contract.
2. Reduce MathOS's typed-semantic-IR to backend gap and measure the effect on the frozen 3,574-case benchmark.

The two results must not be conflated. The fixed benchmark gain mainly comes from executable symbolic semantics. The AG2 work improves the geometry construction backend, but the public benchmark contains too few directly formalized geometry cases for that backend alone to explain the gain.

## What was recovered from AlphaGeometry 2

The paper and official code establish the following reusable design.

- DDAR computes a deductive closure rather than matching solution templates.
- Angles, distances, and log-distances use separate algebraic normal forms.
- Similar-triangle and cyclic facts are indexed by structural hashes.
- SKEST runs multiple search distributions, including narrow/deep and wide/shallow trees.
- Failed nodes can publish facts about the original problem to a workspace shared by other trees.
- Auxiliary-point-specific facts are not shared as if they were original assumptions.

The public AG2 repository contains DDAR and formalized examples. It does not publish the full Gemini proposer used in the paper. Eleven of the 26 harder public examples already contain manually supplied auxiliary points. Therefore, passing the 26 public examples is a DDAR regression result, not a reproduction of the paper's 42/50 end-to-end result.

MathOS now maintains one DDAR-certified workspace across its finite search trees. Only proved predicates over original problem points are shared. The goal itself and facts containing generated auxiliary points are excluded. Every addition is recorded in `shared_facts_added` and the final `shared_workspace`.

## Executable semantic operators added

No benchmark problem ID, expected answer, or numeric instance was added to the solver. The new lowering rules are mathematical operators:

- composed function inversion with composition verification;
- piecewise function evaluation;
- finite function graph and inverse evaluation;
- observation of an invariant under underdetermined constraints;
- tuple equality to component constraints;
- absolute-value equations and ordered solution projection;
- inverse proportion as a multiplicative invariant;
- quadratic root ratio through Vieta relations;
- factorial recurrence normalization;
- common polynomial root projection through a resultant;
- zero-set extraction for positive-definite real quadratic factors;
- modulus projection over the complete complex root set;
- trigonometric root aggregation over an explicit interval;
- finite real solution-set cardinality;
- exact comparison of finite scalar sets and equivalent `pi` products.

The critical verifier change is that an empty or partial CAS branch is no longer accepted as a complete answer. A set-valued or aggregate query needs a certified finite solution set before projection.

## Frozen benchmark result

Protocol: same 3,574 cases, same manifest SHA-256, 8 second case timeout, 8 workers, no live retrieval, no external tools, and no surface morphisms.

Manifest: `996fd351f775eaee017ca35420049541f949be283c06923257a1ba81c4f4944a`

| Metric | Before | After | Delta |
|---|---:|---:|---:|
| Exact | 743 | 776 | +33 |
| Exact rate | 20.7890% | 21.7124% | +0.9234 points |
| Answered | 1,098 | 1,137 | +39 |
| Precision among answered | 67.6685% | 68.2498% | +0.5813 points |
| Wrong | 355 | 361 | +6 |
| Abstained | 2,476 | 2,437 | -39 |
| Held-out exact | 520 | 544 | +24 |
| Morphism-to-backend gap | 2,262 | 2,239 | -23 |
| Timeouts | 5 | 12 | +7 |

Case-level comparison found 33 newly correct cases and zero cases that changed from correct to incorrect. Gains were MATH +32 and SVAMP +1. Answer coverage rose faster than precision, so six newly exposed semantic errors remain. The largest remaining failure layer is still the morphism-to-backend gap at 2,239 cases.

Artifacts:

- before: `artifacts/public_benchmark_frozen_3574_before_ag2_reverse_engineering.json`
- after: `artifacts/public_benchmark_frozen_3574_after_ag2_reverse_engineering_final_v2.json`

## Verification

- MathOS Python regression: 148/148.
- Worker targeted auxiliary-search tests: 3/3.
- Worker TypeScript build: passed.
- Official public AG2 DDAR examples: 26/26.

## Remaining work

The next high-value work is not another collection of answer templates. It is to type the requested observation separately from the constraint relation. Current false answers still include cases where a solver returns `x=f(y)` while the question asks for a center, distance, directrix, domain exclusion, or three-dimensional point. Those observations need matrix/quadratic-form and affine-geometry morphisms before CAS execution.

## Primary sources

- AlphaGeometry 2 paper: https://www.jmlr.org/papers/volume26/25-1654/25-1654.pdf
- Official AlphaGeometry 2 code: https://github.com/google-deepmind/alphageometry2
- Official AlphaGeometry code: https://github.com/google-deepmind/alphageometry
