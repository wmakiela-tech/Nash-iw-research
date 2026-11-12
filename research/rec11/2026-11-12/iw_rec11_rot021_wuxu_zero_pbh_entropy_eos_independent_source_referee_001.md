---
artifact_id: IW_REC11_ROT021_WUXU_ZERO_PBH_ENTROPY_EOS_SOURCE_NATIVE_INDEPENDENT_REFEREE_001_20261112
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-12
exposure: PUBLIC
type: I1_NONBLIND_SOURCE_FIRST_EXACT_ALGEBRA_ORIGINAL_1000_ROW_NUMERICAL_RECHECK
source_first: IW_MECH_S9_ROT002_WUXU_RHO_ENTROPY_EOS_NULL_COMPATIBILITY_SOURCE_FIRST_001_20261112
source_commit: d395183674cace6c9906a8911bdeb7234ba4040d
claim_ceiling: CONDITIONAL_ZERO_PBH_BACKGROUND_COMPARISON / NO_AUTHOR_JULIA_NATIVE_REPLAY / NO_JCAP_BUILD_ID / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
owner_acceptance: UNVERIFIED
bw_receipt: UNVERIFIED
---

# REC11 ROT021 — Independent original Wu–Xu source referee: no-PBH entropy null and frozen density/temperature compatibility

## 0. Priority, direct source, and decision

**Mech-S9 ROT002 FIRST** identified the material difference between the original source code's `d_log_ρ_SM_dη` and the adiabatic entropy law quoted in Wu–Xu arXiv v3. REC11 independently confirms the exact source expression and source-table numerical effect, and supplies distinct exact-decimal all-knot derivative-sign and frozen inverse-interpolation controls. This is not discovery-first, physics novelty or a retroactive claim that the published JCAP build ran identical code.

**Direct author native GitHub read** of the ORIGINAL `Fenyutanchan/Primordial-Black-Hole` tree at immutable `d395183674cace6c9906a8911bdeb7234ba4040d` (not a copy in a downstream IW report), successful in this turn:
- `arXiv-2509.05618/main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, lines 77–85 and 145–210;
- `arXiv-2509.05618/tool_script-N_relativistic_species.jl`, Git blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`, original linear degree-of-freedom interpolation in `ln(T/MeV)` and 1000-point inverse density-to-temperature builder;
- `arXiv-2509.05618/data/ext/N_around_m_e.csv`, Git blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`, exactly 1000 source rows/3 columns, each source record read directly with the connected GitHub source interface.

Author text separately authenticated directly from the original HTML `https://arxiv.org/html/2509.05618v3`, §2.1 Eq. (2.7), and Appendix A Eq. (A.1–A.3): the authors explicitly distinguish photon and neutrino temperatures and state `g_(star,s)(T_gamma) a^3 T_gamma^3=constant` using entropy conservation in the adiabatic reference. This **later 2026 v3** text is not the immutable December 2025 v2-executable identity and cannot settle authors' intended multi-temperature source dynamics alone.

Mech-S9 source-first original scientific note: https://github.com/wmakiela-tech/Nash-iw-research/blob/1b84dc3e2a234081d418676fbf3843d18ca1e366/research/mech-s9/2026-11-12/IW_MECH_S9_ROT002_WUXU_RHO_ENTROPY_EOS_NULL_COMPATIBILITY_SOURCE_FIRST_001_20261112.md .

## 1. PASS — exact original source algebra (without any ODE execution)

Set `eta=ln a`, `q_rho=d ln g_rho/d ln T`, `q_s=d ln g_s/d ln T`. With PBH source absent (`n_PBH=0`) the literal frozen `main-scan.jl` line85 reduces to

    f_code = d ln rho/d eta = -4 + q_rho/(3+q_s).

By Eq. (2.7) of the paper, adiabatic comoving entropy `g_s a^3 T^3` yields `d lnT/d eta = -3/(3+q_s)`. Since original source defines `rho=(pi²/30)g_rho T^4`, under that same adiabatic law

    f_ad = -3(4+q_rho)/(3+q_s).

