# M14 ROT028 — calibration-aware field Fisher: one uncalibrated counter fails, two with one shared offset repair

artifact_id: IW_M14_ROT028_CHANNEL_OFFSET_AND_TWO_COUNTER_FISHER_REPAIR_001_20261102
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
date: 2026-11-02
return_id: M14-ROT028-EXTRA_CHANNEL_OFFSET_CALIBRATION_AND_TWO_TONE_FISHER_REPAIR_001_20261102
claim_ceiling: EXACT_CLASSICAL_SYNTHETIC_1D_FIBRE_FIRST_ORDER / NO_NOVELTY / NO_GLOBAL_INVERSE / NO_SOURCE_DEVICE_REPLAY / NO_PHYSICAL_NASH / NO_CANON / NO_EXEC_SIGN
status: EXACT_BERNSTEIN_PASS / INDEPENDENT_MPMATH85_PASS / BW_PENDING / REFEREE_PENDING

FIRST: XH-S5 ROT007 owns actual Schall 2026 Nature Communications DOI 10.1038/s41467-026-78386-z 14N three-overlapping-Lorentz experimental source. Its photon-shot-noise sensitivity LIMIT is NOT achieved device technical-noise sensitivity. M14 ROT026 FIRST certified exact field-Fisher fold on a positive 1D fibre of the 10-counter nominal design. M14 ROT027 FIRST proved that ONE ADDITIONAL KNOWN-CALIBRATION sign-minus x5.5 Poisson counter restores full rank on that fibre. ROT028 audits the load-bearing *new channel offset calibration*: mature Poisson FI/nuisance-projection/Bernstein algebra, no new mathematics.

MODEL: Hypothetical preparations s=± and source mu_s(x)=beta_s-G_s SUM_j w_j/((x-e-sB-jd)^2+v). Original ten unknowns theta=(w_minus,w_center,e,B,v,d,beta_minus,G_minus,beta_plus,G_plus). Shared normalized strictly positive triplet relative weights; gains and per-prep baseline unknown, constant on original five tones. Base five tones (.75,1.25,1.75,2.25,5) PER prep = 10 unit-exposure Poisson counts. Original ROT026 strict positive fibre: w_minus=(155+t)/1000,w_center=.51,w_plus=.49−w_minus,t∈[0,1],e=.04,B=−.03,v=.53,d=.22,beta−/+=3.1/2.9,G−/+=.8/1.2. All-real-frequency means positive.

THEOREM 1 EXACT NEGATIVE: Add ONE s-minus x=5.5 counter but permit ONE otherwise unconstrained additive offset eta affecting ONLY that added reading, NOT original five s-minus readings. Jacobian of 11 counts and 11 parameters (theta,eta) is [[J10,0],[r_5.5,1]]. Profiling eta projects out the entire new observation, leaving EXACT same efficient Fisher about B as original J10. At ROT026 algebraic fold t*=.279418103510806400758..., I_eff_B(10)=I_eff_B(11,one-new-eta)=0 EXACTLY. Two independent free offsets on TWO new observations similarly project out both. This is a per-extra-measurement calibration cost, not an unknown original shared per-preparation baseline (already beta_minus).

THEOREM 2 EXACT POSITIVE: Add TWO s-minus counters x5.5 AND x6, with ONE common UNKNOWN additive eta affecting BOTH new observations. Total 12 Poisson counts, 11 unknown parameters (10 original + eta). Select eleven Jacobian rows: nine old (delete original first s-minus x=.75) and both extras; 11x11 determinant equals (up to orientation) D(t)=det([nine old 10-dimensional rows ; r_6-r_5.5]). D(t) is EXACT rational degree-5 polynomial; interpolation from t=-3,...,3 with independent heldout Fraction values t=1/7 and 2/3. All SIX exact degree-5 Bernstein coefficients b_k satisfy b_k<=b_0<0, hence for ALL t∈[0,1], D(t)<=D(0)<0 and |D(t)|>=|D(0)|≈1.3338143080061883e−19. Independently exact Sturm root count ZERO. Therefore rank J12(t)=11 throughout entire strict-positive frozen fibre; full 11-parameter Poisson Fisher positive definite, field efficient FI after profiling TEN nuisance directions strictly positive and has positive minimum by compactness. Extremely pessimistic but exact uniform bound Ieff_B>=D(0)^2 / ((31/10)*55^20) ≈8.944895268095969e−74 (NOT practical precision).

INDEPENDENT: mpmath 85-digit independently DIFFERENTIATES RAW photon means and profiles nuisance via weighted least squares; independent NumPy COMPLEX-STEP derivative 201-point scan PASS. At original fold:
  original ten channels field FI = ZERO EXACT (independent numeric ≈1.4e−147);
  11 channels with unknown new eta = ZERO EXACT;
  ROT027 11 with known new eta field FI ≈.002140215857985;
  12 channels with SHARED unknown eta field FI ≈.001785678487494;
  12 channels with separate unknown offsets each = ZERO EXACT.
At wminus=.155,.1555,.156, shared-eta 12-channel FI ≈.001780198831,.001789604727,.001797342290. These are corroborating points only; uniform theorem is exact Bernstein. Added two counters mean +20% unit exposures versus original ten, NOT equal total observation time.

LOCAL REPRO: Polish full report, Fraction+SymPy complete exact checker, separate mpmath85+NumPy checker, two frozen JSON, README, dispatch, SHA256 manifest in Moderator-local ZIP IW_M14_ROT028_CALIBRATION_AWARE_TWO_COUNTER_FISHER_REPAIR_FULL_REPRO_001_20261102.zip. ZIP SHA256 bfb33d76a469499457956e8f1a1badd48d759ea9228683cd232954bb726c887b, CRC PASS, payload SHA256 7/7 PASS, both scripts clean isolated re-execution JSON BYTE_IDENTICAL PASS. ZIP is LOCAL, not automatically present on GitHub.

SOURCE STOP: Original Schall data not downloaded/fitted, two physical opposite-sign preparations, per-channel calibration, Poisson independence and technical noise NOT validated on real hardware. No real fT sensitivity, no global 5- or 6-tone Lorentz inverse, no uniform result beyond exact fibre, no NASH gravity/J3/K mechanism, no novelty, no canon, no EXEC. BW/REC/AUD1/LT owner acceptance PENDING. NO_NEW_TASK_CASCADE.