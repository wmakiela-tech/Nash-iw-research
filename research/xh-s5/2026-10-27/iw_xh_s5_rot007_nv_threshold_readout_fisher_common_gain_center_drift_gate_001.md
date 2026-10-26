# XH-S5 ROT007 — NV laser threshold magnetometry: robust readout and exact center-drift alias

artifact_id: IW_XH_S5_ROT007_NV_LASER_THRESHOLD_READOUT_FISHER_GATE_20261027
return_id: XH-S5-ROT007-LASER_THRESHOLD_ODMR_COMMON_MODE_AND_CENTER_DRIFT_GATE_20261027
date: 2026-10-27
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: SOURCE_FULL_HTML_REVIEW / EXACT_SOURCE_MOTIVATED_LORENTZIAN_POISSON_FISHER_TOY / NO_AUTHOR_EXPERIMENT_REPLAY / NO_MATH_NOVELTY / NO_NASH_PHYSICAL_KJ3 / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Source fact and nonconflation
F. Schall, L. Lindner, Y. Rottstaedt et al., "Laser-enhanced quantum sensing boosts sensitivity and dynamic range", Nature Communications 17:10825, PUBLISHED 22 October 2026, DOI https://doi.org/10.1038/s41467-026-78386-z . Full primary HTML and main methods reviewed. Diamond NV embedded in MECSEL cavity at 1042 nm; 100% optical contrast, 2–50 mW output, vector sensing. Quoted <400 fT/sqrt(Hz) for all vector components and minimum 127 fT/sqrt(Hz are PHOTON SHOT NOISE SENSITIVITY LIMITS inferred from spectral fits, **NOT ACTUALLY ACHIEVED SENSOR SENSITIVITY**; authors explicitly say technical noise currently much higher and would require stabilization, balanced detection and laser noise suppression. Different source settings: 1160 fT/sqrt(Hz) PSN limit with intrinsic linewidth-defined range +/-280 microtesla; <400 fT/sqrt(Hz) PSN limit in other diamond sample with intrinsic range +/-40 microtesla. Do not conflate settings. Authors' PSN formula uses eta_B proportional sqrt(I)/|dI/dnu|, warns small-C approximation fails at high contrast and limiting optimum shifts toward resonance minimum. Source experimental dataset advertised in Article Source Data, NOT downloaded, no source hardware or 3-line hyperfine spectrum reproduced.

## Priority subtract: external and NASH
Jeske/Cole/Greentree, Laser threshold magnetometry, NJP 18 013015 (2016), DOI 10.1088/1367-2630/18/1/013015 precedes experiment. Bedford/Sevison/Slocum, US PATENT APPLICATION US20260056270A1, priority 2024-08-21, publication 2026-02-26, https://patents.google.com/patent/US20260056270A1, describes a dual resonance-slope differential measurement canceling correlated optical technical noise and multi-peak approaches for thermal drift. Opposite slope readout NOT our innovation. Fisher projection, Schur complement and sign alias are mature results. Public NASH repo keyword searches "NV magnetometry" and "laser threshold" returned no match; private prior art not ruled out. Other XH-S5 ROT001-006 study different scientific hosts; NASH analogies strictly methodology, NO physics admission.

## Independent EXACT source-motivated mathematics
Not a fit to the Nature device. Synthetic one-line Lorentzian ODMR dip f(x)=1-C/(1+4x^2) with normalized frequency x=(nu-nu0)/FWHM, contrast C=.97, offset a=.5. f(a)=103/200=.515, f'(a)=97/100=.97. Poisson counts at two tones x_i=(-a,+a) with TOTAL OFF-RESONANCE expected photon budget N=10000, common unknown gain g, physical field shift delta, and optional unknown common center-frequency drift e:
mu_i=(g/2)*f(x_i-delta-e).
At nominal g=N, delta=e=0 each channel mean mu=2575. Synthetic count scales are not source mW nor fT.

For independent Poisson channels known-nuisance FI Jdelta=sum_i (partial_delta mu_i)^2/mu_i. Under two symmetric tones at zero shift the delta derivative=(+4850,-4850), common gain score=(2575,2575), and common additive-background nuisance score=(1,1). These weighted scores are mutually orthogonal w.r.t. delta, so effective field information with unknown common gain, or both unknown common gain and common offset, is still EXACT:
J = N*f'(a)^2/f(a) = 1881800/103 = 18269.90291262136, CR stdev=0.0073982990 FWHM.
The gain and additive background are themselves rank-deficient at balanced conditions; effective field score nevertheless remains orthogonal to their nuisance SPAN. This is only a LOCAL two-tone information result.

