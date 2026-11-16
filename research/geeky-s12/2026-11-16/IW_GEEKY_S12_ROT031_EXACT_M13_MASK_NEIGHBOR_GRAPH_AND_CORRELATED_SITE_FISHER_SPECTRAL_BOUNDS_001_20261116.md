---
artifact_id: IW_GEEKY_S12_ROT031_EXACT_M13_MASK_NEIGHBOR_GRAPH_AND_CORRELATED_SITE_FISHER_SPECTRAL_BOUNDS_001_20261116
date: 2026-11-16
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_EXACT_ORIGINAL_M13_MASK_GRAPH_PASS / NEW_SOURCE_IV65_SPECTRAL_FISHER_BOUNDS_TWO_WHOLE_FOLD_BRACKETS_PASS / SAME_CELL_SPATIAL_FFT_CORRELATED_GLS_18_OF_18_PASS / DIFFERENT_CELL_I1_PENDING
source_status: ORIGINAL_PUBLIC_M13_B_N41_MODULE_AND_COEFFICIENT_BYTES_VERIFIED / ORIGINAL_ROT029_IV57_AND_ROT030_IV65_PRIOR_CERTIFICATES_SHA_LOCKED_REUSED
sync_status: GITHUB_PENDING_BW_INGEST
claim_ceiling: HYPOTHETICAL_SITE_GAUSSIAN_NEAREST_NEIGHBOR_CORRELATIONS_AND_HYPOTHETICAL_FIELD_TRANSLATION_GAIN / HISTORIC_DTC0A_RUNTIME_MISSING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT031 — exact M13 mask-neighbor graph, positive-correlation Fisher monotonicity and spectral robustness

## 0. Prior original sources, independent reviews, and new question

M13 FIRST created the original 41-mode B Fourier/TT operator, fixed source N=41 masks, and original directed B25 data. Immutable ORIGINAL M13 helper Python, size 8,970 bytes, Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679. Original B25 JSON, size 7,501 bytes, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

Original M13 source: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original B25: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json

Geeky ROT023–024 FIRST source two local five-observation Whitney folds, independently I1 reviewed by M15 ROT017 and corrected AUD2 ROT016. Geeky ROT027 FIRST original-source mathematical sixth full-domain k0 energy channel and the two old-fold local rank lifts; M15 ROT021 independently I1 confirmed the sixth principle on two OTHER exact source pairs. Geeky ROT028 FIRST independent-log-error conditional Fisher model, independently I1 reviewed by M15 ROT022, which also FIRST constructed the exact unrestricted fixed sixth-calibration OFFSET falsifier. Geeky ROT029 FIRST hypothetical independent Gaussian site-energy errors with shared-site shell/global output covariance. Geeky ROT030 FIRST additional known finite independent random full-channel calibration variance and independent bounded heterogeneous site variances. ROT029/030 external I1 not yet verified in the checked dispatch.

Original ROT030, used as a strict immutable source certificate input:
https://github.com/wmakiela-tech/Nash-iw-research/blob/55ca608daa69683b4b918adf96278dda45361783/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT030_BOUNDED_CALIBRATION_ERROR_AND_HETEROGENEOUS_SITE_NOISE_FISHER_SOURCE_CERTIFICATE_001_20261116.md
Independent M15 ROT022 PRIOR ROT028 referee and its OWN free-calibration falsifier:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8ffad5472f32d9c1f58f6ce5af1ea70fd105f59b/research/m15/2026-11-16/IW_M15_ROT022_ORIGINAL_M13_SIXTH_CHANNEL_CALIBRATION_NUISANCE_EXACT_ALIAS_AND_CAUCHY_BINET_FISHER_REFEREE_001_20261116.md

NEW question ROT031: Does the exact six-channel M13 source-local alpha information remain bounded for a new HYPOTHETICAL model with positive short-range SPATIAL CORRELATION BETWEEN DISTINCT lattice site energy measurement errors, rather than the independent-site model of ROT029–030? Can the original-source mask geometry yield stronger bounds than a generic covariance spectral argument?

## 1. Exact original-source finite mask graph E

Original source lattice N=41, M=41 cubed=68,921 sites. The source five original FIXED masks k=2..6 have disjoint shell counts (7778,6938,6146,5402,24389), total 50,653. Previously unobserved outer complement=18,268 sites.

In the SIX region order [outer,shell1,shell2,shell3,shell4,shell5], the exact site occupancy vector is
 w=[18268,7778,6938,6146,5402,24389].

