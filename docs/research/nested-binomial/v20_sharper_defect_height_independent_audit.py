#!/usr/bin/env python3
"""Separate audit of the root-authored upper-gap proof; imports no producer."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--note",type=Path,
                   default=Path(__file__).with_name("v20_sharper_defect_height.md"))
    p.add_argument("--output",type=Path,
                   default=Path(__file__).with_suffix(".json"))
    args=p.parse_args()
    N0=2**256
    n,L,x,l2,l3,ell,logden,alpha=sp.symbols("n L x l2 l3 ell logden alpha")
    # ell is log(3+x); logden is log(4*e*b). All log symbols are formal.
    f3x=(3+x)*(1-l2-l3-ell)
    f3=3*(1-l2-2*l3)
    direct=(3+x)*n*(1+2*L-l2-l3-ell)-4*(3+x)-logden-6*n*(1+L-l2-l3)
    proposed=n*(3*l2-sp.Rational(103,50)+f3x-f3)-4*(3+x)-logden
    assert sp.expand(direct-proposed-n*(2*x*L-sp.Rational(47,50)))==0
    identity=sp.cancel(L*((3+alpha/L)**2*n/(n-1)-9)
                       -((6*alpha+alpha**2/L)*n+9*L)/(n-1))
    assert identity==0
    A=n*(n-1)*(n-2)/6
    assert sp.expand(7*A-n**3-n*(n*n-21*n+14)/6)==0
    margins={
        "L_gt_100":F(256*56,81)-100,
        "x_lt_one_percent":F(1,100)-F(3807,1433600),
        "bracket_gt_one_twohundredth":F(19,1350)-F(11421,1433600)-F(1,200),
        "log_6y_less_than_3":F(8,3)**3-6*F(301,100),
        "log48_less_than4":F(8,3)**4-48,
        "four_3_plus_x_less_than13":13-4*F(301,100),
        "A_gt_16n_squared_threshold":N0-112,
        "ceil_bound_b_less_than_4n":F(99,100)*N0-1,
        "binomial_ratio_threshold":F(N0,200)-197,
        "upper_log_gap_threshold_monotonicity":F(1,200)-F(1,N0),
        "alpha_squared_over_L_lt_one_fourhundredth":F(1,400)-F(47,100)**2/F(100),
        "nine_L_less_than_n_over_1000":N0-9000*180,
        "n_over_nminus1_lt_1001_over_1000":F(1001,1000)-F(N0,N0-1),
        "defect_constant_margin":17-6*(F(141,50)+F(1,400)+F(1,1000))*F(1001,1000),
        "low_n_range_covered_by_delta_ge_25":425-F(896,5),
        "25_log2_greater_than17":F(1400,81)-17,
    }
    assert all(v>0 for v in margins.values())
    assert 6*(F(141,50)+F(1,400)+F(1,1000))*F(1001,1000)==F(16957941,1000000)
    assert 3*F(56,81)-F(103,50)==F(19,1350)
    assert F(47,100)/(F(256*56,81))==F(3807,1433600)
    result={
        "status":"PASS_INDEPENDENT_WRITTEN_AND_SYMBOLIC_AUDIT",
        "note_sha256":sha256(args.note.read_bytes()).hexdigest(),
        "reviewer_script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version":sp.__version__,
        "producer_imported":False,
        "symbolic_identities":3,
        "positive_rational_margins":{k:str(v) for k,v in margins.items()},
        "written_checks":[
            "Upper and lower factorial integral bounds have the correct directions",
            "Product lower bound uses b^2<A and b<A",
            "Numerator monotonicity keeps the denominator 2*e*b fixed",
            "A logarithmic lower bound is uniform for n>=12",
            "The log-ratio brace and both logarithmic constants are correct",
            "r<ceil(a) implies r<a for every real a because r is an integer",
            "The intrinsic-defect inequality uses K-9C>=1 without a gcd cancellation",
            "The n/(n-1) correction and +9*log(n) term are retained",
            "The low-n case is covered by inherited delta>=25 without circular use of the new bound",
            "No n scan up to 2^256 is required"
        ],
        "blocking_findings":[],
        "limits":"Written/internal AI review with exact symbolic and rational checks; no Lean or external human peer review. Inherited delta>=25 and B<L<2B are taken from the recorded previous results."
    }
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","note_sha256","symbolic_identities","blocking_findings"]},indent=2))


if __name__=="__main__":
    main()
