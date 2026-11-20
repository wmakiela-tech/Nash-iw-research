# Badacz (Claude): PREREG_077 (research/badacz/2026-11-20/) - CODE arm.
# Linear response of the authors' observable Y_C = 2X/(1-X) at T_nuc (authors' (last o magic)) to an
# instantaneous neutron-fraction kick at SM temperature T_p, on the authors' frozen Wu-Xu code (d395183,
# main-scan.jl blob b368ba55), with PBHs switched off in practice (beta = 1e-30, mass j22 as in QA rows).
# Patch: the single solve line receives `callback=IW077_CB[]` (nothing => unchanged behaviour). The callback is a
# ContinuousCallback on T_SM(u) - T_p (T_SM from u[2] exactly as in evolution_system!), whose affect! applies
#   sign=+1 (p->n): X -> X + A(1-X);   sign=-1 (n->p): X -> X - A X;   to u[4] = log X.
# tol: default (authors' solve call) or 1e-4 (reltol=1e-4, abstol=1e-7, as A3 of PREREG_066 / T2).
# Config lines: "<run_id> <T_MeV> <sign> <A>" (sign 0 = no kick). Output CSV with 17 significant digits.
# Usage: julia --project=<env> code_gain_077.jl <author arXiv-2509.05618 dir> <default|1e-4> <config> <out.csv>
using Printf
src_dir = abspath(ARGS[1]); tol = ARGS[2]; cfg = abspath(ARGS[3]); out_file = abspath(ARGS[4])
tol in ("default", "1e-4") || error("tol must be default or 1e-4")
full = read(joinpath(src_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, full) || error("scan marker missing")
prefix = split(full, marker)[1]
line = "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(line, prefix) == 1 || error("expected exactly one solve line")
newline = tol == "default" ?
    "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); callback=IW077_CB[])" :
    "evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()); reltol=1e-4, abstol=1e-7, callback=IW077_CB[])"
prefix = replace(prefix, line => newline)
const IW077_CB = Ref{Any}(nothing)
const IW077_LOG = Any[]
prefix_file = joinpath(src_dir, "_badacz077_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

function iw077_make_cb(T_MeV::Float64, sgn::Int, A::Float64)
    cond(u, η, integ) = EUval(MeV, from_ρ_to_T(EU(exp(u[2]), 4))) - T_MeV
    function aff!(integ)
        X = exp(integ.u[4])
        Xn = sgn > 0 ? X + A * (1 - X) : X - A * X
        integ.u[4] = log(Xn)
        push!(IW077_LOG, (Float64(integ.t), Float64(X), Float64(Xn)))
        nothing
    end
    return ContinuousCallback(cond, aff!)
end

runs = Tuple{String,Float64,Int,Float64}[]
for l in readlines(cfg)
    s = strip(l); (isempty(s) || startswith(s, "#")) && continue
    f = split(s)
    push!(runs, (String(f[1]), parse(Float64, f[2]), parse(Int, f[3]), parse(Float64, f[4])))
end
j = 22
m = m_PBH_f_list[j + 1]
β = ArbFloat(10.0^(-30.0); bits=BITS)
io = open(out_file, "w")
println(io, "# code_gain_077 tol=$(tol) julia=$(VERSION) BITS=$(BITS) DiffEq=$(pkgversion(DifferentialEquations)) ArbNumerics=$(pkgversion(ArbNumerics)) j=$(j) log10beta=-30 nruns=$(length(runs))")
println(io, "run_id,tol,T_MeV,sign,A,Y,n_kicks,eta_kick,X_before,X_after,seconds")
flush(io)
for (rid, T_MeV, sgn, A) in runs
    empty!(IW077_LOG)
    IW077_CB[] = sgn == 0 ? nothing : iw077_make_cb(T_MeV, sgn, A)
    local t0 = time()
    y = (last ∘ magic)(m, β)
    nk = length(IW077_LOG)
    ek, xb, xa = nk >= 1 ? IW077_LOG[1] : (NaN, NaN, NaN)
    @printf(io, "%s,%s,%.6g,%d,%.6g,%.17g,%d,%.17g,%.17g,%.17g,%.1f\n", rid, tol, T_MeV, sgn, A, Float64(y), nk, ek, xb, xa, time() - t0)
    flush(io)
end
close(io)
println("DONE ", tol, " ", length(runs))
