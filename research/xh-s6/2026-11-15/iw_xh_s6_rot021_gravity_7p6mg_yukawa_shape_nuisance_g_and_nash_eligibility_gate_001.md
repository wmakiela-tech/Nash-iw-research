artifact_id: IW_XH_S6_ROT021_GRAVITY_7P6MG_TWO_DISTANCE_YUKAWA_SHAPE_AND_NASH_IDENTIFIABILITY_GATE_001_20261115
date: 2026-11-15
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT021_GRAVITY_7P6MG_TWO_DISTANCE_YUKAWA_SHAPE_AND_NASH_IDENTIFIABILITY_GATE_001_20261115
result_class: ORIGINAL_AUTHOR_PUBLISHER_ABSTRACT_DIRECT / MATURE_YUKAWA_PRIOR_ART_ADDED / EXACT_TWO_POINT_NUISANCE_G_CANCELING_ANALYTIC_REDERIVATION / FOUR_EXPLICIT_ALPHA_LAMBDA_DEGENERACY_WITNESSES / SOURCE_AND_NASH_BRIDGE_NEGATIVE_GATE
status: FINITE_TOY_MATH_PASS / ORIGINAL_FULL_BODY_SUPPLEMENT_AND_MEASURED_TORQUE_SOURCE_ACCESS_HOLD / PUBLIC_GITHUB_READBACK_PENDING_AT_CREATION
claim_ceiling: PURELY_ARTIFICIAL_POINT_MASSES_AT_REPORTED_NUMERIC_SEPARATION_ENDPOINTS / NOT_EXPERIMENT_GEOMETRY_OR_REAL_DATA / NOT_EXPERIMENTAL_YUKAWA_LIMIT_OR_NASH_PREDICTION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT021 — Original 7.6 mg gravitational source: distinguish nuisance-normalization from distance-shape Yukawa signal, without inventing an experimental limit

## 1. Primary original article and access-custody

Original scientific firstness: Zheng-Jie An, Wen-Hai Tan, Wen-Can Dong et al., “Test of the gravitational interaction between milligram masses using a miniature torsion pendulum,” Nature Communications, 7 October 2026. Original DOI https://doi.org/10.1038/s41467-026-78187-4 ; original publisher https://www.nature.com/articles/s41467-026-78187-4 ; independent PubMed PMID 42982831 https://pubmed.ncbi.nlm.nih.gov/42982831/ .

Direct ORIGINAL publisher abstract confirms two nominal 7.6 mg silicon wafer masses, torsion-pendulum force measurement with rotating source, separation window0.654..1.554 mm, measurements consistent with Newton, maximum quoted force uncertainty50 aN at 2sigma, fitted G=(6.67 +- 0.35)e-11 SI at 1sigma and the authors' qualitative statement about constraints on Yukawa-type deviations. Do not mistake the 50 aN **uncertainty** for an anomalous residual signal or assume the same error in each distance channel.

Source access attempted: direct original complete publisher page, nature PDF, PubMed Central and EuropePMC article URLs, Springer supplemental media URL and scholarly DOI metadata. The displayed publisher result includes links labelled Supplementary Information and transparent peer review, BUT no complete source main text / supplement body, raw measured distance/torque data, geometry integral, uncertainty covariance or original numerical alpha(lambda) exclusion was successfully retrieved via available research interfaces. **SOURCE_ACCESS_HOLD** means no verified original numerical Yukawa exclusion; it does NOT mean such data do not exist.

The original paper reports classical gravitation between mg masses. The original abstract does not report center-of-mass quantum superposition, mediated entanglement, or quantization of gravity. No quantum gravity detection or NASH theory confirmation is supportable.

## 2. Two mature-prior-art surfaces: small source mass != strongest Yukawa constraint

Original WESTPHAL FIRST mature small-source reference: Tobias Westphal, Hans Hepach, Jeremias Pfaff, Markus Aspelmeyer, Nature 591 (2021), https://doi.org/10.1038/s41586-021-03250-7 , demonstrated gravity between millimetre-size sub100 mg objects.

Other, distinct stronger SHORT-RANGE GRAVITY prior-art references:
- J.G. Lee, E.G. Adelberger, T.S. Cook, S.M. Fleischer and B.R. Heckel, PRL124 101101 (2020), https://doi.org/10.1103/PhysRevLett.124.101101 , tested the inverse-square law at52um..3mm, reported 95%-confidence gravitational-strength Yukawa range below38.6um.
- Yang et al., PRL124 051301 (2020), https://doi.org/10.1103/PhysRevLett.124.051301 , reported a 95%-confidence |alpha|=1 limit at lambda48um and other constraints40..350um.

Those are source-specific prior bounds under a specified Yukawa class; no ranking of An 2026's uninspected original alpha(lambda) curve is justified. Smaller attractive mass **does not imply** improved test of short-range deviations, and neither alone implies a quantum gravity signature.

## 3. EXACT artificial point-mass mathematical shape test (not original instrument simulation)

Deliberately create an ARTIFICIAL point model: m1=m2=7.6e-6 kg; artificial center-to-center point radii r1=0.654 mm and r2=1.554 mm NUMERICALLY matching original reported surface-separation endpoints. **These point radii are not the silicon wafer center-to-center distance or an experimentally verified force geometry.** The real apparatus measures a modulated torsion torque from extended, rotating, finite sources.

