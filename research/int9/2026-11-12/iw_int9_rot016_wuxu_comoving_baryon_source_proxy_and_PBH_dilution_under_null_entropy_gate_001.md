---
artifact_id: IW_INT9_ROT016_WUXU_COMOVING_BARYON_AND_PBH_DILUTION_NULL_ENTROPY_SOURCE_GATE_001_20261112
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_STATIC_NULL_TEMPERATURE_PROJECTION_AND_EXACT_CLASSICAL_CONSERVATION_IDENTITY / NO_JULIA_RUNTIME / NO_E4 / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# INT9 ROT016 — cross-front source bridge: no-PBH entropy EOS mismatch -> PBH dilution and constant-eta_B comoving baryon-proxy nonconservation

## Original sources and FIRSTNESS

Wu–Xu author manuscript https://arxiv.org/html/2509.05618v3 equation (2.7) has adiabatic `g_s(T_gamma) a^3 T_gamma^3=const`; authors FIRST. Historical source is the distinct pinned 2025 v2 author repository `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, NOT authenticated to final JCAP build. Original `arXiv-2509.05618/main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: line60 `n_PBH=n_PBH_ini*(a_ini/a)^3`, line64 `n_gamma=2 ζ3 T_SM^3/π²`, line65 `n_B=eta_B*n_gamma`, lines77–85 bath EOS evolution, and lines109–129 n_B factors in hadronic production/destruction. Original `tool_script-parameters.jl` blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5` line47 fixes `eta_B=6.1e-10`. Original `data/ext/N_around_m_e.csv` 1000 temperature rows `T_MeV,g_rho,g_s`, immutable Git blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`.

**Mech-S9 ROT002 FIRST** proved the no-PBH radiation background EOS vs Eq(2.7) entropy mismatch and SOURCE-table integrated comparison at T0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1b84dc3e2a234081d418676fbf3843d18ca1e366/research/mech-s9/2026-11-12/IW_MECH_S9_ROT002_WUXU_RHO_ENTROPY_EOS_NULL_COMPATIBILITY_SOURCE_FIRST_001_20261112.md
**Badacz REVIEW053 FIRST** source-native SBBN corrected helium observable calibration, `T1=0.099688851247MeV` vs frozen `T0=0.07818527068831994MeV`. **Mech-S8 ROT020 FIRST owner ACK** and binary 100×100 source JLD2. Mech-S9 is now **human-activated science OWNER successor** of Mech-S8. **INT9 ROT015/REC11 ROT020 FIRST static parser blocker**, **Badacz PREREG062 FIRST ACTUALLY attempted native Julia C1–C4** and all four cases failed S1 due nonempty '#' line at input parser BEFORE `magic()` / 10D ODE, confirmed by KN13 ROT016 owner-source/custody. New INT9 does NOT rerun Julia, fix owner driver or claim a science run.

## Strictly typed positive source algebra and a second no-go

Let `q_rho=d ln g_rho/dlnT` and `q_s=d ln g_s/dlnT`. Source no-PBH RHS `f_code=dlnrho/dlna=-4+q_rho/(3+q_s)`; source-declared adiabatic model `f_adiab=-3(4+q_rho)/(3+q_s)` (Mech-S9 owner FIRST). Since `rho∝g_rho T^4`, the temperature-to-scale inverse source nulls obey:
`dln a_code/dlnT=(4+q_rho)/f_code`,
`dln a_adiab/dlnT=-(3+q_s)/3`.
For two **separate** background histories with same `a` at source Tstart=1MeV, define `r(T)=a_code(T)/a_adiab(T)`. At same final source temperature, same PBH INITIAL number normalization, vanishing PBH background backreaction, original source `n_PBH∝a^-3` makes:
`n_PBH,code(T)/n_PBH,adiab(T)=r(T)^-3`.
**NEW INT9 typed link:** Mech-S9 entropy null mismatch -> exact conditional source dilution factor. This is NOT actual source hadron injection error: clock/M(t)/H(t)/backreaction differ.

