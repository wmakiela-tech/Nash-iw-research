#!/usr/bin/env python3
"""
MT10 independent interval reproduction for PRF7 T-WEB-15 and T-WEB-17.

Requires:
    Python >= 3.11
    mpmath == 1.3.0

Scope:
- T-WEB-15 nonrescalable alpha-family, c in [0.26,0.27],
  alpha in [1.49,1.51].
- T-WEB-17 constant-sector W(c) range tests for c1 and c2.

This script independently reimplements the interval layer from the exact formulas
recorded in the project artifacts. It does not establish novelty, Lorentzian or
complex stability, nonlinear stability, gravity-multiplet stability, or physical
equivalence/inequivalence.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE.
"""
import mpmath as mp

mp.mp.dps = 80
iv = mp.iv

def endpoints(x):
    return mp.mpf(float(x.a)), mp.mpf(float(x.b))

def ein_scalar_bounds(y):
    """Rigorous elementary enclosure for Ein(y), y>=0."""
    y = mp.mpf(y)
    if y == 0:
        return mp.mpf("0"), mp.mpf("0")
    if y <= 1:
        s = mp.mpf("0")
        for k in range(1, 400):
            term = y**k / (k * mp.factorial(k))
            s += term if k % 2 else -term
            if k % 2 == 0:
                nxt = y**(k + 1) / ((k + 1) * mp.factorial(k + 1))
                if nxt < mp.mpf("1e-70"):
                    return s, s + nxt
        raise RuntimeError("Ein series did not converge to target remainder.")
    base = mp.euler + mp.log(y)
    # Classical positive-x E1 enclosure:
    # exp(-y)/(y+1) < E1(y) < exp(-y)/y.
    return base + mp.e**(-y)/(y + 1), base + mp.e**(-y)/y

def ein_iv_x6(x):
    xlo, xhi = endpoints(x)
    ylo, yhi = xlo**6, xhi**6
    lo, _ = ein_scalar_bounds(ylo)
    _, hi = ein_scalar_bounds(yhi)
    return iv.mpf([str(lo), str(hi)])

def G(x, alpha):
    return iv.exp(alpha * ein_iv_x6(x))

def F(x, alpha):
    xlo, _ = endpoints(x)
    if xlo <= 0:
        raise ValueError("F interval requires x>0; use removable value F(0)=0 explicitly.")
    return (G(x, alpha) - 1) / (2 * x)

def Fp(x, alpha):
    xlo, _ = endpoints(x)
    if xlo <= 0:
        raise ValueError("Fp interval requires x>0.")
    y = x**6
    return (1 + G(x, alpha) * (6 * alpha * (1 - iv.exp(-y)) - 1)) / (2 * x**2)

def Fpp(x, alpha):
    xlo, _ = endpoints(x)
    if xlo <= 0:
        raise ValueError("Fpp interval requires x>0.")
    y = x**6
    a2 = (
        2
        + 36 * alpha**2 * (1 - iv.exp(-y))**2
        + 18 * alpha * (-1 + (1 + 2 * y) * iv.exp(-y))
    )
    return (G(x, alpha) * a2 - 2) / (2 * x**3)

def branch_B(c, alpha):
    z = 2 - 3 * c**2
    return G(z, alpha) + 6 * c**2 * (c**2 - 2) * Fp(z, alpha)

def branch_dB(c, alpha):
    z = 2 - 3 * c**2
    y = z**6
    hp = 6 * alpha * (1 - iv.exp(-y)) / z
    return (
        -6 * c * G(z, alpha) * hp
        + 24 * c * (c**2 - 1) * Fp(z, alpha)
        - 36 * c**3 * (c**2 - 2) * Fpp(z, alpha)
    )

def q1(lam, z, alpha):
    flam = iv.mpf([0, 0]) if float(lam.a) == 0.0 and float(lam.b) == 0.0 else F(lam, alpha)
    return (flam - F(z, alpha)) / (lam - z)

def q2(lam, z, alpha):
    return (q1(lam, z, alpha) - Fp(z, alpha)) / (lam - z)

def upper(x):
    return float(x.b)

def lower(x):
    return float(x.a)

