---
artifact_id: IW_MECH_S9_ROT002_WUXU_RHO_ENTROPY_EOS_NULL_COMPATIBILITY_SOURCE_FIRST_001_20261112
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
created_at: 2026-11-12
document_type: RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_NATIVE_STATIC_EQUATION_COMPATIBILITY_NEGATIVE_CONTROL / CONDITIONAL_INCONSISTENCY_CANDIDATE
claim_ceiling: SOURCE_FORMULA_AND_SOURCE_TABLE / NO_NATIVE_JULIA_RUN_BY_MECH_S9 / NO_AUTHOR_EXECUTION_ID / NO_PBH_BOUND / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# Mech-S9 ROT002: thermodynamic background null compatibility of frozen Wu–Xu rho ODE with stated adiabatic entropy law

## Source provenance and scope

Research question: **Does the frozen v2 native Julia RHS for Standard Model energy density preserve the declared photon-temperature/entropy relation when PBH abundance is zero?** A reproducible source-level negative control is needed before interpreting C1–C4 source variations. This is a static conditional mathematics/source audit, not proof of physical error, not proof of the published JCAP executable and not a new PBH contour.

Original Wu–Xu authors repository `Fenyutanchan/Primordial-Black-Hole`, pinned commit `d395183674cace6c9906a8911bdeb7234ba4040d`, root `arXiv-2509.05618/`:
- `main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, source 10D `evolution_system!` around lines 77–85, in particular `d_log_ρ_SM_dη = -4 + d_ln_N_ρ_d_ln_T / (3 + d_ln_N_s_d_ln_T) - d_m_PBH_dt * n_PBH / (H * ρ_SM)`. Here `η=ln a`, `ρ_SM` is the thermodynamic bath energy density, and PBH source term vanishes at `n_PBH=0`.
- `tool_script-N_relativistic_species.jl`, blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`, defines `Nᵨ(T)`, `Nₛ(T)` with linear interpolation in `ln T`, and the density-to-temperature relation sampled from `ρ(T)=(π²/30)Nᵨ(T)T⁴`.
- `data/ext/N_around_m_e.csv`, blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`, 1000 rows with `T` in MeV, `Nᵨ`, `Nₛ`. This is not an observational error budget.
- Author manuscript arXiv 2509.05618 v3 (May 2026), §2.1 Eq (2.7): `g_{*,s}(Tγ) a³ Tγ³ = constant` via entropy conservation. This is **later than** frozen v2 code, and no exact historical JCAP Fig5 executable identity has been proved.
- External standard derivation of entropy/radiation effective degrees of freedom: Eq (2.7) plus `ρ=(π²/30)g_{*ρ}T⁴`, valid for declared adiabatic effective background model. No assumption that entropy is conserved in the presence of PBH heating.
- Later Badacz PREREG062 FIRST launched ROT022 Julia driver, but S1 failed for all four variants BEFORE `magic()` due parsing comment lines `#`. REC11 ROT020 and INT9 ROT015 independently diagnosed parser and related guards. Mech-S9 does not claim a native Julia run.

## 1. Exact equation reconciliation at the zero-PBH null

Define `qρ = d ln gρ/d ln T`, `qs = d ln gs/d ln T`.

Taking Eq (2.7) as the source-declared entropy-conserving control, `d ln T/d η = -3/(3+qs)`. Together with `ρ∝gρT⁴`, this forces:

```
f_adiab(T) := dlnρ/dη = -3(4+qρ)/(3+qs).
```

Setting `n_PBH=0` in frozen source code gives:

```
f_code(T) := dlnρ/dη = -4 + qρ/(3+qs).
```

Subtracting these exactly (no numerical approximation):
```
f_code - f_adiab = 4(qρ-qs)/(3+qs).
```
Thus they agree only when `qρ=qs` (assuming finite denominators). Equality of `gρ` and `gs` is NOT required by the source; the actual table has distinct slopes around electron-positron annihilation. It is therefore an **internal compatibility candidate**, not a direct statement about authors' intent or alternative nonadiabatic physics.

The source-model predicted drift of comoving entropy `S=a³ gs(T) T³` under **zero PBH** is
```
dlnS/dη = 3 + (3+qs) f_code/(4+qρ)
        = 4(qρ-qs)/(4+qρ).
```
The exact null test for a code implementing the manuscript's Eq (2.7) is `dlnS/dη=0`.

Note: if the authors intended an explicitly nonadiabatic, multi-temperature prescription differing from Eq (2.7), this must be specified and checked against their table and first law; one cannot call this an established physics bug without that clarification. In the actual Julia `from_ρ_to_T` is a separately tabulated numerical inverse, so its interpolation can add further numerical differences. We did not run it.

## 2. Source-table numerical check (NOT native ODE)

Source table and interpolation semantics were read directly from the pinned GitHub blob via the authenticated connector. The original 1000-row piecewise-linear log-T interpolation was reconstructed in JavaScript, `qρ,qs` evaluated analytically within each knot segment. Two independent Gauss–Legendre quadratures (2-node/4-node) split at EVERY original interpolation knot agree in computed `Δln a` to less than `3e-13`; a second direct integral of `dlnS/dlnT` matches `3Δln a` to `1.2e-14`.

