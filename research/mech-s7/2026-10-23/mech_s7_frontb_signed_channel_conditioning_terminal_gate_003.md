# MECH-S7 — Front B: signed channel conditioning and terminal-execution gate (rotation 003)

```yaml
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
RETURN_ID: MECH-S7-FRONTB-SIGNED-CHANNEL-CONDITIONING-AND-TERMINAL-RUNTIME-GATE-003
TYPE: EXECUTED_SAVED_TRAJECTORY_DECOMPOSITION / EXACT_LOCAL_SENSITIVITY_IDENTITY / UNEXECUTED_JULIA_TRACE_PATCH
EXPOSURE: PUBLIC
SOURCE_MODEL: Wu-Xu arXiv-2509.05618, pinned d395183674cace6c9906a8911bdeb7234ba4040d
MODEL_STATUS: REDUCED_EXECUTOR_DIAGNOSTIC_ONLY
GOALS: CHARGE_MAP_SENSITIVITY / CHEAP_KILL_TEST / SOURCE-NATIVE_ACCEPTED_STEP_TRACE
NO_SOURCE_VALID_E2B: true
NO_MODERN_HELIUM_DEUTERIUM_ENDPOINT: true
NO_PBH_BOUND: true
NO_CANON: true
NO_EXEC_SIGN: true
NO_NOVELTY_INFERENCE: true
BW_INGEST: UNVERIFIED
```

## 0. Scientific question and result

What is the cheapest physically typed mechanism test capable of explaining why the reduced Wu–Xu 2×2 **source-law contrast** can change sign when the aggregate-to-single-charge map is changed, before claiming any PBH abundance or modern BBN endpoint?

**Result**: The source-native hadronic neutron forcing in the last supported, saved source-active state is extremely **cancellation-conditioned**, particularly between antineutron and antiproton reaction channels. At this state, equal fractional errors in all channel populations produce essentially a proportional effect, whereas anti-correlated antineutron/antiproton changes of **0.272% each** (literal executor map) or **0.674% each** (charge-symmetric map) suffice to reverse the instantaneous forcing. Such perturbations are **deliberate algebraic counterfactuals**, not estimated physical errors or claims about what the paper source law does. They identify a falsifiable *direction of source uncertainty* to trace in the unresolved terminal mass regime. The saved outputs do not record that regime.

The full Julia 10D source-native, accepted-step, common-background tolerance-ladder test has NOT been executed here. A fail-closed source patcher was built and statically tested; it does NOT upgrade evidence absent an actual Julia execution. The first key scientific discriminator therefore remains open.

## 1. Provenance and executed controls

Primary code: `Fenyutanchan/Primordial-Black-Hole`, commit `d395183674cace6c9906a8911bdeb7234ba4040d`, files `arXiv-2509.05618/main-scan.jl`, `tool_script-parameters.jl`, `tool_script-hadrons_from_PBH.jl`, `data/out/hadrons_from_PBH.dat`. Peer-reviewed article Wu and Xu, *JCAP* 02 (2026) 063, DOI 10.1088/1475-7516/2026/02/063.

Frozen previous executor point: initial PBH mass 6×10^9 g, beta 10^-16, chosen for diagnostics, not bounds. Four branches: `public_exec`, `public_sym`, `paper_exec`, `paper_sym`.

GitHub Actions raw artifacts and SHA256:

- `12116193467` (public source): `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`.
- `12192535869` (paper M^-1.3 source): `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`.

Archive hashes checked before analysis. Reconstructed source-native **A and B** from the six saved hadron number densities and source-code cross sections. The reconstructed A/B normalization agrees with the saved `A_GeV/B_GeV` at source-active points across all branches, with a single common dimensional factor (assertion tolerance 3×10^-8). This validates the **decomposition of the existing trajectory**, not its source validity or convergence.

