#!/usr/bin/env python3
"""Review-family concentration in the public IW research corpus.

Implements IW_BADACZ_REVIEW_FAMILY_CONCENTRATION_PREREG_001_20261026
(frozen at commit 829aee3298c972baa6f87cff202260364ba2308f) without changing its
definitions. Reads the corpus from git at a pinned commit, so the result does
not depend on the working tree.

Usage (from the repository root):
    python research/badacz/2026-10-26/code/review_family_concentration.py \
        --pin 921360060946b0ed7bdfad2ef5e6b52e2b7e6dd1 --out <dir>

Outputs: nodes.csv, edges.csv, summary.json, recall_sample.json.
No network access, no private data. Python >= 3.9 standard library only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
import subprocess
from collections import defaultdict
from pathlib import Path

PREREG_COMMIT = "829aee3298c972baa6f87cff202260364ba2308f"
EXCLUDE_NAME = re.compile(r"(^README\.md$)|DISPATCH_LEDGER|CLAIM_ROWS", re.I)
EXCLUDE_LINEAGE = {"badacz"}

# Frozen family map (prereg section 3).
FAMILY = {"nc": "CLAUDE", "badacz": "CLAUDE", "rec10": "GPT", "mt13": "GPT",
          "kn11": "GPT", "prf11": "GPT", "lt5": "GPT"}
FAMILY_BASIS = {"nc": "TRANSPORT_LABEL_CLAUDE", "badacz": "THIS_THREAD",
                "rec10": "MODERATOR_20261026", "mt13": "TRANSPORT_LABEL_CHATGPT",
                "kn11": "TRANSPORT_LABEL_CHATGPT", "prf11": "TRANSPORT_LABEL_CHATGPT",
                "lt5": "TRANSPORT_LABEL_CHATGPT"}
TRAILING_NUMBER_LINEAGES = {"nc", "xh-s3", "xh-s4"}


def family(lineage: str) -> str:
    return FAMILY.get(lineage, "GPT_ASSUMED")


def family_class(lineage: str) -> str:
    """GPT_ASSUMED counts as GPT for contact (prereg section 3)."""
    f = family(lineage)
    return "GPT" if f == "GPT_ASSUMED" else f


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], check=True, capture_output=True).stdout


def load_corpus(pin: str):
    listing = git("ls-tree", "-r", pin, "research/").decode()
    nodes = []
    for line in listing.splitlines():
        meta, path = line.split("\t", 1)
        _mode, kind, blob = meta.split()
        if kind != "blob" or not path.endswith(".md"):
            continue
        name = path.rsplit("/", 1)[-1]
        lineage = path.split("/")[1].lower()
        if EXCLUDE_NAME.search(name) or lineage in EXCLUDE_LINEAGE:
            continue
        text = git("cat-file", "-p", blob).decode("utf-8", "replace")
        nodes.append({"path": path, "name": name, "lineage": lineage,
                      "blob": blob, "text": text})
    return nodes


def cell_regex(lineage: str) -> str:
    parts = lineage.split("-")
    return r"[-_ ]?".join(re.escape(p) for p in parts)


LABEL_IN_NAME = re.compile(r"(?<![a-z])(?:rotation|rot|thread)[-_]?0*(\d{1,3})(?!\d)")


def label_from_name(node) -> int | None:
    low = node["name"].lower()
    lin = node["lineage"]
    m = LABEL_IN_NAME.search(low)
    if m:
        return int(m.group(1))
    tok = cell_regex(lin).replace(r"[-_ ]?", "[-_]?")
    m = re.search(r"(?<![a-z0-9])" + tok + r"[-_]r0*(\d{1,3})(?!\d)", low)
    if m:
        return int(m.group(1))
    if lin in TRAILING_NUMBER_LINEAGES:
        m = re.search(r"_(\d{3})(?:_\d{8})?\.md$", low)
        if m:
            return int(m.group(1))
    return None


PREFIX = r"(?:rotation|rotacj[aiy]|rot\.?|r|thread|art|nr\.?|#)?"


def label_pattern(lineage: str) -> re.Pattern:
    return re.compile(
        r"(?<![A-Za-z0-9])" + cell_regex(lineage)
        + r"(?:[\s_\-/]*" + PREFIX + r"[\s_\-]*)0*(\d{1,3})(?![0-9])",
        re.I)


IDLINE = re.compile(r"^\s*[-*]?\s*`?(?:artifact_id|RETURN_ID|return_id)`?\s*[:=]\s*`?([A-Za-z0-9_.\-]{15,})",
                    re.M)


def build_aliases(nodes):
    exact = []          # (string, node_index) for stem, ids, blob
    labels = defaultdict(set)  # (lineage, n) -> node indices
    for i, n in enumerate(nodes):
        stem = n["name"][:-3]
        exact.append((stem, i))
        for m in IDLINE.finditer(n["text"][:3500]):
            exact.append((m.group(1), i))
        exact.append((n["blob"], i))
        exact.append((n["blob"][:12], i))
        lab = label_from_name(n)
        n["label"] = lab
        if lab is not None:
            labels[(n["lineage"], lab)].add(i)
    return exact, labels


def find_edges(nodes, exact, labels):
    lineages = sorted({n["lineage"] for n in nodes})
    pats = {lin: label_pattern(lin) for lin in lineages}
    edges = []  # (src, dst, kind, ambiguous)
    for a, na in enumerate(nodes):
        text = na["text"]
        hit = {}
        for s, b in exact:
            if b != a and s in text:
                hit[b] = ("EXACT", False)
        for lin, pat in pats.items():
            for m in pat.finditer(text):
                key = (lin, int(m.group(1)))
                targets = labels.get(key)
                if not targets:
                    continue
                amb = len(targets) > 1
                for b in targets:
                    if b == a:
                        continue
                    if b not in hit or (hit[b][0] == "LABEL" and hit[b][1] and not amb):
                        hit[b] = ("LABEL", amb)
        for b, (kind, amb) in hit.items():
            edges.append((a, b, kind, amb))
    return edges


def analyse(nodes, edges, variant: str):
    use = [(a, b) for a, b, kind, amb in edges if variant == "A" or not amb]
    src_lineages = defaultdict(set)
    cross = defaultdict(set)
    for a, b in use:
        la, lb = nodes[a]["lineage"], nodes[b]["lineage"]
        if la != lb:
            src_lineages[b].add(la)
        if family_class(la) != family_class(lb):
            cross[b].add(la)
    rows = []
    for i, n in enumerate(nodes):
        rows.append({"idx": i, "path": n["path"], "lineage": n["lineage"],
                     "family": family(n["lineage"]),
                     "centrality": len(src_lineages[i]),
                     "citing_lineages": sorted(src_lineages[i]),
                     "cross_family_contact": bool(cross[i]),
                     "cross_family_sources": sorted(cross[i]),
                     "assumed_family_among_citers": sorted(l for l in src_lineages[i]
                                                           if family(l) == "GPT_ASSUMED")})
    return rows


def top20(rows, claude: bool):
    pool = [r for r in rows if (r["family"] == "CLAUDE") == claude]
    pool.sort(key=lambda r: (-r["centrality"], r["path"]))
    if len(pool) <= 20:
        return pool
    cut = pool[19]["centrality"]
    return [r for r in pool if r["centrality"] >= cut]


def h1(rows):
    top = top20(rows, claude=False)
    no_contact = sum(1 for r in top if not r["cross_family_contact"])
    return {"top_size": len(top), "no_cross_family_contact": no_contact,
            "fraction": round(no_contact / len(top), 4) if top else None,
            "h1_supported": (no_contact > 10) if len(top) == 20 else (no_contact / len(top) > 0.5),
            "top": [{k: r[k] for k in ("path", "lineage", "centrality", "cross_family_contact",
                                       "cross_family_sources", "citing_lineages",
                                       "assumed_family_among_citers")} for r in top]}


def symmetry(rows):
    pool = [r for r in rows if r["family"] == "CLAUDE" and r["centrality"] > 0]
    with_gpt = sum(1 for r in pool if r["cross_family_contact"])
    allc = [r for r in rows if r["family"] == "CLAUDE"]
    return {"claude_nodes": len(allc), "claude_nodes_cited_by_other_lineages": len(pool),
            "of_which_with_gpt_contact": with_gpt}


def weak_roots(rows):
    cands = [r for r in rows if r["family"] != "CLAUDE" and r["centrality"] >= 3
             and not r["cross_family_contact"]]
    cands.sort(key=lambda r: (-r["centrality"], r["path"]))
    return cands


LIBERAL = None


def recall_sample(nodes, seed=20261026, k=12):
    nc_paths = sorted(n["path"] for n in nodes if n["lineage"] == "nc")
    rng = random.Random(seed)
    return rng.sample(nc_paths, k)


def liberal_mentions(text, lineages):
    tokens = "|".join(sorted((cell_regex(l) for l in lineages), key=len, reverse=True))
    pat = re.compile(r"(?<![A-Za-z0-9])(" + tokens + r")(?![A-Za-z0-9])[^\n]{0,20}?\d+", re.I)
    out = []
    for m in pat.finditer(text):
        s = max(0, m.start() - 30)
        out.append({"span": m.group(0), "context": text[s:m.end() + 40].replace("\n", " ")})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pin", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    nodes = load_corpus(args.pin)
    exact, labels = build_aliases(nodes)
    edges = find_edges(nodes, exact, labels)

    with open(out / "edges.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["src", "dst", "kind", "ambiguous_label"])
        for a, b, kind, amb in sorted(edges, key=lambda e: (nodes[e[0]]["path"], nodes[e[1]]["path"])):
            w.writerow([nodes[a]["path"], nodes[b]["path"], kind, int(amb)])

    res = {}
    for var in ("A", "B"):
        rows = analyse(nodes, edges, var)
        res[var] = {"h1": h1(rows), "symmetry": symmetry(rows),
                    "weak_root_candidates": [{k: r[k] for k in ("path", "lineage", "centrality",
                                                                "citing_lineages",
                                                                "assumed_family_among_citers")}
                                             for r in weak_roots(rows)]}
        if var == "B":
            with open(out / "nodes.csv", "w", newline="") as fh:
                w = csv.writer(fh)
                w.writerow(["path", "lineage", "family", "label", "centrality_B",
                            "cross_family_contact_B", "citing_lineages_B"])
                for r in sorted(rows, key=lambda r: r["path"]):
                    w.writerow([r["path"], r["lineage"], r["family"], nodes[r["idx"]]["label"],
                                r["centrality"], int(r["cross_family_contact"]),
                                ";".join(r["citing_lineages"])])

    lineages = sorted({n["lineage"] for n in nodes})
    sample = recall_sample(nodes)
    by_path = {n["path"]: i for i, n in enumerate(nodes)}
    detected = defaultdict(list)
    for a, b, kind, amb in edges:
        detected[nodes[a]["path"]].append({"dst": nodes[b]["path"], "kind": kind, "ambiguous": amb})
    recall = [{"file": p, "detected": sorted(detected[p], key=lambda d: d["dst"]),
               "liberal_mentions": liberal_mentions(nodes[by_path[p]]["text"], lineages)}
              for p in sample]
    (out / "recall_sample.json").write_text(json.dumps(recall, indent=1, ensure_ascii=False))

    summary = {
        "prereg_commit": PREREG_COMMIT,
        "corpus_pin": args.pin,
        "n_nodes": len(nodes),
        "n_edges_total": len(edges),
        "n_edges_ambiguous": sum(1 for e in edges if e[3]),
        "nodes_by_family": {f: sum(1 for n in nodes if family(n["lineage"]) == f)
                            for f in ("CLAUDE", "GPT", "GPT_ASSUMED")},
        "nodes_with_label": sum(1 for n in nodes if n["label"] is not None),
        "family_basis": FAMILY_BASIS,
        "variants": res,
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    for var in ("A", "B"):
        h = res[var]["h1"]
        print(f"variant {var}: top={h['top_size']} no_cross_contact={h['no_cross_family_contact']} "
              f"fraction={h['fraction']} H1_supported={h['h1_supported']} "
              f"weak_root_candidates={len(res[var]['weak_root_candidates'])} "
              f"symmetry={res[var]['symmetry']}")
    print(f"nodes={len(nodes)} edges={len(edges)} ambiguous={summary['n_edges_ambiguous']}")


if __name__ == "__main__":
    main()
