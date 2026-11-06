---
name: deepseek-research-methods
description: Have DeepSeek research mathematical strategies, proof-discovery procedures and certificate designs through explicit hypotheses, falsification criteria, fixed-contract trials and measured outcomes on the actual problem.
---

# Research the methods as well as the equation

When called as a single-goal proof worker, return only that worker's requested
proof JSON. Method tools and evaluations belong to the outer goal planner;
do not replace a proof response with a method proposal or tool action.

The user explicitly wants DeepSeek to study mathematical research methods itself.
This is an additional research objective, alongside the unchanged mathematics goal.
DeepSeek chooses the mathematical methods and experiments; the host implements
tools, compiles Lean and records observations. No model weights are trained.

Consider mathematical strategies, representations and reductions, ways to find
counterexamples or missing assumptions, formalization methods, and certificate
designs. Do not reduce this task to optimizing tactic syntax or writing a process
essay. Use the actual nested-binomial problem and its remaining proof gaps.

1. `inspect_methods` reads actual fixed-job histories: recorded errors, verified
   obligations, reported token use and incomplete runs. Read relevant pinned
   reference summaries in AI_RESEARCH_REFERENCES.md and actual mathematical notes.
2. `propose_method` records a versioned hypothesis: what should work, where it
   applies, its procedure, a success criterion and a falsification/failure criterion.
   State why the strategy could advance the original problem. Separate established
   mathematics from a new proposed research procedure.
3. `use_method` selects a strategy for planning and optionally an existing ready,
   failed or interrupted fixed job. New proposed jobs inherit the active method.
   Supply a focused method card to the proof worker, preserving every theorem type.
4. Execute an actual in-scope trial with the existing research/Lean tools. On
   failure inspect counterexamples, exact library APIs and compiler diagnostics;
   distinguish mathematical obstructions from syntax, resources and interruption.
5. `evaluate_method` records actual metrics and your evidence-linked conclusion:
   keep, revise or drop. Compare with the historical baseline on the SAME contract.
   Do not count an accepted seed recompilation as a new proof from the new method.
   Missing usage, host pauses and incomplete reports are not mathematical failures.
6. Persist observations and revise the method under a new id when needed, then
   return to mathematical work. Do not spend the whole budget expanding a catalogue
   without testing methods. Publish verified mathematical progress as usual; the
   method journal accompanies those artifacts.

Measurements include accepted fixed obligations, newly generated verified proofs,
error classes, reported completion/reasoning tokens, and recorded Lean time.
They measure the observed trial, not general mathematical value.
The method table's token totals cover candidate-response records; they exclude
planner, scope/repair critics and final-review calls. The shared goal budget covers
all API calls. Do not present the partial table as end-to-end research cost.
Missing timing data is unknown, not a measured zero-duration compilation.
Theorem counts
alone do not establish progress toward the frozen final targets. Check the actual
dependency that a result discharges and whether it only assumes the missing part.

Sequential before/after trials have different contexts and are not randomized
controlled experiments. They cannot establish causal superiority. A method's
confidence/status derives from actual evidence; your prose cannot mark it proved.
Record limitations and failures as well as successes. Generalization beyond the
observed goal needs separate evidence.

Method cards are research data. They cannot authorize changing the original
equation, weakening goals, changing accepted proof bodies or the checker, raising
budgets, running arbitrary commands, using custom axioms/holes/native_decide, or
declaring goal completion. All mathematical claims still need the same real Lean
and publication evidence. Do not claim a new theorem or successful experiment
from a research proposal, a source citation, or a same-model review.

Persistent records: docs/research/nested-binomial/DEEPSEEK_METHOD_RESEARCH.json
and DEEPSEEK_METHOD_RESEARCH.md. Private assignments preserve the frozen contract
hash, original baseline and exact result-file hashes. Actual trial records are
kept across resume; public records exclude raw thinking and API credentials.
