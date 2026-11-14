---
artifact_id: IW_MT15_ROT024_WUXU_ORIGINAL_NATIVE_J22_POSTEV_EOS_RESIDUAL_9200_9300_WINDOW_LOCALIZATION_SOURCE_AUDIT_001_20261114
created_at: 2026-11-14
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: BOUNDED_ORIGINAL_NATIVE_ONE_J22_SOURCE_10D_AND_AUTHENTICATED_THERMO_MODEL_RESULT_TIME_WINDOW_LOCALIZATION
status: ORIGINAL_NATIVE_10000_CSV_SHA_PASS / ORIGINAL_NATIVE_16_MEMBER_HASH_PASS / EXACT_NATIVE_16_ANCHOR_S_REPLAY_PASS / MODEL_LUT_16_SOURCE_FIXTURE_SHA_PASS / LOCALIZED_REFERENCE_INDEPENDENT_SIGNED_TELSCOPING_PASS / CLEAN_OFFLINE_REPLAY_PASS
claim_ceiling: SOURCE_CODE_V2_THERMO_MODEL_VERSUS_SAVED_SINGLE_J22_NATIVE_TRACE / NOT_CAUSE_IDENTIFICATION_OR_NATIVE_SOLVER_ERROR_BOUND / NO_NEW_JULIA / NO_PHYSICAL_Yp_PBH_OR_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT024 — Where does the ROT023 Wu–Xu postev 0.1576% native-versus-source-model entropy residual accrue?

## 1. Original source, custody and novelty ceiling

ORIGINAL AUTHORS FIRST: Quan-feng Wu and Xun-Jie Xu, JCAP 02 (2026) 063; frozen original public author Julia v2 repository Fenyutanchan/Primordial-Black-Hole at commit d395183674cace6c9906a8911bdeb7234ba4040d, main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6, original 1000-row g_rho,g_s(T) Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8, source inverse lookup interpolator Git blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc.

FIRST SCIENCE: Mech-S9 ROT002 FIRST found Wu–Xu source nonadiabatic EOS/entropy-null; other original-source independent checks by REC11, KN13, INT9 and MT15 ROT010. Mech-S9 ROT013 FIRST executed the unchanged author source REAL 10D one j22 Julia run and captured all 10000 source-native CSV rows. MT15 ROT022 FIRST in-cell original 10D postev entropy actual-versus-original code EOS source model comparison; ROT022 V001/V002 earlier helper quadratures explicitly SUPERSEDED by V003 (INT9 ROT030 source correction firstness). MT15 ROT023 FIRST in-cell separated original 1000-node inverse rho-to-T lookup contribution to the 0.158% native-vs-continuum source-model discrepancy. This ROT024 does not claim discovery of the source EOS issue or a new mathematical theorem, only independently localizes the residual along ACTUAL native saved source time-temperature anchor windows without changing source code.

Authentic original native owner data: Mech-S9 GitHub Actions run 43436800793, artifact 14045176436, unchanged original 713794-byte ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486, full original 10000x19 author native CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1, original ZIP CRC and 16/16 original member SHA256 PASS. Original first zero-PBH saved native row8545 to final row10000 yields 1456 actual nPBH_zero source rows. NO new Julia solver ran in this MT15 rotation. Original j22 input is a callable model input, not an original paper on-grid beta sample.

## 2. One mathematically well-typed local source residual

Original source background entropy proxy is S_com proportional to a^3 T^3 g_s(T), not full physical plasma entropy. ROT023 independently source-computed at 16 original native anchor temperatures both:
- Source continuous Wu–Xu no-PBH EOS with IDEAL exact inversion of rho(T).
- SAME original Wu–Xu source equation with AUTHORS' actual 1000-node log-rho-to-log-T inverse lookup.

ROT023 actually fetched and checked the entire original author thermo 1000-row Git blob in connected GitHub; its 16 resulting numerical ratios are available in source-curated data, SHA256 2861cfdb77a40447cee75912245c33545065df168842cac6e30a61e5de6f6171. The 16 source-attested g_s(T) fixture from original author 1000-row source via MT15 ROT022 has SHA256 a908ac6e0263b0ef7f9bb71a9b884cf515984437ad7a28a074353ff22c3e1008. THE FULL ORIGINAL AUTHOR THERMO 1000-ROW TABLE IS NOT INCLUDED in this ROT024 user-local replay ZIP, and no local full 1000-row reintegration is claimed; original connected-GitHub source results are used as separately audited FIXTURES.