At selected source-table temperatures (MeV):
```text
T               qρ         qs         f_code       f_adiab
0.500000        0.140426   0.132262   -3.955168    -3.965594
0.200000        0.620405   0.549072   -3.825192    -3.905589
0.100000        0.716535   0.598849   -3.800899    -3.931703
0.07818527      0.440118   0.359058   -3.868976    -3.965502
```

For matched initial `T=1 MeV`, use the **two compared background laws** to integrate to fixed terminal T. This is a source-table projected temperature/scale-factor comparison, **not** the actual author `magic()` ODE result:
```text
T_end MeV      a_code/a_adiab     (S_end/S_start)_code
0.500000        1.000794119        1.002384249
0.200000        1.010949156        1.033208433
0.100000        1.037517565        1.116828206
0.0781852707    1.046638022        1.146540823
0.050000        1.053206519        1.168262981
0.030000        1.053685052        1.169856136
```
At 0.07818527 MeV, `Δln a=0.0455831430793`. `S` in the adiabatic comparator is constant by definition, whereas static source code implies approximately 14.65% comoving entropy gain across the chosen 1→0.078185 MeV no-PBH interval **under exact source table rho-to-T mapping**. This is not a physical entropy production measurement or Yp shift.

Check: if `qρ=qs` identically (e.g. constant degrees of freedom), the mismatch and spurious comoving-entropy drift vanish identically. The target temperature band includes both the historical `T0≈0.078185MeV` and Badacz's native runtime-local `T1≈0.099689MeV`; neither was calibrated or integrated by Mech-S9.

## 3. Mechanistic implication, falsification and STOP

This candidate affects the **background time-temperature clock**, potentially independent of p13 or B_sym hadronic variants. Mech-S9 ROT001 showed that a shared T1 does not guarantee a shared physical time. Therefore any corrected variant should log the source background thermal functions separately from Yp and hadron channels. Earlier Mech-S7 SOURCE-OFF != HADRON-CONVERSION-OFF, strict ROT035 ODE error OPEN, and unresolved native/physical E4 remain intact.

Falsifier / reopening contract:
1. Determine whether the production-time/final journal executable uses the same `f_code`, and whether the intended model declares Eq (2.7) **for this same total bath** under zero PBH. Both are currently UNKNOWN; a v3 text versus v2 code comparison alone is not journal-build identity.
2. With authorized Julia (none in Mech-S9 runtime), run a **zero-PBH no-injection null** with frozen `gρ,gs` and dense `T(a),ρ(a),S(a)` output. Compare actual `dlnS/dη` and integrated `S` to above source-algebra prediction; check inverse-interpolation/tolerance errors and alternate temperature branches.
3. If the source model explicitly includes nonadiabatic entropy generation in this limit, record the source law and physical carrier, not a silent equation swap. If it intends Eq (2.7), derive the corrected background RHS and assess consistency with physical neutrino/photon sector temperature evolution before mutating code.
4. Only after legal owner approval and native run could one measure any effect on `T1`, `X_n`, 10D trajectories or contours. No numerical source-table comparison is a PBH exclusion or a nuclear-network validation.
5. Remain `NO_PBH_BOUND / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / E4_SOURCE_BLOCK / HISTORICAL_FIG5_BUILD_OPEN`.

**Next action**: treat as a distinct possible **background EoS/entropy null** requiring source-meaning/adjudication, not an automatic C5 grid, external-author contact or task cascade. Do not suppress the positive code/entropy contrast merely because C1–C4 parser is separately blocked.

## 4. Reproducibility and custody

- Companion publicly pinned source-locked Node.js reproducer: `research/mech-s9/2026-11-12/mech_s9_rot002_entropy_null_source.mjs`. Requires original frozen `N_around_m_e.csv` and rejects incorrect Git blob bytes before producing calculations. This code was authored and source-readback checked; **Node CLI execution is not claimed**.
- Independent local Python stdlib `mech_s9_rot002_source_entropy_null.py` synthetic algebra self-test PASS and `py_compile` PASS, SHA256 `2be1a334fb77787a3cef33d6510c8b11d28808e58eeab48df251e0768296ebf8`. Original CSV numerical results above were computed directly in connected JavaScript, not Python from a downloaded original file.
- Cross-code 2/4 Gauss and entropy integral re-expression checks PASS in connected JS. No Julia, BlackHawk/PYTHIA, BBN network, physical observation, independently refereed verdict or BW readback from this turn.

`ROT002 = EXACT_STATIC_ALGEBRA_AND_FROZEN_TABLE_DIAGNOSTIC / REPRO_SOURCE_PINNED / ZERO_PBH_THERMODYNAMIC_NULL_CANDIDATE / NATIVE_JULIA_UNEXECUTED_BY_MECH_S9 / SOURCE_CLASS_VS_JCAP_UNKNOWN / E4_BLOCK / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.
