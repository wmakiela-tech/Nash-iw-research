---
artifact_id: IW_XH_S7_ROT013_NOV2026_QUANTUM_FIELD_ANALOGUE_M87_CLOSURE_QUANTUM_ADC_SIC_SPIN_DATA_EXTERNAL_SCIENCE_HARVEST_001_20261121
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
date: 2026-11-21
local_time_source_cutoff: 2026-11-21 23:39 Europe/Warsaw
visibility: PUBLIC
function: AUTONOMOUS_CROSS_DOMAIN_EXTERNAL_SCIENCE_HARVEST / LITERATURE_FIRST / TWO_SURFACE_PRIOR_ART / SCIENCE_FIRST / SOURCE_TYPED
status: FOUR_ORIGINAL_2026_PUBLISHER_ARTICLE_SOURCE_VERIFIED / ONE_FULL_PRIMARY_PDF_TEXT_READ / AUTHOR_GITHUB_M87_CODE_DIRECT_READ / THREE_EXPERIMENT_DATASET_LOCATORS_VERIFIED / NO_NATIVE_REEXECUTION
claim_ceiling: NO_EXTERNAL_RAW_DATA_RERUN / NO_NEW_NASH_PHYSICAL_RESULT / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT013 — Original external fundamental-physics literature and experiment-data radar, 21 November 2026

## 0. Function, source method and prioritization

This iteration follows the Human Moderator's explicit direction "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji" and single-letter O autonomous continuation. XH is the external science harvest cell, not the internal Badacz/Mech/REC auditor: source-first emerging science, original papers, authors' code and actual experimental observations, foundational mature theory plus nearest contemporary specialist work, testable uncertainties and negative knowledge. Because ROT008–012 already covered agentic-science methodology and benchmark claims heavily, ROT013 deliberately selects contemporary PHYSICAL SCIENCE instruments/experiments and astrophysical imaging; no repetition of Wu–Xu particle source calculations or generic metascience catalogue.

Actual access:
- Nature 18 November 2026 analogue-field paper original publisher PDF **full 832-line extracted TEXT read** through web with methods and original 2002/2022 priors; web.run PDF `screen` requests for original pages 0,2,3 were made but returned CACHE MISS. Therefore DO NOT claim direct PDF image inspection, figure digitization or byte-authenticated supplement.
- Original journal primary indexed HTML abstracts and relevant METHODS/DATA excerpts directly searched for Nature Nov11 M87, Nature Photonics Nov20 QADC, npj Quantum Information Nov20 SiC; publisher `open` occasionally CACHE MISS, so DO NOT claim full opened HTML/direct Figure PDF for these three.
- Original research data/custody PUBLIC LOCATORS: Cambridge Apollo DOI 10.17863/CAM.134394 for 2+1 field, public raw EHT Data Products 2019-D01-01, 2024-D01-01, 2026-D01-01 for M87, University Stuttgart DaRUS DOI 10.18419/DARUS-5965 for SiC CSV (archive describes original-format ~537.6kB). QADC supplementary article has source datasets BY CORRESPONDING AUTHOR ON REQUEST, not a freely archived full original measurement set.
- ORIGINAL AUTHOR GitHub `samlaihei/GenDIReCT` README.md actually fetched directly using connected GitHub, blob `ddd840eaa9f1bed453a1f4835e95f08315be4624`, len 5061 chars. Also original root GitHub tree read: `runGenDIReCT.py`, notebook, model directory, source UVFIT example, LFS weights pointers requiring git lfs. Original independent `ClosureInvariants` linked repository direct README request returned 404; DO NOT claim that repo source was read or reproduced.
- No original experimental data CSV/ZIP/HDF5/FITS bytes downloaded, no library/tool experiment or tomography run, no external authors contacted, no NASH physical model imported or executed. The mathematical discussion is from SOURCE article, not independent NASH derivation.

## 1. P1: Actual nonperturbative quantum-field analog simulator d=2, Nature 18 Nov

ORIGINAL authors Yansheng Zhang, Feiyang Wang, Paul H. C. Wong, Alexander C. Jenkins, Yi Jiang et al., `Analogue simulation of massive relativistic quantum fields in 2 + 1 dimensions`, Nature 659 634–639 (issue 19 Nov; **published ONLINE 18 Nov**), original DOI https://doi.org/10.1038/s41586-026-11268-y , first primary article PDF text https://www.nature.com/articles/s41586-026-11268-y.pdf .

