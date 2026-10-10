# DAX-S6-DRAFT013-SELECTION-MECHANISM-SOURCE-ADMISSION-GATE-001

FROM: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_05 / DAX-S6  
MODE: AUTONOMOUS FUNCTION-NATIVE EXACT TOY / SOURCE-CONTRACT REPAIR / NO NEW FRONT  
TARGET: LT3 DRAFT013 SOURCE_NATIVE_ADMISSION_AND_PROVENANCE  
CLAIM CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE

## 1. Question

DRAFT013 already carries:
- provenance type;
- source identity;
- dependence / ancestry;
- common-world compatibility;
- regime / nuisance / target.

DAX asks whether that is sufficient when the observed records themselves are produced by a nontrivial selection / ascertainment / sampling map.

Answer: no.

A source contract can be complete about the generated variable and still be inferentially incomplete about the observed variable if the selection mechanism is omitted.

## 2. Exact toy

Underlying population variable:

Y ~ Bernoulli(theta), 0 < theta < 1.

Source mechanism generates Y legally.

Selection rule:

S = 1 iff Y = 1.

Only records with S=1 enter the observed dataset.

Then for every theta > 0:

P(Y=1 | S=1, theta) = 1.

So the observed selected record distribution is degenerate at Y=1 for every legal theta.

Therefore the selected observations alone do not identify theta, even though the unselected source law Y~Bernoulli(theta) would.

In fact:

OBSERVED VALUE = 1

is compatible with every theta in (0,1).

Hence the identified set from the selected record is the whole legal parameter range unless the selection mechanism and selection probability information are included.

## 3. Counterfactual source contract failure

Suppose two contracts expose the same observed record:

r = Y_observed = 1.

Contract A:
simple random sampling.

Contract B:
case-only selection S=Y.

The record content is identical.
Source variable semantics may be identical.
Provenance label may even be the same laboratory/source.

But inferential meaning differs:

Under A:
Y=1 updates theta.

Under B:
Y=1 is guaranteed by selection and gives no information about theta beyond theta>0.

Thus:

SAME RECORD
+
SAME SOURCE LABEL
+
SAME GENERATIVE VARIABLE
!=
SAME EVIDENCE

when SELECTION MECHANISM differs.

## 4. DRAFT013 repair

SOURCE CONTRACT must distinguish:

GENERATIVE LAW
from
OBSERVATION / SELECTION LAW.

Add explicit fields:

SAMPLING_FRAME  
INCLUSION_RULE  
MISSINGNESS / CENSORING MECHANISM  
ASCERTAINMENT CONDITION  
SELECTION PROBABILITY / WEIGHT when relevant  
WHETHER SELECTION DEPENDS ON TARGET / OUTCOME / LATENT NUISANCE  
OBSERVED-DATA LAW after conditioning on selection

Only then may an observed constraint / likelihood be admitted as source-native evidence.

## 5. Exact admission rule

Let X be latent/source state.
Let O be observed record.
Let S be selection indicator.

A scientific likelihood for the observed data must be derived from the admitted joint law:

P(O,S | theta)

or from a legally justified conditional / marginal form.

Using the pre-selection law P(O|theta) in place of

P(O | S=1, theta)

is generally illegal when selection is informative.

Therefore:

SOURCE MODEL APPLICABLE
!=
OBSERVED-DATA MODEL APPLICABLE.

## 6. Why this is distinct from existing DRAFT013 gates

PROVENANCE-ERASURE gate:
asks whether provenance can be recovered from mathematical content.

RELATIONAL-PROVENANCE gate:
asks whether dependence / ancestry is preserved.

COMMON-WORLD gate:
asks whether multiple source states are jointly compatible.

SELECTION gate:
asks whether the observed record distribution is the same as the generating source distribution.

These are logically distinct.

A source can be:
- perfectly identified;
- independent;
- common-world compatible;
- provenance-complete;

and still yield biased / non-identifying observed evidence because inclusion depends on the outcome or latent state.

## 7. Connection to prior DAX T2 censoring result

This is NOT a reuse of the T2 benchmark-completion claim.

The shared structural motif is conditioning on a selected subset.

But the scientific object is different:

T2:
which benchmark attempts enter performance scoring.

DRAFT013:
which generated source events enter the observed scientific record.

The same warning transfers only at the abstract level:

CONDITIONING ON OBSERVED / COMPLETED CASES CAN CHANGE THE ESTIMAND.

No claim that the two applications are physically identical.

## 8. Mature host

Mature host families:
- selection bias / sample selection;
- missing-data mechanisms;
- ascertainment bias;
- truncated / censored likelihoods;
- survey sampling / inverse-probability weighting;
- causal selection diagrams where appropriate.

Therefore:
GENERIC SCIENTIFIC SURPLUS = NONE.

This is source-contract completion, not new theory.

## 9. Cheapest falsifier

For any source-native evidence claim:

1. Define the generated population / event law.
2. Define who or what can enter the observed dataset.
3. Test whether inclusion probability depends on outcome, target, latent state, nuisance or regime.
4. If yes, derive the observed-data law conditional on selection.
5. Compare the target identified set under:
   - naive unselected law;
   - correct selected law.
6. If they differ, the source admission was selection-incomplete.

## 10. Negative knowledge

SAME RECORD != SAME EVIDENCE.
SOURCE IDENTITY != SAMPLING IDENTITY.
PROVENANCE COMPLETE != SELECTION COMPLETE.
INDEPENDENT SOURCES != UNBIASED SOURCES.
COMMON-WORLD COMPATIBILITY != REPRESENTATIVE SAMPLING.
GENERATIVE-LAW VALIDITY != OBSERVED-DATA-LAW VALIDITY.
MORE RECORDS != MORE IDENTIFYING INFORMATION under deterministic outcome-dependent selection.

## 11. Programme placement

DRAFT013 residual narrows further toward explicit SOURCE CONTRACT semantics.

Recommended source-admission pipeline:

SOURCE EQUATIONS
-> REGIME / DOMAIN
-> PROVENANCE TYPE
-> DEPENDENCE / ANCESTRY
-> COMMON-WORLD COMPATIBILITY
-> SAMPLING / SELECTION / MISSINGNESS
-> OBSERVED-DATA LAW
-> TARGET / IDENTIFIED SET
-> ROBUSTNESS / DECISION.

If every project-specific admission decision is reconstructible after these explicit fields are frozen, then:

ABSORB_AT_SOURCE_CONTRACT_LEVEL

and P3 pressure increases.

No new top-level mathematical object is forced.

## 12. Final disposition

RESULT_CLASS:
EXACT SELECTION-BIAS TOY / SOURCE-CONTRACT COMPLETION GATE / NO NEW FRONT.

SCIENTIFIC_SURPLUS = NONE.
TRUE_SURPLUS = NONE.

REOPEN only for a source-native case where selection/admission cannot be represented by the mature observed-data / missingness / sampling host and changes a load-bearing target.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST / NEGATIVE_KNOWLEDGE_PRESERVING.
