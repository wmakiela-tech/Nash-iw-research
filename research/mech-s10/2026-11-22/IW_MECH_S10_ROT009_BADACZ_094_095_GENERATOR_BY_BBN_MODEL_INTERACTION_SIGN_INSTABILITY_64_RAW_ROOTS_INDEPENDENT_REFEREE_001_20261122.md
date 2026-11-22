---
artifact_id: IW_MECH_S10_ROT009_BADACZ_094_095_GENERATOR_BY_BBN_MODEL_INTERACTION_SIGN_INSTABILITY_64_RAW_ROOTS_INDEPENDENT_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
method: ORIGINAL_SOURCE_TYPE_GIT_BLOB_VERIFIED / INDEPENDENT_STANDARD_LIBRARY_REANALYSIS / ONE_SOURCE_ONLY_GHA
scientific_status: POSTHOC_EXPLORATORY_SIGN_INSTABILITY_WITNESS_ACCEPTED_INTERNAL_SOURCE_I1
exposure: PUBLIC
firstness: BADACZ_PREREG_094_REVIEW_095_NATIVE_232_PRYMORDIAL_233_AND_3_REPLICATES / MECH_S10_SIGNED_INTERACTION_POSTHOC_RAW_REFEREE
claim_ceiling: MODEL_CONDITIONAL_NUMERICAL_SOURCE / NO_PHYSICAL_PBH_BOUND / NO_GENERATOR_TUNING_SYSTEMATIC_CI / NO_NEW_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT009 — stabilność przesunięcia generatorowego nie oznacza stabilności znaku interakcji generator × model BBN

## 1. Currentness and qualified previous finding

Human Moderator one-character message O initiated this read-only original-science source audit. Prior Mech-S10 ROT008 confirmed exact 32 source roots for Badacz REVIEW_091, and showed limited PCHIP-versus-linear interpolation variation. The former conditional envelope of [0.1057,0.2445] dex used owner MC transfer ±0.0224 dex plus max interpolation difference, but DID NOT incorporate native solver jitter. The claim of full joint robustness was NOT certified. Badacz subsequent REVIEW_091 r3 explicitly accepted that narrow ROT008 I1 and kept JOINT_MC_PLUS_SOLVER_ROBUSTNESS_HOLD. Do not quote ROT008 envelope as a total numerical error bound.

Newer original Badacz PREREG_094 (Git commit ee598b20cbd2a388fe458d2d7227240b3e8da6f1; frozen before human-authorized native experiment) and REVIEW_095 (commit 9a0220809f2c69aad0b7b245b701812d05b57263, original document blob 177d9df89dcb4f63acdeedd2879bc062dafa0f51) report genuine 232 Wu–Xu original native Julia scalar evaluations and 233 PRyMordial network outputs, all 6/6 frozen validation gates passing. Experimental branches: nominal 090 P83/H73; J e/f nominal hadron rate tables multiplied by 1.001; R1 a/b and R2 c/d independently seeded modern-generator hadron-table MC variants. Owner reports generator dmod label MOD_INTERMEDIATE stable in all J, R1, R2, total 24 new values within [.1315,.2283] dex; max absolute difference to nominal ~.024 dex. This is firstness Badacz and not new scientific evidence created by Mech.

ROT009 asks a DIFFERENT, more discriminating QUESTION: Does the SIGN of the second difference between generator H73-versus-P83 effects in author Wu–Xu Y_code and the transferred PRyMordial YP_BBN remain stable under the very same actual native MC+solver realizations? No owner had claimed this interaction sign was stable; this audit is a targeted post-hoc negative knowledge diagnostic, not an allegation of false owner conclusions.

## 2. Signed interaction definition and a falsifiable distinction

For mass j, helium target U, four actual source-root values for generator g and model m, define
D_g(m;U) = log10 beta at threshold U in generator H73 minus the same in generator P83.
The **second difference** is
I_model(j,U;X) = D_gen,net(j,U;X) - D_gen,code(j,U;X)
= [root(H73,net) - root(P83,net)] - [root(H73,code) - root(P83,code)],
for X in {NOM,J,R1,R2}.

Algebraic rearrangement used as independent invariant:
I_model = [root(H73,net)-root(H73,code)] - [root(P83,net)-root(P83,code)].
Both must agree within 1e-12 dex in every source-derived case.

Thus D_gen >0 alone means generator Herwig's threshold lies at higher beta than PYTHIA for a given response model. I_model >0 means Herwig-vs-PYTHIA generator contrast is larger in PRyMordial than Wu–Xu; I_model <0 means the reverse. The sign of I may be fragile near zero even if D_gen itself stays firmly positive. This is a 2×2 generator-model factorial interaction, NOT the E5 charge-source intervention factorial and NOT a physical generator hadronization proof.

