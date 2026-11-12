---
artifact_id: IW_MECH_S9_ROT001_WUXU_EXACT_NEUTRON_DIRECTIONAL_RESPONSE_AND_ENDPOINT_CLOCK_GATE_001_20261112
created_at: 2026-11-12
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_DERIVED_EXACT_IDENTITY_AND_STATIC_G0_CHECK / SCIENCE_FIRST / NOT_JULIA_EXECUTED_HERE
claim_ceiling: MODEL_INTERNAL_MECHANISM / NO_PBH_BOUND / E4_SOURCE_BLOCK / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# Mech-S9 ROT001 — exact neutron-directional response and endpoint-clock separation in original Wu–Xu 10D source

## 0. Sources, predecessor and currentness

This is a source-specific application of elementary scalar ODE variation of constants, **not** a new theorem, physical BBN validation or native Julia 10D result. It responds to the Mech-S8 ROT021/022 C1–C4 design, retains all ownership and negative knowledge, and does not overwrite predecessor files.

- Original authors: Fenyutanchan/Primordial-Black-Hole, commit `d395183674cace6c9906a8911bdeb7234ba4040d`, file `arXiv-2509.05618/main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, specifically lines 87–99 (neutron equation), 145–177 (`magic` setup, `T_nuc` in end horizon), 179–210 (interpolated readout).
- Mech-S8 ROT021 selected C1–C4 with shared same-runtime calibrated `T1`; ROT022 made source-locked Julia driver `0223f0c5bc092cd3b738e0297917b1936864fe9d`, explicitly unexecuted by Mech-S8.
- AUD1 ROT031/032 FIRST found manuscript `2 X_n` vs code `2 X_n/(1-X_n)` discrepancy; Badacz REVIEW053 FIRST native helium calibration; XH-S3 HARVEST022–024 FIRST original E4 source gaps; Mech-S8 ROT020 OWNER ACK; Badacz PREREG062 FIRST actual Julia S1 input failure; REC11 ROT020 and INT9 ROT015 independently established static parser failure and additional guard concerns. No firstness transferred to Mech-S9.
- Mech-S9 read original author Git tree at pinned commit: 13/13 named original source file Git blob SHA1 equal to exact values in ROT022 driver; original `Manifest.toml` absent from that tree. This is repository tree/blob identity check, not a local package-resolution or Julia runtime check.
- Mech-S9 local container: no `julia`, no `juliacall`, no `pyjulia`. Mech-S9 has NOT run native Julia. Badacz did attempt ROT022: all four variants stopped at line 66, `ArgumentError: invalid base 10 digit '#' in "#"`, before any `magic()` call. Existing data have comments. Separate Badacz D1 data-input deviation is an independent continuation; do not rewrite its preregistration.
- No evidence here for BW ingestion or independent referee PASS. Original JCAP final Fig5 execution identity, source-matched BlackHawk/PYTHIA E4 spectra, and rigorous Mech-S7 ROT035 ODE error certificate remain OPEN.

## 1. Source-native directed transition decomposition

Along **each actual source-model trajectory**, define `X(t)=X_n(t)`, `T=T_SM(t)`, `x=Q/T`, and the nonnegative conditional directional coefficient candidates (if all density, rate and lifetime inputs are physical and nonnegative):

```text
A(t) = Γ_SM exp(-x)
     + n_πminus σv_(πminus,p→n)
     + n_Kminus σv_(Kminus,p→n)
     + n_K0L    σv_(K0L,p→n)
     + n_nbar   σv_(nbar,p→n)

B(t) = Γ_SM + 1/τ_n
     + n_πplus  σv_(πplus,n→p)
     + n_Kminus σv_(Kminus,n→p)
     + n_K0L    σv_(K0L,n→p)
     + n_pbar   σv_(pbar,n→p).
```

These terms are a **direct regrouping** of the authors' source `dX_n_dt_SM + decay + π + Kminus + K0L + pbar + nbar`, lines 87–99. In particular Kminus and K0L contribute to BOTH directions. Do not collapse charge-resolved populations to an undirected total emission number.

The source neutron equation is, exactly,
```text
dX/dt = A(t) (1-X(t)) - B(t) X(t)
      = A(t) - λ(t) X(t),     λ=A+B.
```
`A,B` are **endogenous history functionals** of the full coupled 10D solution, NOT externally independent coefficients. Once a complete trajectory is fixed, the above scalar identity holds along it. Its exact integrating-factor representation on a common physical-time interval is:
```text
X(t) = exp(-∫[t0,t] λ) X(t0)
     + ∫[t0,t] exp(-∫[s,t] λ) A(s) ds.
```

## 2. Exact finite-difference identity for any two full 10D model variants

Compare two variants `1,2` on the SAME physical time interval, with their own actual 10D histories `(X_i,A_i,B_i)`. Define `δX=X_2-X_1`, `δA=A_2-A_1`, `δB=B_2-B_1`. Without linearization, and even though the hadron densities and temperatures respond endogenously:
```text
d(δX)/dt + (A_2+B_2) δX = (1-X_1) δA - X_1 δB.
```
Consequently:
```text
δX(tc) = exp(-∫[t0,tc] λ_2) δX(t0)
       + ∫[t0,tc] exp(-∫[s,tc] λ_2)
           ((1-X_1(s)) δA(s) - X_1(s) δB(s)) ds.
