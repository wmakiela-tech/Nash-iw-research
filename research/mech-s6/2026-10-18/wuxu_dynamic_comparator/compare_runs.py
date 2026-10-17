#!/usr/bin/env python3
from __future__ import annotations
import csv, math
from pathlib import Path
import sys

outdir = Path(sys.argv[1])

def read_summary(label):
    d = {}
    for line in (outdir / f"summary_{label}.txt").read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            d[k] = v
    return d

def read_csv(label):
    with (outdir / f"trajectory_{label}.csv").open(newline="") as f:
        return list(csv.DictReader(f))

cur_s, rep_s = read_summary("current"), read_summary("repaired")
cur, rep = read_csv("current"), read_csv("repaired")
assert len(cur) == len(rep)

def arr(rows, key): return [float(r[key]) for r in rows]
a_cur, a_rep = arr(cur,"a"), arr(rep,"a")
grid_diff = max(abs(x-y) for x,y in zip(a_cur,a_rep))
if grid_diff > 1e-10:
    raise RuntimeError(f"scale-factor grids differ: {grid_diff}")

def max_abs_delta(key):
    c, r = arr(cur,key), arr(rep,key)
    vals=[abs(y-x) for x,y in zip(c,r)]
    i=max(range(len(vals)), key=vals.__getitem__)
    return vals[i], i, c[i], r[i]

def normalized_linf(key):
    c, r = arr(cur,key), arr(rep,key)
    scale=max(abs(x) for x in c)
    return math.nan if scale == 0 else max(abs(y-x) for x,y in zip(c,r))/scale

dX,iX,Xc,Xr=max_abs_delta("Xn")
dA,iA,Ac,Ar=max_abs_delta("A_GeV")
dB,iB,Bc,Br=max_abs_delta("B_GeV")
dF,iF,Fc,Fr=max_abs_delta("F_had_GeV")
yp_c,yp_r=float(cur_s["Yp"]),float(rep_s["Yp"])
dyp=yp_r-yp_c
relyp=dyp/yp_c if yp_c else math.nan
source_active=int(cur_s["source_active_points"])
below_edge=int(cur_s["source_active_below_1e9g_points"])
below_frac=below_edge/source_active if source_active else math.nan

report=f"""# Mech-S6 Wu-Xu dynamic charge-pair comparator — one-point diagnostic

**Upstream Wu-Xu commit:** `d395183674cace6c9906a8911bdeb7234ba4040d`  
**NaturalUnits pin:** `4a9f007ff1df416c9fef28c4d83d8fe8846099cf`  
**Diagnostic point:** M_PBH=6e9 g, beta=1e-16  
**Comparator:** published aggregate-to-single map vs charge-symmetric B_sym map  
**Class:** dynamic executor diagnostic / not a modern full-BBN endpoint

## Primary result

| quantity | current | repaired | change |
|---|---:|---:|---:|
| reduced Y_P proxy | {yp_c:.12g} | {yp_r:.12g} | {dyp:+.6g} ({relyp:+.3%}) |

Maximum trajectory differences:

- max |delta X_n| = {dX:.6g} at sample {iX}; current={Xc:.9g}, repaired={Xr:.9g}
- max |delta A| = {dA:.6g} GeV; normalized L-inf vs current max = {normalized_linf("A_GeV"):.3%}
- max |delta B| = {dB:.6g} GeV; normalized L-inf vs current max = {normalized_linf("B_GeV"):.3%}
- max |delta F_had| = {dF:.6g} GeV; normalized L-inf vs current max = {normalized_linf("F_had_GeV"):.3%}

## Source-support confound

Source-active sampled points: {source_active}.  
Source-active sampled points with M_PBH<1e9 g: {below_edge} ({below_frac:.2%}).

Therefore the dynamic difference isolates the charge-map change within the same E0 executor, but it is not a source-valid E2b calculation.

## Log-floor activity

| species | current active-floor samples | repaired active-floor samples |
|---|---:|---:|
| pi- | {cur_s["floor_pi_minus_points"]} | {rep_s["floor_pi_minus_points"]} |
| pi+ | {cur_s["floor_pi_plus_points"]} | {rep_s["floor_pi_plus_points"]} |
| K- | {cur_s["floor_K_minus_points"]} | {rep_s["floor_K_minus_points"]} |
| K0L | {cur_s["floor_K0L_points"]} | {rep_s["floor_K0L_points"]} |
| pbar | {cur_s["floor_pbar_points"]} | {rep_s["floor_pbar_points"]} |
| nbar | {cur_s["floor_nbar_points"]} | {rep_s["floor_nbar_points"]} |

Any nonzero floor activity means the raw executor response need not obey the simple common-background half-response theorem during those samples.

## Claim ceiling

This comparator may establish the effect of the source-map repair on the Wu-Xu reduced executor at one diagnostic point.

It does not establish:
- a modern Y_P or D/H prediction,
- a source-valid terminal hadron model below 1e9 g,
- a PBH abundance bound,
- a global result over the mass/beta plane,
- CANON / EXEC / novelty.

DYNAMIC_ONE_POINT_COMPARATOR = EXECUTED  
FULL_GRID = NOT_RUN  
MODERN_BBN_ENDPOINT = NOT_RUN  
SOURCE_VALID_E2B = OPEN
"""
(outdir/"comparison_report.md").write_text(report)
print(report)
