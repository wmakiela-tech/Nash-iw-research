---
artifact_id: IW_GEEKY_S12_ROT003_INTERACTING_HIDDEN_CTMC_EVENT_CLOCK_EP_NONIDENTIFIABILITY_001_20261111
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
science_status: EXACT_FINITE_CTMC_AUTHOR_PROOF_AND_TWO_CODE_CHECKS / REFEREE_PENDING / OWNER_ADOPTION_PENDING
claim_ceiling: CLASSICAL_FINITE_CTMC_ONLY / NO_SOURCE_NATIVE_THERMODYNAMICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT003 — unbounded hidden entropy production despite complete visible trajectories, event clocks and undirected traffic

## 0. Question and result

In a six-state continuous-time Markov chain whose visible flips sometimes ALSO change the hidden coordinate, can the whole visible trajectory, all microscopic jump timestamps without their hidden labels, the full microscopic stationary distribution and every undirected stationary edge traffic be fixed while microscopic entropy production remains unbounded?

YES. The explicit family below has exactly the same stipulated observations for every parameter choice, but its stationary entropy-production identified set is [0,infinity). Crucially the generator is not an independent visible+hidden product generator. This illustrates a target/source identifiability boundary, NOT a new physical entropy law or a novel mathematical principle.

## 1. Mature foundations and NASH precedence

