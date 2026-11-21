"""PREREG_090: per-event multiplicities of BBN-epoch hadrons for one BlackHawk primary with PYTHIA 8.3 (pythia8mc).
Processes copied from BlackHawk v2.3 scripts/pythia_scripts/table_<primary>.cc (e+e- at eCM = 2E, ISR off,
pTHatMin 0) plus PDF:lepton = off (no radiative return; see PREREG_090 sec. 1). Stable set = PYTHIA defaults
(pi+-, K+-, K0L, mu, n not decayed; K0S and hyperons decayed), asserted at start.
Usage: python3 mult_pythia_090.py <primary> <out.json> <seed> <E1:N1,E2:N2,...>
Output: per energy: events, mean and standard error per event of |id| in {211,321,130,2212,2112}, plus K0S/Lambda checks."""
import json, math, sys, time
import pythia8mc as p8

PROC = {
    "gluon": ["HiggsSM:ffbar2H = on", "25:onMode = off", "25:onIfAny = 21"],
    "higgs": ["HiggsSM:ffbar2H = on"],
    "Wpm": ["WeakDoubleBoson:ffbar2WW = on"],
    "Z0": ["HiggsSM:ffbar2H = on", "25:onMode = off", "25:onIfAny = 23"],
    "tau": ["HiggsSM:ffbar2H = on", "25:onMode = off", "25:onIfAny = 15"],
    "up": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on", "23:onMode = off", "23:onIfAny = 2"],
    "down": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on", "23:onMode = off", "23:onIfAny = 1"],
    "strange": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on", "23:onMode = off", "23:onIfAny = 3"],
    "charm": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on", "23:onMode = off", "23:onIfAny = 4"],
    "bottom": ["WeakSingleBoson:ffbar2ffbar(s:gmZ) = on", "23:onMode = off", "23:onIfAny = 5"],
    "top": ["Top:ffbar2ttbar(s:gmZ) = on"],
}
IDS = [211, 321, 130, 2212, 2112, 310, 3122]
prim, dst, seed, spec = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
out = {"generator": "PYTHIA", "version": p8.__version__ if hasattr(p8, "__version__") else "8.318", "primary": prim, "energies": []}
for item in spec.split(","):
    E, N = float(item.split(":")[0]), int(item.split(":")[1])
    py = p8.Pythia("", False)
    for s in ["Beams:idA = 11", "Beams:idB = -11", "PhaseSpace:pTHatMin = 0.", "PartonLevel:ISR = off", "PDF:lepton = off",
              f"Beams:eCM = {2 * E}", "Random:setSeed = on", f"Random:seed = {seed}", "Next:numberCount = 0",
              "Next:numberShowEvent = 0", "Next:numberShowProcess = 0", "Next:numberShowInfo = 0"] + PROC[prim]:
        assert py.readString(s), s
    pd = py.particleData
    assert not any(pd.mayDecay(i) for i in (211, 321, 130, 13, 2112)) and all(pd.mayDecay(i) for i in (310, 3122, 3222, 3112, 3312, 3322, 3334))
    if not py.init():
        out["energies"].append({"E": E, "init_failed": True}); continue
    s1 = {i: 0.0 for i in IDS}; s2 = {i: 0.0 for i in IDS}; n = 0; fail = 0; t0 = time.time(); esum = 0.0
    while n < N and fail < 10 * N:
        if not py.next():
            fail += 1; continue
        n += 1; c = {i: 0 for i in IDS}; ef = 0.0
        ev = py.event
        for k in range(ev.size()):
            q = ev[k]
            if q.isFinal():
                ef += q.e(); a = abs(q.id())
                if a in c:
                    c[a] += 1
        esum += ef / (2 * E)
        for i in IDS:
            s1[i] += c[i]; s2[i] += c[i] * c[i]
    rec = {"E": E, "events": n, "failed": fail, "seconds": time.time() - t0, "Efinal_over_2E": esum / max(n, 1)}
    for i in IDS:
        m = s1[i] / n; v = max(s2[i] / n - m * m, 0.0)
        rec[str(i)] = m; rec[f"se_{i}"] = math.sqrt(v / n)
    out["energies"].append(rec)
    print(prim, E, n, round(rec["seconds"], 1), flush=True)
json.dump(out, open(dst, "x"), indent=1)
