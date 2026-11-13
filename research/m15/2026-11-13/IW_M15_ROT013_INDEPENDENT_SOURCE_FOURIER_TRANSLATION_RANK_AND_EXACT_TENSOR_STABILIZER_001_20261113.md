---
artifact_id: IW_M15_ROT013_INDEPENDENT_DIRECTED_FOURIER_TRANSLATION_JACOBIAN_AND_EXACT_GLOBAL_STABILIZER_001_20261113
return_id: IW_M15_ROT013_ORIGINAL_M13_SOURCE_FORMULA_FULL_LOCAL_PROJECTIVE_TRANSLATION_RANK_AND_EXACT_TWO_ELEMENT_TENSOR_STABILIZER_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: DIFFERENT_CELL_I1_NONBLIND_INDEPENDENT_SOURCE_FORMULAE_50DIGIT_DIRECTED_INTERVAL_AND_EXACT_INTEGER_SUPPORT_LATTICE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: FROZEN_M13_PUBLIC_OPERATOR_FORMULAE_REIMPLEMENTED / TRANSLATION_HYPOTHETICAL / FULL_B_STABILIZER_NOT_SHELL_OBSERVABLE_STABILIZER / NO_ORIGINAL_SOURCE_MODULE_EXECUTION / HISTORICAL_DTC0A_BYTE_ID_MISSING / NO_EXTERNAL_I3 / NO_FIELD_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# M15 ROT013 — independent 50-digit directed mask Jacobian, exact complete full-B translation stabilizer, XH source protocol erratum

## 1. Decision, object and firstness

This is a separate, nonblind, internally independent I1 mathematical audit of the original M13 N41 sparse Fourier bracket/Lie/TT operator and the first-authored Geeky-S12 ROT020 translation theorem. M13 FIRST source operator and original data; Geeky ROT020 FIRST introduced the explicitly hypothetical common torus-translation family with FIXED five observation windows, FIRST demonstrated its local projective rank four and nontrivial global (pi,pi,pi) parity stabilizer. M15 does not reassign that firstness or assert literature novelty.

**Result 1 — independent source-formula directed IV proof PASS.** At N41, alpha=1/20=.05 and t=(0,0,0), M15 independently reconstructed B on 41 Fourier modes via its previously authored independently M13-source-matched formula implementation. New interval code, not copied from or calling Geeky ROT020, uses iv.dps=50, analytical shift derivatives from Fourier phase and an independent alpha derivative from the original operator's exactly quadratic alpha dependence. It independently builds five fixed-mask energies and the four projective log shell coordinates, then evaluates all 24 4x4 determinant permutations in directed intervals. BOTH 4x4 and 3x3 translation-minor upper interval endpoints are STRICTLY negative, confirming the source-conditional local inverse function theorem result of Geeky ROT020.

**Result 2 — additional exact FULL-TENSOR global translation stabilizer classification.** The 41 source B Fourier support indices all have even total integer parity. Three original B modes with a STRICT certified positive directed interval squared Frobenius tensor norm have integer wavevectors
    m1=(-3,-1,0), m2=(-2,-1,-1), m3=(-2,-1,+1).
Their exact 3x3 integer determinant is +2. Hence these three wavevectors generate an index-2 sublattice of Z^3; all support wavevectors belong to the even-coordinate-sum index-2 lattice. The support lattice must EQUAL that full even sublattice. Its torus annihilator contains EXACTLY two elements:
    Stab_of_ENTIRE_B(torus modulo 2pi) = {(0,0,0),(pi,pi,pi)}.
This classification proves there are no OTHER full-B tensor-preserving translations. It does **NOT** prove that the compressed FIVE shell observations have no additional global aliases, or that local full projective rank implies global unique inverse.

