---
artifact_id: IW_MT15_ROT022_WUXU_REAL_J22_NATIVE_POSTEV_COMOVING_ENTROPY_SOURCE_EOS_TRAJECTORY_AND_ADIABATIC_COUNTERCONTROL_001_20261113
created_at: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: ORIGINAL_1000ROW_AUTHOR_THERMO_AND_ACTUAL_UNCHANGED_NATIVE_10D_TWO_SOURCE_DIAGNOSTIC
status: ORIGINAL_J22_NATIVE_SOURCE_HASH_PASS / ORIGINAL_AUTHOR_THERMO_1000ROW_HASH_PASS / SOURCE_ODE_GAUSS8_ONE_SIDED_SIMPSON64_PASS / 16_NATIVE_SELECTED_POSTEV_S_POINTS_PASS / 123_LATE_A_T_NEGATIVE_CONTROL_PASS / CLEAN_LIMITED_OFFLINE_REPLAY_PASS
claim_ceiling: SOURCE_AUTHOR_V2_MODEL_INTERNAL_DIAGNOSTIC / NOT_SOLVER_CONVERGENCE_CERT / NOT_COMPLETE_OFFLINE_AUTHOR_1000ROW_REPLAY / NOT_Yp_PBH_BBN_PHYSICAL / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT022 — Original Wu–Xu 10D postevaporation comoving-entropy trajectory versus original code-v2 thermodynamic equation

## 1. Source firstness: NOT a new entropy/EOS inconsistency claim

AUTHOR FIRST: Wu and Xu, JCAP 02 (2026) 063. ORIGINAL PUBLIC repository Fenyutanchan/Primordial-Black-Hole pinned to commit d395183674cace6c9906a8911bdeb7234ba4040d. Original author main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6, particularly lines 60–85. Original exact FULL thermodynamic data arXiv-2509.05618/data/ext/N_around_m_e.csv 1000 × (T,g_rho,g_s), Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8. Original interpolator tool_script-N_relativistic_species.jl blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc, piecewise linear g(T) in ln T, constant extrapolation outside its table, and independently constructed inverse rho-to-T on a 1000-point log-rho lookup.

IN-PROJECT FIRST: Mech-S9 ROT002 FIRST original source zero-PBH entropy/EOS nonadiabatic-null discrepancy; Mech-S9 ROT003 original n_B photon/entropy source null. REC11 ROT021, KN13 ROT017/018, and MT15 ROT010 already independently checked the original 1000-row source table, showing deviations of comoving entropy and baryon proxy. INT9 ROT016 first independent baryon proxy/dilution source bridge. Mech-S9 ROT013 FIRST ACTUALLY executed genuine untouched original-author 10-dimensional Julia j22 single input and returned 10000 saved samples of scale factor a(t), temperature T(t), neutron X(t) and six raw hadrons. MT15 ROT017–021 subsequently source-derived various bound/solver diagnostics. This ROT022 does NOT claim entropy/source mechanism as a new discovery, physical result or original-source run. Its distinct bounded contribution is a **joint full-table-source vs ACTUAL executed native 10D-sampled trajectory comparison over the postev interval**, including an explicit same-a adiabatic reference and late low-T null.

ACTUAL NATIVE original source owner Mech-S9 Actions run 43436800793 artifact 14045176436, original untouched ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486, full native 10000x19 CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1, original ZIP CRC PASS and all source provider 16/16 SHA256 entries PASS. Original native source first PBH-zero saved sample ONE-based 8545, native t=.33751037021169 sec, a=185173297559521, T=1.48260941885709MeV; final saved sample10000, t=20075.8047745077sec, a=4.98052146203102e16, T=.00810973699892033MeV. No new Julia process executed in this rotation. All selected 16 native sample decimal tokens independently re-read from this ZIP with exact index/column check.

## 2. Exact original source equation and mathematically different adiabatic null