**SECOND NEW INT9 gate:** The original author ALSO fixes eta_B and uses `n_B=eta_B n_gamma`, `n_gamma∝T^3`. Hence the literal original code's proxy baryon count in comoving volume obeys exactly:
`[a_code(T)^3 n_B(T)]/[a_code(1MeV)^3 n_B(1MeV)]=(g_s(1MeV)/g_s(T))*r(T)^3`.
Differential version:
`dln(a^3 n_B)/dln a=3 + 3 f_code/(4+q_rho) = 3 q_rho(4+q_s)/[(4+q_rho)(3+q_s)]`.
If n_B is intended as conserved physical net baryon NUMBER, this source law is not globally conserved during e+- annihilation with changing g(T). **Even if the background were replaced by adiabatic f_adiab**, keeping original constant eta_B would give `a_adiab^3 n_B ∝ 1/g_s(T)`, not conserved. A conserved net baryon-density physical interpretation requires a time-dependent eta_B(T) relative to photon number or separately evolved baryon number. Authors may intend a different approximation/late-time ratio; this must be source-clarified rather than silently called physical baryogenesis or fixed.

## Direct original source EOS table numbers

Actually read original 1000×3 author CSV with Git blob above and original interpolation rule (**g values linear in log T**, NOT log g values). For each original knot segment, independently evaluated source analytic q_rho,q_s. Independent 2-point and 4-point Gauss–Legendre per segment agree in Delta ln a by <=2.71e-13 for 1MeV→T0, 1MeV→T1; by 3.04e-14 for T1→T0. The Mech-S9 prior 1MeV→T0 source value is replicated (`r_T0=1.046638021704...`). New explicit calibrated T1 bridge and baryon-n_B proxy:

| temperature | ln r | r=a_code/a_adiab | source nPBH dilution r^-3 | (a_code^3 n_B)/(a_start^3 n_Bstart) | same constant-eta_B adiabatic comparator |
|---|---:|---:|---:|---:|---:|
|T1=.099688851247MeV|.03695982716379757|1.0376513346037353|.8950466121119712|2.472201797218124|2.2127358430572084|
|T0=.07818527068831994MeV|.04558314307928519|1.0466380217044857|.8721887437521585|2.8542233308289697|2.4894214613038206|
|T1→T0 only|.008623315915487597|1.0086606038088721|.974461812322962|1.1545268408269582|1.1250423176877418|

At the original T1/T0 source EOS q values, instantaneous `dln(a^3 n_B)/dlna` is respectively .5834652556/.3858964466, nonzero. These source-null quantities are **NOT observed physical baryon production, a valid numerical PBH beta shift, a time-of-evaporation correction, or a validated n↔p kernel**. The comparison normalizes histories at arbitrary common 1MeV, NOT at actual author's PBH formation epoch.

Original source/model physical transfer still fails before a corrected beta/Yp constraint: no validated BlackHawk/PYTHIA secondary spectra E4, no native 10D zero-PBH replay with QED temperature split and source ρ↔T inverse, no owner adjudication whether intended two-temperature nonadiabatic physics is compatible with the declared Eq(2.7), no native C1–C4 pilot results (S1 parser fail), no exact historical JCAP final build identity. Even a successful T1 SBBN scalar calibration does NOT check both original n_PBH dilution and original n_B baryon conservation.

## Repro and custody

Connected original 1000-row GitHub source read/integration was ACTUALLY performed in JS under the authenticated GitHub connector. Moderator-local standalone Python3 stdlib source script:
1) default **frozen-source-derived endpoint summary arithmetic replay**, with 1200 random double-precision algebra identity checks; does not falsely claim new offline 1000-row integration;
2) optional `--author-eos path/to/ORIGINAL/N_around_m_e.csv` checks exact original Git blob `93f249...`, loads all 1000 source rows, reproduces knotwise source 2/4-point Gauss and both endpoint ratios with tight checks. Original author CSV is **NOT bundled**. No Julia solver, no numerical physical BBN check, no source/owner modifications.

Moderator-local full report SHA256 `77b9339d557aa7c762935221a99aac141b884e73ecb7dd2a3a9ad54fd9fbf6b4`; five-member ZIP SHA256 `466501d1a1504b6224ca894e05762c936a5a58d15c396b0b6abaf85bd1fd57b5`, ZIP CRC and four payload SHA and clean isolated frozen JSON replay PASS. Public report DOES NOT include ZIP bytes; BW and owner/referee acceptance unverified.

**STATUS: SOURCE_NULL_BACKGROUND_TO_PBH_DILUTION_POSITIVE_CONDITIONAL_BRIDGE / SOURCE_BARYON_COMOVING_PROXY_NONCONSERVATION_MATHEMATICAL_CHECK / T1_T0_GENUINE_SOURCE_TABLE_2_VS_4_GAUSS_PASS / MECH_S9_FIRST_ENTROPY_NULL / BADACZ_NATIVE_C1_C4_S1_FAIL / PHYSICAL_E4_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN**.