**Result 3 — anti-self-sealing cross-source correction.** XH-S6 ROT018 independently sourced and withdrew the prior assertion that its own ROT017 exactly-250-per-direction balanced neural-model experiment duplicated the original Ruff et al native Nbatch18000 random direction generator. This source-custody correction changes the author-protocol equivalence language previously repeated in M15 ROT011. The 36000 actual ROT017 model output rows and 19 gap exceptions remain genuine observations of the XH balanced test. M15 ROT013 did NOT rerun the original author Task or trained RNN. See section 6.

## 2. Actual original source read and independent equation implementation

Original M13 public source read by connected GitHub tool:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
  immutable Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679.
- https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json
  original 25 directed B quartic coefficient intervals, blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
- Geeky-S12 ROT020 original first science:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/91be7247e878a15f3c60949010f9915f3cd7abcb/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT020_SOURCE_FOURIER_TRANSLATION_FIXED_MASK_PROJECTIVE_RANK_LOCAL_ID_AND_PARITY_STABILIZER_001_20261113.md
  original report blob 89f0438db7dc7b3bb2eb8faa92946bcfd097e09e.

**Actual computation substrate:** The ORIGINAL separately authored M15 ROT012 Python reconstruction of public Fourier source formulas source_shape_operator_check.py, SHA256 4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e, was loaded ONLY after a pre-science SHA256 check. Its formula source had already matched all 25 original M13 B source coefficient MIDPOINTS to ~9.298e-17 relative using 45-digit arithmetic in ROT012. In ROT013 M15 re-executes this source FORMULA implementation using OUTWARD-rounded mpmath.iv 50 decimal digits. Crucially, this is NOT the unchanged author M13 module actually imported or executed byte-for-byte, and not the missing historical dtc0a_runtime_v0_3_1.py. The new verifier verify_m15_rot013_translation_rigorous.py is independent of the original Geeky source and outputs.

## 3. Exact Fourier translation geometry and fixed-mask observation

The original M13 B expression is built from translation-equivariant convolution bracket/Lie terms; the centered difference, E_alpha and TT projection are Fourier-mode diagonal. For an explicitly HYPOTHETICAL common translation of all input fields C1,C2,h by torus t, the source B tensor obeys the EXACT Fourier identity:
    B_alpha,t(m) = exp(i*m dot t) B_alpha,0(m).
This is a standard mathematical identity, not a new physical source parameter. The actual original source() contains fixed field coefficients, not translation control t.

The five observation masks are fixed in spatial coordinates while fields shift. Write W_k(m_j-n_j) for the original source Fourier window factors. For each nested mask k=2,...,6:
    g_k(alpha,t) = Re(sum_(m,n) <B_m,B_n>
       * prod_(j=1..3) W_k(m_j-n_j)
       * exp(i*(m-n) dot t))/6.
Because fixed spatial masks cause off-diagonal m!=n interference, this observable can change under field translation, unlike unmasked Parseval energy.

Analytical derivatives at t=0, computed with directed IV from 41x41 Fourier-mode pairs:
    d_tj g_k = Re(sum_(m,n) i*(m_j-n_j)*<B_m,B_n>*prod W_k)/6.
    d_alpha g_k = 2 Re(sum_(m,n) <Bprime_m,B_n>*prod W_k)/6.
Here Bprime = V+2alpha W is calculated via exact polynomial interpolation of the source B quadratic alpha dependence using alpha=0,+1,-1 source-equation tensors, not an approximate finite difference. The five shell source averages are
    s_i=(n_i*g_i-n_(i+1)*g_(i+1))/w_i, i=1..4; s5=g6;
    n_k=(41-2k)^3, w=(7778,6938,6146,5402,24389).
All five s_i at alpha=.05 have positive 50-digit directed interval lower endpoints, making log ratios legal. The projective local observations f_i=log(s_i/s5), i=1..4, eliminate any unknown common gain. For j in (t_x,t_y,t_z,alpha):
    J_ij = (d_j s_i)/s_i - (d_j s5)/s5.

## 4. Independent strictly directed determinant results

Actual complete 50-digit outward-rounded source-formula calculations yield:

Full 4x4 Jacobian determinant, columns (t_x,t_y,t_z,alpha):
    det(J) contained in
    [-0.00001019825589722441901272528778296285723903604026545036672,
     -0.000010198255897224419012725287782962857239035397291466039].

