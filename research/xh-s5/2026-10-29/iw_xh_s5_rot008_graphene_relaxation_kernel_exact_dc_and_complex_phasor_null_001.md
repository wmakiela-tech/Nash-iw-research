# XH-S5 ROT008 — exact nonidentifiability of graphene-motivated four-exponential relaxation from one complex phasor
artifact_id: IW_XH_S5_ROT008_GRAPHENE_RELAXATION_KERNEL_NONIDENTIFIABILITY_001_20261029
return_id: XH-S5-ROT008-GRAPHENE-RELAXATION_KERNEL_PHASE_NONIDENTIFIABILITY_20261029
date: 2026-10-29
source_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: PRIMARY_2026_NATURE_FULL_TEXT / EXACT_CLASSICAL_POSITIVE_KERNEL_CONSTRUCTION / EXECUTED_2_ROUTE_REPRO / NO_SOURCE_DATA_REPLAY / NO_NOVELTY / NO_NASH_PHYSICAL / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Source facts, original authority and boundaries
Eggers, Inzani, Meierhofer et al., "Subcycle videography of Landau–Zener–Majorana transitions in graphene", Nature, published 28 Oct 2026 DOI https://doi.org/10.1038/s41586-026-11214-y ; preprint https://arxiv.org/abs/2602.12844 . Experimental 30 THz central MIR field, XUV 21.7eV probe, momentum microscopy across first Brillouin zone; observe ultrafast LZM transitions and coherent/distorted electron momentum distributions. Reported electric-field/current mean phase delay 4.9 +/- 0.2 fs, ~8.3 fs for ideal ballistic and effective 9.0 +/- 0.7 fs scattering time from SBE relaxation-time simulations. This paper uses broadband Fourier-phase averaging over frequencies with signal >50% of maximum, NOT a single monochromatic 30 THz measurement. It ALREADY uses 2D momentum maps to distinguish electron-electron and optical phonon scattering. Authors explicitly observe simple T1 approximation fails to reproduce redistribution in momentum. Public author raw/code archive https://doi.org/10.26165/JUELICH-DATA/HZFKTH declared in source; it could not be accessed in this rotation, NOT DOWNLOADED nor run.

