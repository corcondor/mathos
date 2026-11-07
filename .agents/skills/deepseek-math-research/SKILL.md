---
name: deepseek-math-research
description: Delegate math research, proof generation, Lean code generation/repair, and failure diagnosis to DeepSeek (deepseek-v4-1-flash-1017 via Mistral API) using per-call reloaded file state; host verifies with real Lean and never hand-edits successful proofs.
---

# DeepSeek Math Research Skill

Purpose: route proof work to DeepSeek as much as possible, persist what it learns in files (no weight updates), and reload that state on every API call.

## State and references
- Current research state: [DEEPSEEK_STATE.md](../../../docs/research/nested-binomial/DEEPSEEK_STATE.md) (repo `/workspace/mathos`).
- Skill file lives at `.agents/skills/deepseek-math-research/SKILL.md`; `AGENTS.md` references it.
- The API helper reloads this skill, DEEPSEEK_STATE.md and AI_RESEARCH_REFERENCES.md on every call; update research state after each completed run.

## API
- Model: `deepseek-v4-1-flash-1017`
- Endpoint: `https://api.mistral.ai/v1/chat/completions`
- Auth: `MISTRAL_API_KEY` via existing environment binding/proxy. Never print, store, or re-request the key.
- The user has explicitly authorized sending v10/v11 research files and additional files to this API. Do not ask again.

## Private research location
- https://github.com/corcondor/mathos/pull/1; initial inspected base snapshot `bd4d2ad338e62102d60d9fffd8c073a5d48bf250`. Fetch its current head before further changes; verified later uploads are recorded in DEEPSEEK_STATE.md.
- Public `nested-binomial-equation` main has up to v8. The private mathos PR now includes v16: read PROGRESS_v16_ja.md, v16_square_defect_pell.md, v16_lower_gap.md, v16_quadratic_neighbors.md, v16_repeated_neighbor_primes.md and v16_manifest.json. The full compressed certificate is stored on GitHub and can be inspected with bounded read_research. v15 remains a prior input. It adds written deductions and exact Pell computations, not new Lean proofs. v14 gives the two-factor support result and exact 57-case auxiliary classification. v13 supplies the earlier uniform cube-support exclusion and general finite-support reduction. It relies on prior reductions, PARI complete Thue solving and (for the general candidate count) Bennett; it is not Lean-verified. v12 remains the H>=21 numerical bound; see its report, independent verifier and manifest. The complete certificate ZIP is not stored on GitHub and has not been obtained in this environment; report receipt, source/hash checks and full recomputation separately.
- First inspect existing checkouts and GitHub auth; do not make the user re-summarize info available from the known PR. Cloud tasks are isolated; do not create worktrees unless explicitly asked.

## Division of labor
- Host: information retrieval, API delegation, compilation, real verification, saving artifacts.
- DeepSeek: proof generation and repair (the user wants all proof work delegated). Host must not hand-edit a successful proof body.
- Latest correction: DeepSeek must also choose the next mathematical task and drive the persistent goal. Use [deepseek-goal](../deepseek-goal/SKILL.md) and its executor; Codex should not keep issuing individual mathematical assignments.

## Implemented tooling (in docs/research/nested-binomial/v10_formal/)
- `deepseek_goal_worker.py` — one theorem at a time; prefer over batch generation.
- `deepseek_proof_loop.py` — loop driver; add new jobs to `JOBS` with exact types, only proofs go into immutable types. Use a fresh run-dir each time; never overwrite existing successful sources.
- `check_additional_formalization.py`
- Worker supports fixed JSON contracts via `--job-config` and bundled method summaries when downloads are absent. Worker flags: `--seed-proofs` (reuse `accepted_proofs.json`, always recompile), `--extra-context`, `--library-reference` (notes + actual mathlib definitions).