3x3 first-three-projective-rows / first-three translation-columns minor:
    det(J_translation_3x3) contained in
    [-0.000007757010281111687661605171226720284419583092649983956662,
     -0.000007757010281111687661605171226720284419583062786514191431].

The interval signs are established by direct upper bound comparison <0, not decimal-rounded or floating signs. The independent verifier calculates 24 products of matrix elements for the 4x4 determinant directly from the IV matrix; it does NOT call owner source determinant code or read the owner source result as its input. The numbers independently agree with the Geeky ROT020 original local rank first result.

Hence the classical inverse function theorem gives LOCAL identifiability in the hypothetical mathematical class of common source translations relative to FIXED source masks plus alpha after quotienting common amplitude. Nothing proves global invertibility, noise accuracy, physical shift viability, or that fixed masks move with any real field instrument.

## 5. Independently sharpened exact global full-tensor symmetry group

The B output contains 41 Fourier mode-key indices, every one with integer parity m_x+m_y+m_z even. Therefore any common shift by (pi,pi,pi) preserves each B component exactly: exp(i*pi*(even))=1. This gives the known nontrivial symmetry.

M15 adds a complete proof that no other full tensor stabilizer translation exists. The exact three witness mode vectors
    (-3,-1,0), (-2,-1,-1), (-2,-1,+1)
have integer determinant +2. Their ORIGINAL source B coefficient norms squared were independently evaluated by directed iv50:
    ||B(-3,-1,0)||_F² around 4.06920533213449775024559e-15, STRICT positive;
    ||B(-2,-1,-1)||_F² around 2.05730819499537576583429e-14, STRICT positive;
    ||B(-2,-1,+1)||_F² around 2.05730819499537576583429e-14, STRICT positive.
The full exact lower/upper interval endpoints for all THREE are included in the original executable machine JSON.

Let L be the Z-linear span of NONZERO B wavevectors and E the EVEN-parity sublattice of Z³. The witness vector lattice has index 2 (absolute determinant 2), is contained in L, and L is contained in E (also index 2). Thus index2 lattice inclusions force L=E EXACTLY. A torus translation fixes ALL B Fourier coefficients iff exp(i*m dot t)=1 for all m in L. The annihilator of E in R³/(2pi Z³) consists EXACTLY of
    t=(0,0,0) or t=(pi,pi,pi), modulo 2pi.
This holds for the SOURCE-FORMULA B tensor frozen at N41 alpha=.05.

