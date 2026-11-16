---
artifact_id: IW_M15_ROT027_ORIGINAL_M13_MIXED_SITE_CORRELATION_FISHER_UTURN_SOURCE_CERTIFICATE_001_20261117
return_id: IW_M15_ROT027_M13_TWO_SOURCE_FOLD_NONMONOTONE_THETA_FISHER_TWO_UNIQUE_TURNS_AND_BASELINE_CROSSINGS_001_20261117
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-17
exposure: PUBLIC
result_class: DIFFERENT_CELL_NONBLIND_INTERNAL_I1_NEW_ORIGINAL_NATIVE_M13_SOURCE_MATH_IV55_CONTINUUM_NONMONOTONE_FISHER
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: AUXILIARY_PUBLIC_M13_ONLY / NO_HISTORIC_DTC0A_RUNTIME / NONNATIVE_HYPOTHETICAL_TRANSLATION_GAIN_SIXTH_SENSOR_AND_SPATIAL_NOISE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE
---

# M15 ROT027 — Two source-certified U-turns of efficient alpha Fisher information under fixed positive spatial site correlations

## 1. New bounded science and original firstness

M13 FIRST original public N41 Fourier B auxiliary TT/Lie source module, full 8970B unchanged Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679, SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c, original at research/m13/2026-10-24/verify_m13_rot33_interval.py commit 30d8549b822ecec4d6939b01dbd1e76a98495f09. This EXACT original module was ACTUALLY executed by TWO M15 original source programs, which validate its file SHA256 and binary Git object SHA1. Historical dtc0a_runtime_v0_3_1.py full producer is NOT recovered.

Geeky-S12 ROT031 FIRST strict positive axial neighbor original-site graph / Fisher DECREASE source theorem. Geeky ROT032 FIRST indefinite body-diagonal neighbor source graph / Fisher INCREASE continuous-theta theorem. M15 ROT026 independently different-cell I1 reviewed both and first bounded critical diagonal mixing lambdas at theta=0. M15 ROT027 FIRST in this source chain gives TWO explicit fixed positive neighbor mixing ratios where EFFICIENT ALPHA FISHER IS NONMONOTONIC in theta: it initially falls, reaches EXACTLY ONE minimum, rises, and crosses its initial no-correlation value EXACTLY ONCE before theta=0.4. This is an internally independently reproducible source-conditional result, NOT a novel general mathematical theorem.

## 2. Exactly scoped mathematical observer

N=41, total 68921 periodic grid sites. Original 5 fixed disjoint cube observation shell counts (7778,6938,6146,5402,24389) and outer 18268. Original unmodified native M13 tensor_polys(41)[1], dot and window_mode used; 41 original sparse complex 3x3 B tensor Fourier modes, 1681 ordered Fourier pair correlations and 221 q differences; all five original fixed native source mask observations and analytic alpha and three hypothetical common torus translation derivatives constructed on full source alpha intervals. Four nuisance parameters (one common gain b + three common rigid source-field shifts relative to FIXED observation masks) are expressly HYPOTHETICAL extensions, not native M13 input knobs. Sixth full Fourier Parseval source energy, equivalent to extra outer shell information, is NOT a documented physical detector.

Synthetic mean-zero Gaussian RAW SITE energy noise covariance eta²(I+theta*A_lambda), A_lambda=(1-lambda)A_axis+lambda*A_body, where A_axis is normalized symmetric six axial one-site neighbor shifts, A_body normalized symmetric eight body-diagonal one-site neighbor shifts, 0<=lambda<=1, 0<=theta<=0.4. Every named neighbor covariance is nonnegative. Both adjacency averaging operators have spectral norms at most one, so entire site covariance is strictly positive definite for entire theta interval. Optional independent Gaussian raw full-energy calibration with KNOWN finite standard deviation kappa*eta is allowed; the source result is NOT valid under an unrestricted fitted deterministic sixth-only log offset c, as M15 ROT022 proved.

At each exact original old five-channel rank4 alpha fold, define nuisance-annihilating six-observation contrasts L=(l1,...,l5,1). These form a one-dimensional affine family L=A+tB with outer coefficient exactly one. Let C(theta)=C0+theta C1 be the correctly aggregated NONDIAGONAL region-mean covariance of LOG SCORES scaled by epsilon=eta/G, noting this is a local coordinate for exact Gaussian RAW ENERGY mean Fisher, not a claim of Gaussian noisy logs. The optimized nuisance-contrast variance and scaled efficient target alpha information obey
  V(theta) = min_t (A+tB)^T C(theta)(A+tB),
  epsilon² I_eff(theta) = delta_outer² / V(theta), delta_outer !=0 at old source fold.

