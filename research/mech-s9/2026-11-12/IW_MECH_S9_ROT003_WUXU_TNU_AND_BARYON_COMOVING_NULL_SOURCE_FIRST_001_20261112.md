---
artifact_id: IW_MECH_S9_ROT003_WUXU_TNU_AND_BARYON_COMOVING_NULL_SOURCE_FIRST_001_20261112
date: 2026-11-12
origin: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
class: SOURCE_NATIVE_BBN_BACKGROUND_TWO_TEMPERATURE_AND_BARYON_NUMBER_NULL
exposure: PUBLIC
status: STATIC_SOURCE_TABLE_EXACT_ALGEBRA / NATIVE_JULIA_NOT_EXECUTED / REFEREE_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_PBH_BOUND / NO_PHYSICAL_UPGRADE / NO_JCAP_EXECUTABLE_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# Mech-S9 ROT003 — Wu–Xu two-temperature neutrino clock and comoving baryon normalization diagnostic

## Why another rotation

ROT002 first isolated a conditional `rho_SM` vs entropy-Eq(2.7) consistency failure in original Wu–Xu 10D Julia code. ROT003 rereads the **actual later article Appendix A** and identifies a distinct source-control interface: (T_\nu a=constant) (A.3) and baryon-number conservation vs `n_B=eta_B*n_gamma(T)` (source code line 65). No patch is executed and no PBH outcome inferred.

**Original source firstness / hard source locks.** Authors Quan-feng Wu, Xun-Jie Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, arXiv:2509.05618 v3 06 May 2026, DOI 10.1088/1475-7516/2026/02/063. Primary full-text `https://arxiv.org/html/2509.05618v3`, §2.1 Eq(2.7) and Appendix A Eqs(A.1)–(A.3), not third-party summaries. Original author GitHub `Fenyutanchan/Primordial-Black-Hole` pinned at `d395183674cace6c9906a8911bdeb7234ba4040d`: `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`; physical RHS lines 39–142; `n_gamma=2*zeta(3)*T_SM^3/pi^2`, `n_B=eta_B*n_gamma` lines 64–65; `rho_SM` flow line 85; injected hadron physical density sources and collision losses lines 102–128; original thermodynamic `N_rho`/`N_s` interpolation in `tool_script-N_relativistic_species.jl` Git blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`; original `N_around_m_e.csv` blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8` and 1000×3 original rows.

Do not collapse v3 prose and earlier code as the same final JCAP build: final Fig5 producer unknown. No new Badacz D1 native pilot result shown in latest GitHub owner history; original PREREG062 S1 four-variant Julia parser failure before ODE still the verified state. PREREG result firstness belongs Badacz.

## 1. Source A.1/A.3 neutrino clock test is forced by ROT002 null

The *later* article explicitly specifies:
```
Equation (2.7): g_s(T_gamma) a^3 T_gamma^3 = constant
Appendix (A.1): T_nu = T_gamma * min((g_s(T_gamma)/10.75)^(1/3), 1)
Appendix (A.3): T_nu a = constant
```
Assumptions are standard pre-/post-e± neutrino decoupling with negligible subsequent entropy transfer to neutrinos. These equations are related, not statistically independent evidence. However the explicit physical (T_\nu a) contract makes a failed scalar entropy null directly relevant to the two-temperature clock.

For original Julia source `n_PBH=0`, using original table (g_\rho(T),g_s(T)) and `rho(T)=pi²/30*g_rho(T)*T^4`, put (q_\rho=dln g_\rho/dlnT), (q_s=dln g_s/dlnT):
```
f_code(T)=dln rho/dln a=-4+q_rho/(3+q_s)
dln a/dln T=(4+q_rho)/f_code(T)
f_adiab(T)=-3(4+q_rho)/(3+q_s)
```
ROT002 exact `f_code-f_adiab=4(q_rho-q_s)/(3+q_s)` remains. Integrate the *source code projected scalar null* from initial `T_i=1MeV` to selected T to obtain `L(T)=ln(a(T)/a_i)`. For all selected T below 1MeV the source table has `g_s(T)<10.75`, so the A.1 `min` is on its first branch, giving:
```
R_nu(T) := [a(T) T_nu(T)]/[a_i T_nu(T_i)]
         = exp(L(T))*(T/T_i)*(g_s(T)/g_s(T_i))^(1/3)
         = exp(L(T)-L_adiab(T)).
```
The A.3 zero-PBH null requires R_nu=1. This is **the same source background discrepancy re-expressed at the neutrino-clock interface**, NOT a second independent mathematical defect.

