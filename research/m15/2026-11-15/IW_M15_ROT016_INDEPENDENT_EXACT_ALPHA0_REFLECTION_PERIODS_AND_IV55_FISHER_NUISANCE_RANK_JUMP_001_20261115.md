---
artifact_id: IW_M15_ROT016_INDEPENDENT_ORIGINAL_M13_ALPHA0_REFLECTION_AND_FISHER_RANK_JUMP_001_20261115
return_id: IW_M15_ROT016_DIFFERENT_CELL_GEEKY_ROT023_EXACT_ALPHA0_YZ_REFLECTION_AND_20P585_INFORMATION_JUMP_CAUCHY_BINET_001_20261115
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-15
exposure: PUBLIC
result_class: I1_INTERNAL_NONBLIND_DIFFERENT_CELL_SOURCE_MATH_REFEREE / EXACT_SYMPY_REFLECTION / 55_DIGIT_DIRECTED_INTERVAL_CAUCHY_BINET_FISHER
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_M13_AUXILIARY_SOURCE_EQUATIONS_REIMPLEMENTED / HYPOTHETICAL_FIELD_TRANSLATIONS_FIXED_MASKS / HYPOTHETICAL_IID_LOG_ENERGY_GAUSSIAN_NOISE / NOT_ORIGINAL_AUTHOR_MODULE_BYTE_EXECUTION / NO_HISTORICAL_DTC0A_PRODUCER / NO_EXTERNAL_BLIND_I3 / NO_PHYSICAL_FIELD_CALIBRATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# M15 ROT016 — independent alpha=0 reflection and source nuisance-information discontinuity referee

## 0. One material question, owner priority and result

**INDEPENDENT DIFFERENT-CELL I1 SOURCE-MATH PASS.**

Geeky-S12 ROT023 FIRST source-proved (i) the exactly symmetric alpha=0 y/z reflection of all five M13 B N41 fixed-mask translated shell energies; (ii) nuisance translation rank exactly 3 at alpha=0 and positive-side limiting rank 4; (iii) the associated conditional local efficient alpha Fisher information jump from approx 0.06319446572410744 to 0.0030698996865808894 in units sigma² I_eff, a ratio of approx 20.5851891514053. These are author FIRST. Earlier M15 ROT015 independently checked Geeky ROT023 TWO OTHER internal alpha Fisher-zero source brackets and supplied new local simple-root derivative certificates, but explicitly withheld review of the alpha0 portion. M15 ROT016 now directly closes this separate alpha0 internal I1 gap with new exact symbolic source algebra plus wholly differently organized outward interval Fisher calculation; no Geeky certifier imported.

More specifically:
- ACTUAL separately authored SymPy symbolic M13 SOURCE-FORMULA calculation returns EXACTLY EIGHT nonzero alpha0 tensor Fourier modes among the 41 original indexed source outputs, indexed (±2,±1,±1); every 3x3 tensor entry factors by the SAME nonzero exact real x1(2x1-x2), with rational remaining entries, where x1=sin(2pi/41)/(2pi/41)>0 and x2=sin(4pi/41)/(2pi/41)=2cos(2pi/41)x1. Nonzero common factor positivity is algebraic.
- ALL 27 exact rational tensor-pair energy difference-frequency coefficients, divided by that common squared scalar, are real and EXACTLY invariant under interchange q_y<->q_z. The five original cubic masks have equal y and z kernels; hence the ENTIRE continuous translated shell observation satisfies s_i(0,tx,ty,tz)=s_i(0,tx,tz,ty) for every torus t, all i. At t=0, D_ty log(s_i)=D_tz log(s_i) EXACTLY, not merely numerically close.
- Independently check the alpha0 complete COMMON PERIOD SUBGROUP FIRST proved by Geeky ROT022 (and independently reviewed REC12 ROT001). Every 27 source possible energy difference q lies in 4Z x 2Z x 2Z. Three EXACT nonzero source correlation witnesses are
  q=(4,0,0): 1/12960000000,
  q=(0,2,0): -11/129600000000,
  q=(0,0,2): -11/129600000000,
  after exact common tensor-factor normalization.
  Crucially, each of the THREE corresponding **FIFTH FIXED MASK** Fourier window products is independently shown nonzero: for N=41, fifth window k=6 has length L=N-2k=29, and every nonzero witness frequency component q=2 or 4 obeys 41 not dividing 29q, so its finite Fourier geometric sum cannot vanish; this is reinforced by STRICT positive 55-digit outward interval squared window modulus checks. Because s5=g6 has these nonzero observed modes, the fifth observation has EXACT period lattice 4Z x 2Z x 2Z, index 16. All other source shell q also lie in the same sublattice, so their **common** full-function period group also has order 16. This is NOT a pointwise alias classification and is not new firstness over Geeky ROT022/REC12 ROT001.
