"""REVIEW_104 POST-HOC (not preregistered; PREREG_103 ended GATE_FAIL_NO_LABEL on G_BASE): background fraction at the hadronic
thresholds with the reference taken as the mean of the arm-z nodes at log10 beta <= -18.5 (instead of the outlying z base).
Usage: python3 -I posthoc_103.py <analysis103.json> <analysis090.json> <summary_orig_083.csv> <out.json>"""
import csv, json, sys
import numpy as np
a, A, o, dst = sys.argv[1:5]
d = json.load(open(a)); A = json.load(open(A)); o = {r["run_id"]: r for r in csv.DictReader(l for l in open(o) if not l.startswith("#"))}
X = lambda Y: Y / (2 + Y); out = {"label": "POST_HOC_NOT_PREREGISTERED", "masses": {}}
for j in ("22", "62"):
    m = d["masses"][j]; lb = np.array(m["lb"]); Y = np.array(m["Y"]); ref = Y[lb <= -18.5]
    r = {"Yref_mean": float(ref.mean()), "Yref_sd": float(ref.std(ddof=1)), "n_ref": int(len(ref)), "base_z": None, "f": {}, "crossings": m["crossings"]}
    for t in (0.251, 0.2484):
        lr = A["roots"][f"PYBH_{j}|code|{t}"]["lb"]; yz = float(np.interp(lr, lb, Y)); full = X(t) - X(float(o[f"o{j}_base"]["Y"]))
        r["f"][str(t)] = {"lb_PYBH": lr, "Yz": yz, "f": (X(yz) - X(ref.mean())) / full, "f_noise_1sd": (X(ref.mean() + ref.std(ddof=1)) - X(ref.mean())) / full,
                          "gap_dex_to_bg_crossing": (m["crossings"][str(t)] - lr) if isinstance(m["crossings"][str(t)], float) else None}
    out["masses"][j] = r
json.dump(out, open(dst, "x"), indent=1); print(json.dumps(out, indent=1)[:1500])