## 3. Exact closed-form continuum theorem and source interval proof

Set a0=A^T C0 A, b0=B^T C0 A, d0=B^T C0 B>0, and a1,b1,d1 analogously for C1. Classical 1D quadratic minimization gives exactly
  V(theta)=a0+a1 theta -(b0+b1 theta)^2/(d0+d1 theta);
  V''(theta) = -2*(b1*d0-b0*d1)^2/(d0+d1 theta)^3.
The independent ORIGINAL M13 source program actually computes all six coefficients via mpmath.iv.dps55 over the ENTIRE original alpha closed bracket, proving d0+d1*[0,.4] strictly positive and b1*d0-b0*d1 strictly nonzero, and hence V''([0,.4])<0. Thus V is STRICTLY concave and V' strictly decreasing over ALL real theta in [0,.4].

Source further rigorously proves V'(0)>0 and V'(.4)<0 and brackets their sole root (the sole Fisher minimum); V(.4)<V(0) is a separate strict IV55 inequality, hence the final Fisher information is greater than its original value and there is one positive baseline-crossing theta after the unique turn. Source analytically derives that crossing as
  P=a1*d0^2-2*d0*b0*b1+b0^2*d1 = d0^2 V'(0)>0;
  Q=d0*(a1*d1-b1^2)<0;
  theta_cross=-P/Q in (theta_turn,.4).
The source certifies its interval without float root finding. Since the known-variance extra stochastic sixth calibration adds a constant to V independent of t and theta, the derivatives and both landmark thetas are unchanged for ALL fixed FINITE kappa>=0.

ORIGINAL entire alpha root brackets (both source-existence previously reviewed):
 FIRST alpha in [0.01861522133766,0.01861522134166], fixed body lambda=0.609:
  IV55 V'(0) in [9.028103729e-6,1.082497384e-5] STRICT POSITIVE;
  IV55 V'(.4) in [-3.310648806e-5,-3.095579821e-5] STRICT NEGATIVE;
  IV55 V''([0,.4]) in [-1.241124254e-4,-8.837099915e-5] STRICT NEGATIVE;
  EXACT UNIQUE theta_turn in (0.09,0.13);
  EXACT UNIQUE theta_cross in [0.19137494470885,0.23239534348856].

 SECOND alpha in [0.05416739905600,0.05416739906000], fixed body lambda=0.510:
  IV55 V'(0) in [6.499015131e-5,7.035088954e-5] STRICT POSITIVE;
  IV55 V'(.4) in [-8.375476427e-4,-8.322111035e-4] STRICT NEGATIVE;
  IV55 V''([0,.4]) in [-2.326803487e-3,-2.187843538e-3] STRICT NEGATIVE;
  EXACT UNIQUE theta_turn in (0.025,0.035);
  EXACT UNIQUE theta_cross in [0.05599553566357,0.06070598287393].

All displayed upper/lower bounds are deliberately conservative rounded OUTWARD from ORIGINAL complete directed machine JSON. Both results hold for EVERY alpha in the original closed narrow root box, hence in particular at each rigorously existing exact old Fisher-zero root. They do NOT assert original full alpha domain behavior.

## 4. Independent spatial source computation

A SECOND new independently authored original-native M13 Python script constructs nine full 3D tensor B component spatial fields and four analytic derivative spatial fields using actual 41^3 inverse FFT. It independently integrates original fixed site masks and builds six-region covariance from ORIGINAL site-label axial/body rolls. It then performs GLS in TWO exactly equivalent observer bases: old five+outer and old five+FULL with correct NONDIAGONAL covariance, and separately performs an SVD-based nuisance-null contrast minimization, without reading source-IV Fourier-q arrays. For two folds x seven theta values (0,.02,.05,.1,.2,.3,.4) x two random calibration choices kappa in {0,.01}, all 28/28 independent original source numerical GLS cases passed equality and IV source gate. Numeric turn and crossing in full 41³ source spatial code lie strictly inside source IV55 brackets:

 FIRST lambda .609, theta_turn ~0.10744390562745842, theta_cross ~0.21181199205995319; kappa=.01 Fisher at theta0 ~14.94616092646914, theta .4 ~14.95304208926718. At theta .1 ~14.94522324088569 (lower).
 SECOND lambda .510, theta_turn ~0.029153352956642113, theta_cross ~0.05835053486467603; kappa=.01 Fisher theta0 ~470.46779895173853, theta .4 ~472.66474418616710; theta .02 ~470.45528586124556 (lower).

