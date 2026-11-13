---
artifact_id: IW_GEEKY_S12_ROT022_M13_SOURCE_MASK_ENERGY_PERIOD_GROUP_ALPHA_ZERO_JUMP_AND_FULL_POSITIVE_INTERVAL_001_20261113
date_of_source_execution: 2026-11-13
published: 2026-11-14
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_SOURCE_M13_N41_B_SYMBOLIC_SUPPORT_AND_EXACT_DIRECTED_POSITIVE_BERNSTEIN_PASS / M15_ROT013_DIFFERENT_CELL_I1_ROT020_REVIEW_PASS / ROT022_INDEPENDENT_REFEREE_PENDING
source_first: M13_PUBLIC_ORIGINAL_B_FOURIER_TT_OPERATOR_AND_DIRECTED_25_QUARTICS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_PUBLIC_M13_AUXILIARY_B_N41_FIVE_FIXED_MASKS / NEW_HYPOTHETICAL_COMMON_FIELD_TRANSLATION / NO_HISTORIC_DTC0A_RUNTIME_IDENTITY / NO_GENERAL_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT022 — discontinuous period-group enhancement of five fixed-mask source energies at alpha=0

## 0. Prior art, subtraction and new mathematical target

M13 FIRST original N41 sparse Fourier/TT/Lie B operator, its original five fixed spatial masks and outward-directed quartic table. Geeky ROT020 FIRST introduced the expressly HYPOTHETICAL common torus translation of ALL original source fields C1,C2,h relative to FIVE FIXED original observation masks and certified local rank-four (alpha plus three translations) modulo a common gain at alpha=.05; it exhibited the nontrivial translation (pi,pi,pi) leaving B unchanged. M15 ROT013 subsequently independently authored directed iv50 source-formula verifier, confirmed original Geeky ROT020 local rank4 and established that the complete stabilizer of the FULL original B TENSOR at alpha=.05 consists of precisely {0,(pi,pi,pi)}. M15 owns first independent review and tensor-support lattice tightening.

Independent M15 primary:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2613b178cfac6c1ede7f551bcbe6c3707bfbf17a/research/m15/2026-11-13/IW_M15_ROT013_INDEPENDENT_SOURCE_FOURIER_TRANSLATION_RANK_AND_EXACT_TENSOR_STABILIZER_001_20261113.md

ROT022 does NOT count this already mature FULL TENSOR theorem as a new finding. Instead it determines a different object over the FULL parameter interval: the period group of the FIVE SHELL ENERGY FUNCTIONS under common translations of the original source fields relative to FIXED masks. At alpha=0 we find a genuine enhancement that was not addressed by the generic alpha=.05 tensor theorem.

## 1. Definition, not pointwise collisions

Original unmodified M13 source operator:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original immutable source Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679 (8970 bytes).

Original M13 25 B quartic directed coefficients:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Immutable Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 (7501 bytes).

N=41, B channel, original five masks k=2,..,6. For fixed alpha and torus translation t∈T³ applied to ALL three input fields, the original source operator has exact convolution/diagonal covariance B_alpha,t(m)=exp(i m·t) B_alpha,0(m). The observation masks do NOT move. The five disjoint source shell energies S_i(alpha,t) are the original linear combinations of nested M13 mask mean energies with shell weights (7778,6938,6146,5402,24389).

Define the PERIOD GROUP of five whole functions (a group under addition modulo 2pi):

 G_alpha = {u∈T³ : S_i(alpha,t+u)=S_i(alpha,t) for EVERY t∈T³ and EVERY i=1,..,5}.

This is NOT the set of accidental pairs t1,t2 with equal five shell vectors. NOT the period group of four projective ratios alone. NOT the stabilizer of the FULL tensor B unless independently stated. These distinctions matter; energy can be unchanged even if tensor changes by global sign.

## 2. Main exact classification

For original N41 B source and all alpha in [0,1/5]:

- **alpha=0**: G_0 consists of EXACTLY 16 elements:
  { (a*pi/2, b*pi, c*pi) modulo 2pi : a in Z/4, b,c in Z/2 }.
  Corresponding full-B tensor period group at alpha=0 has EXACTLY 8 elements, not 16.

- **every real 0<alpha<=1/5**: G_alpha is EXACTLY {0,(pi,pi,pi)} modulo 2pi, i.e. 2 elements. The FULL tensor B also has 2 elements in this interval.

The group's enlargement from 2 to 16 occurs at the single endpoint alpha=0. No claim of global one-to-one inversion of the translation parameters from five energies is made.

### 2.1 Rigorous alpha=0 symbolic source support

A NEW independently authored SymPy polynomial reconstruction copies the SOURCE FORMULAE (NOT the numerical output) for B at alpha=0 and uses FOUR algebraically independent formal centered-derivative symbols d1,d2,d3,d4. Thus possible numerical cancellations of trigonometric values cannot fake the support result. Out of the 41 original sparse B mode labels, 33 tensor matrices vanish EXACTLY as formal polynomials. The remaining EIGHT labels are exactly:

 (±2,±1,±1), all independent sign combinations.

