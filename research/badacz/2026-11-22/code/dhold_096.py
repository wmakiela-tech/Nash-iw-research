"""NOTE_096 (EKS1-DIR-009 step 3, descriptive, post hoc): spread of dhold = lb_HERBH - lb_H73 over the H73 realizations
of PREREG_094 (J = nominal x1.001, R1, R2) with the HERBH root fixed at its 090 value (its own solver jitter not resampled).
Usage: python3 -I dhold_096.py <analysis090.json> <analysis094.json> <out.json>"""
import json, math, sys
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); out = {"cells": {}}
dd = []; allv = []
for j in (22, 62):
    for m in ("code", "net"):
        for Y in (0.251, 0.2484):
            her = A["roots"][f"HERBH_{j}|{m}|{Y}"]["lb"]; d0 = A["estimands"][f"{j}|{m}|{Y}"]["dhold"]
            c = {"nom": d0}
            for X, a in (("J", "f"), ("R1", "b"), ("R2", "d")):
                v = her - B["roots"][f"{a}_{j}|{m}|{Y}"]["lb"]; c[X] = v; dd.append(v - d0); allv.append(v)
            allv.append(d0); out["cells"][f"{j}|{m}|{Y}"] = c
out["summary"] = {"min": min(allv), "max": max(allv), "max_abs_delta": max(abs(x) for x in dd), "rms_delta": math.sqrt(sum(x * x for x in dd) / len(dd)), "n": len(allv)}
json.dump(out, open(sys.argv[3], "x"), indent=1); print(json.dumps(out["summary"]))
