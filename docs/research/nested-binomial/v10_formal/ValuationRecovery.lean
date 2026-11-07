import Mathlib.Tactic
import Mathlib.NumberTheory.Padics.PadicVal.Basic

namespace NestedBinomialV10

theorem top_dvd_bottom_mul_choose (n k : ℕ) : n ∣ k * n.choose k := by
  cases n with
  | zero => cases k <;> simp [Nat.choose]
  | succ n =>
    cases k with
    | zero => simp
    | succ k =>
      refine ⟨n.choose k, ?_⟩
      simpa [Nat.succ_eq_add_one, Nat.mul_comm] using
        (Nat.add_one_mul_choose_eq n k).symm

/-- The original binomial equation gives the cubic congruence in either outer branch. -/
theorem original_cubic_divisibility (A k X : ℕ) (hk : k ≤ A)
    (heq : A.choose k = X + k ^ 2) :
    A ∣ (min k (A - k)) * (X + (min k (A - k)) ^ 2) := by
  by_cases hm : k ≤ A - k
  · rw [min_eq_left hm]
    simpa [heq] using top_dvd_bottom_mul_choose A k
  · rw [min_eq_right (by omega : A - k ≤ k)]
    let r := A - k
    have hAr : A = k + r := by dsimp [r]; omega
    have hsym : A.choose r = A.choose k := Nat.choose_symm hk
    have hleft : A ∣ r * (X + k ^ 2) := by
      simpa [hsym, heq] using top_dvd_bottom_mul_choose A r
    have hextra : A ∣ 2 * A * r ^ 2 := by
      refine ⟨2 * r ^ 2, ?_⟩
      ring
    have hextra' : A ∣ A ^ 2 * r := by
      refine ⟨A * r, ?_⟩
      ring
    have hid : r * (X + k ^ 2) + 2 * A * r ^ 2 =
        r * (X + r ^ 2) + A ^ 2 * r := by
      rw [hAr]
      ring
    have hd := dvd_add hleft hextra
    rw [hid] at hd
    exact (Nat.dvd_add_iff_left hextra').mpr hd

theorem valuation_le_of_dvd {p A B : ℕ} [Fact p.Prime]
    (hB : B ≠ 0) (h : A ∣ B) : padicValNat p A ≤ padicValNat p B := by
  exact (padicValNat_dvd_iff_le hB).mp ((pow_padicValNat_dvd (p := p) (n := A)).trans h)

theorem nat_valuation_add_eq_min {p a b : ℕ} [Fact p.Prime]
    (ha : a ≠ 0) (hb : b ≠ 0)
    (hne : padicValNat p a ≠ padicValNat p b) :
    padicValNat p (a + b) = min (padicValNat p a) (padicValNat p b) := by
  have hs : (a : ℚ) + (b : ℚ) ≠ 0 := by positivity
  have ha' : (a : ℚ) ≠ 0 := by exact_mod_cast ha
  have hb' : (b : ℚ) ≠ 0 := by exact_mod_cast hb
  have hne' : padicValRat p (a : ℚ) ≠ padicValRat p (b : ℚ) := by
    simp only [padicValRat.of_nat]
    exact_mod_cast hne
  have h := padicValRat.add_eq_min hs ha' hb' hne'
  norm_cast at h

/-- If the full p-part of A is absent from r^3, cancellation forces an even valuation of X. -/
theorem low_cube_valuation_forces_equality {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2))
    (hlow : 3 * padicValNat p r < padicValNat p A) :
    padicValNat p X = 2 * padicValNat p r := by
  by_contra hne
  have hr2 : r ^ 2 ≠ 0 := pow_ne_zero _ hr
  have hsum : X + r ^ 2 ≠ 0 := by omega
  have hprod : r * (X + r ^ 2) ≠ 0 := mul_ne_zero hr hsum
  have hbound := valuation_le_of_dvd (p := p) hprod hdiv
  have hadd := nat_valuation_add_eq_min (p := p) hX hr2 (by simpa using hne)
  rw [padicValNat.mul hr hsum, hadd, padicValNat.pow] at hbound
  have hmin := min_le_right (padicValNat p X) (2 * padicValNat p r)
  omega

/-- Odd valuation of X restores the entire p-part of A in r^3. -/
theorem odd_valuation_recovers_full_cube {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2))
    (hodd : Odd (padicValNat p X)) :
    padicValNat p A ≤ 3 * padicValNat p r := by
  by_contra h
  have hv := low_cube_valuation_forces_equality (p := p) hX hr hdiv (by omega)
  obtain ⟨t, ht⟩ := hodd
  omega

