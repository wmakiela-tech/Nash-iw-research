---
artifact_id: IW_MECH_S10_T2R_NATIVE68_PREREG_001_20261120
cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-20
status: FROZEN_BEFORE_NATIVE_EXECUTION
authorization: MODERATOR_DIRECT_COMMAND_20261120_1449_EUROPE_WARSAW
claim_ceiling: NO_PAPER_ERROR / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---
# Mech-S10 T2R: one independent 68-call Wu-Xu native Julia re-execution

The Human Moderator directly instructed Mech-S10 on 20 Nov 2026: "Wykonaj niezależna replike obliczeń T2 w wykonaniu Mech-S10". This is explicit transfer/reissue of the previously authorized one GPT-family 68-call T2R from Mech-S9 to Mech-S10, following Badacz SYNTH074 r2 consent. Earlier Mech-S9 ROT031 source-only arithmetic is NOT a native T2R. Latest inspected GitHub issue#16 and T2R commits did not identify another native executor. If this workflow fails, record failure; never launch automatic duplicate or unapproved retries.

Original Wu-Xu source Git commit d395183674cace6c9906a8911bdeb7234ba4040d. Original main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6; main-scan-parameters.jl blob 53faee65beda383348580c28d0424188da69b660; tool_script-parameters.jl 0d7198ff3557bdbd5753000bb07a7a7405cc24f5. Julia 1.12.3, independent GPT-family runner, source setup_env.jl at Git blob db9b5c8a462933d329136de572d5d3478de8612b (ArbNumerics 1.6.3, DifferentialEquations 7.17.0). Original source magic(m_PBH_f_list[j+1], ArbFloat(10.0^lb; bits=BITS)) output final author Y_code; use unchanged default solve, target 0.251. E5 exactly Mech-S6 original charge-pair source patch Git blob 4d1f2be94510c576e4f48752911f88ede8b50474: inject one-half of pi+/-, K+/-, proton+antiproton, neutron+antineutron group rates per tracked hadron; K0L unchanged.

EXACT 68 CALLS, one workflow/job, one native executor:
j22 original -17.38,-17.36,...,-17.06; j22 E5 -17.10,-17.08,...,-16.78.
j62 original -19.54,-19.52,...,-19.22; j62 E5 -19.26,-19.24,...,-18.94.
Each of 4 combinations has 17 steps of 0.02 dex. The exact author prereg grid files are research/badacz/2026-11-16/code/cfg069_orig_default.dat Git blob 985dbd074f2a4d8e48d6a47fb94e6a30a7550bc3 and cfg069_e5_default.dat blob e10df7d3a5c3019010da7e5906fd16a6c823baea. No j28/38/51/90, no reltol=1e-4, no grid extension or other source changes.

FROZEN EVALUATION:
- 68 actual native calls exactly once; source and configuration hashes must pass; original 10D author solver (last composed magic) unchanged except E5 injection patch.
- Every 17-point series must bracket target 0.251 exactly once.
- Standalone precommitted Mech-S10 analysis computes independent 7-closest-points centered OLS roots for both j, both arms; delta D_j = root_E5 - root_orig.
- R-SHIFT PASS if abs(D22 - 0.2722992609128987) <= 0.010 dex AND abs(D62 - 0.29812358518660886) <= 0.010 dex (preexisting Badacz owner native result verified by distinct-source replay, not new native output).
- Descriptive R-BIT: Y numeric 17-significant-digit text matches against previous owner CSV rows, without altering shift gate.
- Preserve actual native CSV, stdout/stderr, upstream commit, environment, output manifest. No success claim before source-native execution and readback.

SCIENTIFIC CEILING: native replication of two exact indices and the specific original-vs-E5 model intervention; cannot establish physical paper error, universal charge convention, E4 generator validity, physical PBH exclusion, new physics, novelty, CANON or EXEC_SIGN. Historical Kohri/Yokoyama charge-state semantics remain OPEN. No new BlackHawk run or experimental expansion.
