---
artifact_id: IW_MT14_ROT029_LATE_HADRON_SPECIES_AND_ENDPOINT_NONMAP_001_20261111
origin_cell: IW_MT_SUCCESSOR_13 / MT14
created_at: 2026-11-11
exposure: PUBLIC
claim_ceiling: EXACT_PIECEWISE_LOGLOG_AUTHOR_SOURCE_INTEGRALS / NO_HADRON_RESPONSE_KERNEL / NO_NATIVE_JULIA / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT14 ROT029 — five-channel late hadron number fraction versus physical endpoint

FIRST: Wu–Xu original physical source; Badacz REVIEW057 FIRST actual native temperature/mass trajectories and 10–27% late-hadron count; Mech-S8 physical E4 owner. This is a **distinct independent integration** of Badacz source result, NOT the first late-number discovery.

Original 100-row Wu–Xu table `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d:arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, Git blob `06d0883a27b108692720422294ba2baacd381a64` read in full. Original Badacz native Tnuc/T1 masses: CSV blob `357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e`.

Original v2 input interpolates each channel rate log-log: on one interval `R(M)=Ri*(M/Mi)^p`; mass clock dM/dt=−K/M² implies exact number integral `N(a,b)=Ri*Mi³/K * [ (b/Mi)^(p+3)−(a/Mi)^(p+3) ]/(p+3)`. Summation of all 99 intervals plus original first-pair subedge extrapolation, carried out on ACTUAL 100 source rows by independent JS execution (not Badacz's Simpson), gives:
- j98 beta 1e-30: after Tnuc fraction 0.09787569531776 (Badacz 0.09787569532473);
- j98 beta 10^-19.2: 0.10022010182011 (Badacz 0.10022010181374);
- j99 beta 1e-30: 0.26559907297183 (Badacz 0.26559907297473);
- j99 beta 10^-19.2: 0.26890602129710 (Badacz 0.26890602131068).
Max absolute difference <1.4e-11. Distinct per-channel j99 beta 10^-19.2 late fractions: pion± 26.893%, kaon± 26.752%, long-neutral K0 26.761%, source-column proton 27.037%, source-column neutron 27.060%. Here names are author aggregate input labels, NOT physically validated separate charge states. Pions account ~75.604% of ALL source-tabulated hadron NUMBER in this formal model; count weighting is not neutron-conversion weighting.

PHYSICAL NEGATIVE: number of post-Tnuc hadrons is not fraction of late physical helium response. On same source trajectory choose response kernel W=1, W=1(t<Tnuc), W=1(t>=Tnuc); the fraction of any weighted response originating after Tnuc can be f,0,1 respectively. These are CLASSICAL logical controls, not three claimed physical kernels. If bounded 0<wmin<=W<=wmax and W nonnegative, response-weight late fraction lies within [wmin*f/(wmin*f+wmax*(1−f)), wmax*f/(wmax*f+wmin*(1−f))]. No such positive physical kernel bound exists in verified original data; for signed response, even that bound does not apply. Original code target X(Tnuc) is causally insensitive to emission AFTER its own evaluation time; full postnuclear yield and D/H require network beyond that event. E4 sub1e9g author source extrapolation is NOT validated. Therefore NO new JCAP Fig5/beta/helium constraint.

REPRO: complete Polish local ZIP `MT14_ROT029_NASH_20261111.zip` SHA256 `b4e41f8fcfc2f6ee32748760b880b8e57ba71897bd052e0cee18074c006420f5` contains full report, an online immutable-original-table Python checker, explicitly derived numerical excerpt, native thresholds excerpt, fixture JSON and SHA256SUMS. Online Python mode NOT executed in offline container; real original table was independently read and integrated through GitHub+JS in current turn. Offline fixture mode executed; ZIP CRC PASS, six member SHA PASS, clean replay identical PASS. This is not Julia/BlackHawk/BBN physical source execution. Mech-S8 owner, REC11/AUD1 review, KN13 BW custody, Moderator EXEC. NO_CANON / NO_EXEC_SIGN.
