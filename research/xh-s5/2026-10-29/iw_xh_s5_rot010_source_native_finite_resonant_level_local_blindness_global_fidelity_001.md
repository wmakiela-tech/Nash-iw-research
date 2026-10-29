# XH-S5 ROT010 — Exact local-marginal blindness versus global fidelity in the source-native resonant-level quench

artifact_id: IW_XH_S5_ROT010_RESONANT_LEVEL_LOCAL_GLOBAL_FIDELITY_20261029
return_id: XH-S5-ROT010-RESONANT_LEVEL_LOCAL_MARGINAL_BLINDNESS_GLOBAL_RETURN_001_20261029
date: 2026-10-29
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: ORIGINAL_2026_EQ1_MODEL_EXECUTED / EXACT_MATURE_LOCAL_MARGINAL_BLINDNESS / INDEPENDENT_JORDAN_WIGNER_REPLAY / NO_eNRG_REPRODUCTION / NO_MATHEMATICAL_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## PRIMARY ORIGINAL SCIENCE, provenance
Picoli, Diniz, Oliveira, "Real-Space Renormalization-Group Study of Decoherence and Revival Following a Sudden Quench in a Finite System," Brazilian Journal of Physics 56:246, published 28 Oct 2026, DOI https://doi.org/10.1007/s13538-026-02169-6 ; authors' preprint https://arxiv.org/abs/2605.01612 . Source Eq.(1) finite spinless resonant-level impurity-metal Hamiltonian, switches Eq.(2)/(3), many-body Slater overlap Eqs.(27–28) and Rabi Eq.(14). Authors ALREADY distinguish n_d(t) from global manybody F(t), explicitly report switch-off n_d conserved, oscillating F, and finite-size recurrences; no XH discovery or criticism of that distinction. Authors use eNRG on long-time chains: NOT executed or source plot reproduced here. Source is computational theory, NOT actual measured quantum hardware.

## Exact two-intervention observation-level witness, same initial state
Source Eq.(1): H(V) = eps_d n_d -tau sum_{j=1}^{L-1}(c_j†c_{j-1}+h.c.) + V(c_d†c_0+h.c.), L even, N=L/2+1 electrons. Set hbar=tau=1, eps_d=-0.3, Gamma=0.3, V=sqrt(tau Gamma); L in {4,6,12,24,40}. Prepare the **SAME ground state of H(V)** before t=0 and apply:
- STAY: keep coupling V, initial state is eigenstate, global fidelity F_stay(t)=|<Psi0|Psi_stay(t)>|²=1 for ALL t.
- OFF: at t=0 set V=0, [H_off,n_d]=0 so n_d_off(t)=n_d(0) for ALL t. Fixed total particle number makes the **entire reduced impurity density** exactly rho_d(t)=n_d|1><1|+(1-n_d)|0><0| for BOTH processes and every t.

Thus all one-time local POVM snapshots have identical distributions for all times, even with arbitrarily many fresh independent copies, although global states may differ. The local observation operator annihilates a genuine difference of global dynamics. Crucial: this is **not** equality of multi-time process tensors, interventions/records, bath observables or same-system sequential invasive measurement statistics. And an investigator who knows the intervention already knows the protocol, so observation-only reconstruction must be kept separate from intervention metadata.

## Source-native executed numerical result
Global free-fermion Slater overlap F(t)=|det(Uocc† exp(-i h_final t) Uocc)|². L=24, eps_d=-.3, Gamma=.3, t=8:
- n_d=0.8083093378258936 for STAY and OFF, whole local rho identical.
- Local purity n_d²+(1-n_d)² = 0.6901092955812818 both, no change.
- Global F_stay(8)=1; F_off(8)=0.4438994229713101. Difference 0.5561005770286824.
- Global pure-state trace distance sqrt(1-F_off)=0.7457215143930676; local reduced-state trace distance=0 EXACT by conservation.
- Equal-prior optimal ONE global-copy Helstrom error = (1 - sqrt(1-F_off))/2 = 0.1271392428034662. Any single-time LOCAL measurement of impurity alone remains at uninformative prior binary risk 1/2.
- OFF fidelity t=5:0.4666429890774052, t=60:0.7064131009410991, t=80:0.37928284566477966. The increase at 60 is a FINITE-TIME PARTIAL RETURN, not a certified global recurrence period nor reversible physical entropy claim.
- At L=40,t=8, n_d=0.797139460078143 and OFF F=0.40675612333760075, STAY F=1. All are simulated, not measured.
- L24 OFF maximum n_d deviation over 801 points t in [0,80]: 4.44e-16, OFF vs STAY max n_d discrepancy 1.78e-15 numerical; exact operator equality proven above.

## Independent execution and controls
Algorithm A Python/NumPy directly diagonalizes Eq.(1) 1-particle source H for L=4,6,12,24,40, then computes n_d and Slater overlap F for ON, OFF and STAY. Independent fixed-particle-number Fock Hamiltonian on C(L+1,N) configurations at L4/6 agrees for n,F <=3.19e-14. Original source Rabi Eq.(14) for the impurity + one site controlled to 1e-12. Algorithm B constructs literal 2^(L+1)-dimensional Jordan-Wigner creation/annihilation matrices (L4=32, L6=128), prepares Slater initial state by fermionic creation on vacuum, independently evolves it under second quantized H and compares ALL on/off/stay time samples: maximum occupancy discrepancy 6.66e-15, fidelity 8.66e-15. This is an actual two-implementation full-Fock cross-check, not an author eNRG reproduction.

Local complete ZIP (full Markdown, two runnable sources, two JSON frozen outputs, SHA256 member manifest, README, replay control):
IW_XH_S5_ROT010_RESONANT_LEVEL_GLOBAL_FIDELITY_REPRO_20261029.zip
ZIP SHA256 2761460fb0db5945df08e9ef0404971a1a568c202523ae03bb18b3ed7b1ad0ff
Full local report SHA256 504b3115b71a2f17fd8bf3a8d96200ec79cc7d98be9fd8588589c60579c8a126.
CRC ZIP PASS; SHA256 manifest 7/7 PASS; separate clean extracted script replay outputs 2 JSON BYTE_IDENTICAL PASS (Python 3.13.5 / NumPy 2.3.5). Full ZIP remains local, not claimed uploaded to GitHub. This remote report provides substantive scientific reasoning but does not itself archive code.

## Prior-art ceiling, interpretation, and potential falsifier
Classic Peres/Loschmidt echo, free-fermion Slater determinant and incomplete quantum marginal tomography all predominate. Gorin et al., "Dynamics of Loschmidt echoes and fidelity decay", Physics Reports 435 (2006), https://www.sciencedirect.com/science/article/pii/S0370157306003310 ; Qi & Ranard, Quantum 5:555 (2021), https://doi.org/10.22331/q-2021-09-28-555 (different theorem; conceptual). Source paper itself first reports the source-specific occupation/fidelity contrast. Public NASH repo keyword searches yielded no indexed matching report (not comprehensive of BW/private).

***Important***: reduced local rho unchanged does NOT mean local evolution of quantum PROCESS is the same under interventions, and a decreasing global closed-unitary survival probability does NOT independently prove thermodynamic or irreversible decoherence. No actual experimental measurement, eNRG long chains, original manuscript result figure, GR/GW/PBH/K/J3 physical hypothesis. To discriminate add calibrated bath correlation, nonlocal interferometric Loschmidt readout, controlled multi-time process or protocol metadata, with a predefined nuisance/noise model. Not executed as an experiment; no task assigned to other cells.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_INGESTION_ASSUMED / NO_NEW_TASK_CASCADE.
