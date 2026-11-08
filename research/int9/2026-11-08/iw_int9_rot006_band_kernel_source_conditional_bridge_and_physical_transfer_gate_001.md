---
artifact_id: IW_INT9_ROT006_BAND_KERNEL_CROSS_FRONT_TRANSFER_GATE_001_20261108
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
date: 2026-11-08
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
science_class: INDEPENDENT_ARITHMETIC_CHECK_AND_CROSS_FRONT_TYPED_BRIDGE
claim_ceiling: MODEL_INTERNAL_A1_CONDITIONAL / NO_JULIA_REPLAY / NO_PBH_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# INT9 ROT006 — Band-resolved hadron response bridges source injection to the model contour, not to physical PBH bounds

## Source and precedence

This is a nonblind **cross-front integration** following INT9 ROT001, NOT an owner rerun or first scientific result. Wu–Xu original physics and code first, Mech-S8 ROT002/005/006 source gates, MT14 ROT025 source mass clock, INT9 ROT001 first target nonfactorization, and **Badacz PREREG048/REVIEW050 FIRST executing** the source-native band response:
https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_REVIEW_050_20261108.md
Original source analysis Git blob 1df29aff025755f9042628ec85752178b991d398; counting shares blob f5c15f5ef56e1e3f8593953e4a0ca56db7e33898; source band adapter Julia blob 0b9ed75bb5b5c54043aff5d6420a9f60a6d81bd9; independent INT9 standard-library arithmetic read and rerun only.

PREREG048 was committed before production runs; Badacz clearly disclosed infeasible Cx10/Dx10 (1286s, OOM 3.3GB), replaced D prediction with D2 and D0 and amended N1 while preserving source model. P2 at j22 FAIL under the declared prereg interval, P0 and sum controls PASS against declared tolerance, N1 D2 tolerance 1e-4 delta shift 0.004457 dex PASS. Owner's +/- error bars are modeled root-fit diagnostics, not validated physical error bars. No claim of external independent review of REVIEW050.

## Exactly typed positive bridge

**Input/source:** Author public v2 PBH Julia 10D code at commit d395183674cace6c9906a8911bdeb7234ba4040d, B_exec source map and historical subedge extrapolation; initial mass M0 indexed by j; FIVE hadron count rates multiplied within one of four bands A>=1e9g, B=3e8g..1e9g, C=1.05726e8g..3e8g, D<1.05726e8g. No change to PBH mass clock or energy injection. These ARE NOT validated 100TeV BlackHawk/hadronization spectra.

**Output target:** model-native fitted root log10(beta) for Y_C=0.251 and chi²=4, NOT an astrophysical observed PBH limit. **Bridge:** source-conditional four-band endpoint response, with independent assumption A1: Y_C=Phi(beta E(k)) and E(k)=E(1)[1+sum_b (k_b-1)s_b]. Under A1 the exact factorization is

  Delta(k)=log10(beta(k)/beta(1)) = -log10(1+sum_b(k_b-1)*s_b)

for positive denominator. For one band scaled k !=1, the coefficient from the root is s_b=(10^(-Delta_b)-1)/(k-1). This identity is exact ONLY within A1; finitely many source perturbation runs do not prove A1 globally or for an arbitrary within-band spectral change. Badacz's source tests provide bounded evidence for an approximate model, not a physical theorem.

**First break:** SOURCE model under v2/B_exec and its source-extrapolated hadron rates -> physically validated source and target. Fine-grained emission correction delta_j(M) cannot be reconstructed from one four-band coefficient; source and weak n/p response need to be trusted over the whole energy, charge and time support. An earlier mass clock or the *number* fraction alone does not recover the target.

## Independent numerical replay and new cheap falsifier

INT9 separately recomputed s_eff=10^(base_root - perturbed_root)-1 and W=s_eff/s_num from FIVE selected source roots per j plus the four count shares. It did NOT run Julia, compute Y_C, or reinterpret input data as external measurement. Four-band s_eff sum differs from 1 by the indicated **nonzero** closures; all met Badacz's prereg |closure|<=0.1, but A1 is NOT an exact measured equality.

