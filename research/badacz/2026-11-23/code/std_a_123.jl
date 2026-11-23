# Badacz (Claude): PREREG_123 (research/badacz/2026-11-23/) - native STD_A: Wu-Xu code (arXiv:2509.05618, d395183,
# main-scan.jl blob b368ba55) with the mass-loss normalisation set to BlackHawk v2.3 (REVIEW_120: f_BH/f_code = 0.5817518,
# constant to 1e-6 for 1 g <= M <= 1e10 g; external I1 DAX-S10 ROT007, M16 ROT011). Only line 80 changes:
#   d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2  ->  d_m_PBH_dt = -0.5817518 * N_PBH * NU.m_Pl^4 / m_PBH^2
# The hadron source q_h(M) (hadrons_from_PBH.dat, authors' table) is unchanged (M16 ROT011); the heating term uses the same
# d_m_PBH_dt, so total deposited energy per PBH is unchanged, only its time profile.
# Arms: base (authors' code) / std; solver def (authors' solve call) / r8 (reltol 1e-8, abstol 1e-10).
# Root of Y_code(log10 beta) = 0.251 (paper chi2 = 4 upper edge, Y map of the code):
#   mode "coarse": log10 beta in {-21,-20,-19,-18,-17,-16}; lowest upward crossing bracket; 4 bisections; final linear
#                  interpolation of Y in log10 beta between the last bracket ends.
#   mode "seed:<r>": bracket [r-0.25, r+0.25], widened by 0.25 per side (max 4 times) until it brackets; 3 bisections; same.
#   mode "coarseB": replica, grid {-20.5,...,-15.5} (different solver/bisection path), same refinement.
#   mode "timing:<lb>": pilot, one evaluation, prints wall time only.
# Lifetime gate: at the first evaluation tau = t where ln m crosses the authors' stop (bisection on the dense solution).
# Usage: julia --project=<env> std_a_123.jl <author dir> <base|std> <def|r8> <j> <coarse|seed:R> <out.csv>
using Printf
src_dir = abspath(ARGS[1]); arm = ARGS[2]; solver = ARGS[3]; jj = parse(Int, ARGS[4]); mode = ARGS[5]; outf = abspath(ARGS[6])
arm in ("base", "std") || error("arm"); solver in ("def", "r8") || error("solver")
const YSTAR = 0.251
const RFAC = "0.5817518"
full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
count(marker, full) == 1 || error("marker")
prefix = String(split(full, marker)[1])
function patch(s, old, new)
    count(old, s) == 1 || error("PATCH_NOT_UNIQUE: " * old[1:min(end, 60)])
    replace(s, old => new)
end
prefix = patch(prefix, "               n_p⁻_list, n_n̄_list\n", "               n_p⁻_list, n_n̄_list, evolution_solution\n")
arm == "std" && (prefix = patch(prefix, "d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2", "d_m_PBH_dt = -$(RFAC) * N_PBH * NU.m_Pl^4 / m_PBH^2"))
solve_old = "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
solver == "r8" && (prefix = patch(prefix, solve_old, solve_old[1:end-1] * "; reltol=1e-8, abstol=1e-10)"))
prefix_file = joinpath(src_dir, "_badacz123_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

m = m_PBH_f_list[jj + 1]
if startswith(mode, "timing:")   # pilot: one evaluation, prints wall time and steps only (no Y, no control flow)
    lb = parse(Float64, split(mode, ":")[2]); t0 = time()
    res = magic(m, ArbFloat(10.0^lb; bits=BITS); hadrons_output_flag=true)
    println("TIMING_ONLY $(arm) $(solver) j$(jj) wall_s=$(round(time() - t0; digits=1)) nsteps=$(length(res[14].t)) retcode=$(res[14].retcode)")
    exit(0)
end
io = open(outf, "a")
evals = Dict{Float64,Float64}()
first_eval = Ref(true)
function Yof(lb)
    haskey(evals, lb) && return evals[lb]
    t0 = time()
    res = magic(m, ArbFloat(10.0^lb; bits=BITS); hadrons_output_flag=true)
    Y = Float64(res[7]); sol = res[14]; tau = NaN
    if first_eval[]
        lme = sol.prob.p[3]; lo, hi = Float64(sol.t[1]), Float64(sol.t[end])
        if Float64(sol(hi)[3]) <= Float64(lme)
            for _ in 1:200
                mid = (lo + hi) / 2
                Float64(sol(mid)[3]) > Float64(lme) ? (lo = mid) : (hi = mid)
                hi - lo < 1e-12 && break
            end
            tau = Float64(EU(exp(sol(hi)[1]), -1) / NU.s)
        end
        first_eval[] = false
    end
    @printf(io, "%s,%s,%d,%.17g,%.6f,%.17g,%.17g,%.1f,%d,%s\n", arm, solver, jj, Float64(m / NU.g), lb, Y, tau, time() - t0,
            length(sol.t), string(sol.retcode))
    flush(io); evals[lb] = Y
    return Y
end
function refine(a, b, nbis)
    for _ in 1:nbis
        c = (a + b) / 2
        Yof(c) >= YSTAR ? (b = c) : (a = c)
    end
    ya, yb = Yof(a), Yof(b)
    return a + (YSTAR - ya) * (b - a) / (yb - ya)
end
root = NaN; status = "none"
if mode in ("coarse", "coarseB")   # coarseB: replica with grid shifted by +0.5 dex (different solver/bisection path)
    grid = mode == "coarse" ? [-21.0, -20.0, -19.0, -18.0, -17.0, -16.0] : [-20.5, -19.5, -18.5, -17.5, -16.5, -15.5]
    ys = [Yof(g) for g in grid]
    if ys[1] >= YSTAR
        status = "below_grid"
    else
        k = findfirst(i -> ys[i] < YSTAR && ys[i+1] >= YSTAR, 1:length(grid)-1)
        if k !== nothing
            root = refine(grid[k], grid[k+1], 4); status = "root"
        end
    end
else
    s = parse(Float64, split(mode, ":")[2]); a, b = s - 0.25, s + 0.25; ok = false
    for _ in 0:4
        if Yof(a) < YSTAR && Yof(b) >= YSTAR
            ok = true; break
        end
        Yof(a) >= YSTAR && (a -= 0.25); Yof(b) < YSTAR && (b += 0.25)
    end
    if ok
        root = refine(a, b, 3); status = "root"
    else
        status = "no_bracket"
    end
end
@printf(io, "#ROOT,%s,%s,%d,%s,%s,%.17g\n", arm, solver, jj, mode, status, root)
close(io)
println("DONE $(arm) $(solver) j$(jj) $(status) $(root)")
