#!/usr/bin/env python3
"""MT15 ROT004: conditional source-table/clock hadron-N extrapolation envelope.

Requires ORIGINAL unedited Wu-Xu 100-row table and Badacz 8-row clock.
Does NOT execute Julia, BlackHawk, PYTHIA or compute a physical BBN bound.

Example:
  python mt15_rot004_sharp_slope_envelope_reproducer.py --table hadrons_from_PBH.dat --clock heavy_end_clock.csv
  python mt15_rot004_sharp_slope_envelope_reproducer.py --self-test
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

ORIGINAL_RATE_BLOB = "06d0883a27b108692720422294ba2baacd381a64"
ORIGINAL_CLOCK_BLOB = "357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e"
GEV_PER_GRAM = 5.609588603804452e23

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def load_source(table, clock):
    tb, cb = Path(table).read_bytes(), Path(clock).read_bytes()
    assert git_blob_sha(tb) == ORIGINAL_RATE_BLOB, "Original author table Git blob mismatch"
    assert git_blob_sha(cb) == ORIGINAL_CLOCK_BLOB, "Badacz clock Git blob mismatch"
    text = tb.decode("utf-8").splitlines()
    records = [[float(x) for x in line.split()] for line in text[1:] if line.strip()]
    assert len(records) == 100 and all(len(x) == 6 for x in records)
    assert all(all(math.isfinite(v) and v > 0 for v in row) for row in records)
    mstar = records[0][0]/GEV_PER_GRAM
    assert math.isclose(mstar, 1e9, rel_tol=1e-14)
    masses = [row[0]/GEV_PER_GRAM/mstar for row in records]
    assert all(a < b for a,b in zip(masses,masses[1:]))
    rates = [row[1:] for row in records]
    with Path(clock).open(newline="", encoding="utf8") as handle:
        cs = list(csv.DictReader((ln for ln in handle if not ln.startswith("#"))))
    assert len(cs) == 8
    return mstar, masses, rates, cs

def source_integral(a,b,masses,rates):
    """Integrate x² sum_h R_h(x) dx with SOURCE per-channel log-log slopes."""
    if not (0 < a <= b <= masses[-1]*(1+1e-13)):
        raise ValueError("Outside verified author table domain")
    total = 0.0
    for i in range(len(masses)-1):
        xi, xj = masses[i:i+2]
        lo,hi = max(a,xi),min(b,xj)
        if lo>=hi:
            continue
        for u,v in zip(rates[i],rates[i+1]):
            e = 3.0+math.log(v/u)/math.log(xj/xi)
            if abs(e) < 1e-10:
                total += u*xi**3*math.log(hi/lo)
            else:
                total += u*xi**3*(lo/xi)**e*math.expm1(e*math.log(hi/lo))/e
    return total

def tail_moment(Rstar,p,z=0.0):
    """U(p,z)=integral_z^1 x² Rstar x^(-p) dx (normalized by Mstar³/K)."""
    if not (0 <= z < 1):
        raise ValueError("z must be in [0,1)")
    if z == 0 and p >= 3:
        return math.inf
    if abs(3-p) < 1e-12:
        return -Rstar*math.log(z)
    return Rstar * (-math.expm1((3-p)*math.log(z)) if z>0 else 1.0)/(3-p)

def observed_model(table,clock,pmin=1.15,pmax=1.35,z=0):
    if not (0 <= pmin <= pmax):
        raise ValueError("Assumed positive logarithmic slope band must be ordered")
    if z == 0 and pmax >= 3:
        raise ValueError("For zero mass cutoff require pmax < 3 for finite number tail; otherwise upper fraction has only supremum 1")
    Mstar, masses, rates, cases = load_source(table,clock)
    Rstar=sum(rates[0]); slopes=[-math.log(rates[1][k]/rates[0][k])/math.log(masses[1]) for k in range(5)]
    ulo=tail_moment(Rstar,pmin,z)
    uhi=tail_moment(Rstar,pmax,z)
    ufive=sum(tail_moment(rates[0][k],slopes[k],0) for k in range(5))
    out=[]
    for row in cases:
        j=int(row['j'])
        if j not in (98,99):
            continue
        m0=float(row['m0_g'])/Mstar
        mnuc=float(row['M_T0_g'])/Mstar
        T=source_integral(1,m0,masses,rates)
        L=source_integral(1,mnuc,masses,rates)
        assert 0 < L < T
        f=lambda u:(L+u)/(T+u)
        out.append(dict(j=j,beta_exp=float(row['log10beta']),m0_g=float(row['m0_g']),M_Tnuc_g=float(row['M_T0_g']),T_above_grid_normalized=T,L_post_Tnuc_above_grid_normalized=L,source_only_sharp_lower=L/T,conditional_sharp_lower=f(ulo),conditional_sharp_upper=f(uhi),original_first_pair_extrapolated_fraction=f(ufive),p_constant_needed_for_fraction_half=3-Rstar/(T-2*L)))
    assert len(out)==4
    return dict(status="SOURCE_TABLE_100_ROW_MASS_CLOCK_REPLAY_CONDITIONAL",not_a="physical_PBH_BBN_bound",mstar_g=Mstar,Rstar=Rstar,source_first_two_exponents=slopes,assumed_pmin=pmin,assumed_pmax=pmax,assumed_below_mass_cut_fraction=z,below_grid_tail_range_normalized=[ulo,uhi],source_blobs=[ORIGINAL_RATE_BLOB,ORIGINAL_CLOCK_BLOB],cases=out)

def self_test():
    # Exact power-law unit analytic quadrature on synthetic data, NOT source execution.
    mass=[1.,2.,4.]
    rate=[[float(2*x**(-1.2))]*5 for x in mass]
    got=source_integral(1.,4.,mass,rate)
    expected=10*(4**1.8-1)/1.8
    assert math.isclose(got,expected,rel_tol=1e-13)
    for p in (0.,1.2,1.35,2.999,3.):
        z=.1
        known=(1-z**(3-p))/(3-p) if p!=3 else -math.log(z)
        assert math.isclose(tail_moment(1,p,z),known,rel_tol=1e-12)
    assert tail_moment(1,3,0)==math.inf
    u1,u2=tail_moment(1,1.15),tail_moment(1,1.35)
    assert u1<u2
    print(json.dumps(dict(status="SYNTHETIC_UNIT_SELF_TEST_PASS",source_original_table_executed=False,source_original_clock_executed=False)))

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--table');ap.add_argument('--clock')
    ap.add_argument('--pmin',type=float,default=1.15)
    ap.add_argument('--pmax',type=float,default=1.35)
    ap.add_argument('--z',type=float,default=0.0)
    ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    if args.self_test:
        self_test()
    else:
        if not args.table or not args.clock:
            ap.error('--table and --clock original source files are required')
        print(json.dumps(observed_model(args.table,args.clock,args.pmin,args.pmax,args.z),indent=2))
