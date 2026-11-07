#!/usr/bin/env python3
"""Exact supporting checks for the two written v20 problem solutions."""
from pathlib import Path
from math import gcd
import hashlib
import json
import sympy as sp

for t in range(-2000, 2001):
    assert gcd(t**3, t*t+3*t+3) == gcd(t, 3)
x, a, b, d = sp.symbols('x a b d')
P = a*x*x-b*x-d
numerator = sp.expand(2*x*(x-1)*sp.diff(P,x)-(2*x-1)*P)
assert sp.expand(numerator-(a*x*x*(2*x-3)+b*x+d*(2*x-1))) == 0
note = Path(__file__).with_name('v20_problem_seeds_ja.md')
result = {
  'status':'PASS',
  'gcd_support_samples':4001,
  'samples_are_not_universal_proof':True,
  'derivative_polynomial_identity_verified':True,
  'written_universal_proofs':'Prime valuations; monotonicity for x>=2',
  'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'new_Lean_execution':False,
  'originality_search_performed':False,
}
Path(__file__).with_name('v20_problem_seeds_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
