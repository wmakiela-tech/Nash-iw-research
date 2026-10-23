# Mech-S7 ROT013 — tabulated-source preedge bridge and antispectral robustness (2026-10-24)

**RETURN_ID:** `MECH-S7-FRONTB-TABULATED-EDGE-STATE-TRANSPORT-GATE-013`  \n**PROBLEM:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  \n**TYPE:** `EXECUTED_CONDITIONAL_PREEDGE_10_VAR_BRIDGE_AND_POSTEDGE_7D / MASS_EVENT_ANCHORED / ANTI-SPECTRAL_KILL_RETEST / NO_PHYSICAL_CLAIM`

## 1. Source and provenance / others first
- Wu–Xu source commit `d395183674cace6c9906a8911bdeb7234ba4040d`, table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`; source code uses **log-linear interpolation of production rate against log PBH mass**. First NINE source rows (M between 1.0e9 and >1.84e9 g) copied verbatim into reproducer; they support a software-level interpolation only within that range. Below 1e9g the unchanged public-vs-paper extrapolation remains *unvalidated* physically.
- Four original archived Mech-S6 Julia trajectories from ZIP SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5` and `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`; last source-active saved row index 1469, with M=1.8366330858522944e9 g, t=49.96189862690079s, T=0.1447372645665MeV. The immediately following row is postsource. Historic ROT004 exact mass-cube rate Gamma=4.207579833788249e27 g^3/s; source table edge 1e9g.
- Credit: DAX-S7/PRF11 R21–R22 identified original cooling/EOS constraints; Mech-S7 ROT001–012 established archival common-background, frozen & dynamic 7D, source shape and spectral cancellation; Rec10 secured postsource hadron memory; MT13/LT5 proved time-target nonmaps and exact endpoint-sign error requirements. This rotation corrects a **specific ROT006–012 edge-state transplantation**, not any original Julia 10D simulation.

## 2. New experiment: source-tabulated segment 1.8366e9→1e9g
All modelled branches use one shared archived `public_exec` cosmological background at row 1469; X and six hadron states from the respective public charge map (`exec` or `sym`). In this run, the original used 7D state was copied to 1e9g without evolution. Now integrate the **10 component** vector [T_gamma,ln(a/a_start),ln rho_nu,X,n_pi−,n_pi+,n_K−,n_KL,pbar,nbar], with exact M^3 and 9-row log-log source interpolation over **tabulated** masses. The thermal split chi_EM, EM electron/positron ideal Fermi pressure, effective nu channel, baryon eta prescription, six Wu-Xu collision and weak rate equations are as in ROT011. The original whole-history 10D system **is not** this bridge: (i) its evolution variable is ln a and backgrounds couple differently, (ii) historical preedge states and initial radiation are taken from archive, (iii) EM/nu Hawking branching chi is externally chosen. After reaching M=1e9g, carry both hadron state and EM/nu background to the same ROT012 7D subtable forward integrator. Read at exact T_nuc=0.07818527068831995 MeV. Under public and paper spectral law, evolution ABOVE the table edge is identical within each reaction map.

The exact mass-clock event anchored at last archived active row occurs at t_edge=51.19666294957113 s, whereas re-anchoring from initial archived formation mass yields 51.09825802317032 s. Their 0.0984049264 s difference is **archived mass-invariant error**, not a separately observed PBH physical effect. The bridge explicitly chooses last-row mass+time as anchor; final X comparison does not conflate it with the separate initial-particle-state transport.

## 3. Three thermal partitions, constant eta_B
| chi_EM | map | old ΔXn | new bridged ΔXn | new / old |
|---:|:---|---:|---:|---:|
| 0.0 | `exec` | -6.9508507594e-06 | -1.4739737348e-05 | 2.120566 |
| 0.0 | `sym` | +2.2640745209e-05 | +1.1257271224e-05 | 0.497213 |
| 0.5 | `exec` | -6.8929162508e-06 | -1.4551144640e-05 | 2.111029 |
| 0.5 | `sym` | +2.2605949017e-05 | +1.1282615337e-05 | 0.499099 |
| 1.0 | `exec` | -6.8354673954e-06 | -1.4365030570e-05 | 2.101543 |
| 1.0 | `sym` | +2.2571284824e-05 | +1.1307292376e-05 | 0.500959 |

With chi_EM=0.5, propagating the previously omitted tabulated interval changes |ΔX| by a factor **2.111× for exec** (increase) and **0.4991× for sym** (decrease), without changing either sign. It also changes Xedge from 0.497967914253 to 0.498443725361 (exec), and from 0.496214274722 to 0.497135264226 (sym). All six source-active hadron populations rise approximately 2.07–2.15-fold across the tabulated interval, not remain frozen. This is a CONDITIONAL result, not a correction to the published Wu-Xu PBH/BBN bound.

