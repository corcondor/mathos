"""Complete effective-defect H=13 proof, using a positive-divisor CF sieve.

Only exact integers. The original n interval is never scanned. Completeness
uses the written v9 CF lemma and the v11 divisor lemma D | 6 H T.
"""
from pathlib import Path
from math import gcd, isqrt
import base64
import hashlib
import json
import sys
import zlib

ROOT = Path(__file__).resolve().parent
H_VALUE = 13
CERTIFICATE = ROOT / 'v11_effective_defect_13_certificate.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cube_root_floor(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length()+2)//3)
    while True:
        y = (2*x+n//(x*x))//3
        if y >= x:
            while (x+1)**3 <= n:
                x += 1
            while x**3 > n:
                x -= 1
            return x
        x = y


def prefix(h, t):
    """Exact dyadic enclosure; generation is checked by a cylinder later."""
    common = gcd(t, 6*h)
    num, den = t//common, 6*h//common
    assert not (cube_root_floor(num)**3 == num and cube_root_floor(den)**3 == den)
    bits = 384*h+64
    limit = 1 << (192*h)
    while True:
        scale = 1 << bits
        low = cube_root_floor((t << (3*bits))//(6*h))
        ln, ld, hn, hd = low, scale, low+1, scale
        previous, current = 1, 0
        word = []
        while True:
            a = ln//ld
            if a != hn//hd:
                break
            word.append(a)
            previous, current = current, a*current+previous
            if current >= limit:
                return word
            low_rem, high_rem = ln-a*ld, hn-a*hd
            if low_rem == 0:
                break
            ln, ld, hn, hd = hd, high_rem, ld, low_rem
        bits *= 2


def factor_divisors(n):
    """Generator uses trial prime factorization and products of prime powers."""
    value, p, out = n, 2, [1]
    while p*p <= value:
        exponent = 0
        while value % p == 0:
            value //= p
            exponent += 1
        if exponent:
            out = [d*p**e for d in out for e in range(exponent+1)]
        p += 1 if p == 2 else 2
    if value > 1:
        out += [d*value for d in out]
    return sorted(out)


def direct_divisors(n):
    """Verifier uses complementary divisor pairs, not prime factorization."""
    out = set()
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.add(d)
            out.add(n//d)
    return sorted(out)


def expected_t(h):
    return [t for t in range(162*h+1, 229*h) if gcd(t, h) == 1]


def generate():
    rows = []
    for t in expected_t(H_VALUE):
        rows.append([t, factor_divisors(6*H_VALUE*t), prefix(H_VALUE, t)])
        if len(rows) % 100 == 0:
            print(json.dumps({'phase':'generate', 'curves':len(rows)}), flush=True)
    raw = json.dumps(rows, separators=(',', ':')).encode('ascii')
    packed = zlib.compress(raw, 9)
    record = {
        'format':'nested-binomial-v11-effective-defect-cf-v1',
        'H':H_VALUE, 'primitive_curves':len(rows),
        'all_T_before_coprimality':67*H_VALUE-1,
        'encoding':'base64(zlib(UTF-8 JSON))',
        'decoded_schema':'array of [T, all positive divisors of 6HT, CF prefix]',
        'decoded_bytes':len(raw),
        'decoded_sha256':hashlib.sha256(raw).hexdigest(),
        'packed_sha256':hashlib.sha256(packed).hexdigest(),
        'data':base64.b64encode(packed).decode('ascii')
    }
    CERTIFICATE.write_text(json.dumps(record,separators=(',', ':'))+'\n')
    result = {'phase':'generated', 'H':H_VALUE, 'primitive_curves':len(rows),
              'continued_fraction_terms':sum(len(row[2]) for row in rows),
              'bytes':CERTIFICATE.stat().st_size,'sha256':digest(CERTIFICATE)}
    print(json.dumps(result), flush=True)
    return result


def decode():
    doc = json.loads(CERTIFICATE.read_text())
    assert doc['format'] == 'nested-binomial-v11-effective-defect-cf-v1'
    assert doc['H'] == H_VALUE
    packed = base64.b64decode(doc['data'], validate=True)
    assert hashlib.sha256(packed).hexdigest() == doc['packed_sha256']
    raw = zlib.decompress(packed)
    assert len(raw) == doc['decoded_bytes']
    assert hashlib.sha256(raw).hexdigest() == doc['decoded_sha256']
    rows = json.loads(raw)
    assert [row[0] for row in rows] == expected_t(H_VALUE)
    assert len(rows) == doc['primitive_curves'] == 804
    assert doc['all_T_before_coprimality'] == 870
    return rows


def authenticate(h, t, divisors, word):
    assert divisors == direct_divisors(6*h*t)
    # For h=13 the denominator of a rational cube root would have its cube
    # dividing 78, so it is 1. No integer lies strictly between 3 and 7/2.
    assert h == 13 and 3**3*6*h < t < (7**3*6*h)//8
    assert all(type(a) is int and a >= 1 for a in word)
    assert word[0] == 3 and word[1] >= 2
    conv = []
    pm, pc, qm, qc = 0, 1, 1, 0
    for a in word:
        pn, qn = a*pc+pm, a*qc+qm
        assert abs(pn*qc-pc*qn) == 1
        conv.append((pn, qn))
        pm, pc, qm, qc = pc, pn, qc, qn
    limit = 1 << (192*h)
    assert conv[-2][1] < limit <= conv[-1][1]
    assert all(conv[i][1] < conv[i+1][1] for i in range(len(conv)-1))
    left = 6*h*pc**3-t*qc**3
    right = 6*h*(pc+pm)**3-t*(qc+qm)**3
    assert left*right < 0
    return conv


def inspect(h, t, limit, p, q, residue, divisors, stats, recovered):
    stats['fractions_sieved'] += 1
    if residue not in divisors:
        stats['divisor_residue_rejections'] += 1
        return
    stats['divisor_residue_passes'] += 1
    if gcd(p, q) != 1:
        return
    stats['exact_cubic_checks'] += 1
    d = t*q**3-6*h*p**3
    if d != residue or d <= 0 or (t*q) % d:
        return
    common_squared = t*q//d
    common = isqrt(common_squared)
    if common*common != common_squared:
        return
    n, r = common*q+1, common*p
    assert 6*h*r**3 == t*n*(n-1)*(n-2)
    if n < 104:
        reason = 'n below 104'
    elif n >= limit:
        reason = 'outside height'
    elif not 9*n < 3*r < 10*n:
        reason = 'gap fails'
    elif (n-2) % h:
        reason = 'H does not divide n-2'
    else:
        reason = 'SURVIVES'
        stats['surviving_points'] += 1
    recovered.append({'H':h,'T':t,'n':str(n),'r':str(r),'result':reason})


def verify():
    rows = decode()
    stats = {'H':H_VALUE,'primitive_curves':len(rows),'continued_fraction_terms':0,
             'fractions_sieved':0,'divisor_residue_rejections':0,
             'divisor_residue_passes':0,'exact_cubic_checks':0,'surviving_points':0}
    recovered = []
    limit = 1 << (192*H_VALUE)
    for index, (t, ds, word) in enumerate(rows, 1):
        conv = authenticate(H_VALUE, t, ds, word)
        stats['continued_fraction_terms'] += len(word)
        modulus = 6*H_VALUE*t+1
        ds = set(ds)
        mods = [(p % modulus, q % modulus) for p,q in conv]
        for m in range(len(conv)-1):
            pn, qn = conv[m]
            pp, qp = conv[m-1] if m else (1, 0)
            pnext, qnext = conv[m+1]
            rn, sn = mods[m]
            rp, sp = mods[m-1] if m else (1, 0)
            rnext, snext = mods[m+1]
            upper = min(qnext, limit)
            for b in range(-2, 3):
                for a in range(-1, 5):
                    q = a*qn+b*qp
                    if not qn <= q < upper or not 2*q < qnext:
                        continue
                    p = a*pn+b*pp
                    if p <= 3*q:
                        continue
                    rm, sm = (a*rn+b*rp) % modulus, (a*sn+b*sp) % modulus
                    dmod = (t*sm**3-6*H_VALUE*rm**3) % modulus
                    inspect(H_VALUE,t,limit,p,q,dmod,ds,stats,recovered)
                for c in range(-3, 4):
                    q = b*qnext+c*qn
                    if not qn <= q < upper or not 2*q >= qnext:
                        continue
                    p = b*pnext+c*pn
                    if p <= 3*q:
                        continue
                    rm, sm = (b*rnext+c*rn) % modulus, (b*snext+c*sn) % modulus
                    dmod = (t*sm**3-6*H_VALUE*rm**3) % modulus
                    inspect(H_VALUE,t,limit,p,q,dmod,ds,stats,recovered)
        if index % 100 == 0:
            print(json.dumps({'phase':'verify','curves':index,**stats}),flush=True)
    report = {
        'status':'PASS' if stats['surviving_points'] == 0 else 'CANDIDATES_REMAIN',
        **stats, 'all_T_before_coprimality':870,
        'recovered_integer_points':recovered,
        'certificate_sha256':digest(CERTIFICATE),
        'source_sha256':digest(Path(__file__)),
        'all_arithmetic_exact':True, 'original_n_interval_scanned':False,
        'complete_CF_argument_source':'v9_gcd_defect_continued_fractions.md',
        'new_sieve':'positive D divides 6HT, modulus 6HT+1',
        'whole_original_equation_solved':False,
        'CF_completeness_Lean_formalized':False
    }
    out = ROOT / 'v11_effective_defect_cf_verification.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report),flush=True)
    return report


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv)>1 else 'verify'
    if mode == 'generate':
        generate()
    elif mode == 'verify':
        verify()
    else:
        raise SystemExit('usage: python3 v11_effective_defect_cf_checks.py [generate|verify]')
