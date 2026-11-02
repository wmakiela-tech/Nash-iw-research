# XH-S5 ROT017 — low-flux photon-pairing SNR versus temporal phase memory: exact independent statistical gate

artifact_id: IW_XH_S5_ROT017_PHOTON_PAIRING_PHASE_MEMORY_SNR_SCALING_20261102
return_id: XH-S5-ROT017-PHOTON_PAIRING_PHASE_MEMORY_SNR_SCALING_GATE_20261102
date: 2026-11-02
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: PUBLISHER_ORIGINAL_ABSTRACT_AND_METADATA / CLASSICAL_TWO_ARM_CONDITIONAL_POISSON_TOY / INDEPENDENT_EXECUTED_ANALYTIC_AND_MONTE_CARLO / NO_AUTHOR_EXPERIMENT_REPRO / NO_MATH_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN

## ORIGINAL FIRST — publisher source facts
Jinping Lin, Lai Zhou, Minxue Zhuang, Wenda Shi, Zhenke Shi, Lin Chang, Zhiliang Yuan, "Photon-pairing-enhanced distributed spectroscopy sensing over 400 km optical fiber", Nature Communications, published 2026-10-31, DOI https://doi.org/10.1038/s41467-026-78826-w ; original https://www.nature.com/articles/s41467-026-78826-w . Publisher original ABSTRACT and bibliographic information verified on 2026-11-02; FULL article Methods, SI, original time-tags/code/raw experimental data NOT obtained or executed. Original authors report phase-tolerant second-order photon-pairing rather than coherent first-order stacking, reconstructed INTENSITY spectra at 400 km, received power 5.5e-15 W per comb line, SNR >23.5 dB; their abstract reports SNR increasing linearly with photon-count rate in their operational regime, versus square-root scaling for conventional photon counting. These are AUTHOR results, NOT results reproduced or recalculated here; do not turn measured power into counts without source wavelength/efficiency/time bin.

## MATURE PRIOR ART / NO PRIORITY
Hanbury Brown & Twiss, Nature 177, 27–29 (1956), DOI https://doi.org/10.1038/177027a0 already measure correlations of independently detected intensity fluctuations, losing optical relative phase. Glauber, Physical Review 130, 2529–2539 (1963), DOI https://doi.org/10.1103/PhysRev.130.2529, classical/quantum optical correlation hierarchy. NIST IR 8486 (2023) https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8486.pdf standard g2 correlations. XH model below is CLASSICAL common-source intensity correlation with conditionally independent Poisson detectors, not photonic entangled pairs, not source optical hardware, not a first derivation of moments. PUBLIC Nash-iw-research text searches photon pairing spectroscopy / 400 km fiber / second order optical correlations / g2 spectral / Lin Zhou yielded no indexed hit; this does not settle private BW prior.

## Exact test model, assumptions and source ceiling
For each block k, phi uniform on [0,2pi), shared in two channels. Conditional independent counts:
 A|phi ~ Poi(mu*(1+v*cos phi)),
 B|phi,eps ~ Poi(mu*(1+v*cos(phi+eps))),
where mu>0 externally calibrated average counts per channel per block, 0<v<1 visibility; eps~N(0,sigma_d^2) independently per block models DIFFERENTIAL channel phase jitter. We intentionally exclude actual quantum photon pairs, optical combs, detector deadtime/saturation, instrument efficiency/400km, software pair-matching, fiber physics and author's SNR definition. Statistic X=(A-mu)*(B-mu), reported SNR=E(mean X)/SD(mean X). This toy is not validated against the author measurement.

Set K=exp(-sigma_d^2/2), L=exp(-2*sigma_d^2). Analytic exact Poisson/trigonometric moment calculation gives
 E X=mu^2*v^2*K/2;
 Var X=mu^2*(1+v^2*K/2)+mu^3*v^2+mu^4*v^4*(1/4+L/8-K^2/4).
At sigma_d=0 this reduces to mean=mu^2*v^2/2 and V=mu^2*(1+v^2/2)+mu^3*v^2+mu^4*v^4/8. Exact Fraction test for v=3/5 and mu=1: mean=9/50=.18, variance=7781/5000=1.5562 PASS. For M iid blocks SNR=mean*sqrt(M/V). Low-count mu->0 SNR ~[v^2/(2sqrt(1+v^2/2))] mu sqrt M (LINEAR in mu). High-count mu->infinity SNR/sqrt M -> sqrt2 (saturation). These asymptotes are for THIS toy only; source claims neither universal high-flux linearity nor photon-pairing immunity to differential phase decoherence.

