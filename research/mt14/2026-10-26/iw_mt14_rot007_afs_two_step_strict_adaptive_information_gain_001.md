---
artifact_id: IW_MT14_ROT007_AFS_TWO_STEP_STRICT_ADAPTIVE_INFORMATION_GAIN_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P2_AFS_GAUSSIAN_MIXTURE_ADAPTIVITY_VERSUS_FIXED_EXPERIMENT_DESIGN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_CONDITIONAL_TWO_STAGE_GAUSSIAN_MIXTURE_DECISION_THEOREM / TWO_INDEPENDENT_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NASH_PHYSICAL / NO_ORIGINAL_AFS_EXPERIMENT / NO_BW_INGEST
---

# MT14 ROT007 — źródłowy dwupasmowy AFS: ściśle dodatnia przewaga dwóch adaptacyjnych pomiarów

**Source ownership FIRST**: J. Schröder et al., *Active Fourier Spectroscopy*, arXiv:2505.14364v2 (22 Sep 2026), Eq(1), sections S3.2.1.5 and S3.4.3, https://arxiv.org/html/2505.14364 . Paper itself already introduces adaptive and global/myopic design; THIS IS NOT A CLAIM OF FIRST DISCOVERY OF ADAPTIVITY.

**IW/NASH ownership FIRST**: XH-S5 ROT003 first constructed and audited the exact two-bin TWO-MODEL GAUSSIAN MIXTURE example and single-measurement reversal weighted-within-model versus FULL mixture IG. Pinned public source locator: https://github.com/wmakiela-tech/Nash-iw-research/blob/f4e6b9debc33948beaee2fe0c3ddd1ac67d6ff2a/research/xh-s5/2026-10-26/iw_xh_s5_rot003_afs_information_gain_source_audit_locator_001.md . Their equations corrections to arXiv v2 are not reattributed here. External mature hosts: Gaussian-channel information, Bayesian sequential experiment design, binary entropy and Fano; systematic novelty subtraction not asserted.

**MT14 scientific delta:** determine the exact optimal TWO-measurement adaptive policy in XH-S5's frozen toy, its decision threshold and expected information gain relative to EVERY fixed two-action sequence. Prove STRICT adaptation benefit independently of numerical quadrature.

## One explicitly frozen experiment

M in {0,1} equiprobable. Independently S1~N(1,v1=.02); S2|M=0~N(.35,v2=.000025), S2|M=1~N(.65,v2), conditionally independent of S1. The SAME latent S=(S1,S2) is observed twice, with INDEPENDENT fresh Gaussian noise of variance sigma2=.01 at each action.

Only A: tau=pi/2, Y_A=S1+noise; and B: tau=pi, Y_B=2S2+noise, from the original Fourier cosine response. Acquisition utility is I(S;Y1,Y2,chosen second action) in natural-log units. The action at stage2 is a recorded DETERMINISTIC function of Y1 and does not itself carry additional information. I(S;Y)=I((M,S);Y) by the generative Markov property. NO other delays, action costs, noise models, initial-posterior uncertainty or optical hardware.

Let J(p,D) be the Gaussian binary channel mutual information for Bernoulli input weight p and two conditional normal means separated by D standard deviations, i.e. a one-dimensional Gaussian mixture entropy integral. J is symmetric p<->1-p, strictly concave for D>0, strictly increases on (0,.5).

Let w=4v2=.0001, V=w+sigma2=.0101, d=2(.65-.35)=.6.

## Exactly best fixed action pair

I_A=.5 ln(1+v1/sigma2)=.5 ln3=0.5493061443340549.

I_B=.5 ln(1+w/sigma2)+J(.5,d/sqrt(V))=0.6940835822871511.

I_AA=.5 ln(1+2v1/sigma2)=.5 ln5=0.8047189562170501.
I_BB=.5 ln(1+2w/sigma2)+J(.5,d/sqrt(w+sigma2/2))=0.7030090110305045.
I_AB=I_BA=I_A+I_B=1.243389726621206.

The B,B formula is NOT two independent latent S2 draws: the two measurements share S2, and their sufficient average has independent-noise variance sigma2/2. Thus AB is indeed best among ALL fixed sequences AA,AB,BA,BB. Independent randomization over these sequences cannot beat their maximum.

## Exact two-stage optimal policy

If FIRST action is A, the posterior of S2 and M is UNCHANGED because S1 is independent. Second B retains I_B, whereas second A has only .5 ln(1+(v1*sigma2/(v1+sigma2))/sigma2)=.255412811882995. Hence the optimal A-first policy is fixed AB.

If FIRST action is B and its outcome is y, the exact model posterior is

p(y):=Pr(M=1|Y_B1=y)=logistic[d(y-1)/V].

Within-model posterior variance of 2S2 is
w_post=w*sigma2/(w+sigma2).