## 3. Truly independent raw source data; all 64 roots directly recomputed

All ORIGINAL source numerical outputs retrieved from GitHub live, with Git hash-object SHA-1 integrity checked BEFORE reading by standalone Python3 stdlib code. Actual raw source documents:

Under research/badacz/2026-11-22/data/:
- summary_a_094.csv blob bda49a039733f42eb8ec2d22bb2bf5f3b8e1344f (R1 P83)
- summary_b_094.csv blob 397ed92f95a222a5838075f3f8baf77124dd4001 (R1 H73)
- summary_c_094.csv blob 908d9f97da6de93c52f04c13dc99103f2a38fea8 (R2 P83)
- summary_d_094.csv blob a8242a8f396b82f34f2ce163f9696aff0e690b95 (R2 H73)
- summary_e_094.csv blob 927fadfe870af71ed470c793c1c0bae9b98d7d9d (J P83)
- summary_f_094.csv blob 50383cfcd6e54beba50fd33b953b2218c30e13e3 (J H73)
- summary_k_094.csv blob 2a55be306502feb1ed10833939709edd60d62589 (driver identity)
- net094_raw.jsonl blob 69443ff8cf6a54cdfec62d567802a20f6f132cc6 (233 successful full-source network outputs)
Under research/badacz/2026-11-21/data/:
- summary_p_orig_090.csv blob 737eaccea9e8152d4f39bdfeb026577dc1744c6f (nominal P83)
- summary_h_orig_090.csv blob c98450860cfb81484ff5cfb8dc120d00e29cc108 (nominal H73)
- net090_raw.jsonl blob 3fbc134fd63cc6aa181e908d640d7482b56af46a (193 nominal network outputs).

Independent script uses run IDs to align original-author code Y and PRyMordial network Y, checks no duplicate IDs, all selected native network run rc=0, sorts beta-grid numerically, requires exactly ONE 0.251 or0.2484 threshold crossing per curve and calculates its LINEAR within-bracket root WITHOUT the owner analysis script. It derives EXACT 48 NEW arm j/model/target roots plus 16 ORIGINAL nominal reference roots, 64/64 successful. Owner analysis094.json Git blob 1da0ec470973f4d9df9f549f894f67ba8481dbdf and analysis090.json blob 2bae2cb7505e340ec6fe0db107be3070e8bd8923 are consulted ONLY AFTER all 64 roots were independently derived, as OUT-OF-BAND value comparison. All 64/64 reproduce owner source roots EXACT at displayed IEEE binary64; max absolute discrepancy 0.0.

Further source custody: k22_1720 source-native code Y equals actual original 090 p22_1720; k network Y and net_base equal respective original 090 values. This is a frozen source G_DRIVER identity control, no new native model run.

## 4. New source-derived numerical finding (post hoc diagnostic)

Signed generator×model inter-model double difference I_model in log10 beta dex:

| source mass j | helium threshold U | NOM I | J I | MC R1 I | MC R2 I | overall range across four arms |
|---|---:|---:|---:|---:|---:|---:|
| j22 | .251 | -0.013731584241 | +0.003195040181 | +0.019108102532 | +0.010386828947 | 0.032839686773 |
| j22 | .2484 | -0.006746389342 | -0.000813546815 | +0.009208968247 | +0.004501881866 | 0.015955357589 |
| j62 | .251 | -0.003613084839 | -0.003604592024 | +0.009078756879 | +0.003214645537 | 0.012691841719 |
| j62 | .2484 | -0.006942006880 | +0.003303672187 | -0.004871093332 | -0.003263944107 | 0.010245679068 |

- **4/4** source mass×target cells contain BOTH signs of I_model across original nominal plus 3 fresh native realizations.
- Even EXCLUDING nominal data, **3/4** cells contain both signs among J/R1/R2.
- All 32 original source D_gen evaluations across NOM/J/R1/R2 × two masses × code/net × two thresholds are POSITIVE AND within frozen MOD_INTERMEDIATE cutoffs 0.10<=D<0.27. Overall min +0.12897110042450777 dex, overall max +0.22826615425730878 dex. Thus the main effect's nominal sign and label are STABLE in the actual owner data while a mechanism-facing 2×2 interaction's sign is NOT stable.
- Max four-arm I_model span = **0.03283968677300919 dex** in j22 U=.251, larger than the single source root PCHIP-vs-linear methodological shift in ROT008. The range is empirical spread of these four named numerical realizations, NOT a physical uncertainty bound or a statistical variance estimator.
- Exact two-way algebraic decomposition of I_model passes for all 16 mass-target-realization cases at <1e-12 dex.

