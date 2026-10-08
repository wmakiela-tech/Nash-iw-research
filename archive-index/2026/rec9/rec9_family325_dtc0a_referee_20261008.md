# REC9 Family325 DTC0a referee 001

RETURN_ID: REC9-FAMILY325-DTC0A-DIRECT-HOST-KILL-REFEREE-001
TARGET: PRF10-FAMILY325-DTC0A-KA-DIRECT-HOST-KILL-TEST-001
VERDICT: PASS_WITH_TARGET_RELATIVE_AND_PROVENANCE_REPAIR

Independent reproduction on mounted deepseek_python_20260627_a87249.py matched PRF10 exactly.

N31 alpha 0.00:
K_A=3.788529759260593e-05
A1/A2/Ab relative commutator witnesses =
0.9296149138353976 / 0.7609232056959795 / 0.7592552579548470

N31 alpha 0.05:
K_A=3.7647568532083594e-05
0.9273996365069088 / 0.7537618969932255 / 0.7541063937992870

N31 alpha 0.20:
K_A=3.694723525796834e-05
0.9195072631917873 / 0.7316659144991435 / 0.7345909436269434

N35 alpha 0.05:
K_A=3.796625718750918e-05
0.9288411775631580 / 0.7595339412107236 / 0.7567582962954098

N41 alpha 0.05:
K_A=3.837256295424906e-05
0.9302496383331802 / 0.7656857971363383 / 0.7593919236843094

FULL-OPERATOR RESULT:
M=f(A) implies [A,M]=0.
Thus full-operator identities M_A=f(A1), f(A2), f(Ab) are numerically rejected for the tested finite configurations.

CRITICAL TARGET-RELATIVE GUARD:
Full-operator noncommutation does NOT kill a weaker source/readout identity
Q M_A L = Q f(A)L.
For a frozen target, test
Q M_A L in span{QL,QAL,...,QA^(d-1)L}.
Therefore:
FULL_OPERATOR_DIRECT_F325 = NUMERICALLY_KILLED_ON_TESTED_CONFIGURATIONS.
TARGET_RELATIVE_DIRECT_F325 = UNRESOLVED / NOT TESTED.

NUMERICAL CEILING:
This is robust floating-point exclusion on tested configurations, not an exact symbolic proof for every N, alpha, stencil, field or future DTC variant.

PROVENANCE:
The exact frozen dtc0a_runtime_v0_3_1.py was not mounted.
The verification source reproduces frozen K_A outputs exactly and Rec9 reproduced PRF10 witnesses from it.
Status:
VERIFICATION_SOURCE_CONSISTENCY=STRONG.
FROZEN_RUNTIME_BYTE_IDENTITY=NOT_ESTABLISHED.

BLOCK LANE:
LEGAL_CANDIDATE / UTILITY_UNPROVEN.
Exact block embedding does not imply useful Crouzeix certificate.

E_lin:
ABSORBED_BY_SELFADJOINT_SPECTRAL_CALCULUS.

NO K/J3 invariant.
NO physical interpretation.
NO continuum upgrade.
NO REV021/theory promotion.
NO novelty inference.
NO new task.
