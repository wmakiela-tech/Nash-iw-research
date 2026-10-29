artifact_id: MECH-S7-FRONTB-AUTHOR-SOURCE-EXTRAPOLATION-GATE-CROSSCELL-036_20261029
exposure: PUBLIC
claim_ceiling: PINNED_AUTHOR_SOURCE_CODE_AND_TABLE_PROVENANCE / EXECUTED_CONDITIONAL_7D_EXTRAPOLATION_SENSITIVITY / NO_AUTHOR_NATIVE_JULIA_RUN / NO_SOURCE_VALID_SUBEDGE_HADRONS / NO_PHYSICAL_BBN_OR_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
rotation: ROT036
created_at: 2026-10-29
owner_disposition: SOURCE_VALIDITY_REMAINS_OPEN / SPECTRAL_EXTRAPOLATION_INSTABILITY_EXECUTED / CROSS_CELL_SCIENCE_CHECK

# Mech-S7 ROT036 — Original author hadron-table extrapolation, source-recipe sensitivity and cross-cell science gate

## 1. Priority and result

After ROT035 repaired exact moment-information logic following AUD1, LT6 and Badacz, this rotation does NOT optimize further synthetic source statistics. It tests the **source-recipe gate** of the pinned original Wu–Xu program. Two independent questions remain strictly separated:

1. **Computational provenance:** What do the authors actually prescribe outside their numerical hadron table?
2. **Physical admissibility:** Has that prescription been validated as a physical spectrum in the domain needed by the terminal neutron dynamics?

**Finding:** The upstream Julia code explicitly provides a `LinearInterpolation` in log rate vs log PBH mass with `extrapolation=ExtrapolationType.Linear`. Therefore the code-level prescription below the first tabulated mass is DEFINED, not absent. It is NOT independently physically validated in this analysis. The conditional 7D terminal target is materially sensitive to a different, source-motivated extrapolation slope, including a C² edge-jet-matched variant.

## 2. Pinned first-party source and custody

- Pinned author repository: `Fenyutanchan/Primordial-Black-Hole` commit [`d395183674cace6c9906a8911bdeb7234ba4040d`](https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d).
- [Original hadron data, 100 table rows](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/hadrons_from_PBH.dat), Git blob `06d0883a27b108692720422294ba2baacd381a64`. Original table covers PBH masses **1e9 to 4e12 gram**, five reported hadron yield species `π±`, `K±`, `K0_L`, proton and neutron. Retrieved and inspected via connected GitHub at the pinned commit. Only the original first NINE source rows are independently copied into the local ROT013 `edge_bridge_013.py` for exact terminal-edge checks; the full 100-row file is **not bundled** in this archive.
- [Author hadron interpolation](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl), blob `cc73432910f872d526113ce59b6204f38d0766a9`: for each yield `LinearInterpolation(log.(hadron yield), log.(mass); extrapolation=ExtrapolationType.Linear)`, then exponentiate the interpolation.
- [Author ten-state evolution](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl), blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: ten log variables, explicit `dN_over_dt_species(m_PBH)*n_PBH`, dynamic PBH mass, 6 hadron populations, kinetic neutron fraction; source/energy coupled via SM energy equation and Hubble rate; `n_B=eta_B*n_gamma`. Author `Yp` readout is a further transformation, NOT the `X_nuc` reported below.
- [Author scan parameters](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan-parameters.jl), blob `53faee65beda383348580c28d0424188da69b660`: initial Mmin=6e8 g, Mmax=1e10 g with 100 logarithmically spaced masses; **18 of 100 initial mass parameter values are below the first tabulated 1e9 g**. Source interpolation extrapolation therefore can be used already at the beginning of scan cases, not only in the evaporation tail.
- [Author setup README](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/README.md), Julia **1.12.3**, ArbNumerics, DataInterpolations, DifferentialEquations, NaturalUnits and further named packages. Authors state full 24-process scan can take about one hour on Ryzen 9950X.

**Runtime gate:** `julia` is not installed in the current execution container (`command -v julia` yielded no executable); upstream native 10D script was inspected, **NOT RUN**. Running conditional Python 7D below is not a substitute for that author code.

## 3. First-two-point native slope vs eight-point positive control

Let `u=M/(1e9 g)`. The literal author edge extrapolation uses the log-log slope of its first two table rows, yielding `Q_i(u)=Q_i(1)*u^s_i` for `u<1`. Define a **diagnostic alternative** `s_i^{(8)}` by ordinary least-squares on the first 8 original table points in `(log M,log Q)` and then **anchor the value to the same first table row**: `Q_i^(8)(u)=Q_i(1)*u^(s_i^(8))`. This is NOT an author change, NOT source-fitted physical uncertainty, and the untapered alternative has different first derivative at the edge.

