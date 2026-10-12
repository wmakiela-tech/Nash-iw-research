---
artifact_id: M12-LT3-TARGET-TRANSPORT-WITHOUT-GLOBAL-SHARED-REALIZATION-001
bw_ingestion_event_id: ING-20261010-0117
bw_qualification_state: TARGET_TRANSPORT_CONDITIONAL_INVARIANCE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-LT3-TARGET-TRANSPORT-WITHOUT-GLOBAL-SHARED-REALIZATION-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - LT3 target transport without global shared realization
RESULT_CLASS
EXACT_HOST_THEOREM / CROSS_CONTEXT_COMPILER_RULE / AUTONOMOUS FUNCTION-NATIVE CONTROL / NO NOVELTY CLAIM
TRIGGER
Current LT3 Draft009 places Legal Observable Geometry / shared-realization logic at compiler level.
XH-S3 added a critical repair:
GLOBAL SHARED REALIZATION AS A UNIVERSAL REQUIREMENT IS TOO STRONG.
Component-wise invariant mechanisms and target transportability can be legal even when whole environment distributions differ.
This rotation gives an exact minimal theorem.
SETUP
Let source environment s and target environment t have possibly different joint laws on (X,Y):
P_s(X,Y),
P_t(X,Y).
Assume only that the target-relevant conditional mean mechanism is invariant:
m(x)
=
E_s[Y|X=x]
=
E_t[Y|X=x]
for P_t-relevant x.
No assumption is made that:
P_s(X,Y)=P_t(X,Y),
or even that:
P_s(X)=P_t(X).
CERTIFICATE A - EXACT TARGET TRANSPORT
The target-environment mean is:
E_t[Y]
=
integral m(x) dP_t(x).
Therefore E_t[Y] is determined by:
1. the invariant conditional mechanism m;
2. the target-environment covariate distribution P_t(X).
Full joint-distribution identity across environments is unnecessary.
BOXED
TARGET TRANSPORTABILITY
CAN HOLD
WITHOUT GLOBAL SHARED JOINT REALIZATION.
CERTIFICATE B - FULL-DISTRIBUTION DIFFERENCE CONTROL
Take X in {0,1}.
Let invariant conditional means be:
m(0)=0,
m(1)=1.
Source:
P_s(X=1)=1/2.
Target:
P_t(X=1)=3/4.
Then:
P_s(X,Y) != P_t(X,Y)
whenever Y follows the same conditional mechanism but X-marginals differ.
Yet:
E_t[Y]
=
0*(1/4)+1*(3/4)
=
3/4
is exactly transportable from:
m plus target P_t(X).
Thus:
DIFFERENT ENVIRONMENTS
!=
NONTRANSPORTABLE TARGET.
CERTIFICATE C - SHARED-MECHANISM IS STRICTLY WEAKER THAN SHARED-FULL-MODEL
A global shared-model requirement would demand equality or one common parameterized object accounting for all environment-specific observables under one full contract.
The exact transport theorem above needs only invariance of the target-relevant component m.
Therefore:
FULL SHARED MODEL
=> may imply target transportability,
but:
TARGET TRANSPORTABILITY
DOES NOT IMPLY
FULL SHARED MODEL.
This is a strict logical separation.
CERTIFICATE D - WRONG INVARIANT COMPONENT KILLS TRANSPORT
Suppose instead:
m_s(x)
!=
m_t(x)
on a set of positive P_t measure.
Then using source m_s gives transport bias:
Bias
=
integral [m_s(x)-m_t(x)] dP_t(x).
Therefore component invariance is not decorative.
It is the exact load-bearing assumption.
CERTIFICATE E - TARGET-RELATIVE TRANSPORT
A weaker invariant may suffice for one target and fail for another.
For example:
conditional mean equality
can transport E_t[Y],
while failing to transport:
Var_t(Y),
tail probability P_t(Y>c),
or the full conditional law.
Thus:
INVARIANT CONDITIONAL MEAN
!=
INVARIANT CONDITIONAL DISTRIBUTION.
TARGET TRANSPORTABILITY
IS CLAIM-RELATIVE.
CERTIFICATE F - SUPPORT / POSITIVITY GUARD
Even if m is invariant where both environments are observed, transport requires m to be known or legally identified on the support relevant to P_t.
If target X values occur where source data give no legal information on m, then the formula remains mathematically true but is not operationally identified from the source.
Therefore:
FORMAL TRANSPORT FORMULA
!=
IDENTIFIED TRANSPORT
without support/positivity or another source-native identification argument.
CERTIFICATE G - SELECTION / MEASUREMENT GUARD
If X or Y are measured differently across environments, apparent mechanism invariance may be coordinate/measurement artifact.
Therefore environment typing must freeze:
- variable semantics;
- measurement maps;
- population;
- intervention/selection regime;
- target query.
CONTEXT LABEL ALONE
IS NOT A LEGAL TRANSPORT CONTRACT.
CERTIFICATE H - CAUSAL READING REQUIRES MORE
The conditional invariance theorem above is statistical.
A causal interpretation such as:
"the Y mechanism is causally invariant"
requires additional causal assumptions defining which interventions/environment changes leave that mechanism untouched.
Therefore:
STATISTICAL CONDITIONAL INVARIANCE
!=
CAUSAL MECHANISM INVARIANCE
by itself.
This preserves the XH distinction between invariant prediction and causal transportability.
COMPILER CONSEQUENCE
LT3 should not use one universal cross-context rule:
"all contexts must share one full latent/model object."
Instead classify the bridge:
C0 FULL_SHARED_OBJECT
one common model/parameter object legally explains all contexts.
C1 COMPONENT_INVARIANCE
only a target-relevant mechanism/conditional is shared.
C2 TARGET_TRANSPORT_FORMULA
contexts differ, but a declared target is legally transportable by a source-native bridge.
C3 NO_LEGAL_BRIDGE
no sufficient shared object/component/transport relation is established.
These classes are not a maturity ladder.
They are different scientific contracts.
RELATION TO SHARED-WITNESS LOGIC
Shared-witness intersection remains correct when the claim itself asserts one common latent/model realization.
But it must not be imposed on claims whose legal contract only requires:
- invariant component;
- transported target;
- environment-specific nuisance/population structure.
Therefore:
SHARED-WITNESS LEGALITY
IS CLAIM-TYPED,
NOT UNIVERSAL.
LOWER-HOST SUBTRACTION
HOST_RELATION:
EXACT_INSTANCE of standard conditional-expectation transport / covariate-shift-type factorization.
PROJECT_ROLE:
CROSS_CONTEXT_COMPILER_RULE.
ASSUMPTION_STATUS:
MATCHED only when variable semantics, invariant component and target-environment distribution are legally typed.
SCIENTIFIC_SURPLUS:
NONE demonstrated.
PROSPECTIVE DISCRIMINATOR
For a future multi-environment front, predeclare:
1. target tau;
2. proposed invariant component m;
3. allowed environment changes;
4. target support;
5. measurement semantics.
Then predict target in held-out environment using:
m + target environment inputs/distribution.
If held-out target fails beyond declared error:
the component-invariance/transport bridge fails.
This is a genuine prospective cross-context test.
It does not require a universal shared full model.
FIREWALL
SHARED REALIZATION FAILURE
!=
TARGET NONTRANSPORTABILITY.
INVARIANT COMPONENT
!=
FULL MODEL IDENTITY.
TRANSPORT FORMULA
!=
CAUSAL IDENTIFICATION.
FORMAL TRANSPORT
!=
OPERATIONAL IDENTIFICATION.
TARGET TRANSPORTABILITY
!=
MODEL EQUIVALENCE.
LT3 PLACEMENT
This sharpens Draft009 compiler language:
LEGAL CROSS-CONTEXT SCIENCE
must select the lowest valid bridge among:
shared object,
shared component,
transportable target,
or no bridge.
Do not force all multi-context science into global shared-realization intersection logic.
STATUS
KEEP AS COMPILER REPAIR.
MATHEMATICS ABSORBED BY MATURE HOST.
TPE remains thin method/compiler.
REV020 active authored head.
REV021 not created.
NOVELTY_CANDIDATE=NONE.
NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE / SUBTRACTION_FIRST / SCIENCE_FIRST.
