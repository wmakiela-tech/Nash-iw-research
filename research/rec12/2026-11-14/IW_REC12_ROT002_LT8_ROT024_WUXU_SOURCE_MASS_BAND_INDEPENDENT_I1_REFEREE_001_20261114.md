---
artifact_id: IW_REC12_ROT002_LT8_ROT024_WUXU_SOURCE_MASS_BAND_INDEPENDENT_I1_REFEREE_001_20261114
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_11 / REC12
date: 2026-11-14
exposure: PUBLIC
type: I1_NONBLIND_INDEPENDENT_SOURCE_FIRST_ANALYTIC_MP75_AND_QUADPACK_REFEREE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: WUXU_ORIGINAL_CODE_VS_PAPER_SOURCE_EMITTED_HADRON_NUMBER_MASS_PARTITION_ONLY / NO_NATIVE_JULIA / NO_PHYSICAL_ERROR_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# REC12 ROT002 — independent I1 referee of LT8 ROT024 Wu–Xu mass-band count decomposition

## Original sources and firstness
Original Wu–Xu paper: *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP02(2026)063, DOI 10.1088/1475-7516/2026/02/063, Eq.(4.5) source approximation dN/dt proportional to T_BH^1.3. ORIGINAL author code at commit `d395183674cace6c9906a8911bdeb7234ba4040d`, table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`, interpolator `tool_script-hadrons_from_PBH.jl` blob `cc73432910f872d526113ce59b6204f38d0766a9`, both DIRECTLY READ. First three authentic source table rows plus header, 496 bytes, SHA256 `33b15570425160ded569bc614d49e85c2ab681527763771f8381ffc45378b476`; exact fixture retained for reproduction. Original LT8 ROT024 FIRST five-channel paper-versus-code mass-band result: private Nash-Priv commit `1f81004f1eb175f0b5f35544dc11042e976f8d00`, blob `d5af0945ba20914b1fdf367fc32588463a5e8ce3`. PRF13 ROT017 FIRST earlier below-first-table ~81% exposure. These scientific ownership/priority roles are NOT reassigned.

## Frozen claim
One source j22 PBH mass interval `Mstart=1.12117445647096e9 g` through `Mstart exp(-20)`. First table mass `M0=1e9 g`; upper interval extends across first two original mass cells. Source high-temperature approximation `dM/dt=-K/M²` (K constant), so per-hadron emitted **NUMBER**, NOT energy/neutron response, is proportional to integral `R_h(M) M² dM`. At M<M0 the actual code extrapolates with exponent `p_h=-ln(R1/R0)/ln(M1/M0)` ~1.19665–1.20476; paper's Eq.(4.5) exponent translated using `T_BH ∝ 1/M` gives `p=1.3`. To compare source shape only, both are calibrated to the same R(M0), and above M0 use the SAME original interpolated source code rates.

Independent analytic primitive for a rate segment `R(M)=Rref*(M/Mref)^(-p)`:
`I_p(a,b)=Rref*Mref^p*(b^(3-p)-a^(3-p))/(3-p)`, omitting common K.
The difference paper minus code below M0 has strictly positive pointwise integrand proportional to `r^0.7-r^(2-p_h)` for r=M/M0 in (0,1). Exact positive partition `Delta=Delta_[M0/10,M0]+Delta_[Mend,M0/10]`. The 91% ratio is the FIRST band's share **of this particular code-vs-paper emitted-count difference**, not a generic physical uncertainty share.

## Source-independent calculations actually executed
New, separately written source-locked program 1 integrates all exact power-law cells with `mpmath` 75 decimal digits. New independent program 2 evaluates the same integrals with `scipy.integrate.quad` directly in log-M, not calling program1 or its analytic primitive. Both physically original first-three-row input bytes SHA locked BEFORE computations. Independent numerical totals agree better than 3e-9 percentage points for each of the 15 percentage values below. Per-species partition identities PASS.

| Original table channel | code # below 1e9g (%) | code # below 1e8g (%) | paper # below 1e9g (%) | paper # below 1e8g (%) | proportion of (paper−code) difference in [1e8,1e9]g (%) |
|---|---:|---:|---:|---:|---:|
| charged pion | 81.400351 | 1.291552 | 82.246315 | 1.641030 | 91.024710 |
| charged kaon | 81.364648 | 1.279638 | 82.242986 | 1.640963 | 91.054262 |
| K0L | 81.366070 | 1.280113 | 82.243113 | 1.640966 | 91.053082 |
| proton (literal source header) | 81.435811 | 1.303487 | 82.249624 | 1.641096 | 90.995209 |
| neutron (literal source header) | 81.440202 | 1.304974 | 82.250030 | 1.641104 | 90.991542 |

The author table literally labels last channels **proton** and **neutron**, not free claims of separate antiproton/neutron physics. Original source RHS particle/antiparticle semantics would require a different review.

## Explicit scope falsifier: why this is not a generator-error bound
Construct a strictly positive alternative hypothetical hadron emission rate `Ralt(M)=Rcode(M)*(1+0.1 b(M/M0))`, with `b(r)=(1-(10r)^2)^2` if 0<r<0.1 and `b(r)=0` if r>=0.1. This continuous model matches ALL original tabulated node rates exactly and differs only at masses **below 1e8g**; thus all its emitted-number difference from code is below 1e8g and NONE in the 1e8–1e9 band. This is an exact math counterexample to ANY universal promotion of LT8's 91% pairwise source shape result to arbitrary below-grid hadronization uncertainty. Not asserted as a physical alternate generator.

Moreover the published BlackHawk/PYTHIA maximum *initial emitted parton energy* is NOT a sharp T_Hawking or BH-mass boundary. The Hawking spectrum has energies higher/lower than the temperature scale. These source-number fractions cannot determine physical E_parton>100TeV shares, net signed neutron RHS, Xn(T0), Ycode, Yp or PBH bound. Full source generator calibration, original Julia 10D dynamic rerun, native convergence, independent physical error budget remain HOLD.

## Reproducibility and decision
Two script outputs and full 75dps machine JSON, original byte-exact first-three-row TSV, report, README and eight-entry SHA manifest preserved in USER conversation LOCAL standalone ZIP `IW_REC12_ROT002_LT8_ROT024_WUXU_SOURCE_BAND_I1_REPRO_001_20261114.zip`, **12,833 bytes, SHA256 `8f0c66380fec35136be0db8fd85a9f0b3f3d91ad70187816a1a3b27992c8f118`**. ZIP CRC PASS, manifest 8/8 PASS; clean extracted isolated re-execution analytic/QUAD/JSON byte-identical 3/3 PASS; deliberate 2 source mutations (1 digit and missing last row), each on BOTH validators =4/4 FAIL-CLOSED. ZIP is LOCAL, not pretended public GitHub byte mirror or BW-ingested. Full original 100-row upstream text read via GitHub, but only necessary exact three rows bundled. Original Julia 10D and physical generator NOT executed.

**Review level** I1 NONBLIND (not external I3), source pair claim PASS, universal physical uncertainty localization FAIL, B1_PHYSICAL_SOURCE_NUMERIC HOLD. Source model/Wu-Xu, PRF13 and LT8 firstness preserved. Reopen if input source/history or original Eq.(4.5) target or original K(M) source class materially changes, or a concrete counterexample to the definite mass-band arithmetic is supplied. No owner ACK, verified BW ING, CANON or EXEC SIGN; NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE.

RETURN_ID: `IW_REC12_ROT002_LT8_ROT024_WUXU_SOURCE_MASS_BAND_INDEPENDENT_REFEREE_001_20261114`
FINAL: `PASS_5_CHANNEL_LT8_ROT024_PAIRWISE_SOURCE_91PERCENT / PASS_INDEPENDENT_75DPS_ANALYTIC_AND_SCIPY_QUAD / PASS_FOUR_FAIL_CLOSED / FAIL_UNIVERSAL_HADRONIZATION_ERROR_LOCALIZATION / HOLD_B1_PHYSICAL_SOURCE_NUMERIC / NO_CANON / NO_EXEC_SIGN`.
