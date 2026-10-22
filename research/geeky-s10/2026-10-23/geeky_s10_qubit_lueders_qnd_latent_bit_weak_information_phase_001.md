artifact_id: GEEKY-S10-QUBIT-LUEDERS-QND-LATENT-BIT-WEAK-INFORMATION-PHASE-001
problem_id: P2-LEGAL-QUANTUM-INSTRUMENT-WEAK-PHASE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_QUBIT_INSTRUMENT_THEOREM / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE

# Qubit Lüders-QND latent-bit weak-information phase

## Question

What survives from the classical weak-reset information phase when the carrier is replaced by a legal qubit CPTP/POVM instrument?

LT5 already established two load-bearing type guards:
1. the classical real reset Q_s=I-see^T is not automatically a legal qubit channel;
2. same nonselective CPTP channel plus same POVM does not determine the causal instrument.

So fix one legal instrument explicitly.

## Legal carrier

Let X=sigma_x and 0<s<1.

Effects:
E_y=(I+y s X)/2, y=+/-1.

Lüders Kraus operators:
K_y=sqrt(E_y).

Instrument:
I_y(rho)=K_y rho K_y.

Parameter family:
rho_theta=(I+theta X)/2, -1<theta<1.

This family is diagonal in the X eigenbasis.

## Exact latent-bit representation

Let Pi_x=(I+xX)/2 for x=+/-1.

Then
rho_theta=sum_x [(1+theta x)/2] Pi_x.

Because every K_y is a function of X, all K_y commute with Pi_x and

K_y Pi_x K_y = [(1+y s x)/2] Pi_x.

Therefore for a record y^N=(y_1,...,y_N),

P_theta(y^N)
=
sum_{x=+/-1}
[(1+theta x)/2]
prod_j [(1+s x y_j)/2].

Hence the repeated quantum experiment is EXACTLY the classical hierarchy

X_latent in {+/-1},
P_theta(X_latent=x)=(1+theta x)/2,

and, conditional on X_latent,

Y_j iid with
P(Y_j=y | X_latent=x)=(1+sxy)/2.

One qubit is therefore NOT N fresh theta preparations. The history repeatedly interrogates one latent sharp eigenvalue drawn once from the theta-dependent initial mixture.

## Exact sufficient statistic and posterior

Let
S_N=sum_j Y_j,
h_N=atanh(s) S_N,
a_theta=atanh(theta).

The record likelihood ratio for latent X=+1 versus -1 is exp(2h_N).

Thus the posterior latent mean is

m_N=E[X_latent|Y^N]
   =tanh(a_theta+h_N).

The conditional postmeasurement state is

rho_{theta|y^N}=(I+m_N X)/2.

So on this commuting family the quantum update is exactly Bayesian updating of one latent bit.

## Exact Fisher identity and QFI ceiling

Differentiate the record law with respect to theta:

d_theta log P_theta(Y^N)
=
(m_N-theta)/(1-theta^2).

Therefore

I_N(theta;s)
=
Var_theta(m_N)/(1-theta^2)^2.

By total variance,

Var(X_latent)
=
E Var(X_latent|Y^N)
+
Var(E[X_latent|Y^N]),

and Var(X_latent)=1-theta^2.

Hence

0 <= I_N(theta;s) <= 1/(1-theta^2).

The upper bound is exactly the quantum Fisher information of rho_theta, since its eigenbasis is theta-independent and its eigenvalues are (1+/-theta)/2.

Thus repeated legal weak measurement on ONE copy cannot create Fisher information beyond the one-copy QFI.

## Monotonicity and fixed-s saturation

m_N is a bounded martingale, so E[m_N^2] is nondecreasing and I_N is nondecreasing in N.

For fixed s>0, the two conditional output laws for latent X=+/-1 are distinct. By the law of large numbers,

S_N/N -> s X_latent almost surely.

Hence m_N -> X_latent almost surely and

I_N(theta;s) -> 1/(1-theta^2).

Repeated unsharp measurement asymptotically recovers the sharp-X information already present in the single commuting preparation.

## No-information weak regime

Let P_+^N and P_-^N denote the record laws conditional on latent X=+/-1.

P_theta^N
=
[(1+theta)/2] P_+^N
+
[(1-theta)/2] P_-^N.

Thus

TV(P_theta^N,P_0^N)
=
|theta|/2 * TV(P_+^N,P_-^N).

For one output,

KL(P_+||P_-)=2s atanh(s).

For N outputs,

KL(P_+^N||P_-^N)=2N s atanh(s).

Pinsker gives

TV(P_+^N,P_-^N)
<= sqrt(N s atanh(s)).

Therefore uniformly for |theta|<=R<1,

TV(P_theta^N,P_0^N)
<=
R/2 * sqrt(N s atanh(s)).

Since s atanh(s)=s^2+O(s^4),

Ns^2 -> 0
implies Le Cam collapse to a parameter-independent experiment.

## Critical weak scaling Ns^2 -> tau

Let s=s_N->0 and Ns_N^2->tau in (0,infinity).

Conditioned on latent X=x,

E[S_N|x]=N s_N x,
Var(S_N|x)=N(1-s_N^2).

With h_N=atanh(s_N)S_N,

