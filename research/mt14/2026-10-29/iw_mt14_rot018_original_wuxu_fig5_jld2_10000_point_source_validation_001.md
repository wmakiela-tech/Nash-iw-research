---
artifact_id: IW_MT14_ROT018_ORIGINAL_WUXU_FIG5_JLD2_10000_POINT_SOURCE_VALIDATION_001_20261029
created_at: 2026-10-29
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P1_FRONTB_ORIGINAL_AUTHOR_FIG5_DATA_PROVENANCE_AND_MASS_Yp_LIKELIHOOD
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: ACTUAL_FROZEN_AUTHOR_JLD2_IMPORTED_BY_EXTERNAL_HDF5 / ALL_10000_SOURCE_CHI2_CHECKED / CONDITIONAL_TARGET_RETYPE / NO_NATIVE_JULIA_REPLAY
claim_ceiling: NO_FIRST_DISCOVERY_OF_HELIUM_FORMULA_MISMATCH / NO_NOVELTY / NO_NATIVE_WUXU_JULIA10D / NO_PHYSICAL_Yp_DH_OR_PBH_BETA / NO_PUBLISHED_PAPER_BUG_VERDICT / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT018 — real Wu–Xu Fig.5 binary JLD2 source recovered and all 10,000 points checked

Date 2026-10-29. MT14 is the independent theory scientist and cross-cell scientific programme architect, distinct from M14, Mech source owner and AUD1/REC referee. MT15 packet ready but successor NOT ACTIVATED.

## External scientific FIRST, previous NASH FIRST

Wu–Xu FIRST authors' paper/code source: JCAP 02 (2026) 063, arXiv:2509.05618, original pinned Git commit d395183674cace6c9906a8911bdeb7234ba4040d. DAX-S7 FIRST detected paper/code/He mass fraction mismatch, PRF11 R20 FIRST confirmed author arXiv v3 May2026 corrected Eq 5.1, MT13 and LT5 ROT10 FIRST assimilated. MT14 ROT017 first obtained full original 2.5MB author notebook. These prior credits are controlling and not transferred to MT14. Original NASH ownership receipt:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792743983724229

## SOURCE DIRECT: actual original author binary, NOT synthetic reconstructed data

Author ORIGINAL repository file:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/scanning.jld2

- Author ORIGINAL Git binary blob SHA1: 10cc9b3f078fcadb91b5e520e75845859ca00b74, fetched base64 also through GitHub connector.
- EXACT bytes of original downloaded HDF5/JLD2: 151089.
- Direct SHA256 of original binary, independently using Wolfram FileHash after remote URLDownload: 51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786.
- REAL source HDF5 import by connected Wolfram Language kernel, NOT Julia: 100 original mass points 6e8..1e10 grams; 100 original beta 1e-20..1e-17; original Y_P_mat and chi2_mat each shape 100×100.
- Original Wu author notebook main.ipynb original Git blob 171c4a29e414860d724c817641896628f35982b0, full source inspected MT14 ROT017: cell 7 cached SBBN C=0.24500000000000022 under C(X)=2X/(1-X); cell 10 PBH magic uses same C; cell 14 READS these stored JLD2 matrices to plot heatmap and level-4 chi2 contour; old dashed overlay read from scanning_old.jld2. Author original main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6 creates Y_P_mat using C(X)=2X/(1-X) and chi2_mat=((Y_P_mat-.245)/.003)^2. Even though the source bytes are genuine and source notebook code matches their shape, exact byte identity with the JOURNAL'S FIGURE5 image or historic scan execution environment has NOT been established.

## FULL 10,000 actual original point execution results (not a fitted/synthetic grid)

For ALL 10,000 pairs (Y_P_mat,chi2_mat), independent HDF5 extraction verifies:

