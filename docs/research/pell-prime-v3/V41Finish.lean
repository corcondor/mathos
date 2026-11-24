import Mathlib
namespace PellFinishV4

-- Positive centered expansion, applicable even when the second root is negative.
def centered (c d : ℝ) : ℕ → ℝ × ℝ
  | 0 => (1,0)
  | n+1 => (c*(centered c d n).1+d*(centered c d n).2,
             d*(centered c d n).1+c*(centered c d n).2)

theorem centered_exp (c d : ℝ) (n : ℕ) :
    (c+d)^n = (centered c d n).1+(centered c d n).2 ∧
    (c-d)^n = (centered c d n).1-(centered c d n).2 := by
  induction n with
  | zero => simp [centered]
  | succ n ih =>
    simp only [centered,pow_succ]
    constructor
    · rw [ih.1]; ring
    · rw [ih.2]; ring

theorem centered_bound (c d : ℝ) (hc : 0≤c) (hd : 0≤d) (n : ℕ) :
    c^n ≤ (centered c d n).1 ∧ 0≤(centered c d n).2 := by
  induction n with
  | zero => simp [centered]
  | succ n ih =>
    have ha : 0≤(centered c d n).1 := (pow_nonneg hc _).trans ih.1
    have h1 := mul_le_mul_of_nonneg_left ih.1 hc
    have h2 := mul_nonneg hd ih.2
    have h3 := mul_nonneg hd ha
    have h4 := mul_nonneg hc ih.2
    simp only [centered,pow_succ]
    constructor <;> nlinarith

theorem sum_power_lower (a b : ℝ) (h : 0≤a+b) (n : ℕ) :
    2*((a+b)/2)^n ≤ a^n+b^n := by
  let c := (a+b)/2
  let d := |a-b|/2
  have hc : 0≤c := by dsimp [c]; linarith
  have hd : 0≤d := by dsimp [d]; positivity
  have h0 := centered_bound c d hc hd n
  have h1 := centered_exp c d n
  have h2 : a^n+b^n=(c+d)^n+(c-d)^n := by
    by_cases hab : b≤a
    · have h3 : c+d=a := by dsimp [c,d]; rw [abs_of_nonneg (by linarith)]; ring
      have h4 : c-d=b := by dsimp [c,d]; rw [abs_of_nonneg (by linarith)]; ring
      rw [h3,h4]
    · have h3 : c+d=b := by dsimp [c,d]; rw [abs_of_nonpos (by linarith)]; ring
      have h4 : c-d=a := by dsimp [c,d]; rw [abs_of_nonpos (by linarith)]; ring
      rw [h3,h4]; ring
  change 2*c^n≤a^n+b^n
  rw [h2,h1.1,h1.2]
  linarith [h0.1]

def intSum (T U : ℤ) : ℕ → ℤ
  | 0 => 2
  | 1 => T
  | n+2 => T*intSum T U (n+1)-U*intSum T U n

theorem intSum_eval (T U : ℤ) (a b : ℝ) (ht : a+b=(T:ℝ)) (hu : a*b=(U:ℝ))
    (n : ℕ) : (intSum T U n:ℝ)=a^n+b^n := by
  match n with
  | 0 => norm_num [intSum]
  | 1 => simpa [intSum] using ht.symm
  | n+2 =>
    simp only [intSum,Int.cast_sub,Int.cast_mul]
    rw [intSum_eval T U a b ht hu (n+1),intSum_eval T U a b ht hu n,←ht,←hu]
    simp only [pow_succ]
    ring
termination_by n

theorem intSum_odd_dvd (T U : ℤ) (k : ℕ) : T ∣ intSum T U (2*k+1) := by
  induction k with
  | zero => simp [intSum]
  | succ k ih =>
    rw [show 2*(k+1)+1=(2*k+1)+2 by omega,intSum]
    obtain ⟨v,hv⟩ := ih
    refine ⟨intSum T U ((2*k+1)+1)-U*v,?_⟩
    rw [hv]
    ring

