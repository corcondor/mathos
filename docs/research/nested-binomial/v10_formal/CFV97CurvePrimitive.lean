import Mathlib.Tactic
import CFV97PrimitiveGcd

/-!
# v97: Original cubic curve -> a bounded primitive divisor certificate

This theorem discharges the first *existential* portion missing from
v95: the two gcd-normalized factors really exist for every original
curve point. The conclusion h | 6 and e | T bounds the coefficient
search uniformly. No squarefree decomposition or CF prefix certificate
is assumed or claimed here.
-/

namespace NestedBinomialV10

theorem cf_v97_curve_primitive_factor_certificate
    (S T n r g p q : ℕ)
    (hn : 2 ≤ n) (hg : 0 < g) (hT : 0 < T)
    (hSdiv : S ∣ n - 2)
    (hr : r = g * p) (hq : n - 1 = g * q)
    (hcop : p.Coprime q)
    (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) :
    ∃ h e v : ℕ,
      0 < h ∧ h ∣ 6 ∧ e ∣ T ∧
      T * q ^ 3 - 6 * S * p ^ 3 = h * e ∧
      q = h * v ∧ e.Coprime v ∧ h = Nat.gcd 6 q := by
  let D : ℕ := T * q ^ 3 - 6 * S * p ^ 3
  let h : ℕ := Nat.gcd D q
  have hlt : 6 * S * p ^ 3 < T * q ^ 3 :=
    curve_recovery_lt S T n r g p q hn hg hT hr hq hcurve
  have hDpos : 0 < D := by
    dsimp [D]
    omega
  have hDeq : D + 6 * S * p ^ 3 = T * q ^ 3 := by
    dsimp [D]
    exact Nat.sub_add_cancel (Nat.le_of_lt hlt)
  have hqdiv : q ∣ n - 1 := by
    refine ⟨g, ?_⟩
    rw [hq]
    ring
  have hhExact : h = Nat.gcd 6 q := by
    dsimp [h]
    exact cf_v97_exact_defect_gcd S T n p q D hn hSdiv hqdiv hcop hDeq
  have hh6 : h ∣ 6 := by
    rw [hhExact]
    exact Nat.gcd_dvd_left 6 q
  have hhpos : 0 < h := by
    by_contra hnot
    have hhzero : h = 0 := by omega
    have hdvd : h ∣ D := Nat.gcd_dvd_left D q
    obtain ⟨k, hk⟩ := hdvd
    have hDzero : D = 0 := by simpa [hhzero] using hk
    omega
  obtain ⟨e, he⟩ : ∃ e : ℕ, D = h * e :=
    (show h ∣ D from Nat.gcd_dvd_left D q)
  obtain ⟨v, hv⟩ : ∃ v : ℕ, q = h * v :=
    (show h ∣ q from Nat.gcd_dvd_right D q)
  have hcopEV : e.Coprime v :=
    cf_v97_quotients_coprime D q h e v hhpos he hv rfl
  have hrec : g ^ 2 * D = T * q := by
    simpa only [D] using
      (curve_recovery_eq S T n r g p q hn hg hr hq hcurve).symm
  have hfact : g ^ 2 * (h * e) = T * (h * v) := by
    calc
      g ^ 2 * (h * e) = g ^ 2 * D := by rw [← he]
      _ = T * q := hrec
      _ = T * (h * v) := by rw [hv]
  have heT : e ∣ T :=
    cf_v97_primitive_defect_divides_T T g h e v hhpos hcopEV hfact
  refine ⟨h, e, v, hhpos, hh6, heT, ?_, hv, hcopEV, hhExact⟩
  simpa only [D] using he

#print axioms cf_v97_curve_primitive_factor_certificate

end NestedBinomialV10
