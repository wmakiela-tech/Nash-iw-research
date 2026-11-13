---
artifact_id: IW_DAX_S8_ROT025_MASSIVE_FD_STATIC_DEBYE_SCREENING_AND_ENERGY_LOSS_REGIME_FALSIFIER_001_20261113
date: 2026-11-13
cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
class: MASSIVE_FERMI_DIRAC_STATIC_LONGITUDINAL_DEBYE / ORIGINAL_HEAVY_PARTICLE_QED_STOPPING_APPLICABILITY_NEGATIVE_GATE
status: GITHUB_PENDING_BW_INGEST
ceiling: NO_PHYSICAL_PI_E_STOPPING / NO_DYNAMIC_SCREENED_PION_TRANSPORT / NO_BBN_OR_PBH_BOUND / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT025 — finite-mass e± static screening and pion stopping-formula regime audit

13 Nov 2026. The full original 14-member locally verified source+script+JSON/CSV research bundle is available in the originating conversation; this public text is the standalone scientific summary. The result is a quantified **STATIC LEADING-ORDER** screening scale and an original-literature formula-veto, not a pion stopping power.

## Firstness, inherited source, and original prior art

DAX-S7 R68 FIRST conditional three gamma gamma photon channels; DAX-S8 ROT017 source-pinned real Rivet/Belle 140x12 pion observations, ROT019/020 the conditional pion daughter LAB energy and 1st-neutrino moments, ROT021-022 partial cutoff-dependent point-scalar pion-photon scattering, ROT023 original four PDG/COMPAS piN datafiles, ROT024 massive FD e± plasma density and conditional baryon entropy correction. ROT025 addresses a separate pion-lepton Coulomb-plasma screening preflight. No claim of novel field theory, native BBN network, or entire pion transport.

**Frozen input provenance:** ROT024 53-digit source-typed ideal FD e± snapshot exact JSON, SHA256 fa7cf4cd416408a585eb4847fe9e1181e83fdedbcfd61a9dbe9491f31ce9bf2f, preserved byte-exactly in full ROT025 package and numerically rechecked.

Original publication interfaces:
- Braaten/Thoma, *Energy loss of a heavy fermion in a hot QED plasma*, PRD44 1298 (1991), DOI https://doi.org/10.1103/PhysRevD.44.1298 , original publisher abstract. Leading-order heavy-charge stopping needs properly screened SOFT and recoil-correct HARD momentum transfers.
- Comadran/Manuel/Carignano, *Accounting for plasma constituent mass effects in heavy fermion energy loss calculations in hot QED and QCD*, PRD107 116016 (2023), DOI https://doi.org/10.1103/PhysRevD.107.116016 ; arxiv https://arxiv.org/abs/2304.14182 . Original source explicitly assumes m_e << T << M and E << M²/T. Pion is a charged COMPOSITE SCALAR, not its heavy fermionic probe.
- Peigné/Smilga, *Energy losses in relativistic plasmas: QCD versus QED*, 2009 original review https://ufn.ru/en/articles/2009/7/a/ : collisional + radiation channels.
- Wang/Bertulani/Balantekin, *Electron screening and its effects on big-bang nucleosynthesis*, PRC83 018801 (2011), DOI https://doi.org/10.1103/PhysRevC.83.018801 , established BBN screening prior art for NUCLEAR reaction rates, not pion stopping.
- CODATA2022 m_e and hbarc as frozen in ROT024 source.

## Correct massive equilibrium FD leading-order STATIC electric screening

At R68 T=0.07818527068831995MeV, m_e=0.51099895069MeV, alpha=1/137.035999084, hbarc=1.973269804e-11 MeV·cm and e²=4 pi alpha, electron and positron net mu/T<2.015e-8 from ROT024. Define FD f(p)=1/(exp(sqrt(p²+m_e²)/T)+1). For each spin-two species n_e=1/(pi²(hbarc)³) integral p² f(p) dp.

The static long-wavelength electric susceptibility of both opposite charges is

m_D² = e² [d(n_e−(mu) − n_e+(−mu))/dmu]_(mu=0)
     = (2 e²)/(pi² T) integral_0^infty p² f(p)[1-f(p)] dp.

This is the leading free massive-QED *longitudinal static* polarization, not the whole finite-frequency / finite-momentum photon self-energy or gauge-safe full energy loss.

Executed original 50digit source results:

