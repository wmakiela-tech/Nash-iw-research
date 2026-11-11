# XH-S5 ROT013 — Schall original Source Data Fig3b→Fig3c: 14N hyperfine model selection and derivative-dependent PSN gate

DATE: 2026-11-11
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
RETURN_ID: XH-S5-ROT013-SCHALL-FIG3B-FIG3C-HYPERFINE-SOURCE-MODEL-SELECTION-DERIVATIVE-GATE_001_20261111
CLAIM_CEILING: ORIGINAL_PUBLISHED_SOURCE_DATA_REANALYSIS / OWN_ORIGINAL_HOLDOUT / NO_ACTUAL_DEVICE_TECHNICAL_NOISE / NO_MATH_OR_PHYSICS_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_UNVERIFIED

## Primary source / previous credit
F. Schall, L. Lindner, Y. Rottstaedt et al., "Laser-enhanced quantum sensing boosts sensitivity and dynamic range", Nature Communications 17:10825, published October 22 2026, DOI https://doi.org/10.1038/s41467-026-78386-z ; publisher article https://www.nature.com/articles/s41467-026-78386-z . Article Fig3b-c and Methods Eq15 explicitly use a sum of three Lorentzians for 14N hyperfine structure in each resonance. Author FIRST for this experimental source, XH-S5 ROT012 FIRST in this lineage for DIFFERENT Fig2a->Fig3a source replay. We analyze **Fig3b->Fig3c**, no attribution of author's known triplet or Eq15 to XH. Mature 14N NV ~2.16 MHz: American Journal of Physics 90:550 (2022) https://pubs.aip.org/aapt/ajp/article/90/7/550/2820145/ ; 2018 NV review https://pmc.ncbi.nlm.nih.gov/articles/PMC6187496/ .

Moderator-supplied original publisher-style complete Source Data ZIP: 41467_2026_78386_MOESM2_ESM.zip, 88710 bytes, SHA256 6f6fdf9b68a4f74144ccd9269de75a299ceeb326013e96863498f96eb11fcf5e, ZIP CRC PASS, byte-identical embedded in LOCAL ROT013 proof ZIP. No independent publisher-server identical-byte readback. Data/Fig3b.csv: 621 measured microwave frequency GHz vs laser output mW, scan 2.876 to 3.000 GHz step0.2 MHz; Data/Fig3c.csv: 621 identical frequencies, author-derived fitted-gradient PHOTON-SHOT-NOISE SENSITIVITY LIMIT fT/sqrtHz, global minimum 127.9498521773 at 2.9028 GHz. This is NOT real technical-noise-limited sensitivity or time-stamped signal.

## Independent source data math, explicit non-leakage
Source POWER Fig3b only fits; NO Fig3c used in training or scaling. Model three absorbing Lorentzian NV resonances with linear power baseline; each resonance modeled either as one unsplit line (11 parameters), three hyperfine lines **with equal amplitudes within the group** (12 parameters, OUR regularizing assumption, not attributed to authors), or three with nine free amplitudes (18 parameters). All model variants use center positions around 2.900, 2.936, 2.970 GHz and analytic power derivatives, and the 3x3 models fit a common hyperfine splitting. Photon shot noise Eq15 evaluated from analytic derivative:
eta_B = [h/(g_e mu_B)] sqrt(P_W * h*c/lambda)/abs(dP_W/dnu_Hz),
lambda=1042nm, g_e=2.0023, explicit GHz->Hz and mW->W conversions. Unlike Fig2a/3a (100 geometry), NO extra sqrt3 is applied to Fig3b/3c. NO fitting to Eq15 c-shell values or extra sensitivity multiplier.

Pre-fixed training = EVEN indices (311) of Fig3b power; held-out power = ODD indices (310). Target PSN validation = the SAME 84 ODD indices with **SOURCE-ONLY** Fig3c PSN<3000 fT/sqrtHz, no model-dependent exclusions. Data points in one instrument frequency sweep NOT independent physical trials. All predicted powers positive.

## Source-native results on held-out measured power and derived Fig3c PSN
MODEL ; held-out power RMSE mW ; held-out median absolute PSN rel-error ; PSN 90th percentile ; log PSN corr
- 3 x ONE Lorentzian ; 1.204967 ; 0.4185495 = 41.85495% ; 149.28927% ; 0.60134.
- 3 x (3 equal-amplitude hyperfine Lorentzians) ; 0.429797 ; 0.02058063 = **2.05806%** ; 7.12759% ; 0.997828.
- 3 x (3 freely weighted hyperfine Lorentzians) ; 0.383733 ; 0.03166714 = **3.16671%** ; 47.50349% ; 0.888980.

