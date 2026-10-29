# IW/NASH — DAX-S7 Rotation 67 — Science ledger
Date: 2026-10-29. Custody: BOUNDED_INDEPENDENT_FALSIFICATION / NO_EXEC / NO_CANON / NO_PHYSICAL_PBH_BOUND.

## Finding A — exact single-pair Breit–Wheeler differential kernel
Drebot et al., Phys. Rev. Accel. Beams **20**, 043402 (2017), Eq. (1), DOI https://doi.org/10.1103/PhysRevAccelBeams.20.043402.
For q=1-beta², mu=cos(theta_CM), the unpolarized CM angular density is proportional to
`[1-beta^4*mu^4+2beta²(1-beta²)(1-mu²)]/(1-beta²*mu²)^2`.
Transforming `t=atanh(beta*abs(mu))` yields the finite kernel `F(t)=2-sech²(t)+2q*(1-q/sech²(t))`.
Analytic integration agrees with the standard total BW cross-section to max relative difference 3.33e-16 (17 q values). Conditional Planck target energy/angle and Lorentz boost are sampled.

Independent deterministic energy-biased single-branch moment `E[z²+(1-z)²]`:
- photon 1 TeV: 0.943738; 1 PeV: 0.964458; 1e9 GeV: 0.974024; 1e12 GeV: 0.979533.
- 120000 independent event samples (30000 x 4 energies) agree within MC variation.
- R66 ad hoc 50/50, beta(2,2), 10/90 profiles substantially understate energy asymmetry of the **single-pair QED event**.

Conditional BW+IC only energy-carrier history, Ecut=0.1 GeV (NOT THERMAL DEPOSITION):
- photon 1 TeV median 2.90e-9 s; 1 PeV 2.88e-6 s;
- photon 1e9 GeV 2.77e-3 s; photon 1e12 GeV 2.86 s.
Simulation: 32 configurations x 1800 histories, three grids and two seeds in separate controls, no unresolved histories. These are NOT physical EM thermalization times.

## Finding B — decisive missing QED channel invalidates physical completeness
At high CM energy, **double pair production (DPP)** `gamma gamma -> e+ e- e+ e-` has the known asymptotic total cross section
`sigma_DPP = alpha^4*[175*zeta(3)-38]/(36*pi*me^2) = 6.44433708835e-30 cm²`.
Planck bath T=0.078185270688 MeV -> n_gamma=1.51520257248e28 cm^-3 -> Gamma_DPP=2.92731630134e9 s^-1.
Compare with existing single-BW opacity:
- Gamma_DPP/Gamma_BW = 0.477 at 1 TeV;
- 3.995 at 10 TeV;
- 301.6 at 1 PeV;
- ~220000 at 1e9 GeV.
Equal-rate crossover (DPP asymptotic model): E ≈ 2238.99 GeV.
Literature: https://doi.org/10.1103/PhysRevD.106.123016 ; https://www.mdpi.com/2075-4434/9/4/119 .

**Falsification:** the R64–R67 BW/IC-only model cannot be physically interpreted as complete Hawking energy transport at TeV and above. Even after correcting the BW energy split, dominant four-lepton production is absent. DPP rate alone DOES NOT specify 4-lepton final-state energy distribution, energy transfer, thermalization or BBN constraints.

## Files and next step
Data in same folder:
- IW_DAX_S7_R67_EXACT_BW_VS_R66_PROXIES_20261029.csv
- IW_DAX_S7_R67_ASYMPTOTIC_DPP_CHANNEL_DOMINANCE_20261029.csv
Full local reproducibility packet: IW_DAX_S7_ROTATION_67_REPRODUCIBLE_PACKET_20261029.zip, containing main standalone Python, independent quadrature, numerical controls and SHA-256 manifest.
Next needed: differential four-lepton DPP final-state operator, muon pair production, true deposition response, Hawking source spectra. No original Julia or BlackHawk run; no PBH bound.

VERDICT: DIFFERENTIAL_BW_QED_PASS / DPP_CHANNEL_COMPLETENESS_FAIL / DEPOSITION_OPEN / NO_EXEC / NO_CANON / NO_PBH_BOUND.
