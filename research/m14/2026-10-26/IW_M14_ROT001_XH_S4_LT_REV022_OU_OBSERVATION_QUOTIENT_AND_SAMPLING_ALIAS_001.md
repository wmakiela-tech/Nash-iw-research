# IW/NASH — M14 ROT001 — XH-S4 → LT: iloraz obserwacyjny i aliasowanie próbkowanej dynamiki OU

artifact_id: IW_M14_ROT001_XH_S4_LT_REV022_OU_OBSERVATION_QUOTIENT_AND_SAMPLING_ALIAS_001_20261026  
exposure: PUBLIC  
claim_ceiling: EXACT_CONDITIONAL_CLASSICAL_OU_MATHEMATICS / MATURE_SYSTEM_IDENTIFICATION_HOST / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN  
sync_state: GITHUB_WRITE_TARGET / BW_PENDING_OWNER_REVIEW / LT_AUTHORIAL_UPTAKE_NOT_ASSUMED  
return_id: M14-ROT001-XH4-LT-SAMPLED-OU-OBSERVATION-QUOTIENT-001_20261026  
date: 2026-10-26  
from_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14  
to_cells: XH-S4; current LT author (LT5/LT6 subject to separately verified activation); PRF11/PRF12 and REC10 for optional bounded review  
science_scope: fully specified 2D isotropic OU, exact path-law and transition-kernel statements, no empirical fitting.

## 1. Currentness, source and ownership

- XH-S4 FOUR ROTATIONS 027–030 reported 2026-10-26, independently read primary public research records; their four source controls are XH-owned. We cite, do not relabel those as M14 research.
- XH-S4 ROT030 first posed the dissipative OU stationary-law nonidentifiability: `dZ=(-I+ωJ)Z dt+√2dW`, identical invariant `N(0,I)` and different probability currents. [XH source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_030_DISSIPATIVE_IDENTIFIABILITY_INTERVENTIONS_PAPER_AGENTS_20261026.md).
- LT working **REV022** (Drive document titled “Redukcja, transport i wierność opisu efektywnego”, dated 2026-10-26) already explicitly acknowledges XH-S4 ROT030 in §7.5f; this report is a NON-OWNER addendum candidate, not a modification to the book or a new XH citation claim.
- PRF11 R16 independently studied OU **measurement noise in fixed physical time**: that is a different statistical host (unknown scalar signal with OU observational noise), not rotational drift aliasing of an observed 2D OU state. [PRF R16](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-22/IW_PRF11_R16_OU_physical_time_infill_20261022.md).

## 2. The exact model and sufficient assumptions

Take `Z_t∈R²`, `J=[[0,-1],[1,0]]`, `ω∈R`, independent standard 2D Brownian motion `W`, known diffusion coefficient `√2 I` and linear drift `A_ω=-I+ωJ`. The initial law is specified, is the SAME under the compared ω, and has finite second moment when covariance is needed. Measurements below are exact laws, not finite experimental estimates. No unmodelled gain, anisotropic diffusion, forcing, or changing detector orientation is admitted.

For all ω: stationary covariance `Σ=I`, since `A_ω I+I A_ω^T+2I=0`. The unique invariant Gaussian is `ρ(z)=(2π)^{-1}exp(-|z|²/2)`. With diffusion matrix I, stationary probability current `j_ω(z)=ω Jz ρ(z)` differs across ω, but the one-time stationary marginal does not.

## 3. Bounded result A — the complete radial path has NO information about ω

**Statement.** For any fixed initial point `z0` (and for the same general initial law), the full path law `Law((|Z_t|)_{t≥0})` is independent of ω. Thus any observable that is a measurable function ONLY of the whole radial path, including adaptive sampling times determined by prior radial observations without dynamical intervention, has an ω-independent law. The target `τ(ω)=ω` does not factor through this radial experiment even with continuous ideal measurement.

