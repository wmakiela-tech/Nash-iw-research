---
artifact_id: IW_MECH_S11_ROT016_STOPA_28000_EVENT_RAW_REPLAY_AND_UNATTEMPTED_CELL_CONTINUATION_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
status: PARTIAL_NATIVE / G_E_FAIL / TECHNICAL_CONTINUATION_UNATTEMPTED_ONLY
claim_ceiling: NO_STOPA_CLOSURE / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Actual evidence
Run 45702555163 all four jobs completed failure. All four artifacts downloaded; ZIP CRC PASS, provider SHA256 exact, full manifest coverage and 87/87 file hashes PASS. IDs and hashes:
g off 15063773316 233122b31e78dcc1fe9e14fd05727346f5045f2e0228b0274fad57233eac8ba5 (28 files)
g on 15063024176 5b8165668868633d8cf67c1c0ba0004861217e9b8768156d88388012ca6eb4a0 (11)
u off 15064287358 2cd5fa4c10aeb7f64e0bf39f5e0f87fb9e702948ac698406bd5358c85ffe2126 (24)
u on 15064391495 7815fb74367b562461984f9068998c21974e8d4b58f4b997bef28a3c9ed64171 (24).
Local Python read all 14 CSVs and JSONs, counted 28000 accepted rows, exact agreement with summary event counts, 0 charge3 violations, 77 energy violations, all 56 charge-pair mean/SE tests within 3. Exact energies indices 0..5 =10,30,100,300,1000,2000 TeV. For g off e0..e4, energy violations 0,0,0,0,67; g on e0 1; u off e0..e3 0,0,0,6; u on e0..e3 0,0,0,3. Each attempted cell completed all 2000 accepted events; 10 cells PASS, 4 G_E FAIL. Max relative residual g off e4 1.5062741278271119e-5, u off e3 6.986904277028749e-6, u on e3 1.590770699833044e-6, g on e0 1.3567670895664463e-6. No removal or gate relaxation. No physical conservation failure claim. 
# Conditional selection diagnostic
u ON rejects 266,421,552,814 events respectively (11.74%,17.39%,21.63%,28.93% of attempts), u OFF zero. Pion per-primary mean off/on at 10,30,100,300 TeV: 58.803/58.75075; 81.97125/82.086; 118.15575/120.1085; 166.272/165.59675. Differences -0.089%,+0.140%,+1.653%,-0.406%; independent conditional sample SE z=-.069,.107,1.206,-.296. Last pair fails G_E. Not inclusive weak-shower comparison: increasing hard-process selection fraction is material. Do not equate filtered sample to inclusive population, missing rejected event multiplicities. No correction inferred. P1 at 100..2000 TeV unavailable. No splot/STOP A closure.
# Technical continuation
All four artifacts TIMELINE show final attempted cell START without END, and no subsequent cell START or files; exit immediately after nonzero driver. Exactly ten cells genuinely unattempted: u off indices 4,5; u on 4,5; g off 5; g on 1,2,3,4,5. Preserve all 14 earlier outputs incl 4 failed cells; NO repeat. Correct Bash inherited errexit by if timeout command; then rc=0; else rc=$?; fi. No change driver, seeds, package, physics or gates. Only run these ten cells under same source identity and 8.318.3 wheel digest, with explicit manifest and return-code capture. This is technical completion of unattempted cells, not retry of failed scientific gates. Combined full-stage G_E already FAIL regardless of remaining outcomes; completion measures scope of negative result, does not reverse it. No BW write.
