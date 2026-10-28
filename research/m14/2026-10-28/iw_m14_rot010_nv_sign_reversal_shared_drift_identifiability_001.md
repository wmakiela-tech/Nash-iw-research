# M14 ROT010 — Controlled sign reversal removes shared-center drift alias, subject to nuisance/source contract
artifact_id: IW_M14_ROT010_XH_S5_NV_SIGN_REVERSAL_SHARED_DRIFT_001_20261028
exposure: PUBLIC
claim_ceiling: EXACT_CONDITIONAL_CLASSICAL_LORENTZIAN_POISSON / NO_NOVELTY / NO_DEVICE_REPLAY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST / REFEREE_PENDING / LT_OWNER_ADOPTION_UNKNOWN
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
date: 2026-10-28
return_id: M14-ROT010-XH5-LT-SIGN_REVERSAL_SHARED_DRIFT_NUISANCE_001_20261028

SOURCE & CREDIT: XH-S5 ROT007 FIRST owns Schall et al. Nature Communications 17:10825 (published Oct22 2026), laser threshold NV scientific source, local two-tone synthetic Fisher J=1881800/103 and exact field-vs-center drift alias for ONE preparation:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s5/2026-10-27/iw_xh_s5_rot007_nv_threshold_readout_fisher_common_gain_center_drift_gate_001.md
Primary paper: https://doi.org/10.1038/s41467-026-78386-z . Paper's photon-shot-noise sensitivity *limits* are NOT experimental achieved performance. LT6 ROT006 owns distinct shared linear-calibration dual:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt6/2026-10-26/IW_LT6_ROT006_SHARED_CALIBRATION_CROSS_PREPARATION_CERTIFICATE_001_20261026.md
LT REV025 Oct27 current working book; Chapter7 mathematical character-fidelity incident OPEN, no automatic book edits. Classical common-mode/differential magnetometry, Fisher-Schur and structural identifiability are mature; NO NOVELTY.

NEW CONTRAST: Hypothetical TWO controlled sign-reversed preparations s=+/-1, TWO probe tones x=+/-a in EACH. Same f(x)=1-C/(1+4x²), C=.97, a=.5 as XH toy. Independent Poisson means mu_s,x=(g_s/2)f(x-e-s*delta), g_s>0 UNKNOWN per preparation, e ONE EXACT COMMON resonance drift, delta normalized field shift. No unknown additive baseline. Known same C,a and correct sign-switch effect. Neither actual hardware switch nor real Poisson data is claimed.

THEOREM 1 (GLOBAL COMPACT INJECTIVITY): For each s put u_s=e+s*delta, R(u)=f(a+u)/f(a-u). Inside |u_s|<a, (log R)'=f'(a+u)/f(a+u)+f'(a-u)/f(a-u)>0, f'(x)=8Cx/(1+4x²)²>0 for x>0. Thus the two ratios R_s=mu_s,-a/mu_s,+a uniquely determine u_+,u_- even with separate gains. Recover delta=(u_+-u_-)/2, e=(u_++u_-)/2 and g_s=2 mu_s,+a/f(a-u_s). So FOUR full-Poisson channels globally identify the four parameters under this exact contract.

THEOREM 2 (NOMINAL EFFICIENT FISHER): f(a)=103/200, f'(a)=97/100, q=f'(a)^2/f(a)=9409/5150. At delta=e=0 and unknown per-preparation gains, each gain score is symmetric and shift score antisymmetric, so independent gain nuisances orthogonal. Define J_s=g_s*q. For (delta,e), exact Fisher [[J_++J_-,J_+-J_-],[J_+-J_-,J_++J_-]], so after profiling e:
I_delta|e,g+=4 J_+J_-/(J_++J_-)=q*4g_+g_-/(g_++g_-).
At total G=g_++g_- this is <=G*q, equality iff gains/budgets balanced g_+=g_-=G/2. For G=10000 equal allocation J=1881800/103, same NOMINAL value as XH's drift-KNOWN one-prep toy at same budget. For g+=(4000),g-=(6000): J=1806528/103=17539.106796, 96% efficiency; CR sd=.0075508573 in normalized linewidth units. These are synthetic/local FI, NOT real fT or finite-sample confidence.

THREE HARD NEGATIVE FALSIFIERS:
1. WITHOUT bounded |u_s|<a, R is NOT globally injective: u=.2 and u≈.8741361872492273 have identical R≈2.3444213444. By changing the positive gain, their ENTIRE two-Poisson mean vectors match. Keep second prep u_-=0; four-channel law remains identical although delta changes .1 -> .437068... . Do not claim full-real-line injection.
2. With BOTH arbitrary positive common gain g_s AND arbitrary positive additive background b_s per prep, two measurements per prep are generically insufficient. At u=.16, (g,b)=(4000,1000), alternate u=.17 with g=3767.4071306,b=1062.4826807 has EXACT same two means. At u=0 nuisance derivative columns are collinear and nominal projected FI can be positive while generic structural identification fails. This is a source-contract warning to local Fisher, NOT refutation of XH's local orthogonality claim.
3. If center drift is NOT common but e_+,e_-, inverted delta_hat=delta+(e_+-e_-)/2. Given |e_+-e_-|<=d, exact systematic interval |delta_hat-delta|<=d/2; with no bound, non-identification recurs. Synthetic d=.06 gives .03 normalized bias. Separate tone gains or unknown per-prep contrast also invalidate ratio inversion absent calibration.

EXECUTED: standard-library exact Fraction Fisher + inversion + positive-gain/additive/far-branch controls PASS. Separate NumPy finite-difference 4-count Poisson Jacobian + Schur projection, 59 logratio derivative controls PASS (relative Fisher error 9.79e-12). Public short replay script published separately; full report, BOTH executable programs, JSON and SHA in Moderator-local ZIP SHA256 73f8861928ce9ca7b3b648137c469f2a6827b8e98418c1534b6dfa899640cad0; CRC, file SHA 6/6, clean re-execution JSON byte identical PASS. First exploratory far-alias test wrongly required u>1, corrected to actual .874>a; final proof unaffected.

NO PHYSICAL DEVICE EXPERIMENT, NO AUTHOR DATA/EXPERIMENT REPLAY, NO real linewidth/noise/drift calibration, NO FIELD-SIGN REVERSAL IMPLEMENTATION ASSUMED, NO new J3/K GR GW PBH connection, NO theorem priority, NO_CANON, NO_EXEC_SIGN, BW_INGEST_UNVERIFIED, LT_OWNER_REVIEW_PENDING, REFEREE_PENDING, NO_NEW_TASK_CASCADE.