import NormalizedCancellation

namespace NestedBinomialV10
theorem critical_normalized_square_congruence {p A X r t d : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0) (hdiv : A ∣ r * (X + r ^ 2))
    (hA : padicValNat p A = 3 * t + d) (hd : 0 < d)
    (he : padicValNat p r = t) :
    p ^ d ∣ X / p ^ (2 * t) + (r / p ^ t) ^ 2 := by
  have hlow : 3 * padicValNat p r < padicValNat p A := by
    rw [hA]
    omega
  have hcong := normalized_square_congruence hX hr hdiv hlow
  have hAr : padicValNat p A - 3 * padicValNat p r = d := by
    rw [hA]
    omega
  rw [hAr] at hcong
  have he' : padicValNat p r = t := he
  rw [he'] at hcong
  exact hcong

theorem nonsquare_forces_large_valuation {p A X r t d : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0) (hdiv : A ∣ r * (X + r ^ 2))
    (hA : padicValNat p A = 3 * t + d) (hx : padicValNat p X = 2 * t)
    (hd : 0 < d) (hnonsquare : ¬ ∃ z : ℕ, p ^ d ∣ X / p ^ (2 * t) + z ^ 2) :
    t + d ≤ padicValNat p r := by
  have hdich := critical_exponent_dichotomy (p := p) (A := A) (X := X) (r := r) (t := t) (d := d) hX hr hdiv hA hx
  rcases hdich with he | hge
  · exfalso
    apply hnonsquare
    exact ⟨r / p ^ t, critical_normalized_square_congruence hX hr hdiv hA hd he⟩
  · exact hge

theorem nonsquare_recovers_prime_power {p A X r t d : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0) (hdiv : A ∣ r * (X + r ^ 2))
    (hA : padicValNat p A = 3 * t + d) (hx : padicValNat p X = 2 * t)
    (hd : 0 < d) (hnonsquare : ¬ ∃ z : ℕ, p ^ d ∣ X / p ^ (2 * t) + z ^ 2) :
    p ^ padicValNat p A ∣ r ^ 3 := by
  have hge := nonsquare_forces_large_valuation (p := p) (A := A) (X := X) (r := r) (t := t) (d := d) hX hr hdiv hA hx hd hnonsquare
  have hcube : 3 * t ≤ 3 * padicValNat p r := by omega
  have hA' : padicValNat p A = 3 * t + d := hA
  have hle : padicValNat p A ≤ 3 * padicValNat p r := by omega
  exact (padicValNat_dvd_iff_le (pow_ne_zero 3 hr)).mpr (by
    rw [padicValNat.pow]
    exact hle)

theorem original_nonsquare_recovers_prime_power {p A k X t d : ℕ} [Fact p.Prime]
    (hk : k ≤ A) (hX : X ≠ 0) (hr : min k (A - k) ≠ 0)
    (heq : A.choose k = X + k ^ 2)
    (hA : padicValNat p A = 3 * t + d) (hx : padicValNat p X = 2 * t)
    (hd : 0 < d) (hnonsquare : ¬ ∃ z : ℕ, p ^ d ∣ X / p ^ (2 * t) + z ^ 2) :
    p ^ padicValNat p A ∣ (min k (A - k)) ^ 3 := by
  have hge := nonsquare_forces_large_valuation (p := p) (A := A) (X := X) (r := min k (A - k)) (t := t) (d := d) hX hr (original_cubic_divisibility A k X hk heq) hA hx hd hnonsquare
  have hle : padicValNat p A ≤ 3 * padicValNat p (min k (A - k)) := by omega
  exact (padicValNat_dvd_iff_le (pow_ne_zero 3 hr)).mpr (by
    rw [padicValNat.pow]
    exact hle)

#print axioms critical_normalized_square_congruence
#print axioms nonsquare_forces_large_valuation
#print axioms nonsquare_recovers_prime_power
#print axioms original_nonsquare_recovers_prime_power

end NestedBinomialV10
