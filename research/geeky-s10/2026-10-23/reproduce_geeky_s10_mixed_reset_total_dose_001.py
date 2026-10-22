import math
import numpy as np

try:
    from scipy.linalg import expm
except Exception as exc:
    raise SystemExit("scipy is required for this reproduction") from exc


def mu_plus(G):
    H = 0.5 * (G + G.T)
    return max(float(np.linalg.eigvalsh(H).max()), 0.0)


def heterogeneous_check(seed=20261023, n=4, N=80, T=1.5, eps=0.03):
    rng = np.random.default_rng(seed)
    G = 0.2 * rng.normal(size=(n, n))
    times = np.sort(rng.random(N) * T)

    s = rng.random(N) * eps
    alpha = rng.random(N)
    kappa = 1.0 - alpha

    e = rng.normal(size=(N, n))
    e /= np.linalg.norm(e, axis=1)[:, None]

    d = rng.normal(size=(N, n))
    d /= np.linalg.norm(d, axis=1)[:, None]

    v = rng.normal(size=n)

    xi = v.copy()
    tprev = 0.0
    c = []

    for j in range(N):
        xi = expm(G * (times[j] - tprev)) @ xi
        c.append(s[j] * float(e[j] @ xi))
        xi = (np.eye(n) - kappa[j] * s[j] * np.outer(d[j], e[j])) @ xi
        tprev = times[j]

    lhs = float(np.dot(c, c))

    B = float(s.sum())
    K = float((kappa * s).sum())
    E = float(np.linalg.norm(e, axis=1).max())
    D = float(np.linalg.norm(d, axis=1).max())
    mu = mu_plus(G)

    rhs = (
        float(s.max())
        * B
        * E**2
        * math.exp(2.0 * mu * T + 2.0 * D * E * K)
        * float(v @ v)
    )

    return {
        "lhs": lhs,
        "rhs": rhs,
        "ratio": lhs / rhs,
        "B": B,
        "K": K,
        "mu_plus": mu,
    }


def raw_scalar_sharpness(eps=0.01, N=1000):
    # G=0, e=d=1, alpha=1. Then conditional sensitivity never resets:
    # c_j = eps and B = N*eps, so sum c_j^2 = eps*B exactly.
    B = N * eps
    lhs = N * eps**2
    rhs = eps * B
    return {
        "lhs": lhs,
        "rhs": rhs,
        "ratio": lhs / rhs,
        "B": B,
    }


if __name__ == "__main__":
    print("heterogeneous mixed-reset check")
    print(heterogeneous_check())
    print()
    print("raw scalar exact endpoint")
    print(raw_scalar_sharpness())
