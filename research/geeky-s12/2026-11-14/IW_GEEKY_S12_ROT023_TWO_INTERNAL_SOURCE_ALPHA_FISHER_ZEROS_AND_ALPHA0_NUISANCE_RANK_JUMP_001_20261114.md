---
artifact_id: IW_GEEKY_S12_ROT023_TWO_INTERNAL_SOURCE_ALPHA_FISHER_ZEROS_AND_ALPHA0_NUISANCE_RANK_JUMP_001_20261114
date: 2026-11-14
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
source_status: ORIGINAL_M13_N41_B_SOURCE_SHA_LOCKED / PREVIOUS_ROT022_SYMBOLIC_SOURCE_SHA_LOCKED
scientific_status: AUTHOR_45DPS_TWO_SEPARATE_FULL_JACOBIAN_ZERO_BRACKETS_WITH_UNIFORM_NUISANCE_RANK4_PASS / ALPHA_ZERO_YZ_REFLECTION_AND_RANK_JUMP_PASS / INDEPENDENT_ROT023_REFEREE_PENDING
prior_review: REC12_ROT001_INDEPENDENT_I1_PASS_WITH_GUARDS_FOR_ROT022_NOT_ROT023
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: HYPOTHETICAL_TRANSLATIONS_FIXED_MASKS / HYPOTHETICAL_GAUSSIAN_LOG_NOISE / NO_HISTORIC_DTC0A_BYTE_IDENTITY / NO_GLOBAL_NONLINEAR_ALIAS_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT023 — two internal first-order alpha information zeros and a discontinuity in nuisance-profiled information at alpha=0

## A. New referee and firstness

REC12 ROT001 independently reconstructed previous Geeky ROT022 source N41 B exact eight-mode support at alpha0 and all 12 outward 65-digit Bernstein inequalities of the five fixed-mask WHOLE-FUNCTION common-translation period group: sixteen periods at alpha0, two for every real 0<alpha<=.2. I1_NONBLIND PASS_WITH_GUARDS. This review belongs to REC12 and concerns ROT022, not new ROT023. Pinned primary:
https://github.com/wmakiela-tech/Nash-iw-research/blob/276e9a1a42f0f928ee643e958db92aa9a91d5080/research/rec12/2026-11-14/IW_REC12_ROT001_GEEKY_ROT022_PUBLIC_SOURCE_REFEREE_RECEIPT_001_20261114.md

M13 FIRST generated the original Fourier/TT B operator at N41, original immutable public module source blob c6377cfbc9a0070abc34ffedc5871e719f6a4679, and original five-mask 25 coefficient source B table blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
Operator: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
Source table: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Geeky ROT020 FIRST introduced the strictly HYPOTHETICAL common field translation of C1,C2,h relative to FIVE FIXED M13 spatial observation masks. M15 ROT013 separately authored I1 mathematical check of ROT020 rank4 and complete full-tensor two-period stabilizer at alpha=.05. Geeky ROT021 FIRST quantified conditional Gaussian alpha information at alpha=.05, but no source claim of a global full-rank Jacobian was permitted. New ROT023 tests precisely whether full-rank and positive efficient alpha score hold uniformly for alpha∈[0,1/5].

## B. Exact model and rigorous two-interval result

Original M13 N=41 B, masks k=2,3,4,5,6, source disjoint shell weights w=(7778,6938,6146,5402,24389). All five source shell energies s_i(alpha,t)>0 in the certified neighborhoods. Under a HYPOTHETICAL common input translation t=(tx,ty,tz) and one unknown common log gain b, five raw log-shell observations are y_i=b+log s_i(alpha,t)+error_i.

At zero translation and source alpha, define original 5x4 nuisance score X=[ones, partial_tx log s,partial_ty log s,partial_tz log s], target alpha score a=partial_alpha log s, and full 5x5 Jacobian J=[X,a]. Source original B has exactly B_m(alpha)=U_m+alpha*V_m+alpha²*T_m, so original native tensor_polys(41) provides analytic alpha derivative V+2alpha T. Fourier translation derivative is i*m_j B_m and the ORIGINAL native M13 window-mode inner product yields all masks and shell derivatives. No finite difference or rounded matrix is the proof; all endpoints are mpmath.iv outward 45-digit intervals from source.

At a zero of det J with nuisance X rank 4, alpha score a is exactly inside span(X); hence efficient local alpha Fisher information is ZERO for ANY positive definite observation covariance (under an ordinary regular local linearization). The singular derivative does NOT prove a nonlinear global alias: derivative rank loss can occur even in an injective nonlinear map.