## Lean environment
- Workdir: `/workspace/.cloud-setup/lean/mathlib`
- `ELAN_HOME=/workspace/.cloud-setup/lean/elan`, prepend `/workspace/.cloud-setup/lean/elan/bin` to PATH.
- Lean 4.35.0; mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679`.

## Success criteria (strict)
- No proof holes, no custom axioms, no `native_decide`.
- Success = real Lean exit 0 + axiom dependencies only `propext`, `Classical.choice`, `Quot.sound` + fixed type.
- A model saying PASS is not success. A separate evaluation call to the same DeepSeek is not an independent model or external review.

## Known failure modes to warn DeepSeek about
- Do not replace the original approximation constant 3/2 with Legendre 1/2.
- Do not derive +1 from det=-1 in the same column.
- `pQ-qP = b*(PmQ-PQm)`; do not confuse with the previous column.
- Do not derive `rad(n-2)|S` from `S|n-2`.

## Prior references (procedural only, no code copying)
- OpenAI lean-gym (Lean 3.39.1, do not port directly), OpenAI evals, Anthropic evaluator_optimizer; pinned commit links in RESEARCH_WORKFLOW.md.
- Eleven additional verified repositories, including DeepSeek-Prover-V2, AlphaGeometry/2, formal-conjectures, Evariste, Kimina, LeanDojo/v2, LeanCopilot, REPL and Aesop, were shared with DeepSeek. See AI_RESEARCH_REFERENCES.md and its pinned catalog. Do not claim those systems or model weights are installed.

## Manual checkpoint before the autonomous goal
- 7 new modules / 35 theorems authored and repaired solely by DeepSeek pass Lean: LocalSquareRecovery(4), CriticalPrimeCRT(3), CFApproximationCore(5), GeometricReduction(9), GeometricDescent(6), CFCoefficientRanges(6), CFCandidateCoverage(2).
- RecoveredDivisor and NormalizedCancellation had host edits — keep distinct.
- Dependency + 9 additional modules (10 total) passed latest re-run.
- During the autonomous run, use `deepseek_generation_checks.json`, `goal_verified_modules.json`, and `DEEPSEEK_GOAL_PROGRESS.md` for current machine-verified progress; the counts above are the prior manual checkpoint.
- Python exact revalidation: 5214 curves, 4,877,566 CF coefficients, 25,394,330 reduced fractions, 0 residual; saved in `cf_current_revalidation.json`. Python success ≠ Lean formalization complete.

## Open work (do not claim done)
- 30-cofactor final theorem still assumes the CF part.
- Coefficient-range lemmas and the explicit candidate-set cardinal bound ≤65 are verified in CFCoefficientRanges. CFCandidateCoverage supplies a generic candidate-coverage theorem and finite-prefix interval selection. Pending: instantiate both with actual convergent/certificate data, cylindrical interval certification, Lean check of all curve candidates, final theorem hookup.
- Full four-variable problem unsolved.
- GeometricReduction verifies the rational open-chart maps x=-c*r/y, z=c/y, inverses y=c/z, r=-x/z, plus Delta=-432*c^4, ellipticity, j=0 and the c=6*S/T specialization. It does not prove ranks, descent, all rational points, or solve the original equation.
- The user confirmed: study the CURRENT nested-binomial equation geometrically. Do not ask that question again. Investigate its cubic-curve families and verify all coordinate changes in Lean before using them.

## Working style
- User dislikes frequent questions/confirmations. Proceed autonomously within existing authorization; on one failure, diagnose and switch strategy.
- Do not claim snapshot publication, GitHub push, task restore, or persistent model memory unless actually executed.
- Kernel acceptance is Lean exit 0 with the fixed type and allowed axioms, with no holes/native_decide. Lint warnings are recorded separately; do not spend proof attempts on unused-variable warnings or change fixed hypotheses to silence them.
- The Lean harness classifies errors and retries unchanged source on a pure heartbeat/recursion limit, with bounded resources and the same wall-clock deadline. Use the actual source excerpts and persistent failure memory before trying the same failing proof again.

## Tested commands
Run existing verification from the prepared mathlib checkout:
```bash
export PATH=/workspace/.cloud-setup/lean/elan/bin:$PATH ELAN_HOME=/workspace/.cloud-setup/lean/elan
cd /workspace/.cloud-setup/lean/mathlib
lake env python3 /workspace/mathos/docs/research/nested-binomial/v10_formal/check_additional_formalization.py
```
Inspect the worker's current arguments before configuring a new, uniquely named job:
```bash
cd /workspace/.cloud-setup/lean/mathlib
lake env python3 /workspace/mathos/docs/research/nested-binomial/v10_formal/deepseek_goal_worker.py --help
```
For a new job use `--run-dir` with a fresh directory and `--methods-dir` pointing to the downloaded public reference files. Existing verified modules deliberately refuse to be overwritten. If the documented runtime paths are absent, inspect the current checkout and available tools before rebuilding the pinned runtime.

## Native reasoning
- `deepseek_settings.json`: max, max_tokens 131072, request_timeout_seconds 1800, max_attempts 20, lean_timeout_seconds 180. The API accepted max on a real research request (25,004 reasoning tokens, 63.8s, complete final proposal). High and provider-default omission were also tested. xhigh remains unverified. Request acceptance does not by itself quantify a quality gain.
- Token budget includes reasoning. A research request used all 32768 reasoning tokens without final text; continuation with 65536 produced a real proposal. Missing final text/finish_reason=length is not a successful proof response.
- Preserve provider thinking chunks only server-side for replay. Display final text and usage metadata, never raw reasoning, in the UI.
- Prioritize sufficient established mathematical methods. Necessity of frontier mathematics has not been demonstrated for the remaining equation.

## Earlier official Mistral Studio setup
- The user clarified that "chat UI" means Mistral's official UI, not a new custom frontend. Do not resume custom UI construction.
- Official private Prompt and Skill named mathos-nested-binomial-research were created through /v2/prompts and /v2/skills, with 26 authorized research sources and readback verification. IDs and links are in DEEPSEEK_STATE.md.
- The stored prompt was retrieved and successfully tested with deepseek-v4-1-flash-1017 / high. This does not select the model in the browser UI.
- The browser is at Mistral's login page; no access to the user's signed-in browser session was established. Do not claim UI configuration or a Managed Agent deployment is complete.
- The v1 Agent creation endpoint is disabled for this organization (403, use Managed Agents), not evidence that the API key is invalid or an admin role is missing.

## Active workflow after the user's latest decision
- The user decided to continue in the current Codex chat. Delegate mathematics and proof generation to DeepSeek; the host compiles, checks and saves to the existing GitHub PR.
- Do not continue frontend construction or official UI/login setup unless asked again. The saved private Studio Prompt and Skill remain available, but are not required for this workflow.

## Increased research budget (2026-11-06 JST)
- The user explicitly requested more thinking. Active profile is max, 131072 total output tokens including reasoning, HTTP timeout 1800s, 20 repair attempts, Lean timeout 180s.
- The actual next CF coverage/finite-prefix interval proposal succeeded with max: 25004 reasoning tokens, 63.8s. See max_reasoning_research_check.json. Do not claim a fixed thinking duration or that all budget is consumed.
- Use the added budget on the remaining CF/data connections, not disconnected auxiliary identities. Keep verified theorem types fixed and return actual Lean errors for repair.

## Research on mathematical methods
- The user explicitly requested research on the methods themselves. Apply ../deepseek-research-methods/SKILL.md: DeepSeek proposes falsifiable mathematical strategies, formalization procedures and certificate designs, tries them on fixed contracts, and evaluates measured results. These cards do not authorize changes to the checker, goals or budgets.
