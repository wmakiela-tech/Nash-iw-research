"""PREREG_081 DEV-1 (technical): drop rows whose Float64 T_MeV equals the previous row's T_MeV exactly.
Cause: the merged ln a grid (native + refined) contains near-coincident ArbFloat points that unique() keeps but whose
Float64 temperatures are identical; net_rate_079.py (frozen) requires strictly monotone T. Applied uniformly to all files.
Usage: python3 -I dedupe_rates_081.py <dump_dir> <out_dir>   (copies summary_*.csv unchanged)"""
import csv, os, shutil, sys
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
log = []
for f in sorted(os.listdir(src)):
    p = os.path.join(src, f)
    if f.startswith("summary_"):
        shutil.copy2(p, os.path.join(dst, f)); continue
    if not f.startswith("rates_"):
        continue
    rows = list(csv.DictReader(open(p)))
    keep, dropped = [], []
    for r in rows:
        if keep and float(r["T_MeV"]) == float(keep[-1]["T_MeV"]):
            dropped.append(r["i"]); continue
        keep.append(r)
    with open(os.path.join(dst, f), "w", newline="") as o:
        w = csv.DictWriter(o, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(keep)
    log.append(f"{f},{len(rows)},{len(keep)},{';'.join(dropped)}")
open(os.path.join(dst, "dedupe_log.csv"), "w").write("file,rows_in,rows_out,dropped_i\n" + "\n".join(log) + "\n")
print("files", len(log), "with drops", sum(1 for l in log if not l.endswith(",")))
