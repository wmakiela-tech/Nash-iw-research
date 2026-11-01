# XH-S5 ROT015 — exact spatial field-line mapping and necessary correction to frame-gauge reconnection audit

artifact_id: IW_XH_S5_ROT015_FROZEN_IN_LINE_MAP_COUNTERCONTROL_20261101
return_id: XH-S5-ROT015-FRAME-GAUGE-CONNECTIVITY-MAP-CORRECTION_20261101
date: 2026-11-01
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_MATURE_LOCAL_FRAME_DEPENDENCE / SOURCE_TYPED_PARTIAL_CONTRACT / FULL_ANALYTIC_SPATIAL_FIELD_LINE_MAP / NO_FULL_SOURCE_EQ31_GLOBAL_REPLAY / NO_GRAVITATIONAL_RECONNECTION_PROOF / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

## Original source, provenance and necessary interpretive CORRECTION

Comisso, Asenjo, Reconnection of gravitational fields, Physical Review D 114 084095, 28 Oct 2026 DOI https://doi.org/10.1103/lmqy-pf9k. Primary APS abstract and publication dates RE-VERIFIED Nov1. Original paper defines gravitational reconnection as change of field-sheet CONNECTIONS, not simply local nonideal signals. Full arxiv HTML/PDF were UNAVAILABLE in ROT015. Literal source-like F^a=de^a (eq3), R^a=i_u F^a (eq22), alternate regular transport i_w F=0 (eq28), and line integral (eq31) were transferred explicitly from saved previously full-source-grounded XH-S5 ROT013/014. Full current source reread NOT CLAIMED; original paper code NOT REPRODUCED; exact full separator/global physical criterion NOT TESTED.

Critical mature theory correction: a smooth invertible instantaneous magnetic field-line map DOES NOT exclude 3D reconnection. Reconnection can change material footpoint associations continuously, without magnetic nulls: Priest & Demoulin (1995) DOI 10.1029/95JA02740; Priest, Hornig & Pontin (2003) DOI 10.1029/2002JA009812. This corrects a tempting but WRONG inference from earlier ROT014 endpoint smoothness. NO_NEW_THEOREM, no premature conclusion either reconnection or its absence. Bare coframe derivative changes under smooth local Lorentz rotation while metric remains invariant (mature geometric prior art).

## FULLY EXACT Minkowski test — source-like Eq28 and Eq31 remain nonzero

Metric fixed for ALL kappa: g=diag(-1,1,1,1). u=partial_t fixed. Define b(s)=exp(1-1/(1-s²)) for abs(s)<1, zero otherwise; smooth support. f(y)=b(y), h(t)=t b(t) with h(0)=0,h'(0)=1,h=0 for abs(t)>=1. lambda=.7, beta=lambda*x, alpha=kappa*h(t)*f(y), any real kappa.
Coframe:
 e0=dt;
 A=cos(alpha)dx+sin(alpha)dy;
 e1=cos(beta)A+sin(beta)dz;
 e2=-sin(alpha)dx+cos(alpha)dy;
 e3=-sin(beta)A+cos(beta)dz.
E^T E=I and detE=1 EXACT. Same Minkowski metric, ZERO Riemann and same observer at all times and kappas; control kappa0 and active coframes same entire t0 slice and times abs(t)>=1, same ideal outside abs(y)>=1.
F1=de1=cos(beta)dalpha wedge e2 + dbeta wedge e3, R1=i_uF1=cos(beta)*alpha_t*(-sin(alpha)dx+cos(alpha)dy).
At t0: F1=kappa*f(y)*cos(beta)dt wedge dy +lambda*cos(beta)dx wedge dz, det F1=kappa²*lambda²*f(y)²*cos(beta)^4. Nonzero kappa/f/cos beta gives rank4, no NONZERO four-dimensional transport w with i_wF1=0 locally, a necessary source-like no-slippage test.
Along t=x=z=0, y runs from ideal region through compact nonideal region to ideal, source-Eq31-LIKE component integral abs(int R1)=abs(kappa)*C, C=int_-1^1 b(y)dy=1.2069003224378765. Kappa=.4 => .48276012897515064; kappa arbitrary gives UNBOUNDED source-like raw integral while physical metric stays exactly flat. THIS IS A SINGLE LINE AND COMPONENT, NOT A FULL RECONNECTION RATE OR CONNECTIVITY VERDICT.

## NEW stronger result: COMPLETE closed-form spatial field line maps, not one numerical trajectory

Spatial B1=curl(e1) EXACT:
 Bx=0;
 By=-lambda*cos(lambda*x);
 Bz=sin(alpha)*(cos(lambda*x)*alpha_y-lambda*sin(lambda*x)).
On strip abs(lambda*x)<pi/2, By!=0 for all time and ANY kappa, so x constant along every line and
 dz/dy=tan(lambda*x)*sin(alpha) - sin(alpha)*alpha_y/lambda.

