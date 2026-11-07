import ValuationRecovery
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.GCD.BigOperators

/-!
Global assembly of the prime-local recovery proved in ValuationRecovery.
This extends the v10 formalization, not the underlying mathematical claim.
No analytic height bound, finite certificate completeness, or global
nonexistence assertion is assumed or proved here.
-/

namespace NestedBinomialV10

open scoped BigOperators

theorem recoveredExponent_le (a x : ℕ) : recoveredExponent a x ≤ a := by
  unfold recoveredExponent
  split_ifs
  · exact min_le_left _ _
  · exact le_refl _

theorem min_le_recoveredExponent (a x : ℕ) : min a x ≤ recoveredExponent a x := by
  unfold recoveredExponent
  split_ifs with hx
  · obtain ⟨t, ht⟩ := hx
    omega
  · exact min_le_left _ _

/-- Distinct prime bases allow local divisibilities to be multiplied. -/
theorem prime_power_product_dvd (s : Finset ℕ) (e : ℕ → ℕ) (N : ℕ)
    (hprime : ∀ p ∈ s, p.Prime) (hlocal : ∀ p ∈ s, p ^ e p ∣ N) :
    (∏ p ∈ s, p ^ e p) ∣ N := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert p s hp ih =>
    rw [Finset.prod_insert hp]
    have hcop : (p ^ e p).Coprime (∏ q ∈ s, q ^ e q) := by
      apply Nat.Coprime.prod_right
      intro q hq
      apply Nat.coprime_pow_primes _ _ (hprime p (Finset.mem_insert_self _ _))
        (hprime q (Finset.mem_insert_of_mem hq))
      intro heq
      exact hp (heq ▸ hq)
    exact hcop.mul_dvd_of_dvd_of_dvd (hlocal p (Finset.mem_insert_self _ _))
      (ih (fun q hq => hprime q (Finset.mem_insert_of_mem hq))
        (fun q hq => hlocal q (Finset.mem_insert_of_mem hq)))

/-- The recovered divisor B, defined directly from its prime exponents. -/
def recoveredDivisor (A X : ℕ) : ℕ :=
  ∏ p ∈ A.primeFactors, p ^ recoveredExponent (padicValNat p A) (padicValNat p X)

/-- The deficit E = A/B; A != 0 is required for positive arithmetic use. -/
def recoveredDefect (A X : ℕ) : ℕ := A / recoveredDivisor A X

/-- The exponent d_p used to define E in the v10 mathematical note. -/
def deficitExponent (a x : ℕ) : ℕ := if Even x then a - 3 * (x / 2) else 0

theorem deficitExponent_add_recoveredExponent (a x : ℕ) :
    deficitExponent a x + recoveredExponent a x = a := by
  unfold deficitExponent recoveredExponent
  split_ifs <;> omega

/-- The note's original definition of E as a product, not a quotient. -/
def recoveredDefectProduct (A X : ℕ) : ℕ :=
  ∏ p ∈ A.primeFactors, p ^ deficitExponent (padicValNat p A) (padicValNat p X)

theorem recoveredDivisor_dvd (A X : ℕ) : recoveredDivisor A X ∣ A := by
  apply prime_power_product_dvd
  · exact fun p hp => Nat.prime_of_mem_primeFactors hp
  · intro p hp
    exact (pow_dvd_pow p (recoveredExponent_le _ _)).trans
      (pow_padicValNat_dvd (p := p) (n := A))

theorem recoveredDivisor_dvd_cube {A X r : ℕ}
    (hX : X ≠ 0) (hr : r ≠ 0) (hdiv : A ∣ r * (X + r ^ 2)) :
    recoveredDivisor A X ∣ r ^ 3 := by
  apply prime_power_product_dvd
  · exact fun p hp => Nat.prime_of_mem_primeFactors hp
  · intro p hp
    have : Fact p.Prime := ⟨Nat.prime_of_mem_primeFactors hp⟩
    exact recovered_prime_power_dvd_cube hX hr hdiv

