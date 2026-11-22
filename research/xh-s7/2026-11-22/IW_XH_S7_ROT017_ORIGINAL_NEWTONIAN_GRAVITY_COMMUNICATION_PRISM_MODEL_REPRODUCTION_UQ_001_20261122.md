---
artifact_id: IW_XH_S7_ROT017_ORIGINAL_NEWTONIAN_GRAVITY_COMMUNICATION_PRISM_MODEL_REPRODUCTION_UQ_001_20261122
date: 2026-11-22
lineage: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
exposure: PUBLIC
class: SOURCE_NATIVE_EXTERNAL_SCIENCE_HARVEST / ORIGINAL_PHYSICAL_EXPERIMENT / INDEPENDENT_NEWTONIAN_MODEL_NUMERICAL_REPRODUCTION / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE
execution: ORIGINAL_AUTHOR_SUPPLEMENT_MODEL_INDEPENDENTLY_EXECUTED / QUADRATURE_ORDER_CONVERGENCE_PASS / 4000_DRAW_GEOMETRY_PROPAGATION_EXECUTED / ASCII_FRAME_EXACT_PASS / ORIGINAL_GRAVIMETER_RAW_BYTES_NOT_READ
claim_ceiling: MODEL_ONLY_NOT_EXPERIMENTAL_DATA_REPLAY / NO_EXPERIMENTAL_REPLICATION / NO_QUANTUM_GRAVITY / NO_GW_RADIATION_DETECTION / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# ROT017 — Actual independent scientific model calculation for newly published gravitational communication, UQ / Science Advances

**Moderator intent:** single-letter O, continue autonomous XH-S7 rotation. Standing explicit instruction: "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji" (external science survey and function, not internal B1/BBN numerical job). ROT015–016 covered original MOFGen computational chemistry source. ROT017 returns to high-value original REAL physical instrument data with independently executable precise physics target and sharp epistemic scope.

## 0. Original source publication, provenance and status

Andrew J. Groszek, Charles W. Woffinden, Michael D. Harvey, Andrew G. White and Matthew J. Davis, **"Unblockable communication with gravity"**, *Science Advances* **12(47) eaee0802**, DOI https://doi.org/10.1126/sciadv.aee0802 , first published online **18 Nov 2026**, journal issue data **20 Nov 2026**; authoritative PubMed https://pubmed.ncbi.nlm.nih.gov/43050522/ . DOI and bibliographical dates checked 22 Nov.
Original authors' primary complete technical manuscript plus supplement: **arXiv:2511.16710v1**, first posted **20 Nov 2025**, full primary text and supplement directly read from https://arxiv.org/pdf/2511.16710 . Web rendered screenshot p3 of 11-page PDF actually available: figure 4's 49-bit gravity trace, corrected for drift and tide, and original table I were visually inspected; screenshot p0 and p7/p8 attempts returned CACHE MISS. Source actual technical PDF text still usable for model source geometry from Supplement section II and III; do NOT claim every PDF figure individually verified. Primary journal full-text endpoint was inaccessible but PubMed original journal abstract verified. Original author UQ institution press release: https://news.uq.edu.au/2026-11-uq-researchers-send-unblockable-message-using-gravity published **19 Nov 2026**; press publicity is NOT the physics source.

