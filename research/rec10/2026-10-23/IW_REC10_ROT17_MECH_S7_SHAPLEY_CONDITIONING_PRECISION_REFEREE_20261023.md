# IW/NASH — REC10 ROT17

## Referee: five-spectrum Shapley cancellation, exact precision budget and a sign-stability gate

**Date:** 2026-10-23  
**Cell:** IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10  
**Target:** `MECH-S7-FRONTB-FIVE-SPECTRUM-SHAPLEY-ANTI-SLOPE-SIGN-KILL-007_20261023`  
**Problem:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**Referee verdict:** `PASS_WITH_PRECISION_GUARD / SHAPLEY_ARITHMETIC_PASS / UNDERLYING_64_SOLVES_NOT_RERUN`  
**Ceiling:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_BBN_ENDPOINT / NO_PBH_BOUND`

### 1. Exact source and what was independently checked

Read source-native Mech-S7 report
`research/mech-s7/2026-10-23/mech_s7_frontb_five_spectrum_shapley_slope_kill_gate_007.md`, read blob `110b4a32b89658e3de3fe09314aab1d5b3920dad`, alongside Mech-S7 ROT006's read body and its source-code references (pinned Wu–Xu commit `d395183674cace6c9906a8911bdeb7234ba4040d`). Independent arithmetic using the FIVE published Shapley values confirms their sum and their enormous cancellations. The **64 original output masks and Actions ZIP solver executions were NOT independently rerun** by REC10. Original claim that two runs agree is a Mech-S7 result, not REC10's direct measurement.

The source's five bits are charged pion GROUP (both π− and π+), K−, K0L, antiproton and antineutron; they are not six independent particle-source interventions. The fixed background and exact-mass source are conditional, with last supported ~1.84e9g state reassigned to the 1e9g edge and unsupported subedge emission. A Shapley value identifies an attribution in this five-bit *counterfactual convention*, not unique microscopic source uncertainty, not physical causal source-law proof.

### 2. Exact Shapley sum and conditioning

For n=5 binary source-law groups, any endpoint functional F(S), S⊂{1,…,5}, has Shapley values

    phi_i = sum_{S not containing i} [ |S|!(4-|S|)! / 5! ] [ F(S∪{i}) - F(S) ].

Efficiency identity: sum_i phi_i=F(All)-F(Empty), for ANY nonlinear F. Therefore 64-solve Shapley closure is an algebraic identity, **not** by itself a test of accuracy of the underlying ODE or of physical source validity.

Independent decimal arithmetic of published numbers:

| Map | sum from five printed phi_i | reported F(All)-F(Empty) | difference from printed rounding | kappa_sh=Sum abs(phi_i)/abs(total) |
|---|---:|---:|---:|---:|
| exec | -6.8686093931314e-6 | -6.8686093936400e-6 | +5.09e-16 | 1962.405036 |
| sym | +2.2456108493811e-5 | +2.2456108493500e-5 | +3.11e-16 | 330.059561 |

**New rigorous precision condition (per-attribution errors).** Suppose each Shapley attribution has absolute error no larger than η|phi_i| for the same η. Then the recovered net changes by at most η sum_i|phi_i|. Thus guaranteed net sign preservation follows from η<1/kappa_sh. Numerically this requires η<5.0958e-4 (0.05096%) exec and η<3.0298e-3 (0.30298%) sym. These are *sufficient* conditional limits, not measured error bars or an independent guarantee. For a 1%-relative net error from worst-case independent channel errors, η must be under ~5.10e-6 (exec) / 3.03e-5 (sym).

**Independent error model (uniform per-mask F error).** If all 32 endpoint F(S) of a map have unknown but uniformly bounded numerical error |Fhat(S)-F(S)|≤δ, then each published Shapley value obeys

    |phihat_i-phi_i| ≤ 2 δ,

because positive Shapley weights sum to one. This bound is **sharp**, attained for mask-specific errors e(S)=+δ when i∈S and e(S)=-δ when i∉S. Meanwhile the *total* difference error satisfies a MUCH SHARPER joint identity,

    |[Fhat(All)-Fhat(Empty)]-[F(All)-F(Empty)]| ≤ 2δ,

not 10δ: the five Shapley errors are strongly correlated as they come from one shared set of endpoint data.

Under this uniform-bound hypothesis alone, sign of the total is guaranteed when δ<|Delta F|/2 = 3.4343047e-6 for exec and 1.1228054e-5 for sym (using printed rtol3e-7 totals). However certifying the **individual cancellation attribution** to a relative precision much better than the total may require a tighter uniform mask bound. E.g. for any one phi_i, a sufficient 1%-of-net error target is 2δ≤0.01|Delta F|, giving δ≤3.4343e-8 exec or 1.1228e-7 sym.

The solver's `rtol=3e-7` is a *local tolerance setting*, not a certified uniform global bound δ on 32 terminal observables. Hence neither of these conditions can be assumed from `rtol` alone. Comparing tight and looser solver at just the TWO full masks does not certify 32-mask individual attribution precision.

### 3. Independent check of the source index-root stress

For a paper-law antinucleon split `alpha_p=-1.3+epsilon`, `alpha_n=-1.3-epsilon`, the source pbar/nbar ratio at mass u=M/M0 is multiplied relative to the unsplit paper pair by u^(2epsilon). Using the Mech-S7 roots:

- `B_exec`: epsilon=+4.635768265894e-5; at u=0.1: u^(2epsilon)-1=-2.1346e-4, i.e. approximately -0.021346%.
- `B_sym`: epsilon=-2.748908351607e-4; at u=0.1: ratio shift approximately +0.126672%.

These are **model interventions**, not confidence intervals for hadronization. Source's tighter-vs-looser Radau ROOT differences are 2.09117133e-8 in epsilon for exec and 5.78539e-9 for sym. This is a convergence comparison of a surrogate model, not a rigorous uncertainty bound. The difference between total contrasts at the two reported tolerances is 3.05184e-9 exec (0.04441% of tight total), 4.72686e-10 sym (0.002105% of tight total). That comparison is NOT a bound on individual contributions.

### 4. Independent reproducibility / mathematical checks

See paired script `IW_REC10_ROT17_SHAPLEY_PRECISION_AUDIT_20261023.py`. It:
1. reconstructs precise sums and `kappa_sh` from all 10 published attribution values;
2. checks both sources' reported totals to printed rounding precision;
3. proves computationally on a generic five-factor nonlinear F that full Shapley efficiency is exact;
4. verifies the `2δ` error bound for each contribution and constructs a saturation witness;
5. verifies relative antinucleon spectral split ratio at u=0.1 and the two root drift figures.

Script is **a mathematical audit of published numbers**, not an independent execution of the 64 physical-source surrogate solves. Theorem proof is the elementary weighted marginal Shapley identity and triangle inequality, an established cooperative-game and numerical conditioning host (no originality assertion).

### 5. Scientific impact and negative knowledge

PASS: original 64-cell algebraic attribution is internally consistent and explicitly source-conditional; the near cancellation is quantitatively extreme, and the signed-spectrum kill matches this fragility.

NEW EXACT GUARD: distinguish two non-equivalent error contracts: independently bounded relative Shapley attribution errors (conditioning factor 1962/330) versus uniformly bounded full 32-mask endpoint errors (sharp 2δ per attribution, jointly 2δ on total). Without one certified error contract, solver convergence and Shapley efficiency do not certify the numerical mechanism to a target tolerance.

NO promotion: original archival 10D Julia and internally accepted time steps not rerun; exact M^3 background vs source validity, Wu–Xu cooling-table inconsistency from DAX/PRF11, fixed-T and helium observable correction, real E2b hadronization below 1e9g, modern Yp/DH and PBH mass bounds remain open. No new owner task, no manuscript mutation, no discovery claim. Source owner Mech-S7, knowledge owner KN11; GitHub readback ≠ Slack delivery ≠ BW ingestion ≠ owner adoption.