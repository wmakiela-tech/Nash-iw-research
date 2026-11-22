"""PREREG_101 NET orchestrator (hard-gated). Usage: python3 -I run_net_101.py <patched_repo> <run_dir> <cfg_dir>
Runs: net_base (no rates) + one PRyMordial run per native run listed in cfg101_{k,v,e}.dat, rates from
<run_dir>/dd_<arm>/rates_<id>.csv. Same settings and transfer as 079/081/083/090/094 (frozen net_rate_079.py).
Completeness asserted against dd_<arm>/summary_orig.csv. Exit nonzero on any missing ID or failed run; refuses to overwrite."""
import csv, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
NET = os.path.join(HERE, "..", "..", "2026-11-21", "code", "net_rate_079.py")
ARMS = "kve"


def main(repo, run, cfg_dir):
    dst = os.path.join(run, "out", "net101_raw.jsonl")
    if os.path.exists(dst):
        sys.exit("REFUSE_OVERWRITE")
    runs = [{"run_id": "net_base", "rates_csv": None}]
    for a in ARMS:
        exp = [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg101_{a}.dat")) if l.strip() and not l.startswith("#")]
        got = [r["run_id"] for r in csv.DictReader(l for l in open(os.path.join(run, f"dd_{a}", "summary_orig.csv")) if not l.startswith("#"))]
        if sorted(exp) != sorted(got) or len(set(got)) != len(got):
            sys.exit(f"NATIVE_ID_MISMATCH arm={a} expected={len(exp)} got={len(got)}")
        for i in exp:
            p = os.path.join(run, f"dd_{a}", f"rates_{i}.csv")
            if not os.path.exists(p):
                sys.exit(f"MISSING_RATES {i}")
            runs.append({"run_id": "net_" + i, "rates_csv": p})

    def one(r):
        p = subprocess.run([sys.executable, NET, json.dumps(r)], cwd=repo, capture_output=True, text=True, timeout=3600)
        for line in p.stdout.splitlines():
            if line.startswith("IW079_RESULT "):
                d = json.loads(line[13:]); d["rc"] = p.returncode; return d
        return {"run_id": r["run_id"], "cfg": r, "rc": p.returncode, "error": p.stderr[-3000:]}
    with ThreadPoolExecutor(max_workers=2) as ex:
        res = list(ex.map(one, runs))
    with open(dst, "x") as f:
        for d in res:
            f.write(json.dumps(d) + "\n")
    bad = [d["run_id"] for d in res if d.get("rc") != 0 or "YP_BBN" not in d]
    print("NET101_DONE", len(res), "expected", len(runs), "failed", len(bad), bad)
    sys.exit(1 if (bad or len(res) != len(runs)) else 0)


if __name__ == "__main__":
    main(*sys.argv[1:4])
