---
artifact_id: IW_MECH_S8_ROT002_WUXU_BLACKHAWK_TWO_DOMAIN_SOURCE_SUPPORT_AND_E4_REOPEN_GATE_001_20261102
created_at: 2026-11-02
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
document_type: RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: PINNED_SOURCE_CONFIGURATION_AND_KINEMATIC_ACCOUNTING_ONLY / NO_PHYSICAL_HADRON_VALIDATION / NO_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT002: Wu–Xu source-native support has two independent domain gates

**Decision:** `E4_SOURCE_DUAL_DOMAIN_GATE_IDENTIFIED / HOLD/SOURCE_BLOCK`. No additional conditional source perturbations, no original Julia/BlackHawk execution, no physical-claim promotion.

## Original source chain (read, not re-executed)

1. Wu–Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, JCAP 02 (2026) 063, DOI `10.1088/1475-7516/2026/02/063`; original repo `Fenyutanchan/Primordial-Black-Hole` frozen `d395183674cace6c9906a8911bdeb7234ba4040d`.
2. Original notebook `arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb`, blob `8a10396ae771b17059808fc2b91235dd194cba8d`, code cell 12 explicitly sets `m_PBH_list = geomspace(1e9, 4e12, 100) .* NU.g` and per mass `set_BlackHawk_energy_spectrum!(params, GeV(5), GeV(1e5), 100)`, `close_BlackHawk_dark_matter!`, `set_BlackHawk_BBN!`, `run_BlackHawk_inst`; it integrates secondary `pipm,Kpm,K0L,proton,neutron`. Cell 13 writes `hadrons_from_PBH.dat`. Git blob of that 100-row table: `06d0883a27b108692720422294ba2baacd381a64`.
3. `tool_script-BlackHawk_extension.jl`, blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`, assigns `Emin,Emax,E_number` and BBN `hadronization_choice=0`; original `tool_script-parameters.jl` blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5` defines `T_BH(m)=NU.M_Pl^2/m`. Author scan parameters blob `53faee65beda383348580c28d0424188da69b660`: 100 initial masses `6e8 .. 1e10 g`.
4. Mature host: Arbey–Auffinger BlackHawk, EPJC 79 (2019) 693, DOI `10.1140/epjc/s10052-019-7161-1`, Appendix B.3, 5 to `1e5 GeV` PYTHIA primary input hadronization energies. The code can **extrapolate** branching ratios beyond tabulated input energies but the paper does not guarantee distant extrapolation validity. BlackHawk's nominal primary particle taxonomy includes top, W, Z and Higgs; that does **not** certify their exact v2.3 production/reaction transfer in Wu's execution.

## Type separation: source-table lower mass vs generator energy ceiling

**A. Source mass table:** published author secondary source samples only `M_BH >= 1e9 g`. Outside this interval `tool_script-hadrons_from_PBH.jl` blob `cc73432910f872d526113ce59b6204f38d0766a9` employs log-interpolations with `ExtrapolationType.Linear`. The extension below the table is a numerical definition, **not physical source validation**.

**B. Primary-energy sampling and hadronization:** notebook inputs `E_primary <= 1e5 GeV`; original BlackHawk hadronization primary energies also end at `1e5 GeV`. Merely increasing the sampled BlackHawk `Emax` does not by itself validate/extend the *hadronization table*; beyond-range branches can be extrapolated. Both energy-grid tail and physical particle fragmentation need independent support.

**C. Downstream model/target:** charge-resolved map, relevant greybody/heavy channel coverage, strict native Julia 10D solver error, Wu–Xu published Fig.5 version and valid Yp/D/H endpoint are separate; all remain OPEN. Badacz REVIEW044, MT14 ROT021/022/023, SCOPE9 TOPDOWN016/017, AUD1 ROT021, Mech-S7 ROT035–037 have scientific precedence. The original Julia10D HAS been executed elsewhere in IW (Mech-S6, Badacz); `NO_JULIA_IN_THIS_CELL` is not project-wide `NO_NATIVE_JULIA`.

## One executed kinematic crossover calculation

Standard Schwarzschild `k_B T_H= hbar c^3/(8*pi G M)`. With printed SI constants and rounded G/hbar, `T_H [GeV] × M[g]≈1.057261195158×10^13 GeV·g`. Setting `T_H=Emax=1e5 GeV` yields `M_grid≈1.057261195×10^8 g`. At the **source mass-table** edge `M_table=1e9g`, `T_H≈10.573TeV`, so **these two gates differ by factor ≈9.46 in mass**.

For complete evaporation, ignoring remnant, a fraction of *total gross emitted rest-mass energy* lies in the interval from the original table floor down to `M_grid`. This is a mass-energy identity, not emitted hadron energy, target-weighted deposition or BBN signal.

| initial scan index | M0 [g] | gross total emitted below M_table | gross total emitted between M_table and M_grid | gross total emitted with T_H>=Emax |
|---:|---:|---:|---:|---:|
| j0 | 6.000e8 | 100.00% | 82.38% | 17.62% |
| j22 | 1.121174e9 | 89.19% | 79.76% | 9.43% |
| j24 | 1.186744e9 | 84.26% | 75.36% | 8.91% |
| j99 | 1.000e10 | 10.00% | 8.94% | 1.06% |

From the original 100 scanned masses: 18 start below the mass table; 43 lose >=50% of gross rest-mass energy below that edge under the stated complete-evaporation assumption (ROT001 first). **Correction of interpretation:** the whole subedge interval must NOT be described as `T_H>=100TeV`. Conversely, `T_H<Emax` does NOT validate the missing source, and `T_H=Emax` is NOT a mathematically exact error cutoff: emitted primary spectra include energy tails and depend on greybody factors.

## Source-native falsifier before reopening physical interpretation

Preregister actual-source production at `M=1e9, 3e8, 1e8 g`; audit BlackHawk v2.3 official archive/table provenance, primary energy/greybody/spin/t,W,Z,H channel completeness, hadronization-table support, per-charge hadron emissions and full energy accounting. Increase/regenerate hadronization support as required rather than only increasing input `Emax`. Only after reproducible source spectra may the owner commission a source-corrected native Julia10D paired endpoint run, calibrated Yp and independent D/H, with rigorous numerical/root error and Fig.5 provenance.

**Current status:** `E4_SOURCE_BLOCK / NO_SOURCE_VALIDATED_SUB1E9g_HADRONS / PBH_DE_DYNAMIC_ACCURACY_OPEN / PBH_Yp_DH_TARGET_VALIDATION_OPEN / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.

## Reproduction/custody

Public single-file standard-library source-compatible numeric reproduction: [mech_s8_rot002_two_domain_gate_reproduce.py](mech_s8_rot002_two_domain_gate_reproduce.py). Local extended script was separately executed with machine-readable JSON and SHA256 manifest; this public compact script has the same source parameters/equations, but **is not asserted byte-identical** to the extended local script. All original source pins above were connector-read from immutable GitHub; no original source or instrument runtime was executed. `sync_state: GITHUB_PENDING_BW_INGEST` is an archival label, not accepted BW or scientific promotion.
