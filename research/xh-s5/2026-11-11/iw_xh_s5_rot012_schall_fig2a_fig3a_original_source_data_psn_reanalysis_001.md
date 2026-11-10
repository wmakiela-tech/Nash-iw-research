# XH-S5 ROT012 — Schall 2026: genuine Source Data Fig2a->Fig3a shot-noise limit replay

Artifact: IW_XH_S5_ROT012_SCHALL_ORIGINAL_PSN_FIG2A_TO_FIG3A_SOURCE_NATIVE_REPLAY_20261111
Date: 2026-11-11
Cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
RETURN_ID: XH-S5-ROT012-SCHALL-FIG2A-TO-FIG3A-SOURCE-NATIVE-SHOT-NOISE-RECONSTRUCTION_001_20261111
EXPOSURE: PUBLIC_SOURCE_NATIVE
CLAIM_CEILING: ORIGINAL_USER_SUPPLIED_PUBLISHED_DATA_REANALYSIS / NO_AUTHOR_DEVICE_REPLAY / NO_MEASURED_NOISE_SENSITIVITY / NO_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_INGEST_UNVERIFIED

## Public source fact and original custody
F. Schall, L. Lindner, Y. Rottstaedt et al., Laser-enhanced quantum sensing boosts sensitivity and dynamic range, Nature Communications 17 10825, published 2026-10-22, DOI https://doi.org/10.1038/s41467-026-78386-z. Original complete 12-page publisher article was user supplied (PDF SHA256 a4244e1243b2b337c3ad703172aed1b2b3527d3bea5dda1e9dc70f0c5d29f072). Source Data was separately provided by Moderator, exact original 88710-byte 41467_2026_78386_MOESM2_ESM.zip, SHA256 6f6fdf9b68a4f74144ccd9269de75a299ceeb326013e96863498f96eb11fcf5e. Source native zip bytes included UNMODIFIED in local ROT012 full reproducibility package. No independent publisher-server binary hash proof.

Fig2a.csv: 600 microwave frequencies GHz + source-measured red curve laser power mW, alongside blue comparison. Fig3a.csv: SAME 600 frequency rows, derived gradient-fit photon-shot-noise LIMIT fT/sqrtHz, and two columns containing constant analytic Eq1 and weak-contrast Eq2 limits. Authors had already done both fit and Eq15; this is an INDEPENDENT REANALYSIS of real input data not new experimental data, author error, physical novel theory or time-noise evidence.

## Independent source-native computation
Fit to Fig2a RED POWER ONLY, no parameter fitting against Fig3a: 8-parameter two-Lorentzian absorption dips plus linear power baseline:
P(x) = b0+b1(x-2.87) - A1*w1^2/((x-c1)^2+w1^2) - A2*w2^2/((x-c2)^2+w2^2)
x=GHz; P and A in mW. SciPy TRF nonlinear least squares 600 data rows; source red scan power RMSE 0.3578641283 mW. Centers c1=2.82825539376 GHz, c2=2.91137317557 GHz. This is descriptive spectrum fit, not the source microscopic MECSEL rate model.

Use author Methods Eq15 PSN propagation with SOURCE 1042nm photon energy Eph=h*c/lambda, electron g=2.0023, Bohr magneton, analytical P'(x), correct MW GHz and laser mW conversions, and sqrt(3) geometric projection (100) bias field along NV [111]:
eta_B(x)=sqrt(3)*h/(g mu_B) * sqrt(P_W(x)*Eph)/|dP_W/df_Hz|, in T/sqrtHz.
No fitted multiplicative sensitivity calibration.

Compare ALL 126 source points obeying predeclared finite-slope window: ORIGINAL Fig3a gradient-fit PSN <10000 fT/sqrtHz and reconstructed PSN <30000. Median |eta_XH/eta_source-1|=0.004956330215702187 (0.495633%); p90=0.01637099758414734; log-Pearson=0.9998785467475648; median signed difference=-0.0004306550. Source minimum=1106.5655981711245 fT/sqrtHz at 2.826 GHz; independently reconstructed minimum=1113.0018130771473 at SAME 2.826 GHz; +0.5816388%.

