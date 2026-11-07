import Mathlib.Tactic
import Mathlib.AlgebraicGeometry.EllipticCurve.Weierstrass
def Xcoord (c r y : ℚ) : ℚ := -c * r / y
def Zcoord (c y : ℚ) : ℚ := c / y
def invY (c z : ℚ) : ℚ := c / z
def invR (_c x z : ℚ) : ℚ := -x / z
def mordellModel (c : ℚ) : WeierstrassCurve ℚ := ⟨0, 0, 0, 0, c ^ 2⟩

namespace NestedBinomialV10
theorem forward_map_equation (c r y : ℚ) (hy : y ≠ 0) (hc : c ≠ 0) (h : y ^ 3 - y = c * r ^ 3) : (Zcoord c y) ^ 2 = (Xcoord c r y) ^ 3 + c ^ 2 := by
  unfold Xcoord Zcoord
  field_simp
  nlinarith [h]

theorem inverse_map_equation (c x z : ℚ) (hz : z ≠ 0) (hc : c ≠ 0) (h : z ^ 2 = x ^ 3 + c ^ 2) : (invY c z) ^ 3 - invY c z = c * (invR c x z) ^ 3 := by
  unfold invY invR
  field_simp
  nlinarith [h]

theorem inv_forward_pair (c r y : ℚ) (hy : y ≠ 0) (hc : c ≠ 0) : invY c (Zcoord c y) = y ∧ invR c (Xcoord c r y) (Zcoord c y) = r := by
  constructor
  · unfold invY Zcoord
    field_simp
  · unfold invR Xcoord Zcoord
    field_simp

theorem forward_inv_pair (c x z : ℚ) (hz : z ≠ 0) (hc : c ≠ 0) : Xcoord c (invR c x z) (invY c z) = x ∧ Zcoord c (invY c z) = z := by
  constructor
  · unfold Xcoord invR invY
    field_simp
  · unfold Zcoord invY
    field_simp

theorem mordellModel_delta (c : ℚ) : (mordellModel c).Δ = -432 * c ^ 4 := by
  unfold mordellModel WeierstrassCurve.Δ WeierstrassCurve.b₂ WeierstrassCurve.b₄ WeierstrassCurve.b₆ WeierstrassCurve.b₈
  ring

theorem mordellModel_delta_ne_zero (c : ℚ) (hc : c ≠ 0) : (mordellModel c).Δ ≠ 0 := by
  rw [mordellModel_delta]
  intro h
  apply hc
  have h4 : c ^ 4 = 0 := by
    have := h
    linarith
  exact pow_eq_zero_iff (by norm_num : (4:ℕ) ≠ 0) |>.mp h4

theorem mordellModel_isElliptic (c : ℚ) (hc : c ≠ 0) : (mordellModel c).IsElliptic := by
  rw [WeierstrassCurve.isElliptic_iff]
  exact IsUnit.mk0 _ (NestedBinomialV10.mordellModel_delta_ne_zero c hc)

theorem mordellModel_j_zero (c : ℚ) [(mordellModel c).IsElliptic] : (mordellModel c).j = 0 := by
  have hc4 : (mordellModel c).c₄ = 0 := by
    unfold mordellModel WeierstrassCurve.c₄ WeierstrassCurve.b₂ WeierstrassCurve.b₄
    ring
  exact WeierstrassCurve.j_eq_zero (W := mordellModel c) hc4

theorem research_curve_forward (S T r y : ℚ) (hS : S ≠ 0) (hT : T ≠ 0) (hy : y ≠ 0) (h : 6 * S * r ^ 3 = T * (y ^ 3 - y)) : (Zcoord (6 * S / T) y) ^ 2 = (Xcoord (6 * S / T) r y) ^ 3 + (6 * S / T) ^ 2 := by
  have hc : (6 * S / T) ≠ 0 := by
    intro hc0
    rw [div_eq_zero_iff] at hc0
    rcases hc0 with h6 | hT0
    · have h6S : 6 * S = 0 := by
        rcases mul_eq_zero.mp h6 with h6' | hS'
        · norm_num at h6'
        · rw [hS', mul_zero]
      have hS0 : S = 0 := by linarith
      exact hS hS0
    · exact hT hT0
  have hcubic : y ^ 3 - y = (6 * S / T) * r ^ 3 := by
    field_simp
    linarith [h]
  exact NestedBinomialV10.forward_map_equation (6 * S / T) r y hy hc hcubic

#print axioms forward_map_equation
#print axioms inverse_map_equation
#print axioms inv_forward_pair
#print axioms forward_inv_pair
#print axioms mordellModel_delta
#print axioms mordellModel_delta_ne_zero
#print axioms mordellModel_isElliptic
#print axioms mordellModel_j_zero
#print axioms research_curve_forward

end NestedBinomialV10