**FIRSTNESS:** Nov 2026 is peer-reviewed journal publication, not first public report of the proof-of-principle (preprint was 2025). Authors say first communication with gravity; do not claim first force-gravity measurement or first demonstration of Newtonian gravity, gravimeters, gravity communication proposals or new graviton physics. Mature prior art includes Newtonian inverse-square field, experimental gravimetry, 2012 neutrino communication (Stancil et al Mod Phys Lett A 27,1250077), mass-coupling gravitational measurements (Westphal et al Nature 2021 DOI https://doi.org/10.1038/s41586-021-03250-7 , and Fuchs et al *Measuring gravity with milligram levitated masses*, Science Advances 2024 DOI https://doi.org/10.1126/sciadv.adk2949). Closest specialist = this authors' Nov 2025 preprint and Nov 2026 experiment. Prior theory proposes graviton or gravitational wave communication, but this is **near-field QUASI-STATIC gravitational acceleration**; compare same observable, not gravitational wave emission.

## 1. Author-reported ACTUAL experiment (not remeasured by XH)

University of Queensland 1950s elevator counterweight mass 1800 ±200 kg moves between COM z0=0.39±0.06 m and z1=5.80±0.06 m above a fixed **classical spring-based LaCoste & Romberg model D relative gravimeter**, laterally separated x=0.56±0.03 m and y=0±0.05 m. Shortest geometric range to COM 0.68±0.04 m. Physical brick wall between masses/sensor (wall thickness 0.27±0.02 m). Sensor records only vertical component g_z, with ~1.9Hz acquisitions, nominal digital resolution 10 nm/s², a 40s device lowpass, and experimental ~2 nm/s² sensitivity after ~30 seconds averaging. Original authors report ∆g_z model **50±15 nm/s²**. Correction for Earth tides and instrument drift. Typical observed two-level change ≈50 nm/s²; bit threshold at 25 nm/s², averaging last 25s of each one-minute period.

Message transmitted **"Gravity" = 49 7-bit ASCII data bits**, encodes `1000111 1110010 1100001 1110110 1101001 1110100 1111001`; two additional 7-bit 1010101 framing sequences (7 before +7 after), overall 63 bit windows, with approx 25s elevator travel +10s settle +25s integration each, plus baseline before/after. Authors report exact recovery 49/49 bits and unaveraged bit flip ≈0.01, averaged ≈1e-9 **under Gaussian extrapolation**; 49 bits exactly correct DOES NOT prove actual raw bit error rate 1e-9. They claim channel capacity 2.4 bits/min for this setup (Shannon-type capacity estimator) vs achieved 1bit/min; idealized 5s elevator + better Scintrex yields ~15 bits/min forecast, NOT measured. Idealized 75t mass + ideal gravimeter + geometric alignment and tolerated low SNR yields projected ~500m range, NOT experimental reach. Key caution: "unblockable" is ordinary shielding-resistance, NOT active-jamming/spoofing resistance; authors explicitly discuss moving-mass interference, gravimeter vibration and intrusion.

## 2. Exact original scientific geometry and physically reproduced field integral

SOURCE technical original preprint Supplement II, III:
uniform-density rectangular prism / elevator counterweight
- volume dimensions `Lx=0.205±0.005m`, `Ly=0.82±0.01m`, `Lz=1.47±0.04m`;
- cast-iron density `rho=7300±200 kg/m³`, from measured instrument geometry rather than independent mass measurement;
- sensor to COM x=.56±.03m, y=0±.05m, z0=.39±.06m and upper z1=5.80±.06m; known relative travel 5.41m;
- Newton's G = 6.67430e-11 SI value fixed.

Independent XH model:
`g_z(zc)=G*rho*integral(xc±Lx/2) integral(yc±Ly/2) integral(zc±Lz/2) [z/(x²+y²+z²)^(3/2)] dz dy dx`;
`delta_g_z = g_z(z0) - g_z(z0+5.41m)`.

**Actual Python/NumPy 3D tensor-product Gauss–Legendre cubature independently IMPLEMENTED and EXECUTED in current session**, including 4,6,8,10,12,16,20,24,32 point each dimension convergence. Nominal outputs at order 32:
- derived cuboid mass `rho*Lx*Ly*Lz=1803.8811 kg` (consistent author 1800±200).
- lower COM `g_z(z0)=53.98053204625 nm/s²`;
- upper COM `g_z(z1)=3.575489540792 nm/s²`;
- source mass shift `delta_g_z=50.40504250546 nm/s²`.
- absolute error relative to **authors' model central value 50 nm/s²** is +0.405 nm/s², 0.81% of authors' rounded central, much less than ±15. This is a **strong numerical reproduction of finite-geometry source model**, not measured data replay or physical empirical remeasurement.
- quadrature order 16→32 stable at ~1e-7 nm/s². Code asserts absolute `|delta-50.40504250546|<2e-6 nm/s²`.

**Important physically sharp negative control**: Replacing SAME uniform cuboid with point mass at its COM (mass 1803.8811kg) gives `144.21757417 nm/s²`, a ratio `2.861...` versus finite source, a 93.8nm/s² overestimate. At ~0.7m from the middle of a 1.47m long cuboid the monopole far-field approximation is invalid. Authors' supplement Fig S4 explicitly recognizes and plots this near-field discrepancy. This is NOT a novel author error, but a rigorous choice of correct source geometry. It is why external source-native check must not substitute superficially equivalent `M,r` point model for 3D distributed source.

**Source uncertainty test** independently executed: Monte Carlo fixed NumPy default_rng seed `20261122`, `N=4000`, independent Gaussian draws for quoted rho, x/y COM, dimensions and common z0; z1=z0+5.41 so their common z uncertainty is correctly correlated; travel 5.41 not varied because source quote lacks numeric sigma for travel in this model. Model generated
- sigma of delta ≈`8.859353774446 nm/s²`;
- 2.5% and 97.5% percentiles approximately `[33.0585186244, 68.3406016491] nm/s²`;
- this is NOT the original authors' stated ±15 propagated physics uncertainty, because assumptions, source model error, gravitational background, instrumental/tide/drift, density shape uncertainty and potential parameter correlation are not fully represented. Smaller Monte Carlo sigma is NOT evidence that authors overstate error bars or that uncertainty "should be 8.86". This is narrowly an independent sensitivity study of specified input model.

**Encoding test** Python independently constructed 7-bit ASCII for "Gravity" from characters and checked exact equality with printed 49 bits (not re-decoded gravimeter readings). Framing windows ~63min at 1bit/min correspond to experiment duration but no raw trace decoded here.

## 3. Actual original author data archive — availability != bytes

The University of Queensland released original code and measurement files **30 April 2026**, dataset Woffinden/Groszek/Davis `Unblockable communication with gravity: code for reproducing figures`, DOI https://doi.org/10.48610/cd26dd2 . Exact public metadata https://researchdata.edu.au/unblockable-communication-gravity-reproducing-figures/4023470 enumerates **four reproduction scripts**:
1) gravitational mass dipole polar diagrams;
2) **RAW Lacoste-Romberg gravimeter data analysis decoding actual bits** (author stated original raw data exists);
3) finite-prism numerical source model vs counterweight vertical height;
4) optimize vertical source displacement for laterally offset single-axis gravimeter.

