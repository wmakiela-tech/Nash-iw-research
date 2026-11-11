#!/usr/bin/env python3
"""MT15 ROT007 sharp node-only monotone Wu-Xu hadron number fraction.

Input is author source table and TWO native Badacz clock versions.
Mathematical source-class diagnostic ONLY: not physical BBN or PBH bound.
"""
import argparse, csv, hashlib, json, math

BLOBS = (
    "06d0883a27b108692720422294ba2baacd381a64",
    "357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e",
    "e0759b4a22c3282d3f11c58412c4b6543e6dc4c7")
G = 5.609588603804452e23

def source(path, sha):
    z = open(path, "rb").read()
    got = hashlib.sha1(b"blob "+str(len(z)).encode()+b"\0"+z).hexdigest()
    if got != sha: raise ValueError("pinned Git blob mismatch for "+path)
    return z.decode("utf-8")

def table(raw):
    a = [list(map(float,line.split())) for line in raw.splitlines()[1:] if line.strip()]
    assert len(a)==100 and all(len(r)==6 for r in a)
    rows=[(r[0]/G/1e9,r[1:]) for r in a]
    assert abs(rows[0][0]-1)<1e-12
    assert all(rows[i][0]<rows[i+1][0] for i in range(99))
    assert all(rows[i][1][h]>rows[i+1][1][h]>0 for i in range(99) for h in range(5))
    return rows

def clock(raw, label):
    a=list(csv.DictReader(line for line in raw.splitlines() if line and not line.startswith("#")))
    assert len(a) == (8 if label=="DEFAULT" else 6)
    return [dict(version=label,j=int(r["j"]),log10beta=float(r["log10beta"]),
                 M0_g=float(r["m0_g"]),M_Tnuc_g=float(r["M_T0_g"]))
            for r in a if int(r["j"]) in (98,99)]

def weight(a,b): return (b*b*b-a*a*a)/3

def bound(rows,M0_g,M_Tnuc_g):
    m0=M0_g/1e9; t=M_Tnuc_g/1e9
    assert 1<t<m0<rows[-1][0]
    Llo=Lhi=Elo=Ehi=0.
    cross=None
    for i in range(99):
        x,u=rows[i];y,v=rows[i+1]
        a,b=max(1.,x),min(m0,y)
        if b<=a: continue
        U,V=sum(u),sum(v)
        if b<=t:
            Llo+=V*weight(a,b);Lhi+=U*weight(a,b)
        elif a>=t:
            Elo+=V*weight(a,b);Ehi+=U*weight(a,b)
        else:
            assert cross is None
            cross=(i+1,U,V,weight(a,t),weight(t,b))
    assert cross is not None
    cell,U,V,Wl,We=cross
    frac=lambda l,e:l/(l+e)
    # Crossing cell: all V / all U for infimum, a jump at event for supremum.
    fmin_v=frac(Llo+V*Wl,Ehi+V*We)
    fmin_u=frac(Llo+U*Wl,Ehi+U*We)
    fmax=frac(Lhi+U*Wl,Elo+V*We)
    return dict(sharp_infimum=min(fmin_v,fmin_u),
                sharp_supremum=fmax,
                minimizing_cross_cell=("right_rate" if fmin_v<=fmin_u else "left_rate"),
                event_crossing_cell_one_based=cell)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--table",required=True)
    p.add_argument("--default-clock",required=True)
    p.add_argument("--posthoc-clock",required=True)
    a=p.parse_args()
    rows=table(source(a.table,BLOBS[0]))
    clocks=clock(source(a.default_clock,BLOBS[1]),"DEFAULT")
    clocks+=clock(source(a.posthoc_clock,BLOBS[2]),"POSTHOC_1e-4")
    out=[dict(q,**bound(rows,q["M0_g"],q["M_Tnuc_g"])) for q in clocks]
    print(json.dumps(dict(
        status="SOURCE_TABLE_CLOCK_REPLAY",
        mathematical_scope="positive monotone per-channel above 1e9g; fixed native clock",
        not_physical_BBN_PBH_bound=True,original_git_blobs=list(BLOBS),
        strict_node_monotone_transitions=495,cases=out),indent=2))

if __name__=="__main__": main()
