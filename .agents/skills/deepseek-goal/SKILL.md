---
name: deepseek-goal
description: Use when the user wants DeepSeek itself to own a persistent mathematics goal, select the next tasks, use research and mathlib tools, create and repair Lean proofs, and publish verified progress without Codex selecting each next theorem.
---

# DeepSeek goal agent

The decision maker is `deepseek-v4-1-flash-1017` via the existing Mistral API.
The Python runner executes bounded tools and returns their real results. Codex
implements and monitors the runner; it does not select the next mathematical
subgoal or author proof bodies.

Read the immutable goal in `goal.json`, the latest research state, and the tool
observations. You, DeepSeek, choose each next action and its mathematical purpose.
Do not wait for Codex to tell you which theorem to attempt next.
The machine snapshot includes `working_memory`: observed source excerpts and
search results from prior actions. Reuse them instead of repeatedly reading the
same theorem. They are source observations, not proof certificates. Use
`list_mathlib` to discover actual file paths before opening an uncertain path.

1. Inspect actual notes, existing verified Lean modules, certificate code/data,
   and pinned mathlib declarations before designing a new module.
2. Choose work that advances the frozen final targets. Explain the dependency
   on the final goal; increasing theorem counts is not a completion criterion.
3. Propose a small fixed Lean job. A separate call to the same DeepSeek model
   reviews mathematical scope and relevance. This is not independent external
   review. The runner freezes the exact type and definitions before proof work.
4. Run the proof worker. All proofs and repairs come from DeepSeek. Lean exit
   codes, printed axioms and source hashes determine acceptance, not model claims.
5. On failure inspect the actual error, retrieve real library declarations, and
   choose a repair or a different approach. Previously accepted proof bodies
   and frozen target statements must not be weakened or overwritten.
   `diagnose_job` gives classified failures and exact source excerpts.
   `update_job_context` passes retrieved sources to a retry without changing types.
   `review_failure` asks a separate DeepSeek repair critic for another strategy.
   Unused-variable lint does not invalidate a kernel-checked theorem.
6. Publish each verified module before starting another new module. Only verified
   source, fixed jobs, generated verification reports and goal progress are staged.
   The executor synchronizes the authorized branch before publishing and retries
   concurrent-writer push races at most three times, without force push or changes
   to protected proofs. `sync_research` can fetch newer versioned research notes.
   Unrecoverable publication conflicts/errors stop the round as `blocked` with
   actual Git diagnostics; do not waste actions on publish/checkpoint loops.
   `github_status` reads the authorized PR and head check-runs. The user explicitly
   authorized DeepSeek to operate GitHub as part of this research; select sync,
   publication and PR updates without asking for the same permission again.
   GitHub check status alone is not mathematical or Lean verification.
7. Checkpoint after meaningful progress, then continue choosing the next task.
   A checkpoint or one successful lemma does not stop the goal loop.

Use `set_plan` to preserve a milestone dependency graph when the task spans many
modules. Its evidence comes from actual verification reports; the graph is a
research plan, not permission to declare an intermediate milestone or the final
goal proved. The executor preserves accepted proof prefixes and can recompile
exact earlier DeepSeek outputs that were rejected only because of lint.

Completion requires BOTH final modules in `goal.json`, with EXACTLY the frozen
statements, accepted by real Lean without proof holes/custom axioms/native_decide,
and saved to the authorized GitHub branch. An assumed CF oracle/certificate
soundness, a weaker theorem, a model's PASS, or a partial module cannot complete
the goal. `request_completion` checks evidence; it does not accept self-reported
success. Never change the original squared-index binomial equation.

When this skill is supplied to a single-goal proof worker, follow that worker's
fixed JSON proof contract. The outer goal planner chooses actions; the worker
returns only the requested proof and never changes goal types.

Use the existing math-research skill for proof rules and known failed inferences.
The original approximation constant is 3/(2q²), not Legendre's 1/(2q²).

The user also requested research on mathematical methods themselves. Use
deepseek-research-methods to propose falsifiable mathematical strategies and
certificate designs, apply them to fixed jobs, and evaluate actual trials.
Check research_methods.pending_evaluations after a worker returns. Preserve the
baseline and distinguish seed recompilation, host interruption and missing data.
Method self-reports cannot establish proof, causality, or final-goal completion.

The loop has explicit action, wall-clock and reported-token limits and can be
paused. A limit/pause produces a resumable checkpoint, never `complete`.
API timeout is a waiting limit, not a guaranteed duration of model thinking.
The run depends on the cloud process remaining available; it is not a hosted
Mistral deployment or a permanent background service.

Commands (the host runs them for the user):

```bash
python3 docs/research/nested-binomial/v10_formal/deepseek_goal.py run
python3 docs/research/nested-binomial/v10_formal/deepseek_goal.py status
python3 docs/research/nested-binomial/v10_formal/deepseek_goal.py pause
```

`run` resumes the saved goal with a fresh explicitly bounded execution budget.
There is no claim that `/goal` is a native DeepSeek API command.


## User-submitted v30 research context (2026-11-07)

After synchronizing the authorized research branch, inspect
\`docs/research/nested-binomial/DEEPSEEK_V30_HANDOFF_ja.md\`,
\`docs/research/nested-binomial/V30_LOCAL_CRT_NOTE_ja.md\`, and
\`docs/research/nested-binomial/v30_local_crt_verify.py\`.
The user specifically requested work on the unresolved deep 5-adic collision
\`T ≡ 13,18 (mod 25)\` and certified Mordell–Weil rank/generators for
specialized elliptic curves. GitHub Issue #3 records the request.

**Scope boundary:** This is *research context*, NOT a change to the immutable
\`goal.json\` or the exact two final Lean targets. If a concrete lemma from this
work demonstrably helps the frozen targets, inspect it and pursue it with the
normal fixed-job + Lean-verification workflow. If it is logically unrelated,
report it as a separate pending goal instead of silently diverting this agent,
weakening final statements, or claiming v30 is solved.

A GitHub commit or Issue does not by itself invoke DeepSeek. Do not claim this
context was received by a running Codespaces process until its checked-out
workspace has synced and the actual execution log records an inspection/action.

The machine snapshot now includes `recent_version_notes` after branch synchronization. When the list changes (for example v31/v32), inspect the new source if it may genuinely advance the two frozen targets. Propose genuinely new bridge lemmas only after checking the supplied theorem and certificate. Do not regard version notes as verified by name, and do not let new notes silently change the immutable final-goal contract.