External host: classical exact strong lumpability for continuous-time Markov chains (Ball and Yeo, Lumpability and marginalisability for continuous-time Markov chains, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/lumpability-and-marginalisability-for-continuoustime-markov-chains/52418B77E531D0733B6792C967E1BB6E); hidden entropy production under coarse-graining (Kawaguchi and Nakayama 2013, https://doi.org/10.1103/PhysRevE.88.022147; Physical Review Research 6 023175 (2024), https://doi.org/10.1103/PhysRevResearch.6.023175; Seifert review 2025, https://arxiv.org/abs/2512.07772).

NASH FIRST: Geeky-S10 T3 already proved the general stationary edge factorization sigma_e=a_e xi_e tanh(xi_e/2), sharp universal A L tanh(L/2) upper bound when traffic A AND stationary-flux affinity L are source-admitted, plus traffic-only insufficiency using biased rings. S10 owner original return: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1791656858458499. REC9 referee corrected global vs fixed-topology sharpness and affinity-object semantics: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1791663645846239.

S10's subsequent provenance nonmap used an INDEPENDENT hidden EP component and explicitly excluded interacting hidden-visible carrier generalization. ROT003 adds a concrete coupled six-state observation contract but does NOT rediscover S10's traffic-only no-go or assert a general additive decomposition for coupled EP. It is a deliberately sharper example of mature host facts. Geeky-S12 ROT001/002 addressed different Fourier/filter objects and are not being extended. Fresh #iw-dispatch currentness check 2026-11-11 found NO new direct IWTO_GEEKY_S12 task.

## 2. Exact six-state generator

Let microscopic states be S={0,1} x Z_3. Let x be visible and i (modulo 3) hidden. Choose s>0, lambda>0, p>0, q>0, p+q=s.

Allowed rates from any (x,i), all other off-diagonals zero:
H+: (x,i) to (x,i+1) at rate p;
H-: (x,i) to (x,i-1) at rate q;
V0: (x,i) to (1-x,i) at rate lambda/2;
V1: (0,i) to (1,i+1) at rate lambda/2, and (1,i) to (0,i-1) at rate lambda/2.
Diagonal Q_aa=-(s+lambda) for every microstate. All positive edges have positive reverse rate. The cross V1 transition changes BOTH x and i, hence Q is not Q_visible tensor I + I tensor Q_hidden in the stated physical coordinates. The six-state chain is irreducible.

Observer O sees: full path x(t) for all t>=0; exact epochs of ALL micro jumps but no hidden orientation/state mark; the stationary microscopic law pi (an extra generous piece of information); and even every undirected stationary edge traffic a_e=pi_i Q_ij+pi_j Q_ji. This specifies a mathematical observation sigma-field, not an assertion about a physical instrument.

## 3. Exact theorem and proof

(A) STATIONARITY: pi_(x,i)=1/6 for all states for all p,q. Ring inflow and outflow are both p+q=s at each hidden index; cross V0/V1 edges occur in paired equal-rate reverses, with total cross inflow/outflow lambda. Hence Q column sums vanish, pi Q=0, unique by irreducibility.

(B) ENTIRE VISIBLE PATH: total rate from any microstate with x into visible block (1-x) is lambda. Strong lumpability implies visible generator Q_vis=[[-lambda,lambda],[lambda,-lambda]], and the entire projected CTMC law is identical for ALL initial hidden distributions with the same visible initial law. No argument from only one-time marginals is used.

(C) MORE: ALL JUMP EPOCHS jointly with full visible path. From every microstate microscopic exit rate is r=s+lambda, constant. Thus the full jump epochs are Poisson(r). Conditional on any event, a visible flip has probability lambda/r, and hidden-only jump probability s/r, independently of the microstate. Event types can be generated by independent state-blind marks; the visible-flip and hidden-only epochs are independent Poisson thinnings with respective intensities lambda and s. A V mark flips x, an H mark leaves x unchanged. Hidden orientation is chosen p/s or q/s ONLY after an H mark, which is unobserved. Thus the joint law of observed x(t) and all micro jump epochs is independent of p/q (conditional on visible x_0). Knowing every microscopic event time without its direction still cannot infer p/q.

(D) EVEN UNDIRECTED MICROSCOPIC TRAFFIC: there are exactly SIX hidden unordered ring edges (3 per x) with stationary traffic (p+q)/6=s/6 EACH. There are SIX cross edges (3 same-index, 3 shifted), each rate lambda/2 in BOTH directions, with traffic lambda/6 EACH. Therefore all twelve undirected edge traffic values and sum_e a_e=s+lambda are independent of p/q, despite the cross-label coupling. The stationary microscopic event rate is the same s+lambda.

(E) ENTROPY-PRODUCTION IDENTIFIED SET: for each hidden edge the stationary forward/backward fluxes are p/6 and q/6. Its steady-state EP contribution (Schnakenberg convention, k_B=1) is (p-q)/6*ln(p/q). The six cross edges have zero current. Hence sigma=(p-q)*ln(p/q), which is nonnegative. At p=q=s/2 the whole chain is detailed-balanced and sigma=0. For q->0+ with p=s-q, sigma=(s-2q)*ln((s-q)/q)->infinity while the observation O, microscopic pi, and the complete undirected traffic list remain EXACTLY fixed. By continuity in q and symmetry p<->q every finite sigma>=0 is attained: identified set exactly [0,infinity). This does not require increasing the hidden activity rate.

(F) CONDITIONAL SHARP REPAIR: if an independently justified SOURCE-ADMITTED constraint forces both hidden rates >=delta>0, delta<=s/2, then sigma is bounded exactly in THIS family by 0<=sigma<=(s-2delta)*ln((s-delta)/delta), attained at q=delta or p=delta. Derivation: let J=|p-q|, 0<=J<=s-2delta, then sigma=J ln((s+J)/(s-J)), strictly increasing in J>0. This is the restricted saturated manifestation of S10's existing affinity+traffic bound, NOT a new universal theorem.

If a physically legal measurement resolves hidden signed cycle current J_signed=p-q, then given fixed s, p=(s+J_signed)/2, q=(s-J_signed)/2 and sigma=J_signed ln((s+J_signed)/(s-J_signed)). This is a direct falsifier of any unqualified claim that EP is intrinsically unknowable: it is unidentifiable from O, but identified after a specified additional directional measurement.

## 4. Executed exact arithmetic controls

For s=1, lambda=1/2 and rational q=1/n, p=1-1/n, multiply the entire 6x6 Q by 4n. It becomes an INTEGER matrix: hidden forwards 4(n-1), reverse 4, two visible transitions n each, diagonal -6n. The authored public JS checker was ACTUALLY EXECUTED in the V8 tool and reads back exact after GitHub storage:
https://github.com/wmakiela-tech/Nash-iw-research/blob/b63ff8ac719ede77c8b5cc65bce6a106852d777c/research/geeky-s12/2026-11-11/iw_geeky_s12_rot003_hidden_ctmc_event_clock_reproducer.js

Checks PASS: row+column sums, exact macro block rates, homogeneous micro exit rates, every edge undirected traffic, all 12 reciprocal edges, entropy edge decomposition and explicit cross-coordinate transition. Independent Python Fraction implementation rebuilt each 6x6 generator at n=2,4,16,1000 and verified stationarity/lumpability/entropy formula, PASS; independent code was not separately published.

Illustrative cases (same lambda=0.5, hidden s=1, stationary pi=1/6 and traffic sum 1.5):
q=1/2: sigma=0;
q=1/4: sigma=0.5493061443340549;
q=1/16: sigma=2.3695439259644338;
q=1/1000: sigma=6.892941269091256;
q=1/1000000: sigma=13.815481926944658.
Floats are only for logarithms; generator identities are exact rationals/integers. Numeric cases do NOT substitute for proof of divergence.

## 5. Consequence and scientific claim boundary

PROBLEM_ID: HIDDEN_EP_INTERACTING_LUMPABILITY_EVENT_CLOCK_IDENTIFIED_SET
QUESTION: do visibility of all micro jump times, macro full path and microscopic undirected traffic yield an EP ceiling?
STRONGEST NEGATIVE: NO, sigma identified set [0,infinity) in a concrete irreducible bidirectional coupled 6-state CTMC with fixed event clock and traffic.
VALUE: makes the missing *direction/affinity* information explicit even under an unusually informative passive observation contract. Independent-product arguments are not needed for this witness.
DECISIVE_FALSIFIER: show actual measurement has a direction-resolved hidden current or source-supported finite flux-affinity bound; alternatively show actual source is not an admissible stationary finite-CTMC carrier.
STOP: do not create another general EP theorem factory; S10 already covers classical A,L traffic bounds.
REOPEN_IF: legally sourced interacting-hidden model and physical detector/source contract actually requires this identified-set decision, or an independent referee finds a mathematical counterexample.

No transfer to BBN/PBH, actual experimental detector, non-Markov process, NASH J3/K, general relativity, quantum field theory or physical entropy estimates. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

## 6. Custody and routing

Canonical public full-body primary: research/geeky-s12/2026-11-11/IW_GEEKY_S12_ROT003_INTERACTING_HIDDEN_CTMC_EVENT_CLOCK_EP_NONIDENTIFIABILITY_001_20261111.md. Public JS checker stored in same dated lineage with pinned readback PASS. GitHub readback of this full report is required and will be reported separately after actual write. BW ingestion/cross-surface custody is PENDING; source delivery by Slack does NOT equal BW or receipt/referee/owner adoption. NO_NEW_TASK_CASCADE.

FINAL: EXACT_SOURCE_DISTINCT_INTERACTING_CTMC_NONIDENTIFIABILITY_PASS / OBSERVATION_LAW_AND_ALL_TRAFFIC_FIXED / UNBOUNDED_EP / MATURE_PRIOR_ABSORBED / SOURCE_NATIVE_HOLD / REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
