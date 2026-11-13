---
artifact_id: IW_DAX_S8_ROT026_EXACT_HARD_PION_LEPTON_FD_THERMAL_FIRST_ENERGY_LOSS_GATE_001_20261113
date: 2026-11-13
cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
class: MOVING_MASSIVE_FD_ELECTRON_POSITRON_HARD_SPACELIKE_SINGLE_PHOTON_SCALAR_PION_ENERGY_TRANSFER
exposure: PUBLIC
bw: GITHUB_PENDING_BW_INGEST
ceiling: NO_IN_MEDIUM_PION_STOPPING / NO_FULL_SOFT_HARD_MATCH / NO_FULL_PION_CASCADE / NO_COSMIC_NEUTRINO_YIELD / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT026 — first energy moment of selected hard π±e± scattering in R68 massive FD bath

13 Nov 2026. Original author application of MATURE one-photon QED, not original field theory or full physical cosmic pion energy loss.

## Original provenance / firstness

DAX-S7 R68 original three source channels; DAX-S8 ROT017 real secondary SHA-pinned Belle/Rivet 140x12 pion production source; ROT019 pion LAB second moment, ROT020 conditional pion free-decay first-neutrino moments; ROT021–022 limited real-photon pion Compton; ROT023 4 original PDG pi+p/pi-p hadron datasets; ROT024 equilibrium e± FD density and entropy time-label correction; ROT025 correct static massive-FD Debye screening m_D=2.121244keV and stopping formula veto. ROT026 instead uses a finite spacelike Q² window in **virtual** one-photon pion–lepton elastic scattering.

Frozen original ROT024 exact thermodynamics JSON SHA256 fa7cf4cd416408a585eb4847fe9e1181e83fdedbcfd61a9dbe9491f31ce9bf2f; T=0.07818527068831995MeV, total n(e−)+n(e+)=4.9953665820687041e26/cm³ and m_e=0.51099895069MeV. Original ROT020 Belle/Rivet source mean pion-pair energy JSON SHA256 7ebc9d3a08ba9e78e82017ff53a248ffb62d626de64db2addfb5534e77e09f08, implying one representative E_pi=718.277144397855GeV, NOT full source-energy distribution. Both source bytes saved in original local archive.

Mature first-source contact: Kaiser 2011 one photon plus radiative pion-electron QED https://doi.org/10.1088/0954-3899/38/2/025003 ; Blunden/Melnitchouk/Tjon pion spin-zero EM current and TPE https://arxiv.org/abs/0911.3619 ; Ananthanarayan/Caprini/Das 2018 dispersive pion form factor and charge radius 0.657±0.003fm https://doi.org/10.1103/PhysRevD.98.114015 ; original direct pi-e at p_pi=50GeV/c, Q²=[.013,.036]GeV², Adylov et al https://doi.org/10.1016/0550-3213(77)90056-6 . No one directly measured pion energy loss at R68; no full Fpi or two-photon amplitudes were evaluated.

## Exact model mathematics

