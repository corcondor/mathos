import Mathlib.Tactic


namespace NestedBinomialV10
theorem odd_prime_not_dvd_Q (w p a i : ℕ) (hw : 1 ≤ w) (hp : Nat.Prime p) (ha : 1 ≤ a) (hi : i = w * p ^ a + 2) (q : ℕ) (hq : Nat.Prime q) (hq2 : q ≠ 2) (hqwp : q ∣ w * p) : ¬ (q ∣ (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6)) := by
  have hpa : q ∣ w * p ^ a := by
    obtain ⟨c, rfl⟩ : ∃ c, a = c + 1 := ⟨a - 1, by omega⟩
    rw [pow_succ]
    rw [show w * (p ^ c * p) = (w * p) * p ^ c by ring]
    exact dvd_mul_of_dvd_left hqwp (p ^ c)
  have hqi : ¬ q ∣ i := by
    intro hdiv
    have hsum : q ∣ w * p ^ a + 2 := by
      rw [← hi]
      exact hdiv
    have hsum' : q ∣ 2 + w * p ^ a := by
      rw [Nat.add_comm]
      exact hsum
    have hq2dvd : q ∣ 2 := (Nat.dvd_add_iff_left hpa).mpr hsum'
    rcases Nat.prime_two.eq_one_or_self_of_dvd q hq2dvd with h1 | h2
    · have := hq.two_le
      omega
    · exact hq2 h2
  have hqi1 : ¬ q ∣ i - 1 := by
    intro hdiv
    have hsub : i - 1 = w * p ^ a + 1 := by
      rw [hi]
      omega
    rw [hsub] at hdiv
    have hsum' : q ∣ 1 + w * p ^ a := by
      rw [Nat.add_comm]
      exact hdiv
    have hq1dvd : q ∣ 1 := (Nat.dvd_add_iff_left hpa).mpr hsum'
    have hqeq1 : q = 1 := Nat.dvd_one.mp hq1dvd
    have := hq.two_le
    omega
  intro hprod
  rcases hq.dvd_mul.mp hprod with hleft | hright
  · have hg : Nat.gcd i 3 ∣ i := Nat.gcd_dvd_left i 3
    have heq : Nat.gcd i 3 * (i / Nat.gcd i 3) = i := Nat.mul_div_cancel' hg
    have hdiv : q ∣ Nat.gcd i 3 * (i / Nat.gcd i 3) := dvd_mul_of_dvd_right hleft _
    rw [heq] at hdiv
    exact hqi hdiv
  · have hg : Nat.gcd (i - 1) 6 ∣ i - 1 := Nat.gcd_dvd_left (i - 1) 6
    have heq : Nat.gcd (i - 1) 6 * ((i - 1) / Nat.gcd (i - 1) 6) = i - 1 := Nat.mul_div_cancel' hg
    have hdiv : q ∣ Nat.gcd (i - 1) 6 * ((i - 1) / Nat.gcd (i - 1) 6) := dvd_mul_of_dvd_right hright _
    rw [heq] at hdiv
    exact hqi1 hdiv

theorem cube_prime_coprime_or_two (w p a i : ℕ) (hw : 1 ≤ w) (hp : Nat.Prime p) (ha : 1 ≤ a) (hi : i = w * p ^ a + 2) (q : ℕ) (hq : Nat.Prime q) (hq3 : q ^ 3 ∣ (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6)) : q = 2 ∨ Nat.Coprime q (w * p) := by
  by_cases hq2 : q = 2
  · exact Or.inl hq2
  · right
    by_contra hcop
    have hdiv : q ∣ w * p := (Nat.Prime.dvd_iff_not_coprime hq).mpr hcop
    have hq_dvd : q ∣ (i / Nat.gcd i 3) * ((i - 1) / Nat.gcd (i - 1) 6) :=
      dvd_trans (show q ∣ q ^ 3 from ⟨q ^ 2, by ring⟩) hq3
    exact (NestedBinomialV10.odd_prime_not_dvd_Q w p a i hw hp ha hi q hq hq2 hdiv) hq_dvd

#print axioms odd_prime_not_dvd_Q
#print axioms cube_prime_coprime_or_two

end NestedBinomialV10
