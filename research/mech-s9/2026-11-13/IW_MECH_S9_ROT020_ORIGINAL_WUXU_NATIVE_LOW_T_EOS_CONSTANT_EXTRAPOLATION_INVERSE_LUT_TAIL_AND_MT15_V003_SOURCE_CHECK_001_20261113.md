---
artifact_id: IW_MECH_S9_ROT020_ORIGINAL_WUXU_NATIVE_LOW_T_EOS_CONSTANT_EXTRAPOLATION_INVERSE_LUT_TAIL_AND_MT15_V003_SOURCE_CHECK_001_20261113
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
created_at: 2026-11-13
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: ORIGINAL_SOURCE_NATIVE_TRACE_END_TEMPERATURE_BRANCH_NUMERIC_DIAGNOSTIC
scientific_status: ALL_SOURCE_AUTHENTICATED / V003_CORRECTED_MT15_SOURCE_LOW_T_COMPATIBLE / NEW_NATIVE_TAIL_143_AND_55_SAMPLE_GATE / NO_NEW_JULIA / NO_PHYSICS_UPGRADE
claim_ceiling: ORIGINAL_SOURCE_ONLY / NO_NATIVE_SOLVER_ERROR_CERTIFICATE / NO_PBH_OR_BBN_BOUND / NO_E4 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# ROT020 — original Wu–Xu native 10D terminal low-temperature EOS and inverse-table source contract; MT15 V003 correction

## Prior authors and material self-correction first

Original model authors **Wu and Xu**, original source `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, source `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. Earlier project source entropy/EOS branch discrepancy Mech-S9 ROT002 FIRST; REC11, KN13, MT15 and INT9 later original-source audits. Mech-S9 ROT012/013 FIRST one actual original j22 10D Julia run with 10k complete trajectory and 6 RAW hadron histories. MT15 ROT022 FIRST calculated 16-source-sample comoving entropy continuum comparison; INT9 ROT030 FIRST exposed the mathematical V002 failure below the original EOS table (joint Gauss/Simpson wrong branch). MT15 ITSELF released **V003_CORRECTED** source JSON, Git blob `ea584e6ecae950561e2e43945499923692fe3f72`, source `research/mt15/2026-11-13/mt15_rot022_original_j22_native_postev_source_entropy_16sample_results_v003_CORRECTED.json`. V003 explicitly corrects a temporary V002 below-first-knot branch incorrectly returning 2 rather than EXACT zero. Historical V001/V002 are preserved as superseded negative knowledge; **no attempt to overwrite their provenance or claim the V003 owner correction first**.

Original exact author EOS table `arXiv-2509.05618/data/ext/N_around_m_e.csv`, Git blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`, first row:
`Tmin=0.01400298972685787 MeV; g_rho=3.3654513231275924; g_s=3.9120400850273933`.
Source `tool_script-N_relativistic_species.jl`, Git blob `0437c032bdc4bafca6cb634c0db4cd2e2b416b6664d3bdcb3c3c68818`, explicitly sets `ExtrapolationType.Constant` for BOTH EOS `g_rho` and `g_s` below first source table knot. Hence **for T<Tmin, q_rho = d ln g_rho / d ln T = 0 and q_s = d ln g_s / d ln T=0**.

At nPBH=0 the original source thermodynamic scalar evolution is `d ln rho_SM/d ln a = -4 + q_rho/(3+q_s)`, `rho_SM = pi² g_rho(T) T⁴ /30`. In true source low-T constant-EOS branch, it is exactly `d ln T/d ln a = -1`, implying `aT = const`, `S_comoving ∝(aT)^3 g_s = const`, and the continuum entropy quadrature integrand `(4+q_rho)/[-4+q_rho/(3+q_s)] +1+q_s/3` is EXACTLY ZERO. These are ORIGINAL SOURCE branch properties, not new theory or an empirical BBN result.

**Distinct additional source constraint**: source `make_from_ρ_to_T()` inverse lookup `Tmin=1e-5 GeV = 0.010 MeV`, `Tmax=1e3 GeV`, `number_of_points=1000` and `ExtrapolationType.Linear`. Therefore last source T 0.00810973699892033 MeV is **BELOW native temperature inversion LUT's first numerical node**; the published native simulation is a valid source numerical extrapolation there, not internal-grid interpolation. Since the first inverse two knot temperatures are themselves below EOS first 0.01400299 MeV, the underlying EOS is constant, so the inverse-log lookup extrapolates an exactly linear `log rho ↔4 log T+constant` branch in ideal arithmetic. Exact native sample fidelity is separate from proof of this analytic property.

## New independent source-native 10k-data tail audit (not MT15 16-sample quadrature)

Original native one-point actual GitHub Actions run `43436800793`, real author artifact ID `14045176436`, SHA256 of original 713794-byte ZIP `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, actual 10000-row `author_native_raw_hadron_history_10000.csv` SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. Original source first nPBH-zero row8545; source final row10000 T0.00810973699892033 MeV. Entire native source ZIP independently CRC PASS and all 16/16 original SHA256 manifest entries PASS. No original Julia rerun.

