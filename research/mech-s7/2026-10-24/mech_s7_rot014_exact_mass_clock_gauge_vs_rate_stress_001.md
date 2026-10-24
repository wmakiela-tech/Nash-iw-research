# Mech-S7 ROT014 — Exact PBH mass-clock anchor: time-origin gauge versus emission-rate sensitivity

**Date:** 2026-10-24  
**RETURN_ID:** `MECH-S7-FRONTB-MASS-CLOCK-ORIGIN-VS-RATE-GATE-014`  
**PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**EVIDENCE:** `EXECUTED_CONDITIONAL_PREEDGE_10_COMPONENT_PLUS_7D / SOURCE-PINNED_MASS_LAW / FINITE_DIFFERENCE_RATE_STRESS / NO_PHYSICAL_CLAIM`

## 1. Scientific question and provenance

ROT013 found that the archived Wu–Xu mass history does not obey the source-native analytically integrable mass-cube law at its terminal saved point. Reconstructing the source-tabulated interval from `M≈1.8366×10^9g` to `1×10^9g` changes source-law contrasts and anti-nucleon sign-kill roots by factors of order two; the **transported hadron/neutron state**, not the late event clock, accounted for nearly all of that change in its controlled ablation.

This rotation addresses a narrower question: does the `0.0984049264s` inconsistency between exact-mass event times, when anchored at two different old saved states, itself alter the fixed-temperature terminal neutron response? Or must it be distinguished from an actual change in the mass-loss rate `Γ`?

