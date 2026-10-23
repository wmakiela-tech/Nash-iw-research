# MECH-S7 — ROT007: exact five-spectrum attribution and anti-nucleon slope kill gate (conditional Front B 7D)

```yaml
RETURN_ID: MECH-S7-FRONTB-FIVE-SPECTRUM-SHAPLEY-ANTI-SLOPE-SIGN-KILL-007_20261023
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
PROBLEM_ID: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
EXPOSURE: PUBLIC
RESULT_CLASS: EXECUTED_64-CELL_SOURCE-LAW_FACTORIAL / EXACT_SHAPLEY_DECOMPOSITION / EXECUTED_SPECTRAL-INDEX_ROOT_COUNTERTEST
UPSTREAM: Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d
CLAIM: CONDITIONAL_SEVEN_VARIABLE_EXECUTOR_DIAGNOSTIC
NO_SOURCE_VALID_E2B: true
NO_MODERN_Yp_DH: true
NO_PBH_BOUND: true
NO_CANON: true
NO_EXEC_SIGN: true
NO_NOVELTY: true
BW_INGEST: NOT_VERIFIED
```

## 0. Question and material delta versus ROT006

ROT006 found that 7D Wu–Xu hadron+neutron dynamics on one prescribed cosmological history and exact mass-cube PBH evolution suffices to reproduce **opposite signs** of the paper-minus-public sub-table emission law Xn contrasts for the two aggregate-charge maps. But its signs depend on source amplitude. What SPECIFIC spectral groups create this response? Does the pbar/nbar near-cancellation (ROT003) survive the whole nonlinear X(t), n_i(t) evolution, and how little difference in relative spectral laws would destroy the final sign?

**Answer from executed source-only comparator:** Anti-proton and anti-neutron changes each move Xn by order 10^-3, in **opposite directions**, and nearly cancel; small meson contributions and cancellation residual decide the observed net at order 10^-5. In this model, a differential spectral-index perturbation ≈9.27e-5 (exec) or -5.50e-4 (sym) between pbar/nbar source exponents suffices to drive the source-law contrast through zero. Thus signs can be mechanically reproduced but **are NOT robust on independent source-shape perturbations**, even without invoking between-solve background drift. These are model-controlled perturbations, NOT externally measured particle-emission uncertainties.

## 1. Fully typed source and methods

