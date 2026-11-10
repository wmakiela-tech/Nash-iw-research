---
artifact_id: IW_MT14_ROT028_HEAVY_CLOCK_NATIVE_LIFETIME_SENSITIVITY_001_20261111
origin_cell: IW_MT_SUCCESSOR_13 / MT14
created_at: 2026-11-11
exposure: PUBLIC
claim_ceiling: SOURCE_NATIVE_RECORD_REVIEW / EXACT_MATURE_MASS_CLOCK / NO_NEW_JULIA / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT14 ROT028 — the native heavy-end clock is confirmed, and mass sensitivity needs a parameter-aware gate

SOURCE FIRST: Wu–Xu authors; Badacz REVIEW057 original Julia v2 native run, prereg056 ahead of execution (2026-11-11); Mech-S8 physics owner; MT14 ROT026 earlier reduced clock. Original frozen native data: `wmakiela-tech/Nash-iw-research@5b5521ed1f057d341c1a410193e9a923c8ca1f8e:research/badacz/2026-11-11/data/heavy_end_clock.csv`, Git blob `357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e`. All eight original source rows directly fetched. Local ZIP contains an explicitly TRANSCRIBED eight-row excerpt, not original Git bytes.

For the ORIGINAL author mass-only clock, `M(t)=M0*(1-t/tau)^(1/3)`. At fixed t,M0,
`d ln M/d ln tau = t/[3(tau-t)]`. This is an EXACT classical sensitivity, not a novel evaporation law. The independent reproduced native data:
- j98 beta 1e-30: tau_eff/tau−1=+0.180009%, amplification=21.85352, mass residual +3.78192%.
- j98 beta 10^-19.2: +0.247541%, amplification=21.79143, mass residual +5.11488%.
- j99 beta 1e-30: +0.064303%, amplification=3.15732, mass residual +0.20248%.
- j99 beta 10^-19.2: +0.296781%, amplification=3.15665, mass residual +0.92547%.

The EXACT finite relation `M_native/M_clock = ((1-t/tau_eff)/(1-t/tau))^(1/3)` was checked for all four positive-mass cases to absolute <5e-13. Distinguish a failed 2% mass-window test from a failure of tau∝M0³. Original prereg Badacz verdicts preserved unchanged: P1_CLOCK PASS, P2_MASS_WINDOW FAIL, P3_CLASSIFICATION PASS, P4_BETA_FEEDBACK_WINDOW FAIL. The native r2 post hoc tighter solver tolerance remains pending, and a 2% mass residual is not a statistical significance measure. At j97 source is evaporated by Tnuc; j98,99 not in tested betas. This confirms the conditional endpoint classification in MT14 ROT026, not a physical beta bound.

LOCAL full Polish report, source-excerpt, pure stdlib verifier, output JSON, README and SHA256SUMS: `MT14_ROT028_NASH_20261111.zip`, SHA256 `92e541f40f4e655c834c48021306e84a00135e84ef1d99a868dda1983c63faa6`. ZIP CRC PASS; five members SHA PASS; clean extracted replay byte-identical PASS; NO ORIGINAL JULIA rerun. Mech-S8 owner, REC11/AUD1 review, KN13 BW custody, Moderator EXEC. NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
