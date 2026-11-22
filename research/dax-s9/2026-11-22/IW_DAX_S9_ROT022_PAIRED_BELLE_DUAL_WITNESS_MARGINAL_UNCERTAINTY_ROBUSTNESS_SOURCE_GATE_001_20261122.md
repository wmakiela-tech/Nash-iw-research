---
artifact_id: IW_DAX_S9_ROT022_PAIRED_BELLE_DUAL_WITNESS_MARGINAL_UNCERTAINTY_ROBUSTNESS_SOURCE_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: OFFICIAL_SECONDARY_TWO_BELLE_SOURCE_ERROR_MARGINS / SHARP_DUAL_LINEAR_FRACTIONAL_ROBUSTNESS_FALSIFIER
claim_ceiling: NO_REAL_CORRELATED_COVARIANCE / NO_EXPERIMENTAL_SIGNIFICANCE / NO_PHYSICAL_HADRONIC_AMPLITUDE_FIT / NO_NEUTRINO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT022 — Paired Belle charged/neutral angular dual witness loses guaranteed separation when charged point systematics are allowed

**Date 2026-11-22.** Bounded falsification of possible over-interpretation of DAX9 ROT021. The source-central charged-v-neutral sharp quartic TV contrast remains accurate; this turn checks the SAME fixed charged-selected dual witness under actually reported per-bin asymmetric error margins, with explicit caveats. This result is NOT a measured statistical p-value, experiment rejection, identification of muon background, or new theory.

Original primary experimental sources: T. Mori et al, JPSJ76 074102 (2007), DOI https://doi.org/10.1143/JPSJ.76.074102, Belle charged author Eq4 S+D0+D2 and source discussion of high-angle systematic behavior; S. Uehara et al, PRD79 052009 (2009), DOI https://doi.org/10.1103/PhysRevD.79.052009, Belle neutral pion pair, original HEPData ins815978 Tables5/6/31 with published W-unfolding correlation caveats. Actually reread source-authenticated **official PACKAGED SECONDARY Rivet YODA** bytes: charged SHA256 `28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403`, neutral SHA256 `65ed96b71a3e03e5528c406c336aa07277bff3fd9cf1c6b9596a708f14c573dd`; independent ROT018 original RPM-source acquisition https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45025075860. Primary HEPData native export HTTP403 NOT HELD; original experiment angular covariance NOT obtained. Source labels charged exactly `stat`, `sys_1`, `sys_2`; neutral exactly `stat`, `sys`.

COMMON source support W=[.84,.94]GeV, 20 native charged 5MeV and five neutral 20MeV W bins, twelve native `|cos(theta*)|` bins [0,.6] width .05, original Belle y per angular density unit integrated ONCE, same positive fixed R68 Planck source weight Eγ=1436554MeV,T=.07818527068831995MeV, nominal neutral betaC/betaN adjustment. Re-parsed all native inputs from actual YODA and verified ORIGINAL ROT018 inherited 60-cell CSV source to 5e−13 relative PASS.

Source quartic model J<=2 S+D0+D2 has `I(z)=a+b z²+c z⁴`; integrated moment matrix G, previous ROT021 fixed charged-derived dual |λ_j|<=1, `Gᵀ(λ−μ1)=0`. The SAME angular functional `L(y)=.5[(λ−μ)·y]/sum y` vanishes on ANY true quartic angular distribution; at source CENTRAL Belle gives **L_charged=.04688212712744676** and **L_neutral=.00019011124179592**. Original λ was selected on the charged dataset — this is NOT preregistered or independent charged test.

A deliberately ARTIFICIAL simultaneous independent source-marginal box allows each original positive source cell `y_ij∈[max(0,y_ij−t e^-_ij),y_ij+t e^+_ij]`, where t is a box-width multiplier, **not a Gaussian number of standard deviations, not a joint confidence set and not a real correlated Belle nuisance model**. Charged stat+point quadrature is done PER ACTUAL W×angle source cell BEFORE summing weighted W, not postaggregate quadrature. A fully common multiplicative angular normalization cancels exactly in normalized L; charged `sys_2` and neutral overall `sys` cannot be expanded into independent per-angle random variables without source-level covariance.

