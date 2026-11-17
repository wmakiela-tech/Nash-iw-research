"""INPUT_075 check: KY 1999 (astro-ph/9908160) internal consistency of per-state yields.
Eq.(11): <N_ch> = 1.73 + 0.268*exp(1.42*sqrt(ln(s/Lambda^2))), Lambda = 1 GeV.
Eq.(13): yields per two jets at sqrt(s)=91.2 GeV, labelled per charge state.
Eq.(14): f_Hi = n_Hi / <N_ch(91.2)>.
Question: do the labelled per-state charged yields fit inside <N_ch>?"""
import json, math
sqrt_s = 91.2
nch = 1.73 + 0.268 * math.exp(1.42 * math.sqrt(math.log(sqrt_s**2 / 1.0**2)))
y = {"pi+": 14.1, "pi-": 14.1, "K+": 1.67, "K-": 1.67, "KL": 1.19,
     "p": 0.772, "pbar": 0.772, "n": 0.772, "nbar": 0.772}
charged = ["pi+", "pi-", "K+", "K-", "p", "pbar"]
sum_charged = sum(y[k] for k in charged)
f = {k: y[k] / nch for k in y}
out = {
    "Nch_91p2_eq11": nch,
    "sum_labelled_charged_yields": sum_charged,
    "ratio_sum_charged_over_Nch": sum_charged / nch,
    "pi_plus_plus_pi_minus": y["pi+"] + y["pi-"],
    "ratio_pipm_over_Nch": (y["pi+"] + y["pi-"]) / nch,
    "sum_f_charged": sum(f[k] for k in charged),
    "if_values_are_group_totals_assigned_per_state": {
        "sum_groups_charged": y["pi+"] + y["K+"] + y["p"],
        "ratio_over_Nch": (y["pi+"] + y["K+"] + y["p"]) / nch},
}
print(json.dumps(out, indent=1))