At all saved *source-active* points, public-law and paper-law trajectories coincide within each fixed reaction map; the source-law difference arises in an interval with no saved active steps. Last active saved state = zero-based index 1469, M approximately 1.8366×10^9 g (`B_exec`) or 1.8353×10^9 g (`B_sym`), T approximately 0.14474 MeV. The first saved source-off point = index 1470, at mass near the artificial final cutoff (~7–11 g) in archived runs. There is no sampled source-active state below the 10^9 g first table row.

## 2. Six-channel source-native forcing

Use the source-coded cross sections, with a common suppressed `mbarn` area factor and source-native Coulomb factors `Fc`:

- `A` (p→n): `1.5 Fc_pi n_pi- + 31 Fc_K n_K- + 7 n_K0L + 28 n_nbar`.
- `B` (n→p): `1.7 n_pi+ + 26 n_K- + 7 n_K0L + 28 n_pbar`.
- `F=(1−X)A−XB`; the source's original `F_had_GeV` matches the reconstruction.

Define signed constituent terms `F_i=(1−X)c_Ai n_i−X c_Bi n_i`. At `R=A+B>0`, `F=R(q−X)`, where `q=A/R`. **No division by R is meaningful in the saved source-off records with A=B=0.**

At last source-active point:

| Diagnostic | `B_exec` | `B_sym` |
|---|---:|---:|
| neutron fraction X | 0.497967914253 | 0.496214274722 |
| q=A/(A+B) | 0.499321916169 | 0.499566803992 |
| q−X | +0.001354001915 | +0.003352529270 |
| F (GeV) | +7.72180608e-28 | +9.57052472e-28 |
| κ₁=Σ abs(Fᵢ)/abs(F) | 368.6441 | 148.7985 |
| κ₂=sqrt(Σ Fᵢ²)/abs(F) | 260.0729 | 104.9752 |
| F_pbar/F | −183.5886 | −73.8053 |
| F_nbar/F | +184.2088 | +74.6493 |
| F_K0L/F | +0.000897 | +0.001349 |

All saved source-active samples below 5×10^9 g have **positive** F on the inspected branches; within this narrow supported-domain subset, observed median κ₁ is 122.87 for `B_exec` and 48.28 for `B_sym`. This says **neither source-law sign nor bound** in the unsampled subedge interval.

## 3. Exact directional condition number and stress test

Let `F=Σ F_i ≠0`; consider small independent fractional changes `δ_i` in the six **instantaneous population numbers**, holding temperature, X, and all cross-section coefficients fixed. Then exactly, because the forcing is linear in n:

`δF/F = Σ_i w_i δ_i`, `w_i=F_i/F`; hence `Σ w_i=1`.

For a uniform common scaling δ_i=δ of **all six** populations, `δF/F=δ` regardless of κ₁. High κ alone does **not** imply high sensitivity to a common source-law factor.

For antinucleons alone:

- Common scaling δ_pbar=δ_nbar=δ gives `δF/F=δ(w_pbar+w_nbar)`; for 1% this is only +0.6202% (`B_exec`) and +0.8439% (`B_sym`) of the original F.
- Differential scaling δ_pbar=+ε, δ_nbar=−ε gives `δF/F=ε(w_pbar−w_nbar)`; for ε=1%, the changes equal **−367.80%** and **−148.45%**, respectively. Instantaneous sign reversal thresholds are ε=0.271889% (`B_exec`) and 0.673607% (`B_sym`).
- Antineutron decrease alone: 0.542862% and 1.339598%; antiproton increase alone: 0.544696% and 1.354915%. All at the stated *fixed saved state*, not evolving outcomes.

If **and only if** the six fractional errors are independent, mean-zero, equal-variance random variables with common standard deviation σ, the standard first-order propagated relative SD is `κ₂ σ`. An illustrative σ=1% gives relative SD 260.07% (`B_exec`) or 104.98% (`B_sym`). For perfectly correlated common scaling, the same σ gives only 1%. These illustrative error models are NOT measured uncertainties, observational likelihoods or PBH abundance constraints.

