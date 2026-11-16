artifact_id: IW_XH_S6_ROT023_PRE_DATA_FOURIER_SIGN_CONVENTION_CORRECTION_001_20261116
date: 2026-11-16
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: BEFORE_ANY_ROT023_HARMONIC_NUMERICAL_DATA
claim_ceiling: PURE_SIGN_OF_FOURIER_DIFFERENTIATION_CORRECTION / NO_SCIENCE_CRITERIA_CHANGED / NO_NASH_BRIDGE

# ROT023 pre-data correction: potential-to-torque Fourier sign

Original frozen science prereg GitHub commit 8bc7708f1f380aa726dba1f900c6500edbbd5be1 defines a signed torque tau=dV/dpsi, hence for potential harmonic V=a16*cos(16psi)+... and torque tau=b16*sin(16psi)+..., the mathematically correct exact relation is b16=-16*a16 (NOT +16*a16). The prereg wording loosely states the positive sign. This annex corrects ONLY that algebraic sign, BEFORE any ROT023 numerical harmonic results were computed; all original hypothetical geometry R={1,2,3}mm, invented gaps, 16 source masses, 7.6mg each, lambda grid, negative controls and no-experimental-bridge unchanged. Verify signed b_tau=-16*a_potential for both pure Newton and alpha-unit Yukawa and tau=dV/dpsi by finite difference. The ratio bY/bN is independent of this overall sign.

This is an XH documentation sign correction, NOT a claim about the original scientific authors or their actual apparatus. BW GITHUB_PENDING_BW_INGEST, NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NASH_BRIDGE.
