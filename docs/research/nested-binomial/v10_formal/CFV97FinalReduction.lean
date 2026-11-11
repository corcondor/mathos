import Mathlib.Tactic
import CFV97CompleteParameters
import CFRationalCubeExclusionB

/-!
# v97: Final algebraic connection to v95 and the finite input domain

The full v95 twisted-cube identity and residue condition follow from
the ORIGINAL curve, without any Python certificate assumption.
Also kernel-proves the exact 5214 parameter-count arithmetic and
excludes the unique rational-cuberoot pair S=9,T=2000.
The other 5213 finite CF certificates are NOT yet kernel-verified.
-/

namespace NestedBinomialV10

/-- The normalized cubic identity follows from D=h*e and h | 6. -/
theorem cf_v97_cubic_identity_from_defect
    (S T p q h e s z : ℕ)
    (hh : 0 < h) (hh6 : h ∣ 6)
    (hD : T * q ^ 3 - 6 * S * p ^ 3 = h * e)
    (hq : q = h * s * z ^ 2)
    (hpos : 6 * S * p ^ 3 < T * q ^ 3) :
    ((6 / h) * S) * p ^ 3 + e = T * h ^ 2 * s ^ 3 * z ^ 6 := by
  have h6 : h * (6 / h) = 6 := Nat.mul_div_cancel' hh6
  have hcoeff : h * ((6 / h) * S) = 6 * S := by
    calc
      h * ((6 / h) * S) = (h * (6 / h)) * S := by ring
      _ = 6 * S := by rw [h6]
  have hsum : h * e + 6 * S * p ^ 3 = T * q ^ 3 := by
    calc
      h * e + 6 * S * p ^ 3 =
          (T * q ^ 3 - 6 * S * p ^ 3) + 6 * S * p ^ 3 := by rw [hD]
      _ = T * q ^ 3 := Nat.sub_add_cancel (Nat.le_of_lt hpos)
  have hcubic : h * e + h * ((6 / h) * S) * p ^ 3 =
      T * (h * s * z ^ 2) ^ 3 := by
    calc
      h * e + h * ((6 / h) * S) * p ^ 3 =
          h * e + 6 * S * p ^ 3 := by rw [hcoeff]
      _ = T * q ^ 3 := hsum
      _ = T * (h * s * z ^ 2) ^ 3 := by rw [hq]
  exact cf_twisted_cube_cancellation T p h e s z ((6 / h) * S) hh hcubic

/-- Every original admissible curve point has the complete v95 normal
form: coefficient divisor, squarefree coefficient, sixth-power cubic
identity, and mod-S residue condition, with no existential assumptions. -/
theorem cf_v97_full_twisted_cube_reduction
    (S T n r g p q : ℕ)
    (hn : 2 ≤ n) (hg : 0 < g) (hT : 0 < T)
    (hSdiv : S ∣ n - 2)
    (hr : r = g * p) (hq : n - 1 = g * q)
    (hcop : p.Coprime q)
    (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) :
    ∃ h e A s z : ℕ,
      0 < h ∧ h ∣ 6 ∧ e ∣ T ∧ Squarefree s ∧
      0 < A ∧ 0 < s ∧ T = e * (s * A ^ 2) ∧
      q = h * s * z ^ 2 ∧ g = A * s * z ∧
      n - 1 = h * A * s ^ 2 * z ^ 3 ∧
      ((6 / h) * S) * p ^ 3 + e = T * h ^ 2 * s ^ 3 * z ^ 6 ∧
      (h * A * s ^ 2 * z ^ 3) % S = 1 % S := by
  obtain ⟨h, e, A, s, z, hh, hh6, heT, hsq, hA, hs, hTfact,
      hD, _, hqtw, hgtw, hntw⟩ :=
    cf_v97_curve_twisted_cube_parameters S T n r g p q
      hn hg hT hSdiv hr hq hcop hcurve
  have hlt : 6 * S * p ^ 3 < T * q ^ 3 :=
    curve_recovery_lt S T n r g p q hn hg hT hr hq hcurve
  have hcubic :=
    cf_v97_cubic_identity_from_defect S T p q h e s z
      hh hh6 hD hqtw hlt
  have hmod : (h * A * s ^ 2 * z ^ 3) % S = 1 % S :=
    cf_twisted_cube_mod_constraint S n h A s z hn hSdiv hntw
  exact ⟨h, e, A, s, z, hh, hh6, heT, hsq, hA, hs, hTfact,
    hqtw, hgtw, hntw, hcubic, hmod⟩

/-- The strict integer range in the frozen small-defect theorem has
exactly 67*S-1 entries for each S>=1. -/
theorem cf_v97_curve_index_coverage
    (S T : ℕ) (hS : 1 ≤ S)
    (hlo : 162 * S < T) (hhi : T < 229 * S) :
    ∃ t : ℕ, 1 ≤ t ∧ t ≤ 67 * S - 1 ∧ T = 162 * S + t := by
  refine ⟨T - 162 * S, ?_, ?_, ?_⟩ <;> omega

/-- 66+133+...+803 = 5214. This just counts the curve pairs;
it does not certify that each irrational curve has no solution. -/
theorem cf_v97_curve_count :
    (∑ S in Finset.Icc (1 : ℕ) 12, (67 * S - 1)) = 5214 := by
  decide

/-- The one rational cube-root curve in the existing 5214-pair domain
is excluded directly by an earlier Lean-proved general theorem. -/
theorem cf_v97_rational_exception_excluded
    (n r : ℕ) (hn : 104 ≤ n)
    (hcurve : 6 * 9 * r ^ 3 = 2000 * n * (n - 1) * (n - 2)) :
    False := by
  exact rational_cube_root_excluded 9 2000 n r 10 3
    (by decide) (by decide) hn (by decide) (by decide)
    (by decide) (by decide) (by decide) hcurve

#print axioms cf_v97_cubic_identity_from_defect
#print axioms cf_v97_full_twisted_cube_reduction
#print axioms cf_v97_curve_index_coverage
#print axioms cf_v97_curve_count
#print axioms cf_v97_rational_exception_excluded

end NestedBinomialV10
