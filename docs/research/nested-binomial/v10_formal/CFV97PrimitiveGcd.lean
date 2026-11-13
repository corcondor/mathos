import Mathlib.Tactic
import CFTwistedCubeAlgebra

/-!
# v97: gcd-normalization and primitive divisors for the v96 certificate

These lemmas formalize the missing beginning of v95's twisted-cube
parameterization.  They do not assume the finite Python certificate.
The full squarefree decomposition and 5214-case Lean reflection remain
separate unproved obligations.
-/

namespace NestedBinomialV10

/-- S divides n-2 and q divides n-1, so they are coprime. -/
theorem cf_v97_coprime_from_neighbors
    (S q n : ℕ) (hn : 2 ≤ n)
    (hS : S ∣ n - 2) (hq : q ∣ n - 1) : S.Coprime q := by
  have hA : Nat.gcd S q ∣ n - 2 :=
    dvd_trans (Nat.gcd_dvd_left S q) hS
  have hB : Nat.gcd S q ∣ n - 1 :=
    dvd_trans (Nat.gcd_dvd_right S q) hq
  have hC : Nat.gcd S q ∣ (n - 1) - (n - 2) := Nat.dvd_sub hB hA
  have hOne : (n - 1) - (n - 2) = 1 := by omega
  rw [hOne] at hC
  exact Nat.coprime_iff_gcd_eq_one.mpr (Nat.dvd_one.mp hC)

/-- The primitive cubic difference has exactly the same gcd with q
as the coefficient 6*S; this is the key missing gcd identity in v95. -/
theorem cf_v97_gcd_cubic_difference
    (S T p q D : ℕ) (hcop : p.Coprime q)
    (hD : D + 6 * S * p ^ 3 = T * q ^ 3) :
    Nat.gcd D q = Nat.gcd (6 * S) q := by
  let d := Nat.gcd D q
  let e := Nat.gcd (6 * S) q
  have hqT : q ∣ T * q ^ 3 := by
    refine ⟨T * q ^ 2, ?_⟩
    ring
  have hdA : d ∣ (6 * S) * p ^ 3 := by
    have hsum : d ∣ D + 6 * S * p ^ 3 := by
      rw [hD]
      exact dvd_trans (Nat.gcd_dvd_right D q) hqT
    have hsub : d ∣ (D + 6 * S * p ^ 3) - D :=
      Nat.dvd_sub hsum (Nat.gcd_dvd_left D q)
    simpa only [Nat.add_sub_cancel_left] using hsub
  have hdB : d ∣ (6 * S) * q :=
    dvd_mul_of_dvd_right (Nat.gcd_dvd_right D q) (6 * S)
  have hd6S : d ∣ 6 * S := by
    have h : d ∣ Nat.gcd ((6 * S) * p ^ 3) ((6 * S) * q) :=
      Nat.dvd_gcd hdA hdB
    rw [Nat.gcd_mul_left, (hcop.pow_left 3).gcd_eq_one, Nat.mul_one] at h
    exact h
  have heA : e ∣ (6 * S) * p ^ 3 :=
    dvd_mul_of_dvd_left (Nat.gcd_dvd_left (6 * S) q) (p ^ 3)
  have heB : e ∣ T * q ^ 3 :=
    dvd_trans (Nat.gcd_dvd_right (6 * S) q) hqT
  have hDexpr : T * q ^ 3 - 6 * S * p ^ 3 = D := by omega
  have heD : e ∣ D := by
    have h : e ∣ T * q ^ 3 - 6 * S * p ^ 3 :=
      Nat.dvd_sub heB heA
    rwa [hDexpr] at h
  have hde : d ∣ e :=
    Nat.dvd_gcd hd6S (Nat.gcd_dvd_right D q)
  have hed : e ∣ d :=
    Nat.dvd_gcd heD (Nat.gcd_dvd_right (6 * S) q)
  exact Nat.dvd_antisymm hde hed