theorem gcd_dvd_recoveredDivisor {A X : ℕ} (hA : A ≠ 0) (hX : X ≠ 0) :
    Nat.gcd A X ∣ recoveredDivisor A X := by
  have hg : Nat.gcd A X ≠ 0 := (Nat.gcd_pos_of_pos_left X (Nat.pos_of_ne_zero hA)).ne'
  rw [Nat.prod_primeFactors_pow_factorization hg]
  apply prime_power_product_dvd
  · exact fun p hp => Nat.prime_of_mem_primeFactors hp
  · intro p hp
    have hpp := Nat.prime_of_mem_primeFactors hp
    have : Fact p.Prime := ⟨hpp⟩
    have hpA : p ∈ A.primeFactors := Nat.mem_primeFactors.mpr
      ⟨hpp, (Nat.dvd_of_mem_primeFactors hp).trans (Nat.gcd_dvd_left A X), hA⟩
    have hga := valuation_le_of_dvd (p := p) hA (Nat.gcd_dvd_left A X)
    have hgx := valuation_le_of_dvd (p := p) hX (Nat.gcd_dvd_right A X)
    have he : (Nat.gcd A X).factorization p ≤
        recoveredExponent (padicValNat p A) (padicValNat p X) := by
      rw [Nat.factorization_def _ hpp]
      exact (le_min hga hgx).trans (min_le_recoveredExponent _ _)
    exact (pow_dvd_pow p he).trans (Finset.dvd_prod_of_mem
      (fun q => q ^ recoveredExponent (padicValNat q A) (padicValNat q X)) hpA)

theorem recoveredDefect_dvd_old_defect {A X : ℕ} (hA : A ≠ 0) (hX : X ≠ 0) :
    recoveredDefect A X ∣ A / Nat.gcd A X :=
  Nat.div_dvd_div_left (recoveredDivisor_dvd A X) (gcd_dvd_recoveredDivisor hA hX)

theorem recoveredDefect_mul_recoveredDivisor (A X : ℕ) :
    recoveredDefect A X * recoveredDivisor A X = A :=
  Nat.div_mul_cancel (recoveredDivisor_dvd A X)

theorem recoveredDefectProduct_mul_recoveredDivisor {A X : ℕ} (hA : A ≠ 0) :
    recoveredDefectProduct A X * recoveredDivisor A X = A := by
  unfold recoveredDefectProduct recoveredDivisor
  rw [← Finset.prod_mul_distrib]
  calc
    _ = ∏ p ∈ A.primeFactors, p ^ A.factorization p := by
      apply Finset.prod_congr rfl
      intro p hp
      rw [← pow_add, deficitExponent_add_recoveredExponent,
        Nat.factorization_def _ (Nat.prime_of_mem_primeFactors hp)]
    _ = A := (Nat.prod_primeFactors_pow_factorization hA).symm

/-- The product and quotient definitions of the recovered deficit agree. -/
theorem recoveredDefectProduct_eq_recoveredDefect {A X : ℕ} (hA : A ≠ 0) :
    recoveredDefectProduct A X = recoveredDefect A X := by
  have hB : recoveredDivisor A X ≠ 0 := by
    intro hz
    have := recoveredDivisor_dvd A X
    rw [hz, zero_dvd_iff] at this
    exact hA this
  apply Nat.eq_of_mul_eq_mul_right (Nat.pos_of_ne_zero hB)
  rw [recoveredDefectProduct_mul_recoveredDivisor hA,
    recoveredDefect_mul_recoveredDivisor]

theorem recoveredDefectProduct_dvd_old_defect {A X : ℕ} (hA : A ≠ 0) (hX : X ≠ 0) :
    recoveredDefectProduct A X ∣ A / Nat.gcd A X := by
  rw [recoveredDefectProduct_eq_recoveredDefect hA]
  exact recoveredDefect_dvd_old_defect hA hX

/-- Direct application to both outer branches of the actual binomial equation. -/
theorem original_recovers_divisor {A k X : ℕ}
    (hk : k ≤ A) (hX : X ≠ 0) (hr : min k (A - k) ≠ 0)
    (heq : A.choose k = X + k ^ 2) :
    recoveredDivisor A X ∣ (min k (A - k)) ^ 3 :=
  recoveredDivisor_dvd_cube hX hr (original_cubic_divisibility A k X hk heq)

#print axioms recoveredDivisor_dvd
#print axioms recoveredDivisor_dvd_cube
#print axioms gcd_dvd_recoveredDivisor
#print axioms recoveredDefect_dvd_old_defect
#print axioms recoveredDefect_mul_recoveredDivisor
#print axioms recoveredDefectProduct_mul_recoveredDivisor
#print axioms recoveredDefectProduct_eq_recoveredDefect
#print axioms recoveredDefectProduct_dvd_old_defect
#print axioms original_recovers_divisor

end NestedBinomialV10