**Proof (rotation coupling).** Solve the reference SDE `dX=-Xdt+√2 dB` with initial `X_0=z0`. Define `Y_t=R_{ωt}X_t`. Itô product rule gives `dY=(-I+ωJ)Ydt+√2 R_{ωt}dB`. Because `R_{ωt}` is a deterministic orthogonal matrix, `W_t=∫₀ᵗ R_{ωs}dB_s` is a standard 2D Brownian motion. Therefore `Y` has exactly the target ω-OU law and `|Y_t|=|X_t|` PATHWISE for all t in the coupling. QED. Independently, for `S_t=|Z_t|²` the scalar generator is `(-2s+4)f'(s)+4s f''(s)`, independent of ω. The radial quotient is an exact PROCESS-level nonmap, not just a stationary marginal nonmap.

## 4. Bounded result B — regular sampling aliases the WHOLE vector path experiment

**Statement.** At a fixed cadence `Δ>0`, even an ideal, oriented measurement of the full 2D vector `Z_{nΔ}` has exactly the SAME joint law for `ω` and every `ω'=ω+2πk/Δ`, `k∈Z`, for any common initial law.

**Proof.** The discrete Markov transition is
```text
Z_{(n+1)Δ} | Z_{nΔ}=z ∼ N( Φ_ω(Δ) z, Q(Δ) )
Φ_ω(Δ) = exp(-Δ) R_{ωΔ}
Q(Δ) = (1-exp(-2Δ)) I .
```
The covariance is independent of ω by isotropy. Replacing ω by `ω+2πk/Δ` leaves the rotation, and therefore the entire conditional Markov transition kernel, EXACTLY unchanged. Equal initial laws imply equal finite-dimensional sampled path laws. This is the classical continuous-to-discrete **system aliasing / matrix-logarithm** obstruction, not an original discovery. On an a priori interval `ω∈(-π/Δ,π/Δ)` a single exact full-state transition kernel admits only one ω branch, but finite noisy inference still requires a likelihood and uncertainty model. QED.

## 5. Bounded result C — incommensurate lags remove exact alias, not inverse instability

**Statement.** If exact oriented full-state transition kernels are known for TWO positive lag lengths `Δ1,Δ2` satisfying `Δ2/Δ1∉Q`, the pair uniquely identifies `ω∈R` under this model. If the parameter domain is unbounded, the inverse from the paired transition matrices to ω is nevertheless NOT continuous at the true matrix pair.

**Proof of injectivity.** Equal kernels for ω,ω' give `(ω−ω')Δ_i ∈2πZ` for i=1,2. If `ω−ω'≠0`, division makes `Δ2/Δ1` rational, a contradiction. Hence ω=ω'. **Instability:** choose `Δ1=1, Δ2=√2`, and `ω_n=ω_0+2πn` for integer n tending to infinity with `dist(n√2,Z)→0` (continued-fraction approximations). Then the first kernel is EXACTLY identical, while the second transition matrix tends to that at ω0, yet `|ω_n−ω0|→∞`. Hence the inverse on its image is not continuous at the ω0 pair. On a fixed compact, a priori ω interval it becomes continuous by compactness, but no uniform guarantee independent of that interval follows. QED.

**Legality of the positive clause.** It concerns exact mathematical transition kernels with known state axes and common time units, not a finite noisy record, hidden states, scalar-only readout, unknown delays, arbitrary interventions or a generalized non-Gaussian stochastic differential equation. “Two lags” is NOT a promise of practical identifiability under arbitrary instrument constraints.

## 6. Deterministic control and reproduction

Standalone [verification script](./verify_m14_rot001_ou_visibility.py) checks exact rational stationary Lyapunov algebra and the radial generator on 108 finite monomial instances; numerical 2×2 matrices check regular exact alias and its rejection by lag √2; continued-fraction denominators `n=12,70,408,2378` demonstrate increasingly close nonidentical second-lag matrices at arbitrarily separated parameters.

Execution: `python verify_m14_rot001_ou_visibility.py`. Local deterministic execution PASS; exact Fraction 108/108, max regular-lag alias matrix entry difference `2.78e-17`, incommensurate second-lag difference `0.453673...`, nearly aliased second-lag differences `0.04471,0.007714,0.001324,0.0002271`. These controls check implementation of formulas; the proofs in §§3–5, NOT floating samples, establish the mathematical claims. Original XH source code is not rerun here.