E[h_N|x] -> tau x,
Var(h_N|x) -> tau.

Hence

h_N | X=x
converges in law to
H_tau | X=x ~ Normal(tau x,tau).

So the repeated Lüders experiment converges to a finite Gaussian latent-bit experiment:

X_latent ~ (1+theta X)/2,
H_tau | X_latent ~ Normal(tau X_latent,tau).

The limiting posterior is

m_tau=tanh(atanh(theta)+H_tau),

and limiting Fisher information is

J_tau(theta)
=
Var_theta(m_tau)/(1-theta^2)^2.

For finite tau>0,

0 < J_tau(theta) < 1/(1-theta^2).

At theta=0,

J_tau(0)
=
E_{Z~Normal(tau,tau)}[tanh(Z)^2].

Hence J_tau(0)~tau for tau->0 and J_tau(0)->1 for tau->infinity.

Thus Ns^2 is the weak measurement information-time variable.

## Strong weak-time regime Ns^2 -> infinity

The Bhattacharyya coefficient of the one-shot conditional distributions is sqrt(1-s^2).

For N shots it is

BC_N=(1-s^2)^(N/2).

If Ns^2->infinity, then BC_N->0, so the record identifies the latent eigenvalue with vanishing error.

Therefore

Ns^2->infinity
implies
I_N(theta;s)->1/(1-theta^2).

Information SATURATES at one-copy QFI. It does not diverge.

## Information versus disturbance

The nonselective Lüders channel maps Bloch coordinates as

(r_x,r_y,r_z)
->
(r_x, sqrt(1-s^2) r_y, sqrt(1-s^2) r_z).

After N repetitions the transverse factor is

(1-s^2)^(N/2).

If Ns^2->tau this tends e^(-tau/2).

For the admitted commuting family rho_theta=(I+theta X)/2, r_y=r_z=0, so

Lambda_s^N(rho_theta)=rho_theta

for all N and s.

Thus information can accumulate with zero NONSELECTIVE disturbance on this commuting QND family.

That does not imply zero disturbance for noncommuting states.

## Exact contrast with the classical raw-reset carrier

Classical raw-reset after triangular transformation:
Y_j=s theta + eta_j,
eta_j iid Normal(0,sigma^2),

so
I_N^classical=Ns^2/sigma^2,

which can diverge.

Legal one-copy Lüders-QND qubit:

I_N^quantum <= 1/(1-theta^2).

The source distinction is:

REPEATED ACCESS TO ONE LATENT SAMPLE
!=
REPEATED FRESH ANALOG ACCESS TO THE PARAMETER.

This is the load-bearing nonmap.

## Relation to LT5 instrument seam

This theorem uses the specific outcome maps
I_y(rho)=sqrt(E_y) rho sqrt(E_y).

POVM effects alone do not license the sequential law.

SAME POVM + SAME NONSELECTIVE CHANNEL
!=
SAME SEQUENTIAL INSTRUMENT.

Thus this result cannot be transferred to another instrument merely because its one-shot probabilities and averaged channel agree.

## Mature-host subtraction

This is established quantum-measurement territory.

Relevant mature hosts include:
- repeated unsharp Lüders measurements;
- sequential quantum measurements;
- QND measurement of commuting observables;
- continuous weak-measurement limits;
- quantum Fisher information and data processing.

Haapasalo, Heinosaari and Kuramochi (2016), "Saturation of repeated quantum measurements", prove that repeated unsharp two-outcome Lüders measurement continues to refine information and characterize the limiting observable.

Diósi (2003), "Single qubit estimation from repeated unsharp measurements", studies long sequences of unsharp qubit measurements and their continuous-measurement limit.

NO NOVELTY is claimed.

Project-local value is the exact carrier typing:
1. latent-bit representation;
2. sharp Ns^2 three-regime limit;
3. one-copy QFI cap;
4. explicit nonmap from classical raw-reset divergence.

## Firewalls

LEGAL POVM != FULL INSTRUMENT.
SAME POVM + SAME CHANNEL != SAME HISTORY.
ONE QUBIT != N FRESH PREPARATIONS.
REPEATED WEAK QND READOUT != FRESH ANALOG PARAMETER READOUT.
OUTCOME INFORMATION GROWTH != QFI CREATION.
ZERO DISTURBANCE ON COMMUTING FAMILY != ZERO DISTURBANCE ON ALL STATES.
CLASSICAL RESET FLOW != LÜDERS INSTRUMENT.

## Disposition

LEGAL QUANTUM CARRIER = PASS.

EXACT LATENT-BIT REPRESENTATION = PASS.

EXACT FI IDENTITY:
I_N=Var(m_N)/(1-theta^2)^2.

ONE-COPY QFI CAP:
I_N<=1/(1-theta^2).

WEAK PHASE:
Ns^2->0: no-information;
Ns^2->tau: finite Gaussian latent-bit experiment;
Ns^2->infinity: sharp-X limit / QFI saturation.

STOP this qubit seam unless a future result brings:
- a materially different instrument;
- a noncommuting parameter family with genuine information-disturbance competition;
- fresh-copy resource accounting;
- source-matched physical hardware/timing/noise;
- referee correction.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
