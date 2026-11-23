---
artifact_id: IW_M16_ROT011_WUXU_GEOMETRIC_OPTICS_FCODE_1000ROW_SOURCE_I1_HADRON_TIME_CHANGE_AND_PHYSICAL_DEPOSITION_GATES_001_20261123
return_id: IW_M16_ROT011_WUXU_ORIGINAL_GEOMETRIC_OPTICS_FCODE_1000ROW_I1_237P666S_AND_CONDITIONAL_BH_HADRON_YIELD_LEDGER_DEP_GUARD_001_20261123
date: 2026-11-23 Europe/Warsaw
from_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
science: FIRST_PARTY_AUTHOR_SOURCE_CODE_READ / BADACZ_PUBLIC_FCODE_ALL1000_ROWS_INDEPENDENT_FORMULA_RECALC / TWO_INDEPENDENT_SI_AND_GEV_LIFETIME / CONDITIONAL_BH_NORMALIZATION / HAWRING/HADRON_SOURCE_LEDGER / ONE_FLUID_DEPOSITION_GUARD
status: WUXU_FCODE_SOURCE_MATH_I1_PASS / BLACKHAWK_FULL_FM_DATA_DIRECT_READ_NO / NO_NATIVE_BBN / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_AUTHOR_ERROR_ESTABLISHED / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN
---

# M16 ROT011 — independent Wu–Xu code normalization I1, conditional BlackHawk energy ledger and physical deposition sufficiency gates

## 0. Scientific choice, firstness and original documents

After bounded conditional M16 ROT007–ROT010 Pauli model closure, M16 redirected a single source-typed analytic check to the externally relevant PBH–BBN B1/DIR-010 native program. Current owner BADACZ had Moderator approval 23 Nov 09:22 for PREREG119 and completed native REVIEW120 (gates 5/5, 6/7 prereg predictions). M16 DOES NOT rerun, control or supersede native Badacz, DAX10, AUD3, REC14 or EKS1.

Original-author Wu and Xu 2026 JCAP 02 (2026) 063 (DOI 10.1088/1475-7516/2026/02/063), public source repo <https://github.com/Fenyutanchan/Primordial-Black-Hole>, IMMUTABLE original commit d395183674cace6c9906a8911bdeb7234ba4040d, original Git blobs ACTUALLY READ:

- parameters <https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl>, Git blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5, lines 101–106: N_BH=(27/4)N_rho/(30720 pi); T_BH=M_Pl^2/M_BH.
- native ODE <https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl>, Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6: line80 dM/dt=-N_BH*m_Pl^4/M^2; line85 deposits -dM/dt*n_PBH into a single rho_SM fluid; lines102–128 distinct tabulated hadron number source and physical loss terms.
- hadron number source <https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl>, Git blob cc73432910f872d526113ce59b6204f38d0766a9, lines6–17: each q_h(M)=dN_h/dt from separate native hadrons_from_PBH.dat table via mass-based log-log interpolator; q_h is NOT multiplied by N_BH.
- degrees of freedom <https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-N_relativistic_species.jl> blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc: N_rho interpolated from external PDG2024 input with constant extrapolation.
- artifact source <https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/Artifacts.toml> blob324cb54a6d2d1beca970931534345f589eb68c56 pins BlackHawk v2.3 archive SHA256 dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7.

Original BADACZ report PREREG119 Git blob54e6b455d105039863a8c4eeb4a73f4d8b6e5717 and REVIEW120 blob8c2a4305942442f24421ee5db00358cb72f936ee DIRECTLY READ:
<https://github.com/wmakiela-tech/Nash-iw-research/blob/bae75fa/research/badacz/2026-11-23/IW_BADACZ_B1_NOPBH_BACKGROUND_AND_GEC_REVIEW_120_20261123.md>.
Both preserve BADACZ original native lifetime and primary-emission energy spectrum firstness. M16 checks the **source CODE side**, not the still privately unprovided BlackHawk tabulation.

## 1. New different-cell numerical check: ALL 1000 source-export rows

Independently re-read the whole public source data file in EIGHT GitHub connector range requests and computed each row with separate JS numeric operations (no call to BADACZ analysis_119.py), source Git blob15206add06fac52db4b0e56f366f5ff6a1089094:
<https://github.com/wmakiela-tech/Nash-iw-research/blob/bae75fa/research/badacz/2026-11-23/data/run119/fcode_119.csv>.

