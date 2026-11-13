---
artifact_id: IW_DAX_S8_ROT021_CHARGED_PION_SOFT_COMPTON_VS_VACUUM_DECAY_COMPETITION_GATE_001_20261113
date: 2026-11-13
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
research_class: POINT_SCALAR_BORN_SOFT_CHARGED_PION_COMPTON_FIRST_ENCOUNTER_VS_VACUUM_DECAY / EXACT_PLANCK_ANGLE_REDUCTION / INDEPENDENT_DIRECT_INTEGRAL / NEGATIVE_KNOWLEDGE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_COMPOSITE_PION_QCD_RATE_OR_ERROR_BOUND / NO_PION_ENERGY_TRANSFER / NO_EVENTUAL_NEUTRINO_YIELD / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT021 — soft photon-pion Compton versus first free charged-pion decay in R68

**13 November 2026.** Source-typed, bounded positive FIRST-ENCOUNTER test. This challenges one specific assumption left OPEN by ROT020: an ultrarelativistic charged pion in the hot R68 bath undergoes free two-body decay without prior electromagnetic encounters. It is NOT a physical loss of pions, neutrino transport simulation, complete charged-pion scattering cross section, or cosmic PBH/BBN claim.

## Custody and firstness

DAX-S7 R68 FIRST addressed conditional first-event interaction among 3 specific photon-photon channels; it did not claim complete Standard Model processes. DAX-S8 ROT012 introduced source-conditional point-Born pion pair production, ROT017 FIRST in this DAX branch obtained original SHA-verified officially packaged SECONDARY Rivet-data Belle gamma-gamma pion reference 140x12, ROT019 FIRST extracted the fiducial LAB pion pair energy-splitting moment, and ROT020 FIRST applied the in-vacuum charged pion -> muon + first-generation neutrino exact decay moments. ROT020 explicitly left charged-pion decay VERSUS COLLISION hazard OPEN. Its source-conditioned MEAN single-pion LAB energy is 718277.14439785519748970605269061100285974825 MeV. **ROT021 uses this single mean parent energy, NOT the full Belle 140x12 parent-energy distribution**; nonlinear ensemble probabilities are NOT claimed.

Actual Belle/Rivet SHA-pinned reference source: compressed BELLE_2007_I749358.yoda.gz SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403, original Rivet 4.1.2-2.1 package SHA256 8bed5d37a841e90ffaf1af8fd6f28fc2823c38af87e884d2b78a99a378fc489b, acquired at https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 . This is a SECONDARY numerical reference; original primary HEPData ins749358 byte equality remains not established. The ROT020 frozen result JSON and source YODA SHA included in the original local package for a clear baseline receipt, but ROT021 new collision calculation uses the frozen mean, NOT 140x12 convolution.

## Original literature

- Charged-pion mass m_pi=139.57039 MeV; charged-pion c tau=7.8045m from Particle Data Group 2025 light-meson table https://pdg.lbl.gov/2025/tables/rpp2025-tab-mesons-light.pdf .
- Pion electromagnetic Compton source: J.M. Friedrich (2012), *Chiral Dynamics in Pion-Photon Reactions*, section 2.2.1, original scalar-charged pion real Compton Born plus polarizability amplitudes, https://wwwcompass.cern.ch/compass/publications/theses/2012_hab_friedrich.pdf ; Moinester and Scherer (2019), *Compton Scattering off Pions and Electromagnetic Polarizabilities*, https://arxiv.org/abs/1905.05640 . Correct charge-Born threshold is Thomson; REAL pion structure/polarizability corrections are NOT certified here.
- Planck photon density 2 zeta(3) T^3/pi^2 from Particle Data Group big bang review https://pdg.lbl.gov/2015/reviews/rpp2015-rev-bbang-cosmology.pdf . Convert with hbar c=1.973269804e-11 MeV cm.

## Defined model and exact flux formula

E_pi FIXED at 718.277144397855197 GeV (conditional source mean), T_gamma=0.07818527068831995MeV (R68), m_pi above, gamma=E_pi/m_pi=5146.3433210859065, beta=sqrt(1-gamma^-2). Thermal bath photons are isotropic in LAB. Their energy is epsilon=Tx and direction cosine mu to the pion velocity. Incident relative photon flux factor is t=1-beta mu, and exact photon energy in pion rest is omega=gamma T x t. **Select ONLY omega<=m_pi/20=6.9785195MeV**. High pion-rest photon energies, where Thomson fails, are EXCLUDED.

For a charged POINT-SCALAR pion with Born-level elastic Compton scattering in its rest frame, z is the scattered photon angle and

d sigma_B/dz = (pi alpha^2 / m_pi^2) (1+z^2) / [1 + (omega/m_pi)(1-z)]^2.

Define sigma_Th=8pi alpha^2/(3m_pi²) = 8.9173460480236483e-30cm² (8.917 microbarn), R_B(omega)=sigma_B(omega)/sigma_Th. These are point-scalar QED model quantities; no quantified physical strong interaction error bar.

The ideal blackbody density at R68 is n_gamma=1.5152025724753423e28 photons/cm³. Using sigma_Th for ALL bath photons would produce a bogus ~0.074m collision length, because generic photons are boosted far outside the Thomson regime; THIS IS EXPLICITLY REJECTED.

