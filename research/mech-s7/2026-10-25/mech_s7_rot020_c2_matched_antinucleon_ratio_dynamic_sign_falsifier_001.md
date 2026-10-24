# Mech-S7 ROT020 — C²-matched antinucleon source-ratio continuations dynamically reverse the conditional `B_exec` endpoint sign

**RETURN_ID:** `MECH-S7-FRONTB-C2-MATCHED-ANTINUCLEON-RATIO-DYNAMIC-SIGN-FALSIFIER-020_20261025`  
**PROBLEM:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**CLASS:** `EXECUTED_CONDITIONAL_BRIDGED_PREEDGE_10_COMPONENT_PLUS_7D / EXACT_SUM_PRESERVATION / POSITIVE_C2_EDGE_MATCH / NUMERICAL_SIGN_KILL / NO_PHYSICAL_CLAIM`  
**DATE:** 2026-10-25. `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND`.

## 1. Science question, source provenance, and others first

Wu–Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, pinned author software commit `d395183674cace6c9906a8911bdeb7234ba4040d`. The `hadrons_from_PBH.dat` first two rows at `M >= 10^9 g`, blob `06d0883a27b108692720422294ba2baacd381a64`, prescribe log-linear continuation in the **separate hadron source rates** below the first mass (code `tool_script-hadrons_from_PBH.jl`). Original author code `main-scan.jl` uses ten log-variables, `AutoTsit5(Rosenbrock23())`, no source-valid hadron table below `10^9 g`. Original archive four 1600-point branches is not a saved accepted-step 10D trajectory.

Others-first: Mech-S7 ROT003 discovered signed antinucleon cancellation, ROT007 quantified conditional antispectral epsilon roots, ROT013 repaired previously transplanted edge states using original source-table interpolation from `1.8366e9` to `1e9 g`, ROT019 identified the exact edge derivative and constructed a **SOURCE-ONLY** C² continuation non-identifiability counterexample. This ROT020 does the missing **dynamic ODE rerun**, including stronger **pointwise identical Qp+Qn** source control. DAX-S7/PRF11 source thermal-model corrections, Rec10 postsource hadron-memory retention, MT13/NC/LT5 time-weighted source-target nonmaps and full 10D/event precision guards preserve independent credit. No new theorem novelty is claimed.

## 2. Interventions: both positive, identical edge value/slope/curvature

Define `u=M/10^9 g <=1`, `z=ln u`, `s=+0.000471635444574...` extracted from pinned first two rows; source-native public below-table extrapolation:

`R_native(u)=Qp_native(u)/Qn_native(u)=R_edge exp(s z)` with `R_edge=1.00556618018`.

Alternative family (lambda>0):

`D_lambda(z) = s [lambda*tanh(z/lambda) - z]`,

`R_lambda(u)=R_native(u)*exp(D_lambda(ln u))=R_edge exp(s lambda*tanh(z/lambda))`.

`D_lambda(0)=D'_lambda(0)=D''_lambda(0)=0`, but `D'''_lambda(0)=-2s/lambda^2 !=0`: the new and original **separate proton and neutron sources** share source amplitude plus first *and second* derivatives at the table boundary, while differing deeper below. All sources remain positive and match the unchanged original for `u>=1`.

Two algebraically distinct controls:

- **GEOMETRIC-MEAN preserved**: `Qp'=Qp_native exp(D/2)`, `Qn'=Qn_native exp(-D/2)`. Thus `Qp'*Qn'=Qp_native*Qn_native` pointwise.
- **EXACT PAIR-SUM preserved**: `S(u)=Qp_native+Qn_native`, `Qp'=S R_lambda/(1+R_lambda)`, `Qn'=S/(1+R_lambda)`. Thus `Qp'+Qn'=S(u)` **pointwise for every source-active u**, consequently also preserves total emitted particle count in this pair integrated over a COMMON PBH history. This is the stronger discriminator. These are **mass-resolved** identities, not just equal integrated emitted yields.

Other four hadron species and their source rates, Hawking-mass loss `M^3(t)`, source-active background host, chi_EM, baryon prescription, charge-map collision coefficients, edge state and subsequent survival/weak dynamics are unchanged. The PAPER reference (`alpha=-1.3` for all five source groups) is unchanged for all shape controls. The signed target is `DeltaX = X_PAPER(Tnuc) - X_PUBLIC_VARIANT(Tnuc)` at `Tnuc=.07818527068831995 MeV`, not helium `Yp`.