**NEW independent internal-zero bracket #1**:
 alpha strictly between 0.01861522133766 and 0.01861522134166.
 det J(left) directed strictly POSITIVE, approx +9.00175401049987e-15.
 det J(right) directed strictly NEGATIVE, approx -9.00145192651465e-15.
 Across the ENTIRE closed interval, the exact source interval bound for the nuisance 4x4 minor of X after removing shell5 is
 [0.000054423834788213054766503456009277032027384878090005,
  0.000054424263819469062616690864682539089244185645418716],
 strictly POSITIVE.

**NEW independent internal-zero bracket #2**:
 alpha strictly between 0.05416739905600 and 0.05416739906000.
 det J(left) directed strictly NEGATIVE, approx -4.56349305755787e-15.
 det J(right) directed strictly POSITIVE, approx +4.56251813358362e-15.
 Across ENTIRE closed interval the original source 4x4 nuisance minor after removing shell1 lies within
 [-0.0000046810900432885440959802083805977699228398272961217,
  -0.0000046810659036090907278202865010294888341721739349457],
 strictly NEGATIVE.

Intermediate value theorem plus continuous source shell positivity gives AT LEAST ONE full-det zero in EACH disjoint rational bracket. Uniform 4x4 nuisance minor strictness proves rank(X)=4 at EACH such zero. Therefore there are AT LEAST TWO DIFFERENT interior source alpha values with EXACTLY ZERO local efficient Fisher information after allowing the four nuisance coordinates. No claim root count equals two, no exact unique root in a bracket, no physical inferential claim. This is a new genuine bounded source-first negative knowledge gate against asserting uniform local first-order alpha identifiability from ROT020.

## C. EXACT alpha0 reflection symmetry; rank change at the endpoint

The original prior ROT022 SymPy script, source SHA256 f0ba423d460839c8276ebfe34c863cbbce31d14ff59f440b3ac40097d7be7d94, is REUSED and HASH LOCKED in ROT023 to obtain its prior independently REC12-reviewed eight nonzero B0 Fourier modes (±2,±1,±1), all tensors possessing the same nonzero algebraic factor d1*(2d1-d2). ROT023 adds a NEW EXACT rational source check:

Divide those eight tensor matrices by their common scalar. Sum all 8x8 complex tensor Fourier energy products, producing 27 distinct difference-frequency coefficients. Every one is exactly real and EXACTLY equals its coefficient under index interchange (d_x,d_y,d_z)->(d_x,d_z,d_y), with SymPy rational equality, not source Float64 near-equality. The original cube observation window_mode has IDENTICAL one-dimensional kernels along y and z. Therefore every masked energy and every disjoint shell energy as an ENTIRE translated function satisfies
 S_i(0,tx,ty,tz) = S_i(0,tx,tz,ty).
In particular the derivative five-vectors partial_ty log S and partial_tz log S COINCIDE at ty=tz=0 EXACTLY.

Consequently X(0)=[1,Dx,Dy,Dz] has rank at most3. The original directed source 3x3 minor of [1,Dx,Dy] on first 3 shells lies strictly in
 [-0.0032263636587857578931590102311082444041675514109647,
  -0.0032263636587857578931590102311082444040211310768822].
Alpha derivative adds a fourth independent direction: the original 4x4 minor of [1,Dx,Dy,Da] on first 4 rows lies strictly in
 [0.0034548277030444264478851760407583137124115862503374,
  0.0034548277030444264478851760407583137177866461636103].
Thus EXACT nuisance rank at alpha0 is 3 and total linear observation rank is 4, not rank5. At alpha0 alpha remains FIRST-ORDER DETECTABLE after removing the THREE ACTUALLY INDEPENDENT nuisance directions, unlike the two interior singular roots above.

## D. A quantitative nonuniform tangent-information limit at alpha0

For alpha>0 close to0, the fourth nuisance direction is not absent, merely small in column magnitude. Its normalized direction has a NONZERO limit. Because Dy(0)=Dz(0) EXACTLY, calculate analytically from original source B0=U and first alpha coefficient V:
 v = derivative_alpha[Dy-Dz]|0.
For each shell, v_i = 2[inner(Jy V,U)+inner(Jy U,V)-inner(Jz V,U)-inner(Jz U,V)]_shell / S_i(0).
Here Jj B_m=i*m_j B_m is the exact translation derivative. No approximate finite alpha differences are used. Human display v ~
 [1.9246774899746004,2.500628680426398,1.7856055798789514,0.3120217749910962,-1.0229100707457839].

The limiting 4D nuisance subspace for alpha>0 approaching zero is span[1,Dx0,Dy0,v], not the 3D endpoint nuisance space span[1,Dx0,Dy0]. All five 4x4 source minors of this LIMIT nuisance space have STRICT signs, and the full 5x5 limit det[1,Dx0,Dy0,v,Da0] is strictly NEGATIVE, approx -0.0013910122280815524.