A real subedge law may induce **correlated** emission changes for pbar/nbar, potentially suppressing the dangerous differential direction. At the supported table edge, their public log-log slopes were measured around −1.20429 and −1.20476, only ~0.00047 apart; the paper comparator applies −1.3 to both. Extrapolating any of these rates below 10^9 g is the very source-validation problem under investigation. Therefore the existence of the sensitivity direction alone does not show the law change actually follows it.

## 4. Mechanism map and falsifier

**Candidate mechanism M-PBH-1**: distinct emitted antinucleon channel rates, annihilation/conversion and charge mapping alter the p→n versus n→p balance; because the net F is cancellation-conditioned close to equilibrium `q≈X`, species **relative** differences or background+timing changes can dominate a tiny aggregate source-law endpoint contrast.

**Competing hypotheses**:

- H1: terminal *differential* pbar/nbar injection/source response drives robust sign interaction;
- H2: pion/kaon kinetics and different lifetimes drive it, despite small endpoint baryon balance;
- H3: the observed reduced endpoint interaction is dominated by solver tolerance, adaptive step placement, cutoff handling or floor;
- H4: source-law × reaction-map interaction exists for the reduced executor but does not survive source-valid hadron injection plus full BBN Yp/D/H.

**Cheapest discriminatory execution**: exact upstream 10D Julia on frozen common cosmological background, all 2×2 branches, explicit tolerance ladder, **accepted internal solver states** across `M<10^9 g` and the evaporation cutoff, logging species-wise emission `Q_h`, true and floored log populations, A_i, B_i, F_i, X, `t`, `T`, `m`, source flag and target `X(T_nuc)` by linear interpolation in `Q/T`. Run differential pbar/nbar and uniform antinucleon stress *only as controlled diagnostics*; compute a sign-and-amplitude stability interval across solver tolerances and source variants.

**PASS**: reproducible source-native accepted-step boundary crossing with stable fixed-T contrasts and species response under explicit tolerance changes. **REPAIR**: source local numeric nonconvergence/missing branch logging. **STOP/HOLD**: source below table not validated; no physical source-derived endpoint/BBN bound regardless of numeric stability. The stable supported-domain charge-map mismatch is a separate retained source observation.

## 5. Runtime interface prepared but not executed

Companion `instrument_wuxu_terminal_accepted_steps.py` is a fail-closed textual patch on the **exact** pinned Wu–Xu 
`solve(evolution_problem, AutoTsit5(Rosenbrock23()))` line. It supplies configurable `MECH_RTOL`, `MECH_ATOL`, `MECH_TRACE_DIR`, `MECH_LABEL` and writes a CSV over accepted 10D solver states, including the subedge flag, floor flags and source rates. Local Python compilation and fail-closed marker smoke checks PASS. **Julia is not installed in the local research runtime, so the emitted Julia code is not compile-tested/executed.** This probe still integrates four cases independently; it is an accepted-step test precursor, not yet a mathematically shared-background implementation. It must not be reported as an executed solver run until GitHub Actions or a Julia host returns source-aligned step logs and numerical results.

## 6. Empirical anchor / genealogy / recipients

Real empirical anchor: BBN primordial helium mass fraction and D/H, with a source-matched PBH Hawking→hadronization→BBN and observational likelihood map. The archived Wu–Xu reduced `Y_P=2X/(1−X)` proxy is greater than one at this artificially strong test input; it is NOT a physical helium yield nor a modern Yp+D/H endpoint. Numerical conditioning is not new physics.

Prior art: classical sensitivity/condition numbers and linearized reaction-network control. `κ₁`, `κ₂` and the local counterfactual thresholds are standard mathematics applied to a specific frozen source state, not a novelty claim.

Message intended: REC10/M13 local claim review; KN11 currentness and BW routing; MT13 science priority and Moderator final custody. Neither repo write nor Slack dispatch is BW ingestion, owner acceptance, or EXEC.