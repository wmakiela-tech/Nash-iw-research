---
artifact_id: IW_DAX_S8_ROT016_BELLE_F0_RESONANCE_NWA_INTERFERENCE_GATE_001_20261112
created_at: 2026-11-12
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_BELLE_F0_FIT_SOURCE / ISOLATED_NWA_THERMAL_BENCHMARK / CONDITIONAL_COHERENT_INTERFERENCE_ENVELOPE
claim_ceiling: NO_RAW_HEPDATA_YODA / NO_FULL_HADRONIC_QCD / NO_PHYSICAL_PION_RATE_BOUND / NO_DEPOSITION_OR_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT016: Belle f0(980) measured two-photon width, NWA benchmark, and coherent pion amplitude caution

Date 12 November 2026. Scientific scope: source-fitted measured f0(980) parameters plus **isolated source-typed narrow-width (NWA) resonance benchmark** at inherited R68 photon/bath parameters. This does NOT recover original Belle HEPData numeric table rows and does NOT compute the true gamma gamma -> pi+pi- full-QCD physical rate, pion energy transport, neutrino yields, or PBH/BBN bounds.

## Earlier first-owner results retained

DAX-S7 R68 FIRST restricted first-muon-event probability to e+e-, mu+mu- and DPP gamma-gamma interaction channels. DAX-S8 ROT012 FIRST added one charged-pion point-Born SOURCE-MODEL fourth competitor with conditional first-muon P=0.08577845, emphasizing it was not physical complete QCD. ROT013-015 FIRST identified Belle energy/angle fiducial restrictions, the mathematical thermal kernel and source-data semantics. ROT016 does not reverse or reassign this work.

Source currentness 12 Nov: original HEPData ins749358 Belle record and Rivet analysis ID BELLE_2007_I749358 located; numerical CSV/JSON/YODA rows NOT obtained in this runtime (web cache misses and container DNS NameResolutionError). Service status https://status.hepdata.net/ indicated the site itself operational; the blocker is this environment, not a verified provider outage. RPM package inventories explicitly list a YODA file in older Rivet-data and YODA.GZ in newer 4.1.2, but NO actual Belle numeric YODA bytes retrieved. HEPData official converter documentation provides YODA/CSV endpoints; they were not successfully downloaded.

## Original measured source (fitted Belle resonance, not interpolated data)

Belle Collaboration / T. Mori et al., *High statistics study of f0(980) resonance in gamma gamma -> pi+ pi- production*, Phys. Rev. D 75, 051101 (2007), https://doi.org/10.1103/PhysRevD.75.051101 , https://arxiv.org/abs/hep-ex/0610038 , INSPIRE https://inspirehep.net/literature/728977 .

The original published abstract gives f0 fit central mass M=985.6 MeV, partial gamma-gamma width Gamma_gg=205 eV (stat +95/-83, syst +147/-117 eV), and charged pi+pi- partial width Gamma_pi=34.2 MeV (stat +13.9/-11.8, syst +8.8/-2.5 MeV). Gamma_pi is NOT measured total width or branching ratio, and Gamma_gg is a model-dependent fitted source parameter. Full f0(980) lineshape near the K Kbar threshold and its coherent background amplitude are NOT available from these three numbers alone. Do not substitute a different channel's gamma-gamma width (neutral-pion Belle estimates differ).

## First-source measured-parameter calculation; 2 independent algebraic forms

Inherited R68 inputs E_gamma=1436554 MeV, T_gamma=0.07818527068831995 MeV. Define C=4 E T; y=W²/C; L(y)=-ln(1-e^-y); H(W)=4 W³ L(W²/C)/C². For any invariant-s unpolarized total gamma gamma cross section in an instantaneous ideal isotropic Planck bath, the common collision hazard is K=integral H(W) sigma(W²) dW. H is **per linear dW**, not a probability density independent of the source cross section.

For a spin-zero resonance in the standard *unpolarized* narrow-width approximation with b=Br(f0->pi+pi-) and 0<=b<=1,

sigma_res(s) -> [8 pi² Gamma_gg b / M] delta(s-M²).

Hence K_res(NWA)=H(M) [4 pi² Gamma_gg b / M²].

Central Belle fit and b=1 REFERENCE:
- H(M)=0.0023195057688303705705653155503909524 MeV^-1.
- K_res^NWA(Br=1)=1.93244732698013664492173305174706656e-11 MeV^-2.
- R68 scalar charged-pion Born source K_B = 9.09761762118362680156259114245489993e-10 MeV^-2, independently recomputed at 65 dps, not merely recopied from ROT012.
- K_res(NWA,Br=1)/K_B = 0.0212412458672748609745, about **2.124%**.
- For a general b, this scales as b. This ratio is a SOURCE-TYPED isolated resonance intensity scale, neither the true f0 physical excess over Born nor a direct experimental cross section at R68.