This ROT024 independently rereads original actual native CSV values a_i, T_i, native time t_i at those exact 16 original anchor indices and source-attested g_s(T_i), and recomputes the ACTUAL native proxy S_native(i)/S_native(8545) with 68-decimal-digit Decimal:

    S_native_ratio(i) = (a_i/a_8545)^3 (T_i/T_8545)^3 [g_s(T_i)/g_s(T_8545)].

Let S_LUT(i) be the separately authenticated original AUTHOR-v2 inverse-lookup source-model prediction from ROT023 at the SAME native T_i. Define the dimensionless discrepancy

    E_i = ln[S_native_ratio(i) / S_LUT(i)].

The signed interval residual

    deltaE_(i,j) = E_j - E_i
     = ln[(a_j/a_i)^3 (T_j/T_i)^3 g_s(T_j)/g_s(T_i)]
       - ln[S_LUT(j)/S_LUT(i)]

does NOT depend on arbitrary first-zero source normalization. It measures SOURCE-MODEL-VERSUS-SAVED-TRAJECTORY discrepancy across an observed native anchor pair, not a realized ODE step error or physically measured entropy production. Its telescoping identity holds exactly over anchor chains. A separate E_i^ideal versus source IDEAL inversion serves as a negative comparison; the same dominant interval is found.

## 3. ACTUAL original native 10D source result — temporal localization

All 16 original source anchors are row indices 8545, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900 and 10000. Exactly 15 adjacent ANCHOR windows; 1000-row entropy integral was separately already computed (not rerun offline here). Direct original native source data at the dominant window:

- Original saved row 9200: T=0.146213868999653 MeV, time=48.8300292803444 sec;
- Original saved row 9300: T=0.108068423790714 MeV, time=101.827464911178 sec.
- Reference-independent **signed** deltaE_9200_to_9300 = **-0.00163106739302023160674**.
- Full first-zero 8545 to final10000 E_final-E_first = **-0.00157682430204089327420**.
- Thus this ONE original source anchor interval accounts for **103.4400212445% of the final SIGNED log discrepancy**. This is possible because other intervals have opposing contributions and partly cancel. Do NOT interpret the 103.44% as a physically impossible fraction of entropy production.

The original inverse-lookup-versus-ideal source model contribution on that same window is only

    delta ln(S_LUT/S_ideal) = -0.0000176242750598773097230,

which is **1.08053628779% of the absolute local deltaE**. Thus the local ~0.1631%-log change is NOT an effect explained by original rho-to-T LUT source-model correction alone. The absolute effect is ~92.55 times larger than the LUT-only source-model shift. This is a different, interval-specific negative localization control beyond ROT023's global ~0.145% fraction.

Additional SOURCE-SIGNED interval witness for model nonuniformity:
- source rows9100→9200 (T .1992212→.1462139 MeV): deltaE=**+0.000555176870400527689893**;
- original rows9200→9300: deltaE=**-0.00163106739302023160674**;
- rows9300→9400 (T .1080684→.0786847 MeV): deltaE=**-0.000247421285117489856556**.

The residual versus source-model DOES NOT accumulate monotonically with a single sign across all windows. Total positive signed log increments +0.000780519448181055627409, total negative signed log increments -0.00235734375022194890161; total absolute interval log variation 0.00313786319840300452902, **1.98998911568 times** absolute final signed log residual. Source discrepancy crosses zero in the ORIGINAL 16 anchor pairs 8700→8800, 8800→8900, 9100→9200, and 9200→9300. These are sample-level source-model comparisons, not an assertion that the true continuous original native solution has four exact physically significant zeros.

The previous ROT023 last native S_com versus original-LUT source-model relative ratio remains -0.00157558176777302427 (~-0.15756%), while the *logarithmic* gap analyzed here is -0.00157682430204, a different mathematically correct scale. The local band ~0.108–0.146 MeV overlaps a thermally changing source epoch; NO inference about physical nucleosynthesis, baryon beta contour, or Yp follows solely from these logarithmic differences.

