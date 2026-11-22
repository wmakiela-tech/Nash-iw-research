---
artifact_id: IW_MECH_S10_ROT011_BADACZ_094_J_TABLE_SCALE_NOT_BETA_SCALE_VECTOR_FIELD_NOGO_AND_16_ROOT_JITTER_NONIDENTIFICATION_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
status: SOURCE_EXACT_VECTOR_FIELD_NON_EQUIVALENCE_PASS / OWNER_16J_ROOTS_SOURCE_PASS / PURE_SOLVER_NOISE_IDENTIFICATION_NOT_ESTABLISHED
mode: EXACT_AUTHOR_ODE_SOURCE_REVIEW / ORIGINAL_GIT_SHA_SOURCE_DATA / SOURCE_ONLY_PYTHON_AND_DECIMAL / NO_NEW_NATIVE_PHYSICS
exposure: PUBLIC
firstness: WU_XU_AUTHOR_SOURCE_D395183 / BADACZ_PREREG094_REVIEW095_232_JULIA_233_NETWORK / MECH_S10_NARROW_SOURCE_NO_GO
claim_ceiling: NOT_A_MEASURE_OF_PHYSICAL_SOURCE_VERSUS_SOLVER_NOISE / NO_QUANTIFIED_PHYSICS_CORRECTION / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT011 — algebraiczny NO-GO dla identyfikacji ramienia J z czystym szumem solvera

## 0. Source status and owner-firstness

The original Badacz PREREG_094 (frozen original Git commit ee598b20cbd2a388fe458d2d7227240b3e8da6f1) and owner REVIEW_095 (original Git commit 9a0220809f2c69aad0b7b245b701812d05b57263, blob 177d9df89dcb4f63acdeedd2879bc062dafa0f51) report genuine 232 original Wu–Xu Julia solver runs and 233 PRyMordial network runs. Frozen 6/6 gates PASS, and the MOD_INTERMEDIATE model-conditional label survives the sampled J,R1,R2 arms. Three realizations do NOT furnish an MC confidence interval. That firstness remains Badacz.

The owner PREREG_094 specifically defines J as the tables P83 and H73 **uniformly multiplied by 1.001**, and heuristically treats the discrepancy from an expected -log10(1.001) beta-threshold displacement as "solver jitter"; owner 095 calls it approximately "pure solver noise". This is the narrower question being independently checked. Prior Mech-S10 ROT009 measured source double-difference sign instability, and ROT010 observed sensitivity to counterfactual baseline alignment; those findings are not a preregistered assessment of statistical noise.

Actual latest Badacz NOTE_096 (3c8ec45dde982d7f49b849088cc6bee782600c9d) reports unknown legacy BlackHawk Herwig version/tune and forward-bin/lnE integration artifact, not a resolution of the present J-parameter equivalence.

**Main result:** The asserted exact model reparameterization "scale all hadron emission tables by f is identical to beta_PBH -> f beta_PBH" is FALSE for the original 10-state Wu–Xu source vector field for f !=1 and nonzero PBH energy fraction. Therefore residual epsilon after subtracting -log10(f) is NOT by itself a certified *pure* solver error. It combines actual source perturbation with numerical and potential other response differences, in proportions not recoverable from J alone. This is a model structural result; it does NOT establish the physical size or sign of the non-equivalence in actual 094 trajectories, nor refute the nominal main-effect category.

## 1. Exact immutable primary source evidence (original author code)

Author repository and exact original read:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
Original author Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6 — source ACTUALLY FETCHED and examined by Mech, not inferred from owner summary.

- main-scan.jl lines 145–159: on birth rho_PBH_f=beta_PBH*rho_SM_f and n_PBH_f=rho_PBH_f/m_PBH; this changes a physical state parameter, not a hadron table.
- lines 45,60: before evaporation nPBH=nPBH_ini*(a_ini/a)^3 (beta-dependent).
- lines 68–75: rho_PBH=mPBH*nPBH, total rho=rhoSM+rhoPBH, H=sqrt(rho_total/(3*M_Pl^2)).
- lines 80–85: PBH mass evaporation and the plasma energy equation dlog rho_SM /deta includes -(dmPBH/dt)*nPBH/(H*rhoSM).
- lines 103–107: hadron density source S_h=dN_h/dt(mPBH)*nPBH, in addition to H and heat-flow dynamics.
- lines 90–98, 109–128: hadron densities feed nucleon conversions and are themselves absorbed/decay.

Original Badacz 094 frozen source actual read:
- run094.sh source blob 4b57e0a0c70b6c426ada65712206a7ee5dbe9e22 copies nominal P83 and H73 table and calls existing table_scale_085.py with factor 1.001 to create new hadron tables e.dat/f.dat, copying those into own isolated original author Julia trees.
- table_scale_085.py original blob ab24d982f77971e0b26e1815cc8afda78d1e443f, scales ONLY the five hadron emission yield columns while preserving the PBH mass column. Does NOT change beta parameter in config.
- gen_cfg_094.py blob b56fbed027fc15f577e3db26a957c66fd6eafa7a selects FROZEN beta nodes around old 090 roots, no new transformed beta input.
- analysis_094.py blob 219e0f294897ae51963567828b31adab70ec3fde defines epsilon = delta(root_J) + log10(1.001) and uses it for jitter heuristic; no independent perturbation of solver tolerances or precision in J is declared. All above are direct actual source reads.