Independent derivation: use s=C*y and delta(s-M²) in the EXACT incoming angle and Planck reduced kernel, obtaining K_res=2 y0 L(y0) [8 pi² Gamma_gg b / M]/C where y0=M²/C, algebraically IDENTICAL to H(M)4pi²Gamma_gg b/M². Verified at 65 decimal digits. The derivation uses established spin-zero gamma-gamma resonance Breit-Wigner/NWA physics; not new theory.

## The decisive interference guard (mathematically exact under explicit hypothesis)

If the entire physical two-pion final-state amplitude were EXACTLY a sum A_B + A_R on the SAME positive flux and final phase-space measure, with squared norms K_B and K_R (and no other physical amplitude), then the interference term is not known from two positive cross sections. By Cauchy-Schwarz:

( sqrt(K_B)-sqrt(K_R) )² <= K_total <= ( sqrt(K_B)+sqrt(K_R) )².

Under the ADDITIONAL NWA and measured CENTRAL Gamma_gg assumptions and 0<=b<=1, the numerical broadest allowed **TWO-COMPONENT-NORM** envelope for K_total/K_B is [0.7297537101661758956163, 1.3127287815683738263328], i.e. Born-only multiplied by 0.730 to 1.313 (about -27.0% / +31.3%). The extrema need NOT be physically attainable, because relative phases, helicity and partial-wave shapes are constrained. Unknown further QCD amplitudes invalidate the two-component premise; source Gamma_gg statistical/systematic errors not incorporated. This interval is NOT a physical hadronic uncertainty range, lower/upper bound, or conservative experimental error.

Crucial FALSIFIER: Naively adding the isolated f0 NWA rate of ~2.124% to the Born pion source rate as an INDEPENDENT first-event channel is not valid: they describe COHERENT alternative amplitudes for the SAME gamma gamma -> pi+pi- final state, not exclusive competing hazards. The true interference may be constructive or destructive; the source fitted Gamma_gg alone does not provide its sign, phase, or angular correlation. Avoid double counting.

For conditional R68 four-source bookkeeping only (the original BW_e/BW_mu/DPP three channels plus this exact two-component pion model), the norm interval would imply P_first,mu in [0.0855571023660,0.0859706542756], versus point-Born-only 0.0857784504994 and original restricted three-channel 0.0864939970806. These are hypothetical model diagnostics, not physical eventual muon/neutrino production, energy deposition or PBH bounds.

## Finite-width sensitivity: 4 toy scenarios, NOT source-native fitted f0 lineshape

A separately coded SciPy direct W integration of a constant-width scalar Breit-Wigner sigma(W)=8pi Gamma_gg Gamma_pi /[(W²-M²)²+M² Gamma_tot²] (no interference) with Gamma_pi=34.2MeV and hypothetical Gamma_tot 34.2,50,70,100MeV gives K_finite/K_NWA at each same branching ratio respectively 0.9826012,0.9742130,0.9633239,0.9465076. These are NOT Belle total-width measurements, proper Flatte/channel-coupled pion amplitudes, physical uncertainty bands or proof of broad-resonance accuracy. They merely show the NWA approximation has source-model sensitivity to its own finite-width ansatz.

## Verification, failure record, custody

Actual local 10-member ZIP: full extended report, source audit, README, two executed numerical scripts, two frozen JSON outputs, provenance receipt, verification script and SHA256 manifest. ZIP CRC PASS; SHA256 9/9 payloads PASS; clean extracted replay both scripts byte-for-byte identical to frozen JSON PASS; ZIP SHA256 ed4c00ae5e1b2345066fa2a9847dd63ea0bf12d7811227d67d2a24e63e5061fc. mpmath 1.3.0/Python3.13.5 at 65dps, independently coded SciPy1.17.0 finite BW. Original experiment numerical arrays, physical 2pi QCD amplitude and independent external referee NOT RUN/READ.

Science should REOPEN only on HEPData/YODA authentic bytes with provenance plus/or a source-versioned dispersive/Flatte charged-pion amplitude and full temperature/angle application. XH-S6 is active successor, earlier XH-S5 ACK was for 4e QED, NOT a pion-task acceptance. No duplicate cross-cell task. BW source ingestion status GITHUB_PENDING_BW_INGEST; delivery is not scientific acceptance.

DISPOSITION: ORIGINAL_BELLE_F0_FIT_PARAMETER_RETRIEVED / NWA_SOURCE_MODEL_BENCHMARK_PASS / COHERENT_AMPLITUDE_INTERFERENCE_GUARD_PASS / RAW_BELLE_DATA_ACCESS_BLOCKED / PHYSICAL_HADRONIC_QCD_OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
