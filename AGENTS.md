# Math and Lean research instructions

Apply these preferences to mathematical research and Lean formalization in this repository.

1. Read `.agents/skills/deepseek-math-research/SKILL.md` and `docs/research/nested-binomial/DEEPSEEK_STATE.md` at the start of every task and before every DeepSeek call.
2. Delegate proof generation/repair to DeepSeek via `deepseek_goal_worker.py` / `deepseek_proof_loop.py`; prefer one theorem per worker over batch generation. Use `--extra-context` and `--library-reference` to pass notes and real mathlib definitions.
3. Verify every result with real Lean (exit 0, allowed axioms only, fixed type). Never accept a model's PASS claim. Never hand-edit a successful DeepSeek proof body.
4. Use a fresh run-dir per run; never overwrite successful sources. Add new jobs to `JOBS` with exact types.
5. Update DEEPSEEK_STATE.md after each run. Do not ask the user again for already-granted API/file authorization or for info retrievable from the known PR.
6. On failure, diagnose root cause and try a different strategy before reporting.
