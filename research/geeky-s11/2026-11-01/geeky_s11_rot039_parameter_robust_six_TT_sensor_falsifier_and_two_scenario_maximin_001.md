---
artifact_id: GEEKY-S11-ROT039-PARAMETER-ROBUST-SIX-TT-FALSIFIER-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-01
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: HIGH_PRECISION_NUMERICAL_FALSIFIER_PLUS_FINITE_POOL_TWO_SCENARIO_MAXIMIN
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT039 — nominally optimal six TT channels from ROT038 are NOT robust to all legal plateau profiles

## Ownership and source

OWN SCIENCE FIRST: Geeky ROT015–017 proved auxiliary even-grid raw realcast TT projection issue and true compatible orthogonal B=GA. ROT027/029: exact uniform Lie insertion/Fourier transition. ROT033: varying Ealpha schedules. ROT034: unrestricted schedule nonidentifiability. ROT035–036: restricted continuum 5/6 sensor gain inverse and finite-grid mismatch. ROT037: exact source-finite six-channel local inverse. ROT038: exhaustive numerical six-channel optimum among 177100 subsets of FIXED 25 candidates AT nominal parameter point; it did not prove global parameter robustness. ROT039 gives a source-legal nonnominal counterexample and a 2-scenario repair only. Mature robust/maximin E-optimal experimental design, see Walter–Pronzato 1987 DOI 10.1152/ajpregu.1987.253.3.R530 and NeurIPS 2005 Robust design of biological experiments; no priority claim.

Source immutable auxiliary deepseek_python_20260627_a87249.py actual SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historic production dtc0a_runtime_v0_3_1.py NOT accessible. Mathematical host: full unmasked even periodic real symmetric tensor N³, true source-compatible B=GA, complete centered THREE-term tensor Lie C=(0,cos x,0), Ealpha=I+alpha h² Delta2. NO source historic masked h=fI K_A, NASH physics K/J3, GR/GW/PBH.

## Exact source-finite inverse host

Same restricted six-known-level ramp/plateau model as ROT037/038. Dose levels x_j=j*.009/5, j0..5. Five known ramps speed v=.012 (total time .75), six unknown positive plateau durations d_j sum .25, one unknown gain t>0. m=round(.12N²); sampled cumulative dose a_d gives alpha_j=N²[a_d(j/m)-a_d((j-1)/m)] in [0,1/6]. For TT sideband (p,s), s in {-1,+1}, q_in,j=1-4alpha_j[sin²(pi*p/N)+sin²(pi/N)], q_out,j same with p+s. The EXACT source-spectral one-Lie insertion mean Omega=(m+1)^-1 sum_ell prod_(j<=ell)q_in,j*prod_(j>ell)q_out,j. Six observations y=t*Omega, analytic source-finite 6x6 Jacobian J=[Omega | t*dOmega/dd0..dd4]. Valid inside a time-mesh parameter chamber avoiding ramp breakpoints.

OLD ROT037 channels: H2−,H2+,H3−,H3+,H4−,H4+.
NEW ROT038 nominal-optimal channels: H0+,H1−,H1+,H2−,H3+,H4−.

## NEW reproducible numerical falsifier, N64

From seeded 39038 deterministic 195-profile synthetic scan, severe LEGAL configuration at N=64,m=492:
 t=.8123225702365454,
 d=(.003160219022080221,.0026756342224162114,.0022914955572644483,.0027910331414697223,.04707365145084304,.19200796660592637).
All d>0 and sum d=.25, all sampled alpha in [0,1/6]. Minimum time-mesh distance from ANY ramp kink .0004637318779 >0, so Jacobian derivative valid.

75-decimal INDEPENDENT exact product/derivative construction plus mpmath SVD:
 UNWEIGHTED OLD sigma_min=1.4479144778436006e-6; kappa2=334344.25367588364; determinant +2.235133339156212e-16.
 UNWEIGHTED NEW sigma_min=1.3056041082172022e-7; kappa2=7286013.7627648385; determinant -2.0759646129901345e-15.
NEW loses 11.09x in smallest singular and has 21.79x WORSE condition. Independent NumPy source-finite analytic Jacobian, separate finite differences from independently built forward model (max absolute derivative mismatch 3.13e-9), and direct mpmath calculation concur.

SECOND declared synthetic observation host weights each channel by real projected TT polarization norm w_ps=||B(kout)(T_p+sW_p)||/(2||T_p||); at SAME adverse N64:
 weighted OLD sigma_min=5.85046155294e-7, kappa2=622037.62;
 weighted NEW sigma_min=5.98531056323e-8, kappa2=8742422.15.
