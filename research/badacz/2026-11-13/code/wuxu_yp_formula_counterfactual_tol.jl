# Badacz (Claude): PREREG_064 (research/badacz/2026-11-13/) - copy of 2026-11-08/code/wuxu_yp_formula_counterfactual.jl
# (PREREG_051/REVIEW_053) with ONE addition: env BADACZ_TOL="<reltol>:<abstol>" switches the solver tolerance exactly as in
# 2026-11-08/code/wuxu_band_kernel.jl and 2026-11-11/code/wuxu_heavy_end_clock_record.jl; unset = default path, unchanged.
# Original header follows.
# Badacz (Claude): PREREG_051 (research/badacz/2026-11-08/) - Y_P formula counterfactual in the AUTHORS' native code.
# The authors' magic() (main-scan.jl, commit d395183) evolves X_n = n/(n+p) (initial value 1/(1+exp(Q/T)), decay -X_n/tau_n)
# and returns Y_P = 2 X_nuc / (1 - X_nuc) at T_nuc = 0.0781852706883 MeV (line 210). This driver does NOT modify the ODE:
# it calls magic() unchanged, takes the returned (rho_SM_list, X_n_list), rebuilds the authors' own interpolation of X_n on Q/T
# and evaluates X_n at T0 = T_nuc and at T1, where T1 solves 2 X_SBBN(T1) = 0.245 on the SBBN trajectory (beta = 1e-30).
# Usage: julia --project=<env> wuxu_yp_formula_counterfactual.jl <author arXiv-2509.05618 dir> <out.csv> <configs file>
#   config lines: "grid <id> <j> <center_log10beta> <dlo> <dhi> <step>"  (points center+dlo .. center+dhi)
#                 "scan <id> <j> <lo_log10beta> <hi_log10beta> <step>"
#   j is 0-based in the authors' mass grid (6e8..1e10 g, 100 points). SBBN calibration always runs first (j = 22 and j = 62).
using Printf
src_dir = abspath(ARGS[1]); out_file = abspath(ARGS[2]); cfg_file = abspath(ARGS[3])
cfgs = [split(l) for l in readlines(cfg_file) if !isempty(strip(l)) && !startswith(strip(l), "#")]
full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, full) || error("scan marker missing")
occursin("2 * Xₙ_nuc / (1 - Xₙ_nuc)", full) || error("authors' Y_P line not found")
prefix_file = joinpath(src_dir, "_badacz_yp_prefix_$(getpid()).jl")
prefix = split(full, marker)[1]
solve_call = "solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(solve_call, prefix) == 1 || error("expected exactly one solve() call in magic()")
tolmode = get(ENV, "BADACZ_TOL", "default")
if tolmode != "default"
    tp = split(tolmode, ":")
    prefix = replace(prefix, solve_call => "solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=$(parse(Float64, tp[1])), abstol=$(parse(Float64, tp[2])), saveat=log.(geomspace(a_f, a_end, num_points)), dense=false)")
end
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

const g_GeV = Float64(EUval(GeV, NU.g))
const T0_MeV = Float64(EUval(MeV, T_nuc))

function x_interp(m, β)
    res = magic(m, β)
    ρ_SM_list, Xₙ_list, Yp = res[3], res[6], res[7]
    T_SM_list = from_ρ_to_T.(ρ_SM_list)
    perm = sortperm(Q ./ T_SM_list)
    itp = LinearInterpolation(Xₙ_list[perm], Q ./ T_SM_list[perm]; extrapolation=ExtrapolationType.Linear, cache_parameters=true)
    return itp, Float64(Yp)
end
xat(itp, T_MeV) = Float64(itp(Q / MeV(T_MeV)))

io = open(out_file, "w")
println(io, "# wuxu_yp_formula_counterfactual_tol.jl; tolmode=$(tolmode); T0_MeV=$(T0_MeV)")
# ---- SBBN calibration -------------------------------------------------------------------------------------------
cal = Dict{Int,Any}()
for jc in (22, 62)
    m = m_PBH_f_list[jc + 1]
    t = @elapsed (itp, Yp) = x_interp(m, ArbFloat(1e-30; bits=BITS))
    x0 = xat(itp, T0_MeV)
    lo, hi = T0_MeV, 10 * T0_MeV                       # X increases with T; bracket 2X = 0.245
    (2 * xat(itp, lo) < 0.245 && 2 * xat(itp, hi) > 0.245) || error("T1 not bracketed")
    for _ in 1:200
        mid = sqrt(lo * hi); (2 * xat(itp, mid) < 0.245 ? (lo = mid) : (hi = mid))
        hi / lo - 1 < 1e-14 && break
    end
    T1 = sqrt(lo * hi)
    cal[jc] = (x0, T1, xat(itp, T1), Yp)
    @printf(io, "# SBBN j=%d m_g=%.6e: X0s=%.12f Ycode_native=%.12f Ycode_recomp=%.12f T1_MeV=%.12f X1s=%.12f seconds=%.1f\n",
            jc, Float64(m / NU.g), x0, Yp, 2x0 / (1 - x0), T1, xat(itp, T1), t)
    flush(io)
end
const T1_MeV = cal[22][2]
println(io, "id,j,m_g,log10beta,X_T0,X_T1,Yc_native,Yc_recomp,seconds"); flush(io)
function point(id, j, lb)
    m = m_PBH_f_list[j + 1]
    t = @elapsed (itp, Yp) = x_interp(m, ArbFloat(10.0^lb; bits=BITS))
    x0, x1 = xat(itp, T0_MeV), xat(itp, T1_MeV)
    @printf(io, "%s,%d,%.6e,%.6f,%.15f,%.15f,%.15f,%.15f,%.1f\n", id, j, Float64(m / NU.g), lb, x0, x1, Yp, 2x0 / (1 - x0), t)
    flush(io)
end
for c in cfgs
    if c[1] == "grid"
        id, j, ctr, dlo, dhi, st = c[2], parse(Int, c[3]), parse(Float64, c[4]), parse(Float64, c[5]), parse(Float64, c[6]), parse(Float64, c[7])
        for d in dlo:st:(dhi + 1e-9); point(id, j, round(ctr + d; digits=6)); end
    elseif c[1] == "scan"
        id, j, lo, hi, st = c[2], parse(Int, c[3]), parse(Float64, c[4]), parse(Float64, c[5]), parse(Float64, c[6])
        for lb in lo:st:(hi + 1e-9); point(id, j, round(lb; digits=6)); end
    else
        error("unknown config $(c[1])")
    end
end
close(io)
