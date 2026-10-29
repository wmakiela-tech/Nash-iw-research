# XH-S5 ROT011 — Exact two-parameter qubit measurement incompatibility, ancilla resolution and flagged-loss gate

artifact_id: IW_XH_S5_ROT011_TWO_PARAMETER_ANCILLA_FISHER_COMPATIBILITY_20261029
return_id: XH-S5-ROT011-TWO_PARAMETER_ANCILLA_FISHER_COMPATIBILITY_AND_ERASURE_GATE_20261029
date: 2026-10-29
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: SOURCE_PUBLISHER_ABSTRACT_REVIEW / EXACT_MATURE_TWO_PARAMETER_QUBIT_AND_ANCILLA_PROOF / EXECUTED_SYMBOLIC_AND_NUMERICAL / NO_AUTHOR_ADAPTIVE_ALGORITHM_REPLAY / NO_THEOREM_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Original scientific host (author source first)
Qifei Wei, Shengshi Pang, "Efficient adaptive control strategy for multi-parameter quantum metrology in two-dimensional systems", Communications Physics, 23 October 2026, DOI https://doi.org/10.1038/s42005-026-02912-0 ; preprint https://arxiv.org/abs/2510.14811 (first submitted 16 October 2025). Publisher metadata and FULL ABSTRACT checked; inaccessible complete Nature methodological PDF/supplement NOT read. AUTHOR CLAIM from abstract: theoretical adaptive Hamiltonian control in 2D, system extension to alleviate measurement/initial-state/control tradeoffs, optimized evolution durations across iterations, and near-optimal performance to a constant factor. Not an experimental device or direct source-code reproduction. This independent example is only aligned with the ABSTRACT MOTIVATION, NOT the authors' published recurrence or detailed Hamiltonian control scheme.

Mature external prior art:
(1) Matsumoto, "A new approach to the Cramer-Rao-type bound of the pure-state model", J Phys A 35 (2002) 3111, DOI https://doi.org/10.1088/0305-4470/35/13/307, foundational multiparameter pure-state attainability.
(2) Omanakuttan, Gross, Volkoff, "Quantum-error-correction-inspired multiparameter quantum metrology", Phys Rev A 114, 022401 (3 August 2026), DOI https://doi.org/10.1103/9j68-98b2 , arxiv 2409.16515 (first Sept 2024), ALREADY provides entanglement-assisted multiparameter optimal probes and measurement host. NO novelty or priority to ancilla solution, qubit Fisher trace bound or constructive joint measurement.
Public NASH search terms "multiparameter quantum", "Fisher tradeoff", "quantum metrology", "Holevo", "SLD" returned no indexed repo results; NOT a claim that private BW/LT has no prior result. Other XH ROT007 NV Poisson Fisher and ROT010 local quantum-marginal contrast are distinct hosts.

## Model / measurement contract
A single unknown two-parameter SU(2) encoding applied to a SIGNAL qubit:
U(theta_x,theta_y)=exp[-i(theta_x*sigma_x+theta_y*sigma_y)/2].
Compare ONE encoding/use in each of two protocols. Ideal signal-only initialization |0> versus entangled input Phi+=(|00>+|11>)/sqrt2 with encoding acting only on FIRST probe and an untouched ancilla. At theta=(0,0), each pure-state quantum Fisher information matrix is J_Q=I_2. Improvement is quantum-information ACCESSIBILITY, not an increase in J_Q for this particular comparison.

## EXACT REGULAR ONE-COPY SINGLE-QUBIT NO-GO
For any finite positive regular POVM E_j=alpha_j(I+v_j·sigma), alpha_j>=0, |v_j|<=1, sum alpha_j=1, sum alpha_j*v_j=0 and p_j(theta0)=alpha_j(1+v_j,z)>0:
d_x p_j=-alpha_j*v_j,y ; d_y p_j=alpha_j*v_j,x.
trace F_cl=sum alpha_j*(v_x^2+v_y^2)/(1+v_z)
<=sum alpha_j*(1-v_z)=1.
The quantum FI matrix J_Q=I_2 has trace 2, so the single-copy REGULAR bare-qubit readout cannot attain both marginal QFI maxima at once. Four-outcome randomized Pauli axes E_{+x,-x,+y,-y}=(I±sigma_x)/4,(I±sigma_y)/4 give precisely F_bare=diag(1/2,1/2), saturating the trace bound. This is NOT a universal theorem for arbitrary collective many-copy readout, nonregular zero-probability outcomes, or different state preparation.