Spin0 pion current (P+P')μ Fπ(t) and spin1/2 lepton current give spin-averaged one-photon **vacuum tree** differential cross section, with t=−Q², lambda=[s−(M+m)²][s−(M−m)²]:

dσ/dQ² = 4πα²/lambda *[(s−M²−m²)² −Q²(s−m²)]/(Q²)² |Fπ(−Q²)|².

Electron initially stationary: its exact lab energy gain is Q²/(2m). For moving thermal electron LAB energy eps and momentum k, angle μ, s=M²+m²+2(Eeps−pkμ). Average final electron LAB energy gain over final-scattering azimuth:

<ΔEe> = Q² *[(E+eps)(s+m²−M²) −2s eps]/lambda.

Incident relative flux per pion LAB travel distance is sqrt(lambda)/(2p eps). Integrate ideal massive FD momentum p_e² dp_e, incoming isotropic μ, and exact finite-Q² differential amplitude times mean energy gain for author-chosen HARD SLICE **0.001≤Q²≤0.010GeV²**. NO IR q→0 encountered and NO arbitrary Debye insertion. STATIC ROT025 mD²=4.4996759869e−12GeV²; source Q²min/mD²≈2.22238e8, a hierarchy, NOT a proof that dynamic in-medium photon screening corrections vanish.

## Executed numeric results, true moving massive FD incident distribution

Fixed initial E_pi=718.277GeV:
- selected vacuum-Born hard pion–lepton encounters per pion LAB centimetre: **0.116806741390573/cm**, mean free path **8.56114970844cm**;
- mean LAB pion energy lost per selected encounter: **2.01888566818GeV**;
- initial conditional hard-slice local energy-loss coefficient: **0.235819456140115GeV/cm**;
- initial local loss length E_pi/B_hard: **30.4587736803m**.
- Artificial REST electron bath at same number density: 0.29165284750GeV/cm, so real massive thermal momentum reduces this particular first-loss moment by **19.1438%**. No stationary-lepton approximation is substituted for the FD result.
- Author MONOPOLE pion Fπ(-Q²)=1/[1+(rπ²/6)Q²], matching ONLY the experimentally sourced pion radius slope, gives **0.232471458960675GeV/cm**, a 1.41973% lower model case. Radius alone does NOT prove this form-factor curve or physical bound.
- In an author chosen [.015,.036]GeV² interval overlapping a pion–electron experimental Q² range (but different pion beam energy), point Fπ source-model loss .08730057GeV/cm; monopole .08008907GeV/cm. NOT measured R68 plasma rates.
- Under the SAME fixed Q² model, initial parent E varied 280..1250GeV, initial B_hard varies .233793..236342GeV/cm (max/min1.0109016); NOT full 140x12 Belle energy folding.
- Vacuum pion decay mean path 40.16463569km. Two FROZEN FIRST-EVENT clocks (this selective hard channel versus decay) give P_free_decay_before_first_hard≈2.13151e−6 and local decay length /cooling length ~1318.66; NOT eventual pion suppression or physical neutrino yield, since elastic pi-e event does not destroy pion.

## Two independent codes, self-corrected failures and custody

A: independently coded SciPy/Numpy 80x60 thermal FD incoming Gauss nodes and exact analytic transfer integral in finite Q², plus independent numeric pion monopole integrals. B: independently written 54x48x48 direct **three-variable k,μ,Q²** integration using no analytic Q² primitive from A gives **0.23581945614011626GeV/cm**, ~5e−15 relative mismatch. B tests FOUR explicit NONHEADON Lorentz pion/electron 4vector scatterings with 16 outgoing azimuth values each; transfer equation matches to ~3.01e−10 rel. C: original fixed-pion energy sensitivity source scan. D: compact locally executed public Python reproducer. Initial BAD B quadrature omitted lower interval endpoint, admitted bogus Q²≈0 and inflated result ~580x. Fixed by x=a+(1+node)(b−a)/2 and cross-checked against A; corrected result ONLY. Another correction FD cutoff from k/T=20 (8.54e−6 tail) to32 (1.84e−10 tail). Both source-negative findings preserved.

Complete original 17-file conversation ZIP: full longer author report, audit, original TWO inherited JSON source bytes, four original executed scripts, frozen JSON/CSV, environment, manifest and verifier. ZIP CRC PASS, SHA256 **16/16 member PASS**, clean four-script replay generates FIVE byte-identical frozen files PASS, ZIP SHA256 **8231ca424b2a3c52f548e589fa579eff16e659c15758a59b6cdc5514e83b3735**. Author reproduction, not external referee.

STRICT OPEN: true finite-T dynamic longitudinal+transverse photon response and Ward-consistent soft/hard matching; composite pion source Fπ and photon loops/radiative processes, full Belle parent-energy ensemble, postcollision changing pion energy and final muon/neutrino escape/deposition. Only an author-scoped hard vacuum one-photon rate integrated against thermal initial occupation was computed, NOT true physical pion stopping in R68. No new XH task cascade or KN13 acceptance. GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.

RETURN: FINITE_Q2_MOVING_MASSIVE_FD_QED_ONE_PHOTON_HARD_ENERGY_MOMENT_PASS / FULL_IN_MEDIUM_STOPPING_UNVERIFIED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.