**SHARP independent-box lower separation between charged L and neutral L (charged minimal minus neutral maximal), common t=1:**

| Declared source error boxes | Min separation as percent points | First t where source-box witness ranges touch |
|---|---:|---:|
| No displacement, only observed central | **+4.6692016pp** | N/A |
| Both `stat` alone | **+0.44580497pp** | **1.10567798** |
| Charged `sqrt(stat²+sys_1²)` at original cells; neutral `stat` only | **−0.86905633pp** | **0.84290482** |
| Previous plus independent neutral full `sqrt(stat²+sys²)`, deliberately UNPHYSICAL | **−5.42230055pp** | **0.46602948** |

Therefore CENTRAL source contrast is empirically recorded, but one cannot claim robust experimental charged-v-neutral distinction after source point systematics are admitted. An overlapped single scalar dual witness does **NOT** establish global 12-bin quartic agreement or a physical joined amplitude fit.

**SHARP individual witness ranges at t=1** (absolute fractions):
- charged stat-only [0.0255337373,0.0684906284], t touching witness 0 is 2.19888048;
- charged stat+point quadrature [0.0123851242,0.0793608481], t touching 0 is 1.35976661;
- charged stat+point additive [−0.0008161393,0.0922386492], t touching 0 is .98285114;
- neutral stat-only [−0.0207378155,0.0210756876], t touching 0 is .00909322;
- neutral stat+full sys falsely independent [−0.0655307689,0.0666081298], t touching 0 is .00289435.
These are **not** observed significance, true confidence intervals or p-values.

**Two mathematically independent implemented extremizers:** (i) monotone Dinkelbach-type root of the sign-selected linear fractional endpoint function for each marginal box; (ii) wholly separate Charnes–Cooper linear program `u_j=Y_j/sum Y,s=1/sumY`, constraints `lower_j*s<=u_j<=upper_j*s` and `sum u=1`. Five individual minima/maxima, three paired minima, all eight touching-t values independently coincide; dual quartic annihilation moment residual 2.60e−18. Common angular scaling factors .5,1.13,2.0 leave L unchanged. This proves numerical source-box geometry only, not actual physical correlated systematic robustness.

**Local user-conversation FULL independent executable report and reproducible source bundle:** `DAX9_ROT022_Belle_Paired_Dual_Marginal_Uncertainty_Repro.zip`, ZIP SHA256 **5629782cb9f79c4637491ab3d3c1fd8db8b65bb56280722f3e6e0c028c90f68a**, ZIP CRC PASS, 15/15 payload SHA256 PASS, 16 ZIP members, **2 clean independent directory replays × 4/4 JSON and three CSV byte-identical PASS**. Both original compressed source inputs and ROT018 60-cell source-independent check included. Public GitHub artifact is **TEXT REPORT ONLY**; source ZIP not uploaded to GitHub.

**Scientific disposition:** ROT021 source-central angular-shape anomaly and neutral negative control are correctly retained, but statistical/experimental 'robustness' inference based on CENTRAL magnitude alone must be withheld. Next real science needs experimental per-angle nuisance correlation matrix, unfolding response or source-native strongly constrained cross-channel amplitude fit, not free error-box escalation. NO_I3 / NO_BW_WRITE / NO_OWNER_OVERRIDE / NO_NEUTRINOS_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

RETURN: OFFICIAL_SECONDARY_TWO_SOURCE_MARGINAL_READ_PASS / EXACT_FROZEN_ANGULAR_DUAL_PASS / INDEPENDENT_LINEAR_FRACTIONAL_AND_LP_PASS / POINT_SYSTEMATIC_PAIRED_ROBUST_SEPARATION_FAIL / COMMON_NORMALIZATION_INVARIANCE_PASS / NO_EXPERIMENTAL_CI / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
