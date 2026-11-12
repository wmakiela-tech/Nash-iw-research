# M14 ROT046 — known-field reference removes channel calibration but costs samples: sharp global Gaussian minimax

artifact_id: IW_M14_ROT046_REFERENCE_CALIBRATION_COST_AND_STABILITY_GATES_001_20261112
return_id: M14-ROT046-KNOWN_FIELD_REFERENCE_SHARED_CHANNEL_BIAS_GAUGE_AND_SHARP_GAUSSIAN_RESOURCE_THRESHOLD_001_20261112
date: 2026-11-12 | origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC | ceiling EXACT_CLASSICAL_CONDITIONAL_GAUSSIAN_REFERENCE_MINIMAX / NO_NOVELTY / NO_SENSOR_NATIVE_DATA / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

SOURCE FIRST: XH-S5 ROT007 Schall, Lindner, Rottstaedt et al. *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications **17** (2026), 10825, DOI https://doi.org/10.1038/s41467-026-78386-z, Oct 22. Authors' 127 fT/sqrtHz is a PHOTON-SHOT-NOISE sensitivity LIMIT, not measured technical-noise performance. NO real known-field paired/reference session, calibration stability, equal Gaussian shot budget or source-native time-series. Own first: ROT039 shared simultaneous calibration, ROT044 hidden jitter, ROT045 unequal jitter. ROT046 uses a NEW EXTRA known-field reference experiment; no reattribution. Algebra classical.

FROZEN MODEL, source-typed synthetic: tetra axes A=(+++,+--,-+-,--+), A^TA=4I3, first three rows A3 invertible. Target field z unknown; reference vector z_ref is KNOWN EXTERNALLY. Per-channel arbitrary unknown beta_i appears in BOTH sessions. Target samples T_i=a_i.z+beta_i+d_i+independent N(0,sigma²), reference samples R_i=a_i.z_ref+beta_i+independent N(0,sigma²). Total N unit-cost shots counted across BOTH runs and r=3/4 sensor axes. Equal elemental sigma², adaptive repetition allocation between previously specified target/reference channels allowed; no new times or known physical hardware stability assumed. If d_i=0, exact stable calibration; alternatively independent unknown bounded |d_i|<=D, NOT automatically implied by original sensor. Difference observations X_i=Tbar_i-Rbar_i+a_i.z_ref=a_i.z+d_i+noise with var sigma²(1/n_iT+1/n_iR); any beta_i cancels exactly.

NEW R46.1 EXACT global minimax across all estimators incl biased/adaptive repetition:
- with stable beta, r=4: **R4*=12sigma²/N** (integer N multiple 8);
- with stable beta, r=3: **R3*=18sigma²/N** (integer N multiple 6).
At integer other N these are lower bounds. Take n_iR=n_iT=N/(2r). Four-axis zhat=A^TX/4 yields Cov=4sigma² I3/N, total trace12sigma²/N. Three-axis zhat=A3^-1 X yields trace18sigma²/N. Full RAW 8- or 6-means nuisance Fisher gives identical inverse covariance, verified exactly.

LOWER: after profiling beta_i, efficient Fisher I_z=sigma^-2 sum_i q_i a_i a_i^T with q_i=n_iT n_iR/(n_iT+n_iR)<=n_i/4, n_i=n_iT+n_iR. Four axes trI<=3N/(4sigma²) => trCov>=12sigma²/N. Three axes trace inverse=sigma²/2 sum_i 1/q_i>=18sigma²/N. Proper diffuse Gaussian priors on field and beta_i give same bounds for ANY estimator incl biased and adaptive histories, not just CRLB-unbiased. Equal replication achieves them.

NEW R46.2 exact bounded run-to-run mismatch floors |d_i|<=D:
**R4,D*=12sigma²/N+D²** and **R3,D*=18sigma²/N+3D²** at divisible N.
UPPER: four-axis projected signed cube [-D,D]^4 has worst squared bias D²; for A3^-1 exact worst cube bias²=3D². LOWER two worlds z_s=u+s v, d_i,s=-s a_i.v and common stable arbitrary beta_i. r4 choose v=D e_x (all a_i.v=±D), r3 v=D(1,1,-1) (all first-three a_i.v=D). FULL reference and target means identical under s, so independent binary hidden sign adds ||v||²= D² or 3D² to the sharp Gaussian variance lower, even under adaptive allocation or biased inference. Not physical H/d drift data.

NEW R46.3 NEGATIVE CONTROLS: Without run-to-run stability, if beta_iT and beta_iR are independently unrestricted, z->z+v and beta_iT->beta_iT-a_i.v keeps target/reference raw means unchanged for arbitrarily large v; ABSOLUTE field global minimax INFINITE. With stable beta but UNKNOWN reference field z_ref, simultaneous shifts z,z_ref -> z+v,z_ref+v and beta_i->beta_i-a_i.v preserve all target/reference raw means. Only the relative field z-z_ref is identified; absolute z unidentifiable without external anchor.

NEW R46.4 CROSS-PROTOCOL CHOICE, only if BOTH contracts independently justified: direct four-axis hidden-jitter ROT044 risk=3sigma²/N+(H eps)². Four-axis calibrated-reference risk=12sigma²/N+D². Reference wins iff D<H eps AND
**N>9sigma²/[(H eps)²-D²]**.
Example sigma²1, H eps0.1, D0.02 -> crossover N>937.5. At N240, direct risk 0.0225 < reference 0.0504; at N1200 reference risk 0.0104 < direct 0.0125. This is a mathematical comparison of distinct source-UNVERIFIED contracts, NOT a recommendation for the real NV apparatus.

REPRO ORIGINAL moderator-local Polish report, three executable scripts, two actual generated JSON, README, SHA and dispatch ZIP: IW_M14_ROT046_REFERENCE_RUN_SHARP_MINIMAX_STABILITY_GATES_REPRO_001_20261112.zip, 11992 bytes, SHA256 **240c6cea24fe634532e6c0ae19ae0d73a1876557d0778faaeb9cd33740acf318**. CRC PASS, SHA manifest 8/8 PASS, clean 2 full scripts JSON BYTE IDENTICAL, pure stdlib exact replayer PASS. SymPy Fraction exact 80 checks incl entire 6/8 RAW Gaussian nuisance FI. Independent NumPy/mpmath90 2012 checks, 2000 random positive allocations and 170000 Gaussian MC per r3/r4. Theory at N1200,sigma²1,D.02: r4 0.0104, observed 0.0104287369; r3 0.0162, observed 0.0161830948. Numeric tests do not prove minimax; analytical Fisher+BAYES+two-world proof does. Full ZIP LOCAL, only short science note and exact stdlib script to GitHub.

STRICT GUARDS: no actual Schall known-field calibration, source-native time data, native photon Poisson technical noise/H eps D sigma, measured fT performance, new NASH J3/K GR/GW/PBH physics, novelty, independent REC11/AUD1 verdict, BW ingest, LT adoption, canon or EXEC sign. NO_NOVELTY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE. POSTED != ACK.