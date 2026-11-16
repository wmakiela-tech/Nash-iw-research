#!/usr/bin/env python3
"""Mech-S10 ROT002: read-only source-operator 2x2 factorial check for Wu-Xu.

Takes ONLY original Wu-Xu hadrons_from_PBH.dat from author commit d395183.
Checks original Git blob SHA-1 and 100x6 data; reproduces the paper/code
first-two-node and Badacz p12 first-12-node exponents. Applies *source-only*
E5 charge allocation and p12 exponent modification algebraically; no Julia,
BlackHawk, PYTHIA, 10D kinetics, Yp or PBH bound is computed.

Usage: python3 -I mech_s10_rot002_source_factorial_referee.py /path/to/hadrons_from_PBH.dat
"""
import hashlib
import json
import math
import pathlib
import sys

ORIGINAL_GIT_BLOB = "06d0883a27b108692720422294ba2baacd381a64"
LABELS = ("pipm", "Kpm", "K0L", "proton", "neutron")
# Source-carrying tracked states in original Wu-Xu source. E5 Mech-S6
# changes 4 group input assignments; pion source feeds two charge states.
STATES = (("pi_minus", 0, 0.5), ("pi_plus", 0, 0.5),
          ("K_minus", 1, 0.5), ("K0L", 2, 1.0),
          ("anti_proton", 3, 0.5), ("anti_neutron", 4, 0.5))


def git_blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def parse_rows(raw, require_original=True):
    actual_sha = git_blob(raw)
    if require_original and actual_sha != ORIGINAL_GIT_BLOB:
        raise ValueError("ORIGINAL_BLOB_SHA_MISMATCH: " + actual_sha)
    lines = raw.decode("utf-8").splitlines()
    rows = []
    for index, line in enumerate(lines, 1):
        if not line.strip():
            continue
        cells = line.split()
        # The author header contains units and names; only row 1 is skipped.
        if index == 1 and cells[0] == "m_PBH":
            continue
        if len(cells) != 6:
            raise ValueError(f"ROW_WIDTH at source line {index}")
        values = tuple(float(s) for s in cells)
        if any(not math.isfinite(v) or v <= 0 for v in values):
            raise ValueError(f"NONPOSITIVE_OR_NONFINITE at source line {index}")
        rows.append(values)
    if len(rows) != 100:
        raise ValueError(f"ROW_COUNT expected 100 got {len(rows)}")
    if any(b[0] <= a[0] for a, b in zip(rows, rows[1:])):
        raise ValueError("MASS_ORDER")
    if not math.isclose(rows[0][0], 5.609588603804452e32, rel_tol=1e-13):
        raise ValueError("FIRST_MASS_ANCHOR")
    return rows, actual_sha


def slope(rows, col, n):
    xs = [math.log(r[0]) for r in rows[:n]]
    ys = [math.log(r[col + 1]) for r in rows[:n]]
    xm = math.fsum(xs) / n
    ym = math.fsum(ys) / n
    return math.fsum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / math.fsum((x - xm)**2 for x in xs)


def calculate(rows):
    base_slopes = [slope(rows, col, 2) for col in range(5)]
    long_slopes = [slope(rows, col, 12) for col in range(5)]
    deltas = [b - a for a, b in zip(base_slopes, long_slopes)]
    # Both patches touch only the *source law*. u is identity above and at m0.
    def u(k, mass_ratio):
        return math.exp(deltas[k] * math.log(mass_ratio)) if mass_ratio < 1.0 else 1.0
    groups = []
    for k, label in enumerate(LABELS):
        groups.append({"group": label, "first2_slope": base_slopes[k],
                       "first12_slope": long_slopes[k], "slope_change": deltas[k],
                       "p12_over_code_at_3e8g": u(k, 0.3),
                       "p12_over_code_at_1e8g": u(k, 0.1)})
    states = []
    for label, group, q in STATES:
        item = {"state": label, "source_group": LABELS[group], "q_e5": q}
        for mratio, key in ((1.0, "1e9g"), (0.3, "3e8g"), (0.1, "1e8g")):
            native = rows[0][group+1] * mratio**base_slopes[group]
            multiplier = u(group, mratio)
            # Source-only 2x2 factorial: original, E5, p12, E5+p12.
            s00 = native
            s10 = q * native
            s01 = multiplier * native
            s11 = q * multiplier * native
            interaction = (s11 - s10) - (s01 - s00)
            algebra = (q - 1.0) * (multiplier - 1.0) * native
            if not math.isclose(interaction, algebra, rel_tol=5e-12, abs_tol=1e-10):
                raise ValueError("INTERACTION_IDENTITY_FAILED")
            if not math.isclose(q * (multiplier * native), multiplier * (q * native), rel_tol=1e-15):
                raise ValueError("SOURCE_OPERATOR_ORDER_FAILED")
            item[key] = {"u_p12": multiplier,
                         "interaction_over_unmodified_state_rate": (q-1.0)*(multiplier-1.0),
                         "joint_over_unmodified_state_rate": q*multiplier}
        states.append(item)
    # Both operators equal identity at or above the first table mass.
    assert all(row["1e9g"]["interaction_over_unmodified_state_rate"] == 0.0 for row in states)
    return {"groups": groups, "states": states,
            "claim_scope": "EXACT_SOURCE_FUNCTIONS_ONLY_NOT_NATIVE_KINETICS_OR_PHYSICAL_LIMIT"}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 -I script.py ORIGINAL_hadrons_from_PBH.dat")
    raw = pathlib.Path(sys.argv[1]).read_bytes()
    rows, sha = parse_rows(raw)
    out = calculate(rows)
    out.update({"original_source_git_blob": sha, "original_rows": len(rows),
                "source_owner": "Wu-Xu@d395183", "E5_patch_owner": "Mech-S6", "p12_control_owner": "Badacz PREREG060", "execution": "NO_NATIVE_RUN"})
    print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
