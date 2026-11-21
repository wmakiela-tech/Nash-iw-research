"""PREREG_079 NET arm: one PRyMordial run (patched copy, cwd) with native Wu-Xu hadronic conversion rates.

Usage (cwd = patched repo): python3 net_rate_079.py '<json>'
json: run_id, rates_csv (path or null for no rates), stride (1 default; 2 = every 2nd native point, V5),
      tol_scale (1.0 default; V4), eta (6.1e-10).
Rates are matched by temperature: PRyMordial photon T [MeV] <-> authors' T_SM [MeV]; linear interpolation of
r(T) on log T over the authors' output points, zero outside their range.
"""
import csv, json, math, os, sys, time
import numpy as np

cfg = json.loads(sys.argv[1])
sys.path.insert(0, os.getcwd())
import PRyM.PRyM_init as PRyMini  # noqa: E402

PRyMini.verbose_flag = False
PRyMini.julia_flag = False
PRyMini.smallnet_flag = True
PRyMini.eta0b = float(cfg.get("eta", 6.1e-10))
PRyMini.iw077_tol_scale = float(cfg.get("tol_scale", 1.0))
PRyMini.iw077_kick = None
info = {}
if cfg.get("rates_csv"):
    rows = list(csv.DictReader(open(cfg["rates_csv"])))[:: int(cfg.get("stride", 1))]
    T = np.array([float(r["T_MeV"]) for r in rows]); p2n = np.array([float(r["r_p2n"]) for r in rows])
    n2p = np.array([float(r["r_n2p"]) for r in rows])
    o = np.argsort(T); lT = np.log(T[o]); p2n = p2n[o]; n2p = n2p[o]
    assert np.all(np.diff(lT) > 0), "T not strictly monotone"
    PRyMini.iw079_rate_p2n = lambda TM: float(np.interp(math.log(TM), lT, p2n, left=0.0, right=0.0))
    PRyMini.iw079_rate_n2p = lambda TM: float(np.interp(math.log(TM), lT, n2p, left=0.0, right=0.0))
    info = {"n_points": len(rows), "T_min": float(T.min()), "T_max": float(T.max()),
            "max_r_p2n_below_10MeV": float(p2n[lT < math.log(10.0)].max(initial=0.0)),
            "max_r_n2p_below_10MeV": float(n2p[lT < math.log(10.0)].max(initial=0.0))}
t0 = time.time()
import PRyM.PRyM_main as PRyMmain  # noqa: E402
res = PRyMmain.PRyMclass().PRyMresults()
print("IW079_RESULT " + json.dumps({"run_id": cfg.get("run_id"), "cfg": cfg, "YP_BBN": float(res[4]),
                                     "DH_e5": float(res[5]), "rates_info": info, "seconds": time.time() - t0}))