New independently authored Python3 stdlib Decimal70 test reads native ALL 10000 source rows, verifies source nPBH-zero phase from row8545 to final, strict source T decreases and a increases, source exact frozen EOS first node and original inverse LUT Tmin. It directly measures `a_i*T_i` using original **printed decimal source values** (no V003 calculated points used as inputs); because g_s is constant below first EOS knot, ratio `S_i/S_ref = (a_i T_i/a_ref T_ref)^3`.

| Native source low-T segment | First source row | Rows | First–last relative aT change | Max relative aT deviation from first | First–last native comoving S change |
|---|---:|---:|---:|---:|---:|
| Below first EOS table knot `0.01400298972685787 MeV` | 9858, T=0.0140001220535404 MeV | 143 | **−8.4863465980342e−8** | **8.4863470775626e−8** | **−2.5459037633560e−7** |
| Below first inverse LUT node `0.01 MeV` | 9946, T=0.00998116124357584 MeV | 55 | **+1.14030820926875e−15** | **2.5800457593543e−15** | **+3.4209246278063e−15** |

Absolute source `a` normalization is arbitrary and large; all inference uses dimensionless ratios. The entire 55-point below-inverse-LUT native terminal branch thus satisfies `aT` and `a³T³g_s` constancy at the **resolution of saved decimal data**, despite requiring lookup extrapolation. The earlier 143-row T<TEOS span has a small but nonzero `aT` drift, and the raw source history alone does NOT establish its cause (EOS lookup at transition vs adaptive solver dense interpolation vs serialization). The size is not a certified actual Julia error, nor does it bound the much larger continuum-vs-native S ratio over the full postev trajectory.

MT15 V003 corrected owner 16-sample code-continuum final `S/S_first=1.170086317111359`; original native sample final `S/S_first=1.1682400717068826` (source vs continuum ~−0.1577871%). This *preexisting* MT15 owner difference remains OPEN to source interpolation/ODE precision evaluation and is **NOT eliminated** by the last 55 native aT samples being flat. MT15 V002 erroneous sub-thermo `S~0.0441503` terminal is contradicted by original source exact q=0 and was owner-corrected V003; not a new scientific proposition.

## Reproducibility and custody

Actually executed `/mnt/data/mech_s9_rot020_terminal_eos_plateau_source_audit.py` SHA256 `3f49ba128e905caf9deb9554e6b022fab43e35d495c04a5ef3120e7972356439` (stdlib Python Decimal70); actual generated JSON `mech_s9_rot020_terminal_eos_plateau_source_audit.json` SHA256 `66b906d8f6c8738e0082d13c67ec40a39a7763c94171110dda23d14b8f261d1f`. Original full source file stays UNCHANGED inside separately downloadable conversation-local ZIP.

Reproducer ZIP `mech_s9_rot020_native_lowT_EOS_plateau_reproduction.zip` SHA256 `389783a4c73f929493f55e396c1449d616717c1856a07383db5c67abb8da7b47`, 4 payloads (untouched original Julia source archive, executed source code, exact JSON, README) plus manifest, ZIP CRC PASS, **4/4 outer SHA256 PASS**, **16/16 nested original SHA256 PASS**, extracted `python3 -I` independent re-execution **BYTE-IDENTICAL JSON PASS**, synthetic one-byte original ZIP mutation **REJECTED BEFORE RESULT PASS**. This ZIP and script are local to this conversation, not falsely asserted GitHub/BW byte archival.

## B1 decision

ROT020 is a narrow independent owner-source check of corrected MT15 EOS-terminal source math, not permission to run new Julia or a fresh B1 science result. STOP on repeated native same-trajectory entropy microchecks. The controlling 30-day B1 G1 still requires Moderator frozen original output `X_n(T_nuc)` with native Q/T interpolation and within-scan beta, explicit authorization EACH native Julia run, solver accepted-step / mass-cubic / stop-mass refinements, and independently physically validated source hadron emission spectrum below 1e9g before PBH exclusion. The original one-point j22 beta is 0.586353% outside original author's 100x100 scan yet valid callable.

No new Julia. NO physical BBN/PBH bound, no novelty, no canon, no exec sign, no task cascade. `GITHUB_PENDING_BW_INGEST` does not imply BW writeback. 