## Independent temporal phase-memory falsifier
If shared phi follows stationary wrapped Gaussian random walk phi(k+1)=phi(k)+eta, eta~N(0,sigma_rw^2), with initial phi uniform, while channels still count independently conditional on phi, for h>=1:
 Cov(X_k,X_(k+h)) = mu^4*v^4/8 * exp(-2*h*sigma_rw^2) EXACT.
Hence for finite M:
 Var(mean X)=V/M+(2/M^2)*sum_(h=1)^(M-1)(M-h)*(mu^4*v^4/8)*exp(-2*h*sigma_rw^2).
Naively using iid V/M can dramatically understate variance in this model; its correct uncertainty depends on the phase autocorrelation. This does NOT prove that the AUTHORS neglected time correlations or that their optical scheme shares this covariance.

Executed analytic results for v=.6, M=100000, sigma_rw=.08 rad/block:
 mu=.025: iid SNR 1.3050277; correlated 1.304 (inflation 1.001).
 mu=.1: iid SNR 5.1615102; correlated 5.109 (inflation 1.021).
 mu=.4: iid 19.768; correlated 17.317 (inflation 1.303).
 mu=1.6: iid 67.930; correlated 31.744 (inflation 4.579).
 mu=6.4: iid 178.878; correlated 35.204 (inflation 25.819).
 mu=25.6: iid 317.885; correlated 35.679 (inflation 79.380).
 mu=200: iid 423.917; correlated 35.778 (inflation 140.389).
 Empirical double-rate log2 SNR slope at mu=.025->.05 equals .994542 (low-count near-linear), mu=100->200 equals .071857 (high-count saturation).
 At mu=1, differential channel-phase jitter sigma_d=2rad lowers E X from .18 to .02436035, attenuation e^-2=.135335; DIFFERENTIAL jitter is distinct from COMMON global phase. Independent phases for the two arms => zero covariance. These are synthetic numbers and do not measure Nature paper SNR in dB.

## Independently executed controls (NOT source reconstruction)
Route A rot017_analytic.py (Python standard library) evaluates exact Fraction moment witness, closed-form iid and finite-M Markov formulas, low/high-flux derivatives and differential-phase attenuation; frozen deterministic analytic JSON PASS.
Route B rot017_independent.py (independent NumPy implementation with no import from Route A): 2048-angle phi quadrature + 28-node Gauss-Hermite epsilon quadrature, and 350000 independently generated conditional Poisson count-pairs for EACH of SIX mu/sigma combinations. Mean discrepancy is <5 Monte Carlo standard errors in all six; worst relative variance discrepancy 1.29%. Separate 320 random-phase-walk replicates x 2000 blocks for mu=1,6,20 compare sampling standard deviations to independently quadrature-derived exact lag formula: relative discrepancies 4.0%,2.8%,2.4%, respectively. All pre-specified checks PASS with RNG seed 20261102.
Local ZIP contains independent Python scripts, their two frozen JSON result files, full Polish ~10 KB report, README, SHA256SUMS.json, verifier that reruns scripts in clean temp directory. 8 members, ZIP CRC PASS, 7 individual member SHA256 PASS, clean ZIP extraction and rerun BOTH programs -> JSON BYTE-IDENTICAL PASS.
MODERATOR-LOCAL FULL ZIP: IW_XH_S5_ROT017_PHOTON_PAIRING_PHASE_MEMORY_REPRO_20261102.zip
ZIP_SHA256 2f67b4ae64535d48cad6cbf37fc40757276127b42b229352ee07d193c817ad9d
Local complete report SHA256 c4cf71d031f63e6bee5abf225dd06d631b4c092e47caac109190a02184d30ce5
GitHub report is NOT full ZIP or complete standalone code unless separately deposited/read back.

## Narrow source-native falsifier (proposed, NOT executed)
Need the authors' Methods, full definition of coincidence pairing, spectral estimator/SNR, time bin, optical path noise, true photon rate, detector deadtime, shot noise and phase correlation. Then compare low to high flux, common vs DIFFERENTIAL phase jitter, and segment mean covariance across time using original raw time-tag data, heldout spectral reconstruction and block bootstrap preserving lag. A source algorithm may remove our toy memory impairment by different processing, and their published result remains unchallenged by this toy. No unsupported transfer to quantum hardware advantage, astrophysical NASH-K/J3, gravity, or the author's empirical 400km experiment. No cross-cell tasks; OWNER, BW, AUD, EXEC not assumed.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_SOURCE_EXPERIMENT_REPRO / BW_INGEST_UNVERIFIED.