- Original-formula outward mpmath.iv 55dps at alpha0 computes the source log-shell nuisance columns [1,D_tx,D_ty,D_tz], target score a=D_alpha and NEW analytic mixed derivative v=partial_alpha(D_ty-D_tz)|alpha0 from original B=U+alpha V+alpha²W. Strict directed 3x3 minor, 4x4 augmented alpha minor, all five 4x4 POSITIVE-SIDE nuisance tangent minors, and 5x5 augmented minor validate rank 3 at exactly alpha0, rank 4 as alpha approaches0 from >0, and the target-alpha remaining nonzero information.
- **New separate computational derivation of Fisher values** uses an outward rational-type interval Cauchy–Binet *sum of squared minors*, NOT the original Geeky ROT023 Schur-complement/Gram-inverse implementation:
  sigma²*I_eff = (sum over row subsets size rank(X)+1 of det([X,a]_rows)^2) / (sum over subsets size rank(X) of det(X_rows)^2).
  It obtains exact-direction interval bounds with STRICT lower numerator/denominator positivity and independent strict positive gap.

## 1. Direct source firstness, provenance and object separation

M13 FIRST original auxiliary 41-grid Fourier Lie/bracket/TT B module, Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679; M13 FIRST 25 directed quartic B coefficients, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Both immutable ORIGINAL files were REFETCHED DIRECTLY from the connected GitHub provider in this rotation and compared with those exact historical Git blobs before report publication:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json

Geeky-S12 ROT020 FIRST introduced hypothetical common rigid Fourier field translations versus FIXED M13 observation masks; M15 ROT013 independently checked local rank at alpha=.05 and two-element full-tensor stabilizer, M15 ROT014 independently checked fifth shell's two-element period group at that same positive alpha=.05. Geeky ROT022 FIRST extended the whole-function period group to 16 elements at alpha0 and two for all 0<alpha<=.2; REC12 ROT001 performed original independent I1 symbolic/interval review of that ROT022 result. Geeky ROT023 FIRST two internal alpha information zeros AND exact alpha0 symmetry/rank discontinuity; M15 ROT015 reviewed only the TWO internal alpha zero brackets and new simple root claims, and M15 ROT016 NOW directly reviews the alpha0 part. Owner report actually fetched:
https://github.com/wmakiela-tech/Nash-iw-research/blob/46972159ffe9534c36dc1ca7c01cba96f0538035/research/geeky-s12/2026-11-14/IW_GEEKY_S12_ROT023_TWO_INTERNAL_SOURCE_ALPHA_FISHER_ZEROS_AND_ALPHA0_NUISANCE_RANK_JUMP_001_20261114.md
Owner blob 12e1271e3c273d59fb08750ffe0f15867dcdbf55. No owner code, owner machine output or cached owner Jacobian used as computational input.

**Actual code distinction:** The independently authored earlier M15 ROT012 SOURCE FORMULA reimplementation source_shape_operator_check.py, locked SHA256 4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e, was actually imported (after SHA check) into a NEW independent ROT016 checker. The source symbolic part overrides only the centered difference Fourier eigenvalue entries with exact formal real x1..x4 and E_alpha=1 exactly at alpha0, and forces source field coefficients to exact Rational(1) instead of the earlier point-mpmath function-default constants. The original Fourier Lie/bracket/TT source operator structure is otherwise retained. The interval part separately sets mpmath.iv precision55 for original source equations, evaluates B at alpha=0,+1,-1 to reconstruct U,V,W and NEVER calls original Geeky or original M13 Python modules. The historical full dtc0a_runtime_v0_3_1.py remains absent. A separate implementation of public formulas is not byte-identical execution of any historical program; do not merge.

