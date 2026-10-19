# INT7 — FEEC / pseudospectral numerical-stability gate

RETURN_ID: INT7-XH-S4-FEEC-PSEUDOSPECTRAL-DTC-GATE-001_20261019

## Source

Boffi, Hu, Liang, Zerbinati, *Finite element exterior calculus for spectra and pseudospectra of advection-diffusion of differential forms*, arXiv:2610.01501v1 (2026-10-01).

Primary source: https://arxiv.org/abs/2610.01501

## Source-native result

The paper studies non-normal advection-diffusion operators on differential forms with structure-preserving FEEC discretizations based on finite-element de Rham complexes. It uses conforming subcomplexes and bounded cochain projections.

Its general pseudospectral perturbation result states that if bounded operators S and T satisfy eta = ||T-S||, then

sigma_epsilon(T) subset sigma_(epsilon+eta)(S)

and conversely. Hence operator-norm convergence implies pseudospectral convergence. The paper verifies the required convergence for its own FEEC solution operators.

The same paper stresses that eigenvalues alone may miss finite-time transient amplification for non-normal operators and gives an exact 2x2 separator with identical spectra but arbitrarily different transient growth.

## Project placement

### Monograph Chapter 4

Chapter 4 is primarily a self-adjoint Hodge-Laplacian / bounded Borel functional-calculus framework. The FEEC paper does not alter its theorems. It is a mature numerical host for a different question: validation of non-self-adjoint operators built on differential complexes.

### DTC

No current project artifact establishes that DTC satisfies the FEEC hypotheses used in arXiv:2610.01501, nor an operator-norm solution-map convergence or pseudospectral convergence theorem for DTC.

Therefore:

- FEEC_TO_DTC_DIRECT_THEOREM_TRANSFER = REJECT
- FEEC_TO_DTC_VALIDATION_HOST = PASS

## Validation hierarchy

1. algebraic / structure checks;
2. scalar diagnostic convergence;
3. spectral convergence;
4. operator-norm or resolvent control;
5. pseudospectral / transient fidelity.

For non-normal operators:

- LEVEL_2 != LEVEL_4
- LEVEL_1 != LEVEL_3
- STRUCTURE_PRESERVATION != OPERATOR_NORM_CONVERGENCE

## Exact separator

For

A_N = [[lambda,N],[0,lambda]],
B = lambda I,

the spectra are identical, while

exp(t A_N) = exp(lambda t) [[1,Nt],[0,1]],
exp(t B) = exp(lambda t) I.

Finite-time amplification can therefore differ arbitrarily although the spectrum is the same.

## DTC numerical-stability gate

Before any future DTC claim of non-normal operator-level fidelity, require:

1. a declared continuum carrier and discrete carriers with explicit comparison maps;
2. the actual continuum operator or bounded response/solution operator whose convergence is claimed;
3. a structure-preserving map if a differential complex is load-bearing;
4. operator-norm convergence or source-native resolvent control;
5. only then a pseudospectral/transient conclusion.

Scalar K-convergence may remain sufficient for a scalar target, but must not be upgraded into resolvent or transient fidelity.

## Firewalls

FINITE_ELEMENT_DE_RHAM_SUBCOMPLEX != DTC_BY_DEFAULT  
STRUCTURE_PRESERVATION != OPERATOR_NORM_CONVERGENCE  
SPECTRAL_CONVERGENCE != PSEUDOSPECTRAL_CONVERGENCE  
SAME_SPECTRUM != SAME_TRANSIENT_RESPONSE  
SCALAR_K_CONVERGENCE != RESOLVENT_FIDELITY  
PSEUDOSPECTRAL_FIDELITY != PHYSICAL_VALIDATION  
FEEC_HOST_RELEVANCE != DTC_THEOREM_TRANSFER

## Final status

XH_S4_2610_01501_SOURCE_RELEVANCE = PASS_HIGH  
FEEC_TO_MONOGRAPH_CH4 = PASS_AS_NUMERICAL_STABILITY_HOST  
FEEC_TO_DTC_DIRECT_THEOREM_TRANSFER = REJECT  
DTC_NONNORMAL_VALIDATION_GATE = PASS_AS_GENERAL_MATHEMATICAL_METHOD  
CURRENT_DTC_OPERATOR_NORM_CERTIFICATE = ABSENT  
CURRENT_DTC_PSEUDOSPECTRAL_CERTIFICATE = ABSENT  
CURRENT_DTC_SCALAR_STRUCTURAL_CONTROLS = RETAIN  
MONOGRAPH_CHANGE_REQUIRED = NO; OPTIONAL_GUARD_ONLY

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK.
