# M14 ROT006 — independent numerical/falsifier return
artifact_id: IW_M14_ROT006_XH4_YUKAWA_NUMERICAL_CONTROL_001_20261026
exposure: PUBLIC
claim_ceiling: SYNTHETIC_POINT_SOURCE_NUMERIC_CHECK / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
parent: research/m14/2026-10-26/iw_m14_rot006_yukawa_three_distance_exact_inverse_001.md

SYNTHETIC distances in mm: [0.654,1.054,1.554,1.304]. First/third are endpoints of XH-S4/028's REPORTED experimental distance range, NOT point-source physical data; second and fourth are chosen purely for synthetic tests. Gain A=1.3, alpha=.4, lambda=1mm. NORMALIZED dimensionless observations: [1.747208714374402,1.672269451135643,1.5807570119780743,1.6252114396755761].

Three-distance difference ratio .8188970147514729; limit ratio as nu->0: .523926380368098. Inverse recovers A=1.3000000000000007, alpha=.39999999999999936, lambda=.9999999999999987mm. Fourth synthetic holdout predicts 1.6252114396755761 (error <1e-12).

For observed z_i with |e_i|<=eta=.001 and positive d12=z1-z2,d23=z2-z3 > 2eta, OUTER ratio interval:
[(d12-2eta)/(d23+2eta),(d12+2eta)/(d23-2eta)].
Via monotone Phi inverse: lambda outer [0.9013283524165352,1.1233437309099177]mm. These are assumed MODEL noise units, NOT experimental uncertainty.

Seven nu grid checks 0.15,.35,.7,1,1.7,3,6: h-difference integral vs independent Simpson <=3e-13, log derivative as DIFFERENCE of two weighted means strictly >0, derivative versus central difference <=2e-8. Alpha=0 null branch gives identical y under any lambda. Test script: verify_m14_rot006_yukawa_three_distance.py and machine JSON in Moderator-local complete source bundle. SCRIPT PASS; not a theorem prover.

Original XH-S4/028 source contains REAL finite wafers; this toy does NOT generate G, gravity quantization or physical NASH J3/K claims. Owner/referee/BW not verified.
