# Badacz (Claude): E2 of PREREG_036 (commit 61bfd3f) - sensitivity of the chi2 = 4 boundary of Wu-Xu Fig. 5 to the
# hadron emission law below the first table row (1e9 g). Uses the AUTHORS' magic() (same loader as wuxu_native_audit.jl,
# default solver tolerances); only the five dN_over_dt_* source functions are redefined BELOW the first table mass:
#   native : unchanged (two-point log-log extrapolation of the authors)
#   ols8   : Q_i(m) = Q_i(m1) (m/m1)^s8_i, s8_i = OLS slope of log Q_i vs log m over the first 8 rows (Mech-S7 ROT036)
#   zero   : Q_i(m) = 0 for m < m1 (dependency measure, not a physical variant)
# Boundary: authors' observable Y_C = 2X/(1-X) at their T_nuc crosses 0.251 (chi2 = 4); bisection in log10(beta) on [-21,-15]
# to 0.005 dex.  Usage: julia --project=<env> wuxu_subedge_variant_boundary.jl <author arXiv-2509.05618 dir> <variant[_sym|_nsym]> <out.csv> [j1,j2,...]
using Printf
src_dir = abspath(ARGS[1]); variant = ARGS[2]; out_file = abspath(ARGS[3])
# E5 (PREREG_037): suffix "_sym" applies the Mech-S6 charge-pair source-map patch (B_sym) to main-scan.jl, unchanged:
# research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py (it refuses to run on any other source contract)
# E5b (PREREG_040): suffix "_nsym" halves ONLY the p+pbar and n+nbar aggregates (source-supported half-split, Rec9 2026-10-18);
# pi and K sources stay as in the authors' code. Implemented here (Badacz patch), exact-once line replacement.
charge_nsym = endswith(variant, "_nsym"); variant = replace(variant, r"_nsym$" => "")
charge_sym = endswith(variant, "_sym"); variant = replace(variant, r"_sym$" => "")
variant in ("native", "ols8", "zero") || error("variant must be native, ols8 or zero (optionally with suffix _sym or _nsym)")
masses_j = length(ARGS) >= 4 ? parse.(Int, split(ARGS[4], ",")) : [22, 24, 26, 28, 31, 34, 38, 43, 51, 62, 80, 90]  # 0-based

marker = "@info \"Loading `main-scan-parameters.jl`\""
if charge_sym
    patch = joinpath(@__DIR__, "..", "..", "..", "mech-s6", "2026-10-17", "apply_wuxu_charge_pair_source_map.py")
    tmp_scan = tempname() * ".jl"
    run(`python3 -I $patch $(joinpath(src_dir, "main-scan.jl")) $tmp_scan`)
    full = read(tmp_scan, String); rm(tmp_scan)
else
    full = read(joinpath(src_dir, "main-scan.jl"), String)
end
if charge_nsym
    for (a, b) in ("    d_n_proton_dt_from_PBH = dN_over_dt_proton(m_PBH) * n_PBH" => "    d_n_proton_dt_from_PBH = 0.5 * dN_over_dt_proton(m_PBH) * n_PBH",
                   "    d_n_neutron_dt_from_PBH = dN_over_dt_neutron(m_PBH) * n_PBH" => "    d_n_neutron_dt_from_PBH = 0.5 * dN_over_dt_neutron(m_PBH) * n_PBH")
        count(a, full) == 1 || error("nucleon source line not found exactly once: ", a)
        global full = replace(full, a => b)
    end
end
occursin(marker, full) || error("scan marker missing")
prefix = split(full, marker)[1]
inc = "@everywhere include(\"tool_script-hadrons_from_PBH.jl\")"
count(inc, prefix) == 1 || error("expected one hadron-source include")
variant_file = joinpath(src_dir, "_badacz_subedge_variant.jl")
write(variant_file, """
include("tool_script-hadrons_from_PBH.jl")          # authors' table and interpolations (unchanged)
const _BADACZ_VARIANT = "$variant"
const _logm = log.(hadrons_from_PBH[:, 1])
const _logm1 = _logm[1]
function _ols8(col)
    x = _logm[1:8]; y = log.(hadrons_from_PBH[1:8, col]); xm = sum(x) / 8; ym = sum(y) / 8
    return sum((x .- xm) .* (y .- ym)) / sum((x .- xm) .^ 2)
end
const _S8 = Dict(c => _ols8(c) for c in 2:6)
const _ITP = Dict(2 => π_from_PBH_interpolation, 3 => K_from_PBH_interpolation, 4 => K⁰ᴸ_from_PBH_interpolation,
                  5 => proton_from_PBH_interpolation, 6 => neutron_from_PBH_interpolation)
function _rate(col, m_PBH)
    lm = (log ∘ EUval)(GeV, m_PBH)
    if lm >= _logm1 || _BADACZ_VARIANT == "native"
        return (GeV ∘ exp ∘ _ITP[col])(lm)
    elseif _BADACZ_VARIANT == "ols8"
        return GeV(exp(log(hadrons_from_PBH[1, col]) + _S8[col] * (lm - _logm1)))
    else
        return GeV(zero(lm))
    end
end
dN_over_dt_π(m_PBH) = _rate(2, m_PBH)
dN_over_dt_K(m_PBH) = _rate(3, m_PBH)
dN_over_dt_K⁰ᴸ(m_PBH) = _rate(4, m_PBH)
dN_over_dt_proton(m_PBH) = _rate(5, m_PBH)
dN_over_dt_neutron(m_PBH) = _rate(6, m_PBH)
""")
prefix = replace(prefix, inc => "@everywhere include(\"_badacz_subedge_variant.jl\")")
prefix_file = joinpath(src_dir, "_badacz_subedge_prefix_$(variant).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file); rm(variant_file)

function Y_at(m, lb)
    β = ArbFloat(10; bits=BITS)^ArbFloat(lb; bits=BITS)
    return Float64(magic(m, β)[7])
end

open(out_file, "w") do io
    println(io, "# variant=", variant, " charge_map=", charge_sym ? "B_sym(Mech-S6 patch)" : (charge_nsym ? "B_nsym(nucleons halved, Badacz patch)" : "B_exec(authors)"), " s8=", join([@sprintf("%.9f", _S8[c]) for c in 2:6], ";"),
            " logm1_GeV=", @sprintf("%.12g", _logm1))
    println(io, "j,m_g,boundary_log10beta,status,n_evals,Y_lo,Y_hi,lo,hi")
    for j in masses_j
        m = m_PBH_f_list[j + 1]
        lo, hi = -21.0, -15.0; n = 2
        ylo = Y_at(m, lo); yhi = Y_at(m, hi)
        status = "bracketed"
        if !(ylo < 0.251 < yhi)
            status = ylo >= 0.251 ? "excluded_at_lo" : "allowed_at_hi"
        else
            while hi - lo > 0.005
                mid = (lo + hi) / 2; ym = Y_at(m, mid); n += 1
                if ym > 0.251; hi = mid; yhi = ym; else; lo = mid; ylo = ym; end
            end
        end
        bnd = status == "bracketed" ? lo + (0.251 - ylo) * (hi - lo) / (yhi - ylo) : NaN
        @printf(io, "%d,%.10g,%.6f,%s,%d,%.10g,%.10g,%.6f,%.6f\n", j, Float64(m / NU.g), bnd, status, n, ylo, yhi, lo, hi)
        flush(io)
    end
end
println("DONE ", out_file)
