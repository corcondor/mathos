"""Generate exact CF-prefix certificates and independently verify S <= 12.

All numerical decisions are integer decisions.  The mathematical completeness
argument is in v9_gcd_defect_continued_fractions.md.  No third-party packages.
"""
from pathlib import Path
from math import gcd, isqrt
import base64
import hashlib
import json
import sys
import zlib

ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT / 'v9_cf_certificates'
MAX_S = 12


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


def make_prefix(S, T):
    d = gcd(T, 6*S)
    num, den = T//d, 6*S//d
    if cube_root_floor(num)**3 == num and cube_root_floor(den)**3 == den:
        return None
    bits = 384*S+64
    limit = 1 << (192*S)
    while True:
        scale = 1 << bits
        low = cube_root_floor((T << (3*bits))//(6*S))
        ln, ld, hn, hd = low, scale, low+1, scale
        qprev, qcur = 1, 0
        word = []
        while True:
            a = ln//ld
            if a != hn//hd:
                break
            word.append(a)
            qprev, qcur = qcur, a*qcur+qprev
            if qcur >= limit:
                return word
            low_remainder, high_remainder = ln-a*ld, hn-a*hd
            if low_remainder == 0:
                break
            ln, ld, hn, hd = hd, high_remainder, ld, low_remainder
        bits *= 2


def generate():
    CERT_DIR.mkdir(exist_ok=True)
    summary = []
    for S in range(1, MAX_S+1):
        rows = [[T, make_prefix(S,T)] for T in range(162*S+1,229*S)]
        raw = json.dumps(rows,separators=(',',':')).encode('ascii')
        packed = zlib.compress(raw,9)
        doc = {
            'format':'nested-binomial-v9-cf-prefixes-v1',
            'S':S,
            'first_T':162*S+1,
            'last_T':229*S-1,
            'rows':len(rows),
            'encoding':'base64(zlib(UTF-8 JSON))',
            'decoded_schema':'array of [T, partial_quotient_array_or_null]',
            'decoded_bytes':len(raw),
            'decoded_sha256':hashlib.sha256(raw).hexdigest(),
            'packed_sha256':hashlib.sha256(packed).hexdigest(),
            'data':base64.b64encode(packed).decode('ascii')
        }
        out=CERT_DIR/f'S{S:02d}.json'
        out.write_text(json.dumps(doc,separators=(',',':'))+'\n')
        record={'S':S,'curves':len(rows),'partial_quotients':sum(len(w) for _,w in rows if w),
                'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
        summary.append(record)
        print(json.dumps(record),flush=True)
    return summary


def decode_certificate(S):
    path=CERT_DIR/f'S{S:02d}.json'
    doc=json.loads(path.read_text())
    assert doc['format']=='nested-binomial-v9-cf-prefixes-v1'
    assert doc['S']==S and doc['rows']==67*S-1
    assert doc['first_T']==162*S+1 and doc['last_T']==229*S-1
    packed=base64.b64decode(doc['data'],validate=True)
    assert hashlib.sha256(packed).hexdigest()==doc['packed_sha256']
    raw=zlib.decompress(packed)
    assert len(raw)==doc['decoded_bytes']
    assert hashlib.sha256(raw).hexdigest()==doc['decoded_sha256']
    rows=json.loads(raw)
    assert all(type(t) is int for t,_ in rows)
    assert [t for t,_ in rows]==list(range(162*S+1,229*S))
    return rows,{'path':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,
                 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}


def rational_root(S,T):
    # For S<=12 a reduced rational cube root has denominator <=4 and
    # numerator <=13, because 3<alpha<7/2.  This check uses no cube-root code.
    return next(((u,v) for v in range(1,5) for u in range(1,15)
                 if gcd(u,v)==1 and 6*S*u**3==T*v**3),None)


def verified_convergents(S,T,word):
    rat=rational_root(S,T)
    if rat is not None:
        assert word is None
        assert 3*rat[1] < 206  # x>=103 contradicts x<3v/2.
        return None
    assert word is not None and len(word)>=2
    assert all(type(a) is int for a in word)
    assert word[0]==3 and word[1]>=2
    assert all(type(a) is int and a>=1 for a in word[1:])
    conv=[]
    pm,pc,qm,qc=0,1,1,0
    for a in word:
        pn,qn=a*pc+pm,a*qc+qm
        assert abs(pn*qc-pc*qn)==1
        conv.append((pn,qn))
        pm,pc,qm,qc=pc,pn,qc,qn
    H=1 << (192*S)
    assert conv[-2][1] < H <= conv[-1][1]
    assert all(conv[j][1] < conv[j+1][1] for j in range(len(conv)-1))
    # Independent cylinder certificate: two rational cubes bracket T/(6S).
    left=6*S*pc**3-T*qc**3
    right=6*S*(pc+pm)**3-T*(qc+qm)**3
    assert left*right<0
    return conv


def inspect_fraction(S,T,H,p,q,stats,recoveries):
    if p<=3*q or gcd(p,q)!=1:
        return
    stats['reduced_fractions_checked']+=1
    gap=T*q**3-6*S*p**3
    if gap<=0 or (T*q)%gap:
        return
    g2=T*q//gap
    g=isqrt(g2)
    if g*g!=g2:
        return
    N=g*q+1
    r=g*p
    assert 6*S*r**3==T*N*(N-1)*(N-2)
    if N<104:
        reason='n below 104'
    elif N>=H:
        reason='n outside proved height bound'
    elif not 9*N<3*r<10*N:
        reason='strict r gap fails'
    elif (N-2)%S:
        reason='S does not divide n-2'
    else:
        reason='SURVIVES'
        stats['surviving_points']+=1
    recoveries.append({'S':S,'T':T,'n':str(N),'r':str(r),'result':reason})


def verify():
    report={'status':'RUNNING','max_S':MAX_S,'curves':0,'irrational_curves':0,
            'rational_curves':0,'continued_fraction_terms':0,
            'reduced_fractions_checked':0,'surviving_points':0,'by_S':[],
            'certificates':[],'recovered_integer_points':[],
            'all_arithmetic_exact':True,'original_n_interval_scanned':False,
            'continued_fraction_completeness_Lean_formalized':False,
            'whole_original_equation_solved':False}
    for S in range(1,MAX_S+1):
        rows,file_info=decode_certificate(S)
        report['certificates'].append(file_info)
        local={'S':S,'curves':len(rows),'irrational_curves':0,'rational_curves':0,
               'continued_fraction_terms':0,'reduced_fractions_checked':0,'surviving_points':0}
        H=1 << (192*S)
        for T,word in rows:
            conv=verified_convergents(S,T,word)
            if conv is None:
                local['rational_curves']+=1
                continue
            local['irrational_curves']+=1
            local['continued_fraction_terms']+=len(word)
            for m in range(len(conv)-1):
                pn,qn=conv[m]
                pp,qp=conv[m-1] if m else (1,0)
                pnext,qnext=conv[m+1]
                upper=min(qnext,H)
                # This partitions the two denominator halves, instead of
                # taking the union used by the independent reproduction.
                for b in range(-2,3):
                    for a in range(-1,5):
                        q=a*qn+b*qp
                        if not qn<=q<upper or not 2*q<qnext:
                            continue
                        p=a*pn+b*pp
                        inspect_fraction(S,T,H,p,q,local,report['recovered_integer_points'])
                    for c in range(-3,4):
                        q=b*qnext+c*qn
                        if not qn<=q<upper or not 2*q>=qnext:
                            continue
                        p=b*pnext+c*pn
                        inspect_fraction(S,T,H,p,q,local,report['recovered_integer_points'])
        report['by_S'].append(local)
        for key in ['curves','irrational_curves','rational_curves','continued_fraction_terms',
                    'reduced_fractions_checked','surviving_points']:
            report[key]+=local[key]
        print(json.dumps(local),flush=True)
    assert report['curves']==5214
    assert report['surviving_points']==0
    report['status']='PASS'
    report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out=ROOT/'v9_gcd_defect_cf_verification.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','curves','irrational_curves',
         'rational_curves','continued_fraction_terms','reduced_fractions_checked','surviving_points']}),flush=True)
    return report


if __name__=='__main__':
    command=sys.argv[1] if len(sys.argv)>1 else 'verify'
    if command=='generate':
        generate()
    elif command=='verify':
        verify()
    else:
        raise SystemExit('usage: python3 v9_gcd_defect_cf_checks.py [generate|verify]')
