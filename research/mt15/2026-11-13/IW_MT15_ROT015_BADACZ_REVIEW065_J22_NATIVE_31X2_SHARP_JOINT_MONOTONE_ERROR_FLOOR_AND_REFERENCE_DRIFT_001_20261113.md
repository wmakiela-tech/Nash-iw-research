---
artifact_id: IW_MT15_ROT015_BADACZ_REVIEW065_J22_NATIVE_31X2_SHARP_JOINT_MONOTONE_ERROR_FLOOR_AND_REFERENCE_DRIFT_001_20261113
created_at: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: INDEPENDENT_ORIGINAL_NATIVE_OUTPUT_CROSS_SOURCE_CLASSICAL_MATH_AUDIT
status: ORIGINAL_THREE_NATIVE_GIT_BLOB_AND_SHA256_PASS / SOURCE_31_PLUS_31_IDENTICAL_BETA_GRID / JOINT_SHARP_MONOTONE_FLOOR_PASS / SHAPLEY_PASS / INDEPENDENT_DECIMAL50_PASS / CLEAN_OFFLINE_REPLAY_PASS
claim_ceiling: NO_NATIVE_JULIA_NEW_RUN / NO_SOLVER_UNCERTAINTY_CERTIFICATE / NO_PHYSICAL_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT015 — Independent exact sample-level stability audit of Badacz REVIEW065

## Original science and firstness

WU–XU ORIGINAL physics: JCAP 02 (2026) 063, frozen original author code-v2 public repository Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d. This audit is only of the subsequent original BADACZ NATIVE JULIA OUTPUTS; no original author physical code was run by MT15.

BADACZ FIRST original native REVIEW053, PREREG064 and corrective REVIEW065 (2026-11-13) public report at owner commit a19619dd6b7549931b8f2465e3c3f5bc3127b99e, Git blob c7cb1262d94cc0fd5ce925b4188c6af1e085e291. The original j22 V2 root-error detection belongs to Mech-S9 GPT native L2, KN13 ROT022 and the subsequent owner self-falsification REVIEW065. EKS1 ROT010 also independently examined native-output jaggedness. The firstness of recognizing REVIEW053 root bias and its correction belongs to THEM, not MT15.

ACTUALLY RECOVERED THREE ORIGINAL OWNER CSV FILES (byte identical, SHA1 Git blobs and owner manifest SHA256 independently verified before use):
- research/badacz/2026-11-13/data/yp064_default.csv, 3807 bytes, Git blob 38cdbe2091ef84f35b80f1a96f5506db6f47a3ee;
- research/badacz/2026-11-13/data/yp064_tol_p1.csv, 3220 bytes, Git blob ade202a0e091361b56ecbfc7e563f4247634445e;
- research/badacz/2026-11-13/data/yp064_tol_p2.csv, 2128 bytes, Git blob 98ad01514d4370c654d22fd68d1652813f536eef.
These are original native Julia result CSVs, NOT solver input source generators or independent native execution. The dense reltol1e-4 rows are the interleaved d22t_a 16 rows and d22t_b 15 rows; the DEFAULT d22d has 31 rows. Thus the TWO 31-row dense curves share EXACTLY THE SAME 31 b=log10(beta) coordinates from -17.40 to -16.80 at step 0.02. The nine coarse g22t records remain owner historical context, not used as surrogate dense data.

## Source outputs and sampled sign crossings

Original observable definitions: V0=Ycode_native-.251, V1=2X(T1)-.251, V2=2[X(T0)-X0s]-.006; each X0s from its own original native file SBBN header.
Original DEFAULT j22 X0s=.109037947009; reltol1e-4 j22 X0s=.109069431550, native offset ΔX0s=.000031484541.

Exactly ONE observed negative-to-positive adjacent source node crossing in each of the six series:
- V0 default [-17.22,-17.20], tol [-17.22,-17.20];
- V1 default [-17.14,-17.12], tol [-17.12,-17.10];
- V2 default [-17.00,-16.98], tol [-16.96,-16.94].
Negative native step increments across all 30 intervals: default V0/V1/V2 = 3/1/3 and tol V0/V1/V2 = 4/0/4. A single SAMPLED crossing is not a theorem that the full continuous solver function has a unique root; neither source dataset is strictly monotone as sampled.

## Source-controlled exact SHARP classical two-output monotonicity theorem

For two sequences a_i,b_i measured at the SAME ordered n nodes, ask for a SINGLE latent nondecreasing sequence z_i with absolute errors |z_i-a_i|<=eps and |z_i-b_i|<=eps for every i. Let H_i=max(a_i,b_i), L_i=min(a_i,b_i). The exact sharp minimum common error is:

  eps_joint = (1/2) max_{1<=i<=j<=n} (H_i-L_j)_+.

NECESSITY: z_i>=H_i-eps, z_j<=L_j+eps, and z_i<=z_j for each i<=j imply 2eps>=H_i-L_j. SUFFICIENCY: the explicit construction z_j=max_{i<=j}(H_i-eps) is nondecreasing and lies in both observation error intervals at every j exactly when eps>=eps_joint. Piecewise linear continuous interpolation of z_j is also nondecreasing. This is classical isotonic feasibility, not a new NASH mathematical theorem.

Actually calculated from the SIX ORIGINAL paired 31-point observable arrays:

  variant     epsmin(DEFAULT alone)    epsmin(TOL alone)       epsmin(JOINT latent monotone)
  V0          0.000030485796724        0.000015240250931      0.000141256495308
  V1          0.000000578561054        0.000000000000000      0.000128865421316
  V2          0.000024039169229        0.000012008688013      0.000142817585218

