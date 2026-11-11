# Badacz (Claude): PREREG_060 (research/badacz/2026-11-11/) - native response of the Wu-Xu chi2 = 4 boundary (Y_C = 0.251 root
# in log10 beta) to the ALTERNATIVE sub-edge extrapolation of the authors' hadron rate table identified by Mech-S8 ROT017.
# Derived from research/badacz/2026-11-08/code/wuxu_band_kernel.jl (same prefix injection, same bracket/bisection/7-point fit).
# Only the five dN_over_dt_* hadron rates are touched: below the first table mass m1 (1e9 g) the native log-log linear
# extrapolation (first-pair slope -p2_h) is multiplied by (M/m1)^(-lam*dp_h), dp_h = p12_h - p2_h, p12_h = OLS log-log slope over
# the first 12 table rows; lam = 1 is the p12 alternative anchored at row 1, lam = 0 reproduces the native code bit for bit.
# PBH mass loss (N_BH law) and energy injection are not touched.
# Usage: julia --project=<env> wuxu_subedge_ramp.jl <author arXiv-2509.05618 dir> <out.csv> <configs file>
#   configs file: one line per config "id j lam start_log10beta" (j 0-based); an id starting with "pt" evaluates Y_C at start only
using Printf
src_dir = abspath(ARGS[1]); out_file = abspath(ARGS[2]); cfg_file = abspath(ARGS[3])
cfgs = [split(l) for l in readlines(cfg_file) if !isempty(strip(l)) && !startswith(strip(l), "#")]
all(length(c) == 4 for c in cfgs) || error("config lines must be: id j lam start_log10beta")

full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, full) || error("scan marker missing")
prefix = split(full, marker)[1]
solve_call = "solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(solve_call, prefix) == 1 || error("expected exactly one solve() call in magic()")
tolmode = get(ENV, "BADACZ_TOL", "default")      # "default" or "<reltol>:<abstol>" (as wuxu_variant_grid_v2.jl ladder mode)
if tolmode != "default"
    tp = split(tolmode, ":")
    prefix = replace(prefix, solve_call => "solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=$(parse(Float64, tp[1])), abstol=$(parse(Float64, tp[2])), saveat=log.(geomspace(a_f, a_end, num_points)), dense=false)")
end
inc = "@everywhere include(\"tool_script-hadrons_from_PBH.jl\")"
count(inc, prefix) == 1 || error("expected one hadron-source include")
variant_file = joinpath(src_dir, "_badacz_subedge_ramp_$(getpid()).jl")
write(variant_file, """
include("tool_script-hadrons_from_PBH.jl")          # authors' table and interpolations (unchanged)
const _LAM = Ref(0.0)                                # set at run time
const _logm1 = log(hadrons_from_PBH[1, 1])
const _ITP = Dict(2 => π_from_PBH_interpolation, 3 => K_from_PBH_interpolation, 4 => K⁰ᴸ_from_PBH_interpolation,
                  5 => proton_from_PBH_interpolation, 6 => neutron_from_PBH_interpolation)
function _slope(col, n)                              # log-log slope over the first n table rows (n = 2: first pair)
    x = log.(hadrons_from_PBH[1:n, 1]); y = log.(hadrons_from_PBH[1:n, col])
    mx = sum(x) / n; my = sum(y) / n
    return sum((x .- mx) .* (y .- my)) / sum((x .- mx) .^ 2)
end
const _DP = Dict(col => -(_slope(col, 12) - _slope(col, 2)) for col in 2:6)   # dp = p12 - p2 with R ~ M^-p
function _rate(col, m_PBH)
    lm = (log ∘ EUval)(GeV, m_PBH)
    r = (exp ∘ _ITP[col])(lm)
    lam = _LAM[]
    if lam != 0.0 && lm < _logm1
        r = r * exp(-lam * _DP[col] * (lm - _logm1))
    end
    return GeV(r)
end
dN_over_dt_π(m_PBH) = _rate(2, m_PBH)
dN_over_dt_K(m_PBH) = _rate(3, m_PBH)
dN_over_dt_K⁰ᴸ(m_PBH) = _rate(4, m_PBH)
dN_over_dt_proton(m_PBH) = _rate(5, m_PBH)
dN_over_dt_neutron(m_PBH) = _rate(6, m_PBH)
""")
prefix = replace(prefix, inc => "@everywhere include(\"$(basename(variant_file))\")")
prefix_file = joinpath(src_dir, "_badacz_ramp_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file); rm(variant_file)

const g_GeV = Float64(EUval(GeV, NU.g))
const THR = 0.251
Y_at(m, lb) = Float64(magic(m, ArbFloat(10; bits=BITS)^ArbFloat(lb; bits=BITS))[7])

open(out_file, "w") do io
    println(io, "# wuxu_subedge_ramp.jl; tolmode=", tolmode, " g_GeV=", @sprintf("%.15g", g_GeV), " table_first_mass_g=", @sprintf("%.12g", exp(_logm1) / g_GeV),
            " dp(pi,K,K0L,p,n)=", join([@sprintf("%.6f", _DP[c]) for c in 2:6], ";"))
    println(io, "id,j,m0_g,lam,phase,log10beta,Yc,seconds")
    function ev(id, j, m, lam, phase, lb)
        t0 = time(); y = Y_at(m, lb)
        @printf(io, "%s,%d,%.10g,%.6g,%s,%.6f,%.17g,%.1f\n", id, j, Float64(m / NU.g), lam, phase, lb, y, time() - t0)
        flush(io); return y
    end
    for c in cfgs
        id = c[1]; j = parse(Int, c[2]); lam = parse(Float64, c[3]); b0 = parse(Float64, c[4])
        _LAM[] = lam
        m = m_PBH_f_list[j + 1]
        if startswith(id, "pt")                      # single-point evaluation (identity / determinism controls)
            ev(id, j, m, lam, "point", b0); continue
        end
        a, b = b0 - 0.6, b0 + 0.6
        ya = ev(id, j, m, lam, "bracket", a); yb = ev(id, j, m, lam, "bracket", b)
        while ya >= THR && a > -21.0; a = max(a - 0.6, -21.0); ya = ev(id, j, m, lam, "bracket", a); end
        while yb < THR && b < -15.0; b = min(b + 0.6, -15.0); yb = ev(id, j, m, lam, "bracket", b); end
        if !(ya < THR <= yb)
            @printf(io, "%s,%d,%.10g,%.6g,NOBRACKET,NaN,NaN,0\n", id, j, Float64(m / NU.g), lam); flush(io); continue
        end
        while b - a > 0.02
            mid = (a + b) / 2; ym = ev(id, j, m, lam, "bisect", mid)
            ym < THR ? (a = mid) : (b = mid)
        end
        r = (a + b) / 2
        for d in (-0.09, -0.06, -0.03, 0.0, 0.03, 0.06, 0.09)
            ev(id, j, m, lam, "fit", r + d)
        end
    end
end
println("DONE ", out_file)
