artifact_id: MECH-S7-FRONTB-POSTEVAP-SOURCE-OFF-COMMON-BACKGROUND-FLOOR-GATE-001
return_id: MECH-S7-FRONTB-POSTEVAP-COMMON-BACKGROUND-FLOOR-AND-TARGET-TYPING-GATE-001
cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
date: 2026-10-21
exposure: PUBLIC
result_class: EXECUTED_RAW_TRAJECTORY_DIAGNOSTIC / EXACT_CONDITIONAL_THEOREM / SOURCE_NATIVE_FLOOR_AUDIT
claim_ceiling: NUMERICAL_DIAGNOSTIC_ONLY / NO_SOURCE_VALID_E2B / NO_MODERN_BBN_ENDPOINT / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY
sync_state: GITHUB_PENDING_BW_INGEST

# Mech-S7 rotation 001 — Wu–Xu terminal response: source-off sign, shared-background drift and log-floor blind spot

## 0. Result and boundary

The four archived Mech-S6 Wu–Xu 2×2 trajectories were recovered and checked against their original ZIP SHA256. The paper-vs-public source-law sign reversal under different charge maps is already present immediately after the unobserved terminal PBH injection interval, but the same contrasts flip sign again on the later saved source-off common-scale-factor grid. The upstream cosmological background equations are mathematically independent of the hadron populations and reaction/source map. Hence a **numerical convergence/common-background gate** is required before giving physical meaning to the small reduced endpoint source-law effect, even after bit-identical runner replication.

There is also a separate source-native floor interface error: with PBH source off, log-population flooring may leave the population decay equation unchanged yet alter the neutron-fraction forcing. The prior floor flags do not test the post-evaporation regime because the tracer returns false whenever n_PBH=0.

This work is a source-specific diagnostic and exact conditional control, not a claim of an error in the published Wu–Xu exclusion boundary. Which public helper/law generated its final published scan is not established.

## 1. Evidence and execution

- Primary public Wu–Xu upstream: Fenyutanchan/Primordial-Black-Hole, commit d395183674cace6c9906a8911bdeb7234ba4040d.
- Upstream files: arXiv-2509.05618/main-scan.jl; tool_script-hadrons_from_PBH.jl; data/out/hadrons_from_PBH.dat (blob 06d0883a27b108692720422294ba2baacd381a64).
- Wu & Xu, JCAP02(2026)063, DOI 10.1088/1475-7516/2026/02/063.
- Point M_initial = 6e9 g, beta=1e-16. This is a strong reduced-executor diagnostic, not a PBH bound point.
- Public-law ZIP: Actions artifact 12116193467, SHA256 75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5.
- Paper-law ZIP: Actions artifact 12192535869, SHA256 3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e.
- 1600 samples each, exactly the same sampled scale-factor values. Four cells: public_exec, public_sym, paper_exec, paper_sym.

No fresh Julia solve was performed. Original raw trajectories were downloaded from live Actions artifact custody and analyzed independently with Python, NumPy, Pandas, SciPy. The local reproduction script checks archive hashes, reloads records, recreates the Q/T endpoint, calculates source contrasts, conditional source-free response and edge source-law slopes.

## 2. Terminal interval localization

Define Delta_L X as X(paper M^-1.3 branch) minus X(public helper branch), with reaction map fixed. Source-active points end at zero-based index 1469; source-inactive points begin at index 1470.

| Index | Source | T of public_exec (MeV) | Delta_L X, B_exec | Delta_L X, B_sym | Difference-in-differences |
| --- | --- | ---: | ---: | ---: | ---: |
| 1469 | on | 0.1447372646 | 0 | 0 | 0 |
| 1470 | off | 0.1424339130 | -2.052432093e-5 | +1.355900263e-5 | +3.408332356e-5 |
| 1500 | off | 0.0808077796 | +7.218222398e-8 | -1.394641036e-5 | -1.401859258e-5 |
| 1502 | off | ~0.0775707 | +1.466525607e-6 | -1.945112974e-5 | -2.091765535e-5 |

Under B_sym, the source-law contrast first flips its saved-grid sign after shutoff at index 1494. Under B_exec it flips at 1500. These observations have been checked from raw records, not inferred from the 2×2 scalar endpoints.

No saved source-active output samples the PBH interval below M=1e9 g: last active mass about 1.84e9 g, first inactive mass near the evaporation cutoff. Internal accepted solver steps are NOT recorded. Thus neither Q_h(t) nor per-hadron sources in the crossing interval have been localized.

## 3. Exact conditional source-off sign theorem

Reading the upstream neutron evolution equation with zero effective hadronic forcing:

dX/dt = -Gamma_SM(t) [X - (1-X) exp(-Q/T(t))] - X/tau_n.

For two histories on the SAME prescribed T(t), with source and effective hadron forcing both zero, their difference z obeys:

dz/dt = -[Gamma_SM(t) (1+exp(-Q/T(t))) + 1/tau_n] z.

Consequently z(t)=z(t0) exp[-integral_t0^t (Gamma_SM(1+exp(-Q/T))+1/tau_n) ds]. The multiplier is positive. Therefore the sign cannot flip under these explicit conditions. This is ordinary scalar linear-ODE algebra, not an IW novelty claim.