For V2 the largest exact same-node discrepancy is 0.000285635170436 at b=-16.90. Half of this is already the SHARP eps_joint (the worst pair of nodes happens to have i=j). The same holds for V0 at b=-16.90 and V1 at b=-17.06. An explicit latent monotone witness was constructed and numerically verified for each variant, establishing sufficiency, not just a lower bound.

INTERPRETATION: If each native output were claimed within a UNIFORM ordinate error <=1e-4 of one same monotone latent curve, the two actually observed outputs would contradict that claim at identical b nodes. This does NOT falsify a Julia reltol=1e-4 setting, since reltol is NOT an a priori absolute error bound on Y or V0/V1/V2. Nor is eps_joint a measured solver error or physical uncertainty.

Conditional root outer regions IF a true underlying response curve is globally nondecreasing AND both observations are within genuine supnorm error eps_joint:
 V0 [-17.24,-17.18] dex, V1 [-17.16,-17.10] dex, V2 [-17.02,-16.96] dex (V2 width .06 dex).
Derived from last definitely negative and first definitely positive node under errors; these are exterior CONDITIONAL localizations, NOT certified ODE intervals, 95% confidence intervals, or unique-root claims.

## New independent 2x2 reference-swap exact arithmetic

V2 depends on TWO source choices: native curve X(T0;b) and native background calibration X0s. Holding the method of FIRST negative-to-positive bracketing and LINEAR interpolation fixed, recompute all four source-typed counterfactual roots:

  native curve / SBBN ref           DEFAULT X0s              reltol1e-4 X0s
  DEFAULT native curve              -16.990591698945352       -16.984131220836598
  reltol1e-4 native curve           -16.971117356023294       -16.958503633964465

Total tolerance-pair root shift = +0.0320880649808873 dex. Native data do not uniquely attribute this to curve vs calibration because the two switches INTERACT:
- calibration at default curve: +.006460478108754 dex;
- calibration at tolerance-1e-4 curve: +.012613722058829 dex;
- curve at default SBBN ref: +.019474342922058 dex;
- curve at tolerance-1e-4 SBBN ref: +.025627586872133 dex.
Interaction of orders +.006153243950075 dex (binary64 slight rounding).

An explicitly declared SYMMETRIC two-factor averaging-over-orders (Shapley bookkeeping) gives:
- curve term: +0.02255096489709566 dex;
- calibration term: +0.00953710008379165 dex;
- sum: +0.03208806498088731 dex exact by algebra.
The attribution is a transparent explanatory convention, not a uniquely identified physical/numerical error decomposition. Owner Badacz REVIEW065 did its own posthoc selected-path attribution; this does not overwrite owner figures or their j22 V2-V0 correction +0.22...+0.25 dex. Other j28/j34 V2 native dense checks remain OPEN.

## Genuine independent execution and reproducibility

- Original three exact source CSV byte sequences were obtained directly from GitHub connector and reconstituted locally via a transparent lossless 13-bit LZW transfer, then ALL THREE Git blob SHA1s and ALL THREE original owner manifest SHA256s PASS before parsing.
- ACTUALLY RUN Python stdlib source reviewer independently recomputed all 62 rows, source roots, exact sharp single and joint isotonic minima, explicit feasible monotone witnesses and four swapped-reference roots.
- SECOND independently programmed Decimal(50-digit) reviewer used original CSV DECIMAL TEXT, NOT any first reviewer binary64 roots; root/attribution numbers agreed to max ~4.854e-15 dex, and all exact sampled isotonic minima including JOINT source theorem matched.
- Additional 3000 seeded exact integer-array tests of necessity/sufficiency for classical isotonic epsilon formula PASS.
- Self-contained OFFLINE ZIP created locally: mt15_rot015_badacz_review065_source_root_stability_20261113.zip; 17566 bytes, SHA256 c0063231f94b75bcff726fc34cc41e6ce8f24596de5ee7910f3e808b1fa646f6. Ten members: original 3 byte-identical owner CSV, two independent executable Python scripts, two executed result JSON, README, SHA256 manifest covering nine other files, self-verification program.
- ZIP CRC PASS. NEW CLEAN temporary extraction: nine SHA256 manifest checks PASS, both full source programs run to byte-identical SOURCE and DECIMAL result JSON PASS, and three independent 1-byte file tampering attempts correctly REJECTED by source original Git hash locks. Verified command after ZIP extraction: python -I verify_package.py. Original ZIP itself local to this chat and NOT claimed uploaded to GitHub or BW.

## Return and claim ceiling

This confirms the Badacz owner correction is methodologically necessary and identifies an additional exact source-data discrepancy floor that must not be confused with an integrator error guarantee. Owner Mech-S9 GPT L2 8/10 prereg history remains; no new native run performed; no E4 source, PBH beta/helium physical bound or actual Wu–Xu JCAP v3 producer validation. No mathematical novelty: isotonic feasibility, two-factor Shapley attribution and linear interpolation are mature. No external I3 referee approval or BW ingestion inferred.

STOP: ORIGINAL_OWNER_3_BLOBS_BYTEPASS / 31_PLUS_31_PAIRED_SOURCE_AUDIT / SHARP_JOINT_MONOTONE_DATA_EPS_PASS / TWO_FACTOR_REFERENCE_SHAPLEY_PASS / INDEPENDENT_DECIMAL50_PASS / CLEAN_OFFLINE_ZIP_PASS / BADACZ_OWNER_FIRSTNESS_PRESERVED / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
