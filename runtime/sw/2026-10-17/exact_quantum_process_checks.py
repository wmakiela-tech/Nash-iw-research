#!/usr/bin/env python3
"""Exact finite-dimensional witnesses over Q(i), using the Python standard library.

Run: python3 exact_quantum_process_checks.py --output exact_quantum_process_results.json
Tensor order: system, environment; Choi: output, input;
two-comb: output1, input1, output0, input0. Choi vectors are unnormalized.
This checks concrete witnesses, not general process-realization theorems.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json
import platform


@dataclass(frozen=True, eq=False)
class Q:
    r: F = F(0)
    i: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "r", F(self.r))
        object.__setattr__(self, "i", F(self.i))

    def __add__(self, other):
        b = q(other)
        return Q(self.r + b.r, self.i + b.i)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-q(other))

    def __rsub__(self, other):
        return q(other) + (-self)

    def __mul__(self, other):
        b = q(other)
        return Q(self.r*b.r-self.i*b.i, self.r*b.i+self.i*b.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = q(other)
        n = b.r*b.r + b.i*b.i
        if not n:
            raise ZeroDivisionError
        return self * Q(b.r/n, -b.i/n)

    def conj(self):
        return Q(self.r, -self.i)

    def __eq__(self, other):
        b = q(other)
        return self.r == b.r and self.i == b.i

    def __str__(self):
        if not self.i:
            return str(self.r)
        return f"({self.r})+({self.i})i"


def q(x):
    return x if isinstance(x, Q) else Q(x)


def matrix(rows):
    return [[q(x) for x in row] for row in rows]


def zero(n, m):
    return matrix([[0]*m for _ in range(n)])


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def unit(n, i, j):
    a = zero(n, n)
    a[i][j] = Q(1)
    return a


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[q(c)*x for x in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def dagger(a):
    return [[x.conj() for x in row] for row in transpose(a)]


def mm(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q())
             for j in range(len(b[0]))] for i in range(len(a))]


def kron(a, b):
    return [[x*y for x in ar for y in br] for ar in a for br in b]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q())


def conjugate(u, a):
    return mm(mm(u, a), dagger(u))


def ptrace(a, dims, keep):
    """Partial trace, keeping subsystems in the explicitly supplied order."""
    assert len(set(keep)) == len(keep)
    drop = [k for k in range(len(dims)) if k not in keep]
    kept = list(product(*(range(dims[k]) for k in keep)))
    gone = list(product(*(range(dims[k]) for k in drop)))

    def index(x, z):
        coords = dict(zip(keep, x)) | dict(zip(drop, z))
        out = 0
        for k, d in enumerate(dims):
            out = out*d + coords[k]
        return out

    return [[sum((a[index(x, z)][index(y, z)] for z in gone), Q())
             for y in kept] for x in kept]


def determinant(a):
    b = [row[:] for row in a]
    out = Q(1)
    for k in range(len(b)):
        pivot = next((j for j in range(k, len(b)) if b[j][k] != 0), None)
        if pivot is None:
            return Q()
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            out = -out
        p = b[k][k]
        out = out*p
        for j in range(k+1, len(b)):
            f = b[j][k]/p
            b[j] = [x-f*y for x, y in zip(b[j], b[k])]
    return out


I = eye(2)
X = matrix([[0, 1], [1, 0]])
Y = matrix([[0, Q(0, -1)], [Q(0, 1), 0]])
Z = matrix([[1, 0], [0, -1]])
P0, P1 = unit(2, 0, 0), unit(2, 1, 1)
PP = scale(F(1, 2), matrix([[1, 1], [1, 1]]))
PM = scale(F(1, 2), matrix([[1, -1], [-1, 1]]))
PI = scale(F(1, 2), matrix([[1, Q(0, -1)], [Q(0, 1), 1]]))
SIGMA = scale(F(1, 2), I)
UX = add(kron(I, P0), kron(X, P1))
UZ = add(kron(I, P0), kron(Z, P1))
SWAP = matrix([[1, 0, 0, 0], [0, 0, 1, 0],
               [0, 1, 0, 0], [0, 0, 0, 1]])
UNITS = [unit(2, i, j) for i in range(2) for j in range(2)]


def phi(a):
    return ptrace(conjugate(UX, kron(a, SIGMA)), [2, 2], [0])


def choi(fun):
    out = zero(4, 4)
    for e in UNITS:
        out = add(out, kron(fun(e), e))
    return out


def reconstruct(j, a, use_transpose=True):
    right = transpose(a) if use_transpose else a
    return ptrace(mm(j, kron(I, right)), [2, 2], [0])


def histories(refresh=False, move_instrument_before_gate=False):
    out = zero(2, 2)
    initial = kron(P0, SIGMA)
    for a in range(2):
        k = kron(unit(2, 0, a), I)
        if move_instrument_before_gate:
            state = conjugate(UX, conjugate(k, initial))
        else:
            state = conjugate(k, conjugate(UX, initial))
        if refresh:
            state = kron(ptrace(state, [2, 2], [0]), SIGMA)
        state = conjugate(UX, state)
        for b in range(2):
            out[a][b] = trace(mm(kron(unit(2, b, b), I), state))
    return out


def endpoint(a, second):
    return ptrace(conjugate(second, conjugate(SWAP, kron(a, SIGMA))),
                  [2, 2], [0])


def intervened(a, second):
    state = conjugate(SWAP, kron(a, SIGMA))
    state = kron(PP, ptrace(state, [2, 2], [1]))
    return ptrace(conjugate(second, state), [2, 2], [0])


def main():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append({"id": name, "status": "PASS"})

    check("controlled_gates_and_swap_unitary",
          all(mm(dagger(u), u) == eye(4) for u in (UX, UZ, SWAP)))
    pi_minus = scale(F(1, 2), add(eye(4), scale(-1, UX)))
    check("autonomous_group_projector_identity",
          mm(pi_minus, pi_minus) == pi_minus and dagger(pi_minus) == pi_minus)
    check("autonomous_group_endpoint_phase_minus_one",
          add(eye(4), scale(-2, pi_minus)) == UX and mm(UX, UX) == eye(4))
    check("one_step_channel_on_all_matrix_units",
          all(phi(a) == scale(F(1, 2), add(a, conjugate(X, a))) for a in UNITS))
    check("two_retained_steps_are_identity_on_all_matrix_units",
          all(ptrace(conjugate(mm(UX, UX), kron(a, SIGMA)), [2, 2], [0]) == a
              for a in UNITS))
    check("refreshed_channel_is_idempotent_on_all_matrix_units",
          all(phi(phi(a)) == phi(a) for a in UNITS))
    check("semigroup_failure_witness", phi(phi(P0)) == SIGMA and SIGMA != P0)

    retained = histories()
    refreshed = histories(refresh=True)
    wrong_order = histories(move_instrument_before_gate=True)
    check("history_retained", retained == scale(F(1, 2), I))
    check("history_refreshed", refreshed == scale(F(1, 4), matrix([[1, 1], [1, 1]])))
    check("history_normalization", sum(sum(row, Q()) for row in retained) == 1
          and sum(sum(row, Q()) for row in refreshed) == 1)
    check("negative_control_instrument_order_detected",
          wrong_order == P0 and wrong_order != retained)

    ji, jx, jt = choi(lambda a: a), choi(lambda a: conjugate(X, a)), choi(transpose)
    check("choi_reconstruction_including_imaginary_coherence",
          all(reconstruct(ji, a) == a for a in UNITS + [PI]))
    check("negative_control_missing_transpose_detected",
          reconstruct(ji, PI, False) == transpose(PI) and transpose(PI) != PI)
    check("choi_trace_preserving", ptrace(ji, [2, 2], [1]) == I
          and ptrace(jt, [2, 2], [1]) == I)
    check("transpose_choi_is_swap", jt == SWAP)
    antisymmetric = matrix([[0], [1], [-1], [0]])
    norm2 = mm(dagger(antisymmetric), antisymmetric)[0][0]
    rayleigh = mm(mm(dagger(antisymmetric), jt), antisymmetric)[0][0]/norm2
    check("transpose_exact_negative_eigenvector",
          mm(jt, antisymmetric) == scale(-1, antisymmetric) and rayleigh == -1)
    bell_partial_transpose = zero(4, 4)
    for e in UNITS:
        bell_partial_transpose = add(bell_partial_transpose,
                                     scale(F(1, 2), kron(e, transpose(e))))
    check("bell_partial_transpose_negative_half",
          bell_partial_transpose == scale(F(1, 2), jt)
          and mm(bell_partial_transpose, antisymmetric) == scale(F(-1, 2), antisymmetric))
    states = [P0, P1, PP, PI]
    pauli_coords = [[trace(mm(p, rho)) for rho in states] for p in (I, X, Y, Z)]
    check("four_density_operators_span", determinant(pauli_coords) == -2)
    check("linear_relation_failure_detected",
          add(P0, P1) == I and add(P0, P0) != I)

    w0 = scale(F(1, 2), add(ji, jx))
    wr = scale(F(1, 2), add(kron(ji, ji), kron(jx, jx)))
    wf = kron(w0, w0)
    check("comb_first_causality", ptrace(w0, [2, 2], [1]) == I)
    check("comb_second_causality",
          all(ptrace(w, [2, 2, 2, 2], [1, 2, 3]) == kron(I, w0) for w in (wr, wf)))
    check("comb_unnormalized_trace", trace(wr) == 4 and trace(wf) == 4)
    check("comb_spectral_polynomials",
          dagger(wr) == wr and dagger(wf) == wf
          and mm(wr, wr) == scale(2, wr) and mm(wf, wf) == wf and wr != wf)
    check("negative_control_trace_one_comb_detected",
          ptrace(scale(F(1, 4), wr), [2, 2, 2, 2], [1, 2, 3]) != kron(I, w0))

    check("swap_transfers_arbitrary_input_on_all_matrix_units",
          all(conjugate(SWAP, kron(a, SIGMA)) == kron(SIGMA, a) for a in UNITS))
    check("identical_endpoint_channels_on_all_matrix_units",
          all(endpoint(a, u) == scale(trace(a), SIGMA) for a in UNITS for u in (eye(4), UZ)))
    check("intervention_output_formula_on_all_matrix_units",
          all(intervened(a, eye(4)) == scale(trace(a), PP)
              and intervened(a, UZ) == add(scale(a[0][0], PP), scale(a[1][1], PM))
              for a in UNITS))
    check("perfect_intervention_distinguishability",
          intervened(P1, eye(4)) == PP and intervened(P1, UZ) == PM
          and trace(mm(PP, PP)) == 1 and trace(mm(PP, PM)) == 0)

    result = {
        "artifact_id": "IW_SW_QUANTUM_PROCESS_EXACT_WITNESSES_001_20261017",
        "status": "PASS", "arithmetic": "Gaussian rational numbers Q(i); no floating point",
        "python_version": platform.python_version(), "checks_passed": len(checks),
        "conventions": {"joint_order": ["S", "E"], "choi_order": ["output", "input"],
                        "comb_order": ["output1", "input1", "output0", "input0"],
                        "choi_normalization": "unnormalized"},
        "values": {"retained_history": [[str(v) for v in row] for row in retained],
                   "refreshed_history": [[str(v) for v in row] for row in refreshed],
                   "wrong_order_history": [[str(v) for v in row] for row in wrong_order],
                   "pauli_coordinate_determinant": "-2", "transpose_choi_negative_eigenvalue": "-1",
                   "bell_partial_transpose_negative_eigenvalue": "-1/2",
                   "comb_trace_retained_and_refreshed": "4", "intervention_total_variation": "1"},
        "checks": checks,
        "scope": "Concrete finite-dimensional witnesses and exact linear identities; general proofs remain analytic.",
        "limits": ["No general supermap-realization proof by finite tests.",
                   "No claim of specifically quantum environmental memory.",
                   "No equality at all continuous times for the two-endpoint example.",
                   "Continuous group exponential identity is proved analytically from the projector, not numerically sampled.",
                   "No novelty, physical-stability or gravity claim."]}
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    body = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(body, encoding="utf-8")
    print(body, end="")


if __name__ == "__main__":
    main()
