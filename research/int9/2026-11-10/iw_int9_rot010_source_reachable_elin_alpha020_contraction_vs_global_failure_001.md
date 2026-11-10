---
artifact_id: IW_INT9_ROT010_SOURCE_REACHABLE_E_FILTER_CONTRACTION_VS_GLOBAL_FAILURE_001_20261110
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-10
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: AUX_HELPER_SOURCE_GENERATOR_ONLY / NO_HISTORIC_PRODUCER / NO_GENERAL_KA_THEOREM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# INT9 ROT010 — positive reachability-restricted E_lin at alpha .2 despite global noncontraction

## Priority and source types

Moderator-frozen diagnostic data `dtc0a_oddN_sparse_convergence_N31_to_N41_manifest.json` cover odd N=31,33,35,37,39,41, E_lin stencil2, alpha=0,.05,.2, interior_k=3. Historical `dtc0a_runtime_v0_3_1.py` SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084` still NOT available byte-identical. Source helper is unchanged user's `deepseek_python_20260627_a87249.py` SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, actually imported and run. EKS1 ROT002 FIRST located the original Colab notebook; KN13 ROT006 FIRST found notebook cell17 Python AST identical to this helper; SYSS6 migrated original notebook private. Source lineage is NOT historic runtime identity.

INT8 ROT046 FIRST proved centered-Lie vs RAW Fourier TT symbol mismatch. INT8 ROT051 FIRST proved positive intermediate-filter z-Fourier source dark fibers on a DISTINCT input H(z) class and alpha<=1/6:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-11-02/iw_int8_rot051_exact_stable_filter_dark_fibers_full_z_kernel_001.md
INT9 ROT009 FIRST directly verified global E_lin L2 expansion at historic alpha=.2:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e2e5ba83c4c99d8ac4795a964b3fbaf827d08d60/research/int9/2026-11-10/iw_int9_rot009_dtc0a_elin_alpha020_global_l2_noncontraction_and_historic_source_gate_001.md

Distinct ROT010 target: **the exact Fourier input supports encountered by E_lin within SOURCE-AUX `generate_smooth_fields` followed by source-aux full `compute_K_A_out`**, and whether E is expansive THERE. No claim of novelty or historic execution.

## Typed exact support argument

The unchanged helper generator sets C1=(.05sin x,.05cos y,0), C2=(.04cos z,0,.04sin x) and h=.1sin x cos y * I3. Their signed discrete Fourier supports at odd N>=7 are
H={(±1,±1,0)}, S1={(±1,0,0),(0,±1,0)}, S2={(±1,0,0),(0,0,±1)}.

The literal `compute_K_A_out` calls original `apply_E` FIVE times: h (three times), projected_T(C2,h), projected_T(C1,h). Centered derivatives and original RAW-k TT projector are Fourier-diagonal, preserving frequency support, while multiplication by the shears shifts at most by source S1 or S2. All E inputs therefore have spectral support within
R=H UNION (H+S1) UNION (H+S2),
a 24-frequency signed set with max|k_i|<=2. This exact support restriction depends on the source generator, NOT any high-frequency smallness assumption. It is an exact finite Fourier-support statement; the 24 modes form the possible superset, not a claim all always have nonzero coefficient.

E_lin has original literal Fourier multiplier e_N(k,alpha)=1-4alpha SUM_i sin²(pi*k_i/N). For alpha=.2 its bounds on R are SHARP:
min_{k in R} e_N(k,.2)=1-.8[sin²(2pi/N)+sin²(pi/N)] >0,
max_{k in R} e_N(k,.2)=1-.8 sin²(pi/N) <1.

Hence **E_lin restricted to fields supported in R is a strict L2 contraction** for all historical odd N31..41, even though its UNRESTRICTED L2 operator norm exceeds 1.39 by ROT009. The full-grid high corner mode is NOT in R.

|N|E_.2 minimum on R|E_.2 maximum on R|unrestricted ||E_.2|| L2|
|---:|---:|---:|---:|
|31|0.9593951011|0.9918119765|1.3938431881|
|33|0.9641186521|0.9927714789|1.3945663071|
|35|0.9680657837|0.9935718354|1.3951691528|
|37|0.9713973423|0.9942463641|1.3956769863|
|39|0.9742346818|0.9948201051|1.3961087698|
|41|0.9766707263|0.9953121695|1.3964789614|

## Original helper executable full K_A source control

SHA-verified original helper's `generate_smooth_fields(N,2*pi)`, `compute_K_A_out(C1,C2,h,'E_lin',dx,2,alpha)` and `rms_norm(out,slice(3,N-3))` were actually run on **N31 and N35**, for alpha 0,.05,.2. An outer-only instrumentation wrapper recorded FFT input to EACH unmodified original E call and checked that every frequency belongs to R. Stage nonzero-support sizes 4,12,4,8,4 at every run. Original E output FFT divided by the expected eigenmultiplier for every active mode agrees with relative error less than 5e-16. This is real source-code execution, NOT a new historical production run.

|N|alpha|masked 3-interior auxiliary K_A RMS|full all-9-coordinate RMS|
|---:|---:|---:|---:|
|31|0|3.788529759260593e-5|3.311733472356171e-5|
|31|.05|3.764756853208360e-5|3.291860136411103e-5|
|31|.2|3.694723525796834e-5|3.233104493910561e-5|
|35|0|3.815297095716949e-5|3.321582740766242e-5|
|35|.05|3.796625718750918e-5|3.305938800505109e-5|
|35|.2|3.741397506696358e-5|3.259544546164760e-5|

Observed masked RMS ratios alpha.2/0 are 0.9752394096325994 (N31) and 0.9806307117986826 (N35). These are **particular generated-field observations**, not a theorem about all h,C or operator norm of K_A. A broad N41 full helper run exceeded execution timeout: **NO PASS** there; N33,37,39,41 have MATH-ONLY spectral certificate, no full native K_A replay.

Independent stdlib frequency-support verifier, without NumPy, FFT or original helper, checked all 18 combinations of six historical Ns and three alphas. The full helper native script and stdlib script generate frozen strict JSON. Complete Moderator-local eight-member ZIP: SHA256 `913961e0501b9d88e29ed3658bb7e44ec82d34e6f44fdd92eefdda2489015387`; 7 SHA256 payloads PASS, CRC PASS, clean independently extracted full rerun produced BOTH source and math JSON BYTE IDENTICAL. Full local report SHA256 `406db090f948e62c1fd08c0cf62045473a4f0f8695dc8ff1dc290c51a327e4de`. Original helper NOT included in ZIP and needed separately for native script.

## First unsupported transfers / currentness

**Valid:** original auxiliary source generator -> reachable supports -> E multiplier contraction **on E inputs** -> native observation for two input grids. ROT009 global instability stands, with no contradiction.

**Invalid:** per-E contraction -> all-input nonlinear composed K_A contraction, because different summands may cancel differently; actual two-grid attenuation does not establish a universal K_A norm. Even less may it imply truth or falsity of historical masked producer diagnostics or any J3/K/GR/GW physics.

**Separate contemporaneous referee correction:** REC11 ROT011 independently refined sharp nominal fit-SE thresholds of rank loss for Badacz REVIEW050 C/D inverse. This supports only conditional INT9 ROT008 forward-vs-inverse target typing and does NOT enter this DTC spectral calculation. Source A1 finite-amplitude deviations from Badacz REVIEW054 also remain open; not a physical PBH limit.

No owner ACK, independent referee of ROT010, BW ingest, canonicity or execution signed by this dispatch. Per owner contact protocol, stop rather than multiplying source-absent experiments.

**FINAL:** `REACHABLE_SOURCE_E_CONTRACTION_PASS / ALPHA020_GLOBAL_E_NONCONTRACTION_RETAINED / SOURCE_NATIVE_N31_N35_PASS / N41_NATIVE_TIMEOUT_NOT_PASS / HISTORIC_KA_RUNTIME_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
