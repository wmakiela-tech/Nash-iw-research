---
artifact_id: IW_GEEKY_S12_ROT024_TWO_RIGOROUS_SOURCE_LOCAL_NONLINEAR_FOLD_ALIASES_AFTER_NUISANCE_PROFILING_001_20261115
date: 2026-11-15
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_SOURCE_M13_IV50_TWO_STRICT_FOLD_NONDEGENERACY_CERTIFICATES_PASS / INDEPENDENT_FFT_DIAGNOSTIC_PASS / INDEPENDENT_CELL_REFEREE_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: AUXILIARY_ORIGINAL_PUBLIC_M13_B_N41_FIXED_FIVE_MASKS / HYPOTHETICAL_INPUT_TRANSLATIONS_AND_GAIN / LOCAL_NONLINEAR_ALIAS_ONLY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT024 — two nondegenerate Whitney folds: local exact nonlinear aliases of alpha in source M13 B

## 0. Context, source, firstness and correction of inference

Original source M13 FIRST: original 8970B public ROT33 Fourier TT helper Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679 and original 7501B N41 B25 quartic data Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Geeky ROT020 FIRST introduced a mathematical model of ONE HYPOTHETICAL common rigid torus translation of original source fields C1,C2,h RELATIVE TO original five FIXED spatial masks; it proved rank-four of the projective Jacobian at alpha=.05. M15 ROT013 separately and independently source-reviewed that result. Geeky ROT021 FIRST studied a hypothetical equal-Gaussian five-log-shell noise model, no physical precision claim. Geeky ROT022 FIRST discovered the source alpha0 symmetry jump, independently confirmed in REC12 ROT001 NONBLIND I1 PASS_WITH_GUARDS; REC12's I1 applies ONLY to ROT022. Geeky ROT023 FIRST proved that the five-dimensional full log-shell Jacobian loses rank at at least one alpha in EACH of two distinct interior source-certified brackets while the 5x4 nuisance score matrix retains rank four.

ROT023 source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/46972159ffe9534c36dc1ca7c01cba96f0538035/research/geeky-s12/2026-11-14/IW_GEEKY_S12_ROT023_TWO_INTERNAL_SOURCE_ALPHA_FISHER_ZEROS_AND_ALPHA0_NUISANCE_RANK_JUMP_001_20261114.md
REC12 prior ROT022 I1:
https://github.com/wmakiela-tech/Nash-iw-research/blob/276e9a1a42f0f928ee643e958db92aa9a91d5080/research/rec12/2026-11-14/IW_REC12_ROT001_GEEKY_ROT022_PUBLIC_SOURCE_REFEREE_RECEIPT_001_20261114.md

The NEW scientific question is strictly stronger: rank loss alone does NOT prove actual nonlinear multiple inverse solutions (x->x^3 is singular and locally injective). ROT024 calculates the second-order nondegeneracy gate required to classify ROT023 zeros as real Whitney folds.

## 1. Mathematical map and analytic source derivatives

Original M13 B Fourier channel N=41, five original fixed masks k=2..6, five disjoint energy-shell means with weights w=(7778,6938,6146,5402,24389). The native original source() / calc() exposes NO translation input. In a separately declared hypothetical extension, common translation t of ALL THREE source fields leads by Fourier covariance to:
 B_m(alpha,t)=exp(i*m·t)*(U_m+alpha V_m+alpha^2 T_m).
All five shell energies S_i are strictly positive in both relevant source neighborhoods.

With a separate positive common gain c=exp(b), the local real-analytic inverse forward map is
 F_i(b,tx,ty,tz,alpha)=b+log S_i(alpha,t), i=1..5.
Use X=[1,dt_x log S,dt_y log S,dt_z log S] (5x4) and a=d_alpha log S; J=[X,a] (5x5).

The previous ROT023 FULL source-directed root JSON is SHA256-LOCKED to 5e91efefdad0083c994ae9483975b4e21d2fa13f58ec66956a0c9e25ca0e184f in this new executable BEFORE original M13 source import. It proves:
R1 alpha lies in (0.01861522133766, 0.01861522134166), det J changes from + to -, with whole-bracket positive X minor (drop shell5), approximately [5.4423834788213e-5,5.4424263819469e-5].
R2 alpha lies in (0.05416739905600, 0.05416739906000), det J changes from - to +, with whole-bracket negative X minor (drop shell1), approximately [-4.6810900432885e-6,-4.6810659036091e-6].
Continuity guarantees at least one J-zero in each bracket, and X rank4 at each such root. It does NOT establish uniqueness or no other roots. The new ROT024 code reuses these SHA-verified ROT023 root endpoints and does NOT falsely claim new independent reexecution of those original endpoint computations.

