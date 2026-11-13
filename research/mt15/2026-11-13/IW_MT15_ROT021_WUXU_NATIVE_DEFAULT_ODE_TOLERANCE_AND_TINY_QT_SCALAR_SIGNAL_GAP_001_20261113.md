---
artifact_id: IW_MT15_ROT021_WUXU_NATIVE_DEFAULT_ODE_TOLERANCE_AND_TINY_QT_SCALAR_SIGNAL_GAP_001_20261113
date: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
type: BOUNDED_INDEPENDENT_SOURCE_NUMERICAL_RESOLUTION_AUDIT
status: ORIGINAL_NATIVE_16_SHA_PASS / DOCUMENTED_DEFAULT_LOCAL_CONTROLLER_SCALE_VS_TINY_COMPARATOR_AUDIT_PASS / RUNTIME_SOLVER_ERROR_HOLD
claim_ceiling: NO_PHYSICAL_PBH_BBN_BOUND / NO_NEW_NATIVE_JULIA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT021: The author original Julia 100-bit native trajectory does not certify 1e-15 reduced-comparator resolution

## Scope, custody and firstness

ORIGINAL: Quan-feng Wu and Xun-Jie Xu, JCAP 02 (2026) 063; frozen public original author code at Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d. Source main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6 uses 10-dimensional source ODE state, including u4=ln X_n. Native parameters blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5 sets BITS=100. The source solves with solve(evolution_problem, AutoTsit5(Rosenbrock23())) WITHOUT explicit reltol or abstol and separately returns 10000 dense interpolated samples. Mech-S9 FIRST native original Julia j22 one-point; LT8 FIRST identified unspecified tolerances and dense sample-count non-equivalence. KN14 FIRST independent cubic mass-clock native drift; MT15 ROT020 FIRST exact saved cutoff-mass invariant failure. INT9 ROT025 FIRST Q/T matched output operator. MT15 ROT017/018/019 FIRST corresponding bounded auxiliary fixed-background scalar Duhamel estimates. No priority or physical novelty appropriated.

AUTHENTIC Mech-S9 original Actions run43436800793, artifact14045176436, original unmodified 713794 byte ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486. Native original 10000-row CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1; original 16/16 internal manifest SHA PASS, ZIP CRC PASS. Original PKG_STATUS actually confirms DifferentialEquations v7.17.0, ArbNumerics v1.6.3, NaturalUnits v0.1.0; native summary confirms BITS100, one original magic() run. All 1456 source postev nPBH-zero saved rows retain six effective-floor flags. No new Julia run or code modification.

## Externally documented local controller scale, NOT a measured numerical error

The *version-matched* official SciML docs at https://docs.sciml.ai/DiffEqDocs/v7.17/basics/common_solver_opts/ state ODE default reltol=1e-3, abstol=1e-6 and a generic local controller scale abstol+max(abs(u_prev),abs(u))*reltol, for each ODE state coordinate. These local error-estimate scales are NOT global error bounds or realized error estimates. Source author code does not explicitly override options; however MT15 DID NOT inspect live integrator.opts in the ArbFloat+AutoTsit5 runtime, so DO NOT claim literal runtime option values verified. 100-bit arithmetic improves number representation, not demonstrated physical solution convergence to 1e-15.

Correct source coordinate is u4=ln X. The earlier ROT019 conditional scalar signal is D = original source clamped X - a separately defined SAME-T frozen-background weak-only auxiliary W. It is NOT a second full 10D unclamped solution or physical delta Yp. At the two original Q/T source readout targets, compute source x directly from the original decimal native CSV by the original linear-in-Q/T map, not from prior printed estimates. The corresponding log-coordinate auxiliary signal is exactly delta_u4=ln x-ln(x-D) = -ln(1-D/x). Compare with the DOCUMENTED NOMINAL local controller coordinate scale epsilon_nominal=1e-6+1e-3*abs(ln x).