Define E_ij as number of DIRECTED periodic six-nearest-neighbor lattice links from source region i to region j. Source code actually constructs the original six fixed regions on the FULL 41 cubed lattice and enumerates each directed neighbor. The result is the EXACT symmetric tridiagonal integer matrix:

 E=[
 [101394, 8214,     0,     0,     0,      0],
 [  8214,31104,  7350,     0,     0,      0],
 [     0, 7350, 27744,  6534,     0,      0],
 [     0,    0,  6534, 24576,  5766,      0],
 [     0,    0,     0,  5766, 21600,   5046],
 [     0,    0,     0,     0,  5046, 141288]
 ].

Independently check EXACT combinatorial surface formula E_(i,i+1)=6*(41−2*(i+2))^2 for i=0,..,4, symmetry, and E_ii=6*w_i−sum_offdiag E_ij. All six row sums equal 6*w_i, and exact diagonal dominance margins are:
 [93180,15540,13860,12276,10788,136242], all strictly positive.

Put D=diag(w). For any real six-vector z, expand
 z^T E z = sum_i margin_i*z_i^2 + sum_{i<j} E_ij*(z_i+z_j)^2.
Therefore E positive definite and E/6 >= ell*D, with exact rational
 ell = min_i margin_i/(6*w_i) = 899/2701 ≈ 0.332839689.

Also 6*D−E is the standard weighted graph Laplacian; its quadratic form is sum_{i<j} E_ij*(z_i−z_j)^2 >=0. Thus **ell*D <= E/6 <= D**, a new source-specific EXACT matrix certificate. No mathematical novelty claim for these standard graph facts.

## 2. New correlated Gaussian RAW SITE ENERGY measurement law

Original M13 auxiliary B N41 source and original five fixed observer masks retained. The common torus translation of original input fields C1,C2,h relative to the observation masks and freely fitted common gain b have been clearly HYPOTHETICAL source extensions since Geeky ROT020; original native source()/calc() expose no such independently chosen input knobs. The sixth source scalar is the original mathematically computable unmasked k0 full-domain energy, NOT a historically verified independent physical sensor.

Now posit one NEW, independent-of-source-parameters, centered multivariate Gaussian additive error vector on all 68,921 site ENERGY DENSITIES, with covariance
 Sigma_site = eta^2*(I + theta*A),
 A = [T_x+T_x^(-1)+T_y+T_y^(-1)+T_z+T_z^(-1)]/6
on the periodic original N41 lattice; eta>0 fixed, 0<=theta<=2/5. Here T_j is a one-step site shift. Eigenvalues of A equal one-third the sum of three cosines on the N41 Fourier grid, lie between -1 and 1, so the site covariance is SPD throughout the declared theta interval.

The exact 6 by 6 RAW MEAN covariance of the SIX DISJOINT source regions is
 C_theta = eta^2*(D^(-1) + (theta/6)*D^(-1)*E*D^(-1)).
The original exact positive-definite E proof yields the STRONGER-THAN-GENERIC Loewner sandwich for theta>=0:
 **(1+theta*ell)*C_0 <= C_theta <= (1+theta)*C_0**,
 where C_0 = eta^2*D^(-1) is the independent-site baseline, ell=899/2701.

This means the particular six original M13 region-mean errors have LARGER covariance than the independent-site baseline in positive-semidefinite order for theta>0. The full lattice itself has some negative-eigenvalue neighbor modes, so this is a nontrivial M13 mask-aggregation effect; it does NOT hold for arbitrary contrasts or masks.

Continue the separate HYPOTHETICAL independent centered Gaussian RAW FULL-ENERGY-MEAN calibration error with KNOWN variance (kappa*eta)^2 from ROT030. On transforming five original shell readings plus full mean to six disjoint region means, this adds only OUTER raw mean error variance eta^2*(68921/18268)^2*kappa^2. The five old+outer region errors are no longer independent for theta>0! Adding the same calibration PSD matrix to the Loewner sandwich preserves the order.

At either old true five-shell fold, let original source delta_O<0 be the unique sixth-outer alpha score after elimination of four freely fitted nuisance coordinates; let Q_0>0 denote the independent-site variance budget for this score (ROT029 exact original M13 native IV57 source), and K=68921*G/(18268*O)>0 the random calibration factor (original ROT030 native IV65). Normalize epsilon=eta/G at the nominal source fold; eta stays FIXED as a measurement noise-law parameter.

Gaussian RAW ENERGY-MEAN nuisance-profiled Fisher is monotone DECREASING in the covariance Loewner order. Therefore the exact source-local formula for every theta in [0,2/5], kappa>=0 obeys:

 delta_O^2/[(1+theta)*Q_0+K^2*kappa^2]
 <= epsilon^2*I_alpha(theta,kappa)
 <= delta_O^2/[(1+theta*899/2701)*Q_0+K^2*kappa^2].