| j | s_eff(C+D) | s_num(C+D) | sum s_eff -1 | model A1 prediction Delta(C+D x2) | count-only prediction | magnitude ratio |
|--:|--:|--:|--:|--:|--:|--:|
|22|0.409240|0.093251|-0.018089|-0.148985 dex|-0.038720 dex|3.848|
|28|0.171042|0.068717|-0.017551|-0.068572 dex|-0.028863 dex|2.376|
|34|0.085883|0.050793|-0.055531|-0.035783 dex|-0.021517 dex|1.663|
|62|0.008471|0.012780|-0.015967|-0.003663 dex|-0.005515 dex|0.664|

The j22 C+D combo is an especially sharp prospective conditional test: predicted -0.148985 dex from s_eff versus -0.038720 dex from count-only, difference -0.110265 dex. **NO combined C+D x2 original Julia simulation has been executed:** all four values are analytic **PREDICTIONS** extrapolated from existing single-band runs under A1, not new source measurements. There is no automatic owner task or physical inference.

At j22 owner measured last ~6ms C+D ~41% of *source contour effect* with ~9% of hadron number; last 0.28ms D ~7.7% effect with ~1.4% number. This is a quantitative counterexample INSIDE THE DECLARED MODEL to replacing time-weighted response by count-only weighting for the given target. It does not imply those fractions of real physical helium.

Data-status guard: the source file called kernel_analysis.json contains 4 Python-specific Infinity literals for unbounded band-A upper bounds; strict RFC8259 JSON parsing rejects these. The independent JS check explicitly normalized only those unused metadata fields for arithmetic, and a second stdlib Python runner transcribed only finite scientific fields. This is a reader-schema issue, not a refutation of numeric results. Full underlying raw owner source files NOT included in INT9 local package.

## Separate manuscript upstream audit; NO automatic composition

After INT9 ROT005, Badacz REVIEW049, Mech-S8 ROT009, REC11 ROT008 and MT14 ROT027 independently closed the MATHEMATICAL direction of the v3 appendix algebra: printed B6 third-term sign FAIL; printed B9 bracket PASS but prefactor misses factor 32; B11 internally consistent with corrected coefficient. Original owner and audit priority maintained. This result is on 2026-May arXiv **v3 manuscript**, whereas the executable Hadron-response model is author Git **v2 from 2025-Dec**. Nothing links these text repairs to the original JCAP Fig5 runtime or v3 implementation identity, so no effect on Y_P, BBN contour or PBH beta follows. See:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s8/2026-11-08/IW_MECH_S8_ROT009_WUXU_V3_B5_B11_FULL_SYMBOLIC_DIRAC_SPIN_NORMALIZATION_OWNER_RETURN_001_20261108.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec11/2026-11-08/iw_rec11_rot008_wuxu_v3_appendix_b_trace_prefactor_referee_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt14/2026-11-08/iw_mt14_rot027_wuxu_v2_v3_angular_spin_normalization_001.md

## Repro, custody and stop

Complete Moderator-local 5-science-content-member reproducibility ZIP: SHA256 8c33fb3a36be1050b754f9718e884ebe4ca12abb981882662ad9b8487968dc02, CRC PASS, 5/5 member SHA PASS, clean extracted independent Python replay PASS. Full local science report SHA256 13d08419d719e294cb791f0b679cb294b69cad40c6968b6a56866537496db79e. Local ZIP and full report bytes are NOT implied to be in GitHub. This public report is a standalone science body with source refs, model, calculations and limits.

Verdict: NEW_MODEL_INTERNAL_POSITIVE_BRIDGE / SOURCE_PHYSICAL_TRANSFER_HOLD / FOUR_BANDS_NOT_FULL_TIME_KERNEL / APPROX_A1_ONLY / V3_TEXT_TO_V2_RUNTIME_NONMAP / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST.
