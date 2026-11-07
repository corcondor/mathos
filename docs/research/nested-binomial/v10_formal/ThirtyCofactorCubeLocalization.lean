import Mathlib.Tactic
import ThirtyCofactorCubePrimeExtraction
import ThirtyCofactorPrimeSeparation


namespace NestedBinomialV10
theorem prime_cube_dvd_coprime_factor (a b q : ℕ) (hq : Nat.Prime q) (hcop : Nat.Coprime a b) (hdvd : q ^ 3 ∣ a * b) : q ^ 3 ∣ a ∨ q ^ 3 ∣ b := by
  have hdvd' : q ^ 3 ∣ b * a := mul_comm a b ▸ hdvd
  by_cases ha : q ∣ a
  · left
    have hqb : ¬ q ∣ b := by
      intro hb
      have hqg : q ∣ Nat.gcd a b := Nat.dvd_gcd ha hb
      rw [hcop] at hqg
      have hq1 : q = 1 := Nat.dvd_one.mp hqg
      have hq2 : 2 ≤ q := hq.two_le
      omega
    have hqcb : Nat.Coprime q b := (hq.coprime_iff_not_dvd).mpr hqb
    have hq3cb : Nat.Coprime (q ^ 3) b := hqcb.pow_left 3
    exact hq3cb.dvd_of_dvd_mul_left hdvd'
  · right
    have hqca : Nat.Coprime q a := (hq.coprime_iff_not_dvd).mpr ha
    have hq3ca : Nat.Coprime (q ^ 3) a := hqca.pow_left 3
    exact hq3ca.dvd_of_dvd_mul_right hdvd'

theorem coprime_Q_factors (i : ℕ) (hi : 1 ≤ i) : Nat.Coprime (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6) := by
  rw [Nat.coprime_iff_gcd_eq_one]
  apply Nat.dvd_one.mp
  have hdiv1 : i / Nat.gcd i 3 ∣ i := by
    refine ⟨Nat.gcd i 3, ?_⟩
    rw [mul_comm]
    exact (Nat.mul_div_cancel' (Nat.gcd_dvd_left i 3)).symm
  have hdiv2 : (i - 1) / Nat.gcd (i - 1) 6 ∣ i - 1 := by
    refine ⟨Nat.gcd (i - 1) 6, ?_⟩
    rw [mul_comm]
    exact (Nat.mul_div_cancel' (Nat.gcd_dvd_left (i - 1) 6)).symm
  have hg1 : Nat.gcd (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6) ∣ i :=
    dvd_trans (Nat.gcd_dvd_left (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6)) hdiv1
  have hg2 : Nat.gcd (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6) ∣ i - 1 :=
    dvd_trans (Nat.gcd_dvd_right (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6)) hdiv2
  have hsub : Nat.gcd (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6) ∣ i - (i - 1) :=
    Nat.dvd_sub hg1 hg2
  have hione : i - (i - 1) = 1 := by omega
  rwa [hione] at hsub

theorem prime_cube_dvd_index_or_pred (i q : ℕ) (hi : 1 ≤ i) (hq : Nat.Prime q) (hq3 : q ^ 3 ∣ (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6)) : q ^ 3 ∣ i ∨ q ^ 3 ∣ i - 1 := by
  have hcop : Nat.Coprime (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6) :=
    coprime_Q_factors i hi
  rcases prime_cube_dvd_coprime_factor (i / Nat.gcd i 3) ((i - 1) / Nat.gcd (i - 1) 6) q hq hcop hq3 with h | h
  · left
    refine dvd_trans h ?_
    refine ⟨Nat.gcd i 3, ?_⟩
    rw [mul_comm]
    exact (Nat.mul_div_cancel' (Nat.gcd_dvd_left i 3)).symm
  · right
    refine dvd_trans h ?_
    refine ⟨Nat.gcd (i - 1) 6, ?_⟩
    rw [mul_comm]
    exact (Nat.mul_div_cancel' (Nat.gcd_dvd_left (i - 1) 6)).symm

theorem cube_prime_localization (w p a i r : ℕ) (hw : 1 ≤ w) (hp : Nat.Prime p) (ha : 1 ≤ a) (hi : i = w * p ^ a + 2) (hr : 0 < r) (hdvd : (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) ∣ r ^ 3) (hnot : ¬ (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) ∣ r ^ 2) : ∃ q : ℕ, Nat.Prime q ∧ (q ^ 3 ∣ i ∨ q ^ 3 ∣ i - 1) ∧ (q = 2 ∨ Nat.Coprime q (w * p)) := by
  have hQ : 0 < (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) := by
    by_contra h
    have hQ0 : (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) = 0 := by omega
    rcases hdvd with ⟨c, hc⟩
    rw [hQ0, zero_mul] at hc
    have hr3 : 0 < r ^ 3 := pow_pos hr 3
    exact hr3.ne' hc
  have hi1 : 1 ≤ i := by
    rw [hi]
    omega
  obtain ⟨q, hq, hq3Q, _⟩ :=
    prime_cube_dvd_of_dvd_cube_not_dvd_sq
      ((i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6)) r hQ hr hdvd hnot
  exact ⟨q, hq,
    prime_cube_dvd_index_or_pred i q hi1 hq hq3Q,
    cube_prime_coprime_or_two w p a i hw hp ha hi q hq hq3Q⟩

#print axioms prime_cube_dvd_coprime_factor
#print axioms coprime_Q_factors
#print axioms prime_cube_dvd_index_or_pred
#print axioms cube_prime_localization

end NestedBinomialV10
