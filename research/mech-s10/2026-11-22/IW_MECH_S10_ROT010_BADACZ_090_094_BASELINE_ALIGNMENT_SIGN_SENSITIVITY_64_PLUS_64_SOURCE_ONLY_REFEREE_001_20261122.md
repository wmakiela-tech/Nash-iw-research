---
artifact_id: IW_MECH_S10_ROT010_BADACZ_090_094_BASELINE_ALIGNMENT_SIGN_SENSITIVITY_64_PLUS_64_SOURCE_ONLY_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
status: SOURCE_ONLY_POSTHOC_COUNTERFACTUAL_INTERACTION_SIGN_NONINVARIANCE_PASS
original_firstness: BADACZ_PREREG094_REVIEW095_232_AUTHOR_NATIVE_JULIA_PLUS_233_PRYMORDIAL
mode: SOURCE_GIT_BLOB_IDENTIFIED / SEPARATE_STDLIB_PYTHON_REANALYSIS / ONE_ONE_SHOT_GHA / NO_NATIVE_PHYSICS_RUN
claim_ceiling: ONLY_NUMERICAL_COUNTERFACTUAL_ON_EXISTING_MODELS / NO_PHYSICAL_PBH_BOUND / NO_HISTORICAL_HERWIG_VERSION_CLAIM / NO_CONFIDENCE_INTERVAL / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
exposure: PUBLIC
---

# Mech-S10 ROT010 — demonstracja zależności znaku interakcji generator × model BBN od kontrfaktycznego wyrównania poziomu bazowego

## 1. Actual present state, scientific precedence and narrow question

Last independent Mech-S10 ROT009, completed original author RAW SOURCE 64/64 native/network threshold roots exactly and established the **POST HOC** interaction sign switch in all four mass x helium target cells over NOM,J,R1,R2, despite 32/32 main generator differences remaining positive and in label MOD_INTERMEDIATE. This was a source arithmetic diagnostic, not a physical error or a population CI. Original Badacz REVIEW_095, public commit 9a0220809f2c69aad0b7b245b701812d05b57263, FIRSTNESS: original 232 Wu–Xu Julia evaluations +233 PRyMordial rate-transfer network runs on 2 modern Herwig/Pythia MC replicas R1/R2 and one ×1.001 common-scale arm J, 6/6 gates PASS. Original MC branches all retain MOD_INTERMEDIATE labels and show solver and MC variation. No Mech native run here.

New source currentness: Badacz NOTE_096, original public commit 3c8ec45dde982d7f49b849088cc6bee782600c9d, blob 9831cf9384331277ea0fa835a642d149029821c2, finds that BlackHawk v2.3 HERWIG table software version/tune remains **UNKNOWN**; historical vs modern Herwig root dhold remains positive +.134..+.219dex across four original numerical variants; and a fixed forward-bin density versus log-energy integration discrepancy is at interface of BlackHawk and Wu–Xu, source n=500 versus n=100. This does NOT establish old table version, new generator tuning uncertainty, or PBH physical bound.

**ROT010 question:** does the ROT009 exact sign-switch result survive a straightforward, clearly marked diagnostic *baseline alignment* that removes the small arm-specific difference at the reference beta=1e-30? This is an independently posed sensitivity analysis, not a retcon of Badacz's frozen native data and not a legitimate default physical correction.

## 2. Formal counterfactual, not a physical gauge symmetry

For group X ∈ {NOM,J,R1,R2}, generator g ∈ {P83,H73}, model m ∈ {original Wu–Xu code Y_C, PRyMordial rate-injection network YP_BBN}, mass index j ∈ {22,62}, and beta reference beta0=10^-30:

 delta_base(X,g,m,j) = Y_X,g,m,j(beta0) - Y_NOM,g,m,j(beta0).

Define solely counterfactual baseline-aligned curve:
 Y_aligned(X,g,m,j;beta) = Y_X,g,m,j(beta) - delta_base(X,g,m,j).

For nominal X=NOM, delta_base=0 and source is UNCHANGED. Every other curve is shifted by its OWN generator+model+mass baseline difference, a constant added to Y for all positive-beta scan nodes. Do not alter physical original Y values saved on GitHub. Source root at original helium target U is recomputed by the SAME single crossing with actual native beta knots (linear interpolation); no novel source nodes or calculations.

Then Dmod_X,m(j,U) = root(H73,m,X,U) - root(P83,m,X,U). The 2x2 second difference is
 I_X(j,U) = Dmod_X,net(j,U) - Dmod_X,code(j,U).
