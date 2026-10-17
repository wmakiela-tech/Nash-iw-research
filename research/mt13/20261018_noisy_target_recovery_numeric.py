"""MT13 numerical cross-check for bounded-noise scalar target recovery."""
from math import sqrt, hypot
from scipy.optimize import minimize_scalar

for noise in (0, 0.1, 0.2, 0.5, 1/sqrt(2), 0.9, 1):
    expected = noise + sqrt(1-noise**2) if noise <= 1/sqrt(2) else sqrt(2)
    objective = lambda w: hypot(1-w, 1) + noise*abs(w)
    value = minimize_scalar(objective, bounds=(-1,3), method="bounded").fun
    assert abs(expected-value) < 1e-6, (noise, expected, value)
    print(f"noise={noise:.9f}; expected={expected:.9f}; dual={value:.9f}")

print("7/7 bounded-noise dual checks passed")