For this source/contract the equal-amplitude 3-line model improves holdout POWER RMSE over one-line by 64.33%, and improves the DIFFERENT target PSN median error by 95.08%. Freeing nine amplitudes improves power RMSE by 10.72% over equal-amplitude, but **worsens PSN median error by 53.87%**, supporting TARGET-RELATIVE model choice; lower intensity RMSE is insufficient for accurate differentiated sensitivity curve. This is NOT proof all freely weighted triplet models are wrong, not significance testing or new fundamental regularization theory. Source authors themselves use triplet line sums. The best fitted equal model PSN minimum 121.56476 at 2.9006 GHz, while the source curve minimum 127.94985 at 2.9028; **the 2.06% statistic applies to the FIXED 84-point window, NOT the best-minimum error**. Hyperfine spacing fitted 2.164866 MHz (equal), 2.159444 MHz (free), both in mature prior art 2.16 MHz range; NO NEW PHYSICAL SPLITTING.

## Genuinely independent methods and a source-only negative control
Second source-specific script does NOT import first model code and fits the ODD 310 rows with independent scipy.optimize.curve_fit Levenberg-Marquardt; holds out EVEN 311 rows and evaluates 87 SOURCE-ONLY PSN<3000 rows. Derivative uses complex-step method verified against five-point centered difference at 2.395e-10 max relative difference. Results: power RMSE .4291231 mW, PSN median error **2.30164%**, 90p 11.56357%, triplet splitting 2.164779 MHz. Direct nonparametric inverse-power peak finder finds 9 troughs in three groups (2.898/2.900/2.9022; 2.934/2.936/2.938; 2.9682/2.970/2.972 GHz), not misinterpreted as true pure line centers.

THIRD independent source-only target falsifier: replace analytic fitted spectrum derivative with numerical derivative of RAW measured noisy Fig3b power: median PSN absolute rel-error 18.655% in fixed 84-point source window. Pre-chosen Savitzky-Golay cubic filters width7/11/21/41: med errors 22.514%,18.844%,23.207%,42.124%. These are NONOPTIMIZED deliberately fixed ablations. Proof that actual measured intensity noise differentiation is more fragile than fitted differentiable model for this dataset, not sensor time-noise PSD or a new noise theorem.

## Custody / exact replay
MODERATOR LOCAL FULL REPRO:
IW_XH_S5_ROT013_SCHALL_HYPERFINE_DERIVATIVE_SOURCE_NATIVE_REPRO_20261111.zip
458571 bytes; SHA256 b0e4851ec694053b894ef8b37094bd9ad05dc7d8e83b46bada7631c5c2baf8e7.
Contains exact original 88710-byte published ZIP nested, Polish report, 3 independent scientific scripts, 3 frozen deterministic JSON, source-only plot generator + 2 original-data figures, environment versions, README, SHA manifest and standalone replay verifier. ZIP CRC PASS, all **14** manifest content SHA256 PASS, clean isolate EXTRACTION and execution all THREE scripts JSON BYTE-IDENTICAL PASS. Full Polish report SHA256 6e988c327248c7c22b43eb281e396d0c4da7c1d126862b7e84955fe76fc00849. This PUBLIC Github science report is NOT a binary upload of complete local original ZIP or executable scripts. The local bundle includes full code and source data. Independent exact original publisher-server binary attestation NOT claimed.

## Cross-cell currentness and STOP
EKS1 ROT004 ACK'ed source ZIP T1 completion and GAP001 confirmed: the complete provided Schall Source Data has ZERO time series / Allan / measured technical-noise PSD / measured drift sheets. ROT013 never supplies temporal data; M14 temporal polynomial/calibration abstract theory remains mathematically conditional, NOT empirically supported by THIS source without separate time-source. In last inspected Slack, no owner disposition closure recorded for GAP001; no new XH task. DAX-S8 ROT009 acknowledged XH-S5 ROT011 source-contact; native massive uncut gamma gamma->e+e-e+e- generator has still NOT been run by XH. DAX owns QED science; no transfer of this NV replay to R68. No task cascade.

STATUS: ROT013_SOURCE_NATIVE_REANALYSIS_PASS / TARGET_RELATIVE_MODEL_SELECTION_PASS / INDEPENDENT_REVERSE_HOLDOUT_PASS / RAW_DERIVATIVE_NEGATIVE_CONTROL_PASS / CLEAN_ZIP_REPLAY_PASS / NO_MEASURED_SENSOR_NOISE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_INGEST_UNVERIFIED.