FFT and SVD are NUMERICAL DIAGNOSTICS and not the interval proof.

## 5. Real executable reproducibility, corrected failed preliminary controls

COMPLETE ORIGINAL source and new runnable code in the actually created USER-LOCAL ZIP
  IW_M15_ROT027_ORIGINAL_M13_NONMONOTONE_SPATIAL_FISHER_IV55_REPRO_001_20261117.zip
  38,688 bytes
  SHA256 172b79f27a2b38589fc903bf5c2e258bad14f9e4891c8019c43434283261c5e4.
11 members, zip CRC PASS, 10/10 manifest member SHA256 PASS and 11/11 exact archive byte reread PASS. Unchanged original native M13 module file, original IV55 source checker (SHA256 ee05367b6926ffe2d1560b6422a1203b22d15a3341e0f81a9f1ff03b33d4b033), its ACTUAL complete source IV55 result JSON (SHA256 d5cdcbc3029373bc26dbe48f4030a46ff45a8974ab0098b1043ff33c1a233b1e); separate original spatial FFT/GLS script (SHA256 93cafeebfe956b9f40d347900ce50c9e30184a9d68dec377bb388ee2be2554dc), its actual full 28-case output JSON (SHA256 0720dbb6b91677b14ac9bb7ab5b5cac9f53ef472df6c10cf8073575f47f3ab8a), actual replay/negative test code and receipt, README, source report, manifest.

ACTUAL original programs copied to an independent CLEAN temp directory and EXECUTED Python -I, both complete original machine JSON outputs BYTE IDENTICAL to original (2/2 PASS). SIX actual NEGATIVE fixtures were ALL rejected as required: original M13 one-byte tampering against BOTH new scripts, one-byte new primary IV55 cert tampering against spatial checker, two deliberately INCORRECT lambda substitutions (first and second) causing expected science-sign failure, and a deliberately wrong original six-region BODY graph integer count causing exact combinatorial failure. Controls are real executions, not just assertions written on paper.

Two earlier prepublication bugs were detected and genuinely corrected: first IV source JSON did not serialize the analytic crossing and turn data (spatial script raised KeyError), then early spatial code shadowed original Fourier source dictionary u with a local floating bisection variable (TypeError at second fold). Neither failed run was counted as PASS. Corrected and rerun both science programs, exact clean repro and negatives complete.

## 6. Science ceilings

Only ORIGINAL M13 public auxiliary Fourier source and explicitly synthetic six-output Gaussian observer. The original native M13 program contains no freely tunable input shift t, common gain b, or physical sixth measurement. No actual spatial correlations, site errors, calibration precision, sensor SNR, physical mechanism, NASH K/J3/TPE, GR/GW, global inversion, historic full DTC0a producer equivalence, or novel general mathematical theorem. Geeky ROT031/032 original firstness preserved. Internal different-cell nonblind I1, no REC13/AUD3 or external blind I3 approval; KN15 BW native ING receipt unverified. Slack POST != owner ACK. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.

FINAL: TWO_WHOLE_ORIGINAL_ALPHA_ROOT_SOURCE_IV55_STRICT_U_SHAPED_FISHER_PASS /
 TWO_UNIQUE_INTERIOR_THETA_TURNS_AND_TWO_UNIQUE_BASELINE_CROSSINGS_PASS /
 ORIGINAL_NATIVE_M13_GIT_BLOB_IMPORTED_EXECUTED /
 28_OF_28_INDEPENDENT_SPATIAL_DUAL_GLS_PASS /
 2_OF_2_BYTE_IDENTICAL_COLD_REPLAYS /
 6_OF_6_NEGATIVE_REJECTIONS /
 ZIP_CRC_SHA10_OF10_PASS / ORIGINAL_FIRSTNESS_PROTECTED /
 BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