## 4. Independent real-source executions and falsifiers

Actually executed independent Python STDLib producer mt15_rot024_anchor_residual_audit.py SHA256 03656d7237a8c019411594b977b76134f4a84b5970ec84e2a7b3f0842aa42cfa on the **UNCHANGED real owner native ZIP**, original inner 16 SHA manifest, and original ROT022/023 separately GitHub-authenticated source fixtures. It parses ALL actual 1456 recorded postev source rows from original 10000-row owner CSV, verifies source indices/floor-event nPBH_zero, recomputes 16 native source proxy S using **68-digit Decimal** directly from printed CSV values and original source-derived fixture, reproduces previous source native S within 2e-12 absolute, and calculates all 15 signed interval differences. It verifies exact Decimal anchor chain telescoping and the independent first-normalization-free 9200→9300 expression.

Independent verifier mt15_rot024_verify.py SHA256 280be0c0af9b00ebe320bad2fa974b74908802da73cf38ae62ee2ad515fce1d9 redoes the full anchor source proxy and L/ideal residual via a SEPARATE binary64 log path; all 16 source anchor and 15 interval comparisons PASS, same dominant original saved interval 9200→9300 for both original ideal and LUT predictions. Source-independent 3500 seeded random anchor-pair telescoping falsifier PASS. THREE input tampering negative tests (original owner native ZIP, source g_s fixture, ROT023 source-LUT source-model 16-ratio fixture) each REJECT before science. No arbitrary-smooth interpolation claim or full Julia solver error certificate.

Standalone LOCAL ZIP source-limited replay mt15_rot024_wuxu_native_EOS_residual_window_localization_20261114.zip, **730464 bytes**, SHA256 **d233c5c580b19c1a8bcbbaff82172af729b651c96faf0fdb89c20f63608d22ee**. Contains original unmodified Mech-S9 full native provider ZIP, original full source 10000 CSV inside it, both original source-typed g_s/ODE 16-anchor fixtures, actual producer/verifier Python and output JSON, README, SHA256 manifest. ZIP CRC PASS, payload 7/7 SHA256 PASS, nested provider original 16/16 SHA256 PASS. Extract to a NEW EMPTY temp directory; run python -I producer followed by python -I verifier: FULL source-native anchor output JSON BYTE IDENTICAL and 3500 random identities plus 3 corruption controls PASS. This local package is **NOT** source-complete for original 1000-row g functions, so its original source physical-model step is the earlier authentic GitHub fixture, not a fresh full 1000-row offline calculation. Local ZIP user conversation only; NO claim public Git or BW uploaded those 730464 binary bytes.

## 5. Scientific ceiling and no owner action

This is a **falsification of a uniform/one-sign residual-drift narrative**, and source-specific localization of the earlier 0.158% model-native mismatch into an original recorded T∈[.108,.146] MeV window. It DOES NOT falsify correctness of the original Wu–Xu ODE exact mathematical flow, identify Julia solver error as its source, or prove the true native 10D has a physical entropy uncertainty of ~0.16%. Residual can reflect solver convergence, dense output, native thermo inverse implementation, source equation conventions, numerical event handling or model-code mismatch; no causal attribution without owner native tolerance/frozen observable re-runs.

The original native j22 input remains slightly outside Wu–Xu historical beta scan upper range; physical hadron-source E4 below original first mass-grid node M=1e9g remains uncalibrated. MT15 has NOT run Julia, changed B1/30-day owner budget, created a new simulation task, signed a source physical claim, issued CANON or EXEC_SIGN, or claimed independent I3 or BW ACK.

FINAL VERDICT: ORIGINAL_NATIVE_SOURCE_ANCHOR_REPLAY_PASS / ORIGINAL_SOURCE_LUT_RESIDUAL_LOCALIZATION_PASS / LARGEST_WINDOW_9200_9300_103p44PCT_OF_FINAL_SIGNED_GAP / LUT_ALONE_EXPLANATION_FAIL / TRUE_SOLVER_CAUSE_HOLD / NO_PHYSICAL_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
