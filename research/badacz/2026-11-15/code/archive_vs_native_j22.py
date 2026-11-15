#!/usr/bin/env python3
"""Badacz (Claude), POST HOC static comparison (no Julia): authors' archived scanning.jld2 (Wu-Xu d395183, file SHA-256
51844a46...) row j=22 versus my native default-tolerance dense grid (REVIEW_065, yp064_default.csv) and 1e-4 grid.
JLD2 arrays are read by locating the deflate streams (h5py cannot open JLD2 chunk encoding); extraction is validated by
reproducing Mech-S8 ROT020 statistics (Y range, 4469 cells chi2<=4, chi2 formula). Matrix is Iterators.product(m, beta):
first index = mass. Usage: python3 -I archive_vs_native_j22.py <scanning.jld2> <yp064_default.csv> <yp064_tol_p1.csv> <yp064_tol_p2.csv> <out.json>
"""
import zlib, json, sys, csv, hashlib, numpy as np
b = open(sys.argv[1], 'rb').read()
streams = []
i = 0
while i < len(b) - 2:
    if b[i] == 0x78 and b[i + 1] in (0x01, 0x5e, 0x9c, 0xda):
        try:
            d = zlib.decompressobj(); out = d.decompress(b[i:]); used = len(b[i:]) - len(d.unused_data)
            if len(out) >= 64:
                streams.append(np.frombuffer(out, '<f8')); i += used; continue
        except Exception:
            pass
    i += 1
m, be = streams[0], streams[1]
Y = [s for s in streams[2:] if s.max() < 2][0]; C = [s for s in streams[2:] if s.max() >= 2][0]
check = {"file_sha256": hashlib.sha256(b).hexdigest(), "Y_min": float(Y.min()), "Y_max": float(Y.max()),
         "n_chi2_le_4": int((C <= 4).sum()), "chi2_formula_max_resid": float(np.max(np.abs(((Y - 0.245) / 0.003) ** 2 - C)))}
F = Y.reshape((100, 100), order='F')
lb_arch = np.log10(be); row = F[22]
def load(paths, ids):
    rows = []
    for p in paths:
        rows += [r for r in csv.DictReader(l for l in open(p) if not l.startswith('#')) if r['id'] in ids]
    pts = sorted((float(r['log10beta']), float(r['Yc_native'])) for r in rows)
    return np.array([p[0] for p in pts]), np.array([p[1] for p in pts])
xd, yd = load([sys.argv[2]], {'d22d'}); xt, yt = load([sys.argv[3], sys.argv[4]], {'d22t_a', 'd22t_b'})
sel = (lb_arch >= xd.min() - 1e-9) & (lb_arch <= xd.max() + 1e-9)
cmp = []
for k in np.where(sel)[0]:
    cmp.append({"k": int(k), "log10beta": float(lb_arch[k]), "Y_archive": float(row[k]),
                "Y_native_default_interp": float(np.interp(lb_arch[k], xd, yd)), "Y_native_1e-4_interp": float(np.interp(lb_arch[k], xt, yt))})
dd = np.array([c["Y_archive"] - c["Y_native_default_interp"] for c in cmp]); dt = np.array([c["Y_archive"] - c["Y_native_1e-4_interp"] for c in cmp])
def root_lin(x, y, thr=0.251):
    for i in range(len(x) - 1):
        if y[i] < thr <= y[i + 1]:
            return float(x[i] + (thr - y[i]) * (x[i + 1] - x[i]) / (y[i + 1] - y[i]))
res = {"extraction_check": check, "point_j22_betamax": {"m_g": float(m[22]), "beta": float(be[99]), "Y_archive": float(F[22, 99])},
       "comparison": cmp,
       "diff_archive_minus_default": {"mean": float(dd.mean()), "min": float(dd.min()), "max": float(dd.max()), "n": int(len(dd))},
       "diff_archive_minus_1e-4": {"mean": float(dt.mean()), "min": float(dt.min()), "max": float(dt.max())},
       "root_Y0251": {"archive_row_linear": root_lin(lb_arch, row), "native_default_linear": root_lin(xd, yd), "native_1e-4_linear": root_lin(xt, yt)}}
json.dump(res, open(sys.argv[5], 'w'), indent=1, allow_nan=False)
print(json.dumps({k: v for k, v in res.items() if k != 'comparison'}, indent=1))
for c in cmp:
    print("%.4f  arch %.6f  def %.6f  1e-4 %.6f  d_def %+.2e" % (c["log10beta"], c["Y_archive"], c["Y_native_default_interp"], c["Y_native_1e-4_interp"], c["Y_archive"] - c["Y_native_default_interp"]))
