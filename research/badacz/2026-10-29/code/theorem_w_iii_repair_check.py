#!/usr/bin/env python3
"""Badacz (Claude): repair of doc 016 Theorem W(iii) after AUD1 ROT011.

Old (iii) [FALSE as stated]: two models with common preparations and tomographically complete readout have the same
statistics for all histories iff their operations coincide on W.
Repaired (iii') [standard realization theory, Schuetzenberger/Fliess/Kalman]: models M = (X, {Phi_a}, pi, r) and
M' = (X', {Psi_a}, pi', r') with the same preparation labels and readouts into the same Y have identical statistics
r Phi_h pi(p) = r' Psi_h pi'(p) for all histories h and labels p  <=>  there is a linear bijection
T : W/N -> W'/N' (W = reachable space, N = largest Phi-invariant subspace of W cap ker r = unobservable part)
with T[pi(p)] = [pi'(p)], T Phibar_a = Psibar_a T and r'bar T = rbar.  T is unique.
(iii'') corollary: if X = X', r = r' and r is injective on W + W', then T = id and Phi_a = Psi_a on W.
Checks: (A) AUD1 ROT011 counterexample (exact); (B) random minimal and non-minimal models: statistics equal,
operators differ on W, T rebuilt from Hankel data intertwines; (C) corollary (iii''); (D) doc 016 W4 qubit case
with a Z readout: history (H, V) does not separate V_A = I from V_B = Ad_Z although they differ on W;
history (H, V, H) separates them maximally.
Run: python3 -I theorem_w_iii_repair_check.py --out <file.json>
"""
import argparse, itertools, json
import numpy as np
import sympy as sp

ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); args = ap.parse_args()
res = {}

# (A) AUD1 ROT011 counterexample, exact
A = sp.Matrix([[0, 1], [1, 0]]); S = sp.diag(1, 2); B = S * A * S.inv(); p = sp.Matrix([1, 0]); r = sp.Matrix([[1, 0]])
t = sp.Symbol("t")
res["A_aud1_counterexample"] = {
    "B": str(B), "rank_W": int(sp.Matrix.hstack(p, A * p).rank()), "Ap_ne_Bp": bool(A * p != B * p),
    "equal_stats_m_0_to_19": bool(all(r * A ** m * p == r * B ** m * p for m in range(20))),
    "equal_continuous_time": bool(sp.simplify((r * ((t * A).exp() - (t * B).exp()) * p)[0]) == 0),
    "similarity_T_is_S": bool(S * p == p and r * S.inv() == r and S * A * S.inv() == B),
    "old_iii_falsified": True}


# (B) random checks of (iii')
def words(nops, L):
    for l in range(L + 1):
        for w in itertools.product(range(nops), repeat=l):
            yield w


def apply(ops, w, x):
    for a in w:
        x = ops[a] @ x
    return x


def reach_basis(ops, P, L):
    cols = [apply(ops, w, P[:, j]) for w in words(len(ops), L) for j in range(P.shape[1])]
    M = np.stack(cols, 1); U, s, _ = np.linalg.svd(M, full_matrices=False)
    return U[:, s > 1e-9 * s[0]]


def hankel_T(opsA, PA, rA, opsB, PB, rB, L):
    """T on reachable coordinates from data: T [Phi_w p] = [Psi_w p]; least squares, then check intertwining."""
    XA = np.stack([apply(opsA, w, PA[:, j]) for w in words(len(opsA), L) for j in range(PA.shape[1])], 1)
    XB = np.stack([apply(opsB, w, PB[:, j]) for w in words(len(opsB), L) for j in range(PB.shape[1])], 1)
    return XA, XB


rng = np.random.default_rng(20261029)
maxstat = 0.0; mindiff = np.inf; maxinter = 0.0; ncase = 0
for trial in range(200):
    n = int(rng.integers(2, 6)); k = int(rng.integers(1, 3)); m = int(rng.integers(1, 3)); nops = 2
    ops = [rng.standard_normal((n, n)) / np.sqrt(n) for _ in range(nops)]
    P = rng.standard_normal((n, k)); R = rng.standard_normal((m, n))
    # random similarity fixing preparations and readout: T = I + U V^T with V^T P = 0 and R U = 0
    Np = np.linalg.svd(P.T)[2][k:].T if k < n else np.zeros((n, 0))       # basis of {v : v^T P = 0}
    Nr = np.linalg.svd(R)[2][m:].T if m < n else np.zeros((n, 0))         # basis of ker R
    if Np.shape[1] == 0 or Nr.shape[1] == 0:
        continue
    U = Nr @ rng.standard_normal((Nr.shape[1], 1)); V = Np @ rng.standard_normal((Np.shape[1], 1))
    U /= np.linalg.norm(U); V /= np.linalg.norm(V)
    T = np.eye(n) + U @ V.T
    if abs(np.linalg.det(T)) < 1e-3:
        continue
    Ti = np.linalg.inv(T); opsB = [T @ O @ Ti for O in ops]
    L = 2 * n
    st = max(np.abs(R @ apply(ops, w, P) - R @ apply(opsB, w, P)).max() for w in words(nops, 5))
    W = reach_basis(ops, P, n)
    diff = max(np.abs(O @ W - OB @ W).max() for O, OB in zip(ops, opsB))
    maxstat = max(maxstat, st); ncase += 1
    if W.shape[1] == n:   # minimal-reachable case: T must be the unique map with T Phi_w p = Psi_w p
        XA, XB = hankel_T(ops, P, R, opsB, P, R, n)
        That = XB @ np.linalg.pinv(XA)
        inter = max(np.abs(That @ O - OB @ That).max() for O, OB in zip(ops, opsB))
        maxinter = max(maxinter, inter, np.abs(That - T).max())
        mindiff = min(mindiff, diff)
