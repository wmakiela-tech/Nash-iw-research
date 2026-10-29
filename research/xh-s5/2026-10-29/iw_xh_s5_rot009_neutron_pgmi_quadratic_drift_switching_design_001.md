# XH-S5 ROT009 — neutron PGMI source-mass differential phase: exact ABBA quadratic alias and six-shot design
artifact_id: IW_XH_S5_ROT009_NEUTRON_PGMI_PHASE_DRIFT_DESIGN_20261029
return_id: XH-S5-ROT009-NEUTRON-PGMI-QUADRATIC-DRIFT-DESIGN-001_20261029
date: 2026-10-29
source_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: CURRENT_PRIMARY_REVIEW / EXACT_MATURE_POLYNOMIAL_DRIFT_FINITE_DESIGN / EXECUTED_STDLIB_FRACTION_AND_NUMPY_MONTE_CARLO / NO_SOURCE_PGMI_MONTE_CARLO_REPLAY / NO_NOVELTY / NO_NASH_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## ORIGINAL SOURCE FACTS
Kapahi, Sarenac, Heacock et al., "Design and Monte Carlo simulation of a phase grating moire neutron interferometer to measure the gravitational constant", Communications Physics, published 15 October 2026; DOI https://doi.org/10.1038/s42005-026-02853-8 ; FULL original preprint HTML https://arxiv.org/html/2505.00170 (first posted Apr 2025). SOURCE proposal (NOT completed G measurement) of a polychromatic three-phase-grating neutron interferometer (3-PGMI) with 150 parts-per-million TARGET uncertainty, split 130 ppm statistical and 73 ppm combined systematic. Table 2 items include mean grating period 58 ppm, mean wavelength 40 ppm, Sagnac phase 10 ppm, lunar gravity 1.7 ppm, atmospheric effects 2.7 ppm. SOURCE uses source-mass vs null-phase measurements, models changing atmosphere and lunar potentials and proposes external X-ray alignment monitoring. This XH return does NOT claim authors neglected drift or that an experimental 150 ppm result exists.

CRITICAL DOMAIN BOUNDARY: Original source Eqs.10–12 infer effective fringe phase from a polychromatic, multipath nonlinear INTENSITY mixture and do NOT merely average single-neutron phases. XH computes a separate scalar effective-phase regression toy, NOT author's WKB/Monte Carlo neutron quantum forward model, geometry, laser/beam-count noise, or real-data replication.

## MATURE PRIOR ART — PRIORITY SUBTRACTION
Swanson & Schlamminger (2010), "Removal of zero-point drift from AB data and the statistical cost", Meas Sci Technol 21:115104, DOI https://doi.org/10.1088/0957-0233/21/11/115104, arxiv:1009.1894 — establishes ABBA linear drift cancellation and polynomial drift correction. NIST metrology handbook https://itl.nist.gov/div898/handbook/mpc/section3/mpc3312.htm ; NIST drift eliminating designs https://pmc.ncbi.nlm.nih.gov/articles/PMC4909179/ . Neutron 3-PGMI demonstrated earlier in Sarenac et al., PRL120 (2018) 113201 (2021 NIST page https://www.nist.gov/publications/three-phase-grating-moir19e-neutron-interferometer-large-interferometerarea). NO mathematical novelty or claim that the proposed 6-point pattern is a novel design-method theorem. NASH public keyword searches PGMI / neutron interferometer / ABBA / phase drift returned no indexed hit, NOT exhaustive of private context.

## PREDEFINED SYNTHETIC MODEL
A=no mass, q=0; B=mass in, q=1. At equally spaced timestamps (normalized units t = odd integers), assume extracted phase:
Y_i = phi0 + alpha*t_i + kappa*t_i^2 + S*q_i + noise_i,
with E noise=0 and independent homoscedastic Var(noise_i)=sigma^2. S would be related to G only under external calibrated neutron phase/source-mass assumptions not executed here. All controls SOURCE-MOTIVATED only.

Let D=[ones,t,t^2], r=(I-P_D)q. If r!=0 then minimum variance linear unbiased signal estimate S_hat=(r dot Y)/(r dot r) and Var(S_hat)=sigma^2/(r dot r). If r=0, exact alias: no source/phase contrast identifiable with arbitrary quadratic nuisance. No further theorem priority claimed.

## RESULT 1 — EXACT 4-POINT ABBA NO-GO
t=(-3,-1,1,3), q=(0,1,1,0). Identity q=(9-t^2)/8 at every observation. Thus source column in nuisance span; rank([1,t,t^2,q])=3, S unidentifiable. Observations y=(0,1,1,0) arise BOTH from S=1, all nuisance zero AND from S=0, intercept=9/8, quadratic coefficient=-1/8, no linear drift. These worlds generate the same full data likelihood under any common additive measurement-noise law. More bits, replicates at same 4 positions do not resolve unknown quadratic component.

