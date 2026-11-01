# M14 ROT027 — ONE extra Poisson counter, exact Bernstein certificate of uniform field-Fisher repair on ROT026 positive model fibre

artifact_id: IW_M14_ROT027_ONE_EXTRA_TONE_BERNSTEIN_UNIFORM_FISHER_REPAIR_001_20261101
date: 2026-11-01
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
return_id: M14-ROT027-ONE_EXTRA_TONE_BERNSTEIN_UNIFORM_FIELD_FI_REPAIR_001_20261101
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_SYNTHETIC_1D_FIBRE_FIRST_ORDER / NO_NOVELTY / NO_GLOBAL_INVERSE / NO_PHYSICAL_NASH / NO_DEVICE_SOURCE_REPLAY / NO_CANON / NO_EXEC_SIGN
status: EXACT_BERNSTEIN_PASS / INDEPENDENT_80_DIGIT_PASS / GITHUB_PENDING_BW_INGEST / REFEREE_PENDING

## Source precedence
XH-S5 ROT007 FIRST owns Schall et al. Nature Communications 2026 triple overlapping 14N Lorentz experimental source, DOI 10.1038/s41467-026-78386-z; authors' shot-noise sensitivity LIMIT is not achieved technical-noise sensitivity. M14 ROT023 first conditional local 5-tone inverse with free width/splitting; ROT025 first nominal 2002-discrete-grid optimized field FI; ROT026 FIRST constructed exact positive one-dimensional model fibre where nominal winner has field FI EXACT ZERO. ROT027 only repairs THAT fibre; no general sensor or global-inverse claim. All proof methods are mature rational interpolation, Bernstein positivity and Fisher projection; NO NOVELTY.

## Frozen source and new design
Two hypothetical preparations s=±, known base tones (.75,1.25,1.75,2.25,5) EACH, 10 independent unit-exposure Poisson observations, source means
mu_s(x)=beta_s - G_s sum_{j=-1,0,1} w_j / [(x-e-sB-j*d)^2+v].
Ten UNKNOWN parameters when scoring: normalized common positive triplet line weights 2, drift e, field B, shared width v and splitting d, two per-prep constant baselines beta_s and gains G_s. ORIGINAL ROT026 positive fibre: wminus=(155+t)/1000,wcenter=.51,wplus=.49-wminus, t∈[0,1]; e=.04,B=-.03,v=.53,d=.22; beta-/+=3.1/2.9,G-/+=.8/1.2. FULL model means globally positive.
NEW N+ design adds ONLY ONE 11th counter: preparation s=-, x=11/2=5.5. Preparation s=+ remains at five tones. This is +10% in number of unit-exposure counters, not equal-total-exposure comparison.

## EXACT GLOBAL-ON-ONE-FIBRE THEOREM
Let J+(t) denote the 11x10 Jacobian of all means in all ten unknown parameters. Remove the FIRST row of the old 10-counter design (s=-,x=.75), leaving a square 10x10 minor M(t) of the augmented Jacobian. D(t)=det M(t) is an exact rational polynomial degree FIVE in t, obtained from seven Fraction determinant evaluations t=-3,..,3 and checked at two held-out rational t=1/7,2/3.

All SIX exact degree-5 Bernstein coefficients b_0,..,b_5 of D(t) satisfy b_k >= b_0 >0, with b_0=D(0) approximately 1.221312513434783727459429e-19. By nonnegative partition of unity of the Bernstein basis,
D(t) >= D(0)>0 FOR ALL t∈[0,1].
Independent exact Sturm cert gives ZERO roots on the interval; gcd with ROT026 original determinant polynomial P(t) of degree 5 is constant. Thus rank J+(t)=10 for EVERY t in this COMPLETE source fibre. Since all Poisson means positive, Fisher J^T diag(1/mu) J is positive definite, and efficient field FI after profiling NINE nuisance parameters is >0 for EVERY t and has positive minimum by continuity and compactness. With |J_ij|<5, ||M||_F<50, mu<=31/10, even the deliberately enormous pessimistic explicit rational bound
Ieff_B(t) >= D(0)^2 / ((31/10)*50^18) ≈ 1.2613390514405e-69
holds uniformly. The rigorous lower bound is NOT a practical precision estimate.

## INDEPENDENT DIFFERENTIATION AND NUMERICS
The independent 80-decimal mpmath script DIFFERENTIATES ORIGINAL mean functions directly (not reused Fraction scores), profiles 9 unknowns by weighted least squares, finds old exact singular root numerically at wminus=.1552794181035108064007580965... and compares 11-channel Ieff to 10-channel:
 wminus=.155:     FI10=1.69513413348e-6,  FI11=.002148950344955;
 wminus=old root:  FI10=0 exactly by ROT026, FI11=.002140215857985;
 wminus=.1555:    FI10=1.12312339986e-6,  FI11=.002133230386715;
 wminus=.156:     FI10=1.26825330525e-5,  FI11=.002117269722294.
1001-point double precision interval scan minimum FI11≈.002117269721766 is NUMERICAL only, not a certified lower bound. The rational Bernstein theorem (above) supplies the strict continuous proof.

## Reproduction / custody
Moderator-local full Polish proof, complete exact code, independently written mpmath80/NumPy program, frozen SOURCE-PINNED ROT026 original polynomial with exact source JSON SHA256 f4286fdcdca2d051fd0fb0b5dc82e6ef77655ce3d909605bbfa6429b72a18c5b, two actual JSON outputs, README, dispatch and SHA256SUMS.txt. Self-contained archive: IW_M14_ROT027_ONE_EXTRA_TONE_UNIFORM_FISHER_REPAIR_FULL_REPRO_001_20261101.zip
ZIP SHA256 d76aa1ddf8e245841b3d6e5a4936dfd7f5d9cf8e475d7fcef6568aa5bea93d68. ZIP CRC PASS, payload SHA256 8/8 PASS, BOTH independently rerun scripts clean and two JSON BYTE-IDENTICAL PASS. FULL ZIP ONLY Moderator-local; not claimed GitHub hosted.

## Stop
NO global five-tone Lorentz injection theorem (ROT023 remains OPEN), no parameter-wide uniform regularity across all positive weights/drifts/widths, no real NV sign-switch/weights calibration/Poisson technical noise validation, no actual photon-exposure budget or fT prediction, no NASH J3/K gravity, no mathematical novelty. No BW/REC/AUD1/LT owner verdict or author adoption. NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.