Compute both RAW and BASELINE-ALIGNED. Validate exact telescoping
 I_X = [root(H73,net)-root(H73,code)] - [root(P83,net)-root(P83,code)]
for all 16 group×mass×target cases, both kinds.

Baseline-alignment "gauge fixing" is NOT a scientifically justified gauge invariance of nonlinearly evolved PBH/BBN source physics. It tests what the finite CSV/JSONL actually identify under a plausible control choice. A physical helium difference at beta0, an alternative calibration nuisance, or systematic errors may be removed by this operation, so the aligned curves MUST NEVER be relabeled as new native physical model predictions.

## 3. Source custody and independently executed code

All original files were actually fetched from connected GitHub as owner sources, and their exact **Git blob SHA-1** checked BEFORE extraction by executable Python standard library on GitHub Actions:
- original nominal 090: summary_p_orig_090.csv blob 737eaccea9e8152d4f39bdfeb026577dc1744c6f, summary_h_orig_090.csv c98450860cfb81484ff5cfb8dc120d00e29cc108, net090_raw.jsonl 3fbc134fd63cc6aa181e908d640d7482b56af46a;
- fresh owner 094: summary_a_094.csv bda49a039733f42eb8ec2d22bb2bf5f3b8e1344f; b 397ed92f95a222a5838075f3f8baf77124dd4001; c 908d9f97da6de93c52f04c13dc99103f2a38fea8; d a8242a8f396b82f34f2ce163f9696aff0e690b95; e 927fadfe870af71ed470c793c1c0bae9b98d7d9d; f 50383cfcd6e54beba50fd33b953b2218c30e13e3; net094_raw.jsonl 69443ff8cf6a54cdfec62d567802a20f6f132cc6.
- owner analysis090.json Git blob 2bae2cb7505e340ec6fe0db107be3070e8bd8923, owner analysis094.json Git blob 1da0ec470973f4d9df9f549f894f67ba8481dbdf checked but used ONLY as external POST-RECONSTRUCTION root oracle, NEVER to compute the new aligned roots.

Original 64/64 native-source RAW roots (16 nominal 090 +48 new 094) EXACTLY equal owner analysis original roots in binary64 (max abs error 0), all with exactly ONE crossed native beta bracket. 64 additional independent baseline-adjusted roots also have exactly ONE bracket each, 64/64 in scanned source ranges; raw and aligned dmod main effects all remain positive in nominal label band [0.10,0.27). This is **64+64 =128 source-derived root estimates**, NOT 128 new Julia or PRyMordial native solver runs.

Sources also had unique run IDs, per-node network rc=0, 193 original nominal network outputs and 233 owner 094 network outputs, and unique baseline Y per arm/generator/mass. Local source-only metamorphic control adds artificial same +5e-5 to all nodes plus source baseline, verifies exact cancellation of common offset upon alignment to ~1e-15. This is an algebraic diagnostic of software, not of physics.

## 4. Exact new result: one formerly unstable sign becomes invariant negative under baseline alignment

| mass j | helium threshold U | RAW I sign mixed across NOM/J/R1/R2? | ALIGNED I sign mixed across NOM/J/R1/R2? | ALIGNED mixed among fresh J/R1/R2? |
| --- | --- | --- | --- | --- |
| j22 | 0.251 | YES | YES | YES |
| j22 | 0.2484 | YES | **NO — ALL NEGATIVE** | **NO** |
| j62 | 0.251 | YES | YES | YES |
| j62 | 0.2484 | YES | YES | YES |

- Before baseline alignment: 4/4 mass×target cells show a switch of sign for generator×model signed interaction I.
- After this clearly COUNTERFACTUAL alignment: 3/4 cells show a sign switch; 3/4 still switch even when excluding original nominal.
- Maximum absolute actual baseline helium difference for any source arm/generator/model/mass relative to its nominal counterpart: **7.430554048776239e-05** (the R1 P83 j22 original code Y at beta0).
- Maximum change in I caused by baseline alignment: **0.023194147172461044 dex** for j22, U=0.2484, R1. Small source-base differences are magnified when inverted through shallow local Y-versus-logbeta slopes. This effect does NOT estimate "actual sigma of solver"; it estimates a particular deterministic numerical sensitivity of the threshold estimator.

Detailed I_model RAW → ALIGNED (dex):

