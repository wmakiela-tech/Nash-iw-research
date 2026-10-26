---
artifact_id: IW_MT14_ROT008_B_GLOBAL_NEAREST_BOUNDARY_CERTIFIED_COUNTEREXAMPLE_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P3_DTC0A_B_FIVE_MASK_PROFILED_GLOBAL_NEAREST_BOUNDARY
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_DIRECT_B_STRICT_RATIONAL_INTERVAL_COUNTEREXAMPLE / INDEPENDENT_GLS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_J3_K / NO_HISTORIC_RUNTIME_IDENTITY / NO_DELTA001_FALSIFICATION
---

# MT14 ROT008: exact B counterexample to ALL-delta nearest-boundary inference

26 October 2026. MT14 is DISTINCT FROM M14. This is a source-conditional mathematical counterexample for the exact **M13 ROT040 CHANNEL B** synthetic 5-mask host, and not a physical NASH upgrade.

## SOURCE OWNERS FIRST; TWO-SURFACE prior art

M13 ROT040 FIRST owns the original N41 direct source quartics, A/C global all-alpha/all-delta nearest-boundary certificates, B nonradial derivative sign counterexample and explicit OPEN status of B global minimizer:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md

Original source-certified B coefficient intervals FIRST M13: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json ; exact Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. MT13 owns earlier projective positive-gain nuisance geometry. Classical external host: Golub and Pereyra, SIAM Journal on Numerical Analysis 10 (1973), DOI 10.1137/0710036, variable projection; Bates and Watts JRSS B 42 (1980), DOI 10.1111/j.2517-6161.1980.tb01094.x, nonlinear model curvature. No mathematical novelty priority.

## Exact model, no source-class shift

N=41, five nested masks k=2,...,6, total voxel counts n=[50653,42875,35937,29791,24389], disjoint shell weights w=[7778,6938,6146,5402,24389]. Source M13 provides five quartic polynomials g_k(alpha), each MASK MEAN ENERGY, with rigorous coefficient intervals. Define disjoint-shell MEAN energy profiles

s_i(alpha) = (n_i*g_i(alpha) - n_(i+1)*g_(i+1)(alpha))/w_i (i=0,1,2,3); s_4(alpha)=g_4(alpha).

Source M13 iid synthetic voxel ENERGY perturbation model has nested mask mean covariance Sigma_ij/tau²=1/n_min(i,j). It is EXACTLY equivalent to diagonal W=diag(w) in shell means (not independent five RMS readouts). One UNKNOWN common POSITIVE energy gain t is profiled out. For a=s(alpha), b=s(beta),

D²(alpha,beta) = min_(t>0) sum_i w_i*(a_i-t*b_i)^2
 = ||a||_W² - <a,b>_W²/||b||_W².

Needed shell values and cross-products are positive; gain constraint does not bind. This is the exact frozen M13 ROT040 source-typed geometry, not an unspecified different observation class.

## COUNTEREXAMPLE: FAR candidate beats the ONLY legal nearest boundary

Choose rational alpha0=21/200=.105 and delta=1/10=.1, with legal alternative beta in [0,.2] satisfying |beta-alpha0|>=delta. The only legal NEAREST endpoint is beta_near=alpha0-delta=1/200=.005; the other nominal nearest endpoint alpha0+delta=.205 lies OUTSIDE [0,.2]. A strictly FAR legal beta is beta_far=0 because |0-.105|=.105>.1.

By exact rational GLS independent check, displayed only as rounded decimal values (source coefficients energies multiplied by 10^14 before evaluating D²):

- D²(.105,.005) * 10^28 = 696530.4972350348; normalized by ||s(.105)||²_W = 0.040604455790886736.
- D²(.105,0) * 10^28 = 652867.2630609168; normalized = 0.03805909436199318.

Consequently FAR beta=0 is about **6.268675147% closer in squared profiled statistical distance** than the sole nearest legal beta=.005. This DIRECTLY falsifies the general all-delta boundary minimizer assertion, without locating the true global minimizer. It is stronger/different than M13 ROT040's FIRST failed radial monotonicity test.

## SOURCE-CERTIFIED EXACT INTERVAL PROOF (not a grid claim)