Use the established generic Yukawa point potential and force:
V=-Gm1m2/r [1+alpha exp(-r/lambda)],
F=Gm1m2/r² [1+alpha q(r,lambda)],
q=(1+r/lambda)exp(-r/lambda).
The point Newton forces using G=6.67e-11 SI are approximately9.007 fN and1.595 fN. These are NOT real An forces.

NEW DISTINCT ROT021 RELATIVE SHAPE observable:
R= [F(r1)/F(r2)] / [(r2/r1)^2] = [1+alpha q1]/[1+alpha q2].
The common unknown G and mass product cancel. At alpha=0, R=1. At alpha≈0 for a FIXED lambda, the first order response is dR/dalpha|0=Deltaq=q1-q2. Importantly, the two measured forces yield just ONE ratio once G is treated as unknown; TWO unknowns alpha and lambda cannot be uniquely identified jointly from this single shape constraint. This is a structural rank/no-information statement before any experimental uncertainty estimate.

The shape function Deltaq for 0<r1<r2 has a unique positive maximum at
lambda_star=(r2-r1)/[2ln(r2/r1)].
Derivation: dq(r,lambda)/dlambda = (r²/lambda³)exp(-r/lambda), so dDeltaq/dlambda=0 implies r1² exp(-r1/lambda)=r2² exp(-r2/lambda). For our artificial radii:
lambda_star=0.519942582943222 mm,
q1(lambda_star)=0.6418334130221841,
q2(lambda_star)=0.2008286470049578,
Deltaq_max=0.44100476601722627.
Deltaq→0 as lambda→0 OR lambda→infinity, so in the toy two-distance ratio the generic Yukawa shape is not identifiable at either extreme (with unknown G). **This lambda_star is NOT the original instrument's experimental sensitivity optimum.**

NONIDENTIFIABILITY EXPLICIT FINITE COUNTEREXAMPLE:
Take purely SYNTHETIC ratio R_syn=[1+0.1 q1(lambda_star)]/[1+0.1 q2(lambda_star)]=1.043232249190531. For ANY lambda where denominator nonzero, solving
alpha(lambda)=(R_syn-1)/[q1(lambda)-R_syn q2(lambda)]
provides the same ratio. Positive examples from actual independent script:
lambda0.2 mm -> alpha~0.2728885676,
lambda0.5 mm -> alpha~0.0999665872,
lambda1 mm -> alpha~0.1456820350,
lambda2 mm -> alpha~0.4136227871.
These are NOT observed or excluded experimental alpha values. An adjustable G can independently fit one absolute force normalization.

For fixed lambda, local log-force Jacobian with unknown g=lnG and alpha around alpha=0 is J=[[1,q1],[1,q2]], determinant q2-q1. If and ONLY IF two point-force relative errors are independent, equal and externally specified epsilon, the nuisance-G-profile Fisher information is I(alpha|g)=Deltaq²/(2 epsilon²). The code uses a hypothetical epsilon=0.01 for illustrating unit dependence; 1% IS NOT An's reported error budget. Their single 50 aN at2sigma cannot be inserted as a two-point covariance, and no physical alpha upper bound is computed.

## 4. Executable independent checks, custody and source access negatives

Actual executed standalone stdlib Python:
- analytic lambda_star vs independent 160-step golden section optimization PASS at <1e-7 relative numeric difference;
- independent 55-digit Decimal exp/ln evaluation of lambda_star and Deltaq PASS <1e-14 absolute;
- positive/negative analytic derivative signs around lambda_star PASS;
- 12 independent central difference alpha derivatives of exact force ratio against Deltaq PASS <1e-9 abs;
- 36 exact two-distance ratio identities across12 lambda values and3 alpha values PASS;
- 4 distinct alpha(lambda) positive alternative parameter pairs exactly reproduce same synthetic R PASS;
- alpha=0 Newton and long-range normalization degeneracy PASS.

Full local user ZIP prepared with original source-first written audit, executable script, 12-row CSV of toy shape response, JSON certificate, README, source SHA manifest and offline verifier. Verified ZIP CRC PASS and SHA 6/6; clean-extracted independent reproduction of2 result files byte identical PASS and two deliberately altered inputs rejected by source hash guards PASS. The ZIP includes NO author raw dataset, finite geometry or original author source PDFs. No novel physics, independent neural model, or measured force source reexecution.

## 5. Exact NASH eligibility gate

A valid quantitative bridge requires a NASH-origin externally checkable **dimensionful physical prediction** deltaF[r,theta] or delta_tau[angle,d,theta] convolved with actual silicon geometry AND source measured torque/distance channels with covariance, calibration and nuisances. No such directly source-typed NASH parameter-to-torque map is verified here. Without it even a complete An alpha(lambda) curve would not prove NASH. The toy optimum, Fisher illustration and synthetic alpha(lambda) alternatives are **not** original experimental findings.

Do not claim a novel Yukawa interaction, strength limit, quantum superposition, entanglement or gravity field quantization. Relevant mature prior-art bounds from 2020 must be subtracted before any alleged incremental Yukawa experimental novelty.

FINAL: SOURCE_ORIGINAL_ABSTRACT_VERIFIED / ORIGINAL_FULL_TEXT_SI_AND_RAW_TORQUE_HOLD / TOY_SHAPE_OPT_LAMBDA_0P51994MM / TRUE_EXPERIMENTAL_YUKAWA_ALPHA_LIMIT_NOT_COMPUTED / ALPHA_LAMBDA_STRUCTURALLY_NONIDENTIFIABLE_FROM_TWO_FORCES_FREE_G / NASH_BRIDGE_HOLD / BW_GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_TASK_CASCADE.