```
For C1–C4 comparisons with same mass, beta and original initial data, `δX(t0)=0` in exact source semantics. No assertion of physical source adequacy is involved.

**Practical discriminator:** after an authorized corrected native run, reconstruct `A_i,B_i,X_i,T_i` from full saved high-precision trajectories and their source-specific directional rates; evaluate the integral independently. A material difference beyond separately bounded quadrature/interpolation/solver errors falsifies the purported source-to-readout reconstruction (or exposes a missing term/convention). It does not by itself falsify the physical Wu–Xu paper.

## 3. Exact end-clock partition — same T1 is not automatically same t

The target in all corrected variants is `Y_i = 2 X_i(t_i^*)`, where `t_i^*` denotes the uniquely selected physical-time crossing `T_i(t)=T1` (if it exists). The two variants may have DIFFERENT `t_i^*`, because different emission/charge histories can affect `ρ_SM` and the temperature clock. A shared MeV value `T1` is not a shared cosmic time.

Choose `tc` within the common verified integration domain, `tc <= min(t_1^*, t_2^*)`. Exactly:
```text
Y_2 - Y_1
 = 2 [ X_2(tc)-X_1(tc) ]
 + 2 ∫[tc,t_2^*] (A_2(1-X_2)-B_2 X_2) dt
 - 2 ∫[tc,t_1^*] (A_1(1-X_1)-B_1 X_1) dt.
```
First bracket = common-clock dynamic difference (section 2). Last two integrals = different endpoint/temperature-crossing tails; the tails include weak, decay AND post-source existing-hadron conversion as written in original RHS. `SOURCE_OFF != HADRON_CONVERSION_OFF` remains true.

This exact identity provides a **source-native mechanism attribution protocol** for C2−C1 (source law), C3−C1 (conditional charge map), C4 interactions, and heavy-end clock effects, without pretending that a fitted beta-root shift is additive. It is not an independent strict numerical error certificate, because `A,B,t_i^*` still require accurate source-matched native trajectories and certified integration/interpolation.

## 4. Exact algebraic control (NOT Julia / NOT Wu–Xu simulation)

Choose dimensionless constant rates `A1=1/3,B1=2/3,A2=2/3,B2=1/3`, common `X(0)=1/4`, thus `λ1=λ2=1`. Then
```text
X1(t)=1/3 - exp(-t)/12
X2(t)=2/3 - 5 exp(-t)/12
δX(t)=(1-exp(-t))/3.
```
The exact finite-difference forcing is `(1-X1)δA-X1δB=1/3`, yielding precisely the above difference, **despite identical summed `A+B`**. A distinct terminal time `t2*=2`, `t1*=1` also satisfies the endpoint partition with `tc=1`. Independent symbolic SymPy control returned two exact zero residuals (difference formula, clock formula). This is a known algebraic example of directional identifiability failure, not fresh experimental data and not a physical calibration.

## 5. Requirements / kill gates for any future native test

1. Repair the comment-parser before reusing either pinned point fixture and preserve BOTH original frozen files. Validate index bounds, exactly two finite columns and 17-digit Float64 log-beta roundtrip as INT9 pointed out. Pin effective source patches, especially the `B_sym` helper, separately from the 13 original author SHA1s.
2. Real same-runtime `T1` receipt requires source, manifest/runtime, solver, unique/declared temperature crossing and monotonicity/branch check. Single SBBN `2X=.245` checkpoint is not source provenance proof (REC11).
3. When G1 and authorized small G2 actually succeed, save `A,B,T,t,X` and individual directional rates on the SAME time grid for the selected common mass/beta inputs. Check the scalar source identity and the exact paired finite-difference/clock partition with a preregistered error budget (solver, interpolation, quadrature, floating input and physical source are distinct error objects).
4. If the source's `T(t)` has nonunique crossings, stop and declare branch/endpoint convention. If no common time support, no paired decomposition claim. If residuals exceed the discretization/solver budget, no mechanism attribution or contour promotion until resolved.
5. Even perfect tests are MODEL_INTERNAL: no unvalidated E4 hadronization, no PBH beta bound, no full 100×100 run, no author contact or canonical upgrade from this note.

## 6. Disposition

`MECH_S9_REHYDRATED / 13_OF_13_GIT_TREE_BLOBS_PASS / AUTHOR_MANIFEST_ABSENT / LOCAL_JULIA_ABSENT / BADACZ_NATIVE_S1_INPUT_PARSER_FAIL / DIRECTED_NEUTRON_IDENTITY_EXACT / END_CLOCK_PARTITION_EXACT / SYNTHETIC_SYMBOLIC_CONTROL_PASS / MECH_C1_C4_ODE_NOT_EXECUTED_HERE / E4_SOURCE_BLOCK / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.

Next owner-side opening: preserve Badacz PREREG062 input-deviation provenance, wait for its actual result rather than duplicate runs; once an authorized corrected and independently reproducible native pilot exists, apply the exact mechanism/clock discriminator on logged trajectories. No new task cascade.
