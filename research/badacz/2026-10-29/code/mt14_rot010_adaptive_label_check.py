#!/usr/bin/env python3
"""BADACZ (Claude): cross-family check of MT14 ROT010 (finite adaptive labels, invariance of domain, threshold bit
versus antipodal alias, K-ary sharp budget, deterministic action labels).
  R1  exact 11-node control: M_ji = i^j (i = 1..11, j = 0,1,2), all 165 3x3 minors positive, kernel dimension 8,
      two distinct positive sources with identical 7 reals and identical bit (Fractions).
  R2  T010.2: f(x) = (x1..x7, [x8 >= 0]) has no antipodal collision on spheres (random points incl. x8 = 0 exactly).
  R3  T010.3: midpoint design attains a/K exactly; for random decoder sets the covering radius is >= a/K.
  R4  T010.4: discrete adaptive example: I(C; Y, A) = I(C; Y) exactly when A = g(Y_<j); the policy changes I(C; Y)
      relative to a non-adaptive schedule.
Synthetic mathematics only. numpy 2.1.3; seed 20261029.
Run: python3 -I mt14_rot010_adaptive_label_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

SEED = 20261029


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def solve3(A, b):
    D = det3(A)
    out = []
    for k in range(3):
        Ak = [[b[i] if j == k else A[i][j] for j in range(3)] for i in range(3)]
        out.append(det3(Ak) / D)
    return out


def part_R1():
    M = [[Fr(i) ** j for i in range(1, 12)] for j in range(3)]
    minors = [det3([[M[j][c] for c in cols] for j in range(3)]) for cols in itertools.combinations(range(11), 3)]
    def source(t):
        c = [Fr(0)] * 7 + [t]
        rhs = [-sum(M[j][i] * c[i] for i in range(8)) for j in range(3)]
        tail = solve3([[M[j][8 + k] for k in range(3)] for j in range(3)], rhs)
        return c + tail
    t = Fr(1, 10 ** 6)
    c1, c2 = source(t), source(t / 2)
    moments_zero = all(sum(M[j][i] * c[i] for i in range(11)) == 0 for c in (c1, c2) for j in range(3))
    positive = all(Fr(1, 2) + x > 0 and Fr(1, 2) - x > 0 for c in (c1, c2) for x in c)
    transcript = lambda c: (tuple(c[:7]), c[7] >= 0)
    return {"minors_count": len(minors), "all_minors_positive": all(m > 0 for m in minors),
            "min_minor": str(min(minors)), "moments_zero": moments_zero, "both_species_positive": positive,
            "max_abs_c": float(max(abs(x) for x in c1 + c2)), "distinct": c1 != c2,
            "identical_transcript": transcript(c1) == transcript(c2)}


def part_R2(rng):
    f = lambda x: (tuple(x[:7]), bool(x[7] >= 0))
    coll = 0
    for i in range(20000):
        x = rng.normal(size=8)
        if i % 4 == 0: x[7] = 0.0
        x /= np.linalg.norm(x)
        coll += int(f(x) == f(-x))
    return {"points": 20000, "antipodal_collisions": coll}


def part_R3(rng):
    a = Fr(1, 17)
    rows = []
    for K in (1, 2, 3, 4, 7, 8, 13, 32, 255):
        z = [-a + a / K * (2 * l + 1) for l in range(K)]
        # worst error of midpoint design = max over x of distance to its cell midpoint = a/K
        edges = [-a + 2 * a * l / K for l in range(K + 1)]
        worst = max(max(abs(edges[l] - z[l]), abs(edges[l + 1] - z[l])) for l in range(K))
        # random decoder sets: covering radius of [-a, a] by K points is >= a/K
        ok = True
        for _ in range(200):
            zs = sorted(Fr(int(v), 10 ** 6) * 2 * a - a for v in rng.integers(0, 10 ** 6 + 1, size=K))
            gaps = [zs[0] + a] + [(zs[i + 1] - zs[i]) / 2 for i in range(K - 1)] + [a - zs[-1]]
            ok &= max(gaps) >= a / K
        rows.append({"K": K, "midpoint_worst": str(worst), "equals_a/K": worst == a / K, "random_decoders_respect_bound": ok})
    return rows


def H(p):
    return -sum(x * math.log2(x) for x in p if x > 0)


def mutual_info(joint):
    """joint: dict {(c, obs): prob}; returns I(C; obs)."""
    pc, po = {}, {}
    for (c, o), p in joint.items():
        pc[c] = pc.get(c, 0) + p; po[o] = po.get(o, 0) + p
    return sum(p * math.log2(p / (pc[c] * po[o])) for (c, o), p in joint.items() if p > 0)


def part_R4():
    # C uniform on {0,1,2}; two binary noisy tests: test0 asks "C == 0?", test1 asks "C == 1?", error eps
    eps = 0.1
    def lik(test, c, y):
        truth = int(c == test)
        return 1 - eps if y == truth else eps
    def run(policy):
        jY, jYA = {}, {}
        for c in range(3):
            for y1 in (0, 1):
                a2 = policy(y1)
                for y2 in (0, 1):
                    p = (1 / 3) * lik(0, c, y1) * lik(a2, c, y2)
                    jY[(c, (y1, y2))] = jY.get((c, (y1, y2)), 0) + p
                    jYA[(c, (y1, a2, y2))] = jYA.get((c, (y1, a2, y2)), 0) + p
        return mutual_info(jY), mutual_info(jYA)
    adaptive = run(lambda y1: 1 if y1 == 0 else 0)    # if test0 says "not 0", ask about 1
    fixed = run(lambda y1: 0)                            # repeat test0
    fixed1 = run(lambda y1: 1)                           # fixed second test about 1
    return {"adaptive_I(C;Y)": adaptive[0], "adaptive_I(C;Y,A)": adaptive[1],
            "fixed_repeat_I(C;Y)": fixed[0], "fixed_other_I(C;Y)": fixed1[0], "H(C)": H([1 / 3] * 3)}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    R1 = part_R1(); R2 = part_R2(rng); R3 = part_R3(rng); R4 = part_R4()
    verdict = {
        "R1_exact_control": R1["minors_count"] == 165 and R1["all_minors_positive"] and R1["moments_zero"]
                            and R1["both_species_positive"] and R1["distinct"] and R1["identical_transcript"],
        "R2_no_antipodal_collision": R2["antipodal_collisions"] == 0,
        "R3_sharp_a/K": all(r["equals_a/K"] and r["random_decoders_respect_bound"] for r in R3),
        "R4_action_label_free": abs(R4["adaptive_I(C;Y)"] - R4["adaptive_I(C;Y,A)"]) < 1e-12
                                and R4["adaptive_I(C;Y)"] > max(R4["fixed_repeat_I(C;Y)"], R4["fixed_other_I(C;Y)"]),
    }
    res = {"R1": R1, "R2": R2, "R3": R3, "R4": R4, "verdict": verdict, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "mt14_rot010_adaptive_label_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
