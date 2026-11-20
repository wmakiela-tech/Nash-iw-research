"""PREREG_077 NET arm: patch PRyMordial (vallima/PRyMordial @725d8a8) with an
instantaneous neutron-fraction kick at photon temperature T_p.

Usage: python3 -I prym_kick_patch_077.py <src_repo_dir> <dst_repo_dir>

Copies the whole repository to dst (PRyM reads rate tables from os.getcwd()),
then patches dst/PRyM/PRyM_main.py:
  * exposes the internal t_of_T interpolator (T in MeV -> t in s) as PRyMini.iw077_t_of_T;
  * routes the n/p-network solve_ivp calls (HT, MT, LT; small and large net) through
    _iw077_solve, which (only if PRyMini.iw077_kick is set and the kick time lies strictly
    inside the era) integrates to t_k, applies the kick to (Yn, Yp), and integrates on.
Kick (fluence A, per-baryon fraction converted at t_k):
  sign=+1 (p->n): Yn += A*Yp, Yp -= A*Yp ;  sign=-1 (n->p): Yp += A*Yn, Yn -= A*Yn.
Optional PRyMini.iw077_tol_scale multiplies rtol (default 1e-3 if absent) and atol of these calls.
With iw077_kick unset and tol_scale == 1 the patched code calls solve_ivp with the original
arguments, i.e. is behaviourally identical to the original.
"""
import hashlib, shutil, sys, os

SRC_MAIN_SHA256 = "98f0724f27ace2927d38c3eec615def05bfbfd9c1c9cc09cfa91470417b3451f"

HELPER = '''
# ---- IW PREREG_077 kick helper (inserted by prym_kick_patch_077.py) ----
def _iw077_solve(fun, tspan, y0, **kw):
    import PRyM.PRyM_init as _ini
    k = getattr(_ini, "iw077_kick", None)
    s = getattr(_ini, "iw077_tol_scale", 1.0)
    if s != 1.0:
        kw = dict(kw)
        kw["rtol"] = kw.get("rtol", 1.e-3) * s
        kw["atol"] = kw.get("atol", 1.e-6) * s
    if k is None:
        return solve_ivp(fun, tspan, y0, **kw)
    t0, t1 = float(tspan[0]), float(tspan[1])
    tk = float(_ini.iw077_t_of_T(k["T_MeV"]))
    if not (t0 < tk < t1):
        return solve_ivp(fun, tspan, y0, **kw)
    s1 = solve_ivp(fun, [t0, tk], y0, **kw)
    y = np.array(s1.y[:, -1], dtype=float)
    Yn, Yp = float(y[0]), float(y[1])
    A = float(k["A"])
    if k["sign"] > 0:
        y[0] = Yn + A * Yp
        y[1] = Yp - A * Yp
    else:
        y[0] = Yn - A * Yn
        y[1] = Yp + A * Yn
    s2 = solve_ivp(fun, [tk, t1], y, **kw)
    k["log"] = {"t_k": tk, "Yn_before": Yn, "Yp_before": Yp,
                "status_pre": int(s1.status), "status_post": int(s2.status), "era_t0": t0, "era_t1": t1}
    return s2
# ---- end IW PREREG_077 helper ----
'''

ANCHOR_IMPORT = "from scipy.special import zeta\n"
ANCHOR_TOFT = "        T_of_t = interp1d(t_vec[:],Tg_vec[:],bounds_error=False,fill_value=\"extrapolate\",kind='linear')\n"
CALLS = [
    "sol_at_HT = solve_ivp(Y_prime_HT,[t_init,t_fin],Yi_vec,method='LSODA',rtol=1.e-6,atol=1.e-9)",
    "sol_at_MT = solve_ivp(Y_prime,[t_init,t_fin],Yi_vec,method='BDF',jac=Jacobian,rtol=1.e-6,atol=1.e-9)",
    "sol_at_MT = solve_ivp(Y_prime_MT,[t_init,t_fin],Yi_vec,method='BDF',jac=Jacobian_MT,rtol=1.e-6,atol=1.e-9)",
    "sol_at_LT = solve_ivp(Y_prime,[t_init,t_fin],Yi_vec,method='BDF',jac=Jacobian,atol=1.e-11)",
    "sol_at_LT = solve_ivp(Y_prime_LT,[t_init,t_fin],Yi_vec,method='BDF',jac=Jacobian_LT,atol=1.e-15)",
]


def main(src, dst):
    main_py = os.path.join(src, "PRyM", "PRyM_main.py")
    h = hashlib.sha256(open(main_py, "rb").read()).hexdigest()
    if h != SRC_MAIN_SHA256:
        sys.exit(f"SOURCE_IDENTITY_MISMATCH {h}")
    if os.path.exists(dst):
        sys.exit("DST_EXISTS")
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git"))
    p = os.path.join(dst, "PRyM", "PRyM_main.py")
    s = open(p, encoding="utf-8").read()
    assert s.count(ANCHOR_IMPORT) == 1 and s.count(ANCHOR_TOFT) == 1
    s = s.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + HELPER, 1)
    s = s.replace(ANCHOR_TOFT, ANCHOR_TOFT + "        PRyMini.iw077_t_of_T = t_of_T\n", 1)
    for c in CALLS:
        assert s.count(c) == 1, c
        s = s.replace(c, c.replace("= solve_ivp(", "= _iw077_solve(", 1), 1)
    assert s.count("_iw077_solve(") == 1 + len(CALLS)
    open(p, "w", encoding="utf-8").write(s)
    print("PATCHED", hashlib.sha256(s.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
