# Badacz (Claude): PREREG_119 (research/badacz/2026-11-23/) - native no-PBH background export of the Wu-Xu code
# (arXiv:2509.05618, repo d395183, main-scan.jl blob b368ba55) and code-side mass-loss normalisation for G_EC+(a).
#
# Arms (string patches of the authors' main-scan.jl prefix, each checked to apply exactly once):
#   code  : authors' equations unchanged.
#   ad    : COUNTERFACTUAL background: line 85 d_log_ρ_SM_dη = -4 + R'/(3+S') ... replaced by the adiabatic form
#           -3(4+R')/(3+S') ... (paper Eq. 2.7, a^3 g_s T^3 = const); everything else unchanged.
#   solver: "def" = authors' solve(...) call unchanged; "r8" / "r9" = same algorithm with reltol=1e-8/1e-9,
#           abstol=1e-10/1e-11 (numerical-precision arms, no physics change).
# Every arm: beta = 0 exactly (n_PBH = 0), magic() called with hadrons_output_flag=true and patched to ALSO return the
# ODE solution object (output-only change, as in rate_dump_081.jl).
# Exports (outdir): bg_<tag>.csv = values at T_SM = 10, 1, 0.5, 0.25, 0.1 MeV and T_nuc (bisection in eta = ln a on the
# dense solution, T_SM from the authors' from_ρ_to_T); dense_<tag>.csv = 3000 points uniform in eta over T_SM <= 30 MeV;
# summary line with Y (authors' formula) and wall time.
# Optional mode "fcode": writes f_code(M) = N_BH(T_BH(M)) * m_Pl^4 [GeV^4] at the masses of BlackHawk fM.txt
# (first column, GeV), the authors' own definitions (tool_script-parameters.jl l.104-105, main-scan.jl l.80).
# Usage: julia --project=<env> bg_export_119.jl <author dir> <code|ad> <def|r8|r9> <j> <outdir> [timing_only]
#        julia --project=<env> bg_export_119.jl <author dir> fcode <fM.txt> <outdir>
using Printf
src_dir = abspath(ARGS[1]); arm = ARGS[2]
full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
count(marker, full) == 1 || error("marker")
prefix = String(split(full, marker)[1])
function patch(s, old, new)
    count(old, s) == 1 || error("PATCH_NOT_UNIQUE: " * old[1:min(end, 60)])
    replace(s, old => new)
end
solve_old = "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
ret_old = "               n_p⁻_list, n_n̄_list\n"
rho_old = "d_log_ρ_SM_dη = -4 + d_ln_N_ρ_d_ln_T / (3 + d_ln_N_s_d_ln_T) - d_m_PBH_dt * n_PBH / (H * ρ_SM)"
rho_ad = "d_log_ρ_SM_dη = -3 * (4 + d_ln_N_ρ_d_ln_T) / (3 + d_ln_N_s_d_ln_T) - d_m_PBH_dt * n_PBH / (H * ρ_SM)"
if arm == "fcode"
    fm_file = abspath(ARGS[3]); outdir = abspath(ARGS[4]); mkpath(outdir)
else
    arm in ("code", "ad") || error("arm")
    solver = ARGS[3]; jj = parse(Int, ARGS[4]); outdir = abspath(ARGS[5]); mkpath(outdir)
    timing_only = length(ARGS) >= 6 && ARGS[6] == "timing_only"
    solver in ("def", "r8", "r9") || error("solver")
    prefix = patch(prefix, ret_old, "               n_p⁻_list, n_n̄_list, evolution_solution\n")
    arm == "ad" && (prefix = patch(prefix, rho_old, rho_ad))
    solver == "r8" && (prefix = patch(prefix, solve_old, solve_old[1:end-1] * "; reltol=1e-8, abstol=1e-10)"))
    solver == "r9" && (prefix = patch(prefix, solve_old, solve_old[1:end-1] * "; reltol=1e-9, abstol=1e-11)"))