Thus failure survives polarization-aware normalization.

This is robust NUMERICAL FALSIFICATION supported by large 75-digit margin, not formal interval-SVD or global theorem. Do not claim formal proof-assistant certification.

## 195 parameter changes, NOT global certification

Deterministic random strict legal six-plateau profiles with nominal/near/moderate/edge Dirichlet cases, gain range .8..1.3: 84 profiles N64, 84 N128, 22 N256, 5 N512. Minimum across tested profiles of new/old sigma_min: N64=.0901713556; N128=5.23385134; N256=11.1807583; N512=12.7414184. Medians respectively 7.2446,13.2643,13.3108,13.2205. Absence of more adverse cases on N128..512 is NOT an all-parameter guarantee. SAME adverse six-plateau vector when run at N128/256 actually favors NEW; the N64 breakdown is grid-phase/model-sensitive and does not disprove ROT038 nominal N1024 result.

## NEW limited two-scenario exhaustive minimax choice

For EXACTLY two N64 profiles: (1) nominal d_j=1/24,t=1.07, (2) above adverse; and EXACT fixed 25-pool {H0+; Hp± p=1..12}, independently enumerated ALL C(25,6)=177100 subsets. Maximize min_scenario sigma_min(J) and independently minimize max_scenario kappa2(J), separately for TWO declared noise hosts.

Host normalized source Omega: BOTH objectives choose [H1−,H1+,H2−,H2+,H3−,H3+]. Worst sigma_min=5.82447912950e-6; worst kappa2=147763.17. By comparison OLD worst sigma_min=1.14676936519e-6, worst condition=539289.54; ROT038 NEW worst sigma_min=1.30560410822e-7, worst condition=7286013.76.

Host weighted by TT polarization: BOTH objectives choose [H0+,H1+,H2−,H2+,H3−,H4−]. Worst sigma_min=3.12695379970e-6; worst kappa2=121349.22. In this host OLD worst sigma_min=4.63572110e-7, ROT038 NEW=5.98531056e-8.

These are exhaustive numerical 2-point comparisons within 25 candidates. They are NOT proof of robustness over all legal d or all N, or all noise/cost models; the two maximin sets differ between noise hosts. Robust design requires declaring prior uncertainty region and measurement standardization.

## Actually executed controls and custody

Five independent paths (with one transparent shared source finite helper for paths 1,3,4):
 A 195 legal synthetic profiles and exact Jacobian SVD: 975 typed checks PASS.
 B independent 75-decimal derivative products and SVD (not imported from helper): 8 checks PASS.
 C TWO independent 177100-subset searches under two noise hosts: 354218 checks PASS, mostly repetitive numerical SVD checks.
 D independent finite source forward and temporal central differences + projected TT weights, four grids/cases: 37 checks PASS, worst derivative abs 3.12572e-9.
 E LITERAL immutable original auxiliary full N³ real P_TT/E/THREE-term Lie at N12/16, nonconstant short filter schedules: 30 checks PASS; max relative Fourier difference 2.39044e-16. This full-grid test does NOT execute all 492 filter placements at N64.

TOTAL 355268/355268 actual typed tests PASS; NOT physical experiments, not independent referees. Initial development errors in mpmath matrix last-singular index, test gain normalization and copied SHA literal were corrected before final, excluded from PASS. Frozen source bytes unchanged.

Self-contained Moderator-local user-conversation ZIP includes 11KB Polish full report, core, FIVE original standalone executable scripts, FIVE original JSON, FIVE stdout logs, unchanged helper, README+SHA manifest: GEEKY_S11_ROT039_PARAMETER_ROBUSTNESS_TT_SENSOR_FALSIFIER_REPRO_001.zip. ZIP SHA256 bbd5c66df16b9c457dcf0175d5f13108705f1d8fa2c337968b1615a483c82b27. Clean extraction ZIP CRC PASS, payload SHA256 19/19 PASS, all FIVE scripts run again sequentially and FIVE output JSON BYTE IDENTICAL PASS. Code/ZIP local, NOT separately hosted on GitHub.

**FIREWALL:** nominal local optimum ROT038 remains valid as stated; ROT039 rejects only ungrounded PARAMETER-ROBUST upgrade. No original historical DTC production/masked K_A, no real noise calibration or broad experimental validity, no mathematical novelty, external referee, BW ingestion, owner adoption, canon, physical claims or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
