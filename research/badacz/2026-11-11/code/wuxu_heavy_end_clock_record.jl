# Badacz (Claude): PREREG_056 (research/badacz/2026-11-11/) - native record of the thermal/mass clock at the heavy end of the
# authors' mass grid. Calls the authors' magic() (main-scan.jl @ d395183) UNCHANGED and reads its returned trajectories
# (t_list [s], rho_SM_list -> T_SM via from_rho_to_T, m_PBH_list [g]); log-linear interpolation in log T between saved points.
# Usage: julia --project=<env> wuxu_heavy_end_clock_record.jl <author arXiv-2509.05618 dir> <out.csv> <j,j,...> <log10beta,log10beta,...>
using Printf
src_dir = abspath(ARGS[1]); out_file = abspath(ARGS[2])
js = parse.(Int, split(ARGS[3], ",")); lbs = parse.(Float64, split(ARGS[4], ","))
full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, full) || error("scan marker missing")
prefix_file = joinpath(src_dir, "_badacz_clock_prefix_$(getpid()).jl")
write(prefix_file, split(full, marker)[1])
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)
const T0_MeV = Float64(EUval(MeV, T_nuc))
const T1_MeV = 0.099688851247                      # REVIEW_053 calibration T1 (2 X_SBBN(T1) = 0.245)
function at_T(Tl, yl, Tq)                          # Tl decreasing; linear interpolation of y in log T
    i = findfirst(T -> T <= Tq, Tl)
    (isnothing(i) || i == 1) && return NaN
    w = (log(Tq) - log(Tl[i-1])) / (log(Tl[i]) - log(Tl[i-1]))
    return yl[i-1] + w * (yl[i] - yl[i-1])
end
io = open(out_file, "w")
println(io, "# wuxu_heavy_end_clock_record.jl; T0_MeV=$(T0_MeV) T1_MeV=$(T1_MeV)")
println(io, "j,m0_g,log10beta,t_T1_s,t_T0_s,M_T1_g,M_T0_g,t_evap_s,M_floor_g,Yc,seconds")
for j in js, lb in lbs
    m = m_PBH_f_list[j + 1]
    sec = @elapsed res = magic(m, ArbFloat(10.0^lb; bits=BITS))
    t_s = Float64.(res[2] ./ NU.s); T_MeV = [Float64(EUval(MeV, from_ρ_to_T(r))) for r in res[3]]
    M_g = Float64.(res[4] ./ NU.g); m0 = Float64(m / NU.g)
    ie = findfirst(<=(1e-3 * m0), M_g)
    tev = isnothing(ie) ? NaN : t_s[ie]
    @printf(io, "%d,%.6e,%.4f,%.6f,%.6f,%.6e,%.6e,%.6f,%.3e,%.12f,%.1f\n", j, m0, lb,
            exp(at_T(T_MeV, log.(t_s), T1_MeV)), exp(at_T(T_MeV, log.(t_s), T0_MeV)),
            at_T(T_MeV, M_g, T1_MeV), at_T(T_MeV, M_g, T0_MeV), tev, minimum(M_g), Float64(res[7]), sec)
    flush(io)
end
close(io)
