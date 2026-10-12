---
artifact_id: EAI-S3-SELECTION-PROVENANCE-EPISTEMIC-SUPPLY-CHAIN-001
bw_ingestion_event_id: ING-20261010-0125
bw_qualification_state: SELECTION_PROVENANCE_SUPPLY_CHAIN
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# EAI-S3-SELECTION-PROVENANCE-EPISTEMIC-SUPPLY-CHAIN-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

EAI-S3 — Selection provenance: epistemic supply chain and outcome-blind curation
STATUS
ROLE-NATIVE EAI SYNTHESIS / DRAFT015 SELECTION-CONTRACT REPAIR / EXTENSION OF INDEPENDENCE-PRESERVING DEPLOYABILITY / NO NEW FRONT / NO NEW TASKS / NO CANON
1. Trigger
The previous EAI rotation established:
INDEPENDENCE IS AN END-TO-END PROPERTY OF THE INFORMATION PATH.
It already included a warning:
BLIND EXECUTION
!=
OUTCOME-BLIND CASE SELECTION.
LT3 DRAFT015 now sharpens a parallel scientific distinction:
PROVENANCE COMPLETE
!=
SELECTION COMPLETE.
This exposes one missing architecture layer.
Knowing where every delivered object came from
does not tell us
why those objects, rather than other eligible objects, were delivered.
Therefore source provenance and selection provenance must be separated.
2. Core distinction
SOURCE PROVENANCE asks:
WHERE DID THIS ITEM COME FROM?
SELECTION PROVENANCE asks:
WHY WAS THIS ITEM INCLUDED, EXCLUDED, PRIORITIZED OR ORDERED?
EXPOSURE PROVENANCE asks:
WHAT DID THE EXECUTOR HAVE ACCESS TO, AND WHEN?
ADJUDICATION PROVENANCE asks:
HOW WAS THE OUTPUT SCORED OR ACCEPTED?
These are distinct.
Thus:
SOURCE-PROVENANCE COMPLETE
!=
SELECTION-PROVENANCE COMPLETE
!=
EXPOSURE-PROVENANCE COMPLETE
!=
ADJUDICATION-PROVENANCE COMPLETE.
A clean scientific supply chain needs the relevant subset of all four,
depending on the claim.
3. Epistemic supply chain
For independence-sensitive or prospective work, the full chain is better represented as:
SOURCE UNIVERSE
->
ELIGIBILITY
->
SELECTION / SAMPLING
->
TRANSFORMATION / SANITIZATION
->
DELIVERY
->
EXECUTION
->
OUTPUT COMMIT
->
GOLD / SCORING
->
REVEAL / INTEGRATION.
Every stage can alter evidential meaning.
This repairs the prior EAI path:
task discovery and executor isolation were necessary,
but selection happens even earlier.
4. Why blind execution can still be biased
Let U be the eligible case universe.
Let S(x) in {0,1} indicate whether case x is selected.
Let Y(x) be the evaluation outcome of interest.
A blind executor may never see Y before solving.
But if the selector chose cases using known or correlated outcome information,
the observed result estimates performance on:
S=1 cases,
not automatically on U.
Therefore:
EXECUTOR BLINDNESS
does not imply
SELECTION BLINDNESS.
And:
BLIND SOLVER
+
OUTCOME-INFORMED CURATION
=
BLIND EXECUTION ON A SELECTED SAMPLE,
not an outcome-blind experiment.
5. Exact statistical control
Let X denote declared pre-resolution metadata.
If selection satisfies a legal predeclared rule based only on X:
S = s(X),
then the experiment is clean relative to that selected stratum.
But a result on S=1 supports the whole universe U only if a legal transport/generalization condition is also established.
For example, under a probabilistic sampling model,
whole-universe performance may require:
known inclusion probabilities;
support/positivity;
and an ignorable or modeled selection mechanism relative to the target.
Without such a bridge:
PERFORMANCE_ON_SELECTED_CASES
!=
PERFORMANCE_ON_ELIGIBLE_UNIVERSE.
This is mature selection-bias / missing-data / covariate-shift structure.
No novelty claim.
6. Deterministic selection is not automatically bad
Many scientific tests deliberately choose:
hard cases;
boundary cases;
counterexamples;
stress regions;
high-value anomalies.
That is legitimate.
The claim ceiling simply changes.
If cases are chosen adversarially to stress a method,
the result is evidence about:
that declared adversarial/stress class.
It is not automatically evidence about:
average performance;
frequency of success;
or representative project-wide utility.
Therefore:
PURPOSIVE SELECTION
!=
INVALID SELECTION.
But:
PURPOSIVE SELECTION
requires
PURPOSIVE CLAIM TYPING.
7. Outcome-blind curation
For a prospective comparator or independent audit,
one strong design is:
freeze an eligible universe using a time cutoff;
freeze metadata allowed for selection;
freeze hard eligibility gates;
freeze ranking or sampling rule;
freeze tie-breaking;
then execute selection without access to post-resolution outcomes.
Call this:
OUTCOME-BLIND CURATION.
This can be performed by:
a mechanical rule;
a fresh isolated selector;
or an auditable precommitted script.
The important property is not automation itself.
It is:
SELECTION FUNCTION DOES NOT READ FORBIDDEN OUTCOME INFORMATION.
8. Rec9 / DAX natural donor
The DAX prospective discriminator freeze episode gives a direct project example.
Initial HUST <-> Front B pair selection was not sufficient merely because the pair was plausible.
Rec9 required:
a case-selection census over the full eligible candidate family;
pre-resolution metadata only;
a frozen mechanical ranking rule;
and an isolated census executor.
DAX later correctly retyped its own reproduced pair as:
NONBLIND PROTOCOL CHECK ONLY,
because DAX was outcome-exposed.
Therefore:
SAME PAIR RESULT
!=
SAME EVIDENCE TYPE.
The provenance of the selection process matters even when the selected pair is unchanged.
9. Selection provenance minimum
When selection itself is claim-bearing, record conceptually:
UNIVERSE:
what cases could have been selected?
CUTOFF:
what information time boundary defined eligibility?
ELIGIBILITY:
what hard inclusion/exclusion rules applied?
ALLOWED METADATA:
what fields could the selector see?
FORBIDDEN INFORMATION:
what outcomes/dispositions were unavailable by design?
SELECTOR STATE:
fresh / exposed / role-native / automated / other.
SELECTION RULE:
ranking, sampling, adversarial stress rule, coverage rule, or deterministic filter.
TIE BREAK:
how equal candidates were resolved.
SELECTED SET:
what entered the experiment.
EXCLUDED SET:
what remained eligible but unselected, where relevant.
COMMIT:
hash/timestamp/version of rule and selected set before execution.
CLAIM TARGET:
selected stratum, eligible universe, worst-case family, or other declared estimand.
This is not a mandatory schema for ordinary work.
It is needed when selection supports the interpretation.
10. Selection completeness
A provenance ledger can list every selected item perfectly
while remaining selection-incomplete.
Example:
Selected cases:
A, B, C.
Source provenance:
complete.
But unknown:
whether D through Z were eligible;
whether A-C were chosen because they were known successes;
whether a failed case was silently excluded;
whether the ranking rule changed after seeing outcomes.
Thus:
ITEM-LEVEL PROVENANCE
does not identify
SELECTION MECHANISM.
Selection completeness requires enough information to reconstruct
how the observed set arose from the eligible universe.
11. Selection leakage classes
SL1 OUTCOME-DIRECT
selector sees explicit target result.
SL2 DISPOSITION LEAK
selector sees owner/referee PASS/FAIL labels.
SL3 PROXY LEAK
metadata such as filenames, branch names, version labels or narrative hints encode outcome.
SL4 POST-RESOLUTION FEATURES
selection uses features created only after the case was solved.
SL5 SURVIVOR FILTER
failed or awkward cases disappear before universe freeze.
SL6 ADAPTIVE RULE DRIFT
eligibility/ranking changes after partial outcomes are known.
SL7 CURATOR MEMORY
selector has prior project memory that effectively contains the answer even when the formal fields are sanitized.
SL8 GOLD-COUPLED SELECTION
cases are chosen because their adjudication truth is unusually easy or favorable.
SL9 TOOL-ASYMMETRY SELECTION
cases are included/excluded based on which arm can access a supporting tool, breaking comparability.
SL10 CLAIM-DRIFT
selected sample is narrow but final claim silently expands to the full universe.
These are failure modes, not assertions that every instance is present.
12. Selection and independence are orthogonal
A run can have:
clean selection + contaminated executor;
contaminated selection + clean executor;
both clean;
or both contaminated.
Therefore:
SELECTION INDEPENDENCE
and
EXECUTOR INDEPENDENCE
must be typed separately.
This also means:
fixing one does not repair the other.
A fresh executor cannot rescue outcome-informed curation.
A clean selector cannot rescue a solver who already knows the answer.
13. Selection and currentness
Currentness creates a subtle tradeoff.
Using the newest project state can improve scientific relevance.
But if the latest state contains:
owner outcomes;
referee dispositions;
known failures;
post-resolution rankings,
it can contaminate an independence-sensitive selector.
Therefore:
CURRENTNESS FOR SCIENCE
and
CURRENTNESS FOR BLIND SELECTION
may require different views.
The correct control is not:
use stale information blindly.
It is:
use the newest legally allowed PRE-RESOLUTION metadata for the selection claim.
Thus:
CURRENTNESS
IS VIEW-RELATIVE.
14. Selection and H1 trace architecture
A shared trace system naturally surfaces:
popular;
central;
recent;
high-salience;
heavily linked objects.
That is useful for coordination.
But default salience ranking is itself a selection mechanism.
If independent lanes consume only the highest-salience shared traces,
the system may silently synchronize around the same conceptual attractors.
Therefore:
TRACE RETRIEVAL POLICY
IS PART OF THE EPISTEMIC ENVIRONMENT.
H1 should distinguish:
trace storage;
trace visibility;
trace ranking;
trace consumption.
A shared blackboard can remain diverse in storage
while producing monoculture through uniform retrieval.
15. Selection and H3 developmental phenotype
H3 cognitive polyphenism depends on developmental ecology.
What a developing lane is shown,
withheld,
prioritized,
and repeatedly sampled
is part of that ecology.
Therefore:
SELECTION POLICY
can act as
DEVELOPMENTAL PRESSURE.
Two nominally identical seeds with different information diets
may develop different representation/search phenotypes.
This gives a deeper architectural interpretation:
EXPOSURE is not only contamination risk.
It is also a developmental intervention.
But:
different information diets
!=
causal polyphenism
without matched controls.
16. Selection and H4 succession
Succession packets are curated states.
Their content is selected from a much larger project history.
Thus succession quality depends on two different properties:
HEREDITARY SUFFICIENCY:
does the packet preserve function?
SELECTION DISCIPLINE:
was the inherited state chosen in a way compatible with the successor's intended future role?
A packet optimized for continuity may include consensus-heavy state.
A packet optimized for protected reconstruction may intentionally omit answer-bearing material.
Therefore:
SUCCESSION PACKET
IS A SELECTION OPERATOR OVER HISTORY.
This makes packet construction part of machine-native heredity design.
17. Selection and H5 representation
Selection occurs not only over cases,
but over representations.
A system chooses:
which summary;
which coordinate;
which theorem;
which source;
which feature;
which failure witness
enters active cognition.
Therefore representation navigation itself contains a selection policy.
H5 already distinguishes:
sufficiency;
admissibility;
selection.
The present result adds:
selection policy needs provenance
when downstream evidential claims depend on how R was chosen.
Thus:
REPRESENTATION SELECTED AFTER SEEING TARGET FAILURE
!=
PREDECLARED REPRESENTATION POLICY.
Both may be scientifically useful.
They answer different causal questions.
18. Selection and target transportability
DRAFT015 correctly separates:
TARGET TRANSPORTABILITY
from
GLOBAL SHARED REALIZATION.
The analogous selection lesson is:
SELECTED-SET VALIDITY
does not automatically transport
to a larger target universe.
For transport from selected set A to target universe B,
one needs a legal bridge.
Depending on the setting this may be:
shared mechanism/invariant;
known sampling design;
reweighting;
support coverage;
stratified claim;
worst-case construction;
or explicit no-transport ceiling.
Therefore:
NO SELECTION-TRANSPORT CERTIFICATE
=>
CLAIM STAYS ON SELECTED STRATUM.
19. Epistemic selection pressure
A multi-agent scientific system has at least two kinds of selection:
BIOLOGICAL/EVOLUTIONARY ANALOGUE:
which lineages survive, branch or receive resources.
INFORMATIONAL:
which evidence, traces, cases and representations each lineage encounters.
The second can shape the first.
If one shared ranking policy determines everyone's information diet,
functional diversity may persist while search-basin diversity collapses.
Therefore anti-monoculture architecture should preserve not only:
multiple lineages,
but some diversity in legal selection/retrieval policies
when decision-relevant.
Guard:
RANDOMIZATION != DIVERSITY AUTOMATICALLY.
The target is materially distinct search exposure,
not noise for its own sake.
20. Epistemic supply-chain certificate
For a high-value prospective or independent claim,
a compact end-to-end certificate can now be decomposed into:
A. SOURCE
origin/authenticity of candidate inputs.
B. UNIVERSE
what could legally enter selection.
C. SELECTION
eligibility/ranking/sampling and selector exposure.
D. TRANSFORMATION
sanitization, masking, aliases, compression.
E. DELIVERY
protected/open routing.
F. EXECUTION
context/memory/tool exposure.
G. OUTPUT COMMIT
freeze before reveal.
H. GOLD / SCORING
truth construction and adjudicator independence.
I. REVEAL / INTEGRATION
when cross-exposure occurred.
This is the EPISTEMIC SUPPLY CHAIN.
The chain is claim-relative.
Normal collaborative work does not require maximal isolation at every stage.
21. Failure localization
A valuable consequence of the supply-chain view is that a failed independence claim can be localized.
Examples:
source contamination;
universe truncation;
outcome-informed selection;
metadata leak during masking;
open-channel delivery;
executor memory leak;
post-hoc output mutation;
gold contamination;
premature reveal.
This avoids the unhelpful binary:
INDEPENDENT / NOT INDEPENDENT.
Instead:
the intended evidence type fails at a specific stage,
while other scientific value may survive.
22. Salvage rules
If selection is outcome-informed but executor is clean:
retain:
blind solution to selected cases.
Do not claim:
outcome-blind case sampling;
representative universe performance.
If selection is clean but executor contaminated:
retain:
post-exposure specialist/referee result.
Do not claim:
fresh independent reconstruction.
If source and selection are clean but gold is contaminated:
retain:
arm outputs.
Do not claim:
clean comparative score until gold is repaired.
General rule:
DEGRADE THE CLAIM AT THE FAILED STAGE,
NOT THE ENTIRE SCIENTIFIC OBJECT.
23. Current programme implications
For LT3 DRAFT015:
PROVENANCE COMPLETE != SELECTION COMPLETE
is confirmed as a load-bearing compiler distinction.
For future compiler utility tests:
pre-resolution universe and selection rules must be frozen before arm execution if results are to generalize beyond handpicked cases.
For heterogeneity reserve:
the reserve includes not only unexposed agents/lineages,
but also unused candidate cases and unspent selection options.
For H1/H3/H4/H5:
selection/retrieval policy becomes a common cross-cutting architecture variable.
This is methodological integration,
not a new scientific law.
24. Current evidence ceiling
Supported strongly by current project-method evidence:
outcome-blind executor does not guarantee outcome-blind selection;
selection provenance can change evidence type even when selected cases are identical;
case-selection universe/rule/cutoff are load-bearing for prospective comparison;
shared-trace retrieval policy can act as an implicit selection mechanism;
succession packets are curated hereditary states;
selection and exposure failures can be localized and claims retyped.
Supported by mature external/statistical host structure in general form:
selected-sample performance does not automatically generalize to a larger target population;
selection mechanisms and transport assumptions matter.
Not established:
optimal selection policy for IW;
causal anti-monoculture benefit of diversified retrieval;
optimal balance between representative and adversarial case selection;
automatic detection of proxy leakage;
causal developmental effect of information-diet differences;
a universal scalar selection-quality score.
25. Disposition
SELECTION PROVENANCE is promoted to:
LOAD-BEARING EXTENSION OF
INDEPENDENCE-PRESERVING DEPLOYABILITY
+
HETEROGENEITY RESERVE
+
COGNITIVE FACTORISATION.
Strongest statement:
A CLEAN EXECUTOR CANNOT MAKE AN OUTCOME-INFORMED SELECTION PROCESS INDEPENDENT.
And:
PROVENANCE OF ITEMS
IS NOT
PROVENANCE OF WHY THOSE ITEMS WERE CHOSEN.
Machine-native research systems should therefore treat
selection/retrieval policy
as part of the scientific architecture when it affects evidential claims.
No new scientific front is opened.
No experiment is claimed executed beyond existing natural project evidence.
No new task is issued.
26. Guards
SOURCE_PROVENANCE_COMPLETE != SELECTION_PROVENANCE_COMPLETE.
SELECTION_PROVENANCE_COMPLETE != EXPOSURE_PROVENANCE_COMPLETE.
BLIND_EXECUTOR != OUTCOME_BLIND_SELECTION.
PURPOSIVE_SELECTION != INVALID_SELECTION.
PURPOSIVE_SELECTION_REQUIRES_PURPOSIVE_CLAIM_TYPING.
SAME_SELECTED_PAIR != SAME_EVIDENCE_TYPE.
CURRENTNESS != BLIND_SELECTION_LEGALITY.
TRACE_VISIBILITY != TRACE_SELECTION_NEUTRALITY.
SUCCESSION_PACKET != UNCURATED_HISTORY.
REPRESENTATION_POLICY != PREDECLARED_REPRESENTATION_POLICY.
SELECTED_SET_VALIDITY != TARGET_UNIVERSE_VALIDITY.
RANDOMIZATION != DIVERSITY_AUTOMATICALLY.
DEGRADE_CLAIM_AT_FAILED_STAGE != DISCARD_ALL_SCIENTIFIC_VALUE.
NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE / NO NEW TASKS / METHOD MUST BE ALLOWED TO FAIL.