**Do not transfer:** The five shell energies are merely five quadratic projections of the high-dimensional B tensor. Their stabilizer or inverse alias set can be STRICTLY larger than the full-tensor translation stabilizer. A complete full-B lattice proof does NOT classify all solutions s(alpha,t)=s(alpha,t') nor permit global source inversion. This is the most important ceiling of the new stronger mathematical result.

Analytical negative controls: If masks co-translate with fields, field-to-mask relative position does not change, so three shift gradients of all five energies are identically ZERO. If only unmasked Parseval energy is observed, all shift gradients are ZERO. These are exact mathematical counterfactuals, not executed RNN models or physical experiments. The local rank result requires fixed observation mask interference.

## 6. Source self-correction: ROT011 author schedule equivalence withdrawn

Source-priority XH-S6 ROT018 original author generator correction, original owner report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/37729c2819174906bfdb261b7d492c0c16188496/research/xh-s6/2026-11-13/iw_xh_s6_rot018_original_source_random_direction_allocation_250_balanced_protocol_correction_001.md
Original correction source blob 74b5d046e9ad1631bb01f7abd9bc4cd90e9a316b, read directly for this rotation.

The actual original Ruff/Markman/Kim/Cohen generator defines N_batch=72*250 but allows independently random assignment among 72 shown directions (test1ofEach=False). The XH ROT017 user-extended experiment used 250 independent forced-balanced 72-angle stochastic blocks, exactly 250 outputs for EVERY angle; it DID execute original author Task and trained RNN classes, but its angle-allocation schedule is NOT the author's exact random one-shot protocol. XH FIRST self-corrected its earlier overstatement. M15 ROT011 directly audited XH's genuine 36000 model pairs and their 19 stimulus-winner gap events and 500 complete balanced blocks. These source counts remain valid AS A BALANCED EXPERIMENT, but any M15 ROT011 wording equating forced 250-per-angle design to exact original author source RNG input scheduling is explicitly WITHDRAWN by this addendum. No M15 ROT013 original author Task/RNN execution or independent re-verification of XH source RNG is claimed.

No change to the 19 real simulation exceptions within XH's selected balanced model design, but their inference cannot silently be promoted to exact native-author random trial allocation or biological neuronal mechanism. Distinct currentness correction from the new Fourier science.

## 7. Execution, integrity, artifact and guard

Actual new M15 independent executed code:
    verify_m15_rot013_translation_rigorous.py
SHA256 5cedc0318f9f2cf11713b8f6210196135473e7a86d9a43f0d620ef5b548bc5e1.
Exact prior independent M15 original math formula source SHA256
    4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e.
Actual original computed full directed machine JSON SHA256
    debc2db8fe423836a7b4f6890291c75aadccf02a5a5ff877313468a01b4f7d1d.

The two-file source dependency passes mandatory SHA check BEFORE run. Separate independent clean isolated copy of the exact script and original formula code produced BYTE-IDENTICAL JSON PASS. Deliberate one-byte mutation to the formula dependency was REJECTED before source computation with PRE_SCIENCE_BASE_M15_FORMULAE_SHA256_MISMATCH; fail-closed PASS.

Complete reproducibility ZIP held in the USER conversation, containing both original math codes, full directed result JSON, raw stdout, README, isolated replay and original mutation check and SHA manifest:
    IW_M15_ROT013_FOURIER_TRANSLATION_FULL_INTERVAL_AND_EXACT_STABILIZER_REPRO_001_20261113.zip
Size 17,898 bytes; SHA256 8c4baa8d173f654f98b862ec39d2647c9d07df5b3d53e7595670100826f4c290. ZIP CRC PASS, 7/7 payload SHA256 PASS, clean replay BYTE_IDENTICAL PASS, source tamper FAIL_CLOSED PASS. The ZIP uses independently reimplemented source formulas and does not contain the unmodified native M13 historical module or any missing original DTC0a producer.

Scope: internal I1 NONBLIND mathematical review and integer-lattice conditional source theorem; M13 and Geeky ROT020 original firstness preserved. The FULL B tensor stabilizer result is rigorous within the declared source-equation representation, not an I3 external referee, not a physical instrument effect, and not a new mathematics novelty claim. No original historical dtc0a_runtime_v0_3_1.py identity. No real field translation or independently calibrated Fourier data. No NASH K/J3/TPE, Schall actual sensor statistics, Wu-Xu BBN/PBH or animal data. KN14 handles BW custody; GitHub report is NOT BW actual ingest, and no ING event ID, canon or EXEC_SIGN is asserted. No task cascade, no owner override.

FINAL:
M15_ROT013_SOURCE_EQUATIONS_DIRECTED_IV50_LOCAL_JACOBIAN_4X4_AND_3X3_PASS /
EXACT_THREE_NONZERO_SOURCE_MODES_INTEGER_DET2_PASS /
COMPLETE_GLOBAL_TWO_POINT_FULL_B_TENSOR_TRANSLATION_STABILIZER_PASS /
COMPRESSED_FIVE_SHELL_GLOBAL_ALIAS_SET_NOT_CLASSIFIED /
GEEKY_ROT020_SOURCE_FIRST_PRESERVED /
XH_ROT018_PROTOCOL_CORRECTION_APPLIED_TO_M15_ROT011 /
ISOLATED_RERUN_BYTE_IDENTICAL / ONE_BYTE_TAMPER_FAIL_CLOSED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