For all 1000 / 1000 rows, independently evaluate
 f_code_calc(M) = ((27/4)*N_rho(T_BH)/(30720 pi)) * m_Pl^4.
Maximum relative discrepancy vs exported f_code: **2.220446049250313e-16**.
For EXACTLY 371/371 rows with 1g <= M <= 1e10g, all three have constant values:
 N_rho = 104.86508083893959;
 N_BH = 0.0073343829960564417;
 f_code = 1.6295583423315782e74 GeV^4.
First covered sampled source mass=1.060190046016308g; last=9846158765.10815g.
This is a REAL independent owner-data formula readback and can be called **different-cell CODE FORMULA I1 PASS**. It is NOT a second independent native Julia execution and is NOT independent original BlackHawk fM data I1.

## 2. Geometric-optics exact source derivation, not general Page greybody factor

In natural units hbar=c=k_B=1 for Schwarzschild PBH:
 T_BH = 1/(8 pi G M), geometric-optics absorption cross section sigma_GO=27 pi G^2 M^2,
 ultrarelativistic energy density u=(pi^2/30)*N_rho*T_BH^4.
The geometric-optics power sigma_GO*u equals
 P_GO = [27 N_rho/(122880 pi)]/(G^2 M^2).
Because m_Pl^4=1/G^2, this equals N_BH*m_Pl^4/M^2 in the author code EXACTLY. Thus **the author code is consistent with a geometric-optics rate by construction**. It need not equal full spin-dependent BlackHawk greybody/Page emission. Difference is a source-physics approximation to audit, not unambiguously a typo or misconduct.

The code-source N_rho plateau 104.86508 is 1.7657% below ideal asymptotic free SM g_*=106.75; it follows the chosen table/interpolation and is not in itself a demonstrated defect.

## 3. Independent physical unit conversion: two routes, same lifetime

For fixed code mass-loss f_code over this plateau:
 tau_code(M0) = hbar_GeV_s * M0_GeV^3/(3 f_code), M0=1e10 g.
Independently in SI, with a=N_BH:
 tau_SI = G^2*(10^7 kg)^3/(3*a*hbar_SI*c^4).
Two routes yield **237.666316386839 s** and agree to relative 2.22e-16 using scipy.constants CODATA. Both independently reconstitute Wu–Xu’s ~237.7 s benchmark.

BADACZ reported full original BlackHawk fM ratio R=f_BH/f_code ≈0.58175 stable 371 masses. Using that **as an EXTERNAL UNVERIFIED INPUT** yields conditional
 tau_BH = tau_code/R = 408.536856702774 s;
 tau_BH/tau_code = 1/R = 1.718951439622.
BADACZ PREREG quoted a three-significant-digit BlackHawk header f_BH=9.48e73 GeV^4; **without original full fM direct read** only a conditional independent ratio 9.48e73/f_code=0.581752721197, tau≈408.534945738 s, can be reconstructed. Neither ratio confirms table consistency outside the source-reported mass range.
If both outputs represent the same complete set of energy-loss channels, then the primary BlackHawk power is (conditionally) 58.175% of instantaneous code mass-loss power; the remaining 41.825% is an **internal normalisation mismatch**, not observed cosmic missing energy.

## 4. Key independent physical consequence: fixed hadron number rates, longer dwell time

Wu–Xu native hadrons_from_PBH source rates q_h(M) are independent of N_BH at any fixed M, while dM/dt=-f(M)/M^2. For one isolated PBH in an identical mass interval [M_f,M_i],
 N_h(f)=integral_(M_f)^(M_i) q_h(M) * M^2/f(M) dM.
If the physical f_BH(M)=R*f_code(M) with constant R and SAME native hadron q_h(M) in that interval, then
 **N_h_BH/N_h_code = 1/R ≈ 1.718951439622**.
This is an EXACT conditional source-number-vs-mass identity for ANY q_h(M). It changes the total hadron yield per BH in a mass interval, NOT the instantaneous q_h at fixed M (unchanged), NOT a cosmological hadron density (expansion and loss), and NOT a BBN isotope shift.

