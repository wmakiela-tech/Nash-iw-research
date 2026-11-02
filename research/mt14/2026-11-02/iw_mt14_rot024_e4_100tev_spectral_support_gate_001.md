---
artifact_id: IW_MT14_ROT024_E4_100TEV_SPECTRAL_SUPPORT_GATE_001_20261102
origin_cell: MT14
created_at: 2026-11-02
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_PHYSICAL_BOUND / NO_JULIA_RUN / NO_CANON / NO_EXEC_SIGN
---

# ROT024: original Wu-Xu E4 primary energy coverage and thermal benchmark

ORIGINAL Wu-Xu source pinned d395183674cace6c9906a8911bdeb7234ba4040d, notebook valid_hadrons_from_BlackHawk.ipynb Git blob 8a10396ae771b17059808fc2b91235dd194cba8d cell12: mass grid 1e9-4e12 g, 100 values; BlackHawk primary energy from 5 to 100000 GeV, 100 values. Input primary energy coverage ends at 100 TeV. Source code and first published physical claims remain Wu-Xu and BlackHawk authors.

Schwarzschild T=1.06e5GeV*(1e8g/M). Source grid upper energy equals Hawking temperature at Mcrit=1.06e8g. If PBH mass initially 1e9g evaporates fully to 0, the remaining rest-mass energy after Mcrit crossing is 10.6% initial mass-energy. This is NOT the amount radiated above 100TeV, and may not coincide with BBN sensitivity.

An EXPLICIT IDEALIZED thermal benchmark only, NOT a BlackHawk spectrum: energy shape u^3/(exp(u)+s) with s=+1 Fermi or -1 Bose. Instantaneous above-cut fraction F_inst=integral_x^inf shape / integral_0^inf shape. Complete evaporation proxy F_full=(1/x0)*integral_0^x0 F_inst(x)dx. Here x0=M0/1.06e8g.

Numerical source-support benchmark (NOT actual hadron physics):
- M0=1e9g: F_inst fermion 1.6453%, F_full fermion 43.2894%, boson 40.4170%.
- M0=1.121e9g: F_inst fermion 0.713%, F_full fermion 38.732%.
- M0=3.494e9g: F_full fermion 12.456%.
- M0=7.743e9g: F_full fermion 5.621%.
- M0=1e10g: F_full fermion 4.352%.
The large gap between initial tail and full history demands a source-valid TIME-RESOLVED E4 test. Proxy values are NOT a physical omitted-energy fraction, not source-valid Yp/DH or beta changes, and MUST NOT be combined with Badacz E5 contour shifts. Real E4 requires spin greybody, full primary and secondary spectra beyond 100TeV, correct BBN-stable hadronization, correct time window, calibrated original Julia10D and numerical stability.

Priority FIRST: original Wu-Xu and BlackHawk; Mech-S6/S7 source runs, Badacz original E4 and 2026-11-02 T1/T3, SCOPE9 root stability, DAX/PRF helium. This MT14 result is a conditional classic support calculation and admission criterion, not original physical science. REC11 active after REC10 technical failure; Mech/SCOPE threads technically affected. No owner role takeover.

Original public papers: https://doi.org/10.1088/1475-7516/2026/02/063 ; https://doi.org/10.1140/epjc/s10052-019-7161-1 .

REPRO local ZIP MT14_ROT024_E4_Original_WuXu_100TeV_Time_Integrated_Source_Support_20261102.zip sha256 0f98b3869cd0e56fea22758f9a5c2575b53aa67642acabc127e6bb988ba8e6e1. Python SciPy and independent mpmath 45-digit 36 comparisons max abs diff 3.26e-16, CRC PASS, payload 5/5 SHA PASS, clean extracted JSON regeneration byte identical PASS. No original Julia/BlackHawk run here; BW ingest unverified.

STATUS: ORIGINAL_PRIMARY_GRID_READ / IDEALIZED_SUPPORT_TEST_PASS / PHYSICAL_ADMISSION_HOLD / NO_CANON / NO_EXEC_SIGN.
