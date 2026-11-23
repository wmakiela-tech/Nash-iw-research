"""NOTE_114 r2 (O1, version archaeology of the BlackHawk BBN hadronization tables). For one official archive: SHA-256 of
the archive; per-file identity of the HERWIG and PYTHIA BBN tables with the v2.3 reference directory (paths:
src/tables/herwig_tables/ in v1.x, src/tables/hadronization_tables/herwig_tables/ from v2.0); identity of the HERWIG
generator recipe scripts/herwig_scripts/up/{LEP.in, main.cpp} with v2.3; the LuminosityFunction line of up/LEP.in; and,
descriptively, log10 of the per-primary charged-pion multiplicity of the 'up' column (sum over final energies) of this
version's PYTHIA table over the v2.3 one at 11 initial energies. Archives are read as data only (tarfile streaming).
Usage: python3 -I bh_versions_herwig_114.py <archive.tar.bz2> <v2.3 hadronization_tables dir> <v2.3 herwig_scripts dir> <out.json>"""
import hashlib, io, json, os, sys, tarfile
import numpy as np


def tot(raw, col):
    L = raw.decode().splitlines()
    if L and L[0].startswith("<<<<<<<"):  # v2.0 ships git merge-conflict markers; the HEAD block (up to '=======') is read
        L = L[1:L.index("=======")]
    hdr = L[0].split(); a = np.array([[float(x) for x in l.split()] for l in L[1:] if l.strip()])
    Ei = np.unique(a[:, 0]); ic = hdr.index(col)
    return Ei, np.array([a[a[:, 0] == e, ic].sum() for e in Ei])


def main(arc, ref, refscripts, dst):
    out = {"archive": os.path.basename(arc), "archive_sha256": hashlib.sha256(open(arc, "rb").read()).hexdigest(),
           "herwig_tables": {"same": [], "different": []}, "pythia_tables": {"same": [], "different": []}, "scripts": {}}
    pip = None
    with tarfile.open(arc, "r:bz2") as t:
        for m in t:
            if not m.isreg() or "/" not in m.name:
                continue
            p = m.name.split("/", 1)[1]; b = os.path.basename(p)
            for kind in ("herwig_tables", "pythia_tables"):
                if (p.startswith(f"src/tables/{kind}/") or p.startswith(f"src/tables/hadronization_tables/{kind}/")) and b.endswith(".txt") \
                        and b != "infos.txt" and "/old/" not in p:
                    raw = t.extractfile(m).read(); r = os.path.join(ref, kind, b)
                    same = os.path.exists(r) and raw == open(r, "rb").read()
                    out[kind]["same" if same else "different"].append(b)
                    if kind == "pythia_tables" and b == "pipm.txt":
                        pip = raw
                    if any(l.startswith(("<<<<<<<", "=======", ">>>>>>>")) for l in raw.decode(errors="replace").splitlines()):
                        out.setdefault("conflict_markers", []).append(f"{kind}/{b}")
            if p in ("scripts/herwig_scripts/up/LEP.in", "scripts/herwig_scripts/up/main.cpp"):
                raw = t.extractfile(m).read(); r = os.path.join(refscripts, "up", b)
                out["scripts"][b] = {"same_as_v23": raw == open(r, "rb").read(), "sha256": hashlib.sha256(raw).hexdigest()}
                if b == "LEP.in":
                    out["scripts"]["LEP.in_energy_line"] = [l for l in raw.decode().splitlines() if "LuminosityFunction:Energy" in l]
    for k in ("herwig_tables", "pythia_tables"):
        out[k] = {kk: sorted(v) for kk, v in out[k].items()}
    if pip is not None:
        E1, N1 = tot(pip, "up"); E2, N2 = tot(open(os.path.join(ref, "pythia_tables", "pipm.txt"), "rb").read(), "up")
        pts = [5, 10, 20, 50, 100, 300, 1000, 3000, 1e4, 3e4, 1e5]
        out["pythia_pipm_up_log10_ratio_to_v23"] = {f"{E1[np.argmin(abs(E1 - e))]:.4g}": float(np.log10(N1[np.argmin(abs(E1 - e))] / N2[np.argmin(abs(E2 - e))])) for e in pts}
    json.dump(out, open(dst, "x"), indent=1, sort_keys=True)
    print(out["archive"], out["archive_sha256"][:16], "HERWIG same/diff", len(out["herwig_tables"]["same"]), len(out["herwig_tables"]["different"]),
          "PYTHIA same/diff", len(out["pythia_tables"]["same"]), len(out["pythia_tables"]["different"]), {k: v.get("same_as_v23") for k, v in out["scripts"].items() if isinstance(v, dict)})


if __name__ == "__main__":
    main(*sys.argv[1:5])
