# v2 (2 XI, PREREG_046): tolerance mode accepts an optional 4th field maxiters (ladder:<reltol>:<abstol>:<maxiters>); all else unchanged.
# Badacz (Claude): PREREG_043 T2/T3 (commit ec6d473) - Y_P on a given (mass index, log10 beta) list for one source variant,
# using the AUTHORS' magic() with the same source variants as wuxu_subedge_variant_boundary_v2.jl (research/badacz/2026-10-31/code/,
# copied here; variant definitions unchanged). Extra: optional solver tolerance mode "ladder:<reltol>:<abstol>" which, as in
# wuxu_native_audit.jl, sets explicit tolerances on magic()'s single solve() and saves only at the authors' output nodes.
# Usage: julia --project=<env> wuxu_variant_grid.jl <author arXiv-2509.05618 dir> <variant[_sym|_nsym]> <out.csv> <points file: "j log10beta" per line> [default|ladder:<r>:<a>]
# Badacz (Claude): E2 of PREREG_036 (commit 61bfd3f) - sensitivity of the chi2 = 4 boundary of Wu-Xu Fig. 5 to the
# hadron emission law below the first table row (1e9 g). Uses the AUTHORS' magic() (same loader as wuxu_native_audit.jl,
# default solver tolerances); only the five dN_over_dt_* source functions are redefined BELOW the first table mass:
#   native : unchanged (two-point log-log extrapolation of the authors)
#   ols8   : Q_i(m) = Q_i(m1) (m/m1)^s8_i, s8_i = OLS slope of log Q_i vs log m over the first 8 rows (Mech-S7 ROT036)
#   zero   : Q_i(m) = 0 for m < m1 (dependency measure, not a physical variant)
#   p13    : Q_i(m) = Q_i(m1) (m/m1)^(-1.3), the authors' paper-declared analytic law (arXiv:2509.05618 Eq. 4.5), PREREG_041 A
#   pyt    : Q_i(m) = Q_i(m1) R_i(T(m))/R_i(T1) from a PYTHIA multiplicity table (PREREG_041 C); table path in env
#            BADACZ_PYT_TABLE: CSV with header ln_u,pi,K,K0L,p,n where ln_u = ln(m/m1) <= 0 and columns are ln(R_i/R_i(T1));
#            linear interpolation in ln_u, beyond the table linear extrapolation with the last segment
# Boundary: authors' observable Y_C = 2X/(1-X) at their T_nuc crosses 0.251 (chi2 = 4); bisection in log10(beta) on [-21,-15]
# to 0.005 dex.  Usage: julia --project=<env> wuxu_subedge_variant_boundary.jl <author arXiv-2509.05618 dir> <variant[_sym|_nsym]> <out.csv> [j1,j2,...]
using Printf, SHA
src_dir = abspath(ARGS[1]); variant = ARGS[2]; out_file = abspath(ARGS[3]); pts_file = abspath(ARGS[4])
tolmode = length(ARGS) >= 5 ? ARGS[5] : "default"
# E5 (PREREG_037): suffix "_sym" applies the Mech-S6 charge-pair source-map patch (B_sym) to main-scan.jl, unchanged:
# research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py (it refuses to run on any other source contract)
# E5b (PREREG_040): suffix "_nsym" halves ONLY the p+pbar and n+nbar aggregates (source-supported half-split, Rec9 2026-10-18);
# pi and K sources stay as in the authors' code. Implemented here (Badacz patch), exact-once line replacement.
charge_nsym = endswith(variant, "_nsym"); variant = replace(variant, r"_nsym$" => "")
charge_sym = endswith(variant, "_sym"); variant = replace(variant, r"_sym$" => "")
variant in ("native", "ols8", "zero", "p13", "pyt") || error("variant must be native, ols8, zero, p13 or pyt (optionally with suffix _sym or _nsym)")
pyt_table = variant == "pyt" ? abspath(ENV["BADACZ_PYT_TABLE"]) : ""
pts = [(parse(Int, split(l)[1]), parse(Float64, split(l)[2])) for l in readlines(pts_file) if !isempty(strip(l))]  # j 0-based

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
solve_call = "solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(solve_call, prefix) == 1 || error("expected exactly one solve() call in magic()")
if tolmode != "default"
    startswith(tolmode, "ladder:") || error("tolerance mode must be default or ladder:<reltol>:<abstol>[:<maxiters>]")
    tp = split(tolmode, ":")
    mi = length(tp) >= 4 ? ", maxiters=$(parse(Int, tp[4]))" : ""
    prefix = replace(prefix, solve_call => "solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=$(parse(Float64, tp[2])), abstol=$(parse(Float64, tp[3]))$mi, saveat=log.(geomspace(a_f, a_end, num_points)), dense=false)")
