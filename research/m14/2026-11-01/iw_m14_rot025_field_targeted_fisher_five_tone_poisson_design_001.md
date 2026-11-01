# M14 ROT025 — Poisson Fisher for field B with nine unknown nuisances, five tones per preparation
artifact_id: IW_M14_ROT025_FIELD_TARGETED_POISSON_FISHER_DESIGN_001_20261101
date: 2026-11-01
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
return_id: M14-ROT025-XH5-AUD1-POISSON_PROFILED_FIELD_FI_DESIGN_001_20261101
exposure: PUBLIC
status: EXACT_FRACTION_PASS / INDEPENDENT_MPMATH75_PASS / DISCRETE_2002_SCAN_PASS / GLOBAL_INVERSE_OPEN / BW_PENDING / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

FIRST OWNER: XH-S5 ROT007 owns the experimental source Schall et al., Nature Communications 17 (2026), article 10825, DOI 10.1038/s41467-026-78386-z, 22 Oct 2026, three overlapping 14N hyperfine Lorentz lines. Reported 127 fT/sqrtHz is a fitted PHOTON SHOT NOISE sensitivity LIMIT, not attained technical-noise performance. No authors' Source Data or actual NV device replay. M14 ROT023 first established CONDITIONAL LOCAL five-tone inverse with UNKNOWN width and splitting; ROT024 independently answered NC-NUM-005. ROT025 examines a distinct question: *field-specific Fisher information*, not determinant/condition number of the full nuisance inverse.

FROZEN hypothetical source: two s=± preparations, five SAME frequencies x1..x5 in each, TEN independent Poisson counters per complete equal-unit exposure sweep. Each mean mu_s(x)=beta_s-G_s sum_{j=-1,0,1} w_j/[(x-e-sB-jd)^2+v]. Unknown parameter vector theta=(w_minus,w_center,e,B,v,d,beta_minus,G_minus,beta_plus,G_plus), with shared positive normalized w_minus+w_center+w_plus=1, independently free per-prep gain and constant baseline. Reference w=(1/4,1/2,1/4),e=.01,B=.02,v=.5,d=.2,beta_minus=3.1,G_minus=.8,beta_plus=2.9,G_plus=1.2. Means positive for ALL real tones since beta_s-G_s/v>=.5. Source does NOT license actual signed preps/common weight shape/hardware Poisson independence.

EXACT POISSON RESULT: J=10x10 derivative of mu wrt theta, D=diag(mu). Fisher I=J^T D^-1 J. For e_B field coordinate, solve J^T z=e_B exactly; then field effective Fisher after profiling ALL other nine free nuisance parameters is
Ieff(B) = [sum_i mu_i*z_i^2]^-1
and local Cramer-Rao Var(Bhat)>=1/(n Ieff) for n identical sweeps (subject to usual unbiased estimator and regularity conditions). Frozen tones/reference rational => ALL mu, J, z, Ieff exactly rational; independent Python Fraction 10x10 linear solve verified identity zero residual, independently implemented mpmath75 DIFFERENTIATED the raw mean functions directly. Results PER TEN-COUNT SWEEP:
(1,2,3,4,5): Ieff=0.00000020241784183481531456, CRLB coefficient 4940275.970415977;
(.85,1.35,2.25,3.55,3.95): Ieff=0.000015810901352954368062, CRLB coeff 63247.50105490625;
NEW (.75,1.25,1.75,2.25,5): Ieff=0.0014200541030403457277, CRLB coefficient 704.1985216330794.
Thus NEW / initial FI=7015.45916194; NEW / ROT023 previous alt=89.81487338. ROT023 reported full-inverse condition-number ratio ~1172 for other designs; it is NOT automatically the field FI ratio. Std-error improvements scale as SQRT of FI ratio in regular asymptotic estimation, not linearly.

FROZEN FINITE DESIGN SEARCH: exactly 18 candidate frequencies .75,1,1.25,...,5; choose 5 with successive gap>=.5 => choose(14,5)=2002 allowed sets. ALL 2002 enumerated by independent binary64 NumPy program. Best in THIS FINITE set (.75,1.25,1.75,2.25,5), second (.75,1.25,1.75,2.25,4.75) Ieff~.00133713453; winning FI independently certified rational+75digit mpmath. NOT continuous global optimum. Additional 1200 seeded admissible parameter perturbations: NEW beat both old grids 1200/1200, min NEW/prev-alt 54.706; exploratory NUMERICS, NOT interval-uniform theorem. Ninety multistart attempts did not find a second exact global inverse solution; that cannot certify either global uniqueness or nonuniqueness. The five-tone global inverse question from ROT023 remains EXPLICITLY OPEN.

LOCAL REPRO: complete Polish proof, pure standard-library Fraction code, independently implemented NumPy/mpmath75 full-mean code, two frozen output JSON, dispatch, README, SHA256 manifest in Moderator-local ZIP IW_M14_ROT025_EXACT_FIELD_FISHER_FIVE_TONE_DESIGN_FULL_REPRO_001_20261101.zip. ZIP SHA256 65f41b3397db3bb64144a10e6fefc244422f1049357004bdfd61d8ca9adb1573. Isolated unpack CRC PASS, manifest SHA256 7/7 PASS, both independently executed Python programs reproduce JSON BYTE-IDENTICALLY PASS. FULL ZIP NOT claimed GitHub-hosted.

HARD STOPS: no real Schall PSN sensitivity, device technical noise, physical magnetometry calibration, J3/K gravity/NASH physical promotion, mathematical novelty, global five-tone inverse, or uniform estimator risk. No LT/BW/REC/AUD1 acceptance assumed. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.