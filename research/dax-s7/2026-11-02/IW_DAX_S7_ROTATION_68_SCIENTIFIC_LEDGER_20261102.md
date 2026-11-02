# DAX-S7 R68 — Source-typed scientific ledger
Date: 2026-11-02. Status: BOUNDED_QED_FALSIFIER / NO_CANON / NO_EXEC / NO_PBH_BOUND.

## Sources
- Wu–Xu original: https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/main/arXiv-2509.05618
- PDG muon mass 105.6583755 MeV and lifetime 2.1969811 microseconds: https://pdglive.lbl.gov/DataBlock.action?node=S004M
- Gamma gamma double-pair asymptotic sigma=alpha^4[175 zeta(3)-38]/(36*pi*m_e^2); numeric 6.44433708835e-30 cm2
- Literature on muon-pair and double-pair contributions to neutrino cascades: https://doi.org/10.1103/PhysRevD.106.123016

## Numerically verified, source-typed
At fixed Planck Tgamma=0.07818527068831995 MeV, use gamma gamma -> e+e- and mu+mu- total Breit-Wheeler cross sections, gamma gamma -> four electrons asymptotic total sigma, and correct isotropic factor 1/2.
- Among ONLY THESE THREE photon interaction channels, mu+mu- first-event probability peaks at 0.0864887438349 for Egamma=1436.554 GeV. It is NOT an EM deposition fraction, neutrino loss fraction, or branching ratio among all SM channels.
- At muon E=1000 GeV, BG isotropic inverse-Compton first collision mean 1.470116e-9 s, mean scattered photon energy fraction 0.607464, lab muon decay time 0.02079325 s. Competing Poisson clocks give probability decay BEFORE FIRST IC ~=7.07016e-8.
- The CONDITIONAL deterministic mean-continuous IC cooling model down to muon gamma=100 gives time ~=6.125817e-9 s and decay probability ~=5.44472e-6. This is NOT a full stochastic cascade and does not exclude subsequent muon decay/neutrino losses.
- Total DPP sigma does not identify the differential four-lepton energy distribution: test partitions [0.25]*4, [0.49,0.49,0.01,0.01], and [0.97,0.01,0.01,0.01] all have sum(z)=1, but sum(z^2)=0.25/0.4804/0.9412. These are mathematical sensitivity examples, NOT QED differential operators.
- Validation: R67 electron BW 1TeV reproduction rel diff=1.34796e-5; N100 vs N260 total-rate quadrature max relative spread=1.88535e-4; BG muon Thomson limit ratio=0.9999993183; independent deterministic rerun byte-for-byte PASS for four CSVs and validation JSON.
- DPP asymptote at low energy not guaranteed; full transport requires all channels and dynamic bath. Wu-Xu original Julia and BlackHawk NOT_RUN; no PBH bounds, no novelty inference.

## Exactly matched source-byte CSV files in this directory
- IW_DAX_S7_R68_GAMMA_GAMMA_THREE_CHANNEL_RATES_20261102.csv
- IW_DAX_S7_R68_DPP_DIFFERENTIAL_UNIDENTIFIABILITY_PROXIES_20261102.csv
- IW_DAX_S7_R68_CONTINUOUS_MUON_COOLING_AND_DECAY_HAZARD_20261102.csv
- IW_DAX_S7_R68_QUADRATURE_CONVERGENCE_20261102.csv

Full standalone reproducer and all-artifacts manifest in locally verified R68 ZIP. No separate claim of their GitHub upload.
