#!/usr/bin/env python3
"""MT15 ROT001: exact log-log mass integrals and sharp unknown-tail bounds.

Inputs are pinned ORIGINAL public files, fetched separately:
  1. Wu-Xu hadrons_from_PBH.dat @ d395183674cace6c9906a8911bdeb7234ba4040d
  2. Badacz heavy_end_clock.csv @ 5b5521ed1f057d341c1a410193e9a923c8ca1f8e
Example: python3 -I iw_mt15_rot001_tail_partial_identification_reproducer.py \
  --table hadrons_from_PBH.dat --clock heavy_end_clock.csv
No native Julia/BlackHawk run and no Yp claim.
"""
import argparse
import csv
import json
from math import expm1, log
from pathlib import Path

EXPECTED = {
    (98, -30.0): 0.09787569531776,
    (98, -19.2): 0.10022010182011,
    (99, -30.0): 0.26559907297183,
    (99, -19.2): 0.26890602129710,
}

def read_table(path):
    lines = Path(path).read_text(encoding="utf-8").strip().splitlines()
    rows = [list(map(float, line.split())) for line in lines[1:] if line.strip()]
    assert len(rows) == 100 and all(len(row) == 6 for row in rows)
    mass_first = rows[0][0]
    a = [[row[0] / mass_first] + row[1:] for row in rows]
    assert all(a[i][0] < a[i+1][0] for i in range(99))
    assert all(y > 0 for row in a for y in row)
    return a

def mass_integral(table, lo, hi, col):
    """Integral of M^2 R_col(M) dM, in x=M/(10^9 g) coordinates.
    Suppresses one common strictly positive conversion/clock factor.
    """
    if hi <= lo:
        return 0.0
    assert lo >= 1 and hi <= table[-1][0]
    edges = [lo] + [row[0] for row in table if lo < row[0] < hi] + [hi]
    total = 0.0
    for x, y in zip(edges[:-1], edges[1:]):
        middle = (x*y)**0.5
        j = next((i for i in range(len(table)-1)
                  if table[i][0] <= middle < table[i+1][0]), len(table)-2)
        xj, xnext = table[j][0], table[j+1][0]
        rj, rnext = table[j][col], table[j+1][col]
        p = log(rnext/rj)/log(xnext/xj)
        q = p + 3.0
        rate_x = rj * (x/xj)**p
        u = log(y/x)
        term = expm1(q*u)/q if abs(q) > 1e-10 else u
        total += rate_x * x**3 * term
    return total

def extrapolated_tail(table, col):
    """Hypothetical first-two-row log-log continuation from x=1 to x=0."""
    p = log(table[1][col]/table[0][col])/log(table[1][0]/table[0][0])
    if p <= -3:
        return float("inf"), p
    return table[0][col]/(p+3), p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", required=True)
    ap.add_argument("--clock", required=True)
    args = ap.parse_args()
    table = read_table(args.table)
    with open(args.clock, newline="", encoding="utf-8") as stream:
        lines = (line for line in stream if not line.startswith("#"))
        clocks = list(csv.DictReader(lines))
    output = []
    for row in clocks:
        j, beta = int(row["j"]), float(row["log10beta"])
        if (j, beta) not in EXPECTED:
            continue
        m0 = float(row["m0_g"]) / 1e9
        mnuc = float(row["M_T0_g"]) / 1e9
        assert 1.0 < mnuc < m0 < table[-1][0]
        T = L = U = 0.0
        slopes = []
        for channel in range(1, 6):
            T += mass_integral(table, 1., m0, channel)
            L += mass_integral(table, 1., mnuc, channel)
            tail, slope = extrapolated_tail(table, channel)
            U += tail
            slopes.append(slope)
        flo = L/T
        fext = (L+U)/(T+U)
        assert abs(fext - EXPECTED[(j, beta)]) < 3e-10, (j,beta,fext)
        output.append({
            "j": j, "log10beta": beta,
            "m0_g": float(row["m0_g"]), "M_Tnuc_g": float(row["M_T0_g"]),
            "late_fraction_no_tail_sharp_lower": flo,
            "late_fraction_first_pair_tail": fext,
            "tail_share_total_first_pair_model": U/(T+U),
            "tail_share_late_first_pair_model": U/(L+U),
            "first_segment_slopes": slopes,
            "readback_ref_MT14_ROT029_matched": True
        })
    assert len(output) == 4
    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