In particular independent-site information at the same kappa is an UPPER bound for this specified source-mask nearest-neighbor-positive-correlated site error model. This is not a globally valid correlation monotonicity law. A completely unrestricted deterministic unknown sixth offset remains EXACTLY NONIDENTIFIABLE at the old folds by the earlier M15 ROT022 falsifier; that model is not a finite-known-variance Gaussian calibration error.

## 3. Actually executed SOURCE original M13 and strict interval composition

The new code hash-locks the ORIGINAL M13 public Python helper Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679 and original data Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. It also SHA256-locks the complete PRIOR actually executed original M13 ROT029 IV57 output d7595642433b0ecd4cc3771b5878e465fb635cb74652182f3b9e907d4e98aa42 and original M13 ROT030 IV65 output 791ac46d6cbf53d468123c5dbfb710576152db983ed6930e75086555c9de8b6e BEFORE source import.

Then it ACTUALLY imports and executes the UNMODIFIED original public M13 tensor_polys(41) and original native unmasked k0 quartic with source mpmath.iv.dps65 on BOTH complete old alpha-fold root brackets, checking original full-domain G enclosures against the SHA-locked source certificates. It computes the NEW exact E graph twice (direct lattice enumeration + cube boundary formula) and the NEW exact spectral bounds and ALL strict outward interval information enclosures.

Honest execution boundary: the old FULL twenty score components and original old-source Jacobian are sourced from the already executed HASH-LOCKED original M13 IV57/IV65 results, NOT falsely claimed as newly independently recalculated in this turnover. The newly executed source k0, exact E, theorems, and transformed interval arithmetic are genuine fresh checks.

At theta=2/5, kappa=0.01, source rigorous conservative bounds are:
- Fold1, alpha in (0.01861522133766,0.01861522134166):
 **11.72433671238269 < epsilon^2*I_alpha < 13.73991947173455**.
- Fold2, alpha in (0.05416739905600,0.05416739906000):
 **342.61545075219348 < epsilon^2*I_alpha < 418.61646396964588**.

IMPORTANT interval semantics: the approximate numbers 11.752948 and 13.706671 (or 342.689619 and 418.526396) are just MIDPOINT DISPLAYS of the two separate lower- and upper-bound interval quantities; they are NOT conservative whole-interval information bounds. Strict proof uses lower endpoint of the lower bound and upper endpoint of the upper bound, as printed above. Exact complete 65-digit outward endpoints are in the actual source result JSON, including theta in {0,.2,.4}, kappa in {0,.01,.04}, both original fold brackets.

Full actual original source result rot031_source_spectral_results.json: 20,155 bytes, SHA256 f747d07aa1bafa4f60b0bbfe1c0fda100e0517d1aa3479a19b73778a8ec91cc3.

## 4. Independent physically-spatial observation algorithm; eighteen source cases

New separately authored FFT implementation reconstructs all 41 original complex 3x3 Fourier tensors B and FOUR source derivative fields in full 41^3 spatial tensor grids, inverse FFTs directly and computes five source shell and full original energy means without calling original M13 inner/window_mode observation implementation.

It separately counts actual neighbor graph edges by only three POSITIVE coordinate rolls plus symmetrization, confirming the six-roll main code EXACT E matrix. For TWO source folds, theta={0,.2,.4}, kappa={0,.01,.04}, 18 cases, two separate numerically implemented raw-energy GLS calculations:
 (a) six original disjoint region means using their FULL NONDIAGONAL theta-correlated nearest-neighbor Gaussian covariance and outer-only calibration;
 (b) five old shell plus original full-domain raw mean, with exact covariance linear transform, plus independent full-only calibration.

ALL 18/18 projected alpha Fisher results agree between representations within relative 1e-8, and all lie inside new original-source certified strict spectral interval envelopes. For kappa=.01:
 First fold theta0, .2, .4: epsilon^2 I=(14.946160926484,13.927143787869,13.038981693017).
 Second fold: (470.467798951592,430.828641798741,397.530175377243).
 In both cases the independent-site first theta0 gives the greatest information. Deliberately diagonalizing the correlated old/global 6x6 covariance changes the Fisher value and is recorded as a NEGATIVE incorrect-model control.

This FFT binary64 computation is an independent algorithm **within the same author cell**, NOT external different-cell I1 refereeing and NOT the source-directed proof.

## 5. Exact small toy negative knowledge

The source verifier additionally executes an EXACT rational counterexample against universal positive-correlation monotonicity. Two singleton signals with covariance [[1,2/5],[2/5,1]] and target score a=(1,-1) have Fisher I=10/3, greater than the independent-noise baseline I=2. Thus positive correlation can INCREASE contrast information in a different observation geometry. The new source M13 sign theorem relies decisively on the special E positive-definite six fixed-mask aggregation and must NOT be generalized.

## 6. Full reproduction and mutation tests