Let S_t(y)=int_-a^y sin(kappa*h(t)*f(s))ds for a>=1. Exact line trajectory for seed (x,-a,z0):
 z(y)=z0+W_t(x,y),
 W_t=tan(lambda*x)*S_t(y)+(cos(alpha(t,y))-1)/lambda.
At y=+a, where alpha=0, field-line ENDPOINT MAP is
 M_t(x,z0)=(x,z0+tan(lambda*x)*I_t),
 I_t=int_-1^1 sin(kappa*h(t)*f(y))dy.
Thus every instantaneous map on this strip is an invertible shear with exact 2D Jacobian det1 and inverse z0=z_end-tan(lambda*x)I_t. Exact smooth spatial 3D diffeomorphism Psi_t(x,y,z)=(x,y,z+W_t(x,y)) has Jacobian det1 and pushforward Psi_t*(B0)=Bt; the full identity was SYMBOLICALLY VERIFIED. Both Psi_t and M_t are IDENTITY at t0 and abs(t)>=1.

IMPORTANT MATHEMATICAL DISTINCTION: this 3D flow of B1 exists while the SOURCE-LIKE 4D ideal condition i_w F1=0 has no nonzero solution in the rank4 region. The former does NOT satisfy the latter. AND invertibility does NOT itself prove no 3D reconnection of material field connections, as classical prior art confirms. Global field SHEETS/source eq30 remain untested.

Precise extra countercontrol: on line x=0, Eq31-like integral abs(kappa)C is positive for kappa!=0, BUT endpoint z_end=z0 for ALL t since tan(0)=0. Nearby x lines change connections in the frame, so this does NOT prove the global absence of slipping reconnection. At x=.25,kappa=.4, initial time derivative of mapped endpoint equals kappa*C*tan(.7*.25)=.085356150809, although physical metric time derivative and Riemann remain ZERO.

## Two independent executed checks and custody

Route A standalone SymPy derives orthonormality and all F/R/B components, exact F determinant, line ODE, W derivative, 2D and 3D Jacobians and global pushforward Psi*(B0)=B(t). All exact assertions PASS.
Route B separately implemented raw coframe 5-point finite difference, independent DOP853 ODE integration of 42 field lines spanning t=-1.2 to +1.2 and kappa=.4/2, separate sine quadrature, R line integral at kappas0/.4/2/10. Max numerical endpoint difference from exact = 1.633779792186417e-10. On x∈[0,.5], analytic uniform lower bound abs(By)>=.7*cos(.35)=.6575608989931652, independent time and kappa. Numerical 2D Jacobian determinants within 2e-12 of 1.
At kappa=.4, seed x=.25,z0=.2: mapped z_end at t0=.2, t.3=.22316316826607094, t.6=.22911631193307402, t1.2=.2. At x=0,kappa=.4 raw line integral numeric .4827601289751498 vs exact .48276012897515064. Separate kappa10 numeric12.069003224378744 vs exact12.069003224378765.

Local Moderator COMPLETE ZIP: IW_XH_S5_ROT015_FIELD_LINE_MAP_FRAME_GAUGE_AUDIT_REPRO_20261101.zip
SHA256 8816b7214af2cd3877851317cd0e09cfaf70d8afde408b9164a05f6414b97434
Complete report SHA256 3a015bfe3827d427bb62df03ab299147ecda676593d3b9cf064ce1906e90a527
Route A Python SHA256 31339848618658de46228d770398fb8480e832c9a326aab4911a4d777051b650
Route B Python SHA256 dd2af7b30beb1f765927df317558708efa42368a890cef86ed9ad2be98d8f54f
ZIP 10 members, CRC PASS, 9 scientific/source-lineage SHA256 member checks PASS, fresh extracted clean REPLAY of both Python scripts regenerates two JSON BYTE IDENTICAL PASS. Included as unchanged prior evidence full ROT013 and ROT014 reports. Original article PDF NOT included. This GitHub text is detailed science, not complete ZIP remote upload.

## Scientific verdict and claim ceiling
CONFIRMED: frame-dependent raw F/R and a frame-dependent 3D field-line map under identical physical metric and observer, with exact smooth coframes and independent numerical replay. NOT CONFIRMED: genuine physical gravitational reconnection, absence of reconnection, author full separator/field-sheet definition, author physically allowed frame class, nonflat Einstein evolution, gravitational waves, or NASH K/J3/GR/PBH theory. EXPLICIT correction: continuous diffeomorphic line map does NOT imply no 3D reconnection. The open referee question is what frame selector or Lorentz-covariant completed observable allows gravitational reconnection to be distinguished from arbitrary time-compact pure local frame rotation at fixed metric. No downstream task cascade, BW/OWNER/REFEREE/EXEC acceptance NOT assumed.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_INGEST_PENDING.