- ORIGINAL Y_P_mat minimum 0.24457984107485917, maximum 1.2891415044418126.
- 158 actual original source values Y_P_mat > 1. A mass fraction of helium cannot exceed unity, but the original unnormalized code ratio C(X)=2X/(1-X) can. This is a source-native semantic diagnostic consistent with FIRST DAX/PRF correction, NOT first discovery of source mismatch.
- chi2_mat minimum 4.654971782718935e−8, maximum 121136.83125533462.
- Max abs residual of the AUTHOR formula chi2=((Y_P_mat-0.245)/0.003)^2 across the whole grid = 4.3655745685100555e−11; max ratio abs_error/(1+abs(chi2)) = 8.319884148363292e−15. Source values obey original code to numerical roundoff.
- Original stored chi2>4 at 5531 points, remaining 4469 points with chi2<=4.

The above are ACTUAL original author binary arrays, not derived from a plot pixel extraction or a regenerated model, and original Git commit, binary size and SHA256 are frozen for reproduction.

## Separate counterfactual raw-target retyping diagnostic, NOT corrected BBN

Author May2026 corrected helium mass target for the SAME neutron fraction X is M(X)=2X. Author original code output C=2X/(1−X). Algebraically M=2C/(2+C). Holding the 10,000 source states and author standard-BBN C-calibration fixed, then comparing the retyped M against the SAME observed-mass 0.245±0.003 gives a mathematically well-defined but PHYSICALLY INCORRECT partial patch:

- 6131 M values BELOW .239 and 3356 ABOVE .251;
- naive retyped chi2>4 in 9487/10000 cases (old source 5531);
- confusion counts (original allowed / naive excluded)=4469; (original excluded / naive excluded)=5018; (original excluded / naive allowed)=513; (allowed in both)=0. Exactly 4982/10000 binary labels would change on this deliberately UNRECALIBRATED target map.

This proves no physical PBH exclusion can be repaired by merely relabelling Y_P_mat, swapping C to M, or replotting the same scan with the old standard reference. The old author SBBN normalization was tuned under C≈.245: at the same source neutron state M=98/449≈.21826, 8.91 nominal sigma below the mass observation, as independently derived MT14 ROT017. Physical rescanning must REESTABLISH standard BBN calibration with correct MASS fraction, self-consistent EOS, baryon conservation and source evolution and proper original observation model.

## Scientific Front B admission status and relation to other owners

Mech-S7 ROT011 FIRST ran 7D conditional source-on baryon conservation contrasts, ROT035 repaired exact moment/source claim after AUD1 finding, ROT036 investigated original extrapolation source limits. Its source/native physics task is distinct from this source DATA-READ. Wu–Xu below-1e9g hadronic injection and full native 10D Julia accepted-step dynamics are not validated or replayed here. BIV 2025 D/H with later fixed CMB eta and adjusted H(T) is another physical mechanism not resolved by this Yp/source calibration. DTC0a/TT is not physically equated with PBH. No new audit/task cascade; REC/AUD1 independent, KN12/BW custody, Moderator only EXEC.

## Reproducer

Local downloadable packet: MT14_ROT018_WuXu_Fig5_Original_Binary_10000_Point_Source_20261029.zip SHA256 f635c2dd7f37878efde24160a309a46de0ca21b0c8575e78bdcf1c8210f5f905. Includes full Polish source report, reproducible Wolfram Language real-source HDF5 URLDownload + SHA256 + 10k point assertions, independently written Python h5py/numpy reader that fetches original source and enforces both SHA256 and Git blob SHA1, verified original Wolfram results JSON, and separately executed synthetic HDF5 fixture JSON plus SHA256 manifest. ZIP CRC PASS, payload SHA256 6/6 PASS, clean unzipped PYTHON FIXTURE rerun byte-identical PASS. **Only Wolfram original-binary reader ran on original author source**; the Python HDF5 original-source mode could NOT run in offline local container, while Python synthetic fixture did. No Julia or original author program rerun. User can rerun original HDF5 source in Wolfram or Python with internet enabled and original SHA integrity checks.

STATUS: ACTUAL_AUTHOR_ORIGINAL_JLD2_10000_POINT_READ / SOURCE_STATISTIC_IDENTITY_PASS / SOURCE_MASS_FRACTION_TYPE_GAP / 4982_NAIVE_COUNTERFACTUAL_LABEL_CHANGES / ORIGINAL_JULIA_PHYSICAL_RECALIBRATION_HOLD / SOURCE_OWNER_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
