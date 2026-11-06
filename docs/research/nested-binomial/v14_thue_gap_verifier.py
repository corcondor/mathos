#!/usr/bin/env python3
"""Completely solve fixed-support binomial cubic Thue equations.

Each coprime cube-free coefficient pair is solved in two encodings using
the same PARI/GP backend, with thueinit flag 1. This is not an independent
implementation of the complete solver. No bound on either variable is used.
The input, raw stdout, stderr, and result hashes are retained.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import time


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prime(n):
    if n < 2:
        return False
    return all(n % p for p in range(2, math.isqrt(n)+1))


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def core_pairs(primes):
    require(primes and len(set(primes)) == len(primes), 'distinct primes required')
    require(all(prime(p) for p in primes), 'support must consist of primes')
    choices = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2))
    pairs = set()
    for exponents in itertools.product(choices, repeat=len(primes)):
        a = math.prod(p**e[0] for p, e in zip(primes, exponents))
        b = math.prod(p**e[1] for p, e in zip(primes, exponents))
        require(math.gcd(a,b) == 1, 'pair not coprime')
        pairs.add((a,b))
    require(len(pairs) == 5**len(primes), 'coefficient count')
    # Second, independent enumeration for finite coverage.
    cores = [math.prod(p**e for p,e in zip(primes,exponents))
             for exponents in itertools.product(range(3), repeat=len(primes))]
    independent = {(a,b) for a in cores for b in cores if math.gcd(a,b)==1}
    require(pairs == independent, 'independent coefficient coverage')
    return sorted(pairs)


def integer_pairs(data):
    require(isinstance(data,list), 'solution list required')
    pairs=[]
    for row in data:
        require(isinstance(row,list) and len(row)==2, 'integer pair required')
        require(all(type(v) is int for v in row), 'noninteger solution')
        pairs.append(tuple(row))
    require(len(pairs)==len(set(pairs)), 'duplicate solution')
    return sorted(pairs)


def run(gp, primes, rhs, odd_bases, destination, timeout):
    require(rhs > 0, 'positive RHS required')
    pairs = core_pairs(primes)
    commands = ['print(version());']
    for a,b in pairs:
        commands.append(f'print([{a},{b},thue(thueinit({a}*x^3-{b},1),{rhs}),'
                        f'thue(thueinit(x^3-{a*a*b},1),{rhs*a*a})]);')
    commands.append('quit;')
    program='\n'.join(commands)+'\n'
    destination.parent.mkdir(parents=True,exist_ok=True)
    input_path=destination.with_suffix('.gp')
    stdout_path=destination.with_suffix('.stdout')
    stderr_path=destination.with_suffix('.stderr')
    input_path.write_text(program)
    started=time.monotonic()
    # Stream raw outputs to files so timeout does not discard completed records.
    with input_path.open() as inp, stdout_path.open('w') as out, stderr_path.open('w') as err:
        process=subprocess.run([str(gp),'-f','-q'],stdin=inp,stdout=out,stderr=err,
                               timeout=timeout,check=False)
    elapsed=time.monotonic()-started
    stdout=stdout_path.read_text()
    stderr=stderr_path.read_text()
    require(process.returncode == 0, 'PARI process exit code')
    require(not stderr.strip(), 'PARI reported stderr: '+stderr)
    raw=[ast.literal_eval(line) for line in stdout.splitlines()]
    require(len(raw)==len(pairs)+1, 'PARI output row count')
    version=raw[0]
    rows=raw[1:]
    require([(r[0],r[1]) for r in rows] == pairs, 'PARI output coefficient order')
    results=[]
    positive_n=set()
    positive_n_unfiltered=set()
    for a,b,first,second in rows:
        direct=integer_pairs(first)
        transformed=integer_pairs(second)
        require(all(a*x**3-b*y**3==rhs for x,y in direct),'direct exact substitution')
        require(all(u**3-a*a*b*y**3==rhs*a*a for u,y in transformed),
                'transformed exact substitution')
        recovered=sorted((u//a,y) for u,y in transformed if u%a==0)
        require(direct==recovered,'complete encoded solution sets disagree')
        positive=[(x,y) for x,y in direct if x>0 and y>0]
        selected=[(x,y) for x,y in positive if not odd_bases or (x%2==1 and y%2==1)]
        ns=sorted(a*x**3 for x,y in selected)
        positive_n.update(ns)
        positive_n_unfiltered.update(a*x**3 for x,y in positive)
        results.append({'A':a,'B':b,'all_integer_solutions':direct,
                        'monic_all_integer_solutions':transformed,
                        'positive_solutions_before_parity':positive,
                        'selected_positive_solutions':selected,'selected_n':ns})
    report={
        'status':'PASS','pari_version':version,'support_primes':primes,
        'rhs':rhs,'odd_bases_required':odd_bases,'coefficient_pair_count':len(pairs),
        'pari_calls':2*len(pairs),'thueinit_flag':1,'process_exit_code':process.returncode,
        'stderr_empty':True,'elapsed_seconds':elapsed,
        'unbounded_variables':['x','y','n'],
        'same_backend_twice':True,
        'completeness_dependency':'PARI/GP complete Thue solver; exact substitution does not prove completeness independently',
        'selected_n':sorted(positive_n),
        'positive_n_before_parity':sorted(positive_n_unfiltered),
        'source_sha256':sha256(Path(__file__).read_bytes()),
        'gp_input_sha256':sha256(input_path.read_bytes()),
        'gp_stdout_sha256':sha256(stdout_path.read_bytes()),
        'gp_stderr_sha256':sha256(stderr_path.read_bytes()),
        'records':results,
    }
    destination.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='records'}))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gp',type=Path,required=True)
    parser.add_argument('--primes',type=int,nargs='+',required=True)
    parser.add_argument('--rhs',type=int,required=True)
    parser.add_argument('--odd-bases',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--timeout',type=int,default=600)
    args=parser.parse_args()
    run(args.gp,args.primes,args.rhs,args.odd_bases,args.output,args.timeout)
