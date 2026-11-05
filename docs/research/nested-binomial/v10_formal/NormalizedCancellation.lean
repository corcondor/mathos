import ValuationRecovery

namespace NestedBinomialV10

/-!
# Normalized cancellation for the cubic congruence

Given `A ∣ r * (X + r^2)` with `e = padicValNat p r`, `a = padicValNat p A`,
and `3e < a`, we prove:

* `padicValNat p X = 2e`;
* `Nat.Coprime p (r / p^e)`;
* `p^(a - 3e) ∣ X / p^(2e) + (r / p^e)^2`.

The last statement is the normalized square congruence `u^2 ≡ -v mod p^(a-3e)`
written as a natural-number divisibility.
-/

/-- General cancellation: if `d` is coprime to `c` and `d ∣ c * a`, then `d ∣ a`. -/
theorem dvd_of_dvd_mul_of_coprime {d a c : ℕ} (hcop : Nat.Coprime d c)
    (h : d ∣ c * a) : d ∣ a :=
  hcop.dvd_of_dvd_mul_left h

/-- The valuation of `X` is exactly `2e` under the strict inequality `3e < a`. -/
theorem normalized_valuation_X {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2))
    (hlow : 3 * padicValNat p r < padicValNat p A) :
    padicValNat p X = 2 * padicValNat p r :=
  low_cube_valuation_forces_equality hX hr hdiv hlow

/-- `p` is coprime to the normalized `r / p^e`. -/
theorem coprime_p_normalized_r {p r e : ℕ} [Fact p.Prime]
    (hr : r ≠ 0) (he : e = padicValNat p r) :
    Nat.Coprime p (r / p ^ e) := by
  have hp : p.Prime := Fact.out
  rw [Nat.Prime.coprime_iff_not_dvd hp]
  intro hdvd
  -- If `p ∣ r / p^e`, then `p^(e+1) ∣ r`, contradicting `e = padicValNat p r`.
  have hpe : p ^ e ∣ r := by
    simpa [he] using (pow_padicValNat_dvd (p := p) (n := r))
  have hmul : p ^ e * (r / p ^ e) = r := Nat.mul_div_cancel' hpe
  have hstep := Nat.mul_dvd_mul_left (p ^ e) hdvd
  rw [hmul] at hstep
  have hpe1 : p ^ (e + 1) ∣ r := by
    simpa [pow_succ] using hstep
  have hle : e + 1 ≤ padicValNat p r :=
    (padicValNat_dvd_iff_le hr).mp hpe1
  omega

/-- The normalized square congruence in divisibility form. -/
theorem normalized_square_congruence {p A X r : ℕ} [Fact p.Prime]
    (hX : X ≠ 0) (hr : r ≠ 0)
    (hdiv : A ∣ r * (X + r ^ 2))
    (hlow : 3 * padicValNat p r < padicValNat p A) :
    p ^ (padicValNat p A - 3 * padicValNat p r) ∣
      X / p ^ (2 * padicValNat p r) +
        (r / p ^ padicValNat p r) ^ 2 := by
  let e := padicValNat p r
  let a := padicValNat p A
  have he : e = padicValNat p r := rfl
  have ha : a = padicValNat p A := rfl
  have hp : p.Prime := Fact.out
  have hlow' : 3 * e < a := by simpa [e, a] using hlow
  have hXv : padicValNat p X = 2 * e :=
    normalized_valuation_X hX hr hdiv (by simpa [e, a] using hlow)
  -- Divisibility witnesses.
  have hpe : p ^ e ∣ r := by
    simpa [he] using (pow_padicValNat_dvd (p := p) (n := r))
  have hXe : p ^ (2 * e) ∣ X := by
    have : p ^ padicValNat p X ∣ X := pow_padicValNat_dvd
    rwa [hXv] at this
  obtain ⟨u, hu⟩ := hpe
  obtain ⟨v, hv⟩ := hXe
  -- `u = r / p^e`, `v = X / p^(2e)`.
  have hu' : u = r / p ^ e := by
    rw [hu, Nat.mul_div_cancel_left _ (pow_pos hp.pos _)]
  have hv' : v = X / p ^ (2 * e) := by
    rw [hv, Nat.mul_div_cancel_left _ (pow_pos hp.pos _)]
  -- Algebraic identity: `r * (X + r^2) = p^(3e) * (u * (v + u^2))`.
  have hpow : p ^ (3 * e) = p ^ e * p ^ e * p ^ e := by
    rw [show 3 * e = e + e + e by ring, pow_add, pow_add]
  have halg : r * (X + r ^ 2) = p ^ (3 * e) * (u * (v + u ^ 2)) := by
    rw [hu, hv, hpow]
    ring
  -- `p^a ∣ r * (X + r^2)` from `A ∣ ...` and `p^a ∣ A`.
  have hpaA : p ^ a ∣ A := by
    simpa [ha] using (pow_padicValNat_dvd (p := p) (n := A))
  have hpa_prod : p ^ a ∣ r * (X + r ^ 2) := hpaA.trans hdiv
  rw [halg] at hpa_prod
  -- Split `p^a = p^(3e) * p^(a - 3e)` and cancel `p^(3e)`.
  have h3ea : 3 * e ≤ a := by omega
  have hsplit : p ^ a = p ^ (3 * e) * p ^ (a - 3 * e) := by
    rw [← pow_add]; congr 1; omega
  rw [hsplit] at hpa_prod
  have hp3e_pos : 0 < p ^ (3 * e) := pow_pos (hp.pos) _
  have hpa3e_mul : p ^ (a - 3 * e) ∣ u * (v + u ^ 2) :=
    (Nat.mul_dvd_mul_iff_left hp3e_pos).mp hpa_prod
  -- `u` is coprime to `p^(a - 3e)`.
  have hcop : Nat.Coprime p u := by
    rw [hu']
    exact coprime_p_normalized_r hr he
  have hcop' : Nat.Coprime (p ^ (a - 3 * e)) u :=
    Nat.Coprime.pow_left _ hcop
  -- Cancel `u`.
  have hfinal : p ^ (a - 3 * e) ∣ v + u ^ 2 :=
    dvd_of_dvd_mul_of_coprime hcop' hpa3e_mul
  -- Rewrite back to the original form.
  simpa [e, a, hu', hv'] using hfinal

/-- Application to the original binomial equation: from
`A.choose k = X + k^2` and `r = min k (A - k)`, the normalized congruence holds. -/
theorem original_normalized_square_congruence {p A k X : ℕ} [Fact p.Prime]
    (hk : k ≤ A) (hX : X ≠ 0) (hr : min k (A - k) ≠ 0)
    (heq : A.choose k = X + k ^ 2)
    (hlow : 3 * padicValNat p (min k (A - k)) < padicValNat p A) :
    p ^ (padicValNat p A - 3 * padicValNat p (min k (A - k))) ∣
      X / p ^ (2 * padicValNat p (min k (A - k))) +
        (min k (A - k) / p ^ padicValNat p (min k (A - k))) ^ 2 :=
  normalized_square_congruence hX hr
    (original_cubic_divisibility A k X hk heq) hlow

#print axioms coprime_p_normalized_r
#print axioms normalized_square_congruence
#print axioms original_normalized_square_congruence

end NestedBinomialV10