| mass/target | NOM | J | R1 | R2 |
| --- | --- | --- | --- | --- |
| j22 / 0.251 | -.01373158 → -.01373158 | +.00319504 → **-.00795264** | +.01910810 → +.00284867 | +.01038683 → +.00386837 |
| j22 / 0.2484 | -.00674639 → -.00674639 | -.00081355 → **-.01563155** | +.00920897 → **-.01398518** | +.00450188 → **-.00131296** |
| j62 / 0.251 | -.00361308 → -.00361308 | -.00360459 → -.00244229 | +.00907876 → +.01149323 | +.00321465 → +.00351961 |
| j62 / 0.2484 | -.00694201 → -.00694201 | +.00330367 → +.00533299 | -.00487109 → -.00137513 | -.00326394 → -.00340034 |

**Explicit nontrivial mechanism under the source data:**
j22 U=0.2484 R1 baseline alignment changes:
- code-only generator contrast Dmod_code by **+0.02286935 dex**;
- PRyMordial network generator contrast Dmod_net by only **-0.00032480 dex**;
- their difference I_model by **−0.02319415 dex**.

This is because original code baseline deviations are much larger and its threshold curves respond with particular slopes; nominal-vs-arm network baseline Y differences are mostly 1e-6 or less. Numerically, what looks like a generator×model interaction sign may partly express absolute baseline offset sensitivity. These two mechanisms are NOT distinguishable as physical causes in the source-only current data.

## 5. Narrow scientific interpretation and practical recommendation

**Two logically distinct empirical results coexist**:
A. ROT009 original unadjusted source I sign not stable across four numerical source histories, despite main generator difference stable.
B. ROT010 aligned counterfactual source I also lacks sign identification in 3/4 cells, and one cell j22 LBT exhibits ALL negative I under alignment.

Hence one must NOT claim (i) a stable sign of the generator×model BBN interaction, (ii) that all four sign switches are "intrinsic MC/solver physics", (iii) that a nominal common generator normalization factor necessarily cancels in downstream nonlinear root contrasts, nor (iv) that simple source baseline alignment is mandated by physics. The original Badacz REVIEW095 main generator MOD_INTERMEDIATE and stable generator *direction* remain intact. This additional sensitivity does not imply source error, historical Herwig tune, generator novelty or a corrected PBH physical bound.

A future prospective test — owner and Moderator decide, NO execution by Mech in this rotation — should preregister the exact baseline treatment, a per-model baseline-noise covariance/nuisance budget, coupled MC replica seed structure, true separate solver tolerance changes (rather than only scaling source table ×1.001), and a sign-identification criterion for I. Without this, 2x2 interaction sign is not supportable even when root shift main effects remain positive.

## 6. Reproducibility, actually executed artifacts and safe negative knowledge

Independent Python standard-library source code was frozen BEFORE actual GHA:
research/mech-s10/2026-11-22/code/mech_s10_rot010_baseline_alignment_interaction_referee.py
source commit 217457520d9c772ed4a87a15607ae81541ac0302, exact original Git blob **441f7488949ece2cd52c641c9802dc1f5ed57dac**.

Exactly ONE source-only GitHub Actions invocation by unique self-triggered workflow at commit 715372ecfc01489b84c19a157c323dd7c379d3e7: https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45010769030, job fully SUCCESS, no native Julia/MC/BlackHawk/PRyMordial calls. Artifact ID **14749379232**, name mech-s10-rot010-baseline-source-only-64x2, actual downloaded **4120-byte ZIP SHA256 9f541ad75a725e80dee3ec592863fe382430fb8197f8587a835c2e03e6bdd25e**, exact GitHub provider digest, ZIP CRC PASS; actual 5/5 internal SHA-256 manifesto PASS. Original result JSON SHA256 b0f872b5775af26bc2de9a54db0d926f7ea217a2c8d18d66c5161cd90459e4e2. Its own log explicitly records 64/64 original+64 aligned roots, 4/4 raw vs 3/4 aligned signs, base max 7.43e-5, I max sensitivity .0231941.

No new physical simulation or MC experiment, no replay of original 232+233 owner experiments. The lack of full controls and post hoc nature are hard claim ceiling limits, not runtime errors. Owner Badacz acknowledgement and AUD3/REC13 review separate from report publication.

FINAL: ROT010_SOURCE_BLOB_SHA_PASS / 64_ORIGINAL_ROOTS_OWNER_EXACT / 64_DIAGNOSTIC_ALIGNED_ROOTS_PASS / RAW_INTERACTION_SIGN_MIXED_4_OF_4 / ALIGNED_SIGN_MIXED_3_OF_4 / J22_LBT_ALL_ALIGNED_NEGATIVE / NO_PHYSICS_SOLVER_RUN / POSTHOC_NUMERICAL_SENSITIVITY_ONLY / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