Conditional replay using the public_exec saved T(t) as a common post-shutoff background, PCHIP interpolation and a high-resolution positive damping integral yields attenuation 0.795570572 near T_nuc. At saved index 1502:

| Law contrast | Conditional common-background null | Actual same-a raw contrast |
| --- | ---: | ---: |
| B_exec | -1.632854575e-5 | +1.466525607e-6 |
| B_sym | +1.078714348e-5 | -1.945112974e-5 |

This FAILS the deliberately simplified same-background/no-effective-hadrons null, but DOES NOT prove the full executor is wrong: the solver may use floored hadron populations after nominal source shutoff, and separate adaptive trajectories have different numerical cosmological backgrounds. Appropriate decision is to isolate these seams rather than promote this null into full-dynamics truth.

## 4. Triangular background and target readout

In audited evolution_system!, t, rho_SM and m_PBH depend only on background/PBH state. Hadron populations and X_n do not feed back into these background differential equations. Hence all four scenarios should share the background for identical initial parameters in the exact ODE, even though independently integrated solver realizations drift numerically.

The source code interpolates X_n as a function of Q/T to evaluate the reduced YP proxy. Independent replication of this interpolation using the saved trajectories reproduces all four published diagnostic YP values to displayed precision. It is NOT correct to interpolate linearly in T and call that the executor readout.

At fixed physical target T_nuc=0.07818527068831995 MeV:

- Delta_L X(B_exec, fixed T) = -1.898856657e-5.
- Delta_L X(B_sym, fixed T) = +1.266713121e-5.

At a common a_ref selected so that public_exec reaches T_nuc:

- Delta_L X(B_exec, same a) = +1.290456921e-6.
- Delta_L X(B_sym, same a) = -1.844731929e-5.

Both change sign between the two DIFFERENT conditioning coordinates. The fixed-T target is correctly source-typed; however, numerical T(a) divergence between scenarios that should have identical background is significant relative to this small effect. A frozen common-background replay with tolerance/step convergence is therefore required before certification.

## 5. New source-native log-floor correction

The source uses n_eval=exp(max(log_n,-100)) in evolution_system!, but the exported trajectories use un-floored n=exp(log_n).

For a population with injection S and loss D, the log-state prescription induces dn/dt=(n/n_eval)S-D n. When S=0 this reduces exactly to dn/dt=-D n even if the floor is active. That parent observation is TRUE FOR THE POPULATION SUBEQUATION.

However the upstream neutron equation reads n_eval, not n. Define epsilon=exp(-100) in the source number-density units, d_i=max(epsilon-n_i,0), and positive p-to-n and n-to-p per-population coefficients c_Ai,c_Bi. The exact additive discrepancy relative to an unfloored neutron equation is:

rho_X_floor=(1-X) sum_i c_Ai d_i - X sum_i c_Bi d_i.

Thus rho_X_floor can be nonzero when PBH injection S is zero. SOURCE OFF does not imply that full coupled neutron evolution is floor-preserving.

The tracer run_one_point.jl sets floor_active(n,npbh)=false whenever npbh=0. Therefore the prior zero floor flags give NO INFORMATION about the post-evaporation log-population floor. Nor do saved sample flags constitute an accepted-internal-step audit.

Magnitude of this floor forcing: NOT YET BOUNDED in a source-matched run. Exact structural difference is not a claim of order-one or observable target error.

## 6. Subedge source sign control

The first two rows of pinned hadrons_from_PBH.dat yield public log-log exponents:

| Aggregate channel | Edge slope |
| --- | ---: |
| charged pion pair | -1.200486 |
| charged kaon pair | -1.196651 |
| K0L | -1.196805 |
| p+pbar | -1.204291 |
| n+nbar | -1.204763 |

Paper-branch scaling below the table edge is M^-1.3. It therefore increases ALL species emission rates relative to the public-helper extrapolation: +6.8%-7.4% at M/M0=0.5, and +24.5%-26.9% at M/M0=0.1. These are extrapolation-branch comparisons only; NO source-valid E2b species uncertainty is derived.

Because hadronic neutron forcing is F=(1-X)A-XB, sign-uniform increases in emitted hadrons need not produce a sign-uniform X target response. Species and directional A/B response and feedback must be disentangled.

## 7. Scientific placement / cheapest falsifier

- PRESERVE: Mech-S6 source-level aggregate-vs-single-charge mismatch and measured supported-domain M>=1e9g charge-map effects (a different claim).
- HOLD: the small terminal source-law effect as a numerically qualified physical/source-specific correction. Bit-identical rerun does not establish solver convergence.
- NEXT ACTION: freeze one background t(a), T(a), H(a), m(a); replay all four hadron/X blocks on this common background and vary solver tolerances and max steps. Export raw log n, injection S, true n, floored n_eval, A,B,F,X on accepted steps, especially M=1e9g -> evaporation. Compare fixed Q/T readout to fixed common-a controls with explicit coordinate typing.
- After this gate, identify whether K0L vs charged channels or X feedback produces robust interaction. If it disappears under a common-background/tolerance or floor gate, record NEGATIVE_KNOWLEDGE rather than a corrected paper bound.

The reproduction and raw-artifact hash audit are available in the accompanying Mech-S7 rotation-001 reproducibility package. Primary GitHub scientific body is subject to BW owner qualification. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_BOUND / GITHUB_PENDING_BW_INGEST.