Original author main-scan.jl line85 AFTER switch n_PBH=0 (and m'_PBH=0) has

    fcode := d ln rho_SM / d ln a = -4 + q_rho/(3+q_s),

where q_rho := d ln g_rho/d ln T, q_s := d ln g_s/d ln T; rho_SM=(pi²/30)g_rho(T)T^4. Define the useful SOURCE PROXY comoving equilibrium entropy Scom proportional to a³ T³ g_s(T), corresponding to equilibrium background photons/thermal SM and without claiming full physical species-network entropy conservation. Direct chain rule gives exactly:

    d ln Scom / d ln a =
        3+(3+q_s) * [-4+q_rho/(3+q_s)]/(4+q_rho)
      = 4 (q_rho-q_s)/(4+q_rho).

Thus the source equation is adiabatic in this proxy only if q_rho=q_s, or the T variation is trivial. The comparison uses the ORIGINAL code equation; a physically adiabatic equation would instead have d ln rho/d ln a = -3(4+q_rho)/(3+q_s), as Mech-S9 FIRST showed. Here no source equations are silently changed or repaired.

For the source continuous EOS, the exact model-predicted log ratio relative to first native zero-PBH Tref is

    ln[(aT g_s^(1/3))/(a_ref T_ref g_s(Tref)^(1/3))]
       = integral_{ln Tref}^{ln T} [
         (4+q_rho)/(-4+q_rho/(3+q_s))
         + 1+q_s/3 ] d ln T.

Original g_rho,g_s are linear in lnT on each original source cell. At table knots their derivatives q have JUMPS. We therefore split the integral at EVERY original 1000-row source logT knot and evaluate by (A) 8-point Gauss–Legendre strictly WITHIN cells and (B) independent 64-subpanel Simpson using CELL-LOCAL ONE-SIDED derivatives at each boundary. Below first source temperature node .01400298972685787 MeV, ORIGINAL constant extrapolation has q_rho=q_s=0 and this integrand is EXACTLY ZERO. This is a non-ambiguous original-source math choice, not a numerical fit to native a(T).

## 3. ACTUAL original numeric source and model results

Original native j22 source first zero sample8545 → last native sample10000:

- native Scom_last/Scom_first = **1.1682400717068826**, i.e. **+16.82400717%**;
- original code-v2 continuum no-PBH EOS model integrated through ALL ORIGINAL source thermal knots predicts **1.170086317111359**, i.e. **+17.00863171%** on the same native endpoint temperatures;
- native-vs-continuum-model relative entropy difference = **-0.0015778711172643733**, i.e. **-0.1577871%** relative to the source-continuum predicted entropy ratio.

The first and last 10D samples are SOURCE EXACT SAVED decimal values. The **actual native value** Scom was evaluated using ORIGINAL author source g_s(T) in the connected GitHub original source (not a guessed thermodynamic degree of freedom). The **predicted model EOS** is an INDEPENDENT source-only continuous quadrature calculation, not the integrated Julia solution. Its small-but-visible difference from actual native Scom can include original ODE solver tolerances, dense output interpolation, rho→T inverse 1000-node LUT approximation and source-model numeric conventions. No root cause or absolute error bound is claimed.

Representative native source windows (row index, T_MeV, actual original Scom ratio):

    8545    1.482609419   1.0000000000
    8900    0.392344898   1.0054436583
    9100    0.199221186   1.0334968500
    9200    0.146213869   1.0650428598
    9300    0.108068424   1.1046064994
    9400    0.078684684   1.1443566373
    9500    0.055207472   1.1648818833
    9600    0.037751702   1.1681452927
    9700    0.025701103   1.1682573500
    10000   0.008109737   1.1682400717

The slight <2e-5 late source proxy decline after around row9700 is preserved; do not claim monotonic increasing Scom at every time. At native row9400 near but NOT EXACTLY the original source T0=.0781852707MeV, source T=.07868468446MeV and Scom/Sref=1.1443566373174445 (14.4357% rise), whereas source continuum-EOS integral predicts about 1.14613310916 at that T. No false source-Q/T event-time claim.

## 4. Mathematically explicit *same scale-factor* adiabatic countercontrol, not an actual replacement universe

At each ACTUAL native saved scale factor a_i, define a separate HYPOTHETICAL adiabatic equilibrium temperature by

    a_i T_ad(a_i) g_s[T_ad(a_i)]^(1/3)
       = a_8545 T_8545 g_s(T_8545)^(1/3).

The source original g_s(T) in the same 1000-node original table makes T*g_s^(1/3) strictly increasing on the analyzed 0.008..1.483MeV range, so bisection gives a unique solution. This comparison has its own frozen scale factor history and is NOT a new fully physical adiabatic 10D solution with self-consistent H(t), particle rates or neutrino clocks.

- At actual native row9400 T_native=.0786846844615MeV, T_ad_same_a=.0755762885672MeV, i.e. native T is **4.11292477% hotter** than that adiabatic *same-a countercontrol*.
- At last native row10000 T_native=.0081097369989MeV, T_ad_same_a=.0077000947732MeV, i.e. **5.31996343% hotter** on the same conditional comparison.

These are source-background mathematical differences, not percent physical temperature/BBN errors of the actual early universe, original code Y, nuclear abundances, or PBH beta exclusion.

## 5. Independent late source-ODE negative control

The source original 1000-row thermodynamics has first temperature node Tfirst=.01400298972685787MeV and CONSTANT extrapolation below it. For T significantly below that transition, g_rho and g_s are constant, q_rho=q_s=0 and ORIGINAL no-PBH source equation becomes dlnrho/dln a=-4, implying exactly a*T=const (as long as source inverse thermo obeys its intended low-T asymptote).

Read ALL 1456 native source postev rows (not just 16 selected g_s rows) and inspect the final **123 rows with T<.013MeV**. Their relative max-min spread of native a*T is only **1.0212742145475756e-14**, computed from untouched original native decimal CSV. This is a strong late-era negative control: the sizeable +16.824% background Scom change is not a uniform solver scale-drift continuing throughout the low-T tail; it is localized principally to the thermal DOF transition. The earlier first 20 rows just below Tfirst show a small interpolation-boundary adjustment up to ~8.49e-8 in aT, so the controlled late threshold was intentionally T<.013 rather than claiming exact aT across all T below Tfirst. This identifies no specific numerical solver bug.

## 6. Numerical checks, corrected negative controls, and honest package scope

The connected ORIGINAL complete 1000-row author table was ACTUALLY fetched/read and Git blob SHA1 verified. The source integral was evaluated independently using all original table intervals with Gauss–Legendre8 and corrected one-sided-cell Simpson64. They agree in the logarithm of aT*g_s^(1/3) to maximum **2.220446049250313e-16** across the 16 native source sample temperatures; all 16 Gauss values reproduce the original independently calculated source continuum EOS ratios within 4.44e-16 in Scom. This is a quadrature consistency test in binary64, NOT a validated original Julia error tolerance.

IMPORTANT SCIENCE TRANSPARENCY: preliminary machine summary V001 used naive global-table derivative evaluation at exact Simpson knots, selecting the wrong one-sided q on derivative jumps; produced an artificial maximum GL/Simpson difference 3.651e-6 in log-r. V002 corrected knot sides but introduced a temporary branch error below Tfirst (returned integrand 2 rather than 0). **Both machine debugging artifacts remain source history but are SUPERSEDED**. Only correction V003, byte-exact Git readback, includes the correct source knot-sided Simpson and below-node constant extrapolation and a clear errata provenance. It agrees with original sound Gauss8 source predictions. No preliminary artifacts are used as final science claims.

The local executable standalone ZIP is SOURCE-LIMITED BY DESIGN: contains unmodified original 713794B Mech-S9 native ZIP and original provider 16/16 SHA256 manifest, executable Python, 16 ORIGINAL-GIT-TABLE-evaluated g_s(T) sample values as an independently source-typed DATA FIXTURE, original native selected source result JSON, verifier, README and six-file SHA256 manifest. The full author 1000-row thermal CSV is **not in the local ZIP**; its original-source integral cannot be independently rerun OFFLINE from this package alone. Full-table source integral + two different quadratures are instead archived in the connected GitHub V003 machine result with the original AUTHOR Git blob source locator. Do NOT misrepresent the local ZIP as a complete two-original-source stand-alone replay. The ZIP ACTUALLY independently reproduces authentic source 16 native sampled entropy ratios, authentic late123-row aT null, and 2000 seeded algebraic controls.

Local source-preserving ZIP: mt15_rot022_wuxu_native_postev_entropy_source_audit_20261113.zip, **720559 bytes**, SHA256 **9450097ba0ba1a4c1a0626993c1e420167a30c4ceb089e5491cd0097c918922e**. Native original ZIP full source checksum/16 internal manifest PASS; outer ZIP CRC PASS, six payload SHA256 PASS, complete isolated NEW CLEAN temp extraction + Python -I mt15_rot022_replay_verify.py recomputes JSON BYTE IDENTICAL PASS; altered original ZIP single-byte tamper fails closed PASS; 2000/2000 independent algebraic positive controls PASS. Local Python producer SHA256 75003bf5d810ff4d4ab0bf598c42ed5aeef85baf402d7bdbf0ec4d1e8ff97199, verifier SHA256 e198fe8d187495660d544975fa5cdfba570eb1baba4cf5210e0a54d12cb22d64, full actual local result JSON SHA256 9665675178e3c167ca39f2a5655cd4a5af34a79de63dc96bf1d81068f37e220f.

## 7. Claims and B1 owner limitations

- Source model internal after PBH zero: original author 1000-row thermodynamics + original returned native j22 10D source sample a,T. No new original Julia execution and no synthetic replacement source.
- No recomputation of true physical species entropy, neutrino heating, baryon number conservation or nuclear reaction network. The source quantity Scom=a³T³g_s(T) is a **MODEL/THERMODYNAMIC PROXY**, not a measured physical entropy balance of a fully coupled plasma.
- No attribution of the -0.1578% native-vs-model residual to a particular solver defect without actual integrator.opts, source inverse-rho interpolation diagnostic and independent tolerance refinement. In particular no claim original source human authors used a wrong physical EOS deliberately.
- Original 10D j22 remains outside the published beta scan maximum by ~0.586%, and the actual source mass-cubic/cutoff numeric inconsistencies identified independently by KN14, LT8, REC11 and MT15 ROT020/021 still require owner convergence gates. This postev entropy diagnostic does not repair or prove physical BBN constraints.
- Exact model mechanism FIRST with Mech-S9 ROT002 and independent MT15 ROT010; no novelty of entropy thermodynamics, no CANON, no EXEC_SIGN, no B1 Julia run authorization or new task cascade, no BW acknowledgment.

FINAL: ORIGINAL_NATIVE_J22_10D_SOURCE_SELECTED_ENTROPY_PLUS_16p824_PERCENT / ORIGINAL_CODE_V2_SOURCE_EOS_PRED_PLUS_17p009_PERCENT / SOURCE_EOS_V003_INDEPENDENT_QUADRATURE_PASS / SELECTED_NATIVE_CLEAN_REPLAY_PASS / OWNER_B1_SOLVER_AND_PHYSICAL_E4_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST.
