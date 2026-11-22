---
artifact_id: IW_M16_ROT010_EXACT_SHARP_SOURCE_TRANSPORT_IDENTIFICATION_SET_FOURFOLD_PAULI_GAUGE_AND_INTERSTAGE_SOURCE_COUPLING_FALSIFIER_001_20261122
return_id: IW_M16_ROT010_EXACT_FOUR_POINT_IDENTIFIED_SET_SHARP_SOURCE_TV_BOUNDS_TWO_SIGNED_FRAME_ANCHORS_AND_CONTEXT_DEPENDENT_SOURCE_NO_GO_001_20261122
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: SOURCE_CONDITIONAL_IDENTIFIABILITY / PAULI_SIX_MIXED_FOURIER / SHARP_FOUR_POINT_TV_SET / Q_CONTEXT_DRIFT_FALSIFIER
status: 3_ORIGINAL_GIT_SCIENCE_SOURCES_READ / 2_INDEPENDENT_NEW_EXECUTABLES_ACTUALLY_EXECUTED_TWICE / 100_RANDOM_RATIONAL_TESTS_PASS / REPRO_ZIP_CRC_SHA_PASS
claim_ceiling: NO_GENERAL_NOVELTY / NO_HARDWARE / NO_UNRESTRICTED_PROCESS_TENSOR / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_WRITE
---

# M16 ROT010 — sharp four-point identified set of classical Pauli source transport and a necessary interstage source-stability gate

## Scope, original sources and scientific question

Original PRF14 ROT024 physically lawful 16-history source model DIRECTLY READ in full, Git blob 7b7a87df05e404e2b8af96755bf946c1fbbabc7f, pinned original:
https://github.com/wmakiela-tech/Nash-iw-research/blob/743a65e0e73677a3191bd6acd01df5f3486be7e8/research/prf14/2026-11-22/IW_PRF14_ROT024_TWO_ROW_SO3_ORTHOGONALITY_SOURCE_TRANSPORT_FOUR_CHARACTER_95PC_TV_LOWER_AND_PHYSICAL_NO_GO_001_20261122.md

Original PRF14 ROT025 broad nonnovelty review DIRECTLY READ, Git blob e18aa585264b47d383899f21ad25ba5060a1533d:
https://github.com/wmakiela-tech/Nash-iw-research/blob/159144f543923d10a22957ed537dc0a74cfb1dff/research/prf14/2026-11-22/IW_PRF14_ROT025_DOCTORAL_PRIOR_ART_EXACT_THEOREM_AUDIT_WHITE_WANG_XU_LI_IST_AND_INSTRUMENT_TRANSPORT_DECISION_001_20261122.md

M16 ROT009 two genuine BETWEEN-errors internal Clifford settings and fourfold input Pauli gauge DIRECTLY READ, Git blob 935f2fc396582f066a9158d6efb194d698f7908e:
https://github.com/wmakiela-tech/Nash-iw-research/blob/23085b1b822414148503b328c13d9834f528d66c/research/m16/2026-11-22/IW_M16_ROT009_TWO_INTERNAL_CLIFFORD_SETTINGS_PROJECTIVE_SO3_RECOVERY_AND_IRREDUCIBLE_FOURFOLD_PAULI_SOURCE_GAUGE_001_20261122.md

PRF firstness of all original 16-histories and physical finite source laws PRESERVED. M16 ROT009 owns its previously published very narrow two-setting conditional observation argument, not general quantum tomography.

ROT010 scientific question: does the EXACT measurement idealization identify the source-to-source total variation, even though its latent UNIT source remains ambiguous under fourfold Pauli frame? Answer: no point estimate without additional anchor, but YES a finite, sharp identified SET and possibly a strict gauge-invariant lower bound. Conversely if the source itself responds to the insertion of the extra internal gate, the identification construction can fail COMPLETELY.

External maturity subtraction: Original GST gauge degrees of freedom explicitly present already in Nature Communications 2017 https://www.nature.com/articles/ncomms14485 ; 2025 npj colored-noise GST https://www.nature.com/articles/s41534-025-00976-4; Xu Liu Chen arxiv:2611.05561 Nov 2026 first-party abstract explicitly treats nonidentifiable gauge/cycle-space. These were checked at abstracts/excerpts this rotation, NOT claimed fully audited. Generic identification up to a group and minimizing a metric over a finite orbit are STANDARD techniques, not NASH novelty.

## The exact restrictive source and observation contracts

History v,w in F2^2 yields 16 legal probabilities. The UNIT law is restricted to one Fourier normalization character equal 1, SIX potentially nonzero off-diagonal mixed characters C_ij for i != j, and NINE remaining nonconstant Fourier characters exactly zero:
  p_C(v,w) = [1 + sum_(i != j) C_ij chi_j(v) chi_i(w)] / 16.

Assume every p_C(v,w) strictly positive, all six offdiagonal C_ij nonzero, one common proper SO(3) middle gate S with nonzero relevant entries, and the SAME p_UNIT (therefore SAME C) under BOTH independently announced and correctly inserted interstage controls I and cyclic P.