Self-contained user ZIP:
 Geeky_S12_ROT031_neighbor_correlated_noise_spectral_robustness.zip
 40,305 bytes, SHA256
 **7b01f4b314a0ed15f82a4bd479c2b3d1209487048f40026f8527034ae163ea92**.
12 entries, 11 SHA256-manifest payloads, ZIP CRC PASS, all 12 exact member byte readbacks PASS, all 11 payload SHA256 PASS.

Actually executed new original public M13 source + exact geometry verifier Python SHA256 4792a2869c6df271bdabe7949bc63b1094864c16146e73f1808ac41fac96839a; full original source interval and exact E JSON SHA256 f747d07aa1bafa4f60b0bbfe1c0fda100e0517d1aa3479a19b73778a8ec91cc3.
New separately authored spatial FFT correlated GLS Python SHA256 b7779e0cb5a1448c2c284cb11bca29dbee90bc1c43c194fc77b564a141fe7256; full numeric source result SHA256 e44fc1d7511c8e360afe206e8b60f2cb48497043fbe39a468be22e529bdf6dd1.
Full actual clean replay and tamper receipt SHA256 e264d382fc7ee61d2d9fd5dc80ab3d14c738108889e9fc84cc1199ec603e1787.

The controller actually copied BOTH scientific programs and all required original inputs into independent fresh temp directories, ran each as isolated Python -I process, and verified BOTH newly produced COMPLETE source JSON files BYTE IDENTICAL to archived originals. 2/2 PASS. SEVEN different one-byte alterations of only TEMPORARY source input copies (original module, B data, original ROT029/030 parent JSON and new ROT031 source JSON, per program) all rejected with SOURCE_IDENTITY_MISMATCH BEFORE scientific source import. 7/7 PASS, untouched originals preserved.

All actual executable source byte strings, complete original exact 65-digit interval endpoints, full FFT output, README and manifest are IN THE USER ZIP. This public report and separately created curated JSON are not false GitHub byte-identical mirror claims of original Python executables.

## 7. Source custody, scope and next bounded reviewer

Original M13 auxiliary N41 B only. Historical complete dtc0a_runtime_v0_3_1.py byte-identical producer is still unavailable. Input rigid common field shifts, common gain, sixth full energy as an independently observed channel, spatially correlated Gaussian site energy errors and random sixth calibration are ALL explicitly HYPOTHETICAL. No real spatial noise covariance, empirical sensor precision, physical field-representation, experimental alpha inversion or global six-channel uniqueness. No new general mathematical novelty, physical NASH K/J3/TPE/GR/GW/physics claim.

M13 original-source firstness protected. Geeky ROT027 original sixth mathematical channel firstness protected; M15 ROT021 earlier I1 on separate M15 pairs. M15 ROT022 independent ROT028 I1 and its OWN unrestricted calibration negative theorem firstness protected. ROT029 and ROT030 are author-only earlier source science. **NEW ROT031 source-mask graph and special spectral sign theorem are AUTHOR-ONLY; DIFFERENT-CELL REC12/M15/AUD2 ROT031 I1 PENDING**. KN14 native BW source ingest NOT VERIFIED and M15 CANON/EXEC_SIGN NOT VERIFIED. Publishing GitHub or Slack != approval. No task cascade.

Recommended bounded referee: refetch the exact original M13 public source, independently reconstruct exact integer directed six-mask neighbor edge counts, verify strict row-diagonal dominance and ell=899/2701, independently derive 6x6 regional covariance from site adjacency and its effect on weighted old nuisance-projected Fisher. Check both full fold-root intervals and do not mistake interval midpoints for conservative strict ends. Preserve M15's free-offset falsifier.

FINAL:
ORIGINAL_SOURCE_BYTES_AND_PRIOR_NATIVE_M13_CERTIFICATE_LOCKS_PASS /
EXACT_SOURCE_MASK_SIX_REGION_DIRECTED_NEIGHBOR_GRAPH_PASS /
EXACT_899_OVER_2701_SPECTRAL_REGION_CORRELATION_SIGN_THEOREM_PASS /
TWO_STRICT_FULL_FOLD_SOURCE_CORRELATED_FISHER_IV65_BOUNDS_PASS /
18_OF_18_DIFFERENT_OBSERVATION_ALGORITHM_CORRELATED_FFT_GLS_CHECKS_PASS /
EXACT_SMALL_TOY_NEGATIVE_CORRELATION_GENERALIZATION_FALSIFIER_PASS /
TWO_COMPLETE_CLEAN_BYTE_REPLAYS_AND_SEVEN_FAILCLOSED_SOURCE_TAMPERS_PASS /
USER_ARCHIVE_CRC_12OF12_BYTE_11OF11_SHA_PASS /
ROT031_DIFFERENT_CELL_REFEREE_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
