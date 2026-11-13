---
artifact_id: IW_MT15_ROT020_WUXU_ORIGINAL_NATIVE_MASS_CUTOFF_FORWARD_INVARIANT_UNDERCUT_AND_TINY_NUMBER_TAIL_001_20261113
created_at: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: INDEPENDENT_ACTUAL_ORIGINAL_NATIVE_SOURCE_ODE_INVARIANT_FALSIFICATION_AND_SEPARATE_CONDITIONAL_RATE_COUNT_CALCULATION
status: ORIGINAL_AUTHOR_AND_NATIVE_HASH_PASS / MASS_CUTOFF_FORWARD_INVARIANT_RECORDED_NUMERIC_FAIL / SOURCE_NUMBER_TAIL_85_DIGIT_AND_INDEPENDENT_QUAD_PASS / CLEAN_OFFLINE_REPLAY_PASS
claim_ceiling: ORIGINAL_ONE_J22_JULIA_NUMERIC_STATE_DIAGNOSTIC / NOT_SOURCE_PHYSICS_OR_SCALAR_XN_ERROR_CERT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT020 — Actual original Wu–Xu j22 native mass state violates the exact code cutoff's forward invariant

## 0. Original source, ownership and earlier independent controls

ORIGINAL scientific authors: Wu and Xu, JCAP 02 (2026) 063; frozen original public code v2 repository Fenyutanchan/Primordial-Black-Hole at immutable commit d395183674cace6c9906a8911bdeb7234ba4040d. Original main-scan.jl Git blob SHA1 b368ba55d5a493f7bc185909730f7fe5691f10d6. In source lines 47, 80–85, 166–180, the evaporation switch is set to log_m_stop=max(log_m_initial-20,log_mPlanck); the PBH mass derivative switches to EXACT ZERO once log(m)<=log_m_stop. The original source solver is solve(ODEProblem,AutoTsit5(Rosenbrock23())) without a source-visible event callback projecting mass back to its cutoff.

FIRSTNESS retained: Mech-S9 ROT012/013 FIRST actually executed the one-point original author 10D Julia j22 source run; Mech-S9 ROT015 FIRST measured mass table-node crossing in native real time and source under-grid duration; Mech-S9 ROT016 FIRST independently source-computed six signed live hadron RHS areas. KN14 ROT002 FIRST independently established a DIFFERENT numeric instability test: the proposed high-T cubic mass-clock invariant from early C=1.4022124e27 g³/s to late C=1.3936516e27 g³/s has a -0.610519% ratio mismatch; this is not the mass cutoff invariant tested here. LT8 ROT018/019 FIRST clarified original journal-paper Eq4.5 subedge M^-1.3 versus original author CODE v2 loglog first-cell extrapolation ~M^-1.20. AUD2 ROT007 FIRST conditional postev exact raw-vs-floor restart negligible residual (not duplicated here); INT9 ROT025 FIRST source Q/T operator matching and MT15 ROT017–019 first/extended scalar conditional weak Duhamel. MT15 ROT020 does not take over owner physical execution or any of those priorities.

Original real SOURCE proof data (not synthetic): Mech-S9 original GitHub Actions run 43436800793 artifact 14045176436, original 713794-byte native 10D ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486; its original 10000×19 full source-history CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. Original ZIP CRC PASS and original 16/16 original inner SHA256 PASS, checked again by this turn. Separate original author 100×5 hadron NUMBER rate table arXiv-2509.05618/data/out/hadrons_from_PBH.dat Git blob SHA1 06d0883a27b108692720422294ba2baacd381a64, locally byte-verified. No new author Julia run requested or performed.

## 1. The forward-invariance theorem (mathematical, classical)

In the frozen Julia source let y=log(m_PBH)-log(m_stop). For y>0 the mass rate obeys y'=-(N_BH(T_BH)*mPl^4)/(H*m^3), strictly negative as long as the standard positive PBH number factor, Hawking source and H are positive. For y<=0 the source explicitly sets d_m/dt=0, hence y'=0. Thus for ANY exact continuous absolutely continuous source ODE trajectory beginning with y>0, the half-space y>=0 is positively invariant. Proof: a trajectory cannot enter the open region y<0, because on every connected segment inside that region y'=0 almost everywhere and therefore y is constant; by continuity it could not depart from the boundary y=0 into a negative value. This statement needs NO constant-K mass-clock approximation and does not depend on the uncertain hadron generator or neutron chemistry. It is ordinary scalar discontinuous event-model comparison mathematics, NOT a novel theorem.