Exact algebra, independent of numerical derivatives:

    f_code - f_ad = 4(q_rho-q_s)/(3+q_s).
    (d ln (a^3 g_s T^3)/d eta)_code = 4(q_rho-q_s)/(4+q_rho).

The zero-PBH null is *only* compatible if `q_rho=q_s` at those temperatures (provided denominators are finite). The source simultaneously contains two distinct tabulated functions. This is a **conditional source-model compatibility fail**, not evidence of physical entropy production or proof the authors omitted another energy/temperature sector in their intended published model.

## 2. PASS — independent full 1000-row frozen input recheck

REC11 independently parsed the original CSV directly through the authenticated GitHub original source and independently implemented logarithmic source interpolation and its per-segment derivative. The original source has 999 knot intervals. For each adjacent source row, let `(r_i,s_i)` and `(r_(i+1),s_(i+1))` denote the printed g_rho and g_s values. On a segment linear in ln T, the EXACT sign of `q_rho-q_s` equals the sign of

    (r_(i+1)-r_i) s_i - (s_(i+1)-s_i) r_i.

REC11 used exact Rational BigInt integer arithmetic on the **decimal source tokens**, not IEEE754 subtraction for the sign classification:

    776 POSITIVE / 223 NEGATIVE / 0 EXACT ZERO across 999 source intervals.

This matters: the code-defined entropy proxy is **not strictly monotonically increasing pointwise on all source intervals**, so an unqualified monotonic-entropy claim would be false; the net integrated effect is positive. There is no nontrivial source-wide equality `q_rho=q_s`.

At T=0.100000 MeV: `q_rho=0.716535056148426`, `q_s=0.5988490653011828`, `f_code=-3.8008988309465375`, `f_ad=-3.931702861581697`. Thus source-resolved RHS differs by `+0.1308040306351595` in dlnrho/dlna at that T.

For source table T from 1 MeV to the historical author-code T0=0.07818527068831995 MeV, integrate `d ln a/d ln T = (4+q_rho)/f` using exact source knot breaks. INDEPENDENT Gauss–Legendre 3- and 5-node interior quadratures over all knot segments agree in the final relative log-scale delta at the `1.39e−17` level:

    Delta ln(a_code/a_ad) = +0.04558314307928519,
    a_code/a_ad = 1.0466380217044857,
    (S_code/S_initial) = exp(3 Delta ln a) = 1.1465408229163758.

These replicate the original Mech-S9 results, but the alternative code and quadrature implementation were not imported from the owner. These **do not follow from a real 10D Julia run**, and the last ratio is a modeled effective entropy-control diagnostic.

For a calibrated **illustrative** `T1=0.099689 MeV` based on Badacz REVIEW053's reported approximate native standard BBN control (the precisely frozen same-runtime T1 is not obtained here):

    Delta ln(a_code/a_ad)=0.03695976530214867,
    a_code/a_ad=1.0376512704129148,
    effective entropy ratio=1.1172600408546873.

Other independent source intervals:
- 1→0.5 MeV: scale ratio 1.0007941189167657;
- 1→0.2 MeV: 1.010949156033821;
- 1→0.1 MeV: 1.0375175647666655;
- 1→0.05 MeV: 1.0532065187463167.

As an explicit positive/negative control, synthetic `g_rho=g_s` yields ZERO exact decimal slope sign differences and zero mismatch/integrated model delta up to machine roundoff, matching the algebra. This synthetic control does **not** substitute for the original table replay.

## 3. NEW source-native inverse-table confound check

The authors' `tool_script-N_relativistic_species.jl` constructs `from_ρ_to_T` by interpolation at 1000 points of `log10T[GeV]∈[−5,+3]`, and source `rho(T)∝g_rho(T)T^4` (this is a SECOND approximation distinct from the original 1000-row g table). REC11 independently reconstructed the **static inversion map** using the authentic 1000-row original source interpolation.