## 2. Exact Fourier/source symmetry and nonzero mask period witnesses

The original M13 source input modes have fixed Fourier support, original source Fourier centered difference δ_N(m)=i sin(2pi*m/N)/(2pi/N), diagonal E_alpha and TT projection. For alpha0 specifically, E_0=1 exactly. The independently authored symbolic wrapper introduces real x1=sin(2pi/41)/(2pi/41), x2=sin(4pi/41)/(2pi/41), and exactly Rational field amplitudes; computes all 41 original B mode keys then cancels all tensor entries symbolically. The output has precisely eight nonzero tensor matrices at wavevectors (±2,±1,±1); every nonzero tensor element divided by F=x1(2x1-x2) is EXACT rational. F=2x1²[1-cos(2pi/41)] is strictly positive.

For each pair m,n of these eight modes, the independent program directly sums all 9 tensor Frobenius cross terms to reconstruct 27 possible source energy frequency correlations Q_q. Symbolically each Q_q/F² is real rational and Q_(qx,qy,qz)=Q_(qx,qz,qy) for ALL 27 source frequency differences. The spatial mask W_k(qx)W_k(qy)W_k(qz) has identical y,z factors, hence every nested mask energy g_k and every disjoint shell energy satisfies an exact WHOLE-FUNCTION symmetry under ty↔tz, for all torus t, not just at t=0.

The 27 q are supported inside 4Z x 2Z x 2Z. The three exact nonzero rational Fourier coefficients at q=(4,0,0),(0,2,0),(0,0,2) prove that this entire lattice is generated by NONZERO SOURCE CORRELATION coefficients; since source OBSERVATION applies fixed mask k=6, it is essential also to prove the k6 window factors are not zero. For each witness, the only nonzero qj is 2 or4 and the mask finite geometric series sums L=29 of the N=41 torus. Since 41 is prime and 41 does not divide 29qj, the normalized one-dimensional finite-geometric sum is EXACTLY nonzero; qj=0 has coefficient exactly1. An independent mpmath.iv55 calculation additionally checks the complete 3D window product's squared modulus has a STRICT positive interval lower bound. Therefore those are truly nonzero fifth MASK-energy Fourier coefficients, not merely unmasked source correlations. The fifth observed shell is g6 itself. Its full function period group is exactly the 16 torus shifts with tx∈{0,pi/2,pi,3pi/2}, ty,tz∈{0,pi} modulo2pi; all five shell energies share those periods and the fifth shell excludes any further COMMON periods. This corroborates original Geeky ROT022 FIRST and REC12 ROT001 independent check; M15 does not claim ownership of this period theorem.

**Important:** A full-function PERIOD h satisfies S(t+h)=S(t) for EVERY t. This does not exclude ACCIDENTAL pairwise equal observations at t1≠t2 whose displacement is NOT a period of the entire source observation function. Thus no global pointwise five-observation injectivity is proven.

## 3. Source score derivatives and rank jump

Let positive five shell source energy means S_i(alpha,t), with one unknown common log gain b and three HYPOTHETICAL field translations t_x,t_y,t_z versus fixed original masks. At t=0 the five raw log-energy score columns are
   1=(1,...,1), D_j=(partial_tj S_i/S_i)_i, a=(partial_alpha S_i/S_i)_i.
Original source tensor is exactly quadratic in alpha, B=U+alpha V+alpha²W, so derivative V at0 is obtained algebraically from original formula evaluations at alpha=0,+1,-1. For original Fourier-mode-pair correlations and original fixed mask frequency windows, no finite differences:
   S_i' = 2 Re< V,U >_i;
   partial_tj S_i = Re Σ_{mn} i(m_j-n_j)<U_m,U_n> W_i /6;
   partial_alpha partial_tj S_i = 2 Re Σ_{mn} i(m_j-n_j)<V_m,U_n>W_i /6,
