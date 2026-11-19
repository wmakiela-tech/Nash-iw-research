#!/usr/bin/env python3
"""PRF14 ROT006: source-only Wu-Xu helium *excess* threshold check.

Run from a clone of Nash-iw-research with:
    python research/prf14/2026-11-19/code/prf14_rot006_helium_excess_gate.py
or specify --csv PATH. Does NOT run Julia, prove a BBN physics transfer,
or make a new physical PBH constraint.
"""
import argparse
import csv
import hashlib
import io
import math
from pathlib import Path

EXPECTED_GIT_BLOB = "431e5fdaf49efad483c946ea10cc7b630654bc42"
EXPECTED_INDICES = (22, 28, 38, 51, 62, 90)
YOBS, SIG_OBS = 0.2458, 0.0013        # Aver 2026 LBT original
YSM, SIG_SM = 0.2472, 0.0008          # Bianco 2026 full-network SBBN
DELTA_FIXED = YOBS + 2 * SIG_OBS - YSM
DELTA_LBT_QUOTED_CMB = YOBS + 2 * SIG_OBS - 0.2467
DELTA_GAUSS = YOBS - YSM + 2 * math.hypot(SIG_OBS, SIG_SM)
EPS_TEST = 0.00025  # hypothetical *differential* model discrepancy, not measured


def crossings(points, target, anchor, max_gap=0.10001):
    """Upward sampled-point brackets only; NEVER bridge -30 to -20."""
    found = []
    for (a, ya), (b, yb) in zip(points[:-1], points[1:]):
        if b - a > max_gap + 1e-10:
            continue
        u, v = ya - anchor, yb - anchor
        if u <= target <= v and v > u:
            root = a + (b - a) * (target - u) / (v - u)
            found.append((a, b, root))
    return found


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def source_rows(path):
    raw = path.read_bytes()
    digest = git_blob_sha(raw)
    if digest != EXPECTED_GIT_BLOB:
        raise RuntimeError(f"FAIL_CLOSED Git blob mismatch {digest} != {EXPECTED_GIT_BLOB}")
    text = raw.decode("utf-8")
    parsed = csv.DictReader(io.StringIO("\n".join(x for x in text.splitlines() if not x.startswith("#"))))
    entries = [r for r in parsed]
    if len(entries) != 192 or sorted({int(r["j"]) for r in entries}) != list(EXPECTED_INDICES):
        raise RuntimeError("FAIL_CLOSED unexpected owner grid shape")
    result = {}
    for j in EXPECTED_INDICES:
        points = sorted((float(r["log10beta"]), float(r["Y"])) for r in entries if int(r["j"]) == j)
        assert len(points) == 32 and points[0][0] == -30 and points[1][0] == -20
        result[j] = points
    return result


def run(path):
    data = source_rows(path)
    print("SOURCE-GIT-BLOB", EXPECTED_GIT_BLOB, "native Julia rows: 192")
    print("Delta_fixed", f"{DELTA_FIXED:.12f}", "Delta_lbt_quoted_cmb", f"{DELTA_LBT_QUOTED_CMB:.12f}", "Delta_gaussian", f"{DELTA_GAUSS:.12f}")
    print("j,anchor,raw_2026_root,delta_fixed_root,delta_lbt_quoted_cmb_root,delta_gaussian_root,gauss_eps_lower,gauss_eps_upper")
    coverage = [0, 0, 0, 0, 0, 0]
    for j, pts in data.items():
        anchor = pts[0][1]
        tests = [crossings(pts, .2484, 0), crossings(pts, DELTA_FIXED, anchor),
                 crossings(pts, DELTA_LBT_QUOTED_CMB, anchor), crossings(pts, DELTA_GAUSS, anchor),
                 crossings(pts, DELTA_GAUSS - EPS_TEST, anchor),
                 crossings(pts, DELTA_GAUSS + EPS_TEST, anchor)]
        if any(len(t) > 1 for t in tests):
            raise RuntimeError("FAIL_CLOSED repeated upward bracket: global root ambiguous")
        coverage = [x + bool(t) for x, t in zip(coverage, tests)]
        def fmt(t): return f"{t[0][2]:.6f}" if t else "HOLD_UNBRACKETED"
        print(f"{j},{anchor:.10f}," + ",".join(fmt(t) for t in tests))
    assert coverage == [6, 4, 6, 6, 4, 6], coverage
    print("BRACKET_COVERAGE", coverage, "PASS; interpolation is conditional, not a physical bound")


def self_test():
    assert abs(DELTA_FIXED - .0012) < 1e-14
    assert abs(DELTA_GAUSS - .0016528675044947) < 1e-12
    assert abs(DELTA_LBT_QUOTED_CMB - .0017) < 1e-14
    assert crossings([(-30., 0.), (-20., .002)], .0012, 0) == []
    assert abs(crossings([(-20., 0.), (-19.9, .002)], .0012, 0)[0][2] - (-19.94)) < 1e-12
    print("SELF_TEST_PASS: threshold arithmetic and 10-dex-gap fail-closed guard")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, help="Original Badacz qa_A.csv checkout path")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    self_test()
    if args.self_test:
        raise SystemExit(0)
    root = Path(__file__).resolve().parents[4]
    default_csv = root / "research/badacz/2026-11-16/data/qa_A.csv"
    run(args.csv or default_csv)
