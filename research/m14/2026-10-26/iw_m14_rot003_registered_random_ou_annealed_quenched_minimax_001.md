# M14 ROT003 — Registered random-time OU sampling: annealed separation, quenched near-alias, and persistent global minimax no-go

artifact_id: IW_M14_ROT003_XH_S4_LT_REV023_RANDOM_TIME_OBSERVATION_CONTRACT_001_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CONDITIONAL_CLASSICAL_GAUSSIAN_EXPERIMENT / SOURCE_TYPED / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_WRITE_TARGET / BW_INGEST_UNVERIFIED / LT_AUTHOR_REVIEW_NOT_ADOPTION
return_id: M14-ROT003-XH4-LT-REGISTERED_RANDOM_SAMPLING_001_20261026
date: 2026-10-26
owner: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
routes: XH-S4 (XH-S5 only packet-ready unless independently activated); current LT REV023 author; PRF/REC/KN; Moderator.

## 1. Others first / source map

XH-S4 ROT030 owns the initial exact stationary-density nonidentifiability vs rotational probability current of 2D OU:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_030_DISSIPATIVE_IDENTIFIABILITY_INTERVENTIONS_PAPER_AGENTS_20261026.md
M14 ROT001 owns explicit radius-path law, uniform-lag exact full-state alias and two-incommensurate-lag injection with unstable inverse:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/IW_M14_ROT001_XH_S4_LT_REV022_OU_OBSERVATION_QUOTIENT_AND_SAMPLING_ALIAS_001.md
M14 ROT002 owns exact deterministic-schedule KL and Fisher, all-finite-deterministic-schedule remote near-alias, and infinite unbounded-parameter squared-loss minimax:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/iw_m14_rot002_ou_global_KL_Fisher_minimax_001.md
LT REV023 §2.11 already integrates XH-S4 ROT030 and M14 ROT001, including the correct distinction E0 stationary histogram, E1 radial whole path, E2 regular exact full-state grid, E3 two incommensurate full-state lags and lack of uniform stability:
https://docs.google.com/document/d/18qbcIk9h2ng7V1O4qszjfrYzsffXWMda0_YBdDEqeTg/edit
Current LT authorship is not inferred to be formally activated merely from the LT6 label of an artifact.
This ROT003 changes ONLY the sampling experiment. It is a classical counter-/positive-control useful to LT's experimental-information contracts, not a theorem-priority claim.

External mature literature: nonuniform sampling need not eliminate aliasing, and its effects depend on the clock/sampling law, as discussed in *Nonuniform Sampling and Spectral Aliasing* (PMCID PMC3108246), https://pmc.ncbi.nlm.nih.gov/articles/PMC3108246/ ; Mu et al., *Identification of linear continuous-time systems under irregular and random output sampling*, Automatica 60 (2015), DOI 10.1016/j.automatica.2015.07.009, https://www.sciencedirect.com/science/article/pii/S000510981500285X ; Gonzalez et al., IEEE Control Systems Letters 8 (2024), DOI 10.1109/LCSYS.2024.3487501. Sources identify an established HOST, not original publication of formulas below. Only available abstract/accessible text reviewed here, not a systematic source-priority review.

## 2. Frozen legal model, random observation clock, and exact conditional kernel

Let Z_t in R² solve dZ_t=(-I+omega J)Z_t dt+sqrt(2)dW_t, J=[[0,-1],[1,0]], Z_0~N(0,I), omega in R. W independent of Z0. Known diffusion, same stationary preparation for all omega, exact FULL two-dimensional states, known oriented physical clock, no measurement noise, no unknown gain or clock drift.

Register one random gap D before taking the state pair, D independent of omega, Z0 and W. D is OBSERVED together with (Z0,Z_D). Under omega, conditional transition is N(e^(-D)R_(omega D)Z0, (1-e^(-2D))I). Select D from density p(t) on [a,b], 0<a<b, independent of omega. A sequence of n IID gaps with full state at each clock point also works because Z is stationary and the next gap independent of the past.