end
inc = "@everywhere include(\"tool_script-hadrons_from_PBH.jl\")"
count(inc, prefix) == 1 || error("expected one hadron-source include")
variant_file = joinpath(src_dir, "_badacz_subedge_variant_$(variant)_$(getpid()).jl")   # v2: unique name (v1 shared one name; safe only for sequential runs)
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
const _PYT = if _BADACZ_VARIANT == "pyt"
    _rows = [parse.(Float64, split(l, ",")) for l in readlines("$pyt_table")[2:end] if !isempty(strip(l))]
    sort!(_rows, by = r -> r[1]); (first.(_rows), Dict(c => [r[c] for r in _rows] for c in 2:6))
else
    nothing
end
function _pyt_lnR(col, lu)
    x, ys = _PYT[1], _PYT[2][col]; n = length(x)
    i = lu <= x[1] ? 1 : (lu >= x[n] ? n - 1 : searchsortedlast(x, lu))
    i = clamp(i, 1, n - 1)
    return ys[i] + (ys[i+1] - ys[i]) * (lu - x[i]) / (x[i+1] - x[i])
end
const _ITP = Dict(2 => π_from_PBH_interpolation, 3 => K_from_PBH_interpolation, 4 => K⁰ᴸ_from_PBH_interpolation,
                  5 => proton_from_PBH_interpolation, 6 => neutron_from_PBH_interpolation)
function _rate(col, m_PBH)
    lm = (log ∘ EUval)(GeV, m_PBH)
    if lm >= _logm1 || _BADACZ_VARIANT == "native"
        return (GeV ∘ exp ∘ _ITP[col])(lm)
    elseif _BADACZ_VARIANT == "ols8"
        return GeV(exp(log(hadrons_from_PBH[1, col]) + _S8[col] * (lm - _logm1)))
    elseif _BADACZ_VARIANT == "p13"
        return GeV(exp(log(hadrons_from_PBH[1, col]) - 1.3 * (lm - _logm1)))
    elseif _BADACZ_VARIANT == "pyt"
        return GeV(exp(log(hadrons_from_PBH[1, col]) + _pyt_lnR(col, Float64(lm - _logm1))))
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
prefix = replace(prefix, inc => "@everywhere include(\"$(basename(variant_file))\")")
prefix_file = joinpath(src_dir, "_badacz_subedge_prefix_$(variant)_$(getpid()).jl")
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
    println(io, "# variant=", variant, " charge_map=", charge_sym ? "B_sym(Mech-S6 patch)" : (charge_nsym ? "B_nsym(nucleons halved, Badacz patch)" : "B_exec(authors)"),
            " tolmode=", tolmode, " logm1_GeV=", @sprintf("%.12g", _logm1))
    println(io, "j,m_g,log10beta,Yp,seconds")
    for (j, lb) in pts
        m = m_PBH_f_list[j + 1]; t0 = time()
        y = Y_at(m, lb)
        @printf(io, "%d,%.10g,%.6f,%.17g,%.1f\n", j, Float64(m / NU.g), lb, y, time() - t0)
        flush(io)
    end
end
println("DONE ", out_file)