For the original j22 source call:
- M_init=1,121,174,456.4709606 g, log10beta=-16.9974609375; beta is +0.586% above the author's historical 100×100 scan upper beta=1e-17 (source callable, NOT published scan node);
- the corresponding code M_stop=M_init*exp(-20)=2.3109127923407016 g, much larger than the actual Planck-mass fallback;
- the UNCHANGED real native CSV first-zero nPBH row one-based 8545 reports m_PBH=1.47268711730633 g, and all remaining 1456 postev saved rows carry the EXACT SAME decimal mass;
- the state therefore has m_frozen/M_stop=0.6372750725113513, undercut 36.27249274886487% or absolute gap 0.8382256750343716g, and y_frozen=-0.45055389164097376<0.

Therefore, the RECORDED NUMERIC ORIGINAL-JULIA MASS STATE fails the exact source ODE forward-invariant condition. This is a source-native numerical consistency FAIL, with directly observed negative witness, not merely an inference from the mass^3 approximate clock. It is CONSISTENT WITH a solver timestep/continuous-event overshoot followed by the original switch to derivative zero, but the precise adaptive step or interpolation fault is NOT established without source owner solver internal logs and a separately authorized refinement. We do not claim the code's mathematical exact ODE lacks a solution or that physics makes the PBH mass wrong by 36% of its initial value.

## 2. Last real source sample interval and negative causality guard

The last saved PBH-active source row one-based 8544: t=.334927351810113 sec, PBH mass=144891220.526512 g, Xn=.470970450717220. First saved zero-PBH 8545: t=.33751037021169 sec, PBH mass=1.47268711730633 g, Xn=.472697125696049. Thus:
- saved event bracket delta t=.002583018401577 sec, not an exact continuous event time;
- saved Xn increases by +.001726674978829 across the bracket (firstness Mech-S9/MT15 ROT018);
- mass shortfall relative to initial is only (2.310913-1.472687)/M_init=7.476317982419914e-10.

Those are different source scales: 36.27% **of the nominal few-gram stop mass**, but only ~7.5e-10 of initial mass; the 0.0017267 neutron change across an unresolved event sampling bracket cannot be attributed to this subcutoff mass state. There was genuine source production and a discontinuity in that bracket. No monotone postev Duhamel certificate can be propagated backward across it.

## 3. Independent source-model NUMBER-only tail calculation: small counts != bound on Xn

To prevent a false 36%-physics-error reading, perform an ADDITIONAL expressly HYPOTHETICAL calculation with the author's original FIVE positive source rate data and original CODE per-species loglog rate extrapolation. Assume a SIMPLIFIED constant-K evaporation clock dt ∝ M² dM. This is NOT the complete original live N_BH(M) Julia clock, which KN14 shows merits independent numeric control. Define the source mass-weighted NUMBER ratio for each source channel h:

deltaN_h/N_h = [integral from M_frozen to M_stop of M² R_h(M) dM] /
               [integral from M_stop to M_init of M² R_h(M) dM].

Below first source node 1e9g, R_h(M)=R_h(1e9g)*(M/1e9g)^(-p_h), where p_h computed from the ORIGINAL first two mass rows. Between original source rows, use the exact original piecewise loglog interpolator. The original start M_init overlaps the first TWO source cells. The integrals are elementary powers M^(3-p) and were computed by actual mpmath85 on the byte-locked original AUTHOR 100×5 table; a genuinely independent second scipy QUADPACK double-precision quadrature of all subsegments agreed to maximum relative deviation 2.3314683517128287e-14.

| Original hadron NUMBER channel | simplified deltaN/N |
|---|---:|
| pi | 1.3010839567206089e-16 |
| charged K | 1.2067036008419407e-16 |
| long neutral K | 1.2103467749872247e-16 |
| antiproton | 1.4020560180586672e-16 |
| antineutron | 1.4151022996992043e-16 |

