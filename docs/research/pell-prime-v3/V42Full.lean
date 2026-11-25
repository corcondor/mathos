import V4Radical
import V41Finish

namespace PellEquationV4
open PellPrimeV4 PellFinishV4

theorem prime_power_ne_twice (p t s : ℕ) (hp : p.Prime) (ht : t.Prime)
    (hs : 3≤s) : t^s≠2*p := by
  intro h
  have htd : t∣2*p := by
    refine ⟨t^(s-1),?_⟩
    rw [←h]
    calc
      t^s = t^((s-1)+1) := congrArg (fun n : ℕ => t^n) (by omega)
      _ = t*t^(s-1) := by rw [pow_succ]; ring
  have ht2 : t=2 := by
    rcases ht.dvd_mul.mp htd with h2|hp'
    · exact (Nat.prime_dvd_prime_iff_eq ht Nat.prime_two).mp h2
    · have htp := (Nat.prime_dvd_prime_iff_eq ht hp).mp hp'
      subst t
      have hsplit : p^s=p*(p*p^(s-2)) := by
        calc
          p^s = p^((s-2)+2) := congrArg (fun n : ℕ => p^n) (by omega)
          _ = _ := by rw [pow_add]; ring
      have hmul : p*(p*p^(s-2))=p*2 := by rw [←hsplit,h]; ring
      have hh := Nat.eq_of_mul_eq_mul_left hp.pos hmul
      have hdp : p∣2 := ⟨p^(s-2),hh.symm⟩
      exact (Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp hdp
  subst t
  have hEq : 2^(s-1)=p := by
    rw [show s=(s-1)+1 by omega,pow_succ] at h
    omega
  have hdiv : 2 ∣ p := by
    refine ⟨2^(s-2),?_⟩
    rw [←hEq]
    calc
      2^(s-1) = 2^((s-2)+1) := congrArg (fun n : ℕ => 2^n) (by omega)
      _ = 2*2^(s-2) := by rw [pow_succ]; ring
  have hp2 : 2=p := (Nat.prime_dvd_prime_iff_eq Nat.prime_two hp).mp hdiv
  have hge : (4:ℕ) ≤ 2^(s-1) := by
    calc
      4=2^2 := rfl
      _ ≤ 2^(s-1) := by gcongr <;> omega
  omega

-- Real signed odd roots; even roots are nonnegative, as in the original problem.
def Equation (p q r s t : ℕ) : Prop :=
  ∃ a b : ℝ,
    a^s=(p:ℝ)+(q:ℝ)*Real.sqrt (r:ℝ) ∧
    b^s=(p:ℝ)-(q:ℝ)*Real.sqrt (r:ℝ) ∧
    a+b=(t:ℝ) ∧ (Even s → 0≤a ∧ 0≤b)

theorem product_power (p q r s : ℕ) (a b : ℝ)
    (ha : a^s=(p:ℝ)+(q:ℝ)*Real.sqrt (r:ℝ))
    (hb : b^s=(p:ℝ)-(q:ℝ)*Real.sqrt (r:ℝ)) :
    (a*b)^s=(((p:ℤ)^2-(q:ℤ)^2*(r:ℤ)):ℝ) := by
  rw [mul_pow,ha,hb]
  push_cast
  calc
    _ = (p:ℝ)^2-(q:ℝ)^2*(Real.sqrt (r:ℝ))^2 := by ring
    _ = _ := by rw [Real.sq_sqrt (by positivity)]

theorem no_square_case (p q r t : ℕ)
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (ht : t.Prime) :
    ¬ Equation p q r 2 t := by
  rintro ⟨a,b,ha,hb,hadd,hn⟩
  obtain ⟨han,hbn⟩ := hn (by decide)
  have hs : a^2+b^2=2*(p:ℝ) := by rw [ha,hb]; ring
  let u : ℚ := ((t:ℚ)^2-2*(p:ℚ))/2
  have hu : (u:ℝ)=a*b := by
    dsimp [u]
    push_cast
    have hsq := congrArg (fun x : ℝ => x^2) hadd
    nlinarith
  let C : ℤ := (p:ℤ)^2-(q:ℤ)^2*(r:ℤ)
  have hpow : (a*b)^2=(C:ℝ) := by
    dsimp [C]
    push_cast
    exact product_power p q r 2 a b ha hb
  have hu2R : (u:ℝ)^2=(C:ℝ) := hu ▸ hpow
  have hu2 : u^2=(C:ℚ) := by exact_mod_cast hu2R
  have hint : IsIntegral ℤ (u^2) := by rw [hu2]; exact isIntegral_algebraMap
  obtain ⟨z,hz⟩ := IsIntegrallyClosed.exists_algebraMap_eq_of_isIntegral_pow (by decide : 0<2) hint
  have hzQ : (z:ℚ)=u := hz
  have hzR : (z:ℝ)=a*b := (by exact_mod_cast hzQ : (z:ℝ)=(u:ℝ)).trans hu
  have htzR : (t:ℝ)^2=2*(p:ℝ)+2*(z:ℝ) := by
    have hsq := congrArg (fun x : ℝ => x^2) hadd
    nlinarith
  have htz : (t:ℤ)^2=2*(p:ℤ)+2*z := by exact_mod_cast htzR
  have hdivZ : (2:ℤ)∣(t:ℤ)^2 := ⟨(p:ℤ)+z,by linarith⟩
  have hdiv : 2∣t^2 := by exact_mod_cast hdivZ
  have ht2 : t=2 := ((Nat.prime_dvd_prime_iff_eq Nat.prime_two ht).mp
    (Nat.prime_two.dvd_of_dvd_pow hdiv)).symm
  have hznon : 0≤(z:ℝ) := hzR ▸ mul_nonneg han hbn
  have hpr : (2:ℝ)≤(p:ℝ) := by exact_mod_cast hp.two_le
  rw [ht2] at htzR
  norm_num at htzR
  have hp2R : (p:ℝ)=2 := by linarith
  have hp2 : p=2 := by exact_mod_cast hp2R
  have hz0 : (z:ℝ)=0 := by linarith
  have hzero : a*b=0 := hzR.symm.trans hz0
  rw [hzero] at hpow
  norm_num [C,hp2] at hpow
  have hlow : 8≤q^2*r := by
    have hq2 : 4≤q^2 := by simpa using Nat.pow_le_pow_left hq.two_le 2
    calc 8=4*2 := rfl
         _≤q^2*r := Nat.mul_le_mul hq2 hr.two_le
  have hqR : (8:ℝ)≤(q:ℝ)^2*(r:ℝ) := by exact_mod_cast hlow
  push_cast at hpow
  nlinarith

theorem odd_case (p q r s t : ℕ) (hp : p.Prime) (hq : q.Prime)
    (hr : r.Prime) (hs : s.Prime) (ht : t.Prime) (ho : Odd s)
    (he : Equation p q r s t) :
    t=2 ∧ r=2 ∧ (coefs 2 s).1=p ∧ (coefs 2 s).2=q := by
  obtain ⟨a,b,ha,hb,hadd,_⟩ := he
  have hs3 : 3≤s := by
    have h2 := hs.two_le
    obtain ⟨k,hk⟩ := ho
    omega
  have hpow : a^s+b^s=2*(p:ℝ) := by rw [ha,hb]; ring
  have hprod := product_power p q r s a b ha hb
  have htQ : a+b=((t:ℚ):ℝ) := by exact_mod_cast hadd
  have hvQ : a^s+b^s=(((2:ℚ)*(p:ℚ)):ℝ) := by push_cast; exact hpow
  have hne : (t:ℚ)^s≠2*(p:ℚ) := by
    exact_mod_cast prime_power_ne_twice p t s hp ht hs3
  obtain ⟨z,hz⟩ := radical_product_integral a b s hs ho (t:ℚ) (2*(p:ℚ))
    ((p:ℤ)^2-(q:ℤ)^2*(r:ℤ)) htQ (by push_cast; exact hpow) (by push_cast; exact hprod) hne
  have ht2 := odd_sum_prime_eq_two p t s hp ht hs3 ho a b z hadd hz hpow
  have hdiff : b<a := by
    apply ho.pow_lt_pow.mp
    rw [ha,hb]
    have hh : 0<(q:ℝ)*Real.sqrt (r:ℝ) := mul_pos (by exact_mod_cast hq.pos)
      (Real.sqrt_pos.2 (by exact_mod_cast hr.pos))
    linarith
  let d := (a-b)/2
  have hdpos : 0<d := by dsimp [d]; linarith
  have hadd2 : a+b=2 := by simpa [ht2] using hadd
  have hdZ : d^2=((1-z:ℤ):ℝ) := by
    calc
      d^2=((a+b)/2)^2-a*b := by dsimp [d]; ring
      _ = _ := by rw [hadd2,hz]; push_cast; ring
  have hZposR : (0:ℝ)<((1-z:ℤ):ℝ) := by rw [←hdZ]; positivity
  have hZpos : (0:ℤ)<1-z := by exact_mod_cast hZposR
  let D : ℕ := (1-z).toNat
  have hDc : (D:ℤ)=1-z := Int.toNat_of_nonneg hZpos.le
  have hDp : 1≤D := by omega
  have hdD : d^2=(D:ℝ) := by rw [hdZ,←hDc]; push_cast; rfl
  have ha1 : a=1+d := by dsimp [d]; linarith
  have hb1 : b=1-d := by dsimp [d]; linarith
  obtain ⟨h1,h2⟩ := coefs_expand D d hdD s
  rw [←ha1,ha] at h1
  rw [←hb1,hb] at h2
  have hP : (coefs D s).1=p := by
    have hPR : ((coefs D s).1:ℝ)=p := by linarith
    exact_mod_cast hPR
  have hB : ((coefs D s).2:ℝ)*d=(q:ℝ)*Real.sqrt (r:ℝ) := by linarith
  have hQ_R := congrArg (fun x : ℝ => x^2) hB
  simp only [mul_pow,hdD,Real.sq_sqrt (by positivity : 0≤(r:ℝ))] at hQ_R
  have hQ : (coefs D s).2^2*D=q^2*r := by exact_mod_cast hQ_R
  obtain ⟨_,hr2,hP2,hQ2⟩ := coefs_prime_force_two D p q r s hp hq hr hDp hs3 hP hQ
  exact ⟨ht2,hr2,hP2,hQ2⟩

theorem radical_iff_pell_coeffs (p q r s t : ℕ)
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime) :
    Equation p q r s t ↔
      s≠2 ∧ t=2 ∧ r=2 ∧ (coefs 2 s).1=p ∧ (coefs 2 s).2=q := by
  constructor
  · intro he
    rcases hs.eq_two_or_odd' with rfl|ho
    · exact False.elim (no_square_case p q r t hp hq hr ht he)
    · have hn : s≠2 := by intro h; rw [h] at ho; exact (by decide : ¬Odd (2:ℕ)) ho
      exact ⟨hn,odd_case p q r s t hp hq hr hs ht ho he⟩
  · rintro ⟨hn,rfl,rfl,hp',hq'⟩
    have ho : Odd s := hs.eq_two_or_odd'.resolve_left hn
    let d := Real.sqrt (2:ℝ)
    have hd : d^2=(2:ℝ) := Real.sq_sqrt (by norm_num)
    obtain ⟨h1,h2⟩ := coefs_expand 2 d (by simpa using hd) s
    rw [hp',hq'] at h1 h2
    refine ⟨1+d,1-d,?_,?_,by ring,?_⟩
    · simpa [d] using h1
    · simpa [d] using h2
    · intro hev
      obtain ⟨k,hk⟩ := ho
      obtain ⟨l,hl⟩ := hev
      omega

#print axioms prime_power_ne_twice
#print axioms no_square_case
#print axioms odd_case
#print axioms radical_iff_pell_coeffs
end PellEquationV4
