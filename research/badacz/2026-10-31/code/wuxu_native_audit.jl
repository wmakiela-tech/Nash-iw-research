# Badacz (Claude): author-native audit of the Wu-Xu Fig. 5 scan (PREREG_034).
# Runs the AUTHORS' OWN code (Fenyutanchan/Primordial-Black-Hole @ d395183, arXiv-2509.05618/main-scan.jl up to the
# parameter-loading marker, exactly as Mech-S6 did in GitHub Actions) and the authors' SBBN cells (main.ipynb 6-7,
# copied verbatim below). Nothing in the physics is changed, except in modes "tight"/"ladder", where the single solve() call of
# magic() and the SBBN solve get explicit tolerances (tight: reltol=1e-10, abstol=1e-12 = N5; ladder: post-hoc values).
# Usage: julia --project=<env> wuxu_native_audit.jl <author arXiv-2509.05618 dir> <points.txt> <out.csv> <mode: default|tight|ladder:<reltol>:<abstol>> [<worker k> <of n>]
using Printf
src_dir = abspath(ARGS[1]); pts_file = abspath(ARGS[2]); out_file = abspath(ARGS[3]); mode = ARGS[4]
wk = length(ARGS) >= 6 ? parse(Int, ARGS[5]) : 1; nw = length(ARGS) >= 6 ? parse(Int, ARGS[6]) : 1

marker = "@info \"Loading `main-scan-parameters.jl`\""
full = read(joinpath(src_dir, "main-scan.jl"), String)
occursin(marker, full) || error("scan marker missing")
prefix = split(full, marker)[1]
solve_call = "solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(solve_call, prefix) == 1 || error("expected exactly one solve() call in magic()")
# mode "tight" = PREREG_034 N5 (reltol=1e-10, abstol=1e-12); mode "ladder:<reltol>:<abstol>" = POST-HOC tolerance ladder
tolkw = mode == "tight" ? "reltol=1e-10, abstol=1e-12" :
        startswith(mode, "ladder:") ? (tp = split(mode, ":"); "reltol=$(parse(Float64, tp[2])), abstol=$(parse(Float64, tp[3]))") :
        mode == "default" ? "" : error("mode must be default, tight or ladder:<reltol>:<abstol>")
# In non-default modes magic() also saves only at the authors' own output nodes (saveat = log.(a_list), dense = false).
# Reason: the preregistered tight run with full dense output was OOM-killed (3.6 GB anon RSS after ~27 min, 31 X).
# results_list = (sol o log).(a_list) then returns the saved node values exactly; ladder:1e-3:1e-6 is the control
# that this storage change alone does not move Y_P.
if tolkw != ""
    prefix = replace(prefix, solve_call => "solve(evolution_problem, AutoTsit5(Rosenbrock23()); $tolkw, saveat=log.(geomspace(a_f, a_end, num_points)), dense=false)")