These ratios are CONDITIONAL source-model particle NUMBER integrals, not measured physics, not the source original numerically integrated N_BH(M), not a calibrated below-table energy/particle source, and NOT a controlled neutron/nucleosynthesis response. They show that a large percent undercut of a few-gram terminal stop has an extremely small count fraction in this simplified mass clock. They DO NOT establish that the corresponding Xn, source Ycode or helium physical error is <1e-15 or insignificant. The last live-to-firstzero Xn jump is much larger and has distinct causal origins.

## 4. Actual independent reproducibility and failure controls

Executed original source-locked producer Python in isolated local runtime:
- original untouched provider/native nested ZIP and original 16-entry SHA256 manifest: PASS;
- original author 100×5 table git blob 06d0883: PASS;
- original 10000-row native CSV SHA256: PASS;
- direct mass cutoff and 1456/1456 identical postev frozen mass: PASS;
- real native mass-invariant violation: DETECTED as expected, status SCIENTIFIC_NUMERIC_FAIL_SOURCE_INVARIANT;
- five 85-digit rate-model power integrals versus independent SciPy quad: PASS all five;
- synthetic 1D constant-K exact-cutoff forward-invariant positive control: 1750/1750 PASS;
- one-byte original native ZIP mutation and original author rate-table mutation: BOTH REJECTED, as intended.

Actual locally executed standalone source: mt15_rot020_native_cutoff_undercut.py SHA256 a957a59204f8dd84e2194bcb145a3a44a0554bc4704c2c7e5c47eceb0a7b76e1; original full results JSON SHA256 5bebad555b0aa613ae83e59aa2213f0d015c006fee63b032d7ab78aaa1ebbee8. Full self-contained current-conversation ZIP mt15_rot020_original_wuxu_native_cutoff_invariant_audit_20261113.zip: 728274 bytes SHA256 60813ec2658d92427ff431f2ad66065e19a7badbacce687fa63049d07ce657b3. Contains UNCHANGED original native Mech-S9 ZIP (including original 10000 source samples), original 100×5 author rates, producer and verifier, actual full results, README and manifest of 5 original payloads. ZIP CRC PASS, 5/5 SHA256 payloads PASS; extracted into an EMPTY CLEAN temp directory, entire real-source producer and all 1750 synthetic controls reexecuted, result JSON BYTE-IDENTICAL, both tamper controls fail-closed. ZIP remains conversation-local, not falsely claimed to be uploaded to GitHub or BW.

## 5. Owner-relevant STOP and non-claims

A source-native mass cutoff threshold refinement should be considered together with KN14's independent separate approximate M^3 clock drift, but these are NOT the same defect. Mech-S9 + Badacz own actual original Julia solver, and the November 13–December 13 thirty-day B1 protocol requires Moderator approval PER new Julia execution. This ROT has NOT requested/started a new numerical Julia run, changed a source threshold, calibrated a new beta or frozen a B1 primary observable. If owner authorizes a future tolerance/event handling check, compare exact M_stop versus M_frozen together with original Q/T-matched Xn(T0), not a posthoc mass-only success.

The original mass-component exact mathematical invariant is violated by the current recorded numeric output; what that does to numerical precision of the whole 10D Xn or physical PBH/BBN remains UNKNOWN. In particular it does not undermine the separately conditional classical scalar intervals from MT15 ROT018/019, which start after first zero native row, but it reinforces their explicit SOLVER_ERROR_UNCERTIFIED caveat. It has no bearing on established external novelty, physical PBH exclusion, real BlackHawk/PYTHIA below-grid source calibration, or the historic paper Figure 5 production build.

FINAL: ORIGINAL_AUTHOR_10D_NATIVE_CUTOFF_INVARIANT_NUMERIC_FAIL / SOURCE_NUMBER_TAIL_MODEL_5x_PASS / CLEAN_SOURCE_REPLAY_PASS / OWNER_SOLVER_CONVERGENCE_HOLD / E4_SOURCE_HOLD / NO_PHYSICAL_PBH_OR_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