## 4. Exact 2x2 state vs host ablation (chi_EM=.5)
| map | uncorrected | update state only | update temperature/clock/nu/PBH host only | update both |
|:---|---:|---:|---:|---:|
| `exec` | -6.8929162508e-06 | -1.4485732933e-05 | -6.9542771416e-06 | -1.4551144640e-05 |
| `sym` | +2.2605949017e-05 | +1.1302202424e-05 | +2.2597990577e-05 | +1.1282615337e-05 |
The **state update**, not the correction to event clock alone, produces nearly the entire change in this conditional endpoint contrast. This identifies a numerical-model attribution, not proof that the historical archive had these same corrected states.

## 5. Recomputed antispectral sign-kill threshold at chi_EM=.5
Define under the PAPER spectrum `alpha_pbar=-1.3+eps`, `alpha_nbar=-1.3-eps`; for each map, bracket and numerically root paper(eps)-public=0, preserving common tabulated bridge. The earlier ROT012 root used transplanted states.
| map | ROT012 epsilon | ROT013 corrected epsilon | relative pbar/nbar source ratio at 1e8g vs epsilon=0 | tight root residual in X |
|:---|---:|---:|---:|---:|
| `exec` | +4.6218791962e-05 | +9.7439681491e-05 | -4.486256535e-04 | +3.4483e-11 |
| `sym` | -2.7506890053e-04 | -1.3709072411e-04 | +6.315254437e-04 | +1.4949e-13 |

The opposite-sign diagnostic remains *highly condition-sensitive* (sub-permille relative pbar/nbar source ratio perturbations). The previous numeric roots should NOT be used without their edge-state typing. Confirmed with Radau rtol3e-8 roots and independently reevaluated at rtol3e-9, root residual ≤3.5e-11 in X, NOT a certified global numerical error. Both initial source law branches share identical preedge species injection and cosmic background; no physical source uncertainty inferred.

## 6. What changed from ROT012, and negative knowledge
- **Material correction:** edge states in all 7D surrogates ROT006–012 were transplanted from M≈1.8366e9g. This relocation is not harmless: affects BOTH endpoint contrasts by factors ~2, and spectral kill roots by comparable factors. ROT012 numeric sign *at its own model* remains valid but cannot be promoted to invariant preedge solver result.
- **Sign not killed by this correction:** exec stays negative, sym positive in all six chi_EM/map tested at fixed eta. The sign itself still fails source-shape robustness under infinitesimal antinucleon spectral-index split. There is no blanket physical sign claim.
- **Source support precision:** segment from M≈1.8366e9g to M=1e9g is within source **table domain**; the entire M<1e9g source segment is extrapolation and physically unsupported. A tabulated row is not a validated particle physics source; source-vs-code agreement is a different gate.
- **Structural cost:** the 10-component bridge is an independently constructed source-informed reduced cosmological calculation, NOT original 10D Julia runtime; no accepted internal Julia steps or global error control; thermal EM fraction chi is synthetic; emission from surviving PBHs has no species-resolved radiation energy reservoir in this surrogate; no neutrino Boltzmann transport.
- **Other unclosed gates:** original Wu-Xu low-T EOS and baryon law discrepancies (DAX-S7/PRF11); formula genealogy for Yp vs Xn; source-valid E2b/D-H chain; inverse likelihood and original published Figure5 provenance. No physical helium number, PBH exclusion, novel theorem, or EXEC authorization.

## 7. Tests, exact files, readback contract
- `edge_bridge_013.py`: executed 10-variable above-table mass evolution, shared public-exec background, two source-map-specific particle states; SHA-input verified by base helper. PIN first 9 exact table rows; source column interpolation in log of mass and log of Q.
- `edge_bridge_ablation_013.py`: run complete 8-cell state/clock ablation; `spectral_bridge_roots_013.py`: root finding for chi=.5, Radau residual retest at stricter tolerance. `active_source_antispectral_012.py` and original ROT010 EOS + ROT009 rates are included locally for self-contained reproducibility, alongside original zipped trajectories.
- `bridge_thermodynamics_comparisons_013.csv`: six source-law comparisons with two states (12 entries); `bridge_state_background_ablation_013.csv`: eight ablations; `bridge_spectral_roots_013.json/csv`: two roots and numerical residuals; per-case bridge states in JSON, source table first 9 lines, stderr logs, manifest and original archives.
- A scripted integration of source table mass M=1.8366e9g to 1e9g is feasible without upstream Julia and is sufficient to demonstrate the CONDITIONAL edge-state artifact. No claim that this constitutes the original 10D rerun; do not conflate 10 COMPONENT bridge with Julia original code.

**NEXT DECISION**: correct/validate whole upstream 10D trajectory **before** assigning physical meaning to relative PBH source-law Xn effects. The immediate cheapest generalizable invariant is exact M³ and accepted-step states around M=1e9g, plus source-table/charge species history. Validate pbar/nbar correlated spectra below 1e9g separately. Existing P1 Front B owner priority preserved; no new cross-cell task cascade.

**STATUS** `EXECUTED_CONDITIONAL_PREEDGE_BRIDGE / 6_FIXED_ETA_CELLS_PASS / 8_ABLATIONS_PASS / 2_SIGN_ROOTS_NUMERIC_PASS / NO_FULL_JULIA_10D / NO_SOURCE_VALID_E2B / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND / BW_INGEST_UNVERIFIED`.