# Proof-obligation / dependency-gate PDCA (2026-08-10)

## Controlled result

The control and treatment use the same source revision, 3,574-case manifest,
12 second case timeout, eight workers, and no live retrieval or external tools.

| Metric | control | dependency gate | delta |
|---|---:|---:|---:|
| exact | 850 | 851 | +1 |
| wrong | 358 | 267 | -91 |
| answered | 1,208 | 1,118 | -90 |
| exact rate | 23.7829% | 23.8109% | +0.0280 pt |
| precision | 70.3642% | 76.1181% | +5.7539 pt |

The gate is enabled by default. Set `MATHOS_REQUIRE_DEPENDENCY_COVERAGE=0`
only for the ablation control.

## Structural change

The quantity reasoner now constructs a premise-dependency graph from typed
object identity and local grammatical attachment. A candidate cannot execute
when a connected premise is silently omitted. Upper bounds, the multiplicative
identity, common-base cancellation, and typed projection can discharge an
otherwise omitted premise.

This is not an answer or problem-family lookup. No benchmark id, expected
answer, or case-specific number was added.

## Interpretation

A proof gate alone cannot synthesize new solutions. Its main effect is to make
abstention honest and reduce semantic false positives. Exact-match growth now
depends on lowering the remaining typed goals to real executable constraints.

The remaining main counts are 2,258 morphism-to-backend gaps and 1,985 generic
CAS partial cases. These are the next implementation target.

## Artifacts

- `artifacts/public_benchmark_3574_dependency_gate_control_20260810.json`
- `artifacts/public_benchmark_3574_dependency_gate_v3_20260810.json`
- `artifacts/proof_gate_ablation_3574_20260810.json`