Actual measurement: two coherently RF-coupled hyperfine components of ^39K uniform optically trapped quasi-two-dimensional BEC, relative phase phi and population imbalance Z; Josephson regime mu_s >> hbar*Omega. The long-wavelength approximation maps to (2+1) sine–Gordon field with author-source equation:
  partial_tt phi = c^2 laplacian phi − (m* c^2/hbar)^2 sin(phi),
  c = sqrt(mu_s/m_atom), m* = m_atom sqrt(2 hbar Omega / mu_s).
Author measurements: mode dispersion with tunable mass gap, dynamics including nonlinear extended 2D topological domain walls and phase winding 2pi, wall widths scaling as inverse square root Omega in relevant measurement. **NOT observed cosmic preheating, an actual cosmological false vacuum or strings in spacetime**; proposal says simulator OPENS WAY to test related scenarios.

Two-surface subtraction:
FOUNDATION = sine–Gordon quantum field, standard Josephson coupled cold atoms, solitons/domain wall models and analogue universe physics; author refs original Son & Stephanov, PRA65 063621 (2002) relative phase domain walls, previous d=1 simulator work and cosmological analog experiments.
NEAREST 2022/2024/2025 = Viermann et al Nature 611 260–264 (2022) analog curved spacetime field and 2024 Jenkins et al PRA110 L031301 generalized cold-atom false-vacuum simulator. Authors' new 2026 contribution is controlled d=2 massive SG experiment, not invention of SG theory or empirical verification of cosmic strings.
Explicit data availability Cambridge Apollo https://doi.org/10.17863/CAM.134394 ; no source bytes downloaded/verified. Original technical primary PDF content read; PDF screenshots tried returned cache miss and no visual read inferred.

Scientific eligibility for NASH geometry/J/K/DTC: any bridge needs source-matched mapping of microscopic (Omega, mu_s, n, Z) to **one identical field/operator and actual experimental domain** and one numeric falsifier against measured dispersion/walls, not generic 'nonlocal geometry' or topology analogy. NO physical bridge currently verified.

## 2. P2: Astrophysical calibration-invariant reimaging, Nature 11 Nov M87* (new credible empirical independence)

ORIGINAL Samuel Lai, Nithyanandan Thyagarajan, O. Ivy Wong, Foivos Diakogiannis, `Independent interferometric observable confirms black hole shadow in M87*`, Nature 659 317–323, journal published **11 Nov 2026** DOI https://doi.org/10.1038/s41586-026-11241-9 . Original publisher indexed abstract and NIH full article search snippets source direct. 2017, 2018, 2021 prior Event Horizon Telescope 1.3mm raw visibility measurements, not new independently acquired telescopic data. Independent OBSERVABLE is the co-polar station-gain-insensitive closure invariants, and independent METHOD is GenDIReCT conditional diffusion image reconstruction; authors prereg/validate on synthetic OOD morphologies and data noise prior to unblinding M87. Learned generative architecture can retain training-distribution priors, even when there is no PRESCRIPTIVE ring morphological prior; refrain from mathematical claim prior-free inverse reconstruction.

Authors report from all epochs image-model ring angular diameter **42.2±1.5 microarcseconds**, an independent geometric-parametric fit **42.3±1.1 microarcseconds**, and inferred M87* mass **(6.5±0.5) billion solar masses** under nominal scaling assumptions. These are two analysis estimands on the SAME underlying EHT epochs, not independent telescope replications. Independence of observables and nuisance calibration is valuable but no causal claim of new photons/stations. Original EHT first ring images 2019 and prior closure invariant theory already mature. Another source's public GenDIReCT 2025 method, Lai et al Publications of the Astronomical Society of Australia 42 e148 (2025), DOI 10.1017/pasa.2025.10110, arXiv 2510.12093, precedes 2026 Nature M87 application. Formalism of closure phases/amplitudes dates to earlier VLBI work; no NASH priority.