Failure controls: a SINGLE probe frequency plus unconstrained gain yields ZERO nuisance-profiled FI for delta; two tones with TWO SEPARATE unconstrained channel gains also have ZERO efficient FI, because nuisance spans both count coordinates. A change from synchronous common gain to asynchronous independent gains can therefore make an otherwise excellent PSN bound non-identifying without calibration.

No wavelength/microwave-tone schedule alone can identify field shift delta separately from unconstrained central-frequency drift e when counts depend only on delta+e. Exact witness delta=.01, e=.02 versus delta=-.04, e=.07: same FULL joint Poisson likelihood for any set of frequencies. Independent Gaussian e reference sigma_e=.02 FWHM restores efficient CR bound Var(delta)>=1/J+sigma_e^2, standard deviation 0.02132451238 FWHM, 2.8823534 times ideal shot-noise stdev. Illustrative calibration, NOT real system.

Global sign control: at exactly resonance center x=0 a SINGLE frequency gives f(-delta)=f(delta) even at 100% C; delta=+/-0.01 predicts IDENTICAL Poisson mean 3.99840063974 for N=10000 and identical likelihood, NOT just approximately. Symmetric two-tone measurement at a=.5 with C=.97 gives different full Poisson likelihood for +/-0.01; their joint Bhattacharyya affinity=0.401018305184, independently checked by summing discrete Poisson PMFs. For C=1, the *off-center local FI* approaches 16N as x approaches zero from above, but this never proves global field sign or regularity AT exact center. Local-Fisher vs global injectivity are different claims.

An independent SciPy scalar optimization of the source-inspired normalized Lorentzian PSN factor f'(x)^2/f(x) gives best normalized offset x=.2868125165 at C=.05 versus x=.1504150546 at C=.97, consistent with source authors' qualitative claim that high contrast optimum moves toward resonance minimum. This is NOT an author curve fit.

## Executed controls, exact and computational
Three independently implemented scripts:
1. pure standard-library Fraction witness: f=103/200, fp=97/100, FI=1881800/103 exactly; exact gain and additive orthogonality, separate gains spanning, resonance drift and sign alias.
2. independent NumPy Jacobian/Fisher projectors and finite-difference checks; deterministic Monte Carlo of 120000 synthetic count-pairs subject to positive common lognormal gain sigma(log g)=.25, with ratio-based differential estimator stdev .007616196 versus leading-order expectation .007633146 (-.222%). This is synthetic ONLY and does not model actual fast independent laser fluctuations.
3. independent SciPy bounded optimization on three contrasts, separate discrete Poisson PMF summation of Bhattacharyya overlap agreeing analytic answer within 1e-10.

All 3 scripts reexecuted after extracting archive in new clean directory: JSON results BYTE-IDENTICAL to frozen source outputs; per-file SHA-256 and ZIP CRC PASS.
MODERATOR FULL LOCAL CODE+REPORT+JSON+MANIFEST+README ZIP:
IW_XH_S5_ROT007_NV_ODMR_FISHER_DRIFT_REPRO_20261027.zip
SHA256 309a1c2f4199d38da1750eb6f072ddf64c4cd6de9934225395cc16f64023a713.
Local full 13k report SHA256 3f0acb88161528f621c9ee1ad430480332dd0f9eaf3724668d60f521a9eb22f0.
This GitHub text contains all core math but NOT full local ZIP/code unless separately uploaded and read back.

## Discriminating future source-native experiment (proposed only)
Freeze sensor line fit and exposure budget; compare one-slope, simultaneous symmetric two-slope, temporally separated symmetric two-slope under matched total photons and independently injected common vs per-channel optical gain fluctuations. Independently inject/calibrate center-frequency drift, using second ODMR resonance or external reference. Record actual technical noise covariance, raw count histograms, field bias and holdout stability; run authors' triple-hyperfine line model. Predicted failure: no independent center reference means field/center drift alias; no common gain across two tones means no nuisance-projected local information. No experiment performed on source hardware; no claim source is unaware.

NO_NEW_NASH_PHYSICS / NO_MATH_NOVELTY / NO_AUTHOR_DEVICE_REPRO / NO_CANON / NO_EXEC_SIGN / NO_BW_INGESTION_ASSUMED / NO_NEW_CELL_TASK.
