"""Exact rational enclosures for the four entropy constants in the proof."""
from fractions import Fraction as Q
from pathlib import Path
import json

def log_interval(z, terms=128):
    assert z > 0
    u = (z - 1) / (z + 1)
    s = Q(0)
    v = u
    for n in range(terms):
        s += 2 * v / (2 * n + 1)
        v *= u * u
    error = 2 * abs(u) ** (2 * terms + 1) / ((2 * terms + 1) * (1 - u * u))
    return s - error, s + error

def entropy_interval(x):
    a, b = log_interval(1 / x)
    c, d = log_interval(1 / (1 - x))
    return x * a + (1 - x) * c, x * b + (1 - x) * d

def main():
    tasks = [(Q(17,50), '<', Q(13,20)), (Q(64,625), '>', Q(33,100)),
             (Q(49,100), '>', Q(69,100)), (Q(1,4), '<', Q(57,100))]
    results=[]
    for x, sign, target in tasks:
        lo, hi=entropy_interval(x)
        assert (hi < target) if sign == '<' else (lo > target)
        # Store modest rational enclosures that are rigorously implied by the
        # larger exact intermediate fractions. Decimal display is not evidence.
        scale=10**12
        flo=lo.numerator*scale//lo.denominator
        cei=-((-hi.numerator*scale)//hi.denominator)
        assert Q(flo,scale)<=lo<=hi<=Q(cei,scale)
        results.append({'x':str(x),'inequality':sign,'target':str(target),
                        'certified_lower':str(Q(flo,scale)),
                        'certified_upper':str(Q(cei,scale))})
    report={'verified':True,'arithmetic':'exact rational','log_terms':128,
            'results':results}
    Path(__file__).with_name('v4_entropy_constants_verification.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
