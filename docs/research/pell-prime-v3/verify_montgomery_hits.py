"""Independent 2x2 matrix modular powers, no Montgomery assumptions."""
from pathlib import Path
import json
from math import isqrt
def mul(a,b,m):
    return [[sum(a[i][k]*b[k][j] for k in range(2))%m for j in range(2)] for i in range(2)]
def coeff(s,m):
    a=[[1,0],[0,1]];b=[[2,1],[1,0]]
    while s:
        if s&1:a=mul(a,b,m)
        b=mul(b,b,m);s//=2
    return (a[0][0]-a[0][1])%m,a[0][1]
j=json.loads(Path(__file__).with_name('montgomery_hits.json').read_text())
assert len(j['hits'])==37==len(set(s for s,c,d in j['hits']))
for s,c,d in j['hits']:
    assert s>2 and all(s%k for k in range(2,isqrt(s)+1))
    assert c in ('X','Y') and 1<d<2**(s-1) and coeff(s,d)[c=='Y']==0
assert sum(a[3] for a in j['stages'])==37 and sum(a[4] for a in j['stages'])==467644422
print('PASS 37 exact proper factors (all previous 750 and full CSV coverage checked separately)')
