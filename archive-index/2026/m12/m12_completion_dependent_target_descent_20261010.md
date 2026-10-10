# M12 — Completion-dependent target descent gate

RETURN_ID: M12-DRAFT009-COMPLETION-DEPENDENT-TARGET-DESCENT-GATE-001

RESULT_CLASS: EXACT_HOST_THEOREM / DRAFT009 TARGET-TYPING REPAIR / NO NOVELTY CLAIM

## Setup

Let the legal model/completion carrier be

A subset Theta x N,

with projection

p:A->Theta,
p(theta,eta)=theta.

Let the scientific target be defined on the full legal carrier:

tau:A->T.

Question:
when is it legal to replace tau(theta,eta) by a theta-only target tau_Theta(theta)?

## Exact theorem

The following are equivalent:

1. There exists tau_Theta:Theta_legal->T such that

tau = tau_Theta o p.

2. tau is constant on every legal completion fiber:

(theta,eta),(theta,eta') in A
=>
tau(theta,eta)=tau(theta,eta').

Therefore:

A COMPLETION-DEPENDENT TARGET DESCENDS TO Theta
IFF
IT IS CONSTANT ACROSS ALL LEGAL COMPLETIONS AT FIXED Theta.

## Minimal counterexample

Theta={theta0},
N={0,1},
A=Theta x N,
tau(theta0,eta)=eta.

The scientific parameter theta is identical in both legal completions, but target values are 0 and 1.

No theta-only target exists.

Thus:

SAME PROFILED PARAMETER
!=
SAME SCIENTIFIC TARGET

when hidden completion is target-bearing.

## Consequence for profiling

If target descent fails, profiling out eta before stating the target is ill-typed.

Legal alternatives are:

1. retain eta, or the target-relevant part of eta, in the scientific carrier;

2. restrict the admissible completion class using source-native information;

3. use a set-valued target

T(theta)={tau(theta,eta):(theta,eta) in A};

4. ask only a coarser target that is constant on completion fibers.

## Set-valued target

When tau does not descend, define

Tau(theta)= {tau(theta,eta): eta legal at theta}.

A scalar/point target is identified only if Tau(theta) is a singleton after all admitted data/constraints.

This makes HIDDEN_COMPLETION_SENSITIVITY explicit rather than silently profiling it away.

## Observation identifiability with completion-dependent target

Given observation map

F:A->Y,

a target tau:A->T is identifiable from F iff

F(theta,eta)=F(theta',eta')
=>
tau(theta,eta)=tau(theta',eta').

This is the ordinary fiber criterion on the FULL legal carrier A.

Only after tau descends through p is it legitimate to state the problem solely on Theta.

## Link to minimal realization

Nonminimal LTI completions provide the exact mature control:
complete transfer behavior can leave unreachable/unobservable completion variables free.

Any target depending on those hidden variables fails completion descent even if the transfer-level theta/model behavior is fully identified.

Hence:

BEHAVIOR-FAITHFUL REDUCTION
!=
TARGET-FAITHFUL REDUCTION

when target lives in hidden completion.

## DRAFT009 repair

Section 3 should type target domain explicitly:

TARGET_DOMAIN =
THETA_ONLY |
FULL_ADMISSIBLE_CARRIER |
QUOTIENT |
SET_VALUED_AFTER_PROFILING |
UNRESOLVED.

Add:

COMPLETION_TARGET_DESCENT =
PASS | FAIL | UNRESOLVED | NA.

Before nuisance/completion profiling:
test whether the target descends through the profiling projection.

## Firewall

NUISANCE FOR THE OBSERVATION MODEL != NUISANCE FOR THE SCIENTIFIC TARGET.

PROFILED PARAMETER IDENTIFIABILITY != COMPLETION-TARGET IDENTIFIABILITY.

BEHAVIOR-PRESERVING HIDDEN COMPLETION != TARGET-IRRELEVANT COMPLETION.

TARGET ON Theta MUST NOT BE INVENTED WHEN THE FULL-CARRIER TARGET VARIES INSIDE p-FIBERS.

HOST_RELATION=EXACT_INSTANCE of quotient/factorization/sufficient-target mathematics.
PROJECT_ROLE=DRAFT009 typing/compiler repair.

REV020 active.
REV021 not created.
TPE thin compiler / HOLD.
NO CANON / NO EXEC_SIGN / NO NOVELTY.