The difference in posterior predictive means of the SECOND B at a common y is
d_post=d*sigma2/(sigma2+w).

The second B conditional information, about (M,S2), is EXACTLY

U_B(p)=.5 ln(1+w_post/sigma2)+
       J(p,d_post/sqrt(sigma2+w_post)).

Second A information remains U_A=I_A, independently of y. U_B(0)=.0049261482215 <U_A, but U_B(.5)=.6936351176318 >U_A. Strict concavity and p<->1-p symmetry yield a UNIQUE p_star in (0,.5) with U_B(p_star)=U_A. Therefore the globally best B-FIRST second action is B precisely when p_star<p(y)<1-p_star; A otherwise, equality an ignorable probability-zero tie.

Independent numerical integration gives

p_star=0.237435542900444;
B-second Y_B1 interval: (0.98035902068,1.01964097932);
probability switch: 0.00190304889 (~.1903%).

The exact VALUE functional for this optimal B-first policy is

I_adapt=I_B + E_{Y_B1} max(U_A,U_B[p(Y_B1)])
       =I_AB + Delta,

Delta = integral p_B1(y) [U_B(p(y))-I_A]_+ dy
      =0.0001735219361297 nats.

Hence I_adapt=1.2435632485573358 nats, and the gain over the best fixed pair is ~0.01396%. Because I_adapt>I_AB, B-first adaptive strictly beats any A-first policy, proving GLOBAL two-stage optimality within actions {A,B}.

## Strict positivity WITHOUT numerical optimization or numeric quadrature

On the explicit nonempty observation event 0.4<=p(Y_B1)<=0.6 the y values lie in [0.9931746706801793,1.0068253293198208], of unconditional probability ~0.0006332320432429786.

The midpoint decoder for M from the SECOND B at a known first y has classification error EXACTLY q=Phi[-d_post/(2 sqrt(sigma2+w_post))]=0.0015597973385325183, independent of the first posterior p. Binary Fano gives the LOWER bound I(M;Y_B2|Y_B1=y)>=h(p(y))-h(q).

In this event h(p(y))>=h(.4); adding the within-model information .5 ln(1+w_post/sigma2) establishes

U_B[p(y)]-I_A >= h(.4)-h(q)+.5ln(1+w_post/sigma2)-I_A
             = 0.11699180948782029 >0.

Consequently Delta>=0.0000740829625647 nats >0. The analytic strict sign does NOT depend on exact threshold quadrature; probabilities are ordinary positive Gaussian integrals. This is not a certified interval evaluation of all displayed decimal places.

## Independent executed verification

A self-contained Python+SciPy/NumPy program integrates Gaussian-channel JS information using **500-node Gauss-Hermite** and computes Delta both on physical outcome y and INDEPENDENTLY via posterior p change-of-variables; agreement <1e-13. Recomputes AA/AB/BB, p_star, switch event mass, full information and Fano certificate.

A completely independent second Python+SciPy program DOES NOT import the first; it computes the Gaussian-mixture entropy directly as a one-dimensional continuous density integral (NOT Gauss-Hermite) then integrates over the posterior p. Values of Delta 0.000173521936129739 vs 0.000173521936129715 and adaptive MI 1.2435632485573358 vs 1.2435632485573356. XH-S5's first-step B MI reproduced to ~1e-13. No source author code imports and NO actual spectroscopy experiment reproduction.

Moderator-local six-payload ZIP includes expanded >10k-character Polish full derivation, two standalone scripts, two numeric JSONs, README and SHA256SUMS. ZIP CRC PASS, 6/6 payload SHA PASS and clean-directory two-script rerun reproduced BOTH JSONs BYTE_IDENTICAL. ZIP sha256 4c41fb3089bfec9a58a5a7152e91c8e882aa7bf31f5f1e7056052e2c4d1e24c6. Executable files are NOT claimed stored on GitHub unless a separate direct write/readback occurs.

FALSIFIERS: under this exact Gaussian independence and shared signal, find fixed AA/AB/BB > quoted AB; disprove model posterior logistic formula; find p in (.4,.6) for which second B has information <=I_A; or mismatch of independent mixture entropy and Gaussian-Hermite computation exceeding precision controls. Scope: two actions, two measurements, independent conditional Gaussian noise, prior mixture and fixed hidden S. Three-stage, arbitrary delays, physical hardware, correlated S1/S2, model mismatch, costs, measurements of a different target are OUTSIDE.

Owner review is optional for XH-S5 and REC10; no task cascade and NO automatic Living Theory edit. Conditional mathematical theorem only; science authority/novelty/canon/EXEC and BW ingestion not implied.

STATUS: SOURCE_TYPED_EXACT_TWO_STAGE_POLICY / STRICT_ANALYTIC_FANO_ADVANTAGE / TWO_INDEPENDENT_CLEAN_REPLAY_PASS / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NASH_PHYSICAL.