/-- If S is coprime to q, the factor S can be stripped from gcd(6*S,q). -/
theorem cf_v97_gcd_six_times
    (S q : ℕ) (hcop : S.Coprime q) :
    Nat.gcd (6 * S) q = Nat.gcd 6 q := by
  let d := Nat.gcd (6 * S) q
  let e := Nat.gcd 6 q
  have hd6q : d ∣ 6 * q :=
    dvd_mul_of_dvd_right (Nat.gcd_dvd_right (6 * S) q) 6
  have hd6 : d ∣ 6 := by
    have h : d ∣ Nat.gcd (6 * S) (6 * q) :=
      Nat.dvd_gcd (Nat.gcd_dvd_left (6 * S) q) hd6q
    rw [Nat.gcd_mul_left, hcop.gcd_eq_one, Nat.mul_one] at h
    exact h
  have hed6S : e ∣ 6 * S :=
    dvd_mul_of_dvd_left (Nat.gcd_dvd_left 6 q) S
  exact Nat.dvd_antisymm
    (Nat.dvd_gcd hd6 (Nat.gcd_dvd_right (6 * S) q))
    (Nat.dvd_gcd hed6S (Nat.gcd_dvd_right 6 q))

/-- The gcd in the v95 primitive recovery equals gcd(6,q), hence divides 6. -/
theorem cf_v97_exact_defect_gcd
    (S T n p q D : ℕ) (hn : 2 ≤ n)
    (hS : S ∣ n - 2) (hq : q ∣ n - 1)
    (hcop : p.Coprime q)
    (hD : D + 6 * S * p ^ 3 = T * q ^ 3) :
    Nat.gcd D q = Nat.gcd 6 q := by
  calc
    Nat.gcd D q = Nat.gcd (6 * S) q :=
      cf_v97_gcd_cubic_difference S T p q D hcop hD
    _ = Nat.gcd 6 q :=
      cf_v97_gcd_six_times S q
        (cf_v97_coprime_from_neighbors S q n hn hS hq)

/-- After removing the common gcd, the two quotients are coprime. -/
theorem cf_v97_quotients_coprime
    (D q h e v : ℕ) (hh : 0 < h)
    (hD : D = h * e) (hq : q = h * v)
    (hgcd : h = Nat.gcd D q) : e.Coprime v := by
  have hcancel : h * Nat.gcd e v = h * 1 := by
    calc
      h * Nat.gcd e v = Nat.gcd (h * e) (h * v) := by
        rw [Nat.gcd_mul_left]
      _ = h := by rw [← hD, ← hq]; exact hgcd.symm
      _ = h * 1 := by ring
  have hOne : Nat.gcd e v = 1 :=
    Nat.eq_of_mul_eq_mul_left hh hcancel
  exact Nat.coprime_iff_gcd_eq_one.mpr hOne

/-- The primitive defect factor e always divides T, without a search. -/
theorem cf_v97_primitive_defect_divides_T
    (T g h e v : ℕ) (hh : 0 < h)
    (hcop : e.Coprime v)
    (heq : g ^ 2 * (h * e) = T * (h * v)) : e ∣ T := by
  have hcancel : h * (g ^ 2 * e) = h * (T * v) := by
    calc
      h * (g ^ 2 * e) = g ^ 2 * (h * e) := by ring
      _ = T * (h * v) := heq
      _ = h * (T * v) := by ring
  have hcore : g ^ 2 * e = T * v :=
    Nat.eq_of_mul_eq_mul_left hh hcancel
  have hdiv : e ∣ T * v := by
    rw [← hcore]
    exact ⟨g ^ 2, by ring⟩
  exact (hcop.dvd_mul_right).mp hdiv

#print axioms cf_v97_coprime_from_neighbors
#print axioms cf_v97_gcd_cubic_difference
#print axioms cf_v97_gcd_six_times
#print axioms cf_v97_exact_defect_gcd
#print axioms cf_v97_quotients_coprime
#print axioms cf_v97_primitive_defect_divides_T

end NestedBinomialV10
