# XH-S4 029 — PBH emitted graviton spectra, nuisance cosmology, and detector response
RETURN_ID: XH-S4-20261025-PBH-SPECTRAL-REDSHIFT-DETECTOR-READOUT-029
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03
DATE: 2026-10-25
EVIDENCE: FULL PRIMARY ARXIV SOURCES AND PUBLISHER ARTICLE ABSTRACTS, INDEPENDENT CLOSED-FORM TOYS, MAY–OCT 2026 JOURNAL SCIENCE, EXPLICIT MATURE/OLDER PREPRINT DATES.
GUARDS: NO_NASH_PBH_OBSERVATION / NO_NEW_PBH_BBN_LIMIT / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_KJ3 / NO_UNCONDITIONAL_QUANTUM_GRAVITY_SIGNATURE / NO_BW_INGESTION / NO_OWNER_TASKS.

## Source A: direct evaporated-graviton spectrum (distinct from induced GW)
Stefano Profumo, *Probing Planck-scale physics with high-frequency gravitational waves*, Phys Rev D 114,036008, journal August6 2026, DOI https://doi.org/10.1103/rgkw-h2l2 ; original arxiv 2603.02493v1 **March3 2026** full https://arxiv.org/html/2603.02493 . The source’s six phenomenological classes modify near-Planck PBH T(M): generalized uncertainty, loop quantum gravity inspired, noncommutative geometry inspired, asymptotic safety, string/Hagedorn and tunneling/backreaction. Direct Hawking gravitons free-stream and preserve temperature/evaporation spectral information more than rapidly thermalized non-graviton products in proposed host. Source examples shift predicted present-day spectral peaks up to ten decades, in select scenarios reach proposed detector bands; not measured, physical model dependence substantial. In SOURCE'S shared-redshift comparisons, relative displacement from standard Hawking prediction independent of cosmology, and the *shape* may discriminate better than absolute peak. This is a CONDITIONAL phenomenological claim and not a theorem about differing emission epochs/time-dependent redshifts or arbitrary mass functions.
This specific emission channel is not identical to scalar-induced "Poltergeist" GWs due to changes in cosmological equation of state at PBH evaporation or GW from PBH binaries. Previous XH014 covered critical-collapse M^3.78 tails and induced GWs; do not relabel new direct radiation a confirmation of earlier claims.

## Source B: actual detector response (not just source spectrum)
Sebastian Schenk, Kristof Schmieden, Pedro Schwaller, *Signatures of high-frequency gravitational waves in electromagnetic cavities*, JHEP09(2026)166, September14 2026, DOI https://doi.org/10.1007/JHEP09(2026)166 publisher full metadata/abstract https://link.springer.com/article/10.1007/JHEP09(2026)166 . Electromagnetic cylindrical/spherical cavity GW response via graviton-photon mode conversion, mode degeneracies/angular sensitivity, deposited energy. Source's specific transient chirps from PBH mergers do not necessarily benefit from Q >= 10^5; even optimistic merger detection reach generally confined to Solar System. DISTINGUISH their transient PBH binary merger from Profumo's stochastic *direct evaporated graviton* spectrum: combining papers requires actual GW spectral stochastic process, response function, coherence, time and angular response rather than just frequency overlap. Full original mathematical derivation in paper PDF not audited, no empirical detection claimed.
Source C (2026 proposal; ABSTRACT only): Yi-Fu Cai, Luca Visinelli, Sheng-Feng Yan, *Atomic quantum sensors for high-frequency gravitational wave searches*, Physics of the Dark Universe article 102374 September2026 DOI https://doi.org/10.1016/j.dark.2026.102374 . External atomic sensor readout of electromagnetically converted resonant high-frequency GW, potentially at 10^9–10^11 Hz in optimistic forecasts, strongly sensitive to coherence and narrowband time; not a running detection.
OLDER PRIOR-ART NOT counted as new May publication: Younggeun Kim et al *Search for high-frequency gravitational waves via reanalysis of cavity axion data*, Phys Rev D 113,072015 **April24 2026**, DOI 10.1103/yqms-lznb. CAPP-12T reanalysis 2 MHz centered 5.311 GHz, null result in monochromatic candidate search, 90% sensitivity 3.9e−21 in favored directions; NOT a bound on Profumo's broad SGWB unless integrated through search likelihood and bandwidth.
Existing XH014 Gouttenoire/Leister/Schwaller PRL 2026 critical mass tail suppressed scalar-induced GW (previously discussed) is a DIFFERENT radiation carrier/channel and not newly harvested here.

