import Mathlib.Tactic
import CFTwistedCubeAlgebra

/-!
# v96: Final finite-output contradiction interface

The external exact integer checker has found five SMALL points on the
5214 CF curves after the twisted-cube constraints. This file formalizes
the elementary final exclusion once their exhaustiveness is provided.

CRITICAL: no theorem in this file claims that the 5214-curve Python
certificate is kernel checked. The missing hypothesis is precisely:
every potential solution belongs to CFV96RecoveredPoint.
That completeness premise must be proved by a future Lean reflection
certificate before the frozen CFSmallDefectGoal can close.
-/

namespace NestedBinomialV10

def CFV96RecoveredPoint (S T n r : ℕ) : Prop :=
  (S = 1 ∧ T = 225 ∧ n = 10 ∧ r = 30) ∨
  (S = 2 ∧ T = 450 ∧ n = 10 ∧ r = 30) ∨
  (S = 4 ∧ T = 900 ∧ n = 10 ∧ r = 30) ∨
  (S = 8 ∧ T = 1800 ∧ n = 10 ∧ r = 30) ∨
  (S = 10 ∧ T = 1681 ∧ n = 82 ∧ r = 246)

/-- Every exactly recovered small curve point fails n >= 104. -/
theorem cf_v96_five_points_excluded_by_height (S T n r : ℕ)
    (hn : 104 ≤ n) (h : CFV96RecoveredPoint S T n r) : False := by
  unfold CFV96RecoveredPoint at h
  rcases h with h | h | h | h | h <;> omega

/-- Independently, all five fail the strict first gap 3*n < r. -/
theorem cf_v96_five_points_excluded_by_gap (S T n r : ℕ)
    (hgap : 3 * n < r) (h : CFV96RecoveredPoint S T n r) : False := by
  unfold CFV96RecoveredPoint at h
  rcases h with h | h | h | h | h <;> omega

#print axioms cf_v96_five_points_excluded_by_height
#print axioms cf_v96_five_points_excluded_by_gap

end NestedBinomialV10
