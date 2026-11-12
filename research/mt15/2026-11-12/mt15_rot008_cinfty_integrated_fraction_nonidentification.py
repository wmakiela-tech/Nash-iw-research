#!/usr/bin/env python3
"""MT15 ROT008: exact nonidentification of late number by smooth positive
rate interpolants that preserve every mass-grid value AND all nodal jets.

Original Wu-Xu 100x5 rates / Badacz native clocks are required for source mode;
Python selftest is SYNTHETIC and explicitly not an original-source execution.
No Hawking/BBN/physical constraint or mathematical novelty is claimed.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

AUTHOR_BLOB = '06d0883a27b108692720422294ba2baacd381a64'
CLOCK_DEFAULT_BLOB = '357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e'
CLOCK_POSTHOC_BLOB = 'e0759b4a22c3282d3f11c58412c4b6543e6dc4c7'
GEV_PER_G = 5.609588603804452e23


def original_text(path, git_blob):
    b = Path(path).read_bytes()
    sha = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
    if sha != git_blob:
        raise ValueError(f'Wrong original Git blob for {path}: {sha}')
    return b.decode('utf8')


def parse_rows(source):
    raw = [list(map(float, ln.split())) for ln in source.splitlines()[1:] if ln.strip()]
    if len(raw) != 100 or any(len(r) != 6 for r in raw):
        raise ValueError('Required 100 positive mass rows with exactly five rate channels')
    rows = [(r[0] / GEV_PER_G / 1e9, r[1:]) for r in raw]
    assert all(rows[i][0] < rows[i+1][0] for i in range(99))
    assert all(rows[i][1][h] > rows[i+1][1][h] > 0
               for i in range(99) for h in range(5))
    return rows


def parse_clock(source, label, n):
    rs = list(csv.DictReader(ln for ln in source.splitlines()
                             if ln and not ln.startswith('#')))
    assert len(rs) == n
    return [dict(j=int(r['j']), beta=float(r['log10beta']),
                 m0=float(r['m0_g'])/1e9, event=float(r['M_T0_g'])/1e9,
                 clock=label) for r in rs if int(r['j']) in (98, 99)]


def flatstep(u):
    if u <= 0: return 0.0
    if u >= 1: return 1.0
    return 1/(1+math.exp(-1/(1-u)+1/u))


def bump(u):
    if abs(u) >= 1: return 0.0
    return math.exp(-1/(1-u*u))


def simpson(f, a, b, n=256):
    if b <= a: return 0.0
    if n%2: raise ValueError('n must be even')
    d=(b-a)/n
    s=f(a)+f(b)
    for j in range(1,n):
        s += (4 if j%2 else 2)*f(a+j*d)
    return s*d/3


def baseline_integral(rows,a,b,n=256):
    total=0.0
    for i in range(len(rows)-1):
        x,u=rows[i];y,v=rows[i+1]
        lo,hi=max(x,a),min(y,b)
        if hi <= lo: continue
        logu=[math.log(z) for z in u]; logv=[math.log(z) for z in v]
        def density(m):
            s=flatstep((m-x)/(y-x))
            return m*m*sum(math.exp((1-s)*a+s*b)
                           for a,b in zip(logu,logv))
        total += simpson(density,lo,hi,n)
    return total


def normalized_cell_bump(cell,weighted_mass=1.0):
    x,y=cell
    c=(x+y)/2; width=(y-x)/4
    assert x < c-width < c+width < y
    J=simpson(lambda m:m*m*bump((m-c)/width),c-width,c+width,1024)
    assert J>0
    return dict(center=c,halfwidth=width,integral=J,
                rate_height_coefficient=weighted_mass/J)


def witness(rows,q,n=256):
    t=q['event'];m0=q['m0']
    assert rows[0][0] < t < m0 < rows[-1][0]
    late_cell=(rows[0][0],rows[1][0]);assert late_cell[1]<t
    early_idx=next(i for i in range(len(rows)-1)
                   if rows[i][0] >= 5 and rows[i+1][0] < 9.5)
    early_cell=(rows[early_idx][0],rows[early_idx+1][0])
    assert t < early_cell[0] < early_cell[1] < m0
    L=baseline_integral(rows,rows[0][0],t,n)
    E=baseline_integral(rows,t,m0,n)
    T=L+E
    f=L/T
    assert 0.01 < f < 0.99
    A_early=L/0.01 - T
    A_late=(0.99*T-L)/0.01
    assert min(A_early,A_late)>0
    be=normalized_cell_bump(early_cell,A_early)
    bl=normalized_cell_bump(late_cell,A_late)
    assert math.isclose((L)/(T+A_early),0.01,rel_tol=1e-13)
    assert math.isclose((L+A_late)/(T+A_late),0.99,rel_tol=1e-13)
    return dict(q,baseline_fraction=f,late_count=L,early_count=E,
                early_bump_target_1pct=dict(A=A_early,**be),
                late_bump_target_99pct=dict(A=A_late,**bl),
                exact_target_fractions=[L/(T+A_early),(L+A_late)/(T+A_late)])


def selftest():
    rows=[(1,[100,25,4,2,1]),(2,[50,20,3,1.5,.8]),
          (4,[15,10,2,1,.5]),(8,[2,1,.5,.25,.125])]
    L=baseline_integral(rows,1,3,64)
    E=baseline_integral(rows,3,7,64)
    assert 0<L and 0<E
    A_early=L/0.01-(L+E)
    A_late=(0.99*(L+E)-L)/0.01
    be=normalized_cell_bump((4,8),A_early)
    bl=normalized_cell_bump((1,2),A_late)
    for b in (be,bl):
        c=b['center'];h=b['halfwidth']
        actual=simpson(lambda m:m*m*bump((m-c)/h)*b['rate_height_coefficient'],
                       c-h,c+h,1024)
        assert math.isclose(actual,b['rate_height_coefficient']*b['integral'],rel_tol=2e-14)
    assert abs(L/(L+E+A_early)-0.01)<1e-14
    assert abs((L+A_late)/(L+E+A_late)-0.99)<1e-14
    print(json.dumps(dict(status='SYNTHETIC_SELFTEST_PASS',original_source_executed=False,
                          baseline_fraction=L/(L+E),witness_early_f=.01,
                          witness_late_f=.99),indent=2))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--author');ap.add_argument('--clock-default');ap.add_argument('--clock-posthoc')
    ap.add_argument('--selftest',action='store_true')
    args=ap.parse_args()
    if args.selftest:
        selftest();return
    if not args.author or not args.clock_default or not args.clock_posthoc:
        ap.error('Original 100x5 author table and both Badacz clock files required')
    rows=parse_rows(original_text(args.author,AUTHOR_BLOB))
    qs=parse_clock(original_text(args.clock_default,CLOCK_DEFAULT_BLOB),'DEFAULT',8)
    qs+=parse_clock(original_text(args.clock_posthoc,CLOCK_POSTHOC_BLOB),'POSTHOC',6)
    a=[witness(rows,q,128) for q in qs]
    b=[witness(rows,q,512) for q in qs]
    for x,y in zip(a,b):
        assert abs(x['baseline_fraction']-y['baseline_fraction'])<2e-10
        assert x['exact_target_fractions']==y['exact_target_fractions'] or all(
            abs(v-w)<1e-13 for v,w in zip(x['exact_target_fractions'],y['exact_target_fractions']))
    print(json.dumps(dict(status='PINNED_ORIGINAL_SOURCE_REPLAY_PASS',
                          source_blobs=[AUTHOR_BLOB,CLOCK_DEFAULT_BLOB,CLOCK_POSTHOC_BLOB],
                          class_scope='POSITIVE_CINF_ALL_NODE_AND_JET_PRESERVING_BUMPS',
                          not_physical_PBH_BBN_bound=True,
                          cases=b),indent=2))


if __name__ == '__main__':main()
