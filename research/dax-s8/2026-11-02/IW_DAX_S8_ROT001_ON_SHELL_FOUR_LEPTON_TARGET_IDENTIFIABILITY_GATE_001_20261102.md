---
artifact_id: IW_DAX_S8_ROT001_ON_SHELL_FOUR_LEPTON_TARGET_IDENTIFIABILITY_GATE_001_20261102
created_at: 2026-11-02
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: EXACT_KINEMATIC_COUNTERMODEL / NEGATIVE_KNOWLEDGE / POSITIVE_SUFFICIENCY_BOUNDARY
claim_ceiling: NO_QED_MATRIX_ELEMENT / NO_DIFFERENTIAL_QED_OPERATOR / NO_EM_DEPOSITION / NO_NEUTRINO_ESCAPE / NO_PBH_BBN_BOUND / NO_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN
independence: NONBLIND_FUNCTIONAL_CONTINUITY
source_ancestor: IW_DAX_S7_ROTATION_68_SCIENTIFIC_LEDGER_20261102
---

# DAX-S8 initial material return — source-level total DPP rate does not identify nonlinear four-lepton targets, even after exact on-shell kinematics

## 0. Scientific currentness and precedence (2 November 2026)

Precedent FIRST: DAX-S7 R67 introduced the high-energy DPP missing-channel falsifier; R68 FIRST clearly separated total DPP hazard from differential four-lepton energy-transfer operator and tested deliberately NON-QED abstract energy splits, with sum(z^2)=0.25/0.4804/0.9412. This return DOES NOT re-claim that result. The incremental carrier change is from unconstrained abstract split vectors to two exact on-shell, four-momentum-conserving four-lepton states.

Verified source: [DAX-S7 R68 public ledger](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-11-02/IW_DAX_S7_ROTATION_68_SCIENTIFIC_LEDGER_20261102.md). Its cross-cell handoff requests a QED DIFFERENTIAL DPP operator; it is not that operator.

Checked latest 2 November publicly accessible MT14 ROT023, Mech-S8 ROT001, XH-S5 ROT017, LT7 ROT001, INT8 ROT050, PRF12 R25/R26 metadata and targeted Slack DPP/direct DAX searches. No source-valid differential DPP operator was established by those inspected items. NO SEARCH HIT != NOVELTY; private live BW owner status may move independently.

## 1. Strongest defensible seed

At FIXED incoming four-momentum and given only the integrated `gamma gamma -> e+ e- e+ e-` rate, total rate plus exact kinematics still does not identify target readouts that depend nonlinearly on outgoing lepton energies. Conversely, for the much narrower target of species-blind instantaneous *sum of all four outgoing lepton energies* at that same fixed incoming four-momentum, conservation alone suffices. Neither target is thermal deposition.

## 2. Lowest mature host: exact on-shell 2->4 phase space

Use natural units c=1 and electron mass m=1. In the centre-of-momentum frame choose incoming photons
`k1=(6,+6 zhat)`, `k2=(6,-6 zhat)`, hence total `P=(12,0,0,0)` and s=144 in m units.

Charge labels in each final pair are one electron and one positron. The four outgoing momenta are (E,px,py,pz):

**State A (balanced):**
- e-: (3,+sqrt(8),0,0), e+: (3,-sqrt(8),0,0)
- e-: (3,0,+sqrt(8),0), e+: (3,0,-sqrt(8),0)

**State B (unbalanced):**
- e-: (4,+sqrt(15),0,0), e+: (4,-sqrt(15),0,0)
- e-: (2,0,+sqrt(3),0), e+: (2,0,-sqrt(3),0)

Both satisfy individually E_i^2-|p_i|^2=1, all E_i positive, and sum of outgoing four-momenta P=(12,0,0,0). Thus both are exactly kinematically allowed points of the same four-lepton final-state phase space, with identical photon initial state. We do NOT claim the exact QED differential cross-section weights these points equally or nonzero. Smooth normalized mathematical densities concentrated in sufficiently small neighborhoods of distinct interior kinematic points can likewise produce distinct moments with identical integrated normalization.

## 3. Decisive exact contrast

| Fixed-input target | State A | State B | Identified from rate+kinematics? |
| --- | ---: | ---: | --- |
| total outgoing energy, sum E_i | 12 m | 12 m | YES, at fixed initial four-momentum |
| sum E_i^2 | 36 m^2 | 40 m^2 | NO |
| number of leptons with E_i > 3.5 m in this COM frame | 0 | 2 | NO |

Define two mathematical normalized final-state kernels supported on the two kinematic configurations (or on their small open neighborhoods), each multiplied by the SAME nonnegative integrated cross section sigma_tot(s). Then `integral d sigma_A = integral d sigma_B = sigma_tot(s)`, but the resulting nonlinear target expectations differ. Their difference is NOT an estimate for physical QED; it is an exact failure of *identification from the total cross section alone*, even under energy-momentum and mass-shell constraints.

**Negative:** TOTAL_RATE + CONSERVATION != DIFFERENTIAL_ENERGY_OPERATOR; adding only exact on-shell kinematics does not close this gap.

**Positive sufficiency boundary:** For a fixed incoming four-momentum, any target `F = a + b sum_i E_i` with identical species-blind coefficients and NO later propagation/cooling/decay/absorption is fixed by `sum_i E_i = E_gamma + epsilon_bath`. In particular total immediate outgoing lepton energy is fixed. The assertion does NOT extend to energy deposited into plasma, high-energy-tail population, stochastic stopping time, neutrino energy or channel-weighted composition. A generic nonlinear F, even one invariant under exchange of the four leptons, is NOT fixed by sigma_tot.

## 4. Tiny exact reproduction and claim limits

File: [dax_s8_rot001_on_shell_dpp_kinematic_witness.py](dax_s8_rot001_on_shell_dpp_kinematic_witness.py). Standard library only. Run `python dax_s8_rot001_on_shell_dpp_kinematic_witness.py`; asserts total E=12, mass-shell square identities, exact moments 36 vs 40, threshold counts 0 vs 2. Pre-commit local execution PASS; initial local file SHA256 a229b8947ba8c952f66fcd7826e61181d3eadf897bba4f3f49d11df62f62bb77 (remote byte identity must be independently fetched/checked). No QED matrix element, exact differential QED cross section, energy-loss operator, dynamic bath, BlackHawk, Julia or BBN execution here.

This demonstrates only a classical kinematics/information boundary. Not a new theorem, new high-energy physics mechanism or empirical estimate.

## 5. Disposition and stable STOP

RESULT: `FALSE GENERICALLY / TRUE UNDER SPECIES-BLIND LINEAR INSTANTANEOUS ENERGY TARGET / OPEN FOR QED DIFFERENTIAL AND ALL DOWNSTREAM DEPOSITION TARGETS`.

No operator was reconstructed or approximated from sigma_tot. No cascade simulation was run. Do not inflate this into a new Front B task or transfer the mathematical witness to a physical PBH bound. Further DAX work on this seam should stop unless a genuinely source-valid differential operator arrives or an owner asks a distinct DAX-native question.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / BW_INGEST_PENDING / OWNER_REVIEW_PENDING / NO_AUTO_R69`.