end
prefix_file = joinpath(src_dir, "_badacz119_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

if arm == "fcode"
    lines = readlines(fm_file)
    io = open(joinpath(outdir, "fcode_119.csv"), "w")
    println(io, "M_GeV,M_g,T_BH_GeV,N_rho_TBH,N_BH,f_code_GeV4,m_Pl_GeV,M_Pl_GeV")
    for l in lines[2:end]
        f = split(strip(l)); isempty(f) && continue
        MG = parse(Float64, f[1]); m = GeV(ArbFloat(MG; bits=BITS))
        TB = T_BH(m); Nr = Nᵨ(TB); NB = N_BH(TB)
        fc = EUval(GeV, NB * NU.m_Pl^4)
        @printf(io, "%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n", MG, Float64(m / NU.g), Float64(EUval(GeV, TB)),
                Float64(Nr), Float64(NB), Float64(fc), Float64(EUval(GeV, NU.m_Pl)), Float64(EUval(GeV, NU.M_Pl)))
    end
    close(io); println("DONE fcode"); exit(0)
end

tag = "$(arm)_$(solver)_j$(jj)"
t0 = time()
m = m_PBH_f_list[jj + 1]
res = magic(m, ArbFloat(0; bits=BITS); hadrons_output_flag=true)
Y = res[7]; sol = res[14]
wall = time() - t0
if timing_only
    println("TIMING_ONLY $(tag) wall_s=$(round(wall; digits=1)) nsteps=$(length(sol.t)) retcode=$(sol.retcode)")
    exit(0)
end
Tof(η) = from_ρ_to_T(EU(exp(sol(η)[2]), 4))
TMeV(η) = Float64(EUval(MeV, Tof(η)))
η0, η1 = Float64(sol.t[1]), Float64(sol.t[end])
function η_at(Tt)   # T decreasing in η; bisection on the dense solution
    lo, hi = η0, η1
    (TMeV(lo) > Tt && TMeV(hi) < Tt) || error("bracket $(Tt)")
    for _ in 1:200
        mid = (lo + hi) / 2
        TMeV(mid) > Tt ? (lo = mid) : (hi = mid)
        hi - lo < 1e-13 && break
    end
    (lo + hi) / 2
end
function row(η)
    u = sol(η); T = Tof(η)
    a = exp(big(η)); tt = Float64(EU(exp(u[1]), -1) / NU.s)
    ρ = Float64(exp(u[2])); X = Float64(exp(u[4]))
    Ns = Float64(Nₛ(T)); Nr = Float64(Nᵨ(T)); Tg = Float64(EUval(GeV, T))
    Qv = Float64(a^3 * Ns * big(Tg)^3)
    (η, tt, ρ, Float64(EUval(MeV, T)), X, Ns, Nr, Qv)
end
targets = [10.0, 1.0, 0.5, 0.25, 0.1, Float64(EUval(MeV, T_nuc))]
io = open(joinpath(outdir, "bg_$(tag).csv"), "w")
println(io, "T_target_MeV,eta,t_s,rho_GeV4,T_MeV,X_n,N_s,N_rho,Q_a3NsT3_GeV3")
for Tt in targets
    r = row(η_at(Tt))
    @printf(io, "%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n", Tt, r...)
end
close(io)
ηs = η_at(30.0); ηe = η1
io = open(joinpath(outdir, "dense_$(tag).csv"), "w")
println(io, "eta,t_s,rho_GeV4,T_MeV,X_n,N_s,N_rho,Q_a3NsT3_GeV3")
for k in 0:2999
    r = row(ηs + (ηe - ηs) * k / 2999)
    @printf(io, "%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n", r...)
end
close(io)
open(joinpath(outdir, "summary_$(tag).csv"), "w") do f
    println(f, "tag,arm,solver,j,m_init_g,Y,wall_s,nsteps,retcode,T_nuc_MeV")
    @printf(f, "%s,%s,%s,%d,%.17g,%.17g,%.1f,%d,%s,%.17g\n", tag, arm, solver, jj, Float64(m / NU.g), Float64(Y), wall,
            length(sol.t), string(sol.retcode), Float64(EUval(MeV, T_nuc)))
end
println("DONE $(tag)")