At 555 original source temperatures in the interval [0.03,1] MeV:
- maximum absolute relative reconstructed inverse temperature error `1.24430967865e−5`, at T≈0.070005375 MeV;
- mean absolute relative error `3.27822250782e−6`.

These are *pointwise interpolation errors on a frozen source* only, NOT error bounds on the 10D ODE trajectory, dynamically measured T_nuc, strong branch monotonicity, all temperatures, or full physical contours. In particular, this source inverse-table interpolation alone does not numerically account for a 4.66% static difference in scale factor; a properly authorized native null replay would still be needed to assess its dynamical interactions.

## 4. Separate native execution and scientific stop conditions

**Currentness:** Badacz PREREG062 has since executed Mech-S8 ROT022 4-point smoke attempt in original Julia environment and confirmed four **input-parser** S1 failures `parse(Int,\"#\")` before any ODE for C1–C4. REC11 ROT020 and INT9 ROT015 first independently diagnosed that interface mistake; KN13 ROT016 independently checked input byte identity. There are still NO C1–C4 native scientific outputs from that prereg. This failure neither validates nor refutes the present source background null, which is independent of the C1–C4 parser.

**HOLD requirements:** (a) historical JCAP published Fig.5 and exact v2/v3 source-build identity; (b) whether the assumed same-bath entropy law is the intended null closure across electron/positron and neutrino decoupling; (c) complete zero-PBH source-native Julia and dense T/ρ/S diagnostics with frozen inverse interpolation, precision/tolerance and reference model; (d) actual corrected-calibration C1–C4 native pilots and E4 hadron source; (e) verified physical BBN/helium/PBH bound. None has been newly executed, authorized, certified or inferred from these finite-source calculations.

The source code's `a_end` uses `Nᵨ(T)` in a numerical integration horizon heuristic rather than an explicit physical entropy law; do not conflate this with an equation for the entire background. The direct source code uses `from_ρ_to_T` rather than a symbolic exact inverse, so the static equations are only an abstraction of its numerical tabulated map.

## 5. Reproducibility, proven execution scope, and disposition

REC11 directly **EXECUTED ON THE FULL ORIGINAL AUTHOR 1000-ROW CSV via connected source read**:
1. exact-decimal BigInt determinant sign test of 999 intervals;
2. independent per-knot interior Gaussian quadratures (3 vs 5 nodes) and source RHS values;
3. separate 1000-node log-density/log-temperature inverse construction and 555-point source-tied error survey.

REC11 also created and actually EXECUTED locally a separate **stdlib Python** source SHA-locked verifier `verify_rec11_rot021_wuxu_eos.py` on its own synthetic identical-g_ρ/g_s **control only**; it supports `--csv PATH_TO_ORIGINAL_1000_ROW_AUTHOR_CSV` and checks blob `93f2494f...`. Due to sandbox's disabled external DNS and lack of direct transfer from connected original GitHub source to filesystem, the original source CSV is **not included in the local ZIP** and the local Python `--csv` original-source replay is **NOT** claimed executed. Do not conflate the connected JavaScript source-run with the separate offline Python self-test.

The original author source can be retrieved unchanged (MIT licensed), at:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/ext/N_around_m_e.csv

The source script is offline-replayable when the user separately supplies that unchanged file. It fails closed if its original blob is not `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`.

**Verdict:** `PASS_INDEPENDENT_DIRECT_ORIGINAL_SOURCE_RECHECK`; `PASS_ZERO_PBH_CONDITIONAL_ENTROPY_NULL_MISMATCH`; `PASS_999_EXACT_DECIMAL_SEGMENT_SIGNS`; `PASS_INVERSE_INTERPOLATION_SURVEY`; `HOLD_AUTHOR_NATIVE_JULIA`; `HOLD_ADIABATIC_MODEL_SECTOR_SEMANTICS`; `NO_JCAP_ID_NO_PBH_BOUND`; `NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.

RETURN_ID: `IW_REC11_ROT021_WUXU_ZERO_PBH_ENTROPY_EOS_SOURCE_NATIVE_INDEPENDENT_REFEREE_001_20261112`.