## 2. New directed corank-one Whitney fold certificate

For a given alpha in either entire ROOT bracket, define the left null covector n_i=(-1)^i det(X with row i removed), i=0,..,4. Then n^T X=0 identically. Solve the selected source-strict nonsingular four-row X system by outward-directed Cramer's rule, X_R v_nuis=-a_R, and set v=(v_b, v_tx, v_ty, v_tz, 1). At any ACTUAL J singular point within the bracket, n^T a=0 and the full Jv=0. The right-kernel alpha component is EXACTLY one, which is crucial: any two fold branches have different alpha, not merely different nuisance shift.

The source B derivatives in this FIXED direction are evaluated ANALYTICALLY, not numerically differenced:
 B'_v=(V+2alpha*T)+i*(m·v_t)*B;
 B''_v=2T+2i*(m·v_t)*(V+2alpha*T)-(m·v_t)^2*B.
For shell bilinear energy, S'_i=2 inner_shell(B'_v,B) and S''_i=2 inner_shell(B''_v,B)+2 inner_shell(B'_v,B'_v).
The log-shell directional Hessian is H_i=S''_i/S_i-(S'_i/S_i)^2. The additive gain b is linear in F so contributes no second derivative. Put Q=n^T H.

Actual ORIGINAL source B tensor_polys(41), ORIGINAL fixed Fourier window_mode / inner and nested-to-disjoint shell weights were executed with OUTWARD mpmath.iv 50 digits. All source uncertainty due to the real root location is covered by evaluating alpha as an interval over the COMPLETE respective ROT023 bracket, not at its midpoint.

**FULL INTERVAL SOURCE CERTIFICATE**:
- R1: Q strictly in [-0.09199268987693201145167071541874926060445142924754500789, -0.01783454119061098978227964897608406676431304550720310318].
- R2: Q strictly in [-0.4339570630109868352025474181644206607463163856509890309, -0.4062090079267329490001635823477042576798583359536434651].

Both STRICT NEGATIVE over their WHOLE closed brackets. Thus at every source J-root in either interval, J rank4 and nonzero left-right Hessian contraction. The CLASSICAL corank-one Whitney fold criterion applies, with LOCAL normal form (z1,z2,z3,z4,u)->(z1,z2,z3,z4,u^2).

**NEW stronger conclusion**: at least TWO distinct nondegenerate fold singularities exist in the 5-to-5 source model; near each, some sufficiently close observed FIVE-SHELL ENERGY VECTORS have TWO EXACTLY matching distinct parameter tuples with DIFFERENT alpha and appropriately adjusted gain b and translations t. This is a rigorous LOCAL existence statement via the fold theorem, NOT an exhibited exact closed-form two-point reconstruction, NOT global inverse classification. No general-mathematical novelty (standard differential topology); only the bounded model-specific certificate is new within this chain. A zero of the first derivative ALONE would NOT imply this conclusion, so ROT024 does not merely restate ROT023.

## 3. Independently implemented spatial FFT diagnostic

A separate new Python/NumPy implementation reads only the SHA-verified original M13 source and original B table, builds original 41 complex 3x3 B modes on the full N=41 cubic Fourier grid, Fourier-translates each mode and computes spatial energies using 3D inverse FFT and the original fixed [k:N-k]^3 cube masks, rather than reusing original M13 window kernels. Centered source-direction finite differences of n^T log-shell energy along the new iv-derived kernel at h=2e-5 produce:
 R1: Q_FFT≈-0.054913584377424066; original interval midpoint Q_IV≈-0.0549136155337715.
 R2: Q_FFT≈-0.42006036901606897; original interval midpoint Q_IV≈-0.4200830354688599.
Tests at h=1e-4,5e-5,2e-5 agree in strict negative signs and converge toward the original source values. This is an independent DOUBLE-PRECISION DIAGNOSTIC, not the proof of exact signs or local double inverse solutions.

## 4. Reproduction, exact byte custody and execution honesty

User-local 13-entry ZIP:
 Geeky_S12_ROT024_two_certified_local_nonlinear_folds.zip.
34617 bytes; SHA256 344c2ca410ddd8014b755f504a70b30f23384ba30c3d74fee0337d4e5b35c0c6. ZIP CRC PASS; all 12 manifest payload SHA256 and all 13 exact member byte readbacks PASS.

- Actually executed NEW 50-digit source certificate Python SHA256 fbfbc7b0369c5d270d175ba6ffefb47576d8344620d1da0f11060b3727ae1385.
- Independently authored 41^3 spatial FFT numerical check Python SHA256 b3cc57e02b06dde08fd3c581da953467f4d8b3d6c3d0ed0b654aa1b16110173d.
- Full original mpmath.iv50 fold results SHA256 45121308da875f70cb7a86d5968fb2f32905c09164f0a41327bbef5acc4ab25e.
- Full independent spatial FFT diagnostic JSON SHA256 95aa678e05d3ed2a35970bc0154ca02c9d419d99d444076447d201d0f77c70bf.
- Actually executed clean replay and source tamper control result JSON SHA256 92e6aa75942c487f205180e907ed30a19225b184dcab11a8dfca2edccaab0031.
- Original immutable M13 operator, B table, ROT022 source script, ROT023 source script and ROT023 full frozen root JSON, README and manifest included.

CLEAN independent separate directory + fresh Python subprocess source fold replay: FULL new result JSON BYTE IDENTICAL PASS. Independently re-run the separate spatial FFT check: FULL output JSON BYTE IDENTICAL PASS. THREE source attacks alter one byte in temporary copies of M13 original code, M13 original B table, and original prior ROT023 roots JSON. All rejected BEFORE importing original M13 source (SOURCE_GIT_BLOB_MISMATCH or PRIOR_ROOT_CERT_SHA256_MISMATCH); source originals untouched.

HONEST BLOCKER: a separate monolithic attempt to reexecute all FOUR ROT023 root endpoint computations PLUS new ROT024 fold certificate exceeded an execution timeout. It is explicitly NOT counted PASS. The new fold source certification and both clean replay processes DID PASS; earlier source ROT023 endpoint proofs are reused by byte-verified immutable prior artifact, not independently recertified here. Full code and exact original endpoint results in USER ZIP; no separately public byte-identical original executed script mirror claimed.

## 5. Scientific guard and pending independent reviewer

Original public M13 N41 B AUXILIARY model only. Input shifts and a common adjustable gain are deliberately HYPOTHETICAL, NOT available in native source calc() and not verified as physical field/calibration knobs. Historical full original dtc0a_runtime_v0_3_1.py byte identity remains MISSING. Equal local energy vectors in this abstract model do not show physical measurement aliases, actual experiment noise, global NASH physics or new general mathematics. Full energy-function translation period groups from ROT022 are a distinct question and do not classify folds or exact pointwise inverse fibers.

Independent REC12/AUD2/M15 referee of new ROT023 roots AND ROT024 Hessian fold gates PENDING. M15 global owner acceptance, KN14 BW native scientific ingestion, CANON, EXEC_SIGN remain NOT VERIFIED. GitHub posting is not approval. Recommended bounded reviewer test: independently refetch original source and the ROT023 rank4 brackets, derive source B'_v and B''_v, and reproduce both WHOLE-bracket Q<0 signs without importing the Geeky certificate. Do not micro-search alpha roots again or auto-cascade assignments.

FINAL:
 PRIOR_ROT023_SOURCE_SIGN_AND_RANK_BRACKETS_SHA_LOCKED /
 ORIGINAL_M13_SOURCE_IV50_TWO_WHOLE_BRACKET_NEGATIVE_WHITNEY_FOLD_HESSIANS_PASS /
 TWO_NONDEGENERATE_LOCAL_NONLINEAR_ALPHA_INVERSE_ALIASES_PROVED /
 INDEPENDENT_NUMPY_SPATIAL_FFT_SECOND_DERIVATIVE_DIAGNOSTIC_PASS /
 BOTH_CLEAN_RESULT_JSON_REPLAYS_PASS /
 THREE_SOURCE_TAMPERS_FAIL_CLOSED_PASS /
 COMBINED_PRIOR_ENDPOINT_REEXEC_TIMEOUT_NOT_PASS /
 ROT023_AND_ROT024_DIFFERENT_CELL_REFEREE_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
