"""PREREG_097 fingerprint of the BlackHawk v2.3 HERWIG BBN tables (DIR-009 step 1, own action).
Same counting as mult_herwig_090r.py (copied below with three changes): (1) version label from argv; (2) sqrt(s) =
FACTOR x E with FACTOR from argv (BlackHawk's archived herwig_scripts/*/main.cpp writes LuminosityFunction:Energy = E,
i.e. FACTOR = 1; the manual's convention and our 090 runs use FACTOR = 2); (3) energy-closure uses sqrt(s).
Usage: python3 mult_herwig_097.py <herwig_bin> <version> <primary> <out.json> <seed> <workdir> <E1:N1,...> <FACTOR>
--- original docstring of mult_herwig_090r.py follows ---
PREREG_090 r2 replicate variant (AUD3 ROT006 F1/F2): identical physics; adds eventwise max |E_final/2E - 1|.
Original docstring follows.
PREREG_090: per-event multiplicities of BBN-epoch hadrons for one BlackHawk primary with Herwig 7.3.0 (conda-forge).
Hard processes copied from BlackHawk v2.3 scripts/herwig_scripts/<primary>/LEP.in (EECollider snippet, e+- NoPDF,
LuminosityFunction:Energy = 2E); MEee2Higgs2SM created explicitly (absent from the 7.3 default repository).
Stable set = Herwig 7.3 defaults (mu, pi+-, K+-, n stable; K0L stable; K0S and hyperons decayed; checked per energy).
Counting from HepMC2 output, final-state (status 1) particles by |PDG id|.
Usage: python3 mult_herwig_090.py <herwig_bin> <primary> <out.json> <seed> <workdir> <E1:N1,...>"""
import json, math, os, subprocess, sys, time

ME = {
    "gluon": ["create Herwig::MEee2Higgs2SM MEee2Higgs2SM HwMELepton.so", "insert SubProcess:MatrixElements[0] MEee2Higgs2SM", "set MEee2Higgs2SM:Allowed Gluon"],
    "higgs": ["create Herwig::MEee2Higgs2SM MEee2Higgs2SM HwMELepton.so", "insert SubProcess:MatrixElements[0] MEee2Higgs2SM", "set MEee2Higgs2SM:Allowed All"],
    "Wpm": ["insert SubProcess:MatrixElements[0] MEee2VV", "set MEee2VV:Process WW"],
    "Z0": ["insert SubProcess:MatrixElements[0] MEee2VV", "set MEee2VV:Process ZZ"],
    "tau": ["insert SubProcess:MatrixElements[0] MEee2gZ2ll", "set MEee2gZ2ll:Allowed Tau"],
    "up": ["insert SubProcess:MatrixElements 0 MEee2gZ2qq", "set MEee2gZ2qq:MinimumFlavour 2", "set MEee2gZ2qq:MaximumFlavour 2"],
    "down": ["insert SubProcess:MatrixElements 0 MEee2gZ2qq", "set MEee2gZ2qq:MinimumFlavour 1", "set MEee2gZ2qq:MaximumFlavour 1"],
    "strange": ["insert SubProcess:MatrixElements 0 MEee2gZ2qq", "set MEee2gZ2qq:MinimumFlavour 3", "set MEee2gZ2qq:MaximumFlavour 3"],
    "charm": ["insert SubProcess:MatrixElements 0 MEee2gZ2qq", "set MEee2gZ2qq:MinimumFlavour 4", "set MEee2gZ2qq:MaximumFlavour 4"],
    "bottom": ["insert SubProcess:MatrixElements 0 MEee2gZ2qq", "set MEee2gZ2qq:MinimumFlavour 5", "set MEee2gZ2qq:MaximumFlavour 5"],
    "top": ["insert SubProcess:MatrixElements 0 MEee2gZ2qq", "set MEee2gZ2qq:MinimumFlavour 6", "set MEee2gZ2qq:MaximumFlavour 6"],
}
IDS = [211, 321, 130, 2212, 2112, 310, 3122, 3222, 3112, 3312, 3322, 3334]
hw, ver, prim, dst, seed, work, spec, FAC = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), sys.argv[6], sys.argv[7], float(sys.argv[8])
os.makedirs(work, exist_ok=True)
out = {"generator": "Herwig", "version": ver, "primary": prim, "sqrt_s_factor": FAC, "energies": []}
for item in spec.split(","):
    E, N = float(item.split(":")[0]), int(item.split(":")[1])
    tag = f"{prim}_{E:g}"
    lines = ["read snippets/EECollider.in", "set /Herwig/Particles/e+:PDF /Herwig/Partons/NoPDF",
             "set /Herwig/Particles/e-:PDF /Herwig/Partons/NoPDF", "cd /Herwig/MatrixElements"] + ME[prim] + [
             "cd /Herwig/Generators", f"set EventGenerator:EventHandler:LuminosityFunction:Energy {FAC * E}",
             "read snippets/HepMC.in", f"set /Herwig/Analysis/HepMC:Filename {tag}.hepmc",
             "set /Herwig/Analysis/HepMC:PrintEvent 100000000", f"saverun {tag} EventGenerator"]
    open(os.path.join(work, f"{tag}.in"), "w").write("\n".join(lines) + "\n")
    t0 = time.time()
    r1 = subprocess.run([hw, "read", f"{tag}.in"], cwd=work, capture_output=True, text=True)
    r2 = subprocess.run([hw, "run", f"{tag}.run", "-N", str(N), "-s", str(seed)], cwd=work, capture_output=True, text=True)
    hp = os.path.join(work, f"{tag}.hepmc")
    rec = {"E": E, "rc_read": r1.returncode, "rc_run": r2.returncode}
    if r1.returncode or r2.returncode or not os.path.exists(hp):
        rec["error"] = (r1.stderr + r2.stderr)[-1500:]; out["energies"].append(rec); print(prim, E, "FAILED", flush=True); continue
    s1 = {i: 0.0 for i in IDS}; s2 = {i: 0.0 for i in IDS}; n = 0; c = None; ef = 0.0; esum = 0.0
    emax = 0.0
    def close():
        global n, esum, emax
        if c is not None:
            n += 1; esum += ef / (FAC * E); emax = max(emax, abs(ef / (FAC * E) - 1))
            for i in IDS:
                s1[i] += c[i]; s2[i] += c[i] * c[i]
    with open(hp) as f:
        for l in f:
            if l.startswith("E "):
                close(); c = {i: 0 for i in IDS}; ef = 0.0
            elif l.startswith("P "):
                t = l.split()
                if t[8] == "1":
                    ef += float(t[6]); a = abs(int(t[2]))
                    if a in c:
                        c[a] += 1
    close()
    rec.update({"events": n, "seconds": time.time() - t0, "Efinal_over_sqrts": esum / max(n, 1), "max_abs_event_Eresidual": emax})
    for i in IDS:
        m = s1[i] / n; v = max(s2[i] / n - m * m, 0.0)
        rec[str(i)] = m; rec[f"se_{i}"] = math.sqrt(v / n)
    out["energies"].append(rec)
    for fn in os.listdir(work):
        if fn.startswith(tag + ".") or fn.startswith(tag + "-"):
            os.remove(os.path.join(work, fn))
    print(prim, E, n, round(rec["seconds"], 1), flush=True)
json.dump(out, open(dst, "x"), indent=1)