The CLASSICAL standard ABBA contrast [-1/2,1/2,1/2,-1/2] cancels intercept + linear drift, but if quadratic coefficient kappa is free, E[estimate]=S-8*kappa. For a purely illustrative conditional 150 ppm relative signal allowance, |kappa/S|<150e-6/8=18.75e-6 in normalized time units. This is NOT a measured instrument drift or a quantified correction to the source's proposed uncertainty budget.

4-point ABAB has nonzero Fisher information after profiling degree2 nuisance: r'r=4/5 and Var(S_hat)=5/4*sigma^2, under the same independent noise model.

## RESULT 2 — EXACT 6-POINT BEST BALANCED SWITCHING IN SPECIFIED CLASS
All 20 patterns of six equally spaced readings with exactly three B and three A were enumerated with Python Fraction arithmetic. t=(-5,-3,-1,1,3,5). Maximum profiled r'r=52/35, attained EXACTLY and ONLY by ABBAAB and its inverse BAABBA. For ABBAAB:
 S_hat=(-15*Y1+19*Y2+18*Y3-18*Y4-19*Y5+15*Y6)/52.
Weights w=(-15,19,18,-18,-19,15)/52 obey sum w=0, sum wt=0, sum wt²=0 and sum wq=1 EXACTLY. Var(S_hat)=35/52*sigma^2 = .6730769231*sigma^2. For 6-point ABABAB Var=35/48*sigma^2; six-point ABBAAB strictly improves at same per-reading noise. This is not optimization of total beam time, mechanical settling, neutron counts, source geometry, wavelength drift, correlated noise or source-motion hysteresis.

Critical negative knowledge: weights are antisymmetric, kill all even-order time polynomials, and cubic moment sum wt^3=672/13. Hence unmodeled cubic coefficient c3 induces bias (672/13)c3. Degree2 robustness != all-order drift immunity.

## EXECUTED INDEPENDENT CONTROLS
Program A xh_s5_rot009_exact.py (only Python stdlib): Fraction exact matrix inversion, full C(6,3)=20 enumeration, optimal solution uniquely {ABBAAB,BAABBA}, ABBA source-no-source identical observations, ABAB comparator, constraints, polynomial moments, illustrative slow-harmonic response. PASS.
Program B xh_s5_rot009_independent.py (independent numpy least squares+rank): repeats complete exhaustive search and verifies contrasts. 80,000 Gaussian mock observations in each of 3 synthetic controls, random seed20261029; sigma=.1 phase units. Six-point predicted std=.0820412654, observed .0819084727. With injected cubic c3=.0002 predicted mean S_hat=1.0103384615 for true S=1, observed 1.0101810741. Four-point ABAB predicted std=.1118034, observed .1114732. All checks PASS.
Illustrative 12h sinusoidal generic additive phase nuisance, observations every 10 minutes (normalized time unit5min), maximum transfer gain into estimated source S: standard 4-point ABBA .0076033602 per unit nuisance amplitude, six-point ABBAAB .00071355445. With purely hypothetical nuisance amplitude=0.1*S this means 760.34 vs 71.36 ppm relative bias. 24h generic harmonic factors .001903104 vs .0000893947. THIS IS NOT lunar ephemeris or source tidal potential computation; the source already models lunar gravity and its spatial orientation.

## REAL EXPERIMENT FALSIFIER (NOT EXECUTED)
Pre-register source-mass inserted/removed block schedules ABBA, ABAB, ABBAAB and BAABBA; randomize complete block order, vary cycle length, measure phase-extraction drift and source switching transients, retain raw polychromatic fringe intensities, x-ray alignment signal, grating-period and neutron-spectrum monitoring and independent moon/atmospheric environmental references. Held-out nuisance traces test common polynomial assumption, detector correlation and hysteresis. Then compute source-native path-integral phase and G transfer with source mass geometry. An unsuccessful toy drift fit falsifies only the *assumed* nuisance family, NOT Newton's constant or evidence for modified gravity.

## CUSTODY
Full local Moderator reproducibility ZIP: IW_XH_S5_ROT009_NEUTRON_PGMI_DRIFT_IDENTIFIABILITY_REPRO_20261029.zip
ZIP SHA256 f6e3f2d1b22418026e6f4d05e248d82f09dec2a24658f543bfba91480173e176.
Local complete markdown SHA256 f7e8c37a57cd63b5aa5d186e87ec2a2652f12ee56742ba12fd6d9d464e78d9b7.
Exact standalone Python SHA256 a88978775cafa5bf07ae01771b8a9754d5db347d4352f7e6a8e69c8680cd3eda.
Independent NumPy/SciPy Python SHA256 6a5d0f94b8eb0cad85f63e97ba2640faf0164f8f7e5c84888db4fbe133333126.
ZIP archive verified CRC PASS, all member SHA PASS, extracted clean replay both scripts PASS and two output JSON files byte-identical PASS, Python3.13.5 / NumPy2.3.5 / SciPy1.17.0.
This public GitHub text is the substantive science, but full scripts/ZIP are LOCAL unless independently deposited and read back.

NO_SOURCE_DATA_OR_MONTE_CARLO_REPLAY / NO_NEW_GRAVITATIONAL_RESULT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED / NO_TASK_CASCADE.
