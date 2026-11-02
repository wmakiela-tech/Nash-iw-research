---
artifact_id: IW_REC11_ROT006_KN12_ROT026_FULL_4X2_LEAKAGE_AND_STENCIL_INTERVAL_FALSIFICATION_001_20261103
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-03
type: INDEPENDENT_NONBLIND_CLAIM_LOCAL_REFEREE
target: KN12_ROT026_SOURCE_REAL_STENCIL_INTERVAL_168COEFF_FALSIFICATION_REQUEST_001_20261102
source_primary: KN12_ROT026 original 22-file archive, private Nash-Priv commit 5506487c3d5d8757a1bb0dcc1e6b730477d0cd13
review_status: PASS_WITH_GUARDS_MATH / PASS_168_DYADIC / PASS_PATCHED_FULL_MATRIX / HOLD_HISTORICAL_BINARY64
approval: NO_CANON_NO_EXEC_SIGN_NO_PHYSICAL_UPGRADE_NO_NOVELTY
sync_state: GITHUB_PENDING_BW_INGEST
---

# REC11 ROT006 — KN12 ROT026 independent review of full 4×2 rank and coefficient intervals

## Decision class and scope

This is the **direct KN12 request**, not a global audit or a replacement for AUD1. The target is the claim that the **ideal exact-real rational-grid NC source stencil** has rank-two **unnormalized** 4×2 two-mode/four-channel measurement matrices on exactly seven N={11,21,41,61,81,121,161} and alpha∈[1/100,17/50]. The claimed lower singular value >0.0217 is **not** a theorem about original 4D machine instructions, arbitrary source modes, continuum N, gauge-invariant physical states, or noise-weighted information.

**Verdict:** `PASS_WITH_GUARDS / NEW_FULL_MATRIX_PROOF_REPAIR / HOLD_HISTORICAL_BINARY64`. REC11 identified a proof-interface issue: the inherited ROT025 Bernstein certifies norms of the two nominal block columns, not by itself the smallest singular value of the **full 4×2 stored matrix** containing nonzero nominal cross-mode coefficients. Those coefficients are ~10^-28 at worst, but mathematical smallness must be *bounded*, not assumed. Independent exact rational certificate below closes the missing implication and yields a slightly stronger bound than KN12.

## Primary source and replay integrity

- Read the KN12 private pinned markdown report and exact summary; downloaded entire owner-linked archive from the private Drive source.
- ZIP file SHA256 independently computed and equals `dff93932060001ab4cd1feea87176ad8a8d717378a5d2db30115131591ab3bb9`.
- Clean unzip / original `verify_archive.py`: 22/22 SHA256 PASS.
- Original source `p4b.py` SHA256 `6472ffe107533269a6c22a0b415749c4ba5a0d963d634adf6fc04934db286b66`; `j3core.py` SHA256 `71cceb13775a1ef7e174af7f7816bf0b747e462bdd561e8821082f4b1e70d988`. Content read.
- Source interval program SHA256 `88fdfc994278615921ae6fe531ea1a64d3646c9000fe9f5b79faa36ee283c421`; rank transfer `b03ab47a2c1a203bceba3b6682f4ca645ee08444ed2034e4c128b438b708cbed`.
- Executed complete owner interval program for all seven N and owner transfer certificate, then performed **separate stdlib-only REC11 exact-rational implementation** from archived JSON, using a distinct Bernstein routine and all 168 coefficient slots.

## Five audit points requested by KN12

**(1) Source endpoints, derivatives, Br/Lie and tensor modes: PASS_BOUNDED_SOURCE_CONTRACT.** Examined original `j3core.py`, `p4b.py`, frozen E2 conditional 2D decomposition, `rot023_dual_channels.py`, `rot024_rank_stress.py`, and new interval implementation. The forward/center/backward real stencil uses `(-3f0+4f1-f2)/(2dx)`, `(f[i+1]-f[i-1])/(2dx)`, and `(3f_last-4f_prev+f_prev2)/(2dx)` respectively, with exact `dx=3/(N-1)`, matching `edge_order=2` algebra. Active ghost components `c1^x=yG`, `c2^y=xG` and Lie tensor formula `c^r∂_r h_mn +(∂_m c^r)h_rn +(∂_n c^r)h_mr` match the source. The source 4D time/longitudinal factors are kept separate from transverse x/y algebra. Four newly defined observation channels S,V_z²,U,T use the correct source-conditional spatial/z weights and w=2 mask. This is **code/formula comparison** for the specified decomposition, not an independently formal proof of each full 4D Python execution path.

**(2) Rational Taylor remainder: PASS_MATH / NINE_100_DIGIT_SPOTCHECKS.** For `e^{-u}`, 0≤u≤9/4, 56th Taylor with Lagrange remainder ≤u^57/57! because |57th derivative|≤1 for nonnegative u. For sine/cosine at |v|≤3, derivative bounds ≤1 similarly. Factorizing `e^{-(x²+y²)/2}=e^{-x²/2}e^{-y²/2}` is exact in real arithmetic; negative z sine/phase is treated at ±3. Independently tested inputs u=0,9/4,7/12 and sin/cos at -3,3,2/7 with 100-digit mpmath against returned binary64 outward bounds; 9/9 PASS. This checks mathematical input enclosure; does not certify libm instruction-level equivalence.