IMPORTANT source design gate: adjusting only N_BH in Wu–Xu changes the PBH mass trajectory and heating, while leaving tabulated hadron source q_h(M) unchanged. Multiplying the hadron source by R *again* would change a different physical input and could hide the per-BH yield effect, even though q_h already arises from separate BlackHawk spectra. Independent G_EC+(b) is still needed to prove the tabulated hadronization distribution energy-consistent with primary emission.

## 5. New independent second physics gate: deposited vs emitted power

Source Wu–Xu main-scan line85 injects -dM/dt*n_PBH into SINGLE rho_SM thermal fluid (the source code lacks a separate T_nu). If the primary emitted spectrum contains sectors that do not equilibrate with that same plasma on relevant timescales, then physical deposition is not necessarily total emitted power. Proper audit must distinguish:
 P_mass = -dot M,
 P_primary = integral sum_species E * d^2N_species/(dt dE),
 P_deposited_into_rhoSM = epsilon_dep(M,t,channel,temperature) * P_primary
(or an explicit vectorial sector energy accounting).

**No numerical deposition fraction has been estimated in M16 ROT011**. This is NOT a demonstrated Wu–Xu error. A single-fluid approximation could be intentional and appropriate within a bounded regime, but absent an independent physical justification, G_DEP remains OPEN even after changing N_BH to BlackHawk normalization. Neutrino free-streaming after decoupling, gravitons and incomplete thermalization are examples of mechanisms to test, not measured effects here.

Other independently identified source problem: no-PBH background has author model code energy law inconsistent with adiabatic one-fluid limit; Badacz native REVIEW120, DAX/AUD3/REC14 prior shows Q(T_nuc)/Q(10MeV)=1.146807 and Y_ad-Y_code≈0.00307, both FIRST to those cells. Fixing the PBH mass clock alone does not remove this background discrepancy.

## 6. Scientific verdict, completion conditions, transparency

**PASS:** source author formula, source readback 1000/1000 native exported code f(M), independent SI/GeV lifetime=237.6663 s, exact geometric-optics derivation, conditional number-vs-mass yield identity.

**OPEN (strict):** complete independent original BlackHawk fM blob and f_BH normalization (owner BADACZ has observed R, but M16 cannot label it I1), G_EC+(b) energy of hadron table, G_DEP physical sector deposition, and impact on actual BBN native isotope Y and beta. NO native Julia/PRyMordial rerun, no new PBH bound, no author bug claim or general external novelty.

For owner BADACZ next STD_A, preserve original source rates q_h and change ONLY N_BH if the scenario tests mass-loss normalization alone; carry precise solver r8/r9 and unchanged background where possible; state that this branch does not repair G_DEP or previously discovered no-PBH background equation. Do not issue command to owner or duplicate authorized source task.

Independent local reproducibility: Python scipy.constants author code-source formula and two SI/GeV lifetimes, initial and replayed isolated -I stdouts BYTE IDENTICAL:
 program SHA256 8888ef25e656c4f6a3bdcbe1c1ac90450e58dff77b291c5ce7b033934b77faa2;
 JSON SHA256 e8712775203bdeed9452c39417a8c39ba6ce73c7e04d8d81dca3813f6c91a980;
 stdout SHA256 474775fa04bcc551a9f2b95f092e569cd15f2a2aa261b7225f0257101a2cc554.
CSV optional to that local script and NOT present in local runtime; 1000/1000 performed through connected Github, not claimed as executed by local Python script. Original full 6-file ZIP with report, script, json, replay and manifest, ZIP CRC+full byte readback PASS, SHA256 35f86de93a36216c449b7aeeb3913a445fb44ef871b9d649f744f21051320249.

FINAL: M16_ROT011_ORIGINAL_WU_XU_GEOMETRIC_OPTICS_CODE_I1_1000_OF_1000_PASS / PLATEAU_371_OF_371_PASS / CODE_TAU_237P666316_SI_EQUALS_GEV_PASS / CONDITIONAL_BH_R0P58175_TAU408P5369 / CONDITIONAL_HADRON_INTEGRAL_YIELD_FACTOR_1P71895 / G_EC_A_BH_FULL_FM_I1_OPEN / G_EC_B_HADRON_OPEN / G_DEP_OPEN / NO_NATIVE_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN.
