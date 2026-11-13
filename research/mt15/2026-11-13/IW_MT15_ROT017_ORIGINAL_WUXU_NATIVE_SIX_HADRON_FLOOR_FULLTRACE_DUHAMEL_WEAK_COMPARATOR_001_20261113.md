---
artifact_id: IW_MT15_ROT017_ORIGINAL_WUXU_NATIVE_SIX_HADRON_FLOOR_FULLTRACE_DUHAMEL_WEAK_COMPARATOR_001_20261113
created_at: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: ACTUALLY_EXECUTED_ORIGINAL_NATIVE_10D_TRACE_INDEPENDENT_SOURCE_UNIT_AUDIT_AND_CLASSICAL_SCALAR_COMPARATOR
status: ORIGINAL_GITHUB_ACTIONS_ZIP_16_SHA_PASS / SIX_NATIVE_RHS_SNAPSHOT_COMPONENTS_36_OF_36_PASS / ALL1456_POSTEV_SOURCE_FLOOR_AND_POSITIVE_SIGN_PASS / TWO_INTERPOLANT_DOP853_COMPARATOR_PASS / CLEAN_OFFLINE_BYTE_IDENTICAL_REPLAY_PASS
claim_ceiling: ONE_NATIVE_J22_TRAJECTORY_ON_PATH_SOURCE_DERIVED_SCALAR_WEAK_ONLY_COMPARATOR / NO_NATIVE_ALT_10D / NO_CERTIFIED_ODE_ERROR / NO_PHYSICAL_BBN_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT017 — Full native six-hadron floor trace, source-unit signed RHS reconstruction and restricted exact Duhamel comparison

## 0. Original provenance, precedence and present scientific scope

AUTHOR FIRST: Wu and Xu, JCAP 02 (2026) 063. Exact frozen public source Fenyutanchan/Primordial-Black-Hole, commit d395183674cace6c9906a8911bdeb7234ba4040d. Original ten-component RHS arXiv-2509.05618/main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6 (lines 39–140), original physical reaction source arXiv-2509.05618/tool_script-parameters.jl Git blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5. The original manuscript's physical helium observable is NOT identified with the code's 2X/(1-X) formula without prior reported qualification.

PROJECT FIRSTNESS: LT8 ROT014/015 FIRST uncovered native RHS floor exp(max(log_h,-100)) versus returned RAW six hadron histories. INT9 ROT022 FIRST independently derived source-unit signed pointwise floor rate bound for T>=T0; AUD2 ROT003 FIRST gave bounded terminal no-floor sufficiency test. BADACZ FIRST original author Julia native REVIEW053 and REVIEW065 source self-correction; EKS1 FIRST restored Actions executor; Mech-S9 ROT012 FIRST preregistered and ROT013 FIRST ACTUALLY EXECUTED one frozen original author magic(j22,beta,hadrons_output_flag=true), preserving 10000 actual solution points and 6 RAW histories. MT15 does NOT claim their discovery or native execution, but provides an independent fulltrace source RHS and a mathematically distinct restricted scalar comparator. MT15 ROT015 already covered sparse-vs-dense source root methodology; ROT016 independent PRF13 rectangle certificate and its owner firstness remain separate.

ORIGINAL real GitHub Actions run 43436800793, original untouched native artifact 14045176436, ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486 (713794 bytes), 17 ZIP members including 16 internally SHA256-guarded source files. Original 10000-row 2157565-byte native source CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. This audit independently DOWNLOADED exact artifact ZIP through GitHub and actually read every native source CSV row. ZIP CRC PASS, all 16 internal SHA256 checks PASS, original author pinned source and native 13-return statement confirmed.

NATIVE frozen source point: original mass j22 M=1.1211744564709606e9 grams, log10 beta=-16.9974609375, source native Julia original 10D, 10000 times, author Ycode=0.25239220435845267. This is ONE example and not paper Fig5 historical producer/BlackHawk/PYTHIA generator validation.

## 1. Original-source full actual 10000-point result and exact six-species RHS

Original author main-scan.jl lines 53–58 use effective RHS number density n_eff,h=EU(exp(max(ell_h,-100)),3) [GeV^3], while the public native returned hadron arrays use n_raw,h=EU(exp(ell_h),3). At original source PBH cutoff, PBH number density becomes zero. At native sample 8544 (one-based, last observed PBH-active), t=0.3349273518101126s T=1.488248517494034MeV; all six raw ell_h>-100. At native sample 8545 (first observed PBH-zero), t=0.3375103702116899s T=1.48260941885709MeV; all six raw ell_h are FAR below -100. All source samples 8545–10000 (1456 points) have six floor flags true, exactly 8736/8736; all preceding 8544 source samples have zero floor flags, 0/51264. Source sampled T(t) and X(t) both strictly decrease after index8545.