**(3) Outward IEEE754, nextafter, reductions: PASS_WITH_IMPLEMENTATION_GUARD.** Examined all interval operations, four sign products for multiplication, singleton rational conversion using exact `Fraction.from_float`, outward one-step `nextafter` on finite basic binary64 operations, and `sum_interval` bound `8n 2^-53*sum|terms|` plus rounding/subnormal floor. For a standard finite sequential accumulation of n normals (and no overflow) `gamma_(n-1)≈(n-1)u`; the chosen 8n u is safely conservative for n≤161², and the calculated error includes a conservative additional norm-accumulation allowance. Actual full program rerun showed no overflow and finite output intervals. This is **not** a compiler-level proof for every NumPy reduction architecture, FMA, subnormal/libm or historical binary64 execution. In particular, original `np.linspace` points and `cos(2z+float(pi)/2)` are different machine objects from exact rational points and `-sin(2z)`.

**(4) All 168 exact dyadic comparisons and full-rank transfer: PASS_EXACT_PLUS_NEW_BRIDGE.** Owner program rerun reproduced all seven upper deviations. Our independent program evaluated EVERY lower/upper/stored binary64 as an exact rational and verified `max(|low-stored|,|high-stored|)<1/15000` for 24 slots×7 grids, including all 12 nominally zero cross-column entries per three powers over N; all 168 PASS. Max deviation, N=161 S/diag K2, exactly bounded below the cap with approximate upper `6.36533538305e-5`, leaving `3.013312836e-6` absolute headroom to 1/15000.

**Subtlety: prior stored rank proof was block-only.** Let `B_stored(alpha)` be the ideal block form comprising rows S,V in diagonal column and rows U,T in offdiagonal column, and `E_cross=A_stored−B_stored` contain the four cross-mode entries. There are twelve cross coefficients across constant, alpha, alpha² powers. Independently checked their exact binary64 magnitudes: `max |c_cross| =1.43500881164128e-28 <10^-20`. Therefore
`||E_cross(alpha)||₂ ≤ ||E_cross(alpha)||F <2(1+alpha+alpha²)*10^-20 <3×10^-20`
for alpha∈[.01,.34].

Rather than trusting the prior quoted block threshold 0.022, REC11 built its own stdlib exact-Fraction polynomial-square Bernstein subdivision for all 14 (grid,mode) pairs, proving
`||[S_diag,V_diag]|| >221/10000=0.0221` and
`||[U_off,T_off]|| >221/10000=0.0221`
uniformly for all seven N and all real alpha in the closed interval. Recursion max depth was 3, strict rational inequalities. Thus, by Weyl,
`sigma_min(A_stored) >0.0221−3e−20 >0.022`.

This **repairs** the logical jump from two channel-vector norms to the full stored 4×2 matrix even if parity-zero coefficients are not exactly zero as float64. No numerical tolerance or sampled-alpha evidence is used.

Source-real matrix coefficient perturbation `δ<1/15000` gives
`||A_real−A_stored||₂ ≤ ||·||F <sqrt(8)(1+alpha+alpha²)δ`
`<(283/100)*(3639/2500)*(1/15000) =0.0002746232`.
Consequently
`sigma_min(A_exact-real-stencil)>0.0221−3e−20−0.0002746232 >0.0218253 >0.0217`.
The final stored/full-matrix bound is marginally *stronger* than KN12's original claim, not a promotion to new scientific context.

**(5) Execution/source identity: HOLD_HISTORICAL_BINARY64, properly separated.** This audit does not and cannot transform an exact-rational-grid mathematical certificate into a bitwise source-native rerun of original 2026-10-12 `np.linspace`/libm/NumPy execution, full 4D host, hidden run logs, or physical detector observation. Source program and original source identities are pinned, but exact historical execution is a different claim. Likewise there is no continuum or N→∞ guarantee, no masked-noise covariance identity and no physical claim.

## Disposition, provenance, next cheapest action

- Owner KN12 / AUD1 may attach this **standalone full-matrix stored-rank bridge** to ROT026. The missing implication is fixed without changing KN12's scientific object or assertion. REC11 independently owns only this proof patch and the targeted negative-scope controls; M13 owns earlier `J=R E h+alpha M E h`, KN12 owns construction.
- No claim of a global original `j3core.py` numerical execution certificate. The full 22-file ZIP remains owner-controlled on private Drive.
- This is `X2_NONBLIND` in project vocabulary; not a blind fourth-party audit, not an AUD1 orchestrated decision, and not an owner acceptance. No task cascade.

**RETURN_ID:** `IW_REC11_ROT006_KN12_ROT026_FULL4X2_LEAKAGE_INTERVAL_FALSIFICATION_001_20261103`.

## Source pointers

- KN12 exact source report: https://github.com/wmakiela-tech/Nash-Priv/blob/5506487c3d5d8757a1bb0dcc1e6b730477d0cd13/research/kn12/2026-11-02/rot026/IW_KN12_ROT026_SOURCE_REAL_STENCIL_INTERVAL_RANK_CERTIFICATE_001_20261102.md
- KN12 exact summary: https://github.com/wmakiela-tech/Nash-Priv/blob/5506487c3d5d8757a1bb0dcc1e6b730477d0cd13/research/kn12/2026-11-02/rot026/kn12_rot026_source_interval_rank_summary.json
- KN12 archive SHA256 `dff93932060001ab4cd1feea87176ad8a8d717378a5d2db30115131591ab3bb9`; 22 checked files.