SHARP GEOMETRIC NEGATIVE: OMIT sqrt(3), same exact fitted spectrum and physical constants; median absolute difference balloons to 0.42289836961758404 (~42.29%), median eta_no_geom/eta_source=0.5771016303824 close to 1/sqrt3. Demonstrates source field projection necessity, no novelty.

## Independently programmed holdout, differentiated again
Second script uses scipy.optimize.curve_fit Levenberg-Marquardt on 300 EVEN rows ONLY, independently written model function and COMPLEX-STEP derivative; evaluates 300 held-out ODD source rows. Train power RMSE 0.3565248738 mW; HOLDOUT power RMSE 0.3592372413 mW. PSN finite-slope window 62 heldout points: median absolute relative disagreement 0.005440432130969841 (0.544043%), p90=0.015915094266263304, log-Pearson=0.9998670187831828. Complex step derivative vs independently computed fourth-order finite difference maximum relative discrepancy 3.85e-10. This is holdout of rows from the SAME original instrument scan, NOT a blind independent sensor experiment.

Third independent source-only script verifies Fig3a 600 rows, column 3 full-optimum Eq1 CONSTANT 1149.2924019572317 fT/sqrtHz, column 4 weak-contrast Eq2 CONSTANT 2832.7680125872666; ratio2.4647931264. Fig3a derivative-fit source minimum 1106.565598 differs from the authors' analytic constant by -3.71766%; they represent DIFFERENT computation columns, no paper error or faulty sensor inference claimed. Source Fig3 caption loosely says 1160, consistent in scale with Eq1 1149; no diagnosis of authors' full fit conventions. Independent isolated single-Lorentz model optimum offset x/FWHM moves from0.286812516 at C=.05 to0.150415054 at C=.97; mature standard known result not source experiment reconstruction.

## Strict nonmaps to actual technical noise, drift and physics
Authors clearly say measured laser technical noise is orders above PSN fundamental LIMIT. Both source PSN curves and reconstructed values are derived **potential shot-noise performance**, NOT actual magnetic-field sensitivity of the laser device; no time-dependent experimental PSD, Allan deviation, drift traces, temporal polynomial or calibrated noise covariance were read. EKS1 ROT004 accepted original Source Data T1=COMPLETE / NO TEMPORAL SHEETS IN THIS ZIP and GAP001 waits for M14 owner disposition STOP or alternate source, not remedied here. The 8-parameter fit does not identify true instrument noise (power RMSE cannot substitute temporal PSD). No connection to new NASH J3K or other physics.

DAX-S8 ROT008 scalar collision gate and XH-S5 ROT011 pinned MadGraph source contact remain separate; no 4e massive uncut generator was run and no cross section is reported. No new repetitive DAX synthetic tests or unsolicited task cascade.

## Local complete deterministic reproducibility
Original full uploaded 88710-byte source ZIP is preserved BYTE-IDENTICAL nested within moderator-local evidence package (not the article PDF). Three independent executable scientific Python scripts, three frozen deterministic JSON results, source-data-only plot and code, full Polish report, README, SHA256SUMS and clean independent verifier.

Moderator-local full archive: IW_XH_S5_ROT012_SCHALL_ORIGINAL_PSN_SOURCE_NATIVE_REPRO_20261111.zip; exact 228390 bytes; SHA256 b46d43a8946491e2070a0d6e4d65d2518474fd53996a48b382dd541f85207719. 13 ZIP members; ZIP CRC PASS; 12 payload SHA256 PASS; clean extracted verifier runs ALL THREE independent programs and compares their JSON BYTE-IDENTICALLY PASS. Full local Polish report SHA256 20e33af42ac9e4f39debc48ff8a53018008f9c8cce65c784420473508c9fab42. GitHub science body is NOT upload of local binary source ZIP, plot or full Python code unless separately and explicitly verified.

Verdict: SOURCE_NATIVE_PSN_FIG2A_TO_FIG3A_REANALYSIS_PASS / HOLDOUT_PASS / GEOMETRY_NEGATIVE_CONTROL_PASS / ORIGINAL_SOURCE_BIN_LOCAL_CUSTODY_PASS / NO_ACTUAL_DEVICE_NOISE / EKS1_T1_COMPLETED_GAP001_M14_PENDING / DAX_MASSIVE_UNCUT_QED_OPEN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_UNVERIFIED / NO_AUTO_TASK_CASCADE.