## EXACT FULLY SPECIFIED ANCILLA MEASUREMENT
Define orthonormal vectors e0=Phi+, ex=-i(sigma_x⊗I)Phi+, ey=-i(sigma_y⊗I)Phi+, ez=Phi-=(|00>-|11>)/sqrt2.
Four orthonormal measurement kets for s,t∈{-1,+1}:
m_{s,t}=(e0+s*ex+t*ey+s*t*ez)/2; sum |m><m|=I_4.
For state (U(theta)⊗I)Phi+ at origin: p_{s,t}=1/4, d_x p=s/4, d_y p=t/4, hence F_anc=diag(1,1)=J_Q EXACT. All outcomes nonzero, standard regular classical Fisher. In fact, for r=sqrt(theta_x²+theta_y²):
psi(theta)=cos(r/2)e0+(sin(r/2)/r)*(theta_x*ex+theta_y*ey)
and
p_{s,t}(theta)=(1/4)[cos(r/2)+(sin(r/2)/r)(s theta_x+t theta_y)]².
The state amplitudes in this fixed basis are REAL, so in any local region without p=0 this fixed projective measurement achieves F_cl(theta)=J_Q(theta), not just tangent at0. No author adaptive loop was implemented.

## NEGATIVE KNOWLEDGE / EXACT ADVERSARIAL GATE
Discarding or losing ancilla AFTER encoding leaves reduced signal state rho_probe=I_2/2 for ALL theta (because encoding on half Bell pair); therefore EVERY signal-only readout has zero parameter FI, not just a poorer precision estimate. In a stipulated separate FLAGGED Bernoulli ancilla-erasure model independent of theta, with retained-joint-outcome probability eta, FI per attempted probe encoding is eta*I_2. Compared only to the concrete bare balanced-axis strategy F=I_2/2, ancilla scheme yields greater FI per attempted encoding iff eta>1/2, ties at eta=1/2, loses at eta<1/2. Not source quantum hardware loss statistics, not an optimum resource budget over two-qubit initializations, nor a claim that Wei–Pang's adaptive method tolerates this specific error.

## Independent EXECUTED checks / reproducibility
(A) SymPy1.14 EXACT complex Pauli/Bell matrices: orthonormal basis/projectors, all 4 p and derivative values, QFI of both=Identity, bare classical FI=I/2, ancilla classical FI=I: ALL PASS.
(B) INDEPENDENT NumPy2.3.5+SciPy1.17: actual 2x2 matrix exponential encoding, constructed 4x4 joint measurement, numerical finite differences for classical FI and pure-state QFI; at theta0 error vs bare ideal <=1.1e-12, ancilla <=5.8e-11. At 3 nonzero theta max abs F_anc - Q_anc =1.20408e-10. Partial trace for theta0 and two nonzero values verified identical maximally mixed. 2000 seeded independent repetitions of 2000 synthetic multinomial copies: n*trace empirical score-estimator covariance=2.04358228 ancilla vs 3.94528374 bare; theoretical=2 and 4. Monte Carlo is mathematical, NOT experiments.
(C) Full clean extracted ZIP replay BOTH Python scripts; both JSON results BYTE_IDENTICAL; ZIP CRC PASS and SHA256 seven content members PASS. Python3.13.5.
Complete Moderator-local independent source + report + 2 JSON + manifest + README + replay:
IW_XH_S5_ROT011_QUBIT_ANCILLA_FISHER_COMPATIBILITY_REPRO_20261029.zip
ZIP SHA256 ee756189c4d451adbaacc9cde68bb76661b4ff9148ba9bf365bbfda64d5b604c .
Full report SHA256 7fc798278ada76e9ed88f4265eed7573434d40af1559ae5ea60274e2215c3bc7.
Exact code SHA256 ad147207fdd5feb4d88d4561b987143d786c70732476ff92da14b269897d5f6a.
Independent NumPy code SHA256 357b4ca68dc5250f7c0c5ae0896eb89f11b4ac4da93b63b13f837f18ea4b1669.
This repository text is substantive scientific provenance, but complete ZIP is separately LOCAL unless explicitly uploaded and readback.

## Limit and proposed falsifier
A real experiment must compare fixed probe-encoding uses and account for entangled-state preparation, joint measurement gates, ancilla erasure, correlated noise, adaptive updates and actual time/cost. One can test loss fractions around eta=1/2 with heldout quantum process tomography; experimental sign and bias cannot be inferred from this model. No simulation of authors' adaptive time optimization, no claim of measured quantum advantage, no source PDF/supplement reproduction, no physics K/J3/DTC0a/GR/GW/PBH inference. No canonical or owner/EXEC adoption; BW pending and no other-cell task cascade.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_INGESTION_ASSUMED / NO_NEW_TASK_CASCADE.