def gap_upper_bounds(c, alpha):
    z = 2 - 3 * c**2
    E = c * (2 - c**2)
    A = 6 * c * E
    Fz = F(z, alpha)
    Fpz = Fp(z, alpha)
    C0 = z + 2 * A * Fz - 6 * E**2 * Fpz
    C1 = -4 * A * z * Fz + 2 * A**2 * Fpz
    C1pos = iv.mpf([0, str(max(0.0, upper(C1)))])
    Uminus = -z + C0 + C1pos / z
    out = {"U_minus": upper(Uminus)}

    for l, u, name in [(0, 0.5, "U_B1"), (0.5, 1.0, "U_B2"), (1.0, 1.5, "U_B3")]:
        li = iv.mpf([str(l), str(l)])
        ui = iv.mpf([str(u), str(u)])
        U = (
            ui + 2 * ui**2 * F(ui, alpha)
            - 2 * A * Fz
            - 4 * A * li * q1(li, z, alpha)
            - 6 * E**2 * Fpz
            + 2 * A**2 * q2(ui, z, alpha)
        )
        out[name] = upper(U)

    li = iv.mpf(["1.5", "1.5"])
    ui = z
    U4 = (
        ui + 2 * ui**2 * Fz
        - 2 * A * Fz
        - 4 * A * li * q1(li, z, alpha)
        - 6 * E**2 * Fpz
        + 2 * A**2 * (Fpp(z, alpha) / 2)
    )
    out["U_B4"] = upper(U4)
    return out

def W(c, alpha):
    z = 2 - 3 * c**2
    V = -c**2 + c**4 / 4
    Vp = c * (c**2 - 2)
    return V - Vp**2 * F(z, alpha)

def main():
    # T-WEB-15 endpoint signs and transversality.
    b026_lowers = []
    b027_uppers = []
    db_lowers = []
    db_uppers = []
    for j in range(10):
        alo = mp.mpf("1.49") + j * mp.mpf("0.002")
        ahi = alo + mp.mpf("0.002")
        alpha = iv.mpf([str(alo), str(ahi)])
        b026_lowers.append(lower(branch_B(iv.mpf(["0.26", "0.26"]), alpha)))
        b027_uppers.append(upper(branch_B(iv.mpf(["0.27", "0.27"]), alpha)))
        for i in range(20):
            clo = mp.mpf("0.26") + i * mp.mpf("0.0005")
            chi = clo + mp.mpf("0.0005")
            db = branch_dB(iv.mpf([str(clo), str(chi)]), alpha)
            db_lowers.append(lower(db))
            db_uppers.append(upper(db))

    # T-WEB-15 full real-Euclidean Hessian gap.
    worst = {k: float("-inf") for k in ["U_minus", "U_B1", "U_B2", "U_B3", "U_B4"]}
    for i in range(20):
        clo = mp.mpf("0.26") + i * mp.mpf("0.0005")
        chi = clo + mp.mpf("0.0005")
        c = iv.mpf([str(clo), str(chi)])
        for j in range(10):
            alo = mp.mpf("1.49") + j * mp.mpf("0.002")
            ahi = alo + mp.mpf("0.002")
            alpha = iv.mpf([str(alo), str(ahi)])
            for key, value in gap_upper_bounds(c, alpha).items():
                worst[key] = max(worst[key], value)

    # T-WEB-17 action-value range certificates.
    w_c1 = W(iv.mpf(["0.26", "0.27"]), iv.mpf(["1.49", "1.51"]))
    w_c2 = W(iv.mpf(["0.70857", "0.70858"]), iv.mpf(["1.5", "1.5"]))

    print("TWEB15_B026_LOWER_MIN", min(b026_lowers))
    print("TWEB15_B027_UPPER_MAX", max(b027_uppers))
    print("TWEB15_dB_GLOBAL_LOWER", min(db_lowers))
    print("TWEB15_dB_GLOBAL_UPPER", max(db_uppers))
    for k in ["U_minus", "U_B1", "U_B2", "U_B3", "U_B4"]:
        print("TWEB15_" + k, worst[k])
    print("TWEB17_c1_W_LOWER", lower(w_c1))
    print("TWEB17_c1_W_UPPER", upper(w_c1))
    print("TWEB17_c2_W_LOWER", lower(w_c2))
    print("TWEB17_c2_W_UPPER", upper(w_c2))

    assert min(b026_lowers) > 0
    assert max(b027_uppers) < 0
    assert max(db_uppers) < 0
    assert max(worst.values()) < 0
    assert upper(w_c1) < -1
    assert lower(w_c2) > -1 and upper(w_c2) < 0
    print("MT10_INTERVAL_REPRODUCTION=PASS")

if __name__ == "__main__":
    main()