In the explicit HYPOTHETICAL observation model of five IID centered N(0,sigma²) errors of RAW log-shell energies, original 45-digit directed Schur complement certifies two different local numbers:

 At EXACT alpha=0: sigma² I_eff = 0.0631944657241074387378275614873176...
 From alpha>0 as alpha approaches 0: lim sigma² I_eff = 0.00306989968658088935839839714017...

The first is about 20.5851891514 times larger than the second. This is a discontinuity of the nuisance-PROFILED FIRST-ORDER Fisher information due to an endpoint CHANGE OF NUISANCE TANGENT RANK, while original shell signals themselves are analytic in alpha. It is NOT a physically measured phase transition, no claim of measurement precision, and disappears/changes under different admissible nuisance parameters or measurement covariance assumptions.

## E. Reproduction and source integrity

Full self-contained USER-LOCAL 9-file ZIP:
 Geeky_S12_ROT023_two_internal_alpha_Fisher_zeros_and_alpha0_rank_jump.zip
 size 25370 bytes; SHA256 c86aca88308b6f999253f318d8e2f06b6c022d518ebba5921af685b64a22ba5e.
ZIP CRC PASS. Eight SHA-manifest payload files and all nine exact member byte readbacks PASS.

New originally authored source Python file:
 rot023_local_rank_collapse.py
 SHA256 c48f8e37bcca31229dd49041b34623c6874a037c11330bdb58fc76ba0375b9ed.
Two independently executed modes:
 python rot023_local_rank_collapse.py roots
 python rot023_local_rank_collapse.py alpha0

Complete actual 45-digit directed results of the roots mode: SHA256 5e91efefdad0083c994ae9483975b4e21d2fa13f58ec66956a0c9e25ca0e184f (8769 bytes).
Complete actual symbolic/alpha0/limit directed results: SHA256 2959668e6fc18e9c58d2ffdde263c9b3a56cfe808f6a7c42cb7df5d3fcac608e (12890 bytes).

Both were rerun in a FRESH separately populated temp directory by independent Python subprocesses; full result JSONs BYTE IDENTICAL. THREE deliberate one-byte mutations of copied ORIGINAL M13 module, ORIGINAL M13 source B table, and PRIOR ROT022 symbolic script were each rejected BEFORE SCIENTIFIC IMPORT with SOURCE_GIT_BLOB_MISMATCH and nonzero exit; originals untouched. All original source bytes are provided in user ZIP along with the actual executable and full exact endpoint results. Do not falsely claim these exact executed scripts were separately mirrored to public GitHub; this report and separate curated summary are GitHub outputs.

## F. Exact custody and recommended bounded review

M13 source FIRST. Geeky ROT020 original fixed-mask translation local rank at alpha=.05 FIRST, independently reviewed M15 ROT013; ROT022 period jump FIRST, independently reviewed REC12 ROT001 I1. ROT023 has NEW same-cell source theorem: TWO distinct internal first-order alpha information zeros with uniform nuisance rank4 + alpha0 exact y/z symmetry and singular profile-information limit. **INDEPENDENT ROT023 DIFFERENT-CELL REFEREE PENDING**.

Original native calc() has NO translation argument; source common t is a mathematical HYPOTHETICAL. Historical full dtc0a_runtime_v0_3_1.py byte identity remains MISSING. Physical field-shape realization, statistical error covariance and detector precision unverified. Full torus function periods do not identify all pointwise energy aliases, and a singular derivative does not automatically imply global nonlinear nonuniqueness. No source evidence for NASH J3/K/TPE/GR/GW physics or mathematical novelty. No BW ingestion event or owner M15 CANON sign verified by mere public report write.

Independent reviewer SHOULD independently redo the four rational full-det endpoint signs and the two uniform X minors directly from original source, then alpha0 exact 27-frequency y/z swap and mixed derivative v. STOP unnecessary root-threshold scanning and do not auto-cascade tasks.

FINAL:
 REC12_ROT001_PRIOR_ROT022_INDEPENDENT_I1_PASS_WITH_GUARDS /
 ROT023_TWO_STRICT_INTERNAL_FISHER_ZERO_BRACKETS_PASS /
 ROT023_WHOLE_BRACKETS_NUISANCE_RANK4_PASS /
 ROT023_ALPHA0_EXACT_YZ_REFLECTION_NUISANCE_RANK3_PASS /
 ROT023_POSITIVE_SIDE_LIMIT_INFORMATION_JUMP_PASS /
 TWO_CLEAN_RESULT_REPLAYS_AND_THREE_TAMPER_CONTROLS_PASS /
 ROT023_INDEPENDENT_REFEREE_PENDING / KN14_BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