## 2. Baryon number is a different conservation law

The **original** source lines 64–65 use `n_B(T)=eta_B n_gamma(T)` with frozen `eta_B=6.1e-10` (parameter file `tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`), and `n_gamma(T)=2*zeta(3)T^3/pi²`. In a post-baryogenesis, no-net-baryon-injection background, the conserved quantity is baryon **number per comoving volume** `n_B a^3`, not strictly `n_B/n_gamma` across `e+e-` annihilation. Photon number per comoving volume changes even for adiabatic expansion, whereas baryon number does not.

For the source-specified fixed-`eta_B` auxiliary and scalar background:
```
R_B(T) := [(a(T)^3 n_B^code(T)) / (a_i^3 n_B^code(T_i))]
        = exp(3L(T))*(T/T_i)^3.
dln(a^3 n_B^code)/dln a = 3+3 f_code/(4+q_rho)
 = 3 q_rho(4+q_s)/[(3+q_s)(4+q_rho)].
```
In a genuinely number-conserving prescription the right side must be zero. Crucial separation:
```
R_B(T)= [g_s(T_i)/g_s(T)] * R_nu(T)^3.
```
The first term is the **ordinary photon-number production** issue from `eta_B` held fixed while photon entropy changes, even if Eq(2.7) is enforced. The second term is the additional `rho_SM`/entropy source-null mismatch isolated in ROT002.

At one **specified final calibration temperature** `T_ref=0.07818527068831995 MeV`, set conserved baryon normalization `n_B^cons(T_ref)=n_B^code(T_ref)` and compute, purely as a conditional source model correction,
```
n_B^cons(T) / n_B^code(T) = R_B(T_ref)/R_B(T).
```
This is an algebraic comparison at matched T, not an edit to the author's 10D model, not an observed baryon measurement and not a predicted change to Yp. An alternative definition of `eta_B` or a genuine net baryon source would alter this contract and must be explicitly documented.

## 3. Frozen original table evidence and numerical cross checks

Performed actual connected JavaScript numerical integration using 1000 original table rows with the author's `LinearInterpolation` semantic (linear values in ln T) and exact analytic within-knot log slopes. Integrations split at **every original log-T knot**, independently 2/4 node Gauss–Legendre. Max absolute difference below `5e-13` across tested temperatures. Independent `R_B = (gs_i/gs_T)*R_nu^3` identity and formula for `dln(a³n_B)/dln a` algebra control PASS (local Python SymPy source-free test separately PASS). **No original Julia/10D/PBH runtime executed by Mech-S9.** Full-table/source-byte-locked Node companion is written and Git readback verified, but actual Node CLI execution is not claimed.

```text
T [MeV]        R_nu=[aTnu]/[a_i Tnu_i]    R_B=[a^3nBcode]/initial   nBcons/nBcode (late-ref)
1.0000000          1.000000000                 1.000000000                 2.854223331
0.8000000          1.000101306                 1.010263060                 2.825227848
0.6000000          1.000405547                 1.032604674                 2.764100729
0.5000000          1.000794119                 1.055219045                 2.704863358
0.3000000          1.003893255                 1.188486819                 2.401560780
0.2000000          1.010949156                 1.445547051                 1.974493552
0.1500000          1.020057832                 1.777663209                 1.605604097
0.1000000          1.037517565                 2.466633922                 1.157132927
0.0781853          1.046638022                 2.854223331                 1.000000000
```

At T_ref:
```
R_B,adiab= g_s(1 MeV)/g_s(T_ref) = 2.4894214613
R_entropy,code = R_nu^3 = 1.1465408229
R_B,code = 2.4894214613 * 1.1465408229 = 2.8542233308
```
Therefore **do not** attribute the total 2.854 factor solely to the ROT002 background discrepancy: the approximately 2.489 term is already present under a perfectly adiabatic background if `eta_B` is frozen across photon-number change. A factor 2.854 source proxy at 1MeV is **not** a claim that physical baryons are actually created.

## 4. Direct native hadron-mechanism contact

