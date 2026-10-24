---
artifact_id: IW_INT8_ROT028_BIDIRECTIONAL_TT_ALIAS_NO_ONE_SIDED_REPAIR_001_20261025
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC_SAFE
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT028 — exact two-way TT/Q alias defect and correction no-go

## Prior authorship
MT13 first constructed metric-transported affine E_g and identified wrapped raw-k TT projector defect; XH-S4 owns curved York. INT8 ROT023–025 previously proved nofold count, sharp spectral norm, 6D singular spectrum and ranks. ROT027 proved arbitrary low-rank correction optimum. PRF11, Geeky-S11 and M13 own separate TT, stencils and historical DTC puretrace KA. ROT028 is a classical block-projector corollary, not a novelty or physical interpretation.

## Exact declared host and theorem
Odd N>=7 on flat periodic 3D lattice; source symmetric tensors with L2 or Fourier Hs norm; shear A=[[1,1,0],[0,1,0],[0,0,1]], pulled FLAT metric g=A^T A. U H(x)=A^T H(Ax) A is geometric-L2 isometric. Source P=flat TT, Q=I-P; target P'=raw wrapped Fourier metric TT, Q'=I-P'. Original retained componentwise stencil E_alpha has symbol e(k)=1-4alpha sum sin²(pi k_i/N), with exact metric-local transported E_g U=U E_alpha (MT13). Let D=P' E_g U-U P E_alpha.

On unfolded k, D=0. On folded k where |kx+ky|>(N-1)/2, let ell=(kx,ky-N sign(kx+ky),kz); in the common orthonormal tensor frame D(k)=e(k)(Pi_ell-Pi_k). Elementary rank-two projector identity yields EXACT:
D = -Q' U P E_alpha + P' U Q E_alpha.
Thus TT-input leaks into target Q', and source-Q leaks into target TT. The two channels have orthogonal inputs AND outputs.

If c=|k.ell|/(|k||ell|), each channel has TWO positive singular values |e|sqrt(1-c²), |e|sqrt(1-(1+c²)²/4), whereas full D has each TWICE. Therefore for ALL s>=0:
||D||_(Hs->L2g)=||DP||=||DQ||=||P'D||=||Q'D||.
Their weighted squared Hilbert-Schmidt norms divide equally. At alpha=.05 e>=.4, exact full rank=N(N²-1); each channel rank=N(N²-1)/2.

## Strong no-go
For ANY linear repair C obeying ANY one condition C=CP, C=CQ, C=P'C or C=Q'C, the full-domain operator norm remains ||D-C|| >= ||D||. Proof compress residual to input complementary sector or target complementary range, where correction vanishes; the surviving defect has the ENTIRE norm ||D||.

For a repair with no cross-sector mixing C=P'CP+Q'CQ, still ||D-C||>=||D||, and EXACTLY ||D-C||_HS²=||D||_HS²+||C||_HS². If actual admissible inputs are RESTRICTED to TT only, repairing just TT->Q is sufficient there. This result says nothing about physically changing the projector.

Numbers alpha=.05:
N31 ||D||=.791410207164, full rank29760, channel rank14880, HS² full9024.5033561 and each4512.2516781.
N41 ||D||=.793853880701, full rank68880, channel rank34440, HS² full20887.2051178 and each10443.6025589.

## Tests, provenance and STOP
Full local Moderator-conversation reproducible package iw_int8_rot028_two_sided_tt_alias_no_one_sided_repair_bundle.zip SHA256 83fb1d11b4182b911a80ce8c3fcd5346e5d23b68f6decbd4846e44b5150c1030 includes full Polish report, executed NumPy source, independent SymPy rational audit, row JSON, log, README, SHA256SUMS. 8 full grids PASS; 60 independent 6x6 SVD cases PASS; 7 exact-rational source/target block matrix audits PASS; 6 real full 3D FFT direct tests N9/17/31 on BOTH TT and Q inputs with original unchanged apply_E/apply_P_TT PASS, max error 9.992e-16. Helper sha256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Explicit failed initial FFT .820696 vs .608318 traced to invalid inverse tensor-index frame; repaired and independently rerun. ZIP clean CRC, SHA7/7, clean no-helper and source-present reruns PASS; native run JSON reproduced byte-identically. Github source CODE upload not asserted.

NO physical curved York, historical KA, NCDG J3/K, gauge or GW energy. Production original DTC runtime bytes unavailable. No independent referee, BW receipt, owner adoption or EXEC. NO_NEW_TASK.