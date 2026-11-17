#!/usr/bin/env python3
"""Conditional source-number arithmetic only. NO author raw data or physics bound.
Sources: An et al. Nat Commun 2026 DOI 10.1038/s41467-026-78187-4
         Tan et al. Phys Rev Applied 26 044045 DOI 10.1103/tcb8-csbs
"""
import math
import json

f_high_mHz = 1000.0 * 16.0 / 600.0
f_low_mHz = 1000.0 * 16.0 / 3600.0
tau_high, se_high = 11.16, 0.27  # aNm; original statistical 1sigma
tau_low, se_low = 11.41, 0.46  # aNm; original statistical 1sigma

delta = tau_low - tau_high
sd_independent = math.hypot(se_high, se_low)
z_independent = abs(delta) / sd_independent
p_independent_normal = math.erfc(z_independent / math.sqrt(2.0))
ci95_independent = [delta - 1.96*sd_independent, delta + 1.96*sd_independent]
# For unknown covariance, rho in [-1,+1]. This does not cover systematic uncertainty.
sigma_min = abs(se_low - se_high)
sigma_max = se_low + se_high
z_min, z_max = abs(delta)/sigma_max, abs(delta)/sigma_min

# Separate related but NOT SAME DEVICE 2026 source: CMR at approximately 2mHz
aps_noise_raw = 1.4e-14
aps_noise_cmr = 1.1e-15

result = {
    "science_type": "PUBLISHED_NUMBER_POSTHOC_ARITHMETIC_ONLY",
    "article_source_DOI": "10.1038/s41467-026-78187-4",
    "other_instrument_DOI": "10.1103/tcb8-csbs",
    "tau_high_aNm": tau_high, "se_high_stat_aNm": se_high,
    "tau_low_aNm": tau_low, "se_low_stat_aNm": se_low,
    "frequency_high_mHz": f_high_mHz,
    "frequency_low_mHz": f_low_mHz,
    "frequency_ratio": f_high_mHz / f_low_mHz,
    "delta_tau_aNm": delta,
    "relative_change_percent_baseline_high": 100.0*delta/tau_high,
    "sigma_independent_aNm": sd_independent,
    "z_independent": z_independent,
    "two_sided_p_independent_normal": p_independent_normal,
    "ci95_independent_stat_aNm": ci95_independent,
    "unknown_correlation_sigma_min_aNm": sigma_min,
    "unknown_correlation_sigma_max_aNm": sigma_max,
    "unknown_correlation_z_min": z_min,
    "unknown_correlation_z_max": z_max,
    "independent_other_instrument_noise_ratio_2mHz": aps_noise_raw/aps_noise_cmr,
    "holds": ["PAPER_RAW_TORQUE_VECTOR", "PAPER_FULL_COVARIANCE", "PAPER_SI_FILE_BYTES", "NASH_OBSERVABLE_INTERFACE", "NO_TRANSPORT_OF_APS_2mHz_CMR_TO_AN_DEVICE"]
}
assert abs(f_high_mHz-26.666666666666668)<1e-12
assert abs(f_low_mHz-4.444444444444445)<1e-12
assert abs(delta-0.25)<1e-12
assert z_max < 1.96
assert ci95_independent[0] < 0 < ci95_independent[1]
assert abs(aps_noise_raw/aps_noise_cmr-12.727272727272728)<1e-12
print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