**Data availability**: source metadata/access status OPEN, UQ eSpace landing https://espace.library.uq.edu.au/view/UQ:cd26dd2, but web tool clicks eSpace and original DOI yielded cache miss or forbidden and runtime local requests had DNS disabled. **NO actual original data ZIP, time-series bytes or author scripts downloaded/read**. Therefore:
- model calculated from published parameters yes;
- independent original raw time-series decoding **NO**;
- claimed 49/49 correct bits / BER 1e-9 only author report, not confirmed;
- no accidental overclaim that public dataset being indexed equals data consumed or reproduced.
Data archive predates 2026 journal, not new raw deposit this week.

## 4. Literature foundation, scientific interpretation and NASH scope

This is **classical Newtonian gravity** near-field perturbation, consistent with GR weak-field stationary limit. It measures acceleration changes from moving mass across a brick wall, **NOT propagating gravitational radiation**, single-graviton detection, a quantum-gravity witness, instantaneous FTL signal or a fundamental new gravitational force. In general relativity field changes propagate causally; laboratory conditions are quasi-static and experiment does not test speed of gravity. No physical challenge to existing gravity theory. Gravimeter classical spring, not an implementation of quantum gravimetry even if prospect discusses future sensors.

Near-field geometry matters: naive point-source can miss the result by factor ≈2.86. This is a source-identifiable boundary for analogous scientific discussions in NASH; it does not produce NASH-specific theoretical firstness or a cross-cell physical bridge.

