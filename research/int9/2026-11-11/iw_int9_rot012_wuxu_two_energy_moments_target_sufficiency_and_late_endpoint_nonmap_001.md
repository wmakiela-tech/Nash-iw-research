---
artifact_id: IW_INT9_ROT012_TWO_ENERGY_MOMENTS_TARGET_RELATIVE_NONSUFFICIENCY_001_20261111
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_CLASSICAL_LINEAR_RESPONSE_MOMENT_GATE / SYNTHETIC_POSITIVE_SPECTRA / NO_BLACKHAWK_RUNTIME / NO_PYTHIA_REPLAY / NO_BBN_KERNEL / NO_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# INT9 ROT012: two-moment spectral target sufficiency, synthetic positive counterexample, and late endpoint gate

## Primary sources and firstness
Wu–Xu, JCAP 02 (2026) 063 DOI 10.1088/1475-7516/2026/02/063, [arXiv:2509.05618v3 §4.1 Eq (4.1)–(4.2)](https://arxiv.org/html/2509.05618v3), FIRST explicitly integrate secondary-hadron energy because they assume rapid hadronic energy loss/thermalization in early-universe plasma. Authors' original public executable code is a DIFFERENT version, Git v2 commit `d395183674cace6c9906a8911bdeb7234ba4040d`. Mech-S8 ROT015 FIRST clarified BlackHawk configured PRIMARY energy endpoint is not automatically the SECONDARY endpoint. Mech-S8 ROT016 FIRST statically audited public source tree (absent complete BlackHawk executable/tables) and original ODE RATE_ONLY interface `S_h(M,E) -> R_h(M)=integral S_h dE`, and produced a nonnegative source-rate-preserving counterexample where mean energies differ:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s8/2026-11-11/IW_MECH_S8_ROT016_WUXU_RATE_ONLY_SPECTRAL_NULLSPACE_AND_BLACKHAWK_RUNTIME_SOURCE_GATE_001_20261111.md
Badacz REVIEW050/054 FIRST source-native C+D band response and joint k0/k2 test; REVIEW057 FIRST native heavy-end after-Tnuc counts. MT14 ROT029 FIRST independent original-table source counting. INT9 ROT001–011 own earlier conditional response/typing only. ROT012 adds ONLY a **two-moment target-relative exact mathematical sufficiency criterion**, an ORIGINAL source-row-scaled continuous nonnegative witness preserving BOTH number and total secondary energy, and the precise conditional positive approximate-affine error gate. Not mathematical/physical novelty.

## Target-typed classical theorem
Fix time t, species h and energy interval I. Let S>=0 be any finite nonnegative spectral measure on I. Number R=integral S dE; energy Q=integral E*S dE. For a SPECIFIED hypothetical LINEAR response kernel K(t,E), define J=integral K(t,E) S(t,E)dE. All source types matter:
(1) J factors through R for ALL possible S iff K is constant in E.
(2) J factors through (R,Q) for ALL possible S iff K=a(t)+b(t) E is AFFINE in E.
(3) If a SOURCE-GROUNDED UNIFORM bound sup_E |K-(a+bE)|<=epsilon exists, then Jhat=aR+bQ has |J-Jhat|<=epsilon R; for two S with same (R,Q), target discrepancy <=2epsilon R. Without K, a,b and epsilon physically sourced this is math only, NOT a numerical physical error bar.

Proof sufficiency by integration. Necessity of (2): for x<y<z, δ_y and λδ_x+(1-λ)δ_z where λ=(z-y)/(z-x) have equal R=1,Q=y. Equality of J forces K(y)=λK(x)+(1-λ)K(z) for every triple; this is barycentric affinity. For densities only, use regularity/approximate identities and almost-everywhere qualification. For (1), equal masses δ_x and δ_z force K(x)=K(z). Bound in (3) follows by positivity and triangle inequality. All classical.

**STRICT CEILING:** The original Wu–Xu neutron-fraction ODE is generally NONLINEAR in source histories; K is NOT derived or verified as a physical BBN response. These iff statements concern a linear target or valid local linearization on the FULL chosen source class, NOT the nonlinear BBN map.

## Exact continuous positive two-moment witness, beyond Mech-S8's number-only witness
Use Mech-S8's triangular density building block h_a(E)=4(E-a) for E in [a,a+1/2], =4(a+1-E) in [a+1/2,a+1], zero elsewhere. Exact moments:
 integral h_a=1;
 integral E h_a=a+1/2;
 integral E² h_a=a²+a+7/24.
Define A(E)=R*h_2(E) and B(E)=R/2*[h_1(E)+h_3(E)] for ANY R>0. Both are nonnegative CONTINUOUS distributions supported in [1,4] GeV and have exactly:
 R_A=R_B=R;
 Q_A=Q_B=5R/2;
 (E²)_A=151R/24;
 (E²)_B=175R/24;
 target `integral_{E>=3GeV} A=0`;
 target `integral_{E>=3GeV} B=R/2`.
Second-moment discrepancy EXACT R, threshold discrepancy EXACT R/2. This preserves **total hadron energy** in addition to numbers, unlike Mech-S8 ROT016's first-moment-distinct synthetic witness. The E>=3GeV threshold and E² response are synthetic MATHEMATICAL FUNCTIONS, NOT measured/proposed BBN reaction kernels and NOT BlackHawk/PYTHIA spectra or physically feasible event-level fragmentation examples.

SOURCE-TYPED original row, author v2 `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`, mass=5.609588603804452e32 GeV (~1e9 g), five ORIGINAL channel total rate numeric strings:
charged_pion=489105.5126008581;
charged_kaon=59105.93631247951;
kaon_zero_long=29086.774913348447;
proton_labeled=34849.08026691193;
neutron_labeled=34656.17773724596.
Each actual source R_h is plugged into BOTH **synthetic** normalized spectra; EXACT Fraction check preserves both R_h and 5R_h/2, while synthetic threshold differs by R_h/2 and second moment by R_h. Authors' public first row is sourced; distributions A/B and physical K are NOT sourced.

## Separate time/endpoint nonmap
The original Wu–Xu ODE does preserve the TIME DEPENDENCE R_h(t) from changing PBH mass and evolving number density, rather than compressing to one time integral. However a causal state X_n(T_nuc) cannot depend on the later t>T_nuc portion of R_h. Badacz REVIEW057 FIRST native source j98/99 heavy-end shows ~10% and ~27% of modeled HADRON NUMBER produced after T_nuc (in author extrapolation), independently checked by MT14 ROT029 with ~9.8–10.0% and ~26.6–26.9%. This is **not** fraction of energy, helium response or PBH bound. A later light-element dissociation target would require its own post-nucleosynthesis reaction/transport kernel. Wu–Xu §2.2 themselves distinguish modification of BBN products from the neutron/proton ingredient calculation and leave dedicated late dissociation beyond study scope.

For a linear time-energy target J=integral dt integral dE K(t,E)S(t,E), knowing **time-resolved** R(t),Q(t) is sufficient universally iff K(t,E)=a(t)+b(t)E (with known functions). Knowing only fully time-INTEGRATED (Rtotal,Qtotal) requires a,b additionally constant across time. Original rate-only model possesses R(t), NOT verified Q(t), and no source-valid physical K. Both energy and endpoint gates remain independent.

## Repro and scientific limits
Moderator-local standalone full Polish report SHA256 `0f9845c8c1b55c71272167c2ab7beff2392c5e7495212099e99cee25ff168aa5`, 5-member ZIP SHA256 `8923f302002a21f70d73ad62d79469ccc40f559e40af7b7d377cd72198a7d673`. Fully self-contained Python3 stdlib `fractions.Fraction` script embeds ONLY pinned author first-row rates and mathematically integrates the synthetic triangles EXACTLY; 1200 fixed-seed 3-point rational barycentric Jensen/affine tests PASS, plus all five author-rate moment controls PASS. ZIP CRC PASS, four payload SHA-256 PASS, isolated clean Python replay JSON BYTE IDENTICAL PASS. The local full ZIP/code is NOT asserted to be stored in this public GitHub text. No BlackHawk install, PYTHIA v2 tables, genuine secondary energy spectra, original Julia ODE, numeric BBN kernel, physical Y_P or beta constraint evaluated.

**STATUS:** `TWO_MOMENT_POSITIVE_SPECTRAL_NONMAP_PASS / CONDITIONAL_AFFINE_TARGET_SUFFICIENCY_PASS / TIME_SUPPORT_ENDPOINT_GATE / BLACKHAWK_PYTHIA_RUNTIME_AND_PHYSICAL_KERNEL_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING`. STOP: Mech-S8 owns physical E4, Badacz native source, MT15 programme, REC11/AUD1 independent audits, Moderator executes if appropriate. No new task cascade.
