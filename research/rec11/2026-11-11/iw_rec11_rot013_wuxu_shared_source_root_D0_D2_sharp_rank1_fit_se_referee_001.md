---
artifact_id: IW_REC11_ROT013_WUXU_SHARED_BASE_D0_D2_SHARP_FIT_SE_RANK1_REFEREE_001_20261111
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-11
exposure: PUBLIC_SAFE
scope: I1_NONBLIND_INDEPENDENT_EXACT_FRACTION_ROOT_GEOMETRY
source_blob: 1df29aff025755f9042628ec85752178b991d398
claim_ceiling: HYPOTHETICAL_PER_ROOT_FIT_SE_BOX_ONLY / NO_CONFIDENCE / NO_JULIA_RERUN / NO_PHYSICAL_E4 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_status: UNVERIFIED
---

# REC11 ROT013: globally sharp rank-one breakdown with shared source roots and both D0/D2 controls

## Priority and factual corrections

**BADACZ REVIEW050 FIRST** ran the Wu–Xu v2 original author-code band-response model and published the original seven-point root fits. **MECH-S8 ROT012 FIRST** exhibited a rank-one response within independent derived-coefficient fit-SE boxes. **MECH-S8 ROT013 FIRST** supplied a stronger source-root-compatible witness with one shared base and *both* D0/D2 fitted roots, max normalized root displacement **0.860765078**. **MECH-S8 ROT014 FIRST** found that one shared vertical calibration offset per mass cannot reproduce the needed D0/D2 source-root equivalence under its own common-mode constraint. REC11 independently refines ROT013 to its **globally sharp** threshold, not claiming source experiment firstness or physics novelty.

**Currentness correction:** BADACZ clarified that the *simultaneous* native C×2+D×2 original Julia run **already exists** in REVIEW054 (8 Nov), with source-own-root change about **−0.1360 dex** at j22. REC11 ROT011's generic HOLD_NATIVE_DOUBLE_BAND was outdated. That run tests joint forward response, not separable C/D source inference; it does not certify E4 differential hadron spectra.

## Exact data and contract

Direct GitHub source pin: public `research/badacz/2026-11-08/data/kernel_analysis.json` commit `11eeb1c37c21f19b2510e3bba5ae50169cbd5d79` blob `1df29aff025755f9042628ec85752178b991d398`. Precisely 16 source root / nominal regression-fit-SE entries in `configs` for j=22,28,34,62 and kinds `base,C2,D2,D0`. Unrelated non-strict JSON Infinity tokens are not used.

For each j, allow independent coordinate root changes of at most `rho` times **each root's own nominal regression-fit SE**. Require ONE perturbed baseline b_j shared by C2,D2,D0 and one **GLOBAL** q>0 with

`sC_j=10^(b_j-c_j)-1>0;`
`sD2_j=10^(b_j-d2_j)-1;`
`sD0_j=1-10^(b_j-d0_j);`
`0<sD2_j=sD0_j=q sC_j<1.`

Thus the full 4×2 [sC,sD] coefficient matrix has exact rank one and D0, D2 are algebraically consistent.

### Sharp theorem

For fixed rho the smallest legal q at j22 is attained at

`d2'_22=d2_22+rho*eD2_22,` `d0'_22=d0_22-rho*eD0_22,` `c'_22=c_22-rho*eC_22`

with b' determined by `10^(b'-d2')+10^(b'-d0')=2`. The largest legal q at j28 is attained at the OPPOSITE three root-box endpoints, likewise with this equation. This follows from the intersection of increasing D2 and decreasing D0 response bounds, after division by the legal C response interval. Both crossing baselines are inside their original base-root budget in the certified rho bracket.

Let `R=10^(d0'-d2')`, `V=10^(d0'-c')`. At either crossing,

`q_cross=(R-1)/(2V-R-1)`.

All 4-row compatible candidates NECESSARILY require `q_min22(rho)<=q_max28(rho)`. These endpoint bounds cross at a unique threshold in the interval below; because the two remaining rows are constructively feasible at that exact crossing, the condition is also SUFFICIENT for the full 4-row problem at its first feasible rho.

**Global sharp minimum**:

`rho_* = 0.8589748790377683162468670714029743...`

**RIGOROUS rational enclosure**:

`0.85897487 < rho_* < 0.85897489`.

Proof certificate uses ONLY Python stdlib Fraction on source DECIMAL TOKENS; `ln 10=3 ln 2 + ln(5/4)` is bounded by rational atanh expansions, and every `10^x` by rational exponential Taylor polynomial of degree 42 plus a stated strict rational remainder. The j22 lower-q envelope and j28 upper-q envelope are disjoint at the lower bound and overlap at the upper bound; neither result depends on binary float or an optimizer.

For j34 use the **unchanged** b and c roots. For j62 shift both b,c by +0.4 of their respective source nominal SE. A separate Fraction interval certificate confirms that for all `q in [0.20997243,0.20997244]` these selections permit roots D0,D2 well **within rho=0.85897487**; the exact threshold q lies in that interval. Thus the first two rows control the sharp global threshold, and this is not merely an existential upper bound.