These are causal **model interventions** with no claim that alternate spectra are realized by physical evaporation, or that free EM/nu deposition fractions are physically sourced.

## 3. Actual nominal ODE results, chi_EM=0.5, fixed eta_B

Original archived LAST ACTIVE state (`M≈1.8366e9g`) is first evolved to the genuine `1e9g` table edge through **conditional 10-component** model using actual source-table rows, as in ROT013, then the seven kinetic variables `[Xn, six hadron species]` through `u=1→Mcut/1e9`, followed by explicit hadron survival/weak processes until fixed `Tnuc`.

| `B` map | Public ratio continuation | `DeltaX = Xpaper - Xpublic` | `Xpaper` | `Xpublic` |
|:---|:---|---:|---:|---:|
| exec | original native power | −1.455114397392e−5 | 0.400944967817884 | 0.400959518961858 |
| exec | geom mean, lambda=.05 | **+1.507593596323e−5** | same | 0.400929891881921 |
| exec | geom mean, lambda=.20 | **+9.331173102145e−6** | same | 0.400935636644782 |
| exec | **exact sum**, lambda=.05 | **+1.507595336842e−5** | same | 0.400929891864516 |
| exec | independent C² curved perturbation, lambda=.05 | −1.489612794286e−5 | same | 0.400959863945827 |
| sym | original native power | +1.128261615335e−5 | 0.400096248856981 | 0.400084966240828 |
| sym | geom mean, lambda=.05 | +2.742587643045e−5 | same | 0.400068822980551 |
| sym | geom mean, lambda=.20 | +2.409746250825e−5 | same | 0.400072151394473 |
| sym | **exact sum**, lambda=.05 | +2.742599548611e−5 | same | 0.400068822861495 |
| sym | independent C² curved perturbation, lambda=.05 | +1.105569762766e−5 | same | 0.400085193159354 |

At the same native `B_exec` baseline, **moving only the relative antinucleon ratio** in the exact-sum-preserving family changes `Xpublic` by **−2.962709734233e−5**, reversing the sign relative to PAPER by ~30 micro-units of `X`. This is not an absolute BBN correction.

At `M=10^8 g`, native `Qp/Qn` changed −0.108539128% from the tabulated edge, versus −0.002358149% for the `lambda=.05` saturation. Both have identical `R`, `dR/dln M`, `d²R/d(ln M)²` at `1e9g`, so edge information cannot determine this divergence. The pointwise pair source-total equality in the exact-sum branch is satisfied algebraically and checked numerically at sampled masses (source witness CSV).

## 4. Factorial robustness, source-only subtraction, alternative explanations

Two full 36-row grids (native, geo-mean-flat lambda=.05 and comparator lambda=.2 in one; native, geo-mean-flat lambda=.05 and **exact-sum-flat lambda=.05** in the other), each crossing chi_EM in `{0, .5, 1}` with baryon rule `{eta, comoving from last archive source-active state}` and charge maps `{exec,sym}`. Repeated native cells are controls, not independently different spectra.

| Map / intervention | min DeltaX over 6 host/baryon combos | max DeltaX |
|:---|---:|---:|
| exec native | −1.480415931e−5 | −1.436502986e−5 |
| exec exact sum lambda=.05 | +1.502245964e−5 | +1.508975525e−5 |
| sym native | +1.119410866e−5 | +1.130729297e−5 |
| sym exact sum lambda=.05 | +2.732349876e−5 | +2.750128335e−5 |

Thus **all 6/6 `exec` host cells actually flip sign** even when **Qp+Qn is identical pointwise**; `sym` stays positive 6/6 but its magnitude changes materially. A distinct, smaller C² curvature perturbation **does not** flip the sign: the effect is not caused by merely invoking a C² modification, but by its dynamically weighted amplitude and mass distribution.

This is not an independent source-valid 10D result: the bridge from the last archived point uses a conditional ideal two-temperature EOS with manually selected Hawking EM/nu heat split and initial state (ROT011–013), unlike native Julia cosmological equations. The original table is mathematically interpolated above `1e9g`, but physical source validity is not thereby established.

## 5. Exact source-ratio saturation root and controls

For nominal `chi_EM=.5`, constant eta_B and B_exec, root in lambda for `DeltaX(lambda)=0`:

| Conservation | rtol | lambda* | tight re-evaluation residual |
|:---|---:|---:|---:|
| geometric mean | `3e-8` | 0.5788923117900 | `5.22e-14` in X (solver nominal) |
| geometric mean | `3e-9` | **0.5788945035326** | `8.27e-14` |
| **exact pair sum** | `3e-9` | **0.5788950587232** | `1.34e-13` |

