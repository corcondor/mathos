import Mathlib.Tactic
import Mathlib.AlgebraicGeometry.EllipticCurve.Weierstrass
import GeometricReduction
def iso3X (c x : ℚ) : ℚ := (x ^ 3 + 4 * c ^ 2) / x ^ 2
def iso3Y (c x z : ℚ) : ℚ := z * (x ^ 3 - 8 * c ^ 2) / x ^ 3
def mordellModel3 (c : ℚ) : WeierstrassCurve ℚ := ⟨0, 0, 0, 0, -27 * c ^ 2⟩

namespace NestedBinomialV10
theorem mordellModel3_delta (c : ℚ) : (mordellModel3 c).Δ = -314928 * c ^ 4 := by
  unfold mordellModel3 WeierstrassCurve.Δ WeierstrassCurve.b₂ WeierstrassCurve.b₄ WeierstrassCurve.b₆ WeierstrassCurve.b₈
  ring

theorem mordellModel3_delta_ne_zero (c : ℚ) (hc : c ≠ 0) : (mordellModel3 c).Δ ≠ 0 := by
  rw [NestedBinomialV10.mordellModel3_delta]
  intro h
  apply hc
  have h4 : c ^ 4 = 0 := by
    exact (mul_eq_zero.mp h).resolve_left (by norm_num : (-314928 : ℚ) ≠ 0)
  exact (pow_eq_zero_iff (by norm_num : (4 : ℕ) ≠ 0)).mp h4

theorem iso3_image_equation (c x z : ℚ) (hc : c ≠ 0) (hx : x ≠ 0) (h : z ^ 2 = x ^ 3 + c ^ 2) : (iso3Y c x z) ^ 2 = (iso3X c x) ^ 3 - 27 * c ^ 2 := by
  unfold iso3X iso3Y
  have hx2 : x ^ 2 ≠ 0 := pow_ne_zero 2 hx
  have hx3 : x ^ 3 ≠ 0 := pow_ne_zero 3 hx
  have hc2 : c ^ 2 ≠ 0 := pow_ne_zero 2 hc
  field_simp [hx, hx2, hx3, hc2]
  rw [h]
  ring

theorem branch_image_coords (c r y : ℚ) (hc : c ≠ 0) (hr : r ≠ 0) (hy : y ≠ 0) (h : y ^ 3 - y = c * r ^ 3) : iso3X c (Xcoord c r y) = (3 * y ^ 2 + 1) / r ^ 2 ∧ iso3Y c (Xcoord c r y) (Zcoord c y) = (9 * y ^ 2 - 1) / r ^ 3 := by
  have hc2 : c ^ 2 ≠ 0 := pow_ne_zero 2 hc
  have hy2 : y ^ 2 ≠ 0 := pow_ne_zero 2 hy
  have hy3 : y ^ 3 ≠ 0 := pow_ne_zero 3 hy
  have hr2 : r ^ 2 ≠ 0 := pow_ne_zero 2 hr
  have hr3 : r ^ 3 ≠ 0 := pow_ne_zero 3 hr
  have hneg : -c ≠ 0 := by
    intro hc0
    apply hc
    linarith
  have hx : -c * r / y ≠ 0 := by
    exact div_ne_zero (mul_ne_zero hneg hr) hy
  have hx2 : (-c * r / y) ^ 2 ≠ 0 := pow_ne_zero 2 hx
  have hx3 : (-c * r / y) ^ 3 ≠ 0 := pow_ne_zero 3 hx
  have hX : iso3X c (Xcoord c r y) = (4 * y ^ 3 - c * r ^ 3) / (y * r ^ 2) := by
    unfold iso3X Xcoord
    field_simp [hx, hx2, hx3, hc, hr, hy, hc2, hy2, hy3, hr2, hr3]
    ring
  have hY : iso3Y c (Xcoord c r y) (Zcoord c y) = (c * r ^ 3 + 8 * y ^ 3) / (y * r ^ 3) := by
    unfold iso3Y Xcoord Zcoord
    field_simp [hx, hx2, hx3, hc, hr, hy, hc2, hy2, hy3, hr2, hr3]
    ring
  have hcr : c * r ^ 3 = y ^ 3 - y := by
    linarith [h]
  constructor
  · rw [hX, hcr]
    have hyr2 : y * r ^ 2 ≠ 0 := mul_ne_zero hy hr2
    field_simp [hy, hr, hr2, hyr2]
    ring
  · rw [hY, hcr]
    have hyr3 : y * r ^ 3 ≠ 0 := mul_ne_zero hy hr3
    field_simp [hy, hr, hr3, hyr3]
    ring

theorem branch_pell_relation (c r y : ℚ) (hc : c ≠ 0) (hr : r ≠ 0) (hy : y ≠ 0) (h : y ^ 3 - y = c * r ^ 3) : iso3X c (Xcoord c r y) * r ^ 2 = 3 * y ^ 2 + 1 := by
  have hX := (NestedBinomialV10.branch_image_coords c r y hc hr hy h).1
  rw [hX]
  have hr2 : r ^ 2 ≠ 0 := pow_ne_zero 2 hr
  field_simp [hr2]

theorem branch_r_sq_relation (c r y : ℚ) (hc : c ≠ 0) (hr : r ≠ 0) (hy : y ≠ 0) (h : y ^ 3 - y = c * r ^ 3) : r ^ 2 * (3 * iso3X c (Xcoord c r y) - iso3Y c (Xcoord c r y) (Zcoord c y) * r) = 4 := by
  obtain ⟨hX, hY⟩ := NestedBinomialV10.branch_image_coords c r y hc hr hy h
  rw [hX, hY]
  have hr2 : r ^ 2 ≠ 0 := pow_ne_zero 2 hr
  have hr3 : r ^ 3 ≠ 0 := pow_ne_zero 3 hr
  field_simp [hr, hr2, hr3]
  ring

#print axioms mordellModel3_delta
#print axioms mordellModel3_delta_ne_zero
#print axioms iso3_image_equation
#print axioms branch_image_coords
#print axioms branch_pell_relation
#print axioms branch_r_sq_relation

end NestedBinomialV10