The source after cutoff has no new hadron injections and each of SIX log-density derivatives reduces to -(Gamma_h+n_B C_h(X,T))/H, with positive coefficients. Thus once an ORIGINAL continuous source solution has ell_h<-100 at sample8545 and stays on the source postevaporation branch, ell_h remains below -100 at ALL subsequent times, not merely at saved output rows. This is conditional on the original unchanged ODE and its positivity, NOT evidence of full physical decay physics beyond the frozen model.

The raw hadrons consequently can be many orders below the artificial numerical floor, yet all effective RHS hadron densities remain exactly e^-100 GeV^3 (one per species). Independent dimensional SI-to-GeV conversion with exact defined h=6.62607015e-34 Js, electric charge 1.602176634e-19 C, c=299792458m/s gives:
- 1 millibarn = 2.56818946114750 GeV^-2;
- one effective species numerical floor e^-100 GeV^3 = 0.00484163893556 cm^-3;
- rate per ONE millibarn source-weight coefficient: k0 = e^-100 GeV^3 * (1 mbarn in GeV^-2) * GeV per second = 1.45148683724038e-19 s^-1.

Original source six n/p reaction terms, for each all-floor-active state (T MeV, 0<=X<=1), reduce EXACTLY to

    F_floor(T,X) = k0 * [ (1-X) A(T) - X B ],
    A(T)=1.5 Fc(T,m_pi) + 31 Fc(T,m_K) + 7 + 28,
    B=1.7 + 26 + 7 + 28 = 62.7.

Source Coulomb Fc(T,m)=z/(1-exp(-z)), z=2*pi*alpha/[sqrt(T/m)+sqrt(T/m_p)] with masses in GeV. Six species signed terms were independently recoded from authors' lines 87–98, not imported from owner ROT013 computed coefficients. The six original owner snapshots (initial, prior to PBH cutoff, first PBH-zero, near T1, near T0, final) provide 36 independently named component values: all 36/36 independently recomputed with MAX ABSOLUTE native printed numeric discrepancy 2.465190328815662e-32 s^-1, and MAX RELATIVE nonzero 1.453602959449565e-14. Owner signed six-sums and sums of absolute species terms also PASS for six snapshots. This tests original numeric units, signs, cross-sections, Coulomb terms and source postev effective-vs-raw selection.

## 2. Stronger source sign diagnosis on the observed postevaporation state rectangle

At the first postevap sampled maximum temperature Tfirst=1.48260941885709MeV, A_min=A(Tfirst)=75.87504105706506. Since Fc decreases as T increases, A(T)>=A_min for any 0<T<=Tfirst. For ANY state with T<=Tfirst and X<=Xfirst=0.472697125696049, the signed floor forcing satisfies

    F_floor(T,X) >= k0*[A_min*(1-Xfirst)-B*Xfirst] = +1.5053395326433183e-18 s^-1 > 0,

because A_min/(A_min+B)=0.5475375686579793 > Xfirst. This positivity is an EXACT classical source-rate inequality over the stated rectangle. The actual 1456 native postevap source sample states all fall within that rectangle, and each of their independently reconstructed signed net forcing is positive, ranging +1.5053395326433186e-18 to +3.558211844838787e-17 s^-1. The saved samples alone do not formally prove the entire continuous T/X trajectory stays inside the rectangle; source physical state monotonicity and ordinary scalar comparison are additional steps if extending the rectangle inclusion to unsampled instants. This is NOT a PBH source spectrum bound.

The floor changes the declared author RHS even after all real RAW log densities have become enormously negative. The direct source signed forcing is, however, very small around BBN T0. No physical Yp conclusion follows just from a pointwise rate.

## 3. New exact conditional scalar comparison identity and source-sampled numerical answer

For this ORIGINAL source path after the first PBH-zero sample let Xc(t) denote the native CLAMPED neutron fraction; freeze exactly the SAME native T(t) and weak coefficients. Define, solely for a bounded mathematical comparison, a WEAK-ONLY one-dimensional W(t):

    W'(t) = Gamma_n(T(t))*exp(-Q/T(t)) - kappa(T(t))*W(t),
    W(tfirst)=Xc(tfirst),
    kappa(T)=Gamma_n(T)*(1+exp(-Q/T))+1/tau_n,
    Gamma_n(T)=(255/tau_n)*(12+6x+x^2)/x^5, x=Q/T, tau_n=878.4s.

Since original source postev Xc equation has exactly this same weak term PLUS F_floor(T,Xc), their difference D(t)=Xc(t)-W(t) obeys an EXACT linear forced relation for continuously known source trajectories in that postev branch:

    D'(t) = -kappa(T(t))*D(t) + F_floor(T(t),Xc(t)), D(tfirst)=0,
    D(t) = integral_tfirst^t exp[-integral_s^t kappa(T(u))du] F_floor(T(s),Xc(s)) ds.

