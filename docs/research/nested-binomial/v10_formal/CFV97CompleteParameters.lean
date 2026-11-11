import Mathlib.Tactic
import CFV97SquarefreeBridge

/-!
# v97: Construct the v95 twisted-cube parameters from the ORIGINAL curve

For EVERY original curve point with S | n-2 and primitive p/q,
this module derives the squarefree coefficient and square lift.
No finite-certificate enumeration, CF precision bound, or unexplained
decomposition hypothesis appears in the statement. Both final frozen
theorems still require the independent finite certificate.
-/

namespace NestedBinomialV10

/-- Dividing the primitive defect equation by e yields the squarefree
parameterization, provided T>0 and e>0. -/
theorem cf_v97_squarefree_parameters_from_core
    (T e g v : ℕ)
    (hT : 0 < T) (he : 0 < e)
    (hedvd : e ∣ T)
    (hcore : g ^ 2 * e = T * v) :
    ∃ A s z : ℕ, Squarefree s ∧ 0 < A ∧ 0 < s ∧
      T = e * (s * A ^ 2) ∧ v = s * z ^ 2 ∧ g = A * s * z := by
  obtain ⟨A, s, hsquare, hfactor⟩ :=
    cf_v97_squarefree_coefficient T e hedvd
  have hA : 0 < A := by
    by_contra hnot
    have hzero : A = 0 := by omega
    have hTzero : T = 0 := by rw [hfactor, hzero]; simp
    omega
  have hs : 0 < s := by
    by_contra hnot
    have hzero : s = 0 := by omega
    have hTzero : T = 0 := by rw [hfactor, hzero]; simp
    omega
  have hcancel : e * g ^ 2 = e * ((A ^ 2 * s) * v) := by
    calc
      e * g ^ 2 = g ^ 2 * e := by ring
      _ = T * v := hcore
      _ = (e * (s * A ^ 2)) * v := by rw [hfactor]
      _ = e * ((A ^ 2 * s) * v) := by ring
  have hsqeq : g ^ 2 = (A ^ 2 * s) * v :=
    Nat.eq_of_mul_eq_mul_left he hcancel
  obtain ⟨z, hgz, hvz⟩ :=
    cf_v97_squarefree_square_lift A s g v hA hs hsquare hsqeq
  exact ⟨A, s, z, hsquare, hA, hs, hfactor, hvz, hgz⟩

/-- Full existential v95 squarefree data, now derived from the original
cubic equation and the original S | n-2 restriction. -/
theorem cf_v97_curve_twisted_cube_parameters
    (S T n r g p q : ℕ)
    (hn : 2 ≤ n) (hg : 0 < g) (hT : 0 < T)
    (hSdiv : S ∣ n - 2)
    (hr : r = g * p) (hq : n - 1 = g * q)
    (hcop : p.Coprime q)
    (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) :
    ∃ h e A s z : ℕ,
      0 < h ∧ h ∣ 6 ∧ e ∣ T ∧ Squarefree s ∧
      0 < A ∧ 0 < s ∧ T = e * (s * A ^ 2) ∧
      T * q ^ 3 - 6 * S * p ^ 3 = h * e ∧
      h = Nat.gcd 6 q ∧ q = h * s * z ^ 2 ∧
      g = A * s * z ∧ n - 1 = h * A * s ^ 2 * z ^ 3 := by
  obtain ⟨h, e, v, hh, hh6, hedvd, hD, hqv, _, hhgcd⟩ :=
    cf_v97_curve_primitive_factor_certificate
      S T n r g p q hn hg hT hSdiv hr hq hcop hcurve
  have hlt : 6 * S * p ^ 3 < T * q ^ 3 :=
    curve_recovery_lt S T n r g p q hn hg hT hr hq hcurve
  have hDpos : 0 < T * q ^ 3 - 6 * S * p ^ 3 := by omega
  have he : 0 < e := by
    by_contra hnot
    have he0 : e = 0 := by omega
    have hD0 : T * q ^ 3 - 6 * S * p ^ 3 = 0 := by
      rw [hD, he0]
      simp
    omega
  have hcancel : h * (g ^ 2 * e) = h * (T * v) := by
    calc
      h * (g ^ 2 * e) = g ^ 2 * (h * e) := by ring
      _ = g ^ 2 * (T * q ^ 3 - 6 * S * p ^ 3) := by rw [← hD]
      _ = T * q := (curve_recovery_eq S T n r g p q hn hg hr hq hcurve).symm
      _ = T * (h * v) := by rw [hqv]
      _ = h * (T * v) := by ring
  have hcore : g ^ 2 * e = T * v :=
    Nat.eq_of_mul_eq_mul_left hh hcancel
  obtain ⟨A, s, z, hsquare, hA, hs, hTfact, hvz, hgz⟩ :=
    cf_v97_squarefree_parameters_from_core T e g v hT he hedvd hcore
  have hqtwist : q = h * s * z ^ 2 := by
    calc
      q = h * v := hqv
      _ = h * (s * z ^ 2) := by rw [hvz]
      _ = h * s * z ^ 2 := by ring
  have hntwist : n - 1 = h * A * s ^ 2 * z ^ 3 :=
    cf_twisted_cube_recover_n g q h s A z hqtwist hgz hq
  exact ⟨h, e, A, s, z, hh, hh6, hedvd, hsquare, hA, hs, hTfact,
    hD, hhgcd, hqtwist, hgz, hntwist⟩

#print axioms cf_v97_squarefree_parameters_from_core
#print axioms cf_v97_curve_twisted_cube_parameters

end NestedBinomialV10