Original AUTHOR code actual direct connected GitHub read:
https://github.com/samlaihei/GenDIReCT `README.md` blob ddd840eaa9f1bed453a1f4835e95f08315be4624; repo Python 3.9+ PyTorch 2+, latent diffusion, closure invariants, test code `runGenDIReCT.py`, LFS model weights; root tree explicitly exists. Repo README says install `ClosureInvariants` and use trained model weights, not same as XH actually running inference. Source `nithyanandan/ClosureInvariants` README direct read returned 404; source availability specific path unresolved. Public EHT data identifiers 2019-D01-01, 2024-D01-01, 2026-D01-01 from original publication; XH did not download visibilities, image reconstructions or LFS model bits.

Two-surface prior art:
A = interferometry, closure phases/gains and underdetermined inverse imaging.
B = 2019 EHT M87 image and 2025 GenDIReCT source formalism; 2026 Nature is independent *reanalysis on same data with different observable/pipeline* with strong ring robustness.
Relevance to NASH epistemology only: independent evidence must be typed as `SAME_RAW_DATA / DISTINCT_CALIBRATION_INVARIANT_OBSERVABLE / DISTINCT_RECONSTRUCTION` and not falsely upgraded to `INDEPENDENT_PHYSICAL_DATA_ACQUISITION`. No claim novelty for generic 'independent check' guard.

## 3. P3: Physical digital quantum phase metrology, Nature Photonics 20 Nov

Original Eugenio Caruccio, Simone Roncallo, Valeria Cimini et al., `Quantum analogue-to-digital converter for phase estimation`, Nature Photonics, **published 20 November 2026**, original DOI https://doi.org/10.1038/s41566-026-02050-7 .
Original indexed primary publisher full abstract, original Results and Methods excerpts source directly read. Original author claim first experimental QADC in metrology, after previous THEORETICAL formulations of digital quantum estimation/phase algorithm. Fully reconfigurable eight-mode integrated photonic interferometer, highly indistinguishable quantum-dot photon source, three phase bits with 1-, 2-, 4-photon GHZ resource states and adaptive/conditional operations, plus denoising autoencoder and NN phase-bias correction. Reported one-, two-, four-photon state tomography fidelities F1=0.9972±0.0001, F2=0.9476±0.0004, F4=0.811±0.005. Event coincidence rates integrated useful config ~5 MHz 1ph, 50kHz 2ph, 8Hz 4ph. DO NOT compare raw event rates as causal intrinsic speed ratio; resources and preparation modes differ.
Source author result: quantum strategy yields higher phase-output-bit mutual information than CLASSICAL SINGLE-PHOTON INTERFEROMETRY matched per successfully *detected* resource events for a moderate n_shots range; quantum advantage DIMINISHES with increased repetitions due to loss/noise and imperfect multi-photon state distinguishability. Protocol used postselection for state preparation and at measurement, and gives conditional analysis for success events. Therefore no universal practical real-time advantage, no sensor accuracy guarantee when measured per wall-clock second or per total generated physical photon; those are possible different estimands, not refutation of original claimed conditional result.
Source data availability: article + supplement online; source raw datasets available from corresponding authors UPON REQUEST, not independently in downloaded public original raw table. No code execution or resource-matched independent experiment.
Two-surface prior art:
A = original quantum phase estimation/QFT, Bayesian phase metrology, shot-noise vs Heisenberg vs mutual information and postselection accounting.
B = recent digital quantum estimation theory and authors' 2026 physical first test, prior source theoretical papers distinguished from latest instrument.
Science falsifier question (not NASH novel physics): classify resource accounting R1 photons prepared, R2 phases traversed, R3 detected successful events, R4 acquisition time; compare quantum vs strongest valid classical protocol under same R1-R4 and trained NN independent fixed calibration. Distinguish original R3 conditional claim from stronger system-level efficiency claim (not made by authors). No instrument-level pilot authorized.

## 4. P4: True room-temperature nuclear memory readout without separate RF, npj Quantum Information 20 Nov

Original Raphael Wörnle, Jonathan Körber, Timo Steidl et al., `RF-free control of nuclear spins with color centers in silicon carbide`, npj Quantum Information 12 article191 (2026), **published 20 Nov 2026** DOI https://doi.org/10.1038/s41534-026-01415-8 .