end
prefix_file = joinpath(src_dir, "_badacz_audit_prefix_$(replace(mode, ":" => "_"))_$(wk).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))     # exact ArbFloat grids m_PBH_f_list, β_PBH_list
end
rm(prefix_file)

# ---- SBBN, verbatim from main.ipynb cells 6-7 (authors) ----
function evolution_system_SBBN!(du, u, p, η)
    a = exp(η)
    log_Xₙ, log_ρ_SM_in_EU = u
    Xₙ = exp(log_Xₙ)
    ρ_SM = EU(exp(log_ρ_SM_in_EU), 4)
    T_SM = from_ρ_to_T(ρ_SM)
    x = Q / T_SM
    Γₙ_SM = (255 / τ_n) * (12 + 6 * x + x^2) / x^5
    dXₙ_dt_SM = -Γₙ_SM * (Xₙ - (1 - Xₙ) * exp(-x))
    dXₙ_dt_decay = -Xₙ / τ_n
    dXₙ_dt = dXₙ_dt_SM + dXₙ_dt_decay
    H = sqrt(ρ_SM / (3 * NU.M_Pl^2))
    d_ln_N_ρ_d_ln_T = EUval(GeV, T_SM) * ForwardDiff.derivative(T_in_GeV -> (log ∘ Nᵨ)(GeV, T_in_GeV), EUval(GeV, T_SM))
    d_ln_N_s_d_ln_T = EUval(GeV, T_SM) * ForwardDiff.derivative(T_in_GeV -> (log ∘ Nₛ)(GeV, T_in_GeV), EUval(GeV, T_SM))
    d_log_ρ_SM_dη = -4 + d_ln_N_ρ_d_ln_T / (3 + d_ln_N_s_d_ln_T)
    du[1] = dXₙ_dt / (H * Xₙ)
    du[2] = d_log_ρ_SM_dη
    return du
end
evolution_problem_SBBN = ODEProblem(evolution_system_SBBN!,
    map(log ∘ (v -> EUval(EU, v)), [inv(1 + exp(Q / GeV(10))), (π^2 / 30) * Nᵨ(GeV(10)) * GeV(10)^4]), (0, log(1e7)))
evolution_solution_SBBN = tolkw == "" ?
    solve(evolution_problem_SBBN, AutoTsit5(Rosenbrock23())) :   # default mode: verbatim authors' call
    eval(Meta.parse("solve(evolution_problem_SBBN, AutoTsit5(Rosenbrock23()); $tolkw)"))
a_list_SBBN = geomspace(1, 1e7, 1000)
results_list_SBBN = (evolution_solution_SBBN ∘ log).(a_list_SBBN)
ρ_SM_list_SBBN = map((x -> EU(x, 4)) ∘ exp ∘ last, results_list_SBBN)
T_SM_list_SBBN = from_ρ_to_T.(ρ_SM_list_SBBN)
Xₙ_list_SBBN = (exp ∘ first).(results_list_SBBN)
permS = sortperm(Q ./ T_SM_list_SBBN)
interpS = LinearInterpolation(Xₙ_list_SBBN[permS], Q ./ T_SM_list_SBBN[permS]; extrapolation=ExtrapolationType.Linear, cache_parameters=true)
X_SBBN_nuc = interpS(Q / T_nuc)
Y_SBBN_C = 2 * X_SBBN_nuc / (1 - X_SBBN_nuc)
# N3: T'_nuc with 2 X_SBBN = 0.245 (bisection in xq = Q/T on the authors' interpolation; X decreases with xq)
target = 0.245 / 2
lo, hi = Float64(Q / T_nuc) / 2, Float64(Q / T_nuc) * 2
flo = Float64(interpS(lo)) - target; fhi = Float64(interpS(hi)) - target
flo * fhi < 0 || error("bracket failed")
for _ in 1:200
    mid = (lo + hi) / 2; fm = Float64(interpS(mid)) - target
    if fm * flo > 0; global lo = mid; global flo = fm; else; global hi = mid; end
end
xq_prime = (lo + hi) / 2
T_nuc_prime_MeV = Float64(EUval(MeV, Q / xq_prime))
T_nuc_MeV = Float64(EUval(MeV, T_nuc))

open(out_file, "w") do io
    println(io, "# SBBN Y_C(T_nuc)=", @sprintf("%.17g", Float64(Y_SBBN_C)), " X_SBBN(T_nuc)=", @sprintf("%.17g", Float64(X_SBBN_nuc)),
            " T_nuc_MeV=", @sprintf("%.17g", T_nuc_MeV), " T_nuc_prime_MeV=", @sprintf("%.17g", T_nuc_prime_MeV),
            " X_SBBN(T_nuc_prime)=", @sprintf("%.17g", Float64(interpS(xq_prime))), " mode=", mode)
    println(io, "label,j,k,m_g,beta,Yp_returned,X_nuc,Y_C,X_nuc_prime,Y_M,seconds")
    lines = filter(!isempty, readlines(pts_file))
    for (idx, line) in enumerate(lines)
        (idx - 1) % nw == wk - 1 || continue
        lab, js, ks = split(line); j = parse(Int, js); k = parse(Int, ks)
        m = m_PBH_f_list[j]; β = β_PBH_list[k]
        t0 = time()
        res = magic(m, β)
        a_list, t_list, ρ_SM_list, m_PBH_list, n_PBH_list, Xₙ_list, Yₚ = res
        T_SM_list = from_ρ_to_T.(ρ_SM_list)
        perm = sortperm(Q ./ T_SM_list)
        interp = LinearInterpolation(Xₙ_list[perm], Q ./ T_SM_list[perm]; extrapolation=ExtrapolationType.Linear, cache_parameters=true)
        Xn = interp(Q / T_nuc); Xp = interp(xq_prime)
        YC = 2 * Xn / (1 - Xn); YM = 2 * Xp
        @printf(io, "%s,%d,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.1f\n", lab, j - 1, k - 1, Float64(m / NU.g), Float64(β),
                Float64(Yₚ), Float64(Xn), Float64(YC), Float64(Xp), Float64(YM), time() - t0)
        flush(io)
    end
end
println("DONE ", out_file)