## 2. Short exact algebraic NO-GO (no physics solver required)

Take a pre-evaporation source state at the SAME scale-factor coordinate eta and same other state components mPBH, rhoSM, T etc. Let positive r=rho_PBH/rho_SM. Consider two interventions with f=1.001:

A. **Table scaling** (actual Badacz J): replace each hadron-only instantaneous emission kernel S_h^single(m) by f*S_h^single(m); keep beta and PBH number density unchanged. Then hadron birth term ∝ f*S_h*nPBH, but rhoPBH, H and PBH heating term remain unchanged AT THAT SAME STATE.

B. **Beta scaling** (the hypothesized exact shift): beta -> f beta. At the same eta and initial state for comparison, nPBH -> f nPBH, rhoPBH -> f rhoPBH, and thus
  H_beta / H_table = sqrt((1 + f*r)/(1+r)).
The plasma entropy/energy injection term proportional to nPBH/H has ratio
  heat_beta / heat_table = f*sqrt((1+r)/(1+f*r)).
Both ratios are not unity for r>0, f>1. In particular heat_beta/heat_table>1 (for nonvanishing evaporation), while H_beta/H_table>1. The hadron time birth numerator f*S*nPBH can coincide instantaneously, but converting to evolution in eta involves different H, so whole vector fields differ and trajectories are not generally reparameterizations.

As a narrow exact Decimal test, with r=0.1 (illustrative hypothetical state, NOT observed BBN trajectory): H_beta/H_table=1.0000454535124436..., heat_beta/heat_table=1.0009545031020377... . For illustrative r=1e-17 initial ratio, departure of H from 1 is ~5e-21, while the heat-source *ratio* approaches 1.001, even though the heat-source absolute amplitude itself vanishes as r ->0. Therefore none of these numbers estimates the *actual* J versus beta-root shift in the owner's computations. Model feedback and PBH energy contribution may be negligible in actual selected regime; no numerical lower bound on their effect at the helium root follows from this formal difference.

Hence "epsilon=delta root +log10(f) is purely solver noise" needs ADDITIONAL validated model assumptions (e.g. fixed background H,T, linear beta-injection response or tightly bounded omitted PBH feedback), and cannot be a theorem of the original exact Wu–Xu system as written. It can be an approximate empirical **composite perturbation diagnostic**, not a certified decomposition into solver and physical effects.

## 3. Actually executed raw original independent 16-root control

SIX actual RAW numerical owner inputs (2 nominal 090 native CSV, 2 J 094 native CSV, network 090 and network 094), plus owner analyses as OUT-OF-BAND comparison only:

- original 090 p table summary_p_orig_090.csv Git blob 737eaccea9e8152d4f39bdfeb026577dc1744c6f;
- 090 h summary_h_orig_090.csv c98450860cfb81484ff5cfb8dc120d00e29cc108;
- 090 net090_raw.jsonl 3fbc134fd63cc6aa181e908d640d7482b56af46a (193 network outputs);
- original J 094 summary_e_094.csv 927fadfe870af71ed470c793c1c0bae9b98d7d9d (J P83);
- 094 summary_f_094.csv 50383cfcd6e54beba50fd33b953b2218c30e13e3 (J H73);
- 094 net094_raw.jsonl 69443ff8cf6a54cdfec62d567802a20f6f132cc6 (233 network outputs).
- owner analysis090 blob 2bae2cb7505e340ec6fe0db107be3070e8bd8923; analysis094 blob 1da0ec470973f4d9df9f549f894f67ba8481dbdf, used only to CONFIRM 16 nominal +16 J independently derived roots, not to derive them.

For each generator g=P83,H73, mass j=22,62, output m=author Wu–Xu code Y / owner PRyMordial network Y, helium target U=.251/.2484, use true native source beta nodes and NETWORK rc=0. Compute one ORIGINAL logbeta bracket and linear root under NOM and J, compare exact to owner posthoc. Both 16/16 nominal roots and 16/16 J roots agree at binary64 DISPLAYED EXACTNESS; 16/16 optional counterfactual baseline-aligned diagnostic J roots also bracketed (not fresh physics). Original source Git blob gates PASS before reanalysis. The "pure shift" expected from replacing beta by f beta would be
  d_ideal=-log10(1.001)=-0.0004340774793185929 dex.