| Quantity | R68 |
|---|---:|
| n_e+ = n_e− | 2.497683291034352e26 cm^-3 each |
| total n_e± | 4.995366582068704e26 cm^-3 |
| m_D² | 4.499675986912470e-6 MeV² |
| **m_D** | **2.121243971567738 keV** |
| **Debye length** | **0.930241797006322 Å** |
| Wigner–Seitz mean radius | 7.818342207477432e-10 cm |
| e± particles per Debye sphere | 1684.39335955448 |
| Coulomb coupling alpha hbarc/(a_WS T) | 0.00235565768164630 |

Since N_D>>1 and Coulomb coupling<<1, classical weak-coupling *static* screening is model-consistent. These conditions do not validate a full pion loss calculation.

Two DISTINCT limits:
(a) classical DEBYE using ACTUAL massive e± density, m_D,classical²=e²(n_e+ + n_e−)/T, differs by 0.0451% at m_D²: exact FD/classical = 0.99954929712063.
(b) ULTRARELATIVISTIC MASSLESS e± screening m_D,ultra²=e²T²/3 predicts m_D=13.66947746989keV, **6.44408548** times over the massive result, squared-mass factor **41.52623763**. It is out of regime because m_e/T=6.53574447196. The massless formula's mathematical integral limit was checked using integral_0^inf q² f(q)(1-f(q)) dq=pi²/6.

Illustrative maximal ideal free-proton STATIC susceptibility relative to massive pair susceptibility is ~2.0141e-8 under the hypothetical assumption all baryon number is free unit-charge targets at the same T (ROT024 entropically corrected n_b). Does NOT imply proton/nucleus interaction rates are negligible.

## Published pion stopping formula *does not transfer* to R68

At inherited source conditional pion energy E_pi=718277.144397855 MeV, pion mass 139.57039MeV,

m_e/T=6.53574447196149, not <<1,
T/m_pi~0.0005602, <<1,
m_pi²/T=249.150429400 GeV,
E_pi/(m_pi²/T)=2.88290550462837, NOT <<1.

Hence Comadran et al (2023) assumed light-plasma-fermion expansion and its stated E<<M²/T energy range are BOTH invalid here. It moreover treats an elementary heavy fermion, not a pion. Reusing a quoted asymptotic stopping-power equation without rederiving massive-lepton and scalar-pion hard/soft kernels is not scientifically justified.

Physical pion-lepton stopping needs the full frequency/momentum longitudinal+transverse thermal polarization and Landau damping, Pauli blocking of *massive* e±, consistent soft/hard exchange matching without arbitrary scale remnants, scalar pion differential amplitudes and possible composite form factors at high transfer, and energy-changing stochastic transport plus radiation. STATIC m_D is an IR scale, not a stopping power; a total Coulomb collision cross section cannot replace an energy-transfer-weighted differential kernel. ZERO physical dE_pi/dx or neutrino yield computed.

## Thermal sensitivity snapshots (independent SciPy)

T(MeV), m_D(keV), Debye length(Å), particles per Debye sphere:
0.060: 0.7164293, 2.754312, 3825.77
0.070: 1.3901899, 1.419425, 2300.54
0.07818527: 2.1212440, 0.930242, 1684.39
0.090: 3.4351178, 0.574440, 1198.03
0.100: 4.7532846, 0.415138, 962.74

## Independently executed controls and negative knowledge

A: mpmath50 massive FD integral, separately convergent Bessel K2 fugacity series (n_e and charge susceptibility), prior ROT024 source-input check and exact massless limit. B: separately written dimensionful SciPy momentum integral, SciPy fugacity series and independently evaluated finite-chemical-potential derivative, agreement at floating precision (finite difference error ~1.67e-9). Earlier finite difference mu/T=1e-3 failed a strict 1e-7 tolerance (actual ~1.64e-7); repaired by finer mu/T=1e-4 and recorded as an author numerical negative control, not physical source anomaly. C: separately written SciPy five-temperature scan.

Local source-complete original 14-member ZIP CRC PASS, SHA256 12/12 content member PASS, three scripts after CLEAN extraction recreate three frozen JSON/CSV result files byte-identically PASS; ZIP SHA256 **36d4c7124b9a5e09691a0b56d1057bfcdf3f847e774e13087df7ff5c2b98372f**. Author-controlled reproducibility, NOT external referee or native BW ING receipt.

DISPOSITION: MASSIVE_FD_STATIC_DEBYE_SCREENING_PASS / MASSLESS_QED_SCREENING_FORMULA_OUT_OF_DOMAIN / COMADRAN_2023_STOPPING_FORMULA_OUT_OF_DOMAIN / FULL_PION_ELECTRON_ENERGY_LOSS_OPEN / GITHUB_PENDING_BW_INGEST / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN.