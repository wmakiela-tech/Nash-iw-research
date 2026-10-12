---
artifact_id: M12-DRAFT013-JOINT-SOURCE-ADMISSION-COMMON-WORLD-GATE-001
bw_ingestion_event_id: ING-20261010-0092
bw_qualification_state: JOINT_SOURCE_COMMON_WORLD_GATE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-DRAFT013-JOINT-SOURCE-ADMISSION-COMMON-WORLD-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - DRAFT013 joint source admission: common-world gate
RESULT_CLASS
EXACT LOCAL CONTROL / SOURCE_NATIVE_ADMISSION_AND_PROVENANCE / NO NOVELTY CLAIM
PURPOSE
Test whether individually admitted source constraints may be combined by naive set intersection, or whether one common source world/completion is required.
SETUP
Let X be the scientific candidate space.
For each source i, let S_i be its source-state space and:
pi_i:S_i->X
map a source state to the scientific candidate it supports.
The marginal source-supported candidate set is:
C_i
=
pi_i(S_i).
Let Gamma be the declared compatibility relation among source states:
Gamma subset product_i S_i.
Gamma encodes shared regime, shared nuisance, common calibration, common physical realization, or any other load-bearing source-level compatibility.
Define the legally jointly supported set:
J
=
{x in X:
 there exists (s_1,...,s_m) in Gamma
 with pi_i(s_i)=x for every i}.
CERTIFICATE A - EXACT INCLUSION
Always:
J
subseteq
intersection_i C_i.
Reason:
a common compatible witness supplies an individual witness for every marginal source.
Therefore naive set intersection is at best an outer approximation to joint source admission.
CERTIFICATE B - STRICTNESS CAN OCCUR
The inclusion can be strict.
Exact toy:
X={theta0}.
Source 1 has one state:
s1=(theta0,k=0).
Source 2 has one state:
s2=(theta0,k=1).
Both marginal candidate sets are:
C_1=C_2={theta0}.
So:
C_1 intersection C_2={theta0}.
But suppose the scientific claim requires one shared calibration state k.
Then Gamma allows only tuples with matching k.
The only available pair has k=0 versus k=1,
so no compatible tuple exists.
Thus:
J=empty
while:
C_1 intersection C_2={theta0}.
Therefore:
NONEMPTY MARGINAL INTERSECTION
DOES NOT IMPLY
ONE LEGAL COMMON SOURCE WORLD.
CERTIFICATE C - EXACT EQUALITY CONDITION
Naive intersection is legally exact iff every x in the marginal intersection admits at least one compatible source tuple:
for every x in intersection_i C_i,
there exists (s_i) in Gamma
such that
pi_i(s_i)=x
for all i.
This is the exact common-witness condition.
CERTIFICATE D - SOURCE-SUPPORTED INDIVIDUALLY != JOINTLY ADMISSIBLE
Each source may be:
- genuine;
- independently validated;
- source-supported in its own regime.
Still, the combined claim can be illegal if the sources cannot coexist under one declared completion.
Therefore:
INDIVIDUAL SOURCE VALIDITY
!=
JOINT SOURCE ADMISSION.
This is orthogonal to whether either source is "wrong."
CERTIFICATE E - SHARED NUISANCE
Suppose source i depends on nuisance eta:
R_i subset X x E.
Marginalizing nuisance gives:
C_i
=
{x:
 exists eta_i with (x,eta_i) in R_i}.
If the scientific claim requires one globally shared eta,
the legal combined set is:
J_shared
=
{x:
 exists eta such that
 (x,eta) in R_i
 for all i}.
In general:
J_shared
subseteq
intersection_i C_i,
with strict inclusion possible.
Thus:
PROFILING EACH SOURCE SEPARATELY
!=
ONE SHARED-NUISANCE REALIZATION.
CERTIFICATE F - REGIME COMPATIBILITY
The same issue occurs for:
- temperature/background regime;
- apparatus configuration;
- cosmological history;
- calibration state;
- model version;
- physical boundary.
If different sources are valid only in mutually exclusive regimes, intersecting their candidate sets can fabricate a claim that no single physical realization supports.
CERTIFICATE G - RELATION TO EVIDENCE DEPENDENCE
Dependence and common-world compatibility are different.
Two sources may be statistically independent but physically incompatible across regimes.
Two sources may be statistically dependent yet physically compatible in one world.
Therefore:
SOURCE DEPENDENCE
!=
SOURCE COMPATIBILITY.
Both may be load-bearing.
CERTIFICATE H - PAIRWISE COMPATIBILITY GUARD
For three or more sources, pairwise compatible source states need not admit one global tuple.
So:
PAIRWISE SOURCE COMPATIBILITY
!=
GLOBAL JOINT SOURCE ADMISSION.
This is the same local-to-global common-witness phenomenon already seen elsewhere in IW, now applied claim-locally to source provenance.
CERTIFICATE I - PROVENANCE CONTRACT REQUIREMENT
A source contract adequate for multi-source claims should preserve:
1 source identity/type;
2 mathematical constraint;
3 source regime/domain;
4 shared/local nuisance status;
5 compatibility/common-world relation;
6 dependence structure if evidential weight matters;
7 target.
Dropping item 5 can make an illegal source fusion look mathematically consistent.
CERTIFICATE J - EMPTY JOINT SET
If:
J=empty,
the correct status is:
JOINT SOURCE ADMISSION CONFLICT.
This does not by itself prove:
- which source is wrong;
- which regime should be preferred;
- the model is false.
It proves only that the declared combined one-world claim has no legal common source witness.
PROGRAMME CONSEQUENCE
The current DRAFT013 residual decomposes further:
A PROVENANCE TYPE
Why is a constraint admitted?
B EVIDENCE STRUCTURE
How are sources statistically related?
C COMMON-WORLD COMPATIBILITY
Can all source records support one declared scientific realization?
All three are source-contract semantics.
The generic mathematics is mature:
relational joins / fiber products / shared-nuisance consistency / common-witness feasibility.
PROJECT ROLE:
SOURCE-CONTRACT LEGALITY COMPILER RULE.
ARCHITECTURE PRESSURE
This third control reinforces:
GENERIC SOURCE_NATIVE_ADMISSION_AND_PROVENANCE
is strongly absorbable at the explicit source-contract level.
A true programme residual would require an existing source-native front where:
- provenance type is explicit;
- dependence is explicit;
- compatibility/common-world relation is explicit;
- target is explicit;
and yet the admission verdict still requires a nonreconstructible theorem/non-map.
No such surplus is established here.
CHEAPEST FALSIFIER
For any multi-source claim:
freeze source states and compatibility relation,
then ask whether every candidate in the naive intersection has one compatible source tuple.
If not:
naive fusion fails before downstream inference.
FIREWALL
INDIVIDUAL SOURCE VALIDITY != JOINT SOURCE ADMISSION.
NONEMPTY SET INTERSECTION != COMMON WORLD.
SHARED-NUISANCE PROFILING != SEPARATE NUISANCE PROFILING.
SOURCE DEPENDENCE != SOURCE COMPATIBILITY.
PAIRWISE COMPATIBILITY != GLOBAL COMPATIBILITY.
EMPTY JOINT SET != UNIQUE BLAME.
DISPOSITION
GENERIC SCIENTIFIC_SURPLUS=NONE.
TRUE_SURPLUS=NONE established.
SOURCE_NATIVE residual narrows to project-specific contract construction/admission.
P3 pressure increases further.
No P3 promotion.
REV020 ACTIVE / TPE HOLD / REV021 NOT CREATED.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SUBTRACTION_FIRST / SCIENCE_FIRST.