Let P = [[0,0,1],[1,0,0],[0,1,0]]. Exact FULL qubit unital Bloch transfer matrices under genuine BETWEEN-errors controls:
  T_I,ij = C_ij S_ij,
  T_P,ij = C_ij (P S)_ij.
Diagonal coefficients are zero in this six-only model. This is not postprocessing a finished channel (P T_I). We assume exact full 3x3 tomography and physically calibrated P but do NOT claim to have performed it.

A distinct destructive BREAK protocol reveals its own classical 16-label source p_BREAK. We do not assert its equality to p_UNIT. The studied property is zeta=TV(p_UNIT,p_BREAK)=1/2 sum |p_UNIT(v,w)-p_BREAK(v,w)|.

## Bounded exact theorem: SHARP four-point identification

For i != j, observed r_ij = T_P,ij / T_I,ij = S_((i-1) mod3),j / S_ij.
For each fixed input column j the two directed edges from i != j connect all three output rows. Therefore they determine all entries of that column of S UP TO A SCALAR. SO(3) orthonormality determines its magnitude; there is one sign for each of the 3 columns. det S=+1 restricts sign product to +1, leaving exactly 4 diagonal sign matrices D in Klein-four.

For each D there is a unique input Pauli label v_D such that chi_j(v_D)=D_jj. Define S_D=S D and p_D(v,w)=p_UNIT(v XOR v_D,w). Then C_D,ij=C_ij D_jj and (Q S_D)_ij=(Q S)_ij D_jj. Their product remains the same for ANY known interstage control Q, while p_D is a positive permutation of the 16 source probabilities and S_D is a proper SO(3) gate.

In the six-mixed Fourier class C uniquely determines the full p_C by inverse Walsh, so these FOUR physical source laws are the COMPLETE measurement fiber, not four arbitrary examples. Thus the SHARP identified set is:
  Z_ID(T_I,T_P,p_BREAK) =
   { TV(p_BREAK,p_UNIT(v XOR v_D,w)) : v_D in F2^2 }.

The set has up to four DISTINCT numbers. Each is exactly compatible with the SAME full T_I,T_P and with the SAME destructive BREAK distribution. The exact sharp lower and upper limits are zeta_min=min Z_ID and zeta_max=max Z_ID; IMPORTANT: the whole numerical interval [min,max] is generally NOT the identified set.

- zeta_min > 0: within this source model, source change under UNIT vs BREAK is NECESSARY regardless of unknown Pauli sign frame.
- zeta_min = 0: no-change is COMPATIBLE, but does not follow; some other physical fiber worlds can have large true source TV.
- zero-width Z_ID: zeta point-identified without necessarily identifying p_UNIT.
No finite-sample alpha, device error or optimal measurement number claimed.

## New actual exact SOURCE data: full reconstruction without using true gate

Original source C0 =
 [[0,9/100,11/100],[7/100,0,1/10],[8/100,12/100,0]].
S0 =
 (1/7)[[2,6,3],[-3,-2,6],[6,-3,2]].
One actual fresh script generates two full physical channels, then reconstructs each projective column of S from OBSERVED T_I,T_P ONLY. It normalizes each column by exact perfect-square Fraction/isqrt, generates eight sign choices, retains four determinant+1 proper gates, retrieves each candidate C_ij by division of T_I by candidate S_ij, and constructs 16 explicit positive p candidates with exact fractions.

Results, all entries of each identified set are actual exact Fractions:

Case N0: p_UNIT=p_BREAK=p_((7/2) C0), no physical source change in one world:
  Z_ID = {0, 203/400, 21/40, 231/400}.
  SHARP lower=0; upper=231/400=0.5775.
  The data CANNOT prove no-change even when it happens to be true.

Case N4: p_UNIT=p_((91/25) C0), p_BREAK=p_((7/2) C0), source Fourier amplitude ratio 26/25 (4%):
  Z_ID={1197/80000, 41559/80000, 1071/2000, 47229/80000}.
  SHARP lower=1197/80000=0.0149625; upper=47229/80000=0.5903625.
  This is a STRICTLY POSITIVE, source-specific, GAUGE-FREE detection in the stated exact idealized two-setting observation contract; not a hardware detection.

Case W1: PRF14 ROT024 original small source change compensated by a proper unknown shifted gate:
  Z_ID has first element 41979/50199950 approximately .000836235893;
  remaining three exact huge fractions in machine JSON approximately
    .50745994838, .52443573533, .57695391172.
  SHARP min=41979/50199950; sharp max about .57695391172.
This W1 was indistinguishable from W0 with only one internal setting I, but differs after true internal P; report does not claim measurement access.

## Critical FALSIFIER: if source changes between I and P, the continuous gauge returns

Alternative world with SAME one proper shifted middle S' in BOTH settings, but allowing positive SIX-only p'_I and p'_P to differ as a consequence of Q.

Choose original W0 C=(7/2)C0 and S, and S'=P R_x(t=1/1000) R0, a proper rational rotation. For q in {I,P}, define independently and exactly:
  C'_q,ij = C_ij (q S)_ij / (q S')_ij for all i != j; 3 diagonal 0 and all ordinary Fourier 0.

