#!/usr/bin/env python3
"""Badacz (Claude): PREREG_041 part B (commit ad6ab99) - PYTHIA 8 pilot for hadron multiplicities of parton jets
from 1 TeV to 30 PeV and the implied temperature scaling of the PBH hadron emission rate below 1e9 g (E4-lite).

Generator: PYTHIA 8.318 (PyPI pythia8mc). ProcessLevel off; a back-to-back parton pair (q qbar for q = d,u,s,c,b, or g g)
is put into the event record, showered with forceTimeShower and hadronized. Stable: pi+-, K+-, K0_L, n, mu (p is stable).
Counted per parton (event total / 2): pi+- (211), K+- (321), K0_L (130), p+pbar (2212), n+nbar (2112).
Hawking convolution (geometric-optics shape, no spin-dependent greybody factors):
  <n>_T = int x^2 f(x) n(xT) dx / int x^2 f(x) dx, f = 1/(e^x+1) (quarks) or 1/(e^x-1) (gluons);
  R_i(T) ~ T [w_q <n_iq>_T + w_g <n_ig>_T], w_q = 72 * 1.5 zeta(3), w_g = 16 * 2 zeta(3).
  slope s_i(T) = d ln R_i / d ln m = - d ln R_i / d ln T; T_BH = 1.058e13 GeV (1 g / m), T1 = T_BH(1e9 g).
Omitted: primary t, W, Z, H; greybody factors; non-SM degrees of freedom.
Outputs: --csv (multiplicities), --json (delta(E), slopes, validation gate B1/B2, predictions), --table (ln_u, ln R_i/R_i(T1)
for wuxu_subedge_variant_boundary.jl variant pyt).
Run: python3 -I wuxu_pythia_multiplicity_pilot.py --csv m.csv --json p.json --table t.csv   (pip install pythia8mc==8.318.3 numpy)
"""
import argparse, json, math, time
import numpy as np
import pythia8mc as p8

ap = argparse.ArgumentParser()
ap.add_argument("--csv", required=True); ap.add_argument("--json", required=True); ap.add_argument("--table", required=True)
ap.add_argument("--nq", type=int, default=80, help="events per quark flavour")
ap.add_argument("--ng", type=int, default=400, help="gluon-pair events")
a = ap.parse_args()

E_TEV = [1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000]
HAD = [("pi", 211), ("K", 321), ("K0L", 130), ("p", 2212), ("n", 2112)]
FLAV = [1, 2, 3, 4, 5]

py = p8.Pythia("", False)
for s in ["ProcessLevel:all = off", "HadronLevel:all = on", "Next:numberCount = 0", "Print:quiet = on",
          "211:mayDecay = off", "321:mayDecay = off", "130:mayDecay = off", "2112:mayDecay = off", "13:mayDecay = off",
          "Random:setSeed = on", "Random:seed = 20261031"]:
    py.readString(s)
py.init()
ev = py.event
pdt = py.particleData


def one_event(kind, E):
    ev.reset()
    if kind == "g":
        ev.append(21, 23, 101, 102, 0., 0., E, E, 0.)
        ev.append(21, 23, 102, 101, 0., 0., -E, E, 0.)
    else:
        m = pdt.m0(kind); pz = math.sqrt(max(E * E - m * m, 0.))
        ev.append(kind, 23, 101, 0, 0., 0., pz, E, m)
        ev.append(-kind, 23, 0, 101, 0., 0., -pz, E, m)
    ev[1].scale(2 * E); ev[2].scale(2 * E)
    py.forceTimeShower(1, 2, 2 * E)
    if not py.next():
        return None
    c = {h: 0 for h, _ in HAD}
    for j in range(ev.size()):
        p = ev[j]
        if p.isFinal():
            ida = p.idAbs()
            for h, pid in HAD:
                if ida == pid:
                    c[h] += 1
    return c