| Source species | Author two-point slope | Eight-point diagnostic slope | Alternative/native at `M=7e7 g` | Alternative/native at cutoff `M=12.3669 g` |
|---|---:|---:|---:|---:|
| Charged pions | -1.200486 | -1.270924 | 1.2060 | 3.6058 |
| Charged kaons | -1.196651 | -1.266333 | 1.2036 | 3.5565 |
| Neutral long kaons | -1.196805 | -1.266512 | 1.2037 | 3.5581 |
| Proton/antiproton channel | -1.204291 | -1.275581 | 1.2087 | 3.6622 |
| Neutron/antineutron channel | -1.204763 | -1.276094 | 1.2089 | 3.6649 |

The terminal artificial cutoff is the original Mech conditional choice `6e9 exp(-20) g = 12.3669217346 g`, which lies **18.20824 log-mass units**, or **217.34 first-table grid steps**, below the tabular edge. This is an illustration of the long extrapolation, not evidence of physical validity to 12 grams. At the 7e7 g scale, independently of any assumed physical error bar, the two arithmetic continuations disagree by approximately 20-21% in each source rate.

**Independent numerical arithmetic:** 70-digit `decimal` implementation directly parses the original first nine rows encoded in pinned ROT013; it matches the double-precision two-point slopes within `1.6e-15` and eight-point OLS slopes within `4.5e-16`. This independently validates slope extraction, NOT hadron yield physics.

## 4. Executed conditional ODE test

The Mech-S7 **supported preedge bridge** from ROT013 is unchanged: pinned, archived 10-comp source-on state above 1e9g; coupled conditional micro-thermal host with `chi_EM`, and source-active 7D kinetic ODE for `u=1 -> U_cut` followed by postsource ODE to fixed `T_nuc`. `eta_B(T)` constant prescription, original 2x2 source on/off archives and normalizations. Both source continuations have identical value at the table edge. All other model ingredients and above-edge states are held fixed. This is a counterfactual extrapolation in our conditional Python model, **not** native Julia execution.

| chi EM | `B_exec`: ΔXnuc (8point - native) | `B_sym`: ΔXnuc (8point - native) |
|---:|---:|---:|
| 0.00 | +1.7356102915e-5 | +2.3858179745e-5 |
| 0.50 | +1.7328582407e-5 | +2.3779129044e-5 |
| 1.00 | +1.7301267261e-5 | +2.3700870135e-5 |

At chi=0.5, `B_exec` gives native `X_nuc=0.400959518962`, eight-point trial `0.400976847544`; `B_sym` native `0.400084966241`, trial `0.400108745370`. These differences are comparable to or larger than source-variant contrasts ~1e-5 from prior ROT025. This is **conditional source-form sensitivity**, not a bound on true uncertainty.

**Solver check:** chi=.5 `Radau` rtol=3e-9 vs 3e-10 changes the *difference* by ~`2.86e-14` for Bexec and `2.56e-13` for Bsym; these comparisons are NOT rigorous trajectory error enclosures. χ=0,1 are out-of-calibration background controls; they were not used to choose the source first-eight regression.

**Edge-regularity falsifier:** To exclude the simple explanation that the first-derivative mismatch caused the sensitivity, replace the extrapolation log-rate difference by `Δs*z*[1−exp(−(z/0.2)^2)]`, where z=log u. It has identical **value, first and second z derivatives** to native at z=0. When run at χ=.5, final changes remain `+1.677491923e-5` Bexec and `+2.281606566e-5` Bsym. The effect persists under C² source-edge matching, with an explicitly arbitrary transition width 0.2.

## 5. Cross-cell currentness and scope controls