This identity is not perturbative. It does NOT represent an alternative full Wu–Xu 10D run, because the weak-only W uses the original recorded background and has NO newly evolved hadron-density states or source-backed counterfactual. It is an exact mathematical comparison definition conditional on the original full source Xc and T, then numerically approximated from discrete native saved values.

Actually executed two source-sample reconstruction methods: (i) piecewise LINEAR interpolation of the 1456 native T(t),Xc(t) postevap samples; (ii) componentwise shape-preserving PCHIP interpolation. Both drive a separately implemented DOP853 solve of the scalar D equation (rtol1e-11, atol1e-28, max step2s). Nonoscillatory source interpolant comparison results:

| event | PCHIP source time seconds | PCHIP damped D = Xc-W | PCHIP undamped integral of F_floor |
| --- | ---: | ---: | ---: |
| T1=0.0996888512474581 MeV | 123.42773687045347 | 1.2223991939725277e-15 | 1.352906064701678e-15 |
| T0=0.07818527068831995 MeV | 214.8591830242949 | 2.204222016560413e-15 | 2.5333136123860324e-15 |
| source final native sample T=0.00810973699892033 MeV | 20075.8047745077 | 3.0952864265192953e-14 | 5.917728409372177e-13 |

At T0 the LINEAR vs PCHIP damped D discrepancy is 5.884485562233779e-21, or 2.669635730244321e-6 RELATIVE TO LINEAR. This measures one source-sampled interpolation sensitivity, NOT a certified numerical error bound from Julia. At native T0 PCHIP Xc≈0.11205518634474068 so restricted D/Xc≈1.967086119315412e-14. At very late native final sample Xc≈1.68560917680474e-11 and D/Xc≈0.001836301361616194 (0.18363%), even though D absolute is only ~3.0953e-14. The very late relative impact is not a primordial helium/BBN epoch sensitivity. No source-native second 10D solve was performed; absence of a numerical high-precision error calibration on source solve(ODEProblem,AutoTsit5(Rosenbrock23())) means do NOT treat these sub-1e-14 absolute values as an independently certified physical observable shift.

The owner previous INT9 source-class upper instantaneous rate at T>=T0 and owner on-path conditional integral upper 3.47243759e-15 remain VALID as a separate conservative bound. Our estimated scalar D(T0)=2.20422e-15 is below this upper, but this does NOT constitute an independent proof of physical solver convergence or actual unclamped source behavior.

## 4. Complete reproducible original source archive and negative knowledge

Actually executed original-source read-only Python NumPy/SciPy reproducer:
- local executable mt15_rot017_postev_floor_fulltrace_reanalysis.py SHA256 90970afdd35d638b2948fbeb03435b0835b2311baa0e6a43baff1a8f3c976131;
- actual full data JSON mt15_rot017_native_fulltrace_math_results.json SHA256 fa5a8542d44065e4584b7daceb50df26d162e8c106f1786a22538074559df693;
- original Mech-S9 official native Actions ZIP included **UNMODIFIED** SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486.

An independent 724417-byte offline ZIP package mt15_rot017_verified_native_floor_duhamel_replay_20261113.zip SHA256 524516f6106c8ec50ffae6a0b11531d8c0703324231f08fecf5464ee84fc8942 holds 5 SHA256-locked payload files plus manifest. ZIP CRC PASS. All 5 package SHA256 PASS. The original GitHub Actions ZIP inside also passes original 16/16 SHA256 and CRC. Extracting the combined package into NEW CLEAN temporary directory, running python -I verify_replay.py, and recomputing both original native source comparator branches produced a BYTE-IDENTICAL full JSON PASS. The offline package is available in the current user conversation sandbox, NOT asserted to be uploaded to GitHub, BW or signed by an external referee.

Negative knowledge: static source floor is a specific source numerical convention, not a physical hadron gas; clipped RHS versus raw source output explains why the six reported tiny densities and ODE influence differ. Direct source owner Mech-S9 already FIRST observed one-run floor ACTUAL. This comparator does not quantify genuine neutron nuclear reactions or full 10D counterfactual source response, source generator E4, original paper Fig5 historical runtime, beta exclusion or physical source helium abundance. It does not falsify existing MT15/PRF13 conditional reduced EKS1 j21 source-rate cone theorem (different quasi-steady source class and historical source j). It shows the importance of typing each source approximation before claiming transferable physical bounds.

END_STATUS: ACTUAL_ONE_AUTHOR_NATIVE_TRACE_10K_SOURCE_FIRST_MechS9 / ALL_16_ORIGINAL_SHA_PASS / 36_OF_36_ORIGINAL_SIGNED_SOURCE_RHS_UNITS_PASS / 1456_POSTEV_ALL_SIX_FLOOR_AND_POSITIVE_SOURCE_SIGN_PASS / SOURCE_PCHIP_LINEAR_DUHAMEL_COMPARATOR_PASS / CLEAN_OFFLINE_BYTE_REPLAY_PASS / E4_SOURCE_HOLD / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