rows = []; fails = 0; t0 = time.time()
mult = {"q": {}, "g": {}}
for E_tev in E_TEV:
    E = 1e3 * E_tev
    for kind, nev, lab in [(f, a.nq, "q") for f in FLAV] + [("g", a.ng, "g")]:
        k = 21 if kind == "g" else kind
        acc = {h: [] for h, _ in HAD}
        for _ in range(nev):
            c = one_event(kind, E)
            if c is None:
                fails += 1; continue
            for h, _ in HAD:
                acc[h].append(c[h] / 2.0)
        for h, _ in HAD:
            arr = np.array(acc[h])
            rows.append({"E_TeV": E_tev, "parton": k, "type": lab, "hadron": h, "n_events": int(arr.size),
                         "mean_per_parton": float(arr.mean()), "sem": float(arr.std(ddof=1) / math.sqrt(arr.size))})
            mult[lab].setdefault(h, {}).setdefault(E_tev, []).append(arr)

with open(a.csv, "w") as fh:
    fh.write("E_TeV,parton,type,hadron,n_events,mean_per_parton,sem\n")
    for r in rows:
        fh.write(f"{r['E_TeV']},{r['parton']},{r['type']},{r['hadron']},{r['n_events']},{r['mean_per_parton']:.6f},{r['sem']:.6f}\n")

# flavour-democratic quark average and gluons: n_{type,h}(E)
lnE = np.log(np.array(E_TEV, float) * 1e3)
n = {lab: {h: np.array([np.concatenate(mult[lab][h][e]).mean() for e in E_TEV]) for h, _ in HAD} for lab in ("q", "g")}
sem = {lab: {h: np.array([np.concatenate(mult[lab][h][e]).std(ddof=1) / math.sqrt(np.concatenate(mult[lab][h][e]).size)
                          for e in E_TEV]) for h, _ in HAD} for lab in ("q", "g")}
delta = {lab: {h: list(np.diff(np.log(n[lab][h])) / np.diff(lnE)) for h, _ in HAD} for lab in ("q", "g")}
tot = {lab: sum(n[lab][h] for h, _ in HAD) for lab in ("q", "g")}
delta_tot = {lab: list(np.diff(np.log(tot[lab])) / np.diff(lnE)) for lab in ("q", "g")}


def n_of_E(lab, h, E):          # log-log interpolation, linear extrapolation in log-log beyond the grid
    x = np.log(E); y = np.log(n[lab][h])
    if x <= lnE[0]:
        s = (y[1] - y[0]) / (lnE[1] - lnE[0]); return math.exp(y[0] + s * (x - lnE[0]))
    if x >= lnE[-1]:
        s = (y[-1] - y[-2]) / (lnE[-1] - lnE[-2]); return math.exp(y[-1] + s * (x - lnE[-1]))
    return math.exp(np.interp(x, lnE, y))


xs = np.exp(np.linspace(math.log(1e-3), math.log(60.), 4000)); dlx = np.diff(np.log(xs)).mean()
wf = xs ** 3 / (np.exp(xs) + 1.0)          # x^2 f(x) dx = x^3 f(x) dlnx
wb = xs ** 3 / np.expm1(xs)
Wq = 72 * 1.5 * 1.2020569031595942; Wg = 16 * 2 * 1.2020569031595942


def avg(lab, h, T):
    w = wf if lab == "q" else wb
    vals = np.array([n_of_E(lab, h, x * T) for x in xs])
    return float((w * vals).sum() / w.sum())


def R(h, T):
    return T * (Wq * avg("q", h, T) + Wg * avg("g", h, T))