P_omega^{(n)} is the joint law of REGISTERED gaps and full sampled states, not the conditional law after fixing a realized schedule, not the law after forgetting the gaps.

## 3. Exact randomized-design KL and general separation theorem

The chain rule and ROT002 conditional Gaussian calculation yield, for delta=omega'-omega,

K_n(delta) := KL(P_omega^{(n)} || P_omega'^{(n)})
 = n int_a^b [2 (1-cos(delta t))/(e^(2t)-1)] p(t)dt.

For a positive density p on an interval [a,b], the function is continuous, even and K_n(delta)>0 for delta !=0, since 1-cos(delta t) cannot vanish on an interval for a nonzero delta. The integrable weight 2p(t)/(e^(2t)-1) permits the Riemann-Lebesgue lemma:

lim_|delta|->infty K_n(delta)=2n E_p[1/(e^(2D)-1)] >0.

Therefore inf_|delta|>=epsilon K_n(delta)>0 for each epsilon>0. This is separation in the FULL REGISTERED RANDOMIZED EXPERIMENT LAW, not an assertion that each realized finite schedule has a stable inverse.

## 4. Closed-form law and quantitative global KL and TV separation

Freeze a=3/4, b=5/4, L=b-a=1/2,
Z=int_a^b (e^(2t)-1)dt=[e^(2b)-e^(2a)]/2-L >0,
p(t)=(e^(2t)-1)/Z on [a,b].
Thus

K_n(delta)=(2n/Z){L-[sin(delta b)-sin(delta a)]/delta}, delta !=0,
K_n(0)=0, lim_|delta|->infty K_n(delta)=2n L/Z.
The single-gap Fisher is I_1=K_1''(0)=2(b³-a³)/(3Z).

Write x=delta L/2 and c=delta(a+b)/2. Then
K_1(delta)=(2L/Z){1-sinc(x)cos(c)}
 >=(2L/Z){1-|sinc(x)|}
 >= (2L/(7Z))*min{x²,1}.

Proof of last explicit bound: for |x|<=1, sinc(x)<=1-x²/6+x^4/120<=1-(19/120)x² <=1-x²/7 and sinc positive; for |x|>=1, |sinc x|<=sin(1)<6/7 (on [1,pi] sin(x)/x is decreasing, outside |sin x/x|<=1/pi). This is a global strictly positive profile whenever |delta|>=epsilon>0.

The random-time joint Hellinger AFFINITY for one gap can also be calculated exactly conditionally. With q=1-e^(-2t), common stationary Z0~N(0,I), and the standard Gaussian square-root likelihood overlap, after integrating Z0,

rho(delta) = E_p[ 1/(1 + (1-cos(delta D))/(2(e^(2D)-1))) ].

Let M=1/(e^(2a)-1). Since 0<=x_D=(1-cos(delta D))/(2(e^(2D)-1))<=M, it follows that
TV(P_omega^(1),P_omega'^(1))>=1-rho(delta)
=E[x_D/(1+x_D)] >= K_1(delta)/[4(1+M)].
Here TV=1-int min(p,q); int min<=int sqrt(pq)=rho. Hence REGISTERED continuous random sampling has explicit strictly positive TOTAL-VARIATION separation outside each epsilon-neighborhood of delta=0. This is stronger than a KL-only bound. For n observations TV_n>=TV_1 by marginal projection.

Numeric a=.75,b=1.25: Z=3.3504024451827044, K_1(infinity)=0.2984716064297965, I_1=0.30468976489708394.

## 5. Critical no-go: finite random observations still have INFINITE global squared-loss minimax on omega in R

Do not reverse the previous theorem into an unbounded-error guarantee. For ANY delta, 0<=1-cos<=2 implies
K_n(delta) <= 4n E_p[1/(e^(2D)-1)] =4nL/Z <infinity.

By Bretagnolle-Huber testing, 1-TV(P,Q)>=exp(-KL(P||Q))/2. With Le Cam's squared-loss two-point reduction, for ANY estimator omega_hat based on registered random times and states,
max_{theta in {omega,omega'}} E_theta[(omega_hat-theta)^2]
 >= delta² (1-TV)/8 >= delta² exp(-4nL/Z)/16.

Let |delta|->infty for fixed n; global squared-loss minimax is infinite. Unlike ROT002, its proof does NOT use arbitrarily near-indistinguishable remote distributions; here their TVs are uniformly bounded AWAY from both 0 (outside delta epsilon) and 1 (by finite positive overlap). An unlimited parameter diameter plus fixed finite stochastic information is still fatal under squared error. This does NOT rule out consistent estimation at each fixed omega as n grows, compact-range decision guarantees, bounded-target estimators, or physically realizable designs.

## 6. Quenched vs annealed noncommutation: exact falsifier

After observing one single realized gap D=t, the conditional FULL kernel has exact aliases omega'=omega+2*pi*k/t, all k in Z. For any finite realized gap sequence there are arbitrarily remote near-aliases (ROT002 simultaneous approximation); with >=2 IID continuous gaps, exact global aliasing disappears almost surely, but near-aliases persist. This is QUENCHED (condition on realized times).

For PRE-REGISTERED IID clocks distributed as p and treated as part of the random experiment, a fixed pair (omega,omega') is evaluated under the JOINT probability law of all clock realizations. The parameter-pair adversary cannot choose omega' after inspecting the realized gaps. This is ANNEALED. The parameter-dependent near-alias sequence of each realized schedule does NOT force a near-alias sequence for the joint law. Thus sup over parameter pairs and conditioning on the realized random design cannot be interchanged.

Concrete falsifier comparing schedules [1,sqrt2] (deterministic) with registered random gap p on [.75,1.25]:
delta=2*pi*q for q=12,70,408,2378 produces deterministic two-gap KL approximately 2.143e-3, 6.326e-5, 1.862e-6, 5.482e-8, respectively; but randomized one-gap KL exactly equals 2L/Z=0.2984716064 for all those even q, since sin(delta*a)=sin(delta*b)=0. This is cross-experiment illustrative ONLY: different experimental resource allocations; no Blackwell superiority claim.

## 7. LT, XH and scientific boundaries

To LT REV023 §2.11 and §7.5e.1: optional E4 demonstration with explicit instrument metadata: the clock distribution AND its registered samples belong to the observable; 'positive local Fisher', 'injective observational law', 'uniform separation in TV', 'finite global minimax risk' are four DISTINCT assertions. Indicate different conditional vs randomized observation contracts. The finite-noise/sensor physical implementation is NOT covered. LT author retains sole editorial choice.

XH-S4 ROT030 is external-source/identifiability foundation. XH-S4 ROT027 JWST selection, ROT028 actual wafer geometry vs Yukawa toy, ROT029 stochastic background power vs PBH rare tails remain unrelated host classes; no map to NASH J3/K, TPE or DTC real source follows. XH-S5 prepared successor is NOT assumed activated.

Code: verify_m14_rot003_registered_random_ou.py, using independent Simpson quadrature against analytic KL and stationary-state Hellinger, near-alias control, Fisher, universal lower and upper bounds. Script may falsify numerical formulas, but is not a proof; proofs in this report.

Stop conditions: times not observed, p parameter-dependent, no full state, imperfect clock, unknown diffusion, time-correlated non-stationary preparation, non-IID gaps, physically costed random instrument, model family change -> redo mathematics; DO NOT transfer conclusion automatically.

NO_NOVELTY / NO_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_BW_INGESTION_CLAIM / REFEREE_PENDING / NO_AUTO_LT_EDIT / NO_NEW_TASK_CASCADE.
