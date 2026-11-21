"""PREREG_079 NET arm: PRyMordial copy with (i) the PREREG_077 helper (kick unused; tol_scale used for V4) and
(ii) additive per-nucleon hadronic conversion rates in all three eras.

Usage: python3 -I prym_rate_patch_079.py <src_repo_dir> <dst_repo_dir>
Applies ../../2026-11-20/code/prym_kick_patch_077.py (verifies its result SHA), then replaces the six
`return NormWeakRates*nTOp_{frwrd,bkwrd}_{HT,MT,LT}(T)` lines by the same expression
`+ _iw079_extra("n2p"|"p2n", T)`. frwrd = n->p per neutron, bkwrd = p->n per proton (PRyMordial convention:
dYn/dt = bkwrd*Yp - frwrd*Yn). _iw079_extra returns 0.0 unless PRyMini.iw079_rate_<kind> is set
(callable of T in MeV, returning 1/s). With no rate set the patched code is behaviourally identical.
"""
import hashlib, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P077 = os.path.join(HERE, "..", "..", "2026-11-20", "code", "prym_kick_patch_077.py")
P077_SHA = "7d9e5f07146b73b25c923d17e310fffd0065fc2cb92cdc8b500dc06ce8d571fa"
MAIN_077_SHA = "cd607965eb711efc20463c754801140db4b4c53a0cae41654a3327e95b4f6fd0"

HELPER = '''
# ---- IW PREREG_079 rate hook (inserted by prym_rate_patch_079.py) ----
def _iw079_extra(kind, T_K):
    import PRyM.PRyM_init as _ini
    f = getattr(_ini, "iw079_rate_" + kind, None)
    if f is None:
        return 0.0
    return f(T_K / _ini.MeV_to_Kelvin)
# ---- end IW PREREG_079 hook ----
'''
ANCHOR = "# ---- end IW PREREG_077 helper ----\n"


def main(src, dst):
    if hashlib.sha256(open(P077, "rb").read()).hexdigest() != P077_SHA:
        sys.exit("P077_IDENTITY_MISMATCH")
    subprocess.run([sys.executable, "-I", P077, src, dst], check=True)
    p = os.path.join(dst, "PRyM", "PRyM_main.py")
    s = open(p, encoding="utf-8").read()
    if hashlib.sha256(s.encode("utf-8")).hexdigest() != MAIN_077_SHA:
        sys.exit("MAIN_077_MISMATCH")
    assert s.count(ANCHOR) == 1
    s = s.replace(ANCHOR, ANCHOR + HELPER, 1)
    n = 0
    for era in ("HT", "MT", "LT"):
        for fb, kind in (("frwrd", "n2p"), ("bkwrd", "p2n")):
            old = f"return NormWeakRates*nTOp_{fb}_{era}(T)\n"
            assert s.count(old) == 1, old
            s = s.replace(old, f"return NormWeakRates*nTOp_{fb}_{era}(T) + _iw079_extra(\"{kind}\", T)\n", 1)
            n += 1
    assert n == 6
    open(p, "w", encoding="utf-8").write(s)
    print("PATCHED_079", hashlib.sha256(s.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
