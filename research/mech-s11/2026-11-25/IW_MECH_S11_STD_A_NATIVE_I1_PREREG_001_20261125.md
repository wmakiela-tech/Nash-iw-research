---
artifact_id: IW_MECH_S11_STD_A_NATIVE_I1_PREREG_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
exposure: PUBLIC_SOURCE_REPLICATION
class: NONBLIND_INDEPENDENT_EXECUTION_PREREG
claim_ceiling: MODEL_CONDITIONAL / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# STD_A-R: independent native execution, part A only

Moderator explicitly confirmed standing authorization for all calculations in the Mech-S11 conversation on 25 November (near deadline). This is not authorization to promote claims. No automatic retry. Owner Badacz firstness REVIEW124/126, EKS1 direction; REC14 ROT016 logical separation H1/H2. Predictions already exposed. No blinded claim.

## Frozen source and estimand
Wu-Xu upstream d395183674cace6c9906a8911bdeb7234ba4040d, directory arXiv-2509.05618; main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6, main-scan-parameters.jl 53faee65beda383348580c28d0424188da69b660, original hadron table blob 06d0883a27b108692720422294ba2baacd381a64. Same default solver, original magic return Y_code=0.251 target. STD changes ONLY active d_m_PBH_dt line to -0.5817518 * N_PBH * NU.m_Pl^4 / m_PBH^2. Common instrumented return of solution for lifetime permitted. Do not patch charge rates. No H2 test. Original source index j zero-based, use j+1.

Six arms base/std at j16,22,62. Each starts six fixed log10beta nodes -21,-20,-19,-18,-17,-16. If upward crossing exists, first bracket, four bisections, linear root in last interval. If no crossing report none; below-grid distinct. Maximum 60 native calls, no retries. Report all sampled values, retcodes, first-evaluation evaporation times (dense-solution cutoff, not physical lifetime outside model), bracket and root. Reject nonfinite / non-Success. Compare independently computed CSV root against recorded root. G_BASE j22/j62 against published author JLD2 owner references -17.2202/-19.3892 within .05 dex; G_TAU within 1% of 1/R for all three; G_MONO coarse downward tolerance 3e-4. G_REPLICA independent shift versus owner -1.3837963852952981 and -0.24378020723688465 within .03 dex, std j16 root within grid; report base j16 status. Gate failure not proof of physical null. No rigorous continuous root error claimed. Owner's G_REP failure not silently upgraded. Reproduction of same code, not new independent physics implementation.

Environment inherited Mech-S10 T2R Julia 1.12.3 and setup_env.jl blob db9b5c8a462933d329136de572d5d3478de8612b; pin direct dependencies and NaturalUnits revision; capture resolved Manifest and package status, not assert identical transitive resolution without comparison. If source/runtime/calls fail preserve failures and STOP. No physical transfer, no BW write. No H2 elimination rule. No new data yet.