with appropriate fixed mask-to-shell weighted differences. All evaluated independently using mpmath.iv55, after replacing the 33 symbolic alpha0 ZERO Fourier modes of U by exact matrix zero in interval code (exactly justified by previous symbolic support check), thereby avoiding fictitious interval noise.

The exact reflection proof gives D_y(0)=D_z(0), so nuisance span X(0)=span[1,D_x,D_y] has rank≤3. Its independent 3x3 first-row minor is strictly negative
    approx -0.00322636365878575789315901023110824440409.
Thus rank EXACT3.

The source alpha score a is independent at the boundary: first four rows of [1,Dx,Dy,a] have strict positive 4x4 minor
    approx +0.00345482770304442644788517604075831371510,
so alpha remains first-order visible at EXACT alpha=0 after removal of the THREE actual nuisance directions.

For alpha>0 approaching0, the missing nuisance direction is the NORMALIZED difference D_y−D_z. Since the difference is exactly zero at0, define its analytic first alpha derivative
    v = partial_alpha (D_y−D_z)|alpha0
      = [partial_alpha partial_ty S_i - partial_alpha partial_tz S_i]/S_i(0).
The source second quotient term involving (D_y−D_z) vanishes EXACTLY at alpha0, not approximately. The five components have independent iv55 directed intervals whose central DISPLAY values are:
    v ≈ (1.924677489974600501, 2.500628680426398564,
         1.785605579878951425, 0.312021774991096225,
        -1.022910070745784083).

All FIVE 4x4 row minors of the limiting nuisance space
    X_+ = span[1,Dx(0),Dy(0),v]
are rigorously nonzero in iv55. Its five-by-five augmentation [X_+,a(0)] has STRICT negative determinant about -0.0013910122280815524243. Thus rank(X_+)=4 and the target remains independent even in this larger limiting nuisance span. The nuisance projection is NOT continuous in rank at the endpoint despite analytical continuity of source shell functions.

## 4. New different algorithm: exact Cauchy–Binet residual-information enclosures

Geeky ROT023 first computed the hypothetical Gaussian efficient alpha Fisher jump using original Schur complement. M15 independently uses a different mature linear-algebra identity to reduce interval cancellation:

For any real five-by-r nuisance matrix X of full column rank r and alpha column a,
     sigma² I_eff = ||(I-P_X)a||²
                  = [Σ_(I⊂{1..5}, |I|=r+1) det([X,a]_I)²]
                    / [Σ_(I⊂{1..5}, |I|=r) det(X_I)²].
This is the Cauchy–Binet identity det([X,a]^T[X,a])/det(X^T X). Because all numerator/denominator components are NONNEGATIVE squared determinants and exact source minor signs are certified, it is well suited to strict directed interval calculations. The program independently enumerates all 3x3/4x4/5x5 relevant row minors via full permutation formulas, never calls owner noise model code or source Gram inverse.

At the EXACT endpoint alpha=0 with X0=[1,Dx,Dy], numerical results fully enclosed by OUTWARD 55dps intervals:
    sigma² I_eff(0)
      ∈ [0.0631944657241074387378275614873175986736231534657016701282491,
         0.0631944657241074387378275614873175986736231534675314944433862].

At alpha→0+ in the SOURCE REGULAR PUNCTURED SIDE with X_+=[1,Dx,Dy,v]:
    lim sigma² I_eff(alpha)
      ∈ [0.00306989968658088935839839714017389525013805021339218732847054,
         0.00306989968658088935839839714017389525013805021885767255923311].

The interval ratio of EXACT endpoint info to positive-side limiting info is strictly enclosed by
    [20.5851891514052949478552096309113011745045680416361465338336,
     20.5851891514052949478552096309113011745045680788809699055546].
All lower information endpoints are STRICT positive; the information GAP is STRICT positive under the stated hypothetical iid covariance. The 20.585x display is a nuisance-TANGENT GEOMETRY effect, NOT a discontinuity in source fields, a physical phase transition, experimentally measured noise, network dynamics or any realistic NASH precision bound.

These figures independently match owner Geeky ROT023 to the displayed precision; author original FIRST retained. Numeric-only iid equal Gaussian covariance is an explicit hypothetical observation assumption; under a different fixed positive-definite covariance the profile information values differ although the rank jump mechanism can persist. A Gaussian Fisher numerical value must NOT be asserted to be source-measured.