Original `main-scan.jl` lines 109–128 use exactly this auxiliary `n_B` in all six hadron collision sinks. The antibaryon channels contain:
```
d n_antineutron/dt =
 J_antineutron(t) - n_B(t) * [X_n sigma_v(nbar+n->n+anything)
                         + (1-X_n) sigma_v(nbar+p->n+anything)] * n_antineutron
d n_antiproton/dt =
 J_antiproton(t) - n_B(t) * [X_n sigma_v(pbar+n->...)
                       + (1-X_n) sigma_v(pbar+p->...)] * n_antiproton
```
Original `X_n` RHS in lines 93–94 then uses `n_antiproton sigma_v(pbar+n)` for n→p and `n_antineutron sigma_v(nbar+p)` for p→n. These are **coupled** source equations: `n_B` indirectly controls conversion through antibaryon survival, not by a direct multiplicative `n_B` factor in `dX_n/dt`.

**Conditional monotone comparison theorem:** if (T(t), X_n(t), J(t)\ge0), initial (n_{\bar N}\ge0) and all cross sections are held identical, and the source-comparison `n_B^cons(t)>=n_B^code(t)` holds on that fixed time interval, then the scalar linear comparison principle gives `nbar_cons(t)<=nbar_code(t)` for the same initial density. This is only a *controlled frozen-trajectory directional statement*. Once (T,X,H,J) and other hadron species are recomputed together, the theorem does **not** establish sign or magnitude of Yp, helium, beta-root or PBH contour change. No steady-state estimate may be transferred blindly.

**One further source-only check to preserve for later (not run):** physical hadron number densities in the original 10D code `n_h` have source/loss terms but no explicit cosmological `-3H n_h` dilution in `dn_h/dt` at lines 109–128, whereas `n_PBH` does dilute as (a^{-3}). For a hypothetical inert stable hadron with zero source/loss, its source equation would keep physical `n_h` constant instead of (a^{-3}). This may be an intentional fast-interaction approximation (typically rates much faster than H) and must NOT be labeled a material physical bug without `H/Gamma` and full model checks. It is distinct from the two main ROT003 null tests.

## 5. Actionable bounded falsifiers and STOP

1. Reconcile v3 *Appendix A two-sector prescription* (A.1/A.2/A.3) and earlier v2 source `rho_SM(T),N_s(T)` semantics in author's actual intended model. Do not silently assume two-sector EoS is a single equilibrium bath, and do not claim exact journal-build identity.
2. Under explicitly authorized original Julia no-PBH run only, log `T_gamma,a,rho_SM,g_s,g_rho,Tnu(T)` and source `n_B(T)`; independently check `Tnu*a`, `g_s*a^3*T_gamma^3`, `a^3*n_B`, and the interpolating inverse `from_rho_to_T`. The original Julia code does not currently contain a dynamic `Tnu` or `n_B` state; do not claim this was already numerically executed.
3. If asking about hadron effect, only compare matched forced trajectories and original source antibaryon collision denominators first, then assess full endogenous 10D recalculation. Additional potential Hubble dilution term is a separate controlled question; not a parameter patch or automatic new variant.
4. Source-author prior science and original calibration firstness: Badacz owns native Julia, REC11/AUD1 bounded referee, XH source E4 remains OPEN. Do not launch C1–C4 as if parser S1 were fixed, and do not propose automatic full 100×100 grid.
5. Explicit nonclaims: no novel physics, no actual `Yp`, no helium/BBN nuclear network, no `beta` bound, no BlackHawk/PYTHIA E4 upgrade, no reproduced published Fig5, no referee signature, no BW verified ingestion.

## 6. Reproducibility & custody

Source-locked Node.js companion:
`research/mech-s9/2026-11-12/mech_s9_rot003_neutrino_baryon_null.mjs`;
requires original `N_around_m_e.csv` with Git blob exactly `93f2494f...`; code rejects any other bytes and tests 2/4-node convergence, baryon/entropy factorization and baryon log derivative.

Source-free locally executed SymPy algebra test:
`rot003_symbolic_null_checks.py`, `PASS` after fixing a draft control formula before publication; exact identity `3*q_rho*(4+q_s)/[(3+q_s)(4+q_rho)]` PASS. This file is local companion, not source-native physical code.

`GITHUB_PENDING_BW_INGEST / PUBLIC_SOURCE_LOCKED_EXACT_ALGEBRA_AND_TABLE / NATIVE_JULIA_NOT_EXECUTED_BY_MECH_S9 / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