NASH methodological transfer is purely source-type architecture:
`THEORY_EQUATION_READ` vs `GEOMETRY_SOURCE_MEASUREMENTS_READ` vs `MODEL_SOLUTION_INDEPENDENT_RERUN` vs `RAW_INSTRUMENT_BYTES_READ` vs `INDEPENDENT_DECODE` vs `FUNDAMENTAL_GRAVITY_INTERPRETATION`.
Here only first three pass, fourth and fifth HOLD. Also *conditional* engineering forecasts cannot be reported as observed material claims. Any NASH reuse would require a quantitatively specified physical observable and independent method.

Mature foundational prior art: Newtonian integration and precision gravimetry; predecessor 2012 neutrino messaging, earlier gravity-coupling experiments. Nearest specialist source: authors' 2025 preprint and 2026 paper and source code UQ archive. The novelty of gravity source coding belongs to Groszek et al. Unblockable as a blanket cybersecurity guarantee would be false: gravity near-field can be actively spoofed or jammed, and bandwidth/range of actual apparatus strongly constrained.

## 5. Reproducible deliverables (current conversation mount)

**Actual created + executed Python original independent XH code**:
`/mnt/data/xh_s7_rot017_gravity_prism_reproduction.py`; 6616 bytes; SHA-256 `92e8381d66486de2f24d99c5ffb5d47f4941562a5941b88acf2d5100321ad7d4`; Python 3 + numpy. Exact geometry, integration and 4000 MC draws; running the script creates full receipt and convergence CSV in same directory. Normal Python source local code, not hidden tool output.

**Actual generated Python calculation receipt**:
`/mnt/data/xh_s7_rot017_gravity_prism_receipt.json`; 3528 bytes; SHA-256 `980f58df88a75f40a375e83355dde8a3783a155d19545ec812aeb02c4f2573b8`. Machine-readable all source parameters/units/raw-data gate, 4–32 order convergence, both g_z, propagated geometry MC, ASCII bit-string/frames and claim ceiling.

**Actual generated quadrature convergence CSV**:
`/mnt/data/xh_s7_rot017_gravity_quadrature_convergence.csv`; 580 bytes; SHA-256 `0bfdf62804d1b7fb5640122dfa0b04a1efbccc074516074c45ff8259120eacb5`.

No device code executed. No generic model-only calculations promoted to independent observation verification. No NASH run, no BW ACK, no physical novelty claim.

**Result verdict**:
`XH_S7_ROT017_NEW_ORIGINAL_SCI_ADV_NOV2026_SOURCE_PASS`
`SOURCE_2025_PREPRINT_DATE_SUBTRACTED_FOR_FIRSTNESS`
`FULL_ORIGINAL_3D_FINITE_PRISM_NEWTONIAN_FIELD_CALC_EXECUTED_PASS`
`NUMERIC_50P405_VS_AUTHOR_50P0_PLUS_MINUS15_PASS`
`POINT_SOURCE_NEARFIELD_144P2_DIFFERENCE_EXPLAINED`
`INPUT_GEOMETRY_MC_4000_SENSITIVITY_PASS`
`EXPERIMENTAL_RAW_GRAVIMETER_DATA_BYTES_NOT_READ_HOLD`
`ASCII_TEXT_VERIFIED_NOT_RAW_SIGNAL_DECODE`
`CLASSICAL_GRAVITY_ONLY_NO_QUANTUM_OR_GW_CLAIM`
`NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
