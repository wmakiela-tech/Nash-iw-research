"""NOTE_111: does the BlackHawk HERWIG BBN-table defect (REVIEW_098/106: rows generated at sqrt(s) = E') persist in BlackHawk v3.0?
Decision rule (REC13 ROT021 / EKS1 ROT023, fixed before this run): per-file SHA-256 of the members under
src/tables/hadronization_tables/herwig_tables/ in the official v2.3 and v3.0 archives (blackhawk.hepforge.org) ->
SAME_CATALOG_BYTES (same file names, all hashes equal) / DIFFERENT_CATALOG_BYTES / ACCESS_OR_CATALOG_HOLD (missing directory).
Also reported, descriptively: the same comparison for pythia_tables and for every other member whose path contains 'herwig'
or 'hadronization' (headers and readers of the tables). Archives are read as data only (tarfile streaming, nothing extracted).
Usage: python3 -I compare_bh_tables_111.py <v2.3.tar.bz2> <v3.0.tar.bz2> <out.json>"""
import hashlib, json, sys, tarfile


def catalog(path):
    out = {}
    with tarfile.open(path, "r:bz2") as t:
        for m in t:
            if not m.isreg():
                continue
            p = m.name.split("/", 1)[1] if "/" in m.name else m.name
            if "hadronization" in p or "herwig" in p.lower():
                f = t.extractfile(m); h = hashlib.sha256(f.read()).hexdigest()
                out[p] = {"sha256": h, "size": m.size}
    return out


def cmp(a, b, pref):
    A = {k: v for k, v in a.items() if k.startswith(pref)}; B = {k: v for k, v in b.items() if k.startswith(pref)}
    if not A or not B:
        return {"verdict": "ACCESS_OR_CATALOG_HOLD", "n_v23": len(A), "n_v30": len(B)}
    same = sorted(k for k in A if k in B and A[k]["sha256"] == B[k]["sha256"])
    diff = sorted(k for k in A if k in B and A[k]["sha256"] != B[k]["sha256"])
    only23 = sorted(set(A) - set(B)); only30 = sorted(set(B) - set(A))
    v = "SAME_CATALOG_BYTES" if not diff and not only23 and not only30 else "DIFFERENT_CATALOG_BYTES"
    return {"verdict": v, "n_v23": len(A), "n_v30": len(B), "n_same": len(same), "different": diff, "only_v23": only23, "only_v30": only30}


def main(p23, p30, dst):
    a = catalog(p23); b = catalog(p30)
    T = "src/tables/hadronization_tables/"
    res = {"archives": {}, "herwig_tables": cmp(a, b, T + "herwig_tables/"), "pythia_tables": cmp(a, b, T + "pythia_tables/"),
           "other_members": {}}
    for p in (p23, p30):
        h = hashlib.sha256(open(p, "rb").read()).hexdigest(); res["archives"][p.rsplit("/", 1)[-1]] = h
    rest = sorted(k for k in set(a) | set(b) if not k.startswith(T + "herwig_tables/") and not k.startswith(T + "pythia_tables/")
                  and not k.startswith(T + "hazma_tables/") and not k.startswith(T + "hdmspectra_tables/"))
    for k in rest:
        res["other_members"][k] = {"v23": a.get(k, {}).get("sha256"), "v30": b.get(k, {}).get("sha256"),
                                   "same": a.get(k, {}).get("sha256") == b.get(k, {}).get("sha256")}
    json.dump(res, open(dst, "x"), indent=1)
    print(json.dumps({k: res[k]["verdict"] for k in ("herwig_tables", "pythia_tables")}))
    print(json.dumps({k: v["same"] for k, v in res["other_members"].items()}))


if __name__ == "__main__":
    main(*sys.argv[1:4])
