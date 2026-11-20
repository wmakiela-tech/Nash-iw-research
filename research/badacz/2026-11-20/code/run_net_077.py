"""PREREG_077 NET arm orchestrator: frozen run plan, one fresh subprocess per run, 2 workers.

Usage: python3 -I run_net_077.py <patched_repo_dir> <out_dir>
Writes <out_dir>/net_raw.jsonl (one IW077_RESULT per line, plus rc/stderr tail on failure) and net_status.txt.
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
T_GRID = [3.0, 2.0, 1.5, 1.2, 0.8, 0.6, 0.45, 0.35, 0.25, 0.18, 0.13, 0.105, 0.095, 0.088, 0.082, 0.075, 0.068, 0.06]
ETA = 6.1e-10


def plan():
    runs = [{"run_id": "net_base", "T_MeV": None, "eta": ETA},
            {"run_id": "net_base_large", "T_MeV": None, "eta": ETA, "net": "large"}]
    for T in T_GRID:
        for A in (2e-3, 1e-3):
            for sg in (+1, -1):
                runs.append({"run_id": f"net_T{T}_A{A}_s{sg:+d}", "T_MeV": T, "sign": sg, "A": A, "eta": ETA})
    runs.append({"run_id": "net_tolbase", "T_MeV": None, "eta": ETA, "tol_scale": 1e-2})
    for T in (1.5, 0.45, 0.18, 0.105):
        for sg in (+1, -1):
            runs.append({"run_id": f"net_tol_T{T}_s{sg:+d}", "T_MeV": T, "sign": sg, "A": 2e-3, "eta": ETA, "tol_scale": 1e-2})
    for T in (0.45, 0.13):
        for sg in (+1, -1):
            runs.append({"run_id": f"net_large_T{T}_s{sg:+d}", "T_MeV": T, "sign": sg, "A": 2e-3, "eta": ETA, "net": "large"})
    return runs


def one(repo, r):
    p = subprocess.run([sys.executable, os.path.join(HERE, "net_gain_077.py"), json.dumps(r)], cwd=repo,
                       capture_output=True, text=True, timeout=1800)
    for line in p.stdout.splitlines():
        if line.startswith("IW077_RESULT "):
            d = json.loads(line[len("IW077_RESULT "):]); d["rc"] = p.returncode
            return d
    return {"run_id": r["run_id"], "cfg": r, "rc": p.returncode, "error": p.stderr[-2000:]}


def main(repo, out):
    os.makedirs(out, exist_ok=True)
    runs = plan()
    with ThreadPoolExecutor(max_workers=2) as ex:
        res = list(ex.map(lambda r: one(repo, r), runs))
    with open(os.path.join(out, "net_raw.jsonl"), "w") as f:
        for d in res:
            f.write(json.dumps(d) + "\n")
    bad = [d["run_id"] for d in res if d.get("rc") != 0 or "YP_BBN" not in d]
    open(os.path.join(out, "net_status.txt"), "w").write(f"runs={len(res)} failed={len(bad)} {bad}\n")
    print("NET_DONE", len(res), "failed", len(bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