theorem odd_sum_prime_eq_two (p t s : ℕ) (hp : p.Prime) (ht : t.Prime)
    (hs : 3≤s) (ho : Odd s) (a b : ℝ) (z : ℤ)
    (hadd : a+b=(t:ℝ)) (hmul : a*b=(z:ℝ)) (hpow : a^s+b^s=2*(p:ℝ)) :
    t=2 := by
  have hsum := intSum_eval (t:ℤ) z a b (by exact_mod_cast hadd) hmul s
  have hsumZ : intSum (t:ℤ) z s = 2*(p:ℤ) := by
    rw [hpow] at hsum
    exact_mod_cast hsum
  obtain ⟨k,hk⟩ := ho
  have hk' : s=2*k+1 := by omega
  have hdiv := intSum_odd_dvd (t:ℤ) z k
  rw [←hk',hsumZ] at hdiv
  have hdivN : t∣2*p := by exact_mod_cast hdiv
  rcases ht.dvd_mul.mp hdivN with h2|hp'
  · exact (Nat.prime_dvd_prime_iff_eq ht Nat.prime_two).mp h2
  · have htp : t=p := (Nat.prime_dvd_prime_iff_eq ht hp).mp hp'
    by_contra ht2
    have ht3 : 3≤t := by have := ht.two_le; omega
    have htR : (3:ℝ)≤(t:ℝ) := by exact_mod_cast ht3
    have h := sum_power_lower a b (by rw [hadd]; positivity) s
    rw [hadd,hpow,←htp] at h
    have hbase : 1≤(t:ℝ)/2 := by linarith
    have hpow3 : ((t:ℝ)/2)^3 ≤ ((t:ℝ)/2)^s := by
      exact pow_le_pow_right₀ hbase hs
    have ht_sq : (9:ℝ)≤(t:ℝ)^2 := by
      have := mul_nonneg (show 0≤(t:ℝ)-3 by linarith) (show 0≤(t:ℝ)+3 by linarith)
      nlinarith
    have hmul' := mul_nonneg (show 0≤(t:ℝ)^2-9 by linarith) (show 0≤(t:ℝ) by linarith)
    nlinarith

-- With D positive, the two binomial coefficient sequences are natural numbers.
def coefs (D : ℕ) : ℕ → ℕ × ℕ
  | 0 => (1,0)
  | n+1 => ((coefs D n).1+D*(coefs D n).2,(coefs D n).1+(coefs D n).2)

theorem coefs_bounds (D : ℕ) (hD : 1≤D) (n : ℕ) :
    1≤(coefs D n).1 ∧ n≤(coefs D n).1 ∧ n≤(coefs D n).2 := by
  induction n with
  | zero => simp [coefs]
  | succ n ih =>
    have hh : (coefs D n).2 ≤ D*(coefs D n).2 := by
      simpa using Nat.mul_le_mul_right (coefs D n).2 hD
    simp only [coefs]
    omega

theorem coefs_even (D : ℕ) (hD : D%2=1) (n : ℕ) :
    (coefs D (n+2)).1%2=0 ∧ (coefs D (n+2)).2%2=0 := by
  induction n with
  | zero =>
    simp [coefs]
    omega
  | succ n ih =>
    change ((coefs D (n+2)).1+D*(coefs D (n+2)).2)%2=0 ∧
      ((coefs D (n+2)).1+(coefs D (n+2)).2)%2=0
    rcases ih with ⟨ha,hb⟩
    constructor
    · rw [Nat.add_mod,Nat.mul_mod,ha,hb]; simp
    · rw [Nat.add_mod,ha,hb]; simp

theorem coefs_expand (D : ℕ) (d : ℝ) (hd : d^2=(D:ℝ)) (n : ℕ) :
    (1+d)^n=(coefs D n).1+(coefs D n).2*d ∧
    (1-d)^n=(coefs D n).1-(coefs D n).2*d := by
  induction n with
  | zero => norm_num [coefs]
  | succ n ih =>
    simp only [coefs,pow_succ,Nat.cast_add,Nat.cast_mul]
    constructor
    · rw [ih.1]
      calc
        _ = (coefs D n).1+(coefs D n).2*d^2+((coefs D n).1+(coefs D n).2)*d := by ring
        _ = _ := by rw [hd]; ring
    · rw [ih.2]
      calc
        _ = (coefs D n).1+(coefs D n).2*d^2-((coefs D n).1+(coefs D n).2)*d := by ring
        _ = _ := by rw [hd]; ring

-- No factorization library assumption: compare the prime factors of the two squares.
theorem square_factor_eq (q r B D : ℕ) (hq : q.Prime) (hr : r.Prime)
    (hB : 2≤B) (hD : 1≤D) (h : B^2*D=q^2*r) : B=q ∧ D=r := by
  obtain ⟨l,hl,hld⟩ := Nat.exists_prime_and_dvd (show B≠1 by omega)
  obtain ⟨k,hk⟩ := hld
  have hld' : l∣q^2*r := by
    refine ⟨l*k^2*D,?_⟩
    rw [←h,hk]
    ring
  have hlq : l=q := by
    rcases hl.dvd_mul.mp hld' with hq'|hr'
    · exact (Nat.prime_dvd_prime_iff_eq hl hq).mp (hl.dvd_of_dvd_pow hq')
    · have hlr : l=r := (Nat.prime_dvd_prime_iff_eq hl hr).mp hr'
      have hh : l*(l*k^2*D)=l*q^2 := by rw [←hlr] at h; rw [hk] at h; nlinarith
      have hh' := Nat.eq_of_mul_eq_mul_left hl.pos hh
      exact (Nat.prime_dvd_prime_iff_eq hl hq).mp
        (hl.dvd_of_dvd_pow (by exact ⟨k^2*D,by simpa [mul_assoc] using hh'.symm⟩))
  have hqk : B=q*k := by simpa [hlq] using hk
  have he : q^2*(k^2*D)=q^2*r := by rw [hqk] at h; nlinarith
  have he' : k^2*D=r := Nat.eq_of_mul_eq_mul_left (pow_pos hq.pos _) he
  have hkd : k∣r := ⟨k*D,by rw [←he']; ring⟩
  rcases (Nat.dvd_prime hr).mp hkd with hk1|hkr
  · subst k
    simp at he' hqk
    exact ⟨hqk,he'⟩
  · have hh : r*(r*D)=r*1 := by rw [hkr] at he'; nlinarith
    have hh' := Nat.eq_of_mul_eq_mul_left hr.pos hh
    have hr1 := (Nat.mul_eq_one.mp hh').1
    have := hr.two_le
    omega

theorem coefs_prime_force_two (D p q r s : ℕ) (hp : p.Prime) (hq : q.Prime)
    (hr : r.Prime) (hD : 1≤D) (hs : 3≤s)
    (hP : (coefs D s).1=p) (hQ : (coefs D s).2^2*D=q^2*r) :
    D=2 ∧ r=2 ∧ (coefs 2 s).1=p ∧ (coefs 2 s).2=q := by
  have hb := coefs_bounds D hD s
  obtain ⟨hB,hDr⟩ := square_factor_eq q r (coefs D s).2 D hq hr (by omega) hD hQ
  have hD2 : D=2 := by
    by_contra hne
    have hpr : D.Prime := hDr ▸ hr
    have hodd : D%2=1 := (hpr.eq_two_or_odd).resolve_left hne
    have hE := coefs_even D hodd (s-2)
    rw [show s-2+2=s by omega,hP] at hE
    have hdvd : 2∣p := Nat.dvd_of_mod_eq_zero hE.1
    have h2p := (Nat.prime_dvd_prime_iff_eq Nat.prime_two hp).mp hdvd
    omega
  subst D
  exact ⟨rfl,hDr.symm,hP,hB⟩

#print axioms sum_power_lower
#print axioms odd_sum_prime_eq_two
#print axioms coefs_expand
#print axioms square_factor_eq
#print axioms coefs_prime_force_two
end PellFinishV4
