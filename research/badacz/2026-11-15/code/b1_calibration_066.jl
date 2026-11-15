# Badacz (Claude): PREREG_066 (research/badacz/2026-11-15/) - ONE bounded native B1 test on the authors' frozen Wu-Xu code
# (d395183, main-scan.jl blob b368ba55). The authors' magic() is used unchanged except, per arm, the single solve() line:
#   archive : unchanged; (last o magic)(m_PBH_f_list[23], beta_PBH_list[k+1]) for k in KLIST (authors' own objects/bits)
#   rep013  : unchanged; magic(m_PBH_f_list[23], ArbFloat(10.0^-16.9974609375; bits=BITS); hadrons_output_flag=true)
#   A0u     : unchanged; magic(m22, beta_PBH_list[100]; hadrons_output_flag=true)
#   A0      : solve line + "; global BADACZ_SOL = evolution_solution" (capture only)
#   A1      : explicit reltol=1e-3, abstol=1e-6 (documented SciML defaults) + capture
#   A2      : as A1 plus saveat=log.(geomspace(a_f, a_end, num_points)), dense=false (= my BADACZ_TOL switch) + capture
#   A3      : reltol=1e-4, abstol=1e-7 + capture;   A4 : reltol=1e-5, abstol=1e-8 + capture
# Output: one JSON object per line. Usage: julia --project=<env> b1_calibration_066.jl <author arXiv-2509.05618 dir> <arm> <out.jsonl>
using Printf
src_dir = abspath(ARGS[1]); arm = ARGS[2]; out_file = abspath(ARGS[3])
arm in ("archive", "rep013", "A0u", "A0", "A1", "A2", "A3", "A4") || error("unknown arm $(arm)")
full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, full) || error("scan marker missing")
prefix = split(full, marker)[1]
line = "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(line, prefix) == 1 || error("expected exactly one solve line")
cap = "; global BADACZ_SOL = evolution_solution"
sv = "saveat=log.(geomspace(a_f, a_end, num_points)), dense=false"
newline = Dict(
    "A0" => line * cap,
    "A1" => "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=1e-3, abstol=1e-6)" * cap,
    "A2" => "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=1e-3, abstol=1e-6, $(sv))" * cap,
    "A3" => "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=1e-4, abstol=1e-7)" * cap,
    "A4" => "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=1e-5, abstol=1e-8)" * cap)
haskey(newline, arm) && (prefix = replace(prefix, line => newline[arm]))
prefix_file = joinpath(src_dir, "_badacz066_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)
const KLIST = 86:99                                  # authors' beta indices (0-based) inside [-17.4, -17.0]
const J = 22
io = open(out_file, "w")
vers = try Dict(string(m) => string(pkgversion(m)) for m in (DifferentialEquations, ArbNumerics)) catch err; "unavailable: " * sprint(showerror, err)[1:min(end, 80)] end
println(io, "{\"arm\":\"header\",\"julia\":\"$(VERSION)\",\"BITS\":$(BITS),\"versions\":\"$(replace(string(vers), "\"" => "'"))\",\"line_changed\":$(haskey(newline, arm))}")  # D1: quote escaping
s(x) = string(BigFloat(x; precision=BITS))
m22 = m_PBH_f_list[J + 1]
if arm == "archive"
    for k in KLIST
        t0 = time(); y = (last ∘ magic)(m22, β_PBH_list[k + 1])
        @printf(io, "{\"arm\":\"archive\",\"j\":%d,\"k\":%d,\"beta\":\"%s\",\"Y\":%.17g,\"Y_big\":\"%s\",\"seconds\":%.1f}\n",
                J, k, s(β_PBH_list[k + 1]), Float64(y), s(y), time() - t0)
        flush(io)
    end
else
    β = arm == "rep013" ? ArbFloat(10.0^-16.9974609375; bits=BITS) : β_PBH_list[100]
    t0 = time(); res = magic(m22, β; hadrons_output_flag=true); sec = time() - t0
    Y = res[7]; X = Y / (2 + Y)
    t_s = Float64.(res[2] ./ NU.s); M_g = Float64.(res[4] ./ NU.g)
    iz = findfirst(iszero, res[5])
    rec = Dict{String,Any}("arm" => arm, "j" => J, "beta" => s(β), "Y" => Float64(Y), "Y_big" => s(Y), "X_T0" => Float64(X),
                           "X_T0_big" => s(X), "seconds" => sec, "first_nPBH_zero_index_1based" => something(iz, -1),
                           "t_s_at_last_live" => isnothing(iz) ? NaN : t_s[iz - 1], "M_g_at_last_live" => isnothing(iz) ? NaN : M_g[iz - 1])
    if arm != "A0u" && arm != "rep013"
        sol = BADACZ_SOL
        rec["retcode"] = string(sol.retcode)
        for f in (:naccept, :nreject, :nf, :nw, :nsolve, :njacs)
            rec[string(f)] = try Int(getproperty(sol.stats, f)) catch; -1 end
        end
        rec["n_saved"] = length(sol.t); rec["saved_every_step"] = arm != "A2"
        lme = max(log(EUval(EU, m22)) - 20, log(EUval(EU, NU.m_Pl)))            # authors' stop threshold (as in magic)
        tf = Float64(t_PBH_formation(m22) / NU.s); m0 = Float64(m22 / NU.g)
        ts = [Float64(EU(exp(u[1]), -1) / NU.s) for u in sol.u]; lm = [u[3] for u in sol.u]
        ie = findfirst(<=(lme), lm)
        rec["stop_logm_threshold"] = Float64(lme); rec["stop_first_index"] = something(ie, -1)
        if !isnothing(ie) && ie > 1
            rec["stop_bracket_t_s"] = [ts[ie - 1], ts[ie]]
            rec["stop_bracket_M_g"] = [Float64(EU(exp(lm[ie - 1]), 1) / NU.g), Float64(EU(exp(lm[ie]), 1) / NU.g)]
            rec["M_stop_g"] = Float64(EU(exp(lme), 1) / NU.g)
            K = Float64[]
            for i in 1:(ie - 1)
                Mi = Float64(EU(exp(lm[i]), 1) / NU.g); frac = 1 - (Mi / m0)^3
                frac > 1e-3 && push!(K, (m0^3 - Mi^3) / (ts[i] - tf))
            end
            rec["Kclock_n"] = length(K)
            rec["Kclock_rel_spread"] = isempty(K) ? NaN : (maximum(K) - minimum(K)) / (sum(K) / length(K))
        end
    end
    println(io, "{" * join(["\"$(k)\":" * (v isa AbstractString ? "\"$(v)\"" : v isa AbstractVector ? "[" * join(v, ",") * "]" : string(v)) for (k, v) in rec], ",") * "}")
end
close(io)
println("DONE ", arm, " ", out_file)