T0 original source 0.07818527068831994MeV:
original Q/T-matched x=0.11205517576826312439;
ROT019 conditional D in [2.202762365163523e-15, 2.2056827742579078e-15];
delta_u4 in [1.965783686529e-14, 1.968389910716e-14];
epsilon_nominal=0.00218976388820661284.
RATIO epsilon_nominal / MAX(delta_u4)=**1.11246449511e11**.

T1 corrected Badacz 0.0996888512474581MeV:
source Q/T-matched x=0.12588190883956387806;
ROT019 conditional D in [1.2216118477080871e-15,1.2231916290604223e-15];
delta_u4 in [9.704427419074e-15,9.716977128297e-15];
epsilon_nominal=0.00207341104293868563.
RATIO epsilon_nominal / MAX(delta_u4)=**2.13380253505e11**.

These ratios demonstrate SOURCE-CONDITIONAL SCALE MISMATCH. They do NOT measure error, prove that the original solver committed an error of a given size, establish that scalar ROT019 mathematics is wrong, or imply a physical helium error. They show why the unvalidated original solver output cannot establish a physical source-native correction to X_n of order 1e-15 merely from the precision of its output.

## Source cutoff numeric invariant distinct cross-check

The original j22 mass cutoff from source is Mstop=2.3109127923407016g; native frozen M=1.47268711730633g. Its recorded exact ODE half-space invariant violation is delta ln M=-0.4505538916409737 (MT15 ROT020 FIRST). Nominal documented log mass coordinate at frozen ~55.071023 natural GeV gives epsilon_nominal ~0.055072, so discrepancy/nominal scale ~8.181. This compares a terminal event discontinuity/cumulative discrepancy to a *local control scale* of a DIFFERENT source coordinate, and is NOT evidence that any accepted individual solver step violated its controller. KN14 independent cubic clock drift is separate; do not confuse the two.

At original native final row X=1.68560917680474e-11, u4≈-24.8063 and nominal documented local scale≈0.0248073. Original six raw log hadron states fall massively below -100, so their own local controller scales also differ across source states. This underscores the need for separate source component tolerances and direct actual integrator-step records, not numeric digits or output-point count alone.

## Reproducibility and gates

Actually executed independent local Python Decimal80 source forensics (SHA256 6b1dc30b70d5bf3e4321ceb94a634976bd6a0ac29a7b2e2761bbc0a84a88ed98) on untouched owner native zip, original full output JSON SHA256 7a75464e415be376808c7f2daccfa80ea2e108a8dbf1b9798b5a2b5021d86569. Independently executed verifier SHA256 6daa93346a9ecac04ba727a60269d937a8e2029fd22082549d84392ad4b50176 checks all original SHA, complete byte-identical replay, 1500 seeded independent Decimal log-scale algebra probes, single-byte mutated original ZIP fail-closed PASS. Complete standalone original source embedded user-conversation ZIP 723149 bytes SHA256 d6479e40c06ce0cae4bf6d596898d3e42c12e3e72f0c3d9fdd8bbdcd623eba3b: source owner ZIP, executed code, output JSON, verifier, README and manifest 5/5 SHA PASS, outer ZIP CRC PASS. Extracted into fresh CLEAN directory; all checks and JSON byte-identical original replay PASS. The ZIP remains conversation-local, not asserted GitHub or BW binary storage.

G1 future original B1 physical execution is governed by explicit Moderator approval per Julia run with Badacz+Mech-S9 native owners. For a defensible code-corrected X_n(T0) claim: freeze legal beta<=original scan max, original Q/T readout, source generator uncertainty below first 1e9g node, save actual integrator.opts, accepted/rejected step counts, source event handling and tolerance convergence. No auto-run, not even for a pure hypothetical floor perturbation. No actual native ODE error bound certified; no physical PBH exclusion; no external novelty, no CANON/EXEC_SIGN or BW writeback claim.

VERDICT: ORIGINAL_NATIVE_SOURCE_AND_PKG_VERSION_PASS / DOCUMENTED_NOMINAL_LOCAL_SCALE_GAP_1E11_PASS_CONDITIONAL / TRUE_RUNTIME_TOLERANCES_UNVERIFIED / SOURCE_SOLVER_CONVERGENCE_HOLD / E4_SOURCE_HOLD / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