Define soft collision flux response F_B(omega0)= [1/(2zeta3)] integral dx x²/(exp(x)-1) integral_-1^1 dmu/2 t R_B(gamma T x t) 1(gamma T x t <= omega0).

Positive Fubini and omega=gamma T x t give EXACTLY

F_B=1/[4 beta zeta3 (gamma T)^2] * integral_0^omega0 d omega
 omega R_B(omega) ln{ [1-exp(-omega/((gamma T)(1-beta)))]/[1-exp(-omega/((gamma T)(1+beta)))] }.

F_Th is the same with R_B=1 and is a FLUX-weighted soft sector, NOT an ordinary photon-number fraction.

For stationary independent two-clock rates ONLY UNTIL THEIR FIRST EVENT:
lambda_soft=beta/(n_gamma sigma_Th F_B),
lambda_dec=beta gamma c tau_pi,
tau_* = gamma (c tau_pi) n_gamma sigma_Th F_B [consistent cm unit conversion],
P(first event is free charged-pion decay)=1/(1+tau_*).

## Executed results and conservative model inequality

At mean source pion energy, omega0=m_pi/20:
- F_Th=0.0001642367729076850532842764.
- Soft Born/Thomson collision flux ratio F_B/F_Th=0.9400634084135743222713136.
- lambda_soft Born=**479.36477888369652 metres**.
- lambda_dec=**40164.635691158115 metres**.
- tau_*=**83.7872064457678037**.
- P(free decay before first soft Compton within the two-process fixed-parent model)=**0.0117942321951558472**, approximately **1.1794%**.

Pointwise Born model inequality: since omega<=omega0 and 0<=1-z<=2, R_B(omega) >= (1+2omega0/m_pi)^(-2)=**100/121**. Therefore WITHOUT detailed Born outgoing-angle integration:
tau_* >= **73.6605898517511967** and P_decay_first <= **0.0133939472214944544** (1.3394%). The inequality is STRICT in the specified scalar Born model, **NOT** a certified bound for a real composite pion with unquantified polarizabilities.

Sensitivity tests (not proof of exact source energy support):
- E_pi=300GeV at cutoff m_pi/20: soft mfp 100.170m, P_decay_first=0.594%.
- E_pi=1200GeV same cutoff: soft mfp 1219.289m, P_decay_first=1.785%.
- E_pi=718.277GeV cutoff m_pi/40: soft mfp 1643.991m, P_decay_first=3.932%.
- E_pi=718.277GeV cutoff m_pi/100: soft mfp 8737.573m, P_decay_first=17.867%.

This model decisively warns against lifting ROT020 free-decay-before-collision assumption to physical neutrino yield. An ELASTIC collision leaves a pion, which may subsequently decay. **FIRST COLLISION != PION DESTRUCTION != NO NEUTRINO**. After the first scatter the charged pion energy/momentum may change, so the two fixed hazard clocks cannot be iterated as a physical cascade. No fully propagated pion energy-loss or eventual escaped-neutrino fraction follows.

## Reproduction, corrections, claim ceiling

Two original author-executed independent algorithms: (A) mpmath55 1-D exact reduced omega Planck kernel with independently evaluated 22pt outgoing Born angular response and 9 sensitivity cases; (B) separate SciPy ORIGINAL 2D photon bath x,mu integration with 22pt incident angular Gauss and independently written 24pt outgoing Born kernel, 5 cases. Benchmark independent mfp=479.3647788836906m, tau=83.78720644576883, relative agreement ~1e-14. Unit-typed duplicate tau=gamma c tau n sigma F identity passed. Full original local bundle has the original source YODA and prior ROT020 frozen mean, two executed original scripts, third compact public script, three generated frozen JSON/CSV outputs, report, source audit, README, environment, manifest and replay verifier. ZIP CRC PASS, SHA256 13/13 member bytes PASS, TWO scripts rerun in clean isolation generating THREE byte-identical source/derived result files PASS. Local ZIP SHA256 ca93925339ec96e5c913ac389f8fd4c3e7b29cfca7e6a6e45b443b3f4b2db3bc.

Self-corrected implementation negative knowledge: a naive log(1-exp(-small)) produced inf/NaN, repaired via log(-expm1(-small)); initial scratch mixed c tau in METRES with n sigma in per CENTIMETRE and gave a wrong factor100 before a direct dimensional cross-check caught it. Both failures preserved in original report, not promoted as source physics errors.

STRICT OPEN: real pion polarizability/error control; real inelastic photon-pion QCD and other plasma collisions; pion FOUR-VECTOR energy changes per collision; eventual pion decay after a sequence; muon decay (polarized), neutrino interactions, escape/deposition; original HEPData data identity, exact source 5MeV fiducial bin semantics; full PBH/BBN physical target. Reopen only with energy-transfer kernel and verified environmental scattering rates, not an automatic owner task cascade. Existing XH-S6 science ownership is for other scope; KN13 BW source intake not presumed. GITHUB_PENDING_BW_INGEST / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN.

**DISPOSITION: SOFT_POINT_SCALAR_BORN_FIRST_SCATTER_COMPETES_STRONGLY_WITH_VACUUM_DECAY / FULL_TRANSPORT_OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.**
