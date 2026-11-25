---
artifact_id: IW_MECH_S11_ROT015_STOPA_FIRST_NATIVE_CELL_ENERGY_GATE_FAIL_AND_SHELL_EARLY_ABORT_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
status: PARTIAL_NATIVE_DIAGNOSTIC / G_E_FAIL / OTHER_ARMS_RUNNING
claim_ceiling: NO_STOPA_CLOSURE / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Source custody
Continuation run 45702555163, job 139516146281 (gluon, weakShower on) completed failure; three other jobs in progress at read. All four installation steps PASS. Artifact 15063024176, 373230 bytes, SHA256 5b8165668868633d8cf67c1c0ba0004861217e9b8768156d88388012ca6eb4a0 independently checked on downloaded ZIP; CRC PASS; all 11/11 manifest entries match. Wheel SHA256 0ebe2dff962631571100dc427fbaa95e388df054ac06cdc8f63b31af07eb3de8, pythia8mc 8.318.3 cp311 manylinux. Source: https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45702555163/artifacts/15063024176 . No claim other data read.

# Native sample
gluon, E'=10000 GeV, weakShower=on, seed121000, 2000 accepted, zero failed/rejected, all charge3=0; four paired G_QS true as exported. G_E FAIL 1/2000, event accepted=attempt=1442, hard_size=2, ratio=0.9999986432329104, |residual|=1.3567670895664463e-6, absolute energy deficit 0.027135341791328926 GeV at eCM=20000 GeV. Relative absolute residual median 9.696854430529811e-12, 99th percentile 2.8426961451444295e-10, 99.9th percentile 7.075683380319923e-10. No relaxation of frozen 1e-6; do not exclude event or infer physical nonconservation. Particle record and exact conservation-check internals not saved; cause not identified. Sample diagnostic only, not admissible full stage.
Local Python direct raw CSV verification: 2000 rows, zero charge violations, one energy violation. Per-primary mean group multiplicities from all events: pi+- 107.1075, K+- 12.86875, K0L 6.3845, p+pbar 7.66, n+nbar 7.5905. These are generator predictions in failed gate sample. Signed counts order (211,-211,321,-321,130,2212,-2212,2112,-2112): sum [214153,214277,25785,25690,25538,15347,15293,15154,15208].
Raw count cross-product matrix computed exactly in int64:
[[24901515,24889654,2962063,2968631,2939751,1769022,1770645,1747485,1745862],[24889654,24918733,2976055,2957400,2940396,1776762,1764134,1741278,1753906],[2962063,2976055,381481,367684,357302,211410,210816,208577,209171],[2968631,2957400,367684,379728,356260,211569,210545,207184,208208],[2939751,2940396,357302,356260,380234,208501,208331,206199,206369],[1769022,1776762,211410,211569,208501,141909,133779,123459,131589],[1770645,1764134,210816,210545,208331,133779,140299,130527,124007],[1747485,1741278,208577,207184,206199,123459,130527,137676,130608],[1745862,1753906,209171,208208,206369,131589,124007,130608,138190]].
Covariance of per-event vector = (cross-sum*sum^T/2000)/1999; covariance of per-primary sample mean = covariance/(4*2000).

# Technical early-abort
Job log exit code 2 immediately after first cell; artifact TIMELINE contains only START gluon_w1_e0, no END or CELL_RC, no files for e1..e5. Workflow uses explicit shell bash (GitHub default -e) and set -uo pipefail which does not disable inherited errexit. Nonzero driver status appears to abort before rc capture; strongest supported explanation, not rerun. Preserve failed e0, do not rerun it. Once other arms finish, inventory all attempted cells; if technically continuing, only genuinely unattempted cells, use if timeout ...; then rc=0; else rc=$?; fi; keep scientific gates unchanged. No new job launched this rotation, no claims of G_OVL, G_COV or response delta. No BW write.