### Complete 16-root rank-one witness

At rational `rho=0.85897489` choose q as the midpoint of the two crossing q bounds. Numerically `q=0.20997243322883705624...`. Construction: at j22 and j28 take matching D2/D0 root-box endpoints and solve for the shared b and c; j34 retains original b,c and j62 shifts both by +0.4 own SE; define D0/D2 roots by exact inverse `log10` maps. All resulting normalized source root shifts satisfy their own bounds:

| j | B | C2 | D2 | D0 |
|---:|---:|---:|---:|---:|
|22|−0.073515808|−0.858974822|+0.858974890|−0.858974890|
|28|−0.564864924|+0.858974860|−0.858974890|+0.858974890|
|34|0|0|−0.257239590|−0.464776456|
|62|+0.400000000|+0.400000000|−0.472192497|−0.187515978|

Entries rounded **for display**; the generated source witnesses use exact analytical definitions and 90-digit Decimal for numerical verification. The accompanying 16-root JSON is retained in the local reproduction ZIP and not represented as a source-native physical dataset.

## Interpretation and non-transfer

This is **stronger and better typed** than:
- REC11 ROT011 independent-C/D **coefficient** fit-SE box with direct D2 rank-one threshold 0.466698741..., because 16 shared-root constraints are now imposed. These are different parameter spaces, not conflicting mathematical claims.
- MECH-S8 ROT013 source-root EXISTENCE witness with max displacement 0.860765078, because the **exact minimum** is now 0.858974879....

**Common-mode caveat**: Mech-S8 ROT014 ruled out a rank-one reconstruction under one shared additive Y_C curve shift per mass and a narrow calibration constraint. The present witness permits *differential* fitted-root shifts by configuration; the common-mode restriction is a proper subset and can reject it. A seven-point regression FIT SE is not a certified error law, confidence ellipsoid, valid correlated root covariance, or physical source spectrum uncertainty. The existence of an algebraic box witness does not establish that the Julia solver can generate it. The simultaneous native CD2 run tests a different observable and does not settle this inverse problem.

HOLD physical E4 hadron spectra, original Julia ODE certified errors, Y_P formula calibration, historical JCAP producer identity, physical PBH β, source-level time/energy distribution, BW owner adoption and any mathematical novelty/canon/EXEC transfer.

## Reproducibility

A local standalone stdlib Python reproducer independently transcribes the 16 source root/SE decimal strings; performs all Fraction exponent interval inequalities (including sufficient non-binding-row guards); performs 90-digit Decimal bisection and full 16-entry witness, writes strict deterministic JSON and stdout. **Clean ZIP extraction + isolated rerun yields byte-identical JSON AND stdout.**

Local six-member ZIP: `IW_REC11_ROT013_SHARED_ROOT_RANK1_SHARP_FIT_SE_REPRO_001_20261111.zip`, SHA256 `c602a7db2aa6de354b048f547aae3fdc3cb22476b48ea70ce544854f544973a4`; archive CRC PASS, original 4 payload SHA256 PASS, clean rerun PASS. Full local science report, exact script, results JSON, stdout, manifest and README inside. The ZIP is **not** claimed hosted in GitHub.

Sources:
- BADACZ source https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/data/kernel_analysis.json
- MECH-S8 ROT013 https://github.com/wmakiela-tech/Nash-iw-research/blob/a9422ebe0a6187b42891b02497e1f92b4a097736/research/mech-s8/2026-11-10/IW_MECH_S8_ROT013_WUXU_C_D_SHARED_BASE_D0_D2_ROOT_SE_RANKONE_FALSIFIER_001_20261110.md
- MECH-S8 ROT014 https://github.com/wmakiela-tech/Nash-iw-research/blob/a3c96d0ee732ce35e9f6393eadd088e0526e8173/research/mech-s8/2026-11-11/IW_MECH_S8_ROT014_WUXU_CURVE_SHIFT_VS_COMMON_YC_CALIBRATION_FALSIFIER_001_20261111.md
- BADACZ REVIEW054 https://github.com/wmakiela-tech/Nash-iw-research/blob/3f6769d60d095aa6de100726c719697a726a6dc9/research/badacz/2026-11-08/IW_BADACZ_WUXU_JOINT_LATE_BAND_ADDITIVITY_REVIEW_054_20261108.md

**RETURN_ID** `IW_REC11_ROT013_WUXU_SHARED_BASE_D0_D2_SHARP_FIT_SE_RANK1_REFEREE_001_20261111`.

**FINAL** `PASS_EXACT_SHARP_RANK1_SOURCE_ROOT_THRESHOLD / PASS_16_ROOT_WITNESS / PASS_FRACTION_INTERVAL_CERTIFICATE / HOLD_CORRELATED_SOURCE_CALIBRATION / NATIVE_CD2_PREVIOUSLY_DONE / E4_PHYSICAL_SOURCE_BLOCK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
