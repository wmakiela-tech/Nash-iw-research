# Badacz (Claude): POST-HOC timing diagnostic for the left wall of the Wu-Xu Fig. 5 contour (Front B synthesis).
# Runs the AUTHORS' OWN magic() unchanged (same loader as wuxu_native_audit.jl, default tolerances) and reports, per point,
# the SM temperature when the PBH mass crosses the hadron-table edge (1e9 g) and when 99.9% of the initial mass is gone,
# plus X_n at those moments. Fraction of the initial mass radiated below the table edge is exactly 1e9 g / m_i.
# Usage: julia --project=<env> wuxu_leftwall_timing.jl <author arXiv-2509.05618 dir> <points.txt> <out.csv>
using Printf
src_dir = abspath(ARGS[1]); pts_file = abspath(ARGS[2]); out_file = abspath(ARGS[3])
marker = "@info \"Loading `main-scan-parameters.jl`\""
full = read(joinpath(src_dir, "main-scan.jl"), String)
occursin(marker, full) || error("scan marker missing")
prefix_file = joinpath(src_dir, "_badacz_timing_prefix.jl")
write(prefix_file, split(full, marker)[1])
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

function first_crossing(xs, ys, level)      # ys decreasing through level; log-linear interpolation of xs
    for i in 1:length(ys)-1
        if ys[i] > level >= ys[i+1]
            w = (log(level) - log(ys[i])) / (log(ys[i+1]) - log(ys[i]))
            return exp(log(xs[i]) + w * (log(xs[i+1]) - log(xs[i])))
        end
    end
    return NaN
end

open(out_file, "w") do io
    println(io, "label,j,k,m_g,beta,frac_mass_below_edge,T_MeV_at_edge,T_MeV_at_999,Xn_at_edge,Xn_at_999,Yp")
    for line in filter(!isempty, readlines(pts_file))
        lab, js, ks = split(line); j = parse(Int, js); k = parse(Int, ks)
        m = m_PBH_f_list[j]; β = β_PBH_list[k]
        a_list, t_list, ρ_SM_list, m_PBH_list, n_PBH_list, Xₙ_list, Yₚ = magic(m, β)
        T = [Float64(EUval(MeV, from_ρ_to_T(ρ))) for ρ in ρ_SM_list]
        mg = [Float64(mm / NU.g) for mm in m_PBH_list]
        Xn = [Float64(x) for x in Xₙ_list]
        mi = Float64(m / NU.g)
        T_edge = first_crossing(T, mg, 1e9); T_999 = first_crossing(T, mg, 1e-3 * mi)
        # X_n at those temperatures (X_n vs T, log-linear in T; T decreases along the list)
        Xat(Tq) = isnan(Tq) ? NaN : (i = findfirst(t -> t <= Tq, T); i === nothing || i == 1 ? NaN :
                  Xn[i-1] + (log(Tq) - log(T[i-1])) / (log(T[i]) - log(T[i-1])) * (Xn[i] - Xn[i-1]))
        @printf(io, "%s,%d,%d,%.10g,%.10g,%.6f,%.6g,%.6g,%.6g,%.6g,%.10g\n", lab, j - 1, k - 1, mi, Float64(β),
                1e9 / mi, T_edge, T_999, Xat(T_edge), Xat(T_999), Float64(Yₚ))
        flush(io)
    end
end
println("DONE ", out_file)