1. Pin original Wu–Xu arXiv-2509.05618 source `main-scan.jl`, `tool_script-parameters.jl`, `tool_script-hadrons_from_PBH.jl` and five source columns in `data/out/hadrons_from_PBH.dat` at commit `d395183674cace6c9906a8911bdeb7234ba4040d`; original Mech-S6 archived 2×2 artifacts re-used with zip SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5` (public) and `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e` (paper).
2. The **unchanged ROT006 core** evolves neutron fraction X and six populations [π−,π+,K−,K0L,pbar,nbar], reconstructed native collision and decay rates, with `u=M/(1e9g)` as time coordinate and exact hot-hole `M^3` mass law. One common PCHIP cosmological `T(t)` and `a(t)` from archived public_exec is prescribed; fixed temperature nuclear endpoint is found by a PCHIP root. Source amplitude held at nominal one, postevaporation populations retained. **No original 10D Julia source run**.
3. **Critical artificial boundary condition:** source-active sample at last saved M~1.84e9g is reassigned as surrogate state at table edge 1e9g. Missing source-valid pre-edge transition, original accepted terminal solver steps, and actual source emission below table edge. Hence not an up-to-date physical PBH model.
4. Five *independently switched* emission spectra: (a) both charged π populations from one aggregate source column; (b) K−; (c) K0L; (d) pbar; (e) nbar. For each of 32 bitmasks, use original public first-two-row loglog spectral extrapolation if bit=0 or publication-associated M^-1.3 if bit=1, all anchored to same table-edge Q_i. For each reaction mapping B_exec/B_sym perform 32 Radau solves (`rtol=3e-7`, `atol=3e-10` on the program's scaled variables): **64 nonlinear 7D integrations**, all source-on and postsource. Exactly compute ΔX at T_nuc and at PBH cutoff.
5. Shapley attribution is the standard average over all orderings of additive marginal endpoint effects. Its algebraic sum equals the 32-bit full-model difference by construction, even with nonlinear cross terms. It is NOT a causal identification of independent hadron measurement uncertainties, nor an IW novelty theorem.
6. Re-run **four nominal endpoints** at `rtol=3e-9`; repeat the full 64-mask factorial using an independent, combined standalone script containing the verbatim ROT006 RHS. Both runs agreed exactly in printed endpoint differences. Separately root-find anti-spectral perturbation with Radau rtol=3e-9, repeat roots with rtol=3e-7.

## 2. Exact factorial source attribution — fixed T_nuc

Values are ΔXn (paper-law marginal minus public-law marginal), **not** Yp. Positive means more Xn at target.

| Source group | B_exec Shapley ΔX | B_sym Shapley ΔX |
|:--|--:|--:|
| pions charged (π−,π+) | +3.650003347748e-06 | +2.044961659422e-06 |
| charged K− | +1.069804688316e-05 | +5.927803586113e-06 |
| neutral K0L | +2.826221296067e-08 | +5.751403527599e-08 |
| antiproton | -6.742931137286e-03 | -3.694698596528e-03 |
| antineutron | +6.721686215449e-03 | +3.709124425741e-03 |

| Map | Total ΔX | Combined pbar+nbar | Combined mesons | Σ|Shapley|/|net| | Sum of all non-additive higher-order contributions vs single-channel baseline |
|:--|--:|--:|--:|--:|--:|
| exec | -6.868609393640e-06 | -2.124492183751e-05 | +1.437631244387e-05 | 1962.405 | -6.937501584314e-07 |
| sym | +2.245610849350e-05 | +1.442582921269e-05 | +8.030279280811e-06 | 330.060 | -3.259591316307e-07 |

*B_exec* precise full difference -6.868609393640e-06, *B_sym* +2.245610849350e-05 at `rtol=3e-7`, consistent with ROT006. Nominal tight (`rtol=3e-9`) independent pairs: exec -6.871661233365e-06, sym +2.245563580777e-05.

The direct **single-channel** source-law interventions have giant pbar and nbar endpoints, but assigning a single species paper-law while all others are public-law changes the physical hypothesis — it is an explicit counterfactual, not a field-measured source model. The Shapley values are its complete well-defined factorial average. Two-body pbar×nbar nonlinear interaction alone: exec -3.869864360628e-07, sym -2.300554161616e-07. Higher-order totals are not numerical error bars; they are difference from first-order source interventions.

**Mechanistic explanation:** a small net neutron change is obtained only after subtraction of two large physically opposite antinucleon directional conversion channels. In the exec map antinucleon residual is net negative; in the sym map it is positive; charged mesons are positive in both. This is stronger than ROT003's pointwise signed forcing condition number: it is a complete nonlinear source-law attribution for the ROT006 reference dynamics. It does **not** establish equivalent attribution in unsolved original 10D code.

## 3. Cheapest falsifier — tiny anti-spectral mismatch

Keep other three spectra exactly M^-1.3, the same common initial state and common background, and original table-edge normalizations. Perturb *only* the two antinucleon power-law exponents by a signed differential amount ε:

    α_pbar = -1.3 + ε,    α_nbar = -1.3 - ε

Define D(ε)=Xn_at_Tnuc[pbar,nbar paper slopes perturbed]−Xn_at_Tnuc[fully public slopes], for each map. Root solve D(ε)=0 using full Radau 7D, postsource memory retained.

| Map | Root ε, rtol 3e-9 | α_pbar−α_nbar at root | D(0), nominal | Root ε, rtol 3e-7 |
|:--|--:|--:|--:|--:|
| exec | +4.635768265894e-05 | +9.271536531787e-05 | -6.871661233365e-06 | +4.633677094563e-05 |
| sym | -2.748908351607e-04 | -5.497816703214e-04 | +2.245563580777e-05 | -2.748966205481e-04 |

At the B_exec root, α_pbar−α_nbar=9.27153653e-05. At PBH mass 1e8 g, the induced pbar/nbar source-rate *ratio* is shifted by just -0.021346% compared to equal paper exponents; at 1e7 g by -0.042688%. The B_sym root requires oppositely directed shifts and a larger index difference -5.49781670e-04; at M=1e8 g the source-rate ratio shifts +0.126672%. Thus an extremely small *relative* change to independently unvalidated source shapes suffices to reverse model endpoint sign. **Not an uncertainty bound or confidence interval.**

Roots at Radau tolerance 3e-7 vs 3e-9 differ by ~2.09e-08 (exec) and ~5.79e-09 (sym). This checks numerical precision of the *reduced model*, not original Julia global errors. More aggressive rtol ladder attempts were computationally intractable/aborted and are NOT reported as PASS.

## 4. Interaction with cross-cell currentness — DAX-S7 and PRF11 findings

**Priority update, others first:** DAX-S7 ROT34–35 first identified a local inconsistency of Wu–Xu source cooling with tabulated adiabatic cooling. PRF11 R21 independently integrated the original 1000-row table on a no-PBH 1MeV→T_nuc interval and found `ln(a_code/a_ad)=0.04558314307928457`, corresponding to `a_code/a_ad=1.046638021704485`; source-table entropy proxy 1.14654082. It separately found a fixed-η_B photon-based baryon comoving proxy 2.85422333 versus 2.48942146 even on adiabatic a(T). These results are SOURCE-CODE/THERMODYNAMIC-PROXY discrepancies, not a measured physical entropy-production or actual perturbation of current ROT007 trajectories.

**Consequences:** ROT007 intentionally holds the same archived source-native T(t), a(t), and baryon n_B=η_B n_gamma(T); its source-law/Shapley *internal* comparison remains algebraically valid, but no simulated fixed-T endpoint can be interpreted as physically validated BBN without separately replacing/testing the source-background and baryon normalization. These newly documented systematic issues cannot be hidden within a purely numerical rtol ladder. The double loss of source credibility is (1) UNVALIDATED subtable hadron source and (2) CONDITIONAL upstream thermodynamic mapping. No physical bound claim.

PRF11 R20 / DAX previous work also identified incompatible Wu–Xu helium readouts across pinned public code `2X/(1−X)`, older article formula and corrected May2026 arXiv v3 near `2X`. This ROT007 uses *only the typed neutron fraction X* at fixed temperature; no helium-abundance conversion is admitted. LT5/MT13 own relevant observation/event framework, REC10 source/referee guard. No originality implied by Shapley or classical exact ODE identities.

## 5. Review, follow-up and stop gates

- Primary report and executable *self-contained* Python reproducer (verbatim ROT006 RHS plus new 32-bit attribution), two original Mech-S6 raw Actions ZIPs and exact metadata, all 64 source mask outputs, spectral index roots, independent tolerance root controls in reproducibility ZIP.
- **Next cheapest discriminator:** original source-native full 10D Julia with archived internal adaptive steps and tolerance ladder; exact PBH M^3 vs t gate; source exponent map at M<1e9g and correct fixed-T event target; insert independent 2026 DAX/PRF cooling correction as separate, explicitly typed background comparator, not as a covert calibration.
- `PASS` here means: all 32 masks per map integrated under declared reduced model; exact Shapley summation; nominal endpoints reproduce ROT006; index root exists and is stable on tested solver tolerances; stand-alone 64-cell script re-executed with exact matching results.
- `STOP` for universal source-law sign assertion: small counterfactual antinucleon spectral mismatch flips signs. Do NOT promote output to physical Yp or D/H, PBH abundance likelihood, new invariant, NOVELTY, CANON, or EXEC. `BW INGEST` must be verified by owner, not assumed.

## 6. Source references

- Original code: https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618
- ROT006 source body: https://github.com/wmakiela-tech/Nash-iw-research/blob/a142d9d35984e0d62f46a174096dbccaf87e6460/research/mech-s7/2026-10-23/terminal_7d_exact_mass_common_background_006.py
- PRF11 R21 source table integral: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r21_integrated_thermal_table_cooling_001.md
- PRF11 R20 / DAX-S7 helium-version source audits (see `#iw-dispatch` 2026-10-23).
- Wu–Xu source version: arXiv:2509.05618, JCAP02(2026)063, v3 corrections treated separately.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_MODERN_BBN / NO_PBH_BOUND / BW_UNVERIFIED`.