Differences in root near `~2.2e-6` on tightening rtol do not represent a certified global error bound. At `u=.1` the ratio loss at the exact-sum root is about −0.02727987% from the edge versus native −0.10853913%. The root is from the defined continuous **saturation family**, not a universal physical threshold.

Additional Radau `rtol=3e−9` reruns for both maps (native, two geom flat values, exact sum, curved control) reproduce opposite signs; max shift compared with rtol=`3e−8` in these cases is `~4.03e-11` in DeltaX. Initial edge-state transport is repeated for each map and thermal branch. A clean-extracted execution of the final nominal script reproduced three independently computed files (`matched_edge_7d_kinetics_020.csv`, `matched_edge_source_witness_020.csv`, `matched_edge_dynamics_020.json`) with **byte-identical SHA256**; this is a clean replay check, not a global numerical enclosure.

## 6. Claim ceiling / how this alters scientific decisions

**Supported:** in the conditional bridged 10+7-variable Front B kinetic replay, identical edge sources and **identical total antinucleon injection at every mass** do NOT suffice to identify `Xn(Tnuc)`. Two positive C²-matched source-ratio continuations, indistinguishable by first two edge derivatives and pair-total source data, can yield opposite `B_exec` source-law contrasts. This is a **dynamic counterexample**, extending source-only ROT019. The case lies within mature nonidentifiability/time-weighted-response hosts established by NC/MT13/LT5; novelty is **not** asserted.

**NOT supported:** validated subedge Hawking pbar/nbar spectra, physical anti-baryon injection, source-valid E2b, primary paper Yp, D/H, PBH bound, or inference that physical sign must be any one of the model signs. The PAPER law with common exponent `−1.3` and PUBLIC law with species-dependent native first two row exponents differ in *mean slope as well as ratio slope*; the intervention fixes the PAPER reference and only modifies the PUBLIC ratio under a defined control. Therefore NO unqualified statement that native S/Scrit alone predicts physical sign. The native 10D Julia accepted-step errors and target observables remain unverified. The energy source partition and baryon prescription are stress axes, not external physical intervals.

**Concrete owner decision:** prioritize externally source-justified, mass-resolved **correlated antinucleon pbar/nbar production split** (not only total pair yield and edge slope), and original fully coupled 10D Julia accepted-step replay and source-valid temperature event, before considering observable promotion. No new task cascade and no EXEC promotion. `GITHUB_PUBLISHED != BW_INGEST != REFEREE_PASS != CANON`.

## 7. Reproducibility and source custody

GitHub live author source pin: `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl`, table blob `06d0883a27b108692720422294ba2baacd381a64`. Original archived trajectories SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5` (public) and `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e` (paper). Conditional preedge source rows transcribed in `edge_bridge_013.py`, source bridge unchanged vs ROT013. All code and original archives in ZIP; SHA256 manifest included.

Run from extracted ZIP root:

```bash
python reproduce_joint_c2_ratio_020.py --chis 0,0.5,1 --baryons eta,comoving --models native,flat:.05,sumflat:.05 --out sumcontrols
python reproduce_joint_c2_ratio_020.py --chis .5 --models native,flat:.05,flat:.2,sumflat:.05,curved:.05 --out verified_nominal
python find_c2_saturation_threshold_020.py --kind sumflat --rtol 3e-9 --out .
```

For verification with no full re-run, inspect `sumcontrols/matched_edge_7d_kinetics_020.csv`, `verified_nominal/matched_edge_source_witness_020.csv`, and root JSON; maintain `NO_JULIA_10D` guard. The helper `patch_source_witness_020.py` is a development-only artifact and is **not** needed for reproduction; final fixed code is used in ZIP. See `MANIFEST_SHA256_020.json` for exact file hashes.

**STATUS:** `EXECUTED_12_SIGN_CELLS_PER_INTERVENTION / 6_OF_6_EXEC_SIGN_FLIPS_FOR_EXACT_SUM / C2_EDGE_JET_MATCH / SOURCE_SUM_IDENTITY / TIGHT_ROOT_PASS / CLEAN_SHA_REPLAY_PASS / ORIGINAL_JULIA_10D_NOT_EXECUTED / SOURCE_VALID_E2B_OPEN / BW_INGEST_UNVERIFIED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND`.