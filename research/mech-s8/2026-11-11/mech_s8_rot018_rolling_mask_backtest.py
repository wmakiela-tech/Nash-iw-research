#!/usr/bin/env python3
"""Mech-S8 ROT018. Leave-future-mass masked extrapolation on original Wu-Xu rates.

IMPORTANT: observational pseudo-holdout using known author table, not below-edge
physical validation; mass-side training is always on *larger* PBH masses.

Original author public git d395183674cace6c9906a8911bdeb7234ba4040d
(arXiv v2 code); file arXiv-2509.05618/data/out/hadrons_from_PBH.dat
Git blob 06d0883a27b108692720422294ba2baacd381a64
Raw SHA256 25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df

Use --table PATH for offline original 100 rows, or --fixture for original first
12 rows. Default downloads pinned ORIGINAL table from author's public GitHub.
Python stdlib only; no BlackHawk or BBN execution. No physical-error inference.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
from statistics import median
from urllib.request import urlopen

ORIGIN = ('https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/'
          'd395183674cace6c9906a8911bdeb7234ba4040d/'
          'arXiv-2509.05618/data/out/hadrons_from_PBH.dat')
SHA_FULL='25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df'
SHA_FIRST12='0a81af204bbfe2ced214b3edaaf31bcd52354d4b1934adb67571e726d9d26ac3'
LABELS=('pi_aggregate','Kpm_aggregate','K0L','p_aggregate','n_aggregate')
HORIZONS=(1,3,6,12,28)
WINDOWS=(2,3,5,8,12)

def source_bytes(args):
    if args.fixture:
        p=Path(__file__).resolve().with_name('hadrons_from_PBH_FIRST12_PINNED_AUTHOR_EXCERPT.dat')
        raw=p.read_bytes(); expected=SHA_FIRST12
    elif args.table:
        raw=Path(args.table).read_bytes(); expected=SHA_FULL
    else:
        with urlopen(ORIGIN, timeout=30) as response: raw=response.read()
        expected=SHA_FULL
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise RuntimeError('Raw author source SHA-256 did not match pinned source')
    return raw

def load(raw,fixture):
    lines=raw.decode('utf-8').strip().splitlines()
    assert lines[0].startswith('m_PBH [GeV]')
    rows=[[float(x) for x in line.split()] for line in lines[1:]]
    assert len(rows)==(12 if fixture else 100)
    assert all(len(row)==6 and all(math.isfinite(v) and v>0 for v in row) for row in rows)
    assert all(rows[i][0]<rows[i+1][0] for i in range(len(rows)-1))
    return rows

def regress(xs,ys):
    # Numerically stable centred fit; slope gives log-rate vs log-mass exponent.
    n=len(xs); xm=sum(xs)/n; ym=sum(ys)/n
    cov=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))
    var=sum((x-xm)**2 for x in xs)
    b=cov/var
    return ym-b*xm,b

def run(rows):
    n=len(rows); xx=[math.log(r[0]) for r in rows]
    result={}; n_predictions=0
    for si,label in enumerate(LABELS,1):
        yy=[math.log(r[si]) for r in rows]
        result[label]={}
        for h in HORIZONS:
            if h+2>n: continue
            result[label][str(h)]={}
            for k in WINDOWS:
                if h+k>n: continue
                errors=[]
                # Training [i..i+k-1] at larger PBH mass than target i-h.
                for i in range(h,n-k+1):
                    a,b=regress(xx[i:i+k],yy[i:i+k])
                    target=i-h
                    error=math.expm1(a+b*xx[target]-yy[target])
                    errors.append({'target_row_1based':target+1,'relative_error':error})
                v=[abs(z['relative_error'])*100 for z in errors]
                maxv=max(v)
                maxarg=max(range(len(v)),key=lambda m:v[m])
                result[label][str(h)][str(k)]={
                    'count':len(v),
                    'median_abs_percent':median(v),
                    'max_abs_percent':maxv,
                    'first_anchor_signed_percent':100*errors[0]['relative_error'],
                    'max_abs_target_row_1based':errors[maxarg]['target_row_1based']}
                n_predictions+=len(v)
    return result,n_predictions

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--table');ap.add_argument('--fixture',action='store_true')
    ap.add_argument('--output');args=ap.parse_args()
    assert not (args.table and args.fixture)
    raw=source_bytes(args);rows=load(raw,args.fixture)
    metrics,n_pred=run(rows)
    gap=math.log(rows[1][0]/rows[0][0])
    report={'status':'PASS_SOURCE_PINNED_PSEUDO_HOLDOUT_ONLY',
        'source_sha256':hashlib.sha256(raw).hexdigest(),
        'source_rows':len(rows),'species':len(LABELS),
        'logmass_spacing_first':gap,'mass_ratio_28_steps':math.exp(28*gap),
        'total_predictions':n_pred,'metrics':metrics,
        'claim_ceiling':'KNOWN_DATA_BACKTEST_NOT_BELOW_GRID_VALIDATION/NO_BLACKHAWK_RUN/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN'}
    txt=json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.output: Path(args.output).write_text(txt,encoding='utf-8')
    else: print(txt,end='')

if __name__=='__main__':main()