T1 = 1.058e13 / 1e9               # GeV at 1e9 g
lnT = np.linspace(math.log(T1 / 10 ** 0.5), math.log(T1 * 1e3), 141)   # 3.5 decades, step ~0.058 in ln T
Ts = np.exp(lnT)
lnR = {h: np.log(np.array([R(h, T) for T in Ts])) for h, _ in HAD}
i1 = int(np.argmin(abs(lnT - math.log(T1))))
slope = {h: list(-np.gradient(lnR[h], lnT)) for h, _ in HAD}
s_at = lambda h, T: float(np.interp(math.log(T), lnT, slope[h]))
# table for the native variant: ln_u = ln(m/m1) = -ln(T/T1) for T >= T1; columns ln(R_i(T)/R_i(T1))
lnR1 = {h: float(np.interp(math.log(T1), lnT, lnR[h])) for h, _ in HAD}
with open(a.table, "w") as fh:
    fh.write("ln_u,pi,K,K0L,p,n\n")
    for T, lt in zip(Ts, lnT):
        if T < T1 * (1 - 1e-12):
            continue
        fh.write(f"{-(lt - math.log(T1)):.10f}," + ",".join(f"{float(np.interp(lt, lnT, lnR[h])) - lnR1[h]:.10f}" for h, _ in HAD) + "\n")

TABLE_EDGE_SLOPE_PI = -1.200486          # authors' first-two-row slope (Mech-S7 ROT036, reproduced in PREREG_036 run header)
idx_10_100 = [k for k in range(len(E_TEV) - 1) if E_TEV[k] >= 10 and E_TEV[k + 1] <= 100]
dq_10_100 = [delta_tot["q"][k] for k in idx_10_100]
B1 = all(0.15 <= d <= 0.45 for d in dq_10_100)
sB2 = s_at("pi", T1)
B2 = abs(sB2 - TABLE_EDGE_SLOPE_PI) <= 0.10
k_lo = E_TEV.index(10); k_hi = E_TEV.index(10000)
pred_delta_decreasing = delta_tot["q"][k_hi] < delta_tot["q"][k_lo] and delta_tot["g"][k_hi] < delta_tot["g"][k_lo]
pred_slope = abs(s_at("pi", 1e6)) < abs(s_at("pi", 1e4))
fals_B = any(not (0.1 <= d <= 0.5) for d in delta_tot["q"] + delta_tot["g"]) or not pred_delta_decreasing
out = {"pythia": "8.318.3 (pythia8mc)", "seed": 20261031, "events_per_quark_flavour": a.nq, "gluon_events": a.ng,
       "failed_events": fails, "E_TeV": E_TEV, "wall_seconds_not_deterministic": "omitted",
       "n_per_parton": {lab: {h: list(map(float, n[lab][h])) for h, _ in HAD} for lab in ("q", "g")},
       "sem": {lab: {h: list(map(float, sem[lab][h])) for h, _ in HAD} for lab in ("q", "g")},
       "delta_by_hadron": {lab: {h: list(map(float, delta[lab][h])) for h, _ in HAD} for lab in ("q", "g")},
       "delta_total": {lab: list(map(float, delta_tot[lab])) for lab in ("q", "g")},
       "T1_GeV": T1, "slope_at": {f"{T:.4g}": {h: s_at(h, T) for h, _ in HAD} for T in (T1, 3e4, 1e5, 3e5, 1e6, 3e6)},
       "gate": {"B1_delta_q_10_100TeV": list(map(float, dq_10_100)), "B1_pass": bool(B1), "B2_s_pi_T1": sB2,
                "B2_table_edge_slope": TABLE_EDGE_SLOPE_PI, "B2_pass": bool(B2)},
       "predictions": {"delta_decreasing_10TeV_vs_10PeV": bool(pred_delta_decreasing),
                       "abs_slope_1PeV_lt_10TeV": bool(pred_slope)},
       "falsified_B": bool(fals_B), "run_C_allowed": bool(B1 and B2)}
json.dump(out, open(a.json, "w"), indent=1, sort_keys=True)
print(json.dumps({"B1": bool(B1), "B2": bool(B2), "sB2": round(sB2, 4), "dq_10_100": [round(float(d), 4) for d in dq_10_100],
                  "pred_dec": bool(pred_delta_decreasing), "pred_slope": bool(pred_slope), "falsified_B": bool(fals_B),
                  "fails": fails, "wall_s": round(time.time() - t0, 1)}))
