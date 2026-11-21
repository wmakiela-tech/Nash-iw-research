"""PREREG_085 NET orchestrator (hard-gated). Usage: python3 -I run_net_085.py <patched_repo> <dump_dedup_her> <out_dir> <cfg_dir>
Plan: base (no rates); one run per HERWIG native rates file listed in cfg085_her_{orig,e5}.dat (completeness asserted
against summary_*.csv); V4 (tol_scale 1e-2) and V5 (stride 2) on ho22_1720 and ho62_1940 (grid085.json V45_cases).
Same PRyMordial settings and transfer method as 081/083 (net_rate_079.py). Exits nonzero if any expected ID is missing
or any run fails. Refuses to overwrite an existing net085_raw.jsonl."""
import csv, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))


def ids_from_cfg(cfg_dir):
    ids = []
    for arm in ("orig", "e5"):
        for l in open(os.path.join(cfg_dir, f"cfg085_her_{arm}.dat")):
            s = l.strip()
            if s and not s.startswith("#"):
                ids.append(s.split()[0])
    return ids


def main(repo, dump, out, cfg_dir):
    dst = os.path.join(out, "net085_raw.jsonl")
    if os.path.exists(dst):
        sys.exit("REFUSE_OVERWRITE")
    exp = ids_from_cfg(cfg_dir)
    got = []
    for arm in ("orig", "e5"):
        got += [r["run_id"] for r in csv.DictReader(l for l in open(os.path.join(dump, f"summary_{arm}.csv")) if not l.startswith("#"))]
    if sorted(exp) != sorted(got) or len(set(got)) != len(got):
        sys.exit(f"NATIVE_ID_MISMATCH expected={len(exp)} got={len(got)}")
    for i in exp:
        if not os.path.exists(os.path.join(dump, f"rates_{i}.csv")):
            sys.exit(f"MISSING_RATES {i}")
    vc = json.load(open(os.path.join(cfg_dir, "grid085.json")))["V45_cases"]
    runs = [{"run_id": "net_base", "rates_csv": None}] + [{"run_id": "net_" + i, "rates_csv": os.path.join(dump, f"rates_{i}.csv")} for i in exp]
    for v in vc:
        runs.append({"run_id": f"net_{v}_tol", "rates_csv": os.path.join(dump, f"rates_{v}.csv"), "tol_scale": 1e-2})
        runs.append({"run_id": f"net_{v}_stride2", "rates_csv": os.path.join(dump, f"rates_{v}.csv"), "stride": 2})

    def one(r):
        p = subprocess.run([sys.executable, os.path.join(HERE, "net_rate_079.py"), json.dumps(r)], cwd=repo,
                           capture_output=True, text=True, timeout=3600)
        for line in p.stdout.splitlines():
            if line.startswith("IW079_RESULT "):
                d = json.loads(line[13:]); d["rc"] = p.returncode; return d
        return {"run_id": r["run_id"], "cfg": r, "rc": p.returncode, "error": p.stderr[-3000:]}
    with ThreadPoolExecutor(max_workers=2) as ex:
        res = list(ex.map(one, runs))
    with open(dst, "w") as f:
        for d in res:
            f.write(json.dumps(d) + "\n")
    bad = [d["run_id"] for d in res if d.get("rc") != 0 or "YP_BBN" not in d]
    print("NET085_DONE", len(res), "expected", len(runs), "failed", len(bad), bad)
    sys.exit(1 if (bad or len(res) != len(runs)) else 0)


if __name__ == "__main__":
    main(*sys.argv[1:5])