Sources:
- Wu–Xu original code and hadron table pinned to `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`; hadron table Git blob `06d0883a27b108692720422294ba2baacd381a64`.
- Mech-S6 original raw public and paper 2×2 trajectories, ZIP SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5` and `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`.
- Mech-S7 ROT013 conditional mass-transport reconstruction and the micro two-temperature EOS inherited from ROT010–012. Others first: DAX-S7 and PRF11 R21–R22 exposed author-code thermodynamics/EOS limitations; Rec10 protects hadron-memory semantics; MT13/LT5 control moving-event target typing and precision.

**Index correctness:** the archived CSV `i` field is **1-based**. Python `iloc[1469]` is source row with `i=1470`, `M=1.8366330858522944e9g` at `t=49.96189862690079s`. There is NO pandas off-by-one error. Earlier summary descriptions saying “saved index 1469” refer to the Python position, not the 1-based `i` field.

## 2. Exact mass clock and gauge proof

The fixed source PBH equation is

`dM/dt = -(Γ/3) M^{-2}`, equivalently `d(M^3)/dt = -Γ`, with

`Γ=4.207579833788249×10^27 g^3/s`.

For the same edge `M_edge=10^9g`:
- event anchored from earliest archived input `t_edge,formation=51.09825802317032s`;
- event anchored from last archived source-active state `t_edge,last=51.19666294957113s`;
- mismatch `δt=+0.09840492640081067s`.

In the ROT013 **conditional** transport, using `u=M/M0`, `dt/du=−3M0³u²/Γ`. The micro EOS, `n_PBH∝a^{-3}`, seven particle/abundance ODEs, and post-evaporation evolution are autonomous apart from an absolute time argument that is consistently translated. Therefore the transformation `t→t+c`, `t_edge→t_edge+c`, `t_cut→t_cut+c`, `t_nuc→t_nuc+c`, holding all corresponding initial states and relative evolution fixed, leaves `X(T_nuc)` **exactly invariant in the mathematical model**. This is a time-coordinate invariance of the reduced comparison, NOT a proof that an arbitrary shift of the original Big-Bang formation clock is physically legal.

Numerical rerun: both `B_exec` and `B_sym`, all four `±δt` shifts, both public and paper source laws. Maximum `|ΔX_shift−ΔX_base| = 1.1102230246251565e−16` and corresponding absolute `X_public` deviations at or below ~`5.6e−17` (Radau, relative tolerance `3e−8`). Two source-law signs are preserved. **A mere consistent clock translation cannot explain ROT013's large corrected state effect.**

The archival mismatch remains a numerical consistency concern because, unlike a global time translation, the original saved trajectory contains a mass-versus-time relation that cannot be corrected by simultaneously moving all physical initial/boundary conditions. It must not be silently converted into a source parameter error estimate.

## 3. Separate synthetic experiment: perturb the cubic mass-loss coefficient

Now deliberately change the equation's `Γ` to `{0.99,1.00,1.01}×Γ_original`, keeping the fixed tabulated `Q_species(M)` source input, same archived preedge initial states, same modelled energy-splitting parameter `χ_EM=0.5`, same fixed-temperature target and `η_B` constant. Reintegrate the source-tabulated `1.8366e9→1e9g` bridge and lower-mass 7D reaction model. This is a **controlled structural stress test**, NOT a physically self-consistent variation of Hawking radiation, since particle spectra, radiation branching, and `Γ` generally share a physical microphysical origin.

| `Γ/Γ0` | `ΔX_n` (`B_exec`) | `ΔX_n` (`B_sym`) |
| ---: | ---: | ---: |
| 0.99 | −1.477098018759504×10⁻⁵ | +1.124026058912930×10⁻⁵ |
| 1.00 | −1.455114464027352×10⁻⁵ | +1.128261533733799×10⁻⁵ |
| 1.01 | −1.433548532037143×10⁻⁵ | +1.132263381153909×10⁻⁵ |

Relative changes in `|ΔX_n|` against the nominal calculation:
- `B_exec`: **+1.51078%** for `Γ−1%`, **−1.48208%** for `Γ+1%`.
- `B_sym`: **−0.37540%** for `Γ−1%`, **+0.35469%** for `Γ+1%`.

Centered finite-difference estimate of local elasticity, `[ΔX(+1%)−ΔX(−1%)]/(0.02 ΔX(1))`, is approximately **−1.49643 (`exec`)** and **+0.36504 (`sym`)**. These values characterize this particular model and parameterization; they do not measure an empirical error distribution.

## 4. Independent precision ladder

Reintegrated all six mass-rate cells using `rtol=3e−9` versus baseline `rtol=3e−8`, with the same prescribed EOS, state interpolation, source law, and fixed-temperature event. The maximum absolute discrepancy of the **source-law contrast** was **3.98030×10⁻¹¹**. Neither source-map sign changed. This is a numerical consistency test, NOT a certified global error bound for the original source Julia 10D solver.

## 5. Decision and negative knowledge

1. The **absolute mass-clock anchor disagreement** (`0.0984s`) is not, by itself, a source-response effect in an autonomous reduced model: consistent time translation changes nothing. This narrows ROT013's state-versus-clock attribution and avoids treating a coordinate shift as a new physical mechanism.
2. The **actual cubic mass-loss rate**, when deliberately modified at the equation level, affects the integrated neutron source-law contrast by measurably different amounts in the two maps. This **does not** license treating the archived `0.0984s` discrepancy as a physical `Γ` uncertainty.
3. The corrected preedge neutron/hadron populations from ROT013 remain load-bearing. The source-law sign remains **conditional**, because antisymmetric proton/neutron spectral index differences below the table can still reverse it.
4. We did **not** run the original Julia 10D integration, obtain original accepted subedge steps, certify global solver error, validate hadron spectra below `1e9g`, derive a mass-fraction helium observable, reconstruct D/H, or infer a PBH exclusion.
5. A stronger next source check remains original Julia `M³(t)` accepted-step trace from full initial state, together with `n_i`, `Q_i`, `T_γ/T_ν`, baryon normalization and event-aligned `X_n`. In particular, correct clocks must be paired with correctly evolved states.

## 6. Artifact contract

Executed reproducible sources: `reproduce_mass_clock_gauge_and_rate_014.py`, `refine_mass_rate_014.py`; input dependencies: ROT013 `edge_bridge_013.py`, `active_micro_bridge_013.py`, `active_source_antispectral_012.py`, ROT009 reaction definitions, ROT010 EOS code and original Mech-S6 2×2 ZIP archives. Outputs: `mass_clock_rate_014.csv/json`, `mass_rate_refinement_014.csv`, log files, signed manifest. No need to trust claimed readback without explicit GitHub fetch verification.

**STATUS:** `EXECUTED_CONDITIONAL_CLOCK_GAUGE_AND_RATE_STRESS / CLOCK_INVARIANCE_PASS / 6_RATE_CELLS_PASS / 6_TIGHT_PRECISION_CELLS_PASS / ORIGINAL_JULIA_10D_NOT_EXECUTED / SOURCE_VALID_E2B_OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_PBH_BOUND`.