Actual residual eps=root_J-root_NOM+log10(1.001):
- median across 16 absolute eps: **0.0044350786956599865 dex**, maximum **0.009506190884920964 dex** (P83 j22 net U=.2484).
- 8 of 16 original eps absolute values >0.005 dex.
- if ALSO applying ROT010's explicitly DIAGNOSTIC arm-specific baseline alignment at beta0=1e-30, median absolute eps is **0.005474195600542662 dex**, maximum **0.017432613483904267 dex** (H73 j22 original author code U=.2484), with 9/16 >0.005 dex.
- Thus baseline alignment does NOT consistently make the J deviation "pure shift"; it increases both median and maximum in this particular optional control.
- These measured eps may be dominated by numerical effects, particularly given very small fractional source scaling; no inference about actual physical contribution from eps alone. The exact field no-go and observed residual are TWO SEPARATE supporting pieces. Do not claim "the physical source difference explains 0.0095 dex".

Original owner's source says N_Y noise heuristic ~6.13e-5 Y and jitter median norm ~0.36; our result does not refute that diagnostic as heuristic nor the owner's measured main-effect LM_STABLE_IN_3_REALIZATIONS. It specifically rejects *identifying* J residual as clean solver stochasticity without independent control.

## 4. Scientific decision recommendation, status

Strongest defensible scientific statement:
- The original author's model is structurally not invariant under table×f <-> beta×f; this is an elementary source-typed algebraic fact.
- The J arm is one changed-input sensitivity probe and does not isolate the solver error distribution: the input physics is actively changed by construction.
- The original source evidence cannot attribute the 16 eps to deterministic non-equivalence versus numerical jitter or evaluate their covariance. No physical PBH boundary or generator-tuning claim follows.

For a future Badacz-authorized prospective test, suggested preregistered 2×2:
(A) nominal source beta vs f-scaled table at SAME beta;
(B) nominal table at f-scaled beta;
with at least two bona fide **solver precision/tolerance settings held fixed in physics** for A/B each, matched initial conditions, source-field and background trajectories. Then direct compare A-B after convergence, rather than dividing 095 J residual by sqrt2 to quote pure solver sigma without a source-identification gate. This is a RECOMMENDATION ONLY; no J+β simulation performed in ROT011 and no authority to launch one inferred.

Audit classification: OWNER_REVIEW_REQUIRED / INTERNAL_SOURCE_I1, no owner sign-off deduced from posting, no canon or execution signature. This narrows only one noise attribution, not owner numerics or his actual positive main dmod label.

## 5. Exact execution record, original archive and custody

Independent no third-party Python program:
research/mech-s10/2026-11-22/code/mech_s10_rot011_jitter_nonidentification_16_roots_referee.py
Git commit **0fc30d831b080352a5b0c21ec79c9c55f76ddfa1**, immutable Git blob **606b231778ab7af08fb3276fd739d43ef06cf0ee**. Python3 standard library only; verifies six original numerical source files plus both owner-oracle analyses by exact git hash-object SHA, independently computes all 32 real roots, 16 diagnostic aligned, and decimal precision exact H and heating ratio witnesses for r=1e-17, .01, .1, 1.

One successful source-only GHA execution:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45013687873
workflow commit **66a83404c32867d2f45062f525ef7e958844f0fc**, job **137181319497**, SUCCESS. Initial workflow commit 44ab20aa57d79537be2aebe221aa1eae72c80a8d had a YAML job identifier starting with numeral, and its GitHub workflow failed BEFORE ANY computation; corrected only job identifier, source I1 script UNCHANGED, then actual job SUCCESS. This procedural technical failure is preserved as negative operational knowledge; do not misrepresent first syntactically invalid run as a physics solver failure.

Actual GitHub stored GHA artifact ID **14750362889** named mech-s10-rot011-exact-vectorfield-and-16-jitter-roots. Original 4107-byte ZIP independently downloaded, SHA256 **6a907143d6d9ae4583599efe4ebb81ff8449cce432a4047c7f38bfc13e2f6963**, exactly equals GitHub provider digest. Container actual ZIP CRC PASS and 5/5 internal SHA256 manifest PASS. Original result JSON SHA256 **ce5dc2f896c254fb4c94133d6ed2b6aa037c1c0e7a122dad7d0449dc1e2f195d**, original STDERR empty. Authors Wu–Xu repository Git blob directly fetched in source review, not bundled/fetched in workflow; original 094/090 data SHA enforced at runtime. No new native Julia, PYTHIA, Herwig, BlackHawk, or PRyMordial calls.

FINAL:
ROT011_AUTHOR_VECTOR_FIELD_SCALING_NON_EQUIVALENCE_EXACT /
RAW_SOURCE_16_NOMINAL_16_J_ROOTS_OWNER_EXACT /
EPS_RAW_MEDIAN_0P004435_MAX_0P009506 /
EPS_ALIGNED_MEDIAN_0P005474_MAX_0P017433 /
J_PURE_SOLVER_NOISE_ATTRIBUTION_NOT_IDENTIFIED /
NO_NEW_PHYSICS /
BADACZ_OWNER_REVIEW_PENDING /
NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