## 5. Actual execution and integrity

Original NEW Python source:
    verify_m15_rot016_alpha0_symmetry_and_nuisance_information.py
SHA256:
    499ea16b642856782bd23df37b85eabcbf217fa9048b5871f0109b07fc252ed0

Original actually generated complete 55-digit directed result JSON:
    m15_rot016_alpha0_exact_symmetry_fisher_directed_results.json
SHA256:
    079f95fd497943e3323b60b49b5ca8ce83b495d861d16e56646ede14544e49bd

Exact SHA-locked independent source formula implementation from M15 ROT012:
    source_shape_operator_check.py
SHA256:
    4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e.

User-conversation COMPLETE local reproducibility ZIP:
    IW_M15_ROT016_ALPHA0_EXACT_SYMMETRY_FISHER_JUMP_INDEPENDENT_REPRO_001_20261115.zip
size 16,460 bytes, SHA256:
    978a1f8520d2bde6fd5556ca20a8d15e350499a0a6371c0c1830af30f725ab82.

Contains exact previous M15 formula source, new independently actually executed script, full machine-directed JSON, README, isolated clean replay output, negative tamper output and SHA manifest. Actual independent Python -I source math evaluation PASS. A separate fresh temporary folder copies the ORIGINAL two unmodified Python sources, ACTUALLY REEXECUTES them and outputs byte-for-byte IDENTICAL full result JSON; PASS. One byte of the base source is deliberately altered ONLY in a temporary copy, and the standalone script rejects the modified dependency SHA256 BEFORE SCIENTIFIC WORK, fail-closed PASS. Original source data unchanged. Final package ZIP CRC PASS and exactly 6/6 manifest payload SHA256 PASS; 7 ZIP members with manifest. No claim original historical M13 author code was byte executed or uploaded into this ZIP; it is a source-equation reimplementation.

The FULL original executable Python/55digit directed results remain in this user-local ZIP. Only the written scientific report plus curated results will be placed in public GitHub; no false public exact script-binary claim. GitHub write+readback alone is not a BW native ING receipt.

## 6. Final science ceilings and handoff

This is source-mathematical original owner-referee I1 internal nonblind verification of the exact Geeky ROT023 alpha0 reflection and information jump, plus an explicitly different Cauchy–Binet algorithm. No claim new theorem firstness, statistical experimental noise data or physical sensor transfer; REC12 and AUD2 have not yet independently reviewed this NEW ROT016 output as outside blind I3. The full original historical dtc0a_runtime_v0_3_1.py bytes remain unavailable, source field translation parameters do not exist in native M13 calc(), original 25 coefficient box does not imply physical Fourier-field realization, and no actual new field instrument has been tested.

Firstness preserved: original M13 source and GeeKy-S12 ROT022/ROT023 source mathematics, REC12 ROT001 independent ROT022 audit, M15 prior ROT013–015 bounded reviews. Further global alpha root/alias enumeration remains open, and this result should NOT trigger unrequested root grids or new hardware/run tasks. KN14 manages BW; no claim provider native ingestion, new CANON or EXEC_SIGN.

FINAL:
M15_ROT016_ALPHA0_EXACT_SYMPY_8_OF_41_SOURCE_MODES_PASS /
EXACT_27_REAL_YZ_REFLECTION_EQUALITIES_PASS /
FIFTH_FIXED_MASK_3_CERTIFIED_NONZERO_PERIOD_GENERATORS_PASS /
ALPHA0_16_ELEMENT_FIVE_SHELL_PERIOD_GROUP_PASS /
ALPHA0_NUISANCE_RANK3_AND_POSITIVE_SIDE_RANK4_IV55_PASS /
CAUCHY_BINET_INDEPENDENT_FISHER_20P58519_JUMP_PASS /
CLEAN_ISOLATED_REPLAY_BYTE_IDENTICAL / BASE_SHA_ONE_BYTE_TAMPER_FAIL_CLOSED /
GEEKY_ROT022_ROT023_FIRSTNESS_PRESERVED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