- **Mech owner ROT035 + AUD1:** AUD1 SELF-002 correctly exposed that numerically almost equal moments do not imply EXACT equal noiseless observations. Mech ROT035 has already corrected ROT032/033/034 claims and used Badacz's Gegenbauer source-perturbation basis with symbolically identical three moments. This DOES NOT justify an extrapolated physical spectrum.
- **LT6 ROT009 + Badacz doc 022/024:** mature exact moment-repair/orthogonality mathematics addresses source-information geometry. Badacz's doc 025 **v2** proposes an interval-bound solver error protocol but has only synthetic Mech-structured tests, pending independent AUD1 review; it is not a certificate for these ROT036 source histories.
- **MT14 ROT013:** cross-front program explicitly separates source-model prediction discrepancy from statistical measurement noise and from target-identifiability claims. The present source-extrapolation experiment exemplifies that SOURCE MODEL gate; it does NOT transfer MT14's DTC target-specific error thresholds to PBH.
- **XH-S5 and science harvest:** source-native hadron yield generation/provenance and author-running resources, rather than more abstract toy near-null constructions, are the next material scientific dependencies. Source author code is accessible, but Julia runtime and physically validated subedge data are not.
- **REC/KN/BW:** this note is a research return with links, not an independent referee verdict, owner admission, BW ingestion or physical canon.

Original cross-cell materials: [LT6 ROT009](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt6/2026-10-29/IW_LT6_ROT009_EXACT_H_MOMENT_REPAIR_TARGET_PERSISTENCE_001_20261029.md), [Badacz interval v2](https://github.com/wmakiela-tech/Nash-iw-research/blob/58ca45d9bd5ef36c13f7ced2b0372d0199596529/research/badacz/2026-10-29/IW_BADACZ_MECH7D_RIGOROUS_SOLVER_BOUND_V2_AFTER_AUD1_ROT009_025_20261029.md), [MT14 programme ROT013](https://github.com/wmakiela-tech/Nash-iw-research/blob/5f36f4a11e45436d7b7a1e3ecfbb751957554d90/research/mt14/2026-10-29/iw_mt14_rot013_scientific_programme_alignment_and_model_error_transfer_gate_001.md), [Mech ROT035 owner repair](https://github.com/wmakiela-tech/Nash-iw-research/blob/73723c6340655187c6127ac694891a8b5b77e68f/research/mech-s7/2026-10-29/mech_s7_rot035_crosscell_exact_moment_nonlinear_witness_owner_aud1_disposition_001.md).

## 6. Decision / admission gate

**Owner recommendation:** the current Front B terminal conditional work is mathematically informative but should now prioritize (i) native Julia 10D deterministic reproduction for one benchmark, (ii) direct audit of tabulated hadron source generation and physical extrapolation below 1e9g, (iii) independent validated operator and ODE error budget; only then physical BBN `Y_P/D/H` or PBH constraints. This is **no owner/EXEC instruction**, only a scientific dependency statement.

| Claim | State |
|---|---|
| First-party code explicitly log-linearly extrapolates yields | PINNED_SOURCE_VERIFIED |
| 100-row mass range, 18 initial scan grid values below table support | SOURCE_DATA_AND_PARAMETERS_VERIFIED |
| Alternative local source slope propagates ΔXnuc~1.7–2.4e-5 | EXECUTED_CONDITIONAL_PYTHON_7D |
| C²-matched alternative retains ΔXnuc~1.7–2.3e-5 | EXECUTED_CONDITIONAL_PYTHON_7D |
| Native author Julia 10D deterministic reproduction | **NOT_EXECUTED / NO_JULIA_RUNTIME** |
| Valid physical hadron spectrum below 1e9g | **UNKNOWN** |
| Independent rigorous error bar for original native model | **UNKNOWN** |
| Mech full-system nonlinear interval certificate | **NOT_AVAILABLE** |
| BW ingestion / canon / EXEC / physical Yp,DH,PBH bound / theorem novelty | **NOT_CLAIMED** |

## 7. Reproduce

The self-contained archive contains two untouched original Mech-S6 2×2 trajectory ZIPs (validated by their embedded SHA256 in the reproducing script), ROT013 source-bridge and thermal equation dependencies, and five new Python scripts with their CSV/JSON results. The two first-author source rows and the first-nine original source samples are in `edge_bridge_013.py` and `source_7d_clock_baryon_stress_009.py`. It does **NOT** package the full original upstream Julia repository or table; pinned public GitHub URLs above establish source provenance. Requires Python, NumPy, SciPy, pandas; Julia is NOT used.

```
python audit_author_extrapolation_036.py
python independent_upstream_edge_audit_036.py
python audit_author_extrapolation_036.py --ode
python heldout_tight_extrapolation_036.py
python c2_edge_matched_extrapolation_036.py
```

Outputs `source_extrapolation_sensitivity_036.csv`, `upstream_extrapolation_gate_036.json`, `independent_edge_036.json`, `conditional_extrapolation_kinetic_036.{csv,json}`, `heldout_and_tight_036.{csv,json}`, `c2_edge_kinetic_036.{csv,json}`. Scope: conditional source diagnostic, not validated physical prediction.