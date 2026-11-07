import Mathlib.Tactic
import Mathlib.Data.Nat.ChineseRemainder

namespace NestedBinomialV10
theorem finite_crt_exists_unique (indices : List ℕ) (modulus residue : ℕ → ℕ)
    (hcop : indices.Pairwise (fun i j => (modulus i).Coprime (modulus j)))
    (hpos : ∀ i ∈ indices, modulus i ≠ 0) :
    ∃! R : ℕ, R < (indices.map modulus).prod ∧
      ∀ i ∈ indices, Nat.ModEq (modulus i) R (residue i) := by
  classical
  -- Existence via chineseRemainderOfList
  have hex : ∃ R : ℕ, R < (indices.map modulus).prod ∧
      ∀ i ∈ indices, Nat.ModEq (modulus i) R (residue i) := by
    refine ⟨Nat.chineseRemainderOfList residue modulus indices hcop,
      Nat.chineseRemainderOfList_lt_prod residue modulus indices hcop hpos, ?_⟩
    intro i hi
    exact (Nat.chineseRemainderOfList residue modulus indices hcop).prop i hi
  obtain ⟨R, hRlt, hRcong⟩ := hex
  refine ⟨R, ⟨hRlt, hRcong⟩, ?_⟩
  intro R' hR'
  obtain ⟨hR'lt, hR'cong⟩ := hR'
  -- Both R and R' are congruent to residue i mod modulus i for all i
  have hmod : R' ≡ R [MOD (indices.map modulus).prod] :=
    (Nat.modEq_list_map_prod_iff hcop).mpr (fun i hi => (hR'cong i hi).trans (hRcong i hi).symm)
  -- Since both are less than the product, they're equal
  have hlt : R' < (indices.map modulus).prod := hR'lt
  exact Nat.ModEq.eq_of_lt_of_lt hmod hlt hRlt

theorem cubic_prime_power_split (p d u lambda : ℕ)
    (hp : p.Prime) (hunit : p.Coprime lambda)
    (hdiv : p ^ d ∣ u * (u ^ 2 + lambda)) :
    p ^ d ∣ u ∨ p ^ d ∣ u ^ 2 + lambda := by
  classical
  rcases Nat.eq_zero_or_pos d with rfl | hd
  · left; exact one_dvd u
  · by_cases hpu : p ∣ u
    · left
      have hpu2 : p ∣ u ^ 2 := by
        rw [pow_two]; exact hpu.mul_right u
      have hnp : ¬ p ∣ u ^ 2 + lambda := by
        intro h
        have h1 : p ∣ (u ^ 2 + lambda) - u ^ 2 := Nat.dvd_sub h hpu2
        have h2 : (u ^ 2 + lambda) - u ^ 2 = lambda := Nat.add_sub_cancel_left _ _
        rw [h2] at h1
        exact (Nat.Prime.coprime_iff_not_dvd hp).mp hunit h1
      have hcop : Nat.Coprime p (u ^ 2 + lambda) := by
        rw [Nat.Prime.coprime_iff_not_dvd hp]; exact hnp
      have hcopd : Nat.Coprime (p ^ d) (u ^ 2 + lambda) := by
        rw [Nat.coprime_pow_left_iff hd]; exact hcop
      exact hcopd.dvd_of_dvd_mul_right hdiv
    · right
      have hcop : Nat.Coprime p u := (Nat.Prime.coprime_iff_not_dvd hp).mpr hpu
      have hcopd : Nat.Coprime (p ^ d) u := by
        rw [Nat.coprime_pow_left_iff hd]; exact hcop
      exact hcopd.dvd_of_dvd_mul_left hdiv

theorem simultaneous_square_value_crt (moduli : List ℕ) (residue : ℕ → ℕ)
    (hcop : moduli.Pairwise Nat.Coprime) (hpos : ∀ m ∈ moduli, m ≠ 0) :
    ∃ R : ℕ, R < moduli.prod ∧ ∀ u : ℕ,
      (∀ m ∈ moduli, Nat.ModEq m (u ^ 2) (residue m)) ↔
        Nat.ModEq moduli.prod (u ^ 2) R := by
  classical
  let R := Nat.chineseRemainderOfList residue id moduli hcop
  refine ⟨R, ?_, ?_⟩
  · have h := Nat.chineseRemainderOfList_lt_prod residue id moduli hcop hpos
    simpa using h
  · intro u
    constructor
    · intro h
      have h' : u ^ 2 ≡ R [MOD (moduli.map id).prod] := by
        refine (Nat.modEq_list_map_prod_iff hcop).mpr ?_
        intro m hm
        exact (h m hm).trans ((Nat.chineseRemainderOfList residue id moduli hcop).prop m hm).symm
      simpa using h'
    · intro h m hm
      have hR : R ≡ residue m [MOD m] := (Nat.chineseRemainderOfList residue id moduli hcop).prop m hm
      have hprod : u ^ 2 ≡ R [MOD moduli.prod] := h
      have hdvd : m ∣ moduli.prod := List.dvd_prod hm
      have hmod : u ^ 2 ≡ R [MOD m] := Nat.ModEq.of_dvd hdvd hprod
      exact hmod.trans hR

#print axioms finite_crt_exists_unique
#print axioms cubic_prime_power_split
#print axioms simultaneous_square_value_crt

end NestedBinomialV10
