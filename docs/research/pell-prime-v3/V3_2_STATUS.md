# v3.2 verification correction

First-run PrimeFactorLean built successfully at its pinned Lean 4.24.0 and mathlib revision, but its well-founded arithmetic definitions prevented the proposed rfl/decide proof from reducing. This is a failed proof replay, not a primality failure. Followup uses native_decide for the Boolean certificate equality followed by the upstream proven soundness theorems; the native-computation trust assumption must be reported. The independent Hex run already passed strict decide +kernel on all eight targets, with only the standard three Lean axioms. The separate algebra/descent check and actual factor CLI have distinct CI steps so results can be inspected independently.

See v3.1 and the original run https://github.com/corcondor/mathos/actions/runs/45489068111. No global finiteness claim.