## 7. XH-S4 source-typed integration for the LT current author

| XH-S4 source | Legal host and existing XH result | LT relevance / boundary |
|---|---|---|
| [ROT027 JWST + heavy seeds](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_027_JWST_HEAVY_SEED_LRD_TRANSFER_IDENTIFIABILITY_20261026.md) | line-scattering versus virial mass proxy; conditional heavy-seed simulation; population×duty×selection degeneracy | §2–3 target descent and nuisance; **heavy astrophysical seed != primordial PBH**, no transfer to NASH physics |
| [ROT028 laboratory gravity](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_028_MILLIGRAM_FORCE_YUKAWA_IDENTIFIABILITY_20261026.md) | measured wafer force vs separate POINT-MASS Yukawa two-distance/gain toy | §2.5/§7.5f partial observation and gain; no wafer fit, no automatic `E_g→Yukawa` map |
| [ROT029 LVK / PBH tails](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_029_LVK_O4A_INDUCED_GW_PBH_TAIL_STATISTICS_20261026.md) | source-specific O1–O4a null; fixed-variance synthetic mixture changes rare tail ~197× | §2 target insufficiency: two-point amplitude != threshold tail, no cosmological abundance conclusion |
| [ROT030 dissipative identifiability](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_030_DISSIPATIVE_IDENTIFIABILITY_INTERVENTIONS_PAPER_AGENTS_20261026.md) | source UIDD theorem with strong assumptions; OU stationary current counterexample | Already in LT §7.5f; M14 adds explicit radial full-process nonmap + discrete full-vector alias + incommensurate-lag unstable recovery |

**LT uptake proposal (NOT APPLIED):** add one compact “OU temporal observation contract” following the existing XH-S4 paragraph in REV022 §7.5f: contrast four DISTINCT observational regimes: stationary marginal, continuous radial history, regularly sampled full 2D state and a pair of incommensurate exact full-state transition kernels; record each regime's own identifiability ceiling. Do NOT order these different experiment classes by an unjustified Blackwell-dominance inequality. Preserve distinct mathematical claims: invariance of radial law; exact alias of regularly sampled vector law; injectivity without stability of irrational-lag design. This supports existing LT §2.4, §2.5 and §7.5f. Owner chooses whether/how to integrate.

## 8. Mature-host subtraction and falsification

Historical roots: matrix exponential / nonunique logarithm in continuous-time identification, OU Gaussian semigroups and isotropic rotations, quotient and statistical experiment theory. Explicit external context (some accessed via abstract/summary, NOT a systematic theorem prior-art review):
- Jason R. Blevins, *Identifying Restrictions for Finite Parameter Continuous Time Models with Discrete Time Data*, Econometric Theory 33 (2017), DOI 10.1017/S0266466615000353, https://jblevins.org/research/sde .
- B. Mu et al., *Identification of linear continuous-time systems under irregular and random output sampling*, Automatica 60 (2015), DOI 10.1016/j.automatica.2015.07.009 .
- *A Sampling Theorem for Exact Identification of Continuous-Time Nonlinear Dynamical Systems*, IEEE TAC 69 (2024), DOI 10.1109/TAC.2024.3409639 .

Falsifiers of the **overbroad** transfer: use `|Z|` alone even with infinitely dense time; use equally spaced full-state sampling with unrestricted ω; allow unknown time clock, unknown two-channel gain, anisotropic diffusion, hidden state, different forcing or source generator; extrapolate the OU proof to UIDD arbitrary SDE or physical NASH geometry. Each invalidates the corresponding positive inference.

Status: `M14_MATERIAL_ROT001 / MATH_HOST_EXACT / REPRO_CONTROL_PASS / XH_CREDIT_PRESERVED / LT_OWNER_REVIEW_ONLY / NO_CANON / NO_EXEC_SIGN / BW_PENDING`. `SENT != RECEIVED != ACCEPTED`.