Every nonzero tensor component is a rational multiple of d1*(2*d1-d2). At N=41, d1=sin(2pi/41)/(2pi/41)>0 and d2=sin(4pi/41)/(2pi/41), so 2*d1-d2=2*d1*(1-cos(2pi/41))>0; all eight modes really are nonzero.

The formal source reconstruction was separately evaluated with original native M13 mpmath.iv 45 dps derivative values and compared directly to 369/369 original unmodified B tensor complex components; ALL 369 complex source differences have real and imaginary directed intervals containing zero (consistency check, distinct from formal proof).

Every energy Fourier difference frequency d=m-n from these EIGHT modes lies in the index-16 lattice:
 L0=4 Z × 2 Z × 2 Z.
So every group element satisfying this lattice's annihilator is a period of ALL five energy functions.

To prove EXACTNESS rather than a mere lower bound on group size, the original innermost fixed mask k=6 spectral energy has three coefficients with frequencies d=(4,0,0),(0,2,0),(0,0,2). All THREE have STRICT positive original iv45 real parts, even though the complex coefficients may also have imaginary parts. Their integer determinant is +16. Since they generate L0, Fourier uniqueness implies every common energy period must annihilate ALL L0; no additional periods exist.

For the FULL B tensor, the lattice generated by the 8 original nonzero mode labels has integer index EIGHT (direct SymPy Hermite normal form). Hence its own exact unit-phase period group has 8 elements. Its difference-frequency energy group has index16 because a common sign of all eight B modes leaves the energies unchanged; a generic energy period need not leave B itself unchanged.

### 2.2 Rigorous EVERY positive real alpha source period group

The original B tensor at any alpha is a quadratic polynomial in alpha, B_m(alpha)=U_m+alpha V_m+alpha² W_m. The exact source parity of its Fourier support makes m_x+m_y+m_z EVEN for every contributing mode, so (pi,pi,pi) and zero are always source B periods and therefore all-shell-energy periods.

To EXCLUDE all other periods for EVERY positive real alpha up to 1/5, construct the original innermost fixed-mask k6 energy Fourier coefficients at the three specific translation frequencies:

 d1=(-2,0,0);
 d2=(-1,1,-2);
 d3=(-3,0,1).

These three integer vectors have determinant -2. Their integer span equals the entire index-two even-total-parity lattice. Their corresponding source spectral energy coefficient c_d(alpha) has EXACT zero constant term at alpha=0 by the separately proven formal eight-mode support (each d is outside the alpha=0 difference lattice). Thus exactly c_d(alpha)=alpha*q_d(alpha), with q_d a degree-at-most-3 polynomial. The source coefficients of the higher terms come from the original unchanged tensor_polys(41) and original window_mode spectral kernel using outward mpmath.iv 45 dps; no substitution of rounded output.

On all real alpha∈[0,1/5], the REAL PART of EACH q_d has its four Bernstein coefficients strictly positive, producing **12/12 STRICT POSITIVE SOURCE-DIRECTED BERNSTEIN SIGNS**. Human-display lower bounds in units 1e-16:

 - d1: [+646.822306618676,+917.9860240804702,+1184.0082057412537,+1444.9614260848207].
 - d2: [+1.1550289035432877,+0.8942261626180719,+0.6382122873264195,+0.3869204054552744].
 - d3: [+2.8574865376889993,+6.199358708915106,+9.478315177445339,+12.695241935224683].

Thus each c_d(alpha) is NONZERO for EVERY alpha>0 in the requested interval. Any common period of the whole energy functions must have exp(i d_j·u)=1 for all THREE independent generators. Their determinant -2 gives at most two periods; the known parity period supplies both. Therefore G_alpha= {0,(pi,pi,pi)} for all 0<alpha<=1/5.

This is continuous-interval source proof, NOT a finite alpha grid nor an inference from only alpha=.05. It says exactly which translation shifts preserve all five entire functions for ALL t, NOT that the five energies have no other individual coincident values.

## 3. Near-endpoint stability warning; no physical response radius

At alpha=0, the additional period u=(pi/2,0,0) preserves ALL five energies exactly. At alpha=.05 the actual unmodified M13 k6 energy difference after this input translation is STRICTLY negative in original source interval arithmetic:

 S_k6(.05,u)-S_k6(.05,0)
 in [-1.8325778429169983886597266613202347025289021345704e-14,
     -1.8325778429169983886597266613202347025285890676156e-14].

The independent direct 3D spatial IFFT checker on original N41³ grids confirms ALL five fixed mask energies exactly unchanged at alpha=0 for the quarter shift and strongly changed at alpha=.05. The actual example k6 difference is -1.8325778429169993e-14 in displayed float. This source fixture is DIAGNOSTIC; the complete group proof uses exact frequency lattice and directed Bernstein intervals, not just the quarter-shift sample.

Because c_d(alpha)=alpha*q_d(alpha), extra frequencies break the enlarged group at first order in alpha as alpha leaves zero. In particular d1=(-2,0,0) changes phase by -1 under u=(pi/2,0,0). Parseval on the torus parameter t gives a rigorous LOWER bound on the root-mean-square difference of k6 translated energy functions:
 RMS_t[S_k6(alpha,t+u)-S_k6(alpha,t)] >= 2 sqrt(2) alpha * 6.46822306618e-14,
