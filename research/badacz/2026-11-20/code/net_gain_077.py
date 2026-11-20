"""PREREG_077 NET arm: one PRyMordial run (patched copy) with an optional neutron kick.

Usage (cwd MUST be the patched repo copy, PRyM reads tables from os.getcwd()):
  python3 net_gain_077.py '<json>'
json keys: run_id, T_MeV (or null for no kick), sign (+1/-1), A (fluence), tol_scale (1.0 default),
           net ("small" default | "large"), eta (6.1e-10 default)
Prints one JSON line with YP_BBN (= 4*Y_He4, PRyMordial res[4]), D/H, and the kick log.
"""
import json, os, sys, time

cfg = json.loads(sys.argv[1])
sys.path.insert(0, os.getcwd())
import PRyM.PRyM_init as PRyMini  # noqa: E402

PRyMini.verbose_flag = False
PRyMini.julia_flag = False
PRyMini.smallnet_flag = (cfg.get("net", "small") == "small")
PRyMini.eta0b = float(cfg.get("eta", 6.1e-10))
PRyMini.iw077_tol_scale = float(cfg.get("tol_scale", 1.0))
kick = None
if cfg.get("T_MeV") is not None:
    kick = {"T_MeV": float(cfg["T_MeV"]), "sign": int(cfg["sign"]), "A": float(cfg["A"])}
PRyMini.iw077_kick = kick

t0 = time.time()
import PRyM.PRyM_main as PRyMmain  # noqa: E402
res = PRyMmain.PRyMclass().PRyMresults()
out = {"run_id": cfg.get("run_id"), "cfg": cfg, "YP_BBN": float(res[4]), "YP_CMB": float(res[3]),
       "DH_e5": float(res[5]), "Neff": float(res[0]), "kick_log": (kick or {}).get("log"),
       "kick_applied": bool(kick and kick.get("log")), "seconds": time.time() - t0}
print("IW077_RESULT " + json.dumps(out))