Both resulting 16-histories p'_q are STRICTLY POSITIVE and normalized, both channels T'_q match the original complete T_q EXACTLY, but:
  TV(p'_I,p'_P) ≈ .001317627662459714 > 0,
  TV(p'_I,p_BREAK) =41979/50199950≈.000836235892665,
  TV(p'_P,p_BREAK) ≈ .0009685874309596.

The exact large rational values are in the machine certificate. Thus exact observational agreement after adding interstage P DOES NOT imply a unique source or a finite four-point identification region if p_UNIT is permitted to respond to changing Q. The stability across Q is a PHYSICAL ASSUMPTION and must be justified from a source generator or apparatus model, not inferred by assuming the very BREAK vs UNIT equality under test.

## Minimal independent signed Pauli-frame anchors

Four frame choices correspond to sign triples d0,d1,d2 with d0*d1*d2=1. One independently externally calibrated sign from one nonzero source mixed Fourier character for input column j (or a true calibrated absolute sign for column j of S) separates these into only TWO remaining worlds. TWO such reliable signs from TWO DISTINCT independent columns uniquely identify D (the third sign fixed by orientation). Exact necessity and sufficiency is a group-of-order-four two-bit counting statement.

Do not obtain the signed UNIT anchors by destructive BREAK and then assume p_UNIT=p_BREAK to infer them: that would be circular. In the six-only p_UNIT, all single-time v marginals vanish, so a purported one-time source measurement of just chi_j(v) does NOT directly supply such a signed anchor. An actual signed independent source-frame monitor, timing and calibration are not demonstrated.

## Reproducibility details; actual independent work

Fresh main Python standard library Fraction script:
 /mnt/data/m16_rot010/m16_rot010_exact_identification_region.py
 SHA256 4001c6d42f56a59dc76b4ef977f5e203f55bd096d7f09a648b000e9591e256db
actual exact JSON:
 /mnt/data/m16_rot010/m16_rot010_machine.json
 SHA256 961174ac5f9130faedcf1e8328895359d35dec6d90fc15e7eafaef370e2200e4.
Actual isolated Python -I initial and repeated runs: stdout SHA256 d5f921c44d421cecb40298ea0d03e04aabc9b0c98b74eae96abdbe68e1e2df16 BOTH, byte-identical.

Separate independently programmed SymPy literal 16-history, 16x16 Walsh full source, random quaternion rational proper SO(3) source/control:
 /mnt/data/m16_rot010/m16_rot010_second_sympy_walsh_test.py
 SHA256 7a5a23fb4265b7cfcb6c301d1826adb998044cdd799fe3720b6fbe36a7630e51
 /mnt/data/m16_rot010/m16_rot010_second_machine.json
 SHA256 537677f080ac8043fcbc573e77eae5fc86540c2a292ef77f48eae0046553e033.
100/100 random rational physical strictly positive six-source cases PASS, 4 physical alternative frame sources, same TWO FULL observable channels, sharp TV orbit holds, two independent sign anchors split 4 candidates; actual source draws vary. Isolated repeated stdout SHA256 3ae8c2a806bb7e1b45b55087cc19ec9493c2a191174ddf236fff84126680dea7 BOTH, byte-identical.

Local 10-member ZIP containing both full codes, both JSONs, stdout, repeats, README and SHA manifest:
 /mnt/data/m16_rot010/m16_rot010_bundle.zip
 SHA256 2872034a981c3a5dac492094c587a3369702ee1d42901697346fe056b4aea401.
ZIP CRC PASS and ALL TEN file contents byte-equal to local originals on full re-read. No source-specific claim exceeds this actual execution.

## Decision and science status

PASS exact source-conditional SHARP 4-point identified set.
PASS strict positive lower bound for original PRF14 4%-scaled strong source.
PASS inability to claim source equality even in W0 with four gauge worlds.
PASS exact different-setting source positive counterexample reinstating continuous gauge if Q changes source.
PASS independent 100-case rational physical source reimplementation.
FAIL/HOLD any interpretation as native measurement, general quantum causal comb, experimental-source stability, or externally novel fundamental mathematical theorem.

M16 recommends closing source-only observer mathematics here and moving any subsequent genuinely important question to physically legal cross-intervention generator coupling and two independently measured signed frame anchors under PRF14/Moderator ownership. NOT owner reassignment, not a new BW entry or CANON promotion and NO_EXEC_SIGN.

FINAL: M16_ROT010_SHARP_FOUR_POINT_TV_PASS / N4_GAUGE_INVARIANT_MIN_1197_OVER_80000 / N0_TV_SET_ZERO_TO_231_OVER_400_DISCRETE / CONTEXT_DEPENDENT_Q_SOURCE_FALSIFIER_PASS / TWO_FRAME_SIGN_ANCHORS_MINIMAL / TWO_INDEPENDENT_EXECUTABLES_ACTUAL_REPLAY_PASS / 100_RANDOM_SOURCE_CASES_PASS / 10_FILE_ZIP_CRC_SHA_FULL_BYTES_PASS / NO_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN.
