; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Int)
(declare-fun alpha () Int)
(declare-fun rho () Int)
(declare-fun beta () Int)
(declare-fun chi () Int)
(declare-fun lambda () Int)
(assert
 (>= c 0))
(assert
 (>= alpha 0))
(assert
 (>= rho 0))
(assert
 (>= beta 0))
(assert
 (>= chi 0))
(assert
 (>= lambda 0))
(assert
 (>= alpha c))
(assert
 (let ((?x20 (* 2 c)))
 (>= chi ?x20)))
(assert
 (let ((?x22 (+ rho lambda)))
 (<= alpha ?x22)))
(assert
 (let (($x25 (= beta rho)))
 (let (($x24 (> alpha rho)))
 (=> $x24 $x25))))
(assert
 (let (($x35 (<= chi lambda)))
 (let ((?x27 (* 2 beta)))
 (let (($x34 (= chi ?x27)))
 (let (($x36 (and $x34 $x35)))
 (let (($x32 (<= lambda chi)))
 (let (($x31 (= lambda ?x27)))
 (let (($x33 (and $x31 $x32)))
 (let (($x29 (<= lambda ?x27)))
 (let (($x28 (= lambda chi)))
 (let (($x30 (and $x28 $x29)))
 (or $x30 $x33 $x36))))))))))))
(assert
 (let ((?x39 (* 3 rho)))
(> c ?x39)))
(check-sat)
