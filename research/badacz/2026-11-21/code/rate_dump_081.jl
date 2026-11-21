# Badacz (Claude): PREREG_081 (research/badacz/2026-11-21/) - native rate dump with refined sampling at PBH death.
# Differences vs rate_dump_079.jl:
#  (1) the authors' magic() return (hadrons_output_flag branch) is patched to ALSO return the ODE solution object
#      (output-only change; solve call untouched => native Y must stay bitwise = T2, gate V1);
#  (2) all exported quantities are evaluated from that solution object on a merged ln a grid: the authors' 10000 output
#      points plus N_REF = 20000 uniform points in ln a over [ln a(i_d - 200), ln a(i_d + 2)], i_d = last alive output index;
#      hadron densities use the SAME clamp as evolution_system! (log n >= -100);
#  (3) gate V2_EXACT: at every merged point, the authors' own evolution_system! is evaluated twice (actual state; state with
#      all six hadron log-densities set to -200, i.e. clamped to e^-100) and
#      had_code = (du4_actual - du4_nohadrons) * H * X,  H = 1/(t * du1_actual),
#      is compared with the exported (1-X) r_p2n - X r_n2p. Reported: max relative difference over points where
#      |had| > 1e-6 * max|had|.
# Only points with T_SM <= 30 MeV are exported/checked (PRyMordial starts at 10 MeV).
# Usage: julia --project=<env> rate_dump_081.jl <author dir> <orig|e5> <config: "run_id j log10beta"> <outdir>
using Printf
src_dir = abspath(ARGS[1]); arm = ARGS[2]; cfg = abspath(ARGS[3]); outdir = abspath(ARGS[4])
arm in ("orig", "e5") || error("arm")
mkpath(outdir)
const N_REF = 20000
const K_BACK = 200
if arm == "e5"
    patch = joinpath(@__DIR__, "..", "..", "..", "mech-s6", "2026-10-17", "apply_wuxu_charge_pair_source_map.py")
    tmp_scan = tempname() * ".jl"; run(`python3 -I $patch $(joinpath(src_dir, "main-scan.jl")) $tmp_scan`)
    full = read(tmp_scan, String); rm(tmp_scan)
    occursin("d_n_π_dt_from_PBH = 0.5 * dN_over_dt_π(m_PBH) * n_PBH", full) || error("E5_PATCH_NOT_APPLIED")
else
    full = read(joinpath(src_dir, "main-scan.jl"), String)
end
marker = "@info \"Loading `main-scan-parameters.jl`\""
count(marker, full) == 1 || error("marker")
prefix = split(full, marker)[1]
count("evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))", prefix) == 1 || error("solve line")
ret_old = "               n_p⁻_list, n_n̄_list\n"
count(ret_old, prefix) == 1 || error("return line")
prefix = replace(prefix, ret_old => "               n_p⁻_list, n_n̄_list, evolution_solution\n")
prefix_file = joinpath(src_dir, "_badacz081_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

persec(r) = Float64(r * NU.s)
clampn(v) = EU(exp(v < -100 ? -100 : v), 3)
summ = open(joinpath(outdir, "summary_$(arm).csv"), "w")
println(summ, "# rate_dump_081 arm=$(arm) julia=$(VERSION) BITS=$(BITS) N_REF=$(N_REF) K_BACK=$(K_BACK)")
println(summ, "run_id,arm,j,log10beta,Y,T_last_alive_MeV,seconds,n_points,i_last_alive,v2_max_rel,v2_n")
for l in readlines(cfg)
    s = strip(l); (isempty(s) || startswith(s, "#")) && continue
    f = split(s); rid = String(f[1]); j = parse(Int, f[2]); lb = parse(Float64, f[3])
    t0 = time()
    m = m_PBH_f_list[j + 1]
    β = ArbFloat(10.0^lb; bits=BITS)
    res = magic(m, β; hadrons_output_flag=true)
    a_l, mP_l, Y, sol = res[1], res[4], res[7], res[14]
    p = sol.prob.p
    lme = p[3]
    fe = findfirst(≤(EU(exp(lme), 1)), mP_l)
    i_d = isnothing(fe) ? length(a_l) : fe - 1
    η_nat = log.(a_l)
    η_set = collect(η_nat)
    if !isnothing(fe) && i_d - K_BACK >= 1 && i_d + 2 <= length(a_l)
        lo, hi = η_nat[i_d - K_BACK], η_nat[i_d + 2]
        append!(η_set, [lo + (hi - lo) * k / N_REF for k in 1:N_REF-1])
    end
    η_all = sort(unique(η_set))
    io = open(joinpath(outdir, "rates_$(rid).csv"), "w")
    println(io, "i,T_MeV,t_s,X,n_PBH_alive,r_p2n,r_n2p,r_p2n_pi,r_n2p_pi,r_p2n_K,r_n2p_K,r_p2n_K0L,r_n2p_K0L,r_p2n_nbar,r_n2p_pbar,had_code_per_s")
    Tlast = NaN; maxhad = 0.0; recs = Tuple{Float64,Float64}[]
    du1 = similar(sol.u[1]); du2 = similar(sol.u[1])
    nwritten = 0
    for (i, η) in enumerate(η_all)
        u = sol(η)
        T = from_ρ_to_T(EU(exp(u[2]), 4)); X = exp(u[4])
        Float64(EUval(MeV, T)) > 30.0 && continue
        nwritten += 1
        nπm, nπp, nKm, nK0, npb, nnb = clampn(u[5]), clampn(u[6]), clampn(u[7]), clampn(u[8]), clampn(u[9]), clampn(u[10])
        pπ = persec(nπm * σv_π⁻_pTOn(T)); nπ = persec(nπp * σv_π⁺_nTOp(T))
        pK = persec(nKm * σv_K⁻_pTOn(T)); nK = persec(nKm * σv_K⁻_nTOp(T))
        pL = persec(nK0 * σv_K⁰ᴸ_pTOn(T)); nL = persec(nK0 * σv_K⁰ᴸ_nTOp(T))
        pN = persec(nnb * σv_nn̄_pTOn(T)); nP = persec(npb * σv_pp⁻_nTOp(T))
        rp = pπ + pK + pL + pN; rn = nπ + nK + nL + nP
        had = Float64(1 - X) * rp - Float64(X) * rn
        evolution_system!(du1, u, p, η)
        u0 = copy(u); u0[5:10] .= -200
        evolution_system!(du2, u0, p, η)
        tt = EU(exp(u[1]), -1)
        H = inv(tt * du1[1])
        hadc = persec((du1[4] - du2[4]) * H * X)
        alive = u[3] > lme
        alive && (Tlast = Float64(EUval(MeV, T)))
        maxhad = max(maxhad, abs(had)); push!(recs, (had, hadc))
        @printf(io, "%d,%.17g,%.17g,%.17g,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n", i,
                Float64(EUval(MeV, T)), Float64(tt / NU.s), Float64(X), alive, rp, rn, pπ, nπ, pK, nK, pL, nL, pN, nP, hadc)
    end
    close(io)
    sel = [(h, c) for (h, c) in recs if abs(h) > 1e-6 * maxhad]
    v2 = isempty(sel) ? NaN : maximum(abs(c / h - 1) for (h, c) in sel)
    @printf(summ, "%s,%s,%d,%.6f,%.17g,%.17g,%.1f,%d,%d,%.6g,%d\n", rid, arm, j, lb, Float64(Y), Tlast, time() - t0,
            nwritten, i_d, v2, length(sel))
    flush(summ)
end
close(summ)
println("DONE ", arm)