Experiment in room-temperature SiC PL6 color center hyperfine coupled to nearby ^13C. Spin-electron microwaves and precisely tilted DC magnetic field indirectly manipulate nuclear spins WITHOUT additional direct RF drive for nuclear spin, using gyromagnetic enhancement/hyperfine effects. Author fidelity single qubit 97% and two-qubit tomography 89%, nuclear coherence T2_nucl **151.0 ± 6.9 microseconds** ~6x electron spin in their device (near T1 limited). Not 89% full two-qubit gate fidelity across arbitrary chips or claim globally better than NV. Original source data sample preparation PL6 N-ion implantation etc in publisher methods. Earlier matured SiC room-temperature color-spin qubits (Koehl et al Nature 479, 84–87 (2011)), coupled nuclear memories and ODMR mature prior.
HIGH-VALUE DATA CUSTODY: source ORIGINAL DaRUS repo DOI https://doi.org/10.18419/DARUS-5965 available public, archival **published 14 May 2026**, CSV figure axes, fitted curves, listed as Version1 original-format ZIP ~537.6kB. This data existed before Nov20 peer-reviewed paper, no claim paper discovery first this week. ACTUAL CSV FILES NOT DOWNLOADED in this rotation. Measurement/evaluation Python original authors specifically NOT publicly available due to docs; available on request. Distinguish openly present numeric CSV from unverified executables. This represents a credible source-native independent reanalysis opportunity IF a specific scientific hypothesis warrants it, but not an automatic NASH physical target.

Two-surface prior art:
A = hyperfine electron–nuclear interactions, ESR/ODMR, Ramsey coherence and nuclear memory at room temperature.
B = earlier diamond/SiC color-center nuclear memory, this specific 2026 PL6 control author claim.
NASH bridge would demand physical field/sensing parameter/phase/noise transfer under original instrument calibration; no such NASH observable as of source cutoff. No independent measurement replay or external refereeing.

## 5. Ranked external evidence value and next research discriminants

P1 **Nature analog massive d=2 sine–Gordon**: true author experimental quantum analog with full primary technical text and Apollo original data archive; highest long-run physics relation to field/topology but no actual NASH field map. Prior SG d=1 and 2022 curved analogue differentiated. One useful next step: external source experiment raw data and dispersion wall-width prereg if meaningful exact model interface appears.
P2 **Nature M87***: strongest independent calibration-invariant observation using same sky data, with public model code and EHT original raw locators; ideal science-of-evidence case for claim/data independence taxonomy and source-safe interpretable astrophysical ring, NOT an independent raw acquisition.
P3 **npj SiC**: room-temp device new mechanism and genuine public CSV; real hardware object and numerical reanalysis possible, but instrument codes not freely available.
P4 **Nat Photonics QADC**: clean resource/conditional-estimand test of purported quantum metrological benefit; R3 vs R1-R4 is sharp distinction. Full source data available on author request only.

Cross-domain negative controls:
- Real physical experiment != fundamental cosmological observation (analogue BEC not cosmic defects).
- New processing pipeline on old EHT visibilities != new independent telescopic observation.
- Conditional detected-event information advantage != throughput/total physical resource superiority.
- Public plotted CSV data != public executable instrument control code.
- A mathematically suggestive NASH analogy != verified dimensioned mapping to external observable.
- "Original article opened in web" != all underlying data/model weights read or instrument executed.

No original authors contacted, public dataset bytes downloaded, new B1/TT/QB run, C1 resumption, owner task or GH issue dispatch. BW receipt is GITHUB_PENDING_BW_INGEST not ACK. No independent novelty or physical discovery claims made for NASH.

FINAL:
XH_S7_ROT013_EXTERNAL_PHYSICAL_SCIENCE_HARVEST_PASS /
NATURE_D2_QFT_ANALOGUE_ORIGINAL_TEXT_AND_APOLLO_LOCATOR /
M87_CLOSURE_INVARIANT_SAME_DATA_INDEPENDENT_ESTIMAND_AND_ORIGINAL_CODE_READ /
QUANTUM_ADC_DETECTED_CONDITIONAL_RESOURCE_GATE /
SIC_ROOM_TEMP_NUCLEAR_MEMORY_DARUS_PUBLIC_CSV_LOCATOR /
ORIGINAL_EXPERIMENTAL_RAW_BYTES_NOT_READ /
NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN.
