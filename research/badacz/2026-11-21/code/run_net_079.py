"""PREREG_079 NET orchestrator. Usage: python3 -I run_net_079.py <patched_repo> <dump_dir> <out_dir>
Plan: base (no rates); one run per native rates_<run_id>.csv listed in summary_{orig,e5}.csv;
V4 (tol_scale 1e-2) and V5 (stride 2) on the two V-cases."""
import csv, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
VCASES = ["o22_n08", "o62_n08"]   # orig nodes nearest the code roots (index 8 of 0..16 T2 grid = centre)

def plan(dump):
    runs = [{"run_id": "net_base", "rates_csv": None}]
    for arm in ("orig", "e5"):
        for r in csv.DictReader(l for l in open(os.path.join(dump, f"summary_{arm}.csv")) if not l.startswith("#")):
            runs.append({"run_id": "net_" + r["run_id"], "rates_csv": os.path.join(dump, f"rates_{r['run_id']}.csv")})
    for v in VCASES:
        runs.append({"run_id": f"net_{v}_tol", "rates_csv": os.path.join(dump, f"rates_{v}.csv"), "tol_scale": 1e-2})
        runs.append({"run_id": f"net_{v}_stride2", "rates_csv": os.path.join(dump, f"rates_{v}.csv"), "stride": 2})
    return runs

def one(repo, r):
    p = subprocess.run([sys.executable, os.path.join(HERE, "net_rate_079.py"), json.dumps(r)], cwd=repo,
                       capture_output=True, text=True, timeout=3600)
    for line in p.stdout.splitlines():
        if line.startswith("IW079_RESULT "):
            d = json.loads(line[13:]); d["rc"] = p.returncode; return d
    return {"run_id": r["run_id"], "cfg": r, "rc": p.returncode, "error": p.stderr[-3000:]}

def main(repo, dump, out):
    os.makedirs(out, exist_ok=True)
    runs = plan(dump)
    with ThreadPoolExecutor(max_workers=2) as ex:
        res = list(ex.map(lambda r: one(repo, r), runs))
    with open(os.path.join(out, "net079_raw.jsonl"), "w") as f:
        for d in res: f.write(json.dumps(d) + "\n")
    bad = [d["run_id"] for d in res if d.get("rc") != 0 or "YP_BBN" not in d]
    print("NET079_DONE", len(res), "failed", len(bad), bad); sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main(*sys.argv[1:4])
