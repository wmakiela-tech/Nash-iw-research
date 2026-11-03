---
artifact_id: IW_MT14_ROT026_WUXU_THERMAL_EVENT_CLOCK_TNUC_MASS_THRESHOLD_001_20261103
created_at: 2026-11-03
origin_cell: IW_MT_SUCCESSOR_13 / MT14
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_SOURCE_FULL_10D_RUN / NO_PBH_FEEDBACK / NO_PHYSICAL_Yp_DH_BETA / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT026 — source-native 1000-row Wu–Xu thermodynamic clock and conditional initial-mass evaporation threshold at T_nuc

MT14 independent theory and cross-cell science, not Mech-S8 or REC11. MT15 NOT ACTIVATED.

PRIORITY FIRST: Wu/Xu author code and BBN, DAX-S7 ROT034–039 ORIGINAL code cooling vs entropy defect, PRF11 R21/R22 FIRST integral of original g(T) tables and Δln(a)=.04558314308, Mech-S7 ROT010/011 first conditional two-temperature thermal host, Mech-S8 ROT002/006 first E4 source count weighting; Badacz original Julia REVIEW035/038/042/044/047; INT9 ROT001 mass-clock insufficiency. No rediscovery claim. Mech-S8 ROT007 2026-11-03 IMPORTANT PROVENANCE CORRECTION: author commit d395183 is **arXiv v2 dated 2025-12-30**, NOT v3 2026-05. Historical journal Fig5 producer code/figure identity remains OPEN. Owner confirmation https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793692679952239 .

ORIGINAL immutable author sources:
- Repo Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d.
- 1000-row exact original N_around_m_e.csv, 56260 bytes, Git blob SHA1 93f2494f026c5d0587ea40fe08bb938dd9d01fa8, byte SHA256 8fa5c8e633b99657099f783e3aa54d2f7311b414d3f327c5d2c75b67ed7797da. Columns T MeV, g_rho and g_s; source uses LINEAR g interpolation in log T.
- original main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6, lines 75–86: f_W=dlnrho/dln a = -4 + D_rho/(3+D_s) without PBHs (D_a=dln(g_a)/dlnT). Original tool_script-parameters.jl blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5: T_nuc=0.07818527068831995 MeV.
- original g interpolation code blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc. Source mass-clock from preceding MT14 ROT025 original PDG2024 tabular high-energy degree constants gives tau(M0)=0.2376664163901 sec*(M0/1e9g)^3. Source 100-mass grid geomspace(6e8,1e10,100) grams.

**EXACT SOURCE RELATION, CLASSICAL, NOT NEW:** at no PBHs, rho=(pi²/30)g_rho(T)T⁴, H=sqrt(rho/(3 M_Pl,reduced²)), f_W=-4+D_rho/(3+D_s); dt/d lnT=(4+D_rho)/(H f_W). Adiabatic host comparator, using SAME effective source g functions but nonoriginal cooling, has dt/d lnT=-(3+D_s)/(3H). Both integrate 10 MeV to T_nuc with explicit approximate high-T age anchor t(10 MeV)=1/(2H10)=0.00738198072260647 sec; g above 10MeV not fully integrated, so absolute t has an unquantified millisecond-scale anchor uncertainty. No physical two-temperature EOS claim.

**REAL ORIGINAL DATA EXECUTIONS x2:** independent linked GitHub 1000-row complete fetch and JS 8point Gauss-Legendre on every logT-linear segment:
t_Wu_noPBH(T_nuc)=214.96750232179298 sec; t_adiabatic=208.86411534279912 sec; delta t=6.10338697899 sec.
Separate Wolfram kernel independently URLDownloaded original full data, verified 1000 rows and SHA256 and performed a distinct composite SEGMENTWISE SIMPSON:
t_Wu_noPBH=214.96750232675404 sec; t_adiabatic=208.86411534706 sec; delta=6.103386979694 sec.
MAX difference between independent methods 4.9611e-9 sec. These are executed ORIGINAL source data computations, NOT original author Julia 10D.

**NEW DISTINCT CONDITIONAL EVENT CLASSIFIER (combines DAX/PRF cooling FIRST with MT14 source mass-clock ROT025):**
- Wu cooling: initial PBH mass ending evaporation exactly at T_nuc = **9.670932029e9 g**.
- Adiabatic comparator: threshold = **9.578525748e9 g** (about 0.965% lower).
- On original 100 log-spaced mass rows, both classify ONLY rows 99 and 100 as not fully evaporated at T_nuc, under NO_PBH_FEEDBACK. Highest three original masses ~9.447484474e9,9.719817115e9,1e10 g.
- For M0=1e10g, source-only PBH mass remaining at t(T_nuc) ~**4.571012627e9 g**, corresponding T_H~2.31297 TeV. This is a SOURCE-REDUCED noPBH radiation clock, NOT native 10D outcome.
- The condition T_H crossing 100 TeV corresponds to a threshold about 4.2e3 g in initial mass above full-end threshold because final source 100TeV→end lasts 0.280876ms. THIS WIDTH IS BELOW THE TIME ANCHOR UNCERTAINTY; NOT PHYSICAL RESOLUTION. A primary E>100TeV can be emitted before T_H=100TeV; the endpoint is not the onset of all high-energy emission.

**NEGATIVE KNOWLEDGE AND PRIORITY:** DAX/PRF/Mech own prior cooling mismatch. A shift of 6sec in a zero-PBH host does NOT imply a Yp, D/H, beta, or Fig5 exclusion change. At finite beta rho_PBH changes H and rhoSM; neutrino decoupling means adiabatic effective-g is proxy. The released source v2 snapshot and historical JCAP Fig5 have not been byte-linked; v3 rate correction has no pinned public source snapshot. No transfer of ROT024 full-evaporation energy proxy to BBN-active time. Real decisive owner check: native original source 10D record t(T_nuc), M(T_nuc), t(M=1e9g), t(T_H=100TeV) for 3 highest M0 rows and representative beta with verified source, numerical tolerance, Yp mass-fraction rebasing and hadron emission. Mech-S8 own, REC11/AUD1 independent, Moderator EXEC, KN/BW custody pending.

LOCAL COMPLETE POLISH ZIP MT14_ROT026_WuXu_1000_Row_Thermal_Clock_Tnuc_Event_Gate_20261103.zip sha256 01a6482a9882d002e046a011885bbb433d40edafcbbcdd75b0a5581ec8493508. Full 8.5 KB Polish report; Python3 stdlib SHA256+original Git SHA1-guarded online/direct full original 1000-row reproducer (local original source mode NOT executed due DNS), independent Wolfram source program ACTUALLY remotely executed, faithful remote original-source numerical JSON, local CONSTANT-g synthetic control and README + SHA256SUMS. ZIP CRC PASS, six payload SHA256 PASS, clean extract byte-identical selftest PASS. Synthetic local replay NOT conflated with real original-data remote replay. No BW ingest, no owner acceptance.

STATUS: ORIGINAL_1000ROW_REMOTE_TWO_FULL_EXECUTIONS_PASS / TNUC_MASS_EVENT_GATE_CONDITIONAL / ORIGINAL_AUTHOR_V2_VERSION_CORRECTED / DAX_PRF_MECH_FIRST / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
