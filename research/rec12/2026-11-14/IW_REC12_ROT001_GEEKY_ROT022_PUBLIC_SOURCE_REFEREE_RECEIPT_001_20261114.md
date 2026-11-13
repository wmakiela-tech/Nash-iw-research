---
artifact_id: IW_REC12_ROT001_GEEKY_ROT022_PUBLIC_SOURCE_REFEREE_RECEIPT_001_20261114
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_11 / REC12
date: 2026-11-14
type: I1_NONBLIND_INDEPENDENT_M13_SOURCE_FORMULA_SYMBOLIC_IV65_REFEREE_RECEIPT
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_N41_B_FIVE_FIXED_MASK_AUXILIARY_WHOLE_FUNCTION_PERIODS_ONLY / NO_GLOBAL_INJECTIVITY / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN
---
# REC12 ROT001 — source-first I1 review of Geeky-S12 ROT022 (five energy period functions)

## Original and independent levels
- **M13 FIRST** original B Fourier/TT operator: `research/m13/2026-10-24/verify_m13_rot33_interval.py`, pinned commit `91be7247e878a15f3c60949010f9915f3cd7abcb`, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`. Independently READ in this review; source functions and formula transcribed, original source not imported/executed as a module.
- **Geeky-S12 ROT022 FIRST** alpha-zero symmetry enlargement and all-positive-alpha period theorem: `research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT022_M13_SOURCE_MASK_ENERGY_PERIOD_GROUP_ALPHA_ZERO_JUMP_AND_FULL_POSITIVE_INTERVAL_001_20261113.md`, commit `1e2b34237326647ff368a218543446e2acc85168`, blob `77fb1d2b7d2176eff8e7ceb0661b0f645dacc0db`. Independently READ.
- **M15 ROT013** and **REC11 ROT036** previously covered the different FULL TENSOR stabilizer at alpha=.05; **M15 ROT014** separately certified the common observed five-energy period group at alpha=.05. Preserve their firstness and scopes. This REC12 check independently addresses Geeky's additional alpha=0 and continuum 0<alpha<=.2 claims.

## Exact object, claim and possible falsifiers
Fix original M13 N41 B field, centered Fourier stencil, original TT and original five spatially FIXED masks. The common rigid translation of C1,C2,h is explicitly hypothetical. Let `S_i(alpha,t)` be the five disjoint masked energies. Review ONLY
`G_alpha = {u in T^3: S_i(alpha,t+u)=S_i(alpha,t) for EVERY t and EVERY i}`.
This is NOT the set of pointwise observation collisions, NOT global inverse identifiability, and NOT the period group of only gain-free four ratios.

Discriminator: an incorrect B source algebra, masked window, source Fourier support, positive coefficient sign, or integer lattice determinant invalidates the relevant theorem. A changed observation class means a new claim, not a post-hoc rescue.

## Actual independent source-formula computations
REC12 wrote and **executed** two independent Python programs. No import/copy of Geeky/M15 or the original M13 module; this is I1 NONBLIND formula-based, NOT external I3.

**A. Symbolic (SymPy).** Algebraically independent centered-derivative symbols in the original B bracket/Lie/TT expressions at alpha=0. Exactly 41 candidate labels, **8 nonzero tensor modes** precisely `(±2,±1,±1)`, whose components are rational multiples of `d1(2d1-d2)`; N41 implies `d1>0, 2d1-d2>0`. Full tensor-support integer lattice index **8**; pair-difference energy lattice EXACTLY `4Z×2Z×2Z`, index **16** (integer HNF).

**B. Independent outward-interval computation (mpmath.iv 65 dps).** Reconstructed original B polynomial `B_m(alpha)=U_m+alpha V_m+alpha^2 W_m`. The fifth shell energy is the original innermost cube k=6. Its spatial Fourier window was recalculated by the direct normalized interior sum rather than the original complement formula. Three alpha-zero energy difference coefficients have **strictly positive real parts**, approximately:
- d=(4,0,0): 3.8728432378766403e-16;
- d=(0,2,0): 1.6470012437049619e-15;
- d=(0,0,2): 1.6470012437049619e-15.
These nonzero frequencies have determinant +16, proving the energy support really generates all of `4Z×2Z×2Z`. Thus **exactly 16** whole-function periods at alpha=0:
`G_0={(a*pi/2,b*pi,c*pi) modulo 2pi: a mod4,b mod2,c mod2}`.

For positive alpha, choose difference frequencies
`(-2,0,0), (-1,1,-2), (-3,0,1)`
with exact integer determinant **-2**. Their `c_d(0)=0` EXACTLY from the preceding symbolic 8-mode support (not from numerically near-zero intervals). For each, `c_d(alpha)=alpha q_d(alpha)`, with q a cubic. ALL **12/12** outward 65dps Bernstein lower endpoints of `Re(q_d)` over the FULL continuum alpha in [0,.2] are strictly positive. Conservatively rounded minimum lower bounds by frequency: `6.46822e-14`, `3.86920e-17`, `2.85748e-16`. Hence all three energy coefficients remain nonzero for EVERY real alpha>0 up to .2. They generate the even-coordinate-sum lattice of index 2, and all original B modes have even parity. Consequently **exactly two** common periods:
`G_alpha={0,(pi,pi,pi)}` modulo 2pi for `0<alpha<=.2`.

**Countercontrol:** u=(pi/2,0,0) is an exact additional period at alpha=0 but its pairing with d=(-2,0,0) gives phase -1 when alpha>0. Thus it is NOT a positive-alpha whole-function period. No pointwise-in-t separation assertion follows.

## Reproducibility, evidence, limits
Both separately written scripts and both full JSON files (including full mpmath.iv 65dps endpoint strings, not just rounded displays) plus the detailed Polish report are in a complete user-conversation local ZIP, SHA256 **8271a71be7a21ee9815cf6013629f485c672835bc179a528d5b679538f94cffc**. ZIP CRC and 5/5 SHA manifest PASS. Both scripts executed in a distinct clean filesystem directory; output JSON files byte-identical **2/2 PASS**. Original source not bundled or tamper-checked automatically; original Git blob read is direct and independently pinned. The ZIP is LOCAL, not claimed GitHub-hosted or BW-ingested. Exact replay source files and full directed endpoints are not falsely represented as GitHub uploads.

**VERDICT:** `PASS_WITH_GUARDS / I1_NONBLIND_SOURCE_FORMULA / EXACT_8_OF_41_ALPHA0 / G0_ORDER16 / 3_ALPHA0_NONZERO_MASK_GATES / 12_UNIFORM_BERNSTEIN_POSITIVE / G_ALPHA_POSITIVE_ORDER2`.

**HOLD:** historical frozen DTC0a byte identity; global pointwise or projective observability; physically realizable source translations, sensor measurement, physical K/J3/GR/TPE claims; mathematical novelty, external I3. Original M13/Geeky/M15 firstness preserved. No owner adoption, BW scientific acceptance, CANON, EXEC_SIGN or automatic audit cascade claimed. No source mutation. A later source correction or concrete falsifying mask-frequency counterexample can reopen this review; otherwise STOP.

RETURN_ID: `IW_REC12_ROT001_GEEKY_ROT022_MASK_ENERGY_PERIOD_GROUP_I1_REFEREE_001_20261114`
