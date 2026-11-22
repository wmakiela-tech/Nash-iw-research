"""POST HOC to PREREG_109 (written after analysis109.json; not a preregistered test): discriminating power of the seam (A).
Same N_BH (2 x column sum at the BlackHawk HERWIG row E' = 1e5) compared with Herwig 7.1.5 at E = 1e5 GeV (sqrt(s) = 2e5), i.e.
the alternative 'row label = primary energy' (sqrt(s) = 2E'). Top is absent at E = 1e5 (DEV-2). Same tolerance rule as (A).
Usage: python3 -I posthoc_109.py <herwig_tables_dir> <run_dir> <out.json>"""
import json, math, os, sys
import numpy as np

SP = {"pipm": "211", "Kpm": "321", "K0L": "130", "proton": "2212", "neutron": "2112"}
CH = {"up": "up", "down": "down", "strange": "strange", "charm": "charm", "bottom": "bottom", "top": "top", "gluon": "gluons", "Wpm": "Wpm", "Z0": "Z0", "tau": "tau"}


def main(tdir, run, dst):
    tab = {}
    for name in SP:
        L = open(os.path.join(tdir, name + ".txt")).read().splitlines(); hdr = L[0].split()
        tab[name] = (hdr, np.array([[float(x) for x in l.split()] for l in L[1:]]))
    out = {"cells": {}, "summary": {}}
    hyp = {"label_sqrts_eq_Eprime": 5e4, "alt_sqrts_eq_2Eprime": 1e5}
    for h, E in hyp.items():
        n_g = n_fail = 0; mx = 0.0; Ls = []
        for c, col in CH.items():
            d = json.load(open(os.path.join(run, "mc109", f"herwig71_{c}.json")))
            es = [e for e in d["energies"] if abs(e["E"] - E) < 1 and e.get("rc_run") == 0 and (e.get("events") or 0) > 0]
            if not es:
                out["cells"][f"{h}|{c}"] = "absent"; continue
            e = es[0]
            for s, p in SP.items():
                hdr, a = tab[s]; iu = hdr.index(col); top = a[:, 0].max()
                nbh = float(2 * a[a[:, 0] == top][:, iu].sum()); n71 = e[p]; se = e["se_" + p]
                if not (n71 * e["events"] >= 20 and nbh > 0 and n71 > 0):
                    continue
                L = math.log10(nbh / n71); tol = max(0.04, 4 * se / n71 / math.log(10))
                n_g += 1; n_fail += abs(L) > tol; mx = max(mx, abs(L)); Ls.append(L)
                out["cells"][f"{h}|{c}|{s}"] = {"L": L, "tol": tol, "pass": abs(L) <= tol}
        out["summary"][h] = {"gated": n_g, "fail": n_fail, "max_abs_L": mx, "median_L": float(np.median(Ls))}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps(out["summary"]))


if __name__ == "__main__":
    main(*sys.argv[1:4])