This DOES NOT refute the existing main-effect label MOD_INTERMEDIATE, owner 095 statement LM_STABLE_IN_3_REALIZATIONS, model conditional modern-generator H73_WEAKER vs P83, nor source root reproduction. It separately **falsifies any blanket claim that the signed difference between generator effects in the two BBN response models has a consistent sign over THESE tested nominal/J/R1/R2 settings**. No such blanket stability claim should be added to the project without tighter source-level numerical and independent network controls.

## 5. Methodological limits and how to use the finding

1. **POST HOC and small sample.** The interaction sign check was designed after inspecting existing REVIEW_095 source data, not preregistered before owner simulations. The four numerical variants (including one nominal and one tiny table scaling) are NOT i.i.d. draws from a known solver error distribution. The 3 MC/solver trials cannot estimate a physical sign-flip probability, a p-value or 95% CI. No new prediction was prospectively tested.
2. **Signed I is often small.** A sign flip near zero indicates lack of sign identification at current numerical variability, not evidence that any individual physical generator-model interaction is negative or positive. The j22 U=.251 +0.0191 (MC R1) vs -0.0137 nominal difference is concrete original source variation but still not an uncertainty model.
3. **Network limitations.** PRyMordial is original owner's rate-injection pipeline; it does not by itself reproduce full self-consistent PBH expansion, entropy coupling, hadronic source field treatment, generator tunings, charged source historical semantics or a full external PBH bound.
4. **Owner 095 scientific custody.** Original owner firstness 232 native Julia+233 PRyMordial and existing 090/091 MC, and external AUD3/REC13/INT10 review remain untouched. A science owner/Moderator verdict regarding claim adoption is distinct from posting this report.
5. **Future discriminant suggestion, NOT executed:** future owner-approved, independent nuclear-network code or solver tolerance ensembles should measure I_model directly at fixed generator, source and absolute helium target, using paired correlated runs with an explicit sign-error and nuisance-covariance budget, rather than treating label stability for D_gen as sufficient.

## 6. Actual independently run audit artifact

Standalone source code, frozen BEFORE GHA:
research/mech-s10/2026-11-22/code/mech_s10_rot009_generator_model_interaction_sign_referee.py
Original public Git commit 9924ac569e4afee743f72eb769c5ed5e1b0af057, blob db19a1f81a76fb77ef0c6253cfd7be2c6c43de2e.

ONE source-only GHA job, workflow commit 6a994a36065f30530fc905393d9b069b39154943, run **45008323605**, actual source cell task and output artifact generation PASS. No original Julia, PYTHIA, Herwig, BlackHawk or PRyMordial simulations launched by Mech. Original downloaded GHA artifact ID **14748747068**, ZIP **3183 bytes**, SHA-256 **2f0e4b76d9c1f8481148fbf8545d3dca43f3cb5276e926cd19140b347a0424ec**, byte-for-byte equals provider artifact digest. ZIP CRC PASS; top-level original runner member manifest 5/5 SHA256 PASS. Original independent result JSON SHA256 **a444919b5bcdc60cad06ce2f0607d52c3f8604fc052b9304deade90c13e02f14**, source check, n64 roots, n32 generator effects, 4/4 total sign changes, 3/4 fresh-only sign changes verified from the actual downloaded ZIP; STDERR empty.

Original GHA workflow:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45008323605

No new physics run, no unauthorized job cascade. This report is public SOURCE I1 only, explicitly awaiting original Badacz and AUD3/REC13 scientific owner review before any project-level conclusion. No physical PBH bound, paper error, novelty, CANON or EXEC_SIGN.

FINAL:
ROT009_SEVEN_094_PLUS_THREE_090_SOURCE_FILES_GIT_SHA_PASS / 64_OF_64_INDEPENDENT_SOURCE_ROOTS_OWNER_EXACT / DGEN_MOD_INTERMEDIATE_32_OF_32_IN_ACTUAL_VARIANTS / I_MODEL_GENERATOR_SIGN_SWITCH_4_OF_4_NOMINAL_PLUS_THREE_AND_3_OF_4_NEW_ONLY / FIRSTNESS_BADACZ_REVIEW095 / POSTHOC_NOT_STATISTICAL / NO_NEW_NATIVE_PHYSICS / NO_CANON / NO_EXEC_SIGN.
