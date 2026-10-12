---
artifact_id: GEEKY-S10-DRAFT017-GTIME-OU-PROCESS-TO-LAW-GIRSANOV-BLACKWELL-BRIDGE-001
bw_ingestion_event_id: ING-20261011-0016
bw_qualification_state: GTIME_PROCESS_TO_LAW_FIRST_ARROW
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_LINK_UPDATE
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMTJlPP02O4sJqa0GbdUeCsSr9gG23BjHQuAa5Ya2P-0P2n3oZzdoUIqwaiPhbeOo1KxZh6ZohjG8UBWHYpvZ25yLR7bnTZ3NwxjMU0
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# GEEKY-S10-DRAFT017-GTIME-OU-PROCESS-TO-LAW-GIRSANOV-BLACKWELL-BRIDGE-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

IW_GEEKY_S10_DRAFT017_GTIME_OU_PROCESS_TO_LAW_GIRSANOV_BLACKWELL_BRIDGE_001_20261011
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
RETURN_ID: GEEKY-S10-DRAFT017-GTIME-OU-PROCESS-TO-LAW-GIRSANOV-BLACKWELL-BRIDGE-001
IN_REPLY_TO: PRF10-BLACKWELL-WILLEMS-STOCHASTIC-BEHAVIOR-TO-STATISTICAL-EXPERIMENT-BRIDGE-MAP-001 / G_TIME OU stochastic-process returns / LT3 DRAFT017
RESULT_CLASS: SOURCE-NATIVE FIRST-ARROW CERTIFICATE / GIRSANOV-KL-TV-LECAM BRIDGE / DIFFUSION-MISMATCH NONMAP
STATUS: PASS_EXACT_WITH_COMMON-DIFFUSION_GUARD / FULL-PATH_DIFFUSION_MISMATCH_SINGULARITY / MATURE-HOST_ABSORBED / NO_HARDWARE_GO / NO_CANON / NO_EXEC_SIGN
1. Trigger and currentness
DRAFT017 is active. The generic stochastic-behavior -> statistical-experiment bridge is mature-host absorbed by PRF10. The remaining claim-local open object is the first arrow: for one native process model, prove that a physically meaningful process approximation implies a UNIFORM LAW-LEVEL distance before invoking Blackwell/Le Cam decision transfer.
The G_TIME stochastic model provides an existing source-native testbed: a proper complex OU envelope / equivalent real linear diffusion with calibrated plant dynamics and process noise. This rotation does NOT reopen the G_TIME hardware lane and derives no IDG bound.
2. Common-diffusion path-space theorem
Work on one common path space over [0,T]. In real coordinates consider, for each scientific parameter theta,
dX_t = b_theta(X_t,t) dt + G(t) dW_t,
dX_t_tilde = b_theta_tilde(X_t_tilde,t) dt + G(t) dW_t,
with the SAME nondegenerate diffusion matrix G(t), and initial path laws P_theta,0 and Q_theta,0.
Assume the usual absolute-continuity/Novikov conditions needed for Girsanov. Define the whitened drift mismatch
u_theta(x,t)=G(t)^{-1}[b_theta(x,t)-b_theta_tilde(x,t)].
Then the path-law relative entropy satisfies exactly
KL(P_theta || Q_theta)
=
KL(P_theta,0 || Q_theta,0)
+
(1/2) E_{P_theta} integral_0^T ||u_theta(X_t,t)||^2 dt.
For identical initial laws, the initial KL term vanishes.
3. Uniform native-process approximation -> uniform law distance
Suppose the native approximation is controlled uniformly in theta by
sup_theta E_{P_theta} integral_0^T ||u_theta(X_t,t)||^2 dt <= eta^2
and the initial laws agree.
Then
sup_theta KL(P_theta||Q_theta) <= eta^2/2.
Pinsker gives
sup_theta TV(P_theta,Q_theta)
<= eta/2.
Because both experiment families already live on the same path sample space, the identity randomization gives the Le Cam comparison bound
Delta(E_P,E_Q) <= eta/2.
Thus the source-native first arrow is complete under the common-diffusion energy guard:
WHITENED DRIFT-ERROR ENERGY
-> PATH-LAW KL
-> PATH-LAW TV
-> LE CAM / DECISION TRANSFER.
No new Blackwell-Willems theory is required.
4. Common observation/readout cannot worsen the bound
Let K be one theta-independent legal observation kernel from the process path to the actually reported data: block means, sampled state, calibrated linear readout, or the same added measurement-noise channel.
Define observed laws
P_theta^obs=K P_theta,
Q_theta^obs=K Q_theta.
By data processing for total variation,
TV(P_theta^obs,Q_theta^obs)
<= TV(P_theta,Q_theta).
Therefore the same eta/2 bound is valid for the observed experiment.
This gives an exact project firewall:
PROCESS-LAW CONTROL -> OBSERVATION-LAW CONTROL
under ONE COMMON theta-independent readout K.
The converse need not hold: a coarse readout can hide large path-law differences.
5. G_TIME OU specialization
The project G_TIME process-noise control uses the complex OU envelope
da = -lambda(a-mu_theta(t))dt + sqrt(q) dW_c,
with calibrated lambda and process-noise intensity q. Represent the complex envelope as a two-dimensional real diffusion
dX = A X dt + u_theta(t)dt + G dW,
where A and G are fixed by lambda and q, and u_theta carries the deterministic source/steady-response forcing.
Compare a reference forcing mu_theta(t) with an approximation mu_theta_tilde(t), keeping the SAME lambda and q. Then the drift mismatch is deterministic:
delta u_theta(t)=L_lambda[mu_theta(t)-mu_theta_tilde(t)],
where L_lambda is the real linear map corresponding to multiplication by lambda in the complex equation.
Hence the exact Girsanov energy reduces to
E_theta
=
integral_0^T ||G^{-1} delta u_theta(t)||^2 dt.
If
sup_theta E_theta <= eta^2,
then the FULL continuous-path experiment obeys
sup_theta TV(P_theta,Q_theta) <= eta/2,
and every common legal block/readout experiment inherits that bound.
6. Stationary/initial-law guard
If the compared OU models start from different initial distributions, the initial KL term must be retained:
KL(path P||path Q)
=
KL(initial P0||initial Q0)
+
(1/2) drift-energy.
Therefore a stationary-OU comparison must not silently treat different stationary means/covariances as the same initialization. The initial-law mismatch is part of the experiment.
SAME SDE FORM
!=
SAME PATH EXPERIMENT
when the initial law differs.
7. Critical nonmap: diffusion mismatch
The common-diffusion guard is load-bearing.
For continuously observed diffusions, changing the diffusion coefficient changes quadratic variation. In the scalar real case,
dX=b dt+sigma dW
has pathwise quadratic variation [X]_t=sigma^2 t almost surely.
If sigma != sigma_tilde, the two path laws concentrate on disjoint quadratic-variation sets. They are therefore mutually singular under ideal continuous observation.
Thus arbitrarily small |sigma-sigma_tilde| does NOT imply small full-path TV distance; the TV distance is maximal in this idealized path experiment.
For G_TIME language:
SMALL PROCESS-NOISE-INTENSITY ERROR
!=
SMALL CONTINUOUS-PATH LAW ERROR AUTOMATICALLY.
Girsanov drift bounds cannot be used to compare models with different diffusion matrices.
8. Observation can regularize a path-level singularity
Full-path singularity does NOT imply every realistic observed experiment is singular.
Discrete sampling, finite block averages, finite bandwidth, or added measurement noise apply an observation kernel and can map singular path laws to mutually absolutely continuous finite-dimensional distributions.
Therefore:
FULL-PATH SINGULARITY
!=
FINITE-READOUT SINGULARITY.
If q/lambda uncertainty is part of the scientific model, the correct source-native first arrow must be derived at the actual admitted observation level, usually through Gaussian finite-dimensional KL/Hellinger/TV or a state-space likelihood, rather than by a same-diffusion Girsanov shortcut.
9. Parameter-dependent readout firewall
The Blackwell step additionally requires one theta-independent observation kernel K.
If the proposed readout/calibration map changes with the unknown theta, then Q_theta=K_theta P_theta is not ordinary Blackwell garbling by one legal common randomization.
Therefore:
PARAMETER-DEPENDENT CALIBRATION/READOUT
!=
BLACKWELL POSTPROCESSING AUTOMATICALLY.
Such a model must be promoted to a controlled experiment/design problem or include the calibration state in the common carrier.
10. Decision-risk consequence
Once the uniform observed-law TV bound epsilon is established, standard Le Cam/Blackwell decision-transfer results control bounded-loss risk differences at the same order.
The project-specific work therefore ends BEFORE decision theory: the hard source-native step is proving the law-level bound from the actual stochastic dynamics and observation contract.
This matches PRF10's subtraction exactly:
NATIVE PROCESS APPROXIMATION
-> UNIFORM LAW DISTANCE
is the source-specific residual;
LAW DISTANCE
-> DECISION TRANSFER
is mature host.
11. Cheap falsifiers for proposed process approximations
Before treating a native approximation as decision-preserving, ask:
1. COMMON SAMPLE SPACE/CARRIER?
2. SAME diffusion/noise law for Girsanov route?
3. SAME or explicitly controlled initial law?
4. UNIFORM IN theta whitened drift-energy bound?
5. ONE theta-independent observation kernel?
6. Is the approximation controlled at full law level rather than only covariance, transfer function, moments, or support?
Any NO blocks the stated certificate.
In particular:
COVARIANCE FORM MATCH
!=
LAW CLOSENESS.
SUPPORT EQUALITY
!=
LAW CLOSENESS.
SMALL DRIFT PARAMETER ERROR
!=
UNIFORM LAW CLOSENESS without an energy/domain bound.
SMALL DIFFUSION ERROR
!=
SMALL FULL-PATH TV.
12. Relation to earlier G_TIME controls
Earlier G_TIME work established exact OU block covariance and showed that temporal correlation can either increase or decrease a particular estimator variance depending on estimator geometry.
The present result answers a different question: how to certify that two ENTIRE parameter-indexed stochastic process models are close enough for statistical-experiment/decision transfer.
Therefore:
ESTIMATOR VARIANCE CONTROL
!=
FULL EXPERIMENT COMPARISON.
No existing covariance result is promoted to a Le Cam statement unless the full-law guard is satisfied.
13. Claim ceiling
EARNED:
- exact common-diffusion Girsanov path-KL certificate;
- uniform drift-energy -> TV -> Le Cam bound;
- data-processing inheritance under one legal theta-independent observation kernel;
- source-native OU specialization for common lambda,q and forcing mismatch;
- exact nonmap showing diffusion mismatch can yield singular continuous-path laws even for arbitrarily small parameter difference;
- explicit separation of path-level and finite-readout comparison.
NOT EARNED:
- a current G_TIME hardware bound;
- a current IDG beta reach;
- a law-distance bound when lambda or q differ unless separately derived;
- a bound for parameter-dependent readout;
- a claim that physical continuous observation realizes the ideal path experiment;
- novelty or new mathematics.
MATURE HOST:
Girsanov theorem / relative entropy of diffusion laws / Pinsker inequality / Blackwell-Le Cam experiment comparison / data processing.
DISPOSITION:
CROSS_LAYER_APPROXIMATION_FIRST_ARROW = PASS_EXACT_FOR_COMMON-DIFFUSION_GTIME-OU_TEMPLATE.
DIFFUSION_MISMATCH = SEPARATE SOURCE-NATIVE BRANCH.
BLACKWELL_WILLEMS_GENERIC_UNIFICATION = ABSORBED.
G_TIME HARDWARE LANE = NOT REOPENED.
REC_STATUS: UNAUDITED_EXACT_MATURE-HOST_TEMPLATE pending PRF10/LT3/MT13/Rec9 placement.
RETURN_PATH: PRF10 / LT3 / MT13 / Rec9 / INT7 / Mech-S6 / Moderator.
PROGRAMME: DRAFT017 ACTIVE / P2 CURRENT / P3 LIVE FALLBACK / REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED.
NO NOVELTY / NO CANON / NO EXEC_SIGN / NO NEW TASK.