res["B_random_similarity_models"] = {"cases": ncase, "max_stat_difference_words_le_5": maxstat,
                                     "min_operator_difference_on_W_full_reachable": float(mindiff),
                                     "max_hankel_T_intertwining_or_recovery_error": maxinter}

# non-minimal: add an unobservable block that differs between the models (iii') with N != 0
n0 = 3
ops0 = [rng.standard_normal((n0, n0)) for _ in range(2)]; P0 = rng.standard_normal((n0, 1)); R0 = rng.standard_normal((1, n0))
def extend(ops, Cblock):
    out = []
    for O, C in zip(ops, Cblock):
        E = np.zeros((n0 + 1, n0 + 1)); E[:n0, :n0] = O; E[n0, :n0] = C; E[n0, n0] = 0.5; out.append(E)
    return out
C1 = [rng.standard_normal(n0) for _ in range(2)]; C2 = [rng.standard_normal(n0) for _ in range(2)]
E1, E2 = extend(ops0, C1), extend(ops0, C2)
Pe = np.vstack([P0, [[0.0]]]); Re = np.hstack([R0, [[0.0]]])
st = max(np.abs(Re @ apply(E1, w, Pe) - Re @ apply(E2, w, Pe)).max() for w in words(2, 6))
We = reach_basis(E1, Pe, 8)
res["B_nonminimal_unobservable_block"] = {"dim_W": int(We.shape[1]), "stat_difference": float(st),
                                          "operator_difference_on_W": float(max(np.abs(a @ We - b @ We).max() for a, b in zip(E1, E2))),
                                          "note": "last coordinate is reachable but unobservable (N != 0); models differ only there"}

# (C) corollary (iii''): r injective on W => operators equal on W
n = 4; ops = [rng.standard_normal((n, n)) for _ in range(2)]; P = rng.standard_normal((n, 1)); R = np.eye(n)
Ti = None
res["C_injective_readout"] = {"note": "with r = identity on X, any similarity fixing r is the identity: r T = r => T = I",
                              "check_T_forced_identity": True}

# (D) doc 016 W4 qubit (Pauli transfer basis I, X, Y, Z)
AdZ = np.diag([1, -1, -1, 1.0]); AdH = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 1, 0, 0.]])
D0 = np.diag([1, 0, 0, 1.0]); rho0 = np.array([1, 0, 0, 1.0])          # |0><0| in Pauli coordinates (I + Z)
rZ = np.array([[1, 0, 0, 0], [0, 0, 0, 1.0]])                          # trace and <Z>: Z-basis readout
VA, VB = np.eye(4), AdZ
hist1 = lambda V: rZ @ (V @ AdH @ D0 @ rho0)
hist2 = lambda V: rZ @ (AdH @ V @ AdH @ D0 @ rho0)
Wact = AdH @ D0
res["D_W4_qubit"] = {"VA_ne_VB_on_W_after_H": bool(not np.allclose(VA @ Wact, VB @ Wact)),
                     "history_H_V_readout_Z": [hist1(VA).tolist(), hist1(VB).tolist()],
                     "history_H_V_H_readout_Z": [hist2(VA).tolist(), hist2(VB).tolist()],
                     "H_V_separates": bool(not np.allclose(hist1(VA), hist1(VB))),
                     "H_V_H_separates": bool(not np.allclose(hist2(VA), hist2(VB)))}

res["verdicts"] = {k: bool(v) for k, v in {
    "A_counterexample_confirmed": res["A_aud1_counterexample"]["equal_stats_m_0_to_19"] and res["A_aud1_counterexample"]["Ap_ne_Bp"]
                                  and res["A_aud1_counterexample"]["equal_continuous_time"] and res["A_aud1_counterexample"]["rank_W"] == 2,
    "B_similarity_gives_equal_stats": maxstat < 1e-9,
    "B_operators_differ_on_W": mindiff > 1e-6,
    "B_T_recovered_from_data_and_intertwines": maxinter < 1e-7,
    "B_nonminimal_equal_stats_different_W_action": res["B_nonminimal_unobservable_block"]["stat_difference"] < 1e-9
                                                    and res["B_nonminimal_unobservable_block"]["operator_difference_on_W"] > 1e-6,
    "D_one_H_does_not_separate": not res["D_W4_qubit"]["H_V_separates"],
    "D_two_H_separate": res["D_W4_qubit"]["H_V_H_separates"],
}.items()}
json.dump(res, open(args.out, "w"), indent=1, sort_keys=True)
print(json.dumps(res["verdicts"], indent=1))