Mature prior: Drude exponential optical conductivity and multi-relaxation-time/memory optical spectroscopy long predate this example (TU Delft Drude notes https://solidstate.quantumtinkerer.tudelft.nl/3_drude_model/ ; older 2000 PRB generalized relaxation analysis https://thz.yale.edu/sites/default/files/files/PRB_2000_GaAs.pdf ). NO novelty or priority to classical inverse response nullspace, and original 2026 paper is not refuted. Public NASH repo keyword searches Eggers, Landau, Drude empty, NOT evidence about private prior art.

## Exact math witness: positive causal kernels with same DC and whole complex transfer at 30 THz
Pure mathematical four-exponential linear toy, NOT real graphene SBE. y(t)=integral_0^infty k(s)E(t-s)ds, k(s)=sum_i w_i exp(-s/tau_i)/tau_i, w_i>0, sum w_i=1. Thus H(omega)=sum_i w_i/(1+i omega tau_i), H(0)=1.

Define omega0=2*pi*0.03 rad/fs for 30THz. Choose x_i=omega0*tau_i=(1/4,1/2,2,4) EXACT rational; tau_i=(1.32629119,2.65258238,10.61032954,21.22065908)fs. Their complex transfer values are EXACT:
h1=(16-4i)/17; h2=(4-2i)/5; h3=(1-2i)/5; h4=(1-4i)/17.
Let A be real 3x4 observation matrix with rows [1,1,1,1], Re(h), Im(h). Exact Fraction Gaussian elimination => rank(A)=3. Exact rational kernel vector v=(-17/25, 1, -1, 17/25) with Av=0, including sum v=0; this proves nonidentification even knowing DC gain and BOTH components of H at omega0. No small-numeric-gap assumption.

For source-motivated target phase phi=omega0*4.9fs, set t=(27/tan(phi)-11)/126=0.07464387270878498, base w0=(t,t,0.5-t,0.5-t). Let epsilon=0.07, two physically positive weight vectors:
wplus=(0.027043872708785,0.144643872708785,0.355356127291215,0.472956127291215)
wminus=(0.122243872708785,0.004643872708785,0.495356127291215,0.377756127291215).
Exact Hplus(omega0)=Hminus(omega0)=(11+126t-27i)/85, numerically (0.240060328956552 - 0.317647058823529i). Both phase delays 4.9fs, both amplitudes equal, H(0)=1, but kernels differ at finite times. A ONE-POLE Drude model with phase 4.9fs would return tau_D=tan(phi)/omega0=7.01977704fs; this is not the source's 9fs SBE scattering constant.

## Held-out calculations (executed independent methods)
Frequency THz : |Hplus-Hminus| : phase delay plus/minus fs
10 : .0213743058643 : 9.86565462 / 9.67441355
15 : .0167809847138 : 7.94399534 / 7.92720255
20 : .0107333746491 : 6.59528790 / 6.63236519
30 : EXACT 0 : 4.9 / 4.9
45 : .0107333746491 : 3.56937850 / 3.45946322
60 : .0167809847138 : 2.84729675 / 2.67471915
90 : .0213743058643 : 2.06996175 / 1.88201623.
For unit switched-on step at 20fs: response plus .76167471023108 versus minus .77758782022270; delta -.01591310999162. Positive kernels are not identical in time despite one identical phasor. These are NOT measured graphene responses.

For two preregistered models and hypothetical iid complex Gaussian phasor noise with independent standard deviation 0.01 per Re/Im component and equal prior, optimal wrong-model risk Phi(-sqrt(n)*|DeltaH|/(2*.01)); minimum repetitions to reach error <=1%: n=5 at 10THz, n=8 at 60THz, n=19 at 45THz, impossible at 30THz for all n. These samples and noise are SYNTHETIC, not apparatus predictions.

Executed A: standalone Python standard library fractions.Fraction verifies exact rank3 and Av=0, positivity, analytic H, 7 frequencies, step response and Gaussian binary test. Executed B: separately implemented independent SciPy integral of k(s)cos/sin(omega s) over positive times; DOP853 integration of 4 separate ODEs for step. Max quadrature comparison error 4.0217274e-12, ODE 1.59428e-13. Fresh clean extracted ZIP replay both programs -> two frozen JSON files BYTE-IDENTICAL; ZIP CRC + six SHA256 members PASS. No author experiments executed.

## Custody and next discriminating question
FULL Moderator local 12k-character report + standalone stdlib code + independent scipy code + 2 JSON + README + SHA manifest in ZIP:
IW_XH_S5_ROT008_GRAPHENE_RELAXATION_IDENTIFIABILITY_REPRO_20261029.zip
ZIP SHA256 a2dea8b9f6344c972ad46bc8b7ff228695163aa35c8179a48d63fc286cbd21a3.
Full local report SHA256 21352d8827c926456fcb9f630837f5f620cafc2864fb13c8e9a52d304d13d6ea.
Stdlib exact script SHA256 0ad20b55e35828a9ac8f5d5e729ef2109402a4948617f3a2f509f7fad3ad7c4d.
Independent SciPy SHA256 f73a14b3ab40ff4d5761f6f16aca7a849631a6bcf11db04c160e900ff0a085c7.
This GitHub report is a substantive return but DOES NOT assert full ZIP/script stored remotely. BW/OWNER/REFEREE/EXEC acceptance separate and not assumed.

Proposed real experimental falsifier (NOT DONE): use actual authors' broadband Fourier-weighted estimator, matched signal window and covariance, compare held-out pump frequencies and 2D momentum fingerprints among fitted multi-timescale kernels; compare same training phasor with independently held-out full spectral and angle-resolved evidence. Their existing 2D observations already provide complementary constraints, and need not be repeated. No physical K/J3/GR/PBH claims, NO_TASK_CASCADE, NO_NOVELTY, NO_CANON, NO_EXEC_SIGN.