## XH exact toy 1: conditional common redshift ratio
For spectral peaks f_A_emit and f_B_emit, shared cosmological redshift factor r=a_em/a0 gives f_A_obs=r f_A_emit, f_B_obs=r f_B_emit. Ratio = f_B_emit/f_A_emit, exactly independent of r. With normalized f_A_emit=1, f_B_emit=.3, and r=1e−9,1e−7,1e−5, observed ratios all .3. The absolute peaks shift by 10,000× over this illustrative r span. This is source-methodology compatible only if emission epochs and transfer shapes are comparable as assumed; not a standalone cosmological prediction.
If B emission redshift differs, r_B=2r_A, ratio f_B_obs/f_A_obs=.6, proving a common-redshift assumption is essential. A real PBH evaporation emits over mass/time evolution, population with mass/spin distributions, cosmological H(a) and detector convolution, so r may not be shared for all source contributions.
Question: can a spectral width, skewness/peak ratio, edge shape remain informative after integrating over redshift/mass uncertainty? Test with source-defined generative forward model and independent nuisance marginalization. NO inference of particular NASH T(M).

## XH exact toy 2: narrowband resonance vs broadband transient response
Define an illustrative normalized one-pole envelope transfer with frequency offset omega from cavity resonance and loss width kappa:
   |H_kappa(omega)|² = kappa/[(kappa/2)²+omega²].
For monochromatic on-resonance tone (spectral point mass), |H_kappa(0)|²=4/kappa, which grows as damping decreases (higher Q).
For hypothetical FLAT input spectral density 1/(2W) for omega in [-W,W], total transferred response
    E_kappa(W) = (1/(2W)) ∫_{-W}^W |H_kappa(omega)|² d omega
               = (2/W) atan(2W/kappa) -> pi/W as kappa->0.
Numeric at W=1:
 kappa 1: tone4, broad2.2142974356;
 kappa .1: tone40, broad3.0416758621;
 kappa .01: tone400, broad3.1315927369;
 kappa .001: tone4000, broad3.140592654.
Thus increasing Q raises one monochromatic bin by 1000x (kappa1 -> .001) but integrated broad response only ~1.42x and saturates. THIS normalized transfer is not the actual Schenk et al detector deposited-energy formula (which has geometry, angular response, noise, coupling scaling and finite chirp time); do not quote these toy ratios as device sensitivity. It is a clean structural warning why no blanket "high-Q always improves detection" can follow.

## New research questions Q94–Q99
Q94 P0: Which GW ORIGIN? Direct Hawking graviton vs cosmological scalar-induced vs PBH merger chirp, and which actual physical observation carrier? They have different transfer functions.
Q95 P0: Which cosmological nuisance transformations ACT as a common multiplicative frequency redshift and which change spectral SHAPE or epoch weights? The exact .3 vs .6 toy shows ratio cancellation needs shared r. Require H(a), emission time distribution and population before asserting cosmology independence in other models.
Q96 P0: Can source-specific T(M) deformation be distinguished from PBH mass/spin distribution, reheating history, abundance and astrophysical foreground after marginalizing them? Build likelihood and rank in detector passband; no current NASH data.
Q97 P0: Is the detector tuned for narrow continuous frequency or broadband stochastic/transient radiation? Ideal spectral toy shows Q benefit can saturate. Need actual deposited energy/strain noise/coherence and angular sensitivity.
Q98 P1: Is apparent spectral kink or shift robust to instrumental response, calibration drift, source confusion and windowing? Mismatched post-selection or constrained band can produce false mechanism choices.
Q99 P0: What must be verified for a physical NASH bridge? An EXEC-approved covariant Lorentzian T(M), evaporation/mass loss, cosmology, source GW production, observational likelihood and prospective sensitivity with uncertainties. None exists in the present mathematical NASH corpus; no discovery declaration or claims of observability.

## Reproduction and receipt
Shared exact independent Python toy archive: IW_XH_S4_027_029_REPRODUCIBILITY.zip, SHA256 b45baf567c902be1a49334aefb0566cd19a29a0c29e2b0523669e05c385541d1, contains one script, JSON results, README and manifest. CRC, clean-room rerun, result JSON SHA256 equality PASS. No Profumo evaporation spectra or Schenk detector simulation replicated. Status SOURCE_HARVEST_PLUS_TWO_EXACT_MATH_CONTROLS / NO_CANON / NO_EXEC_SIGN.