for all 0<alpha<=1/5 (the decimal constant is deliberately rounded DOWN from the minimum directed real Bernstein bound for the first frequency). This is **not** a positive pointwise separation for every t, an empirical physical noise margin, or a lower bound on projective log-ratio separations.

## 4. Actual source execution and adversarial controls

The actual original source and new executable reproduction exist in user LOCAL ZIP (not claimed separately public as byte-identical author scripts):
 Geeky_S12_ROT022_exact_mask_energy_symmetry_transition.zip
 size: 19182 bytes
 SHA256: 5495d8f5fb5e3ad28f9a2ef111a33f11581cdaa9455b4cd5ca8502c54344c6ba

10 members:
- New original Python SymPy+mpmath.iv45 exact group/lattice/exhaustive 12-gate source certificate, 11020 bytes, SHA256 f0ba423d460839c8276ebfe34c863cbbce31d14ff59f440b3ac40097d7be7d94.
- Independent new 3D spatial NumPy FFT masked energy checker, 1688 bytes, SHA256 b75dc6c3c9bb098dc8fcc3427e6c98c034397183a3d632f14c47809a0312b9aa.
- Original immutable M13 helper Python exactly 8970 bytes and B table exactly 7501 bytes, both original Git blob SHA1 identities verified BEFORE importing scientific source.
- Actual FULL 8309-byte source output JSON with exact directed interval endpoints of all three alpha0 energy generators and all TWELVE alpha>0 Bernstein bounds, SHA256 eadc03105b4f2158386dbb750511cff9fe0a553991f883c53f044b2162d32e8c.
- Independent actual FFT result JSON and fail-closed clean replay test, README and full SHA256 manifest.

ZIP CRC PASS, 9 payload members match their complete SHA256 manifest and exact byte readback; total ZIP entries 10 including manifest. Independently extracted and re-executed the full SymPy/mathed source in a clean isolated Python subprocess and checked that its COMPLETE JSON output was byte-identical to the archived result (2026-11-14 confirmation). Two temporary 1-byte corruptions of the original M13 module and original B table were independently rejected BEFORE source import, exit code 1 with ORIGINAL SOURCE GIT BLOB MISMATCH. Original M13 files untouched. The full source code was ACTUALLY executed locally; no false claim the full executable byte string is published as a GitHub code file.

## 5. Limitations, ownership and disposition

The group of WHOLE functions G_alpha is a global symmetry group, NOT the global inverse fibers of five observations, and NOT the period group of the four ratios that remove overall energy gain. Those questions may have larger alias sets.

The common field translation is an explicitly constructed in-memory mathematical test with fixed original observation masks; source() and calc() do NOT expose physical translation controls. Co-translating windows with fields eliminates this effect. Source alpha=0 is an endpoint of the auxiliary source parameter domain and is not an empirically validated physical phase transition or an observed dynamical symmetry-breaking phenomenon. All calculations concern original public M13 source, B channel N41 five fixed masks. Historic original dtc0a_runtime_v0_3_1.py byte identity is still missing.

M15 independently I1 reviewed ROT020's alpha=.05 full tensor local rank and size-two tensor stabilizer. There is NO independent different-cell I1 review of the new ROT022 alpha=0 symbolic support, sixteen energy periods or whole-positive-alpha 12 directed Bernstein gates. M13 is FIRST source; M15 retains independent tensor review firstness; Geeky ROT022 first this new source-specific group classification. Mathematically the lattice duality and Fourier coefficient positivity arguments are standard, no general mathematical novelty. No external physics, NASH J3/K/TPE transfer, physical discovery, CANON or EXEC_SIGN. No owner/KN14 BW acceptance evidenced by GitHub publication.

NEXT valid reviewer question: separately reproduce SymPy alpha0 support using original source or a new implementation, and independently verify 3 nonzero alpha0 spectral coefficients and 12 all-positive-alpha Bernstein signs; compare period group definition and distinguish from global energy observation aliases. Do not micro-scan alpha near zero as a replacement for proof. No automatic task cascade.

FINAL:
 ORIGINAL_M13_IMMUTABLE_SOURCE_CALC_B_N41_LOCK_PASS /
 ALPHA_ZERO_SYMBOLIC_8_OF_41_MODES_EXACT_PASS /
 ALPHA_ZERO_ENERGY_FREQUENCY_LATTICE_INDEX16_PASS /
 ALPHA_ZERO_TENSOR_WAVEVECTOR_LATTICE_INDEX8_PASS /
 ALPHA_POSITIVE_ALL_REAL_0_TO_0P2_12_BERNSTEIN_GATES_PASS /
 ALPHA_POSITIVE_ENERGY_AND_TENSOR_PERIOD_GROUP_ORDER2_PASS /
 QUARTER_SHIFT_ENERGY_DIAGNOSTIC_PASS /
 CLEAN_ISOLATED_BYTE_REPLAY_AND_TWO_INPUT_TAMPERS_PASS /
 INDEPENDENT_ROT022_REFEREE_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