/-- The strong lower bound underlying the recovered divisor B. -/
theorem even_valuation_recovers_cube_part {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2))
    (_heven : Even (padicValNat p X)) :
    min (padicValNat p A) (3 * (padicValNat p X / 2)) ≤
      3 * padicValNat p r := by
  by_cases h : padicValNat p A ≤ 3 * padicValNat p r
  · exact (min_le_left _ _).trans h
  · have hv := low_cube_valuation_forces_equality (p := p) hX hr hdiv (by omega)
    rw [hv]
    omega

/-- Every prime is in the ordinary branch or the exact cancellation branch. -/
theorem valuation_dichotomy {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2)) :
    padicValNat p A ≤ 3 * padicValNat p r ∨
      (padicValNat p X = 2 * padicValNat p r ∧
       3 * padicValNat p r < padicValNat p A) := by
  by_cases h : padicValNat p A ≤ 3 * padicValNat p r
  · exact Or.inl h
  · exact Or.inr ⟨low_cube_valuation_forces_equality hX hr hdiv (by omega), by omega⟩

def recoveredExponent (a x : ℕ) : ℕ :=
  if Even x then min a (3 * (x / 2)) else a

/-- The p-part recovered by the new parity-sensitive divisor always divides r^3. -/
theorem recovered_prime_power_dvd_cube {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2)) :
    p ^ recoveredExponent (padicValNat p A) (padicValNat p X) ∣ r ^ 3 := by
  apply (padicValNat_dvd_iff_le (pow_ne_zero 3 hr)).mpr
  rw [padicValNat.pow]
  unfold recoveredExponent
  split_ifs with hx
  · exact even_valuation_recovers_cube_part hX hr hdiv hx
  · have hodd : Odd (padicValNat p X) := by
      obtain h | h := Nat.even_or_odd (padicValNat p X)
      · exact False.elim (hx h)
      · exact h
    exact odd_valuation_recovers_full_cube hX hr hdiv hodd

/-- Application to the actual outer binomial equation, including both choices of k. -/
theorem original_recovers_prime_power {p A k X : ℕ} [Fact p.Prime]
    (hk : k ≤ A) (hX : X ≠ 0) (hr : min k (A - k) ≠ 0)
    (heq : A.choose k = X + k ^ 2) :
    p ^ recoveredExponent (padicValNat p A) (padicValNat p X) ∣
      (min k (A - k)) ^ 3 :=
  recovered_prime_power_dvd_cube hX hr (original_cubic_divisibility A k X hk heq)

/-- The stronger local alternative used to combine exceptional primes by CRT. -/
theorem critical_exponent_dichotomy {p A X r t d : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2))
    (hA : padicValNat p A = 3 * t + d)
    (hx : padicValNat p X = 2 * t) :
    padicValNat p r = t ∨ t + d ≤ padicValNat p r := by
  by_cases he : padicValNat p r = t
  · exact Or.inl he
  · right
    have hr2 : r ^ 2 ≠ 0 := pow_ne_zero _ hr
    have hsum : X + r ^ 2 ≠ 0 := by omega
    have hprod : r * (X + r ^ 2) ≠ 0 := mul_ne_zero hr hsum
    have hbound := valuation_le_of_dvd (p := p) hprod hdiv
    have hne : padicValNat p X ≠ padicValNat p (r ^ 2) := by
      rw [hx, padicValNat.pow]
      omega
    have hadd := nat_valuation_add_eq_min (p := p) hX hr2 hne
    rw [hA, padicValNat.mul hr hsum, hadd, hx, padicValNat.pow] at hbound
    have hmin := min_le_left (2 * t) (2 * padicValNat p r)
    omega

/-- Once x=a-b, a nonzero residual deficit has only b possible exponents. -/
theorem critical_exponent_parametrization (a b x : ℕ)
    (hab : a = b + x) (heven : Even x) (hcrit : 3 * x < 2 * a) :
    ∃ t : ℕ, t < b ∧ x = 2 * t ∧ a = b + 2 * t ∧ a - 3 * t = b - t := by
  obtain ⟨t, ht⟩ := heven
  refine ⟨t, ?_, ?_, ?_, ?_⟩ <;> omega

#print axioms original_cubic_divisibility
#print axioms low_cube_valuation_forces_equality
#print axioms odd_valuation_recovers_full_cube
#print axioms even_valuation_recovers_cube_part
#print axioms valuation_dichotomy
#print axioms recovered_prime_power_dvd_cube
#print axioms original_recovers_prime_power
#print axioms critical_exponent_dichotomy
#print axioms critical_exponent_parametrization

end NestedBinomialV10
