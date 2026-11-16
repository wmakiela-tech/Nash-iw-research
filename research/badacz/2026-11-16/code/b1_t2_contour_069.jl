# Badacz (Claude): PREREG_069 (research/badacz/2026-11-16/) - B1 question Q-B, test T2 (Moderator-authorized 16 XI 2026 16:47).
# Native contour of the authors' observable Y_C = 2X/(1-X) at T_nuc (authors' (last o magic)) on dense log10(beta) grids,
# two arms on the authors' frozen Wu-Xu code (d395183, main-scan.jl blob b368ba55):
#   orig : unchanged
#   e5   : Mech-S6 charge-pair source map (research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py, unchanged;
#          pi+/-, K+/-, p+pbar, n+nbar aggregate rates x 1/2 into each tracked state; K0L unchanged) = REVIEW_038 variant E5
# tol  : default (authors' solve line unchanged) or 1e-4 (explicit reltol=1e-4, abstol=1e-7, dense output kept; as A3 of PREREG_066)
# Mass objects: authors' m_PBH_f_list[j+1]; beta = ArbFloat(10.0^lb; bits=BITS) with lb rounded to 6 decimals (as REVIEW_065 grids).
# Config lines: "<j> <lb_lo> <lb_hi> <step>". Output CSV: arm,tol,j,m_g,log10beta,Y,seconds (Y with 17 significant digits).
# Usage: julia --project=<env> b1_t2_contour_069.jl <author arXiv-2509.05618 dir> <orig|e5> <default|1e-4> <config> <out.csv>
using Printf
src_dir = abspath(ARGS[1]); arm = ARGS[2]; tol = ARGS[3]; cfg = abspath(ARGS[4]); out_file = abspath(ARGS[5])
arm in ("orig", "e5") || error("arm must be orig or e5")
tol in ("default", "1e-4") || error("tol must be default or 1e-4")
if arm == "e5"
    patch = joinpath(@__DIR__, "..", "..", "..", "mech-s6", "2026-10-17", "apply_wuxu_charge_pair_source_map.py")
    tmp_scan = tempname() * ".jl"
    run(`python3 -I $patch $(joinpath(src_dir, "main-scan.jl")) $tmp_scan`)
    full = read(tmp_scan, String); rm(tmp_scan)
else
    full = read(joinpath(src_dir, "main-scan.jl"), String)
end
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, full) || error("scan marker missing")
prefix = split(full, marker)[1]
line = "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(line, prefix) == 1 || error("expected exactly one solve line")
tol == "1e-4" && (prefix = replace(prefix, line => "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=1e-4, abstol=1e-7)"))
prefix_file = joinpath(src_dir, "_badacz069_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)
pts = Tuple{Int,Float64}[]
for l in readlines(cfg)
    s = strip(l); (isempty(s) || startswith(s, "#")) && continue
    f = split(s); j = parse(Int, f[1]); lo, hi, st = parse.(Float64, f[2:4])
    n = round(Int, (hi - lo) / st)
    for k in 0:n
        push!(pts, (j, round(lo + k * st; digits=6)))
    end
end
io = open(out_file, "w")
println(io, "# b1_t2_contour_069 arm=$(arm) tol=$(tol) julia=$(VERSION) BITS=$(BITS) DiffEq=$(pkgversion(DifferentialEquations)) ArbNumerics=$(pkgversion(ArbNumerics)) npts=$(length(pts))")
println(io, "arm,tol,j,m_g,log10beta,Y,seconds")
flush(io)
for (j, lb) in pts
    local t0 = time()
    y = (last ∘ magic)(m_PBH_f_list[j + 1], ArbFloat(10.0^lb; bits=BITS))
    @printf(io, "%s,%s,%d,%.10e,%.6f,%.17g,%.1f\n", arm, tol, j, Float64(m_PBH_f_list[j + 1] / NU.g), lb, Float64(y), time() - t0)
    flush(io)
end
close(io)
println("DONE ", arm, " ", tol, " ", length(pts))