Set a=s(.105), b=s(.005), c=s(0). Because all dot-product denominators are positive, D²(a,c)<D²(a,b) iff

F = (<a,c>_W)^2 * <b,b>_W - (<a,b>_W)^2 * <c,c>_W > 0.

Fetch pinned original M13 direct_B.json. Its 25 quartic coefficients each have two stored outward decimal intervals; **100 exact decimal endpoints**. A separate exact DECIMAL -> BigInt rational verification executed against the GitHub connector result for source Git blob a6f50... confirmed **ALL 100/100 original endpoints** lie inside 25 explicitly declared, conservative rational coefficient boxes

10^14*c_kj in [C_kj - 10^(-8), C_kj + 10^(-8)],

where the C_kj are NINE-decimal rational constants included verbatim in the Moderator-local standalone certifier. No actual original source interval was replaced by an unverified midpoint. Verification of source bytes and all 100 intervals is reproducible by the certifier optional --source-json parameter and correct original Git blob SHA.

Using only the Python STANDARD LIBRARY fractions.Fraction, exact OUTWARD INTERVAL arithmetic propagates those entire boxes through quartic evaluation at three rational parameters, source mask-to-shell transformation, dot products and polynomial F. The exact Fraction lower endpoint is strictly positive, printed approximately

F_lower = 6.637863577222816e15 > 0,
F_upper = 6.638720652858400e15.

Every needed cross-dot and squared norm has strictly positive exact interval lower endpoint. This constitutes a rigorous certified inequality over an entire source-enclosing coefficient interval box; simple double precision or grid search is NOT its mathematical justification.

Independently, a SECOND program with no import of the certifier reconstructs all five mask polynomial means using exact Fraction arithmetic, inverts the source covariance Sigma_ij=1/n_min(i,j) by full exact 5x5 Gauss-Jordan, checks NINE exact GLS versus disjoint-shell bilinear identities and recomputes the positive signed difference using source-enclosure centers. It is an independent formula/control, while source coefficients are necessarily common.

## Consequence, negative knowledge, strict STOP

DISPOSITION: **B_UNIVERSAL_ALL_DELTA_NEAREST_BOUNDARY = REFUTED_SOURCE_CONDITIONALLY.** M13 A/C certs unchanged and still valid. **B specific delta=.01 STILL OPEN / GRID_ONLY**, NOT falsified by this delta=.1 counterexample; do not misreport the source author's special narrower conjecture. We do NOT identify global minimizer for alpha=.105, nor claim physical hardware/noise relevance, matched original production dtc0a_runtime bytes, source-owner acceptance, independent referee approval, or new NASH K/J3/TPE physics.

The numerical scanning of other deltas (0.1 and .15 suggest additional witnesses) was exploratory FLOAT only; only the above rational witness has formal interval proof. Continued search for universal B radial monotonicity or all-delta nearest-boundary proof is inappropriate given this contradiction. A one-off optional owner M13/M14 or REC10 review may check exact coefficient boxes, shell-to-GLS identity, positivity and parameter admissibility; no new task cascade.

## Reproducibility and custody

Moderator-local ZIP MT14_ROT008_B_Global_Nearest_Boundary_Counterexample_20261026.zip, SHA256 de2a95487d958b14385976bcf2d8785d6d0bf4ce07f0d79a91b10a2a8c39c210. Contains full Polish report, certify_B_far_alternative.py (self-contained STANDARD LIBRARY Fraction exact coefficient interval proof; optional --source-json original direct_B Git blob and 100/100 endpoint verification), independent_B_gls.py (separate Fraction exact covariance inverse), scan_B.py (optional exploratory float only), two JSON outputs, execution logs, README and SHA256SUMS. ZIP CRC PASS, payload SHA256 9/9 PASS, clean empty-directory rerun both Fraction scripts PASS, both result JSON BYTE IDENTICAL.

Original M13 direct_B.json remains at OWNER's GitHub location and is NOT falsely duplicated/reissued as MT14 source. One mathematically load-bearing source-certification precheck of 100/100 endpoints was executed through the connected GitHub read in this turn; local reproduction script allows verifying it from its original file but the source blob was not included in the ZIP.

SOURCE_TYPED_EXACT_B_COUNTEREXAMPLE / CLEAN_REPRO_PASS / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
