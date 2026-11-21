# Badacz (Claude): PREREG_079 (research/badacz/2026-11-21/) - native rate dump.
# For each (j, log10beta) runs the authors' magic(m, beta; hadrons_output_flag=true) on the frozen Wu-Xu code
# (d395183; arm e5 = Mech-S6 charge-pair patch applied exactly as in b1_t2_contour_069.jl; default solver call, unchanged),
# and writes, at the authors' 10000 output points, the per-nucleon hadronic conversion rates computed with the
# AUTHORS' OWN cross-section functions (tool_script-parameters.jl) from the AUTHORS' OWN dense-output densities:
#   r_p2n = n_pi- sv_pi-_pTOn + n_K- sv_K-_pTOn + n_K0L sv_K0L_pTOn + n_nbar sv_nnbar_pTOn     [per proton, 1/s]
#   r_n2p = n_pi+ sv_pi+_nTOp + n_K- sv_K-_nTOp + n_K0L sv_K0L_nTOp + n_pbar sv_ppbar_nTOp     [per neutron, 1/s]
# i.e. exactly the hadronic terms of dX_n/dt in evolution_system! (dX/dt_had = (1-X) r_p2n - X r_n2p).
# Usage: julia --project=<env> rate_dump_079.jl <author dir> <orig|e5> <config: "run_id j log10beta"> <outdir>
using Printf
src_dir = abspath(ARGS[1]); arm = ARGS[2]; cfg = abspath(ARGS[3]); outdir = abspath(ARGS[4])
arm in ("orig", "e5") || error("arm")
mkpath(outdir)
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
prefix_file = joinpath(src_dir, "_badacz079_prefix_$(getpid()).jl")
write(prefix_file, prefix)
cd(src_dir) do
    include(prefix_file)
    include(joinpath(src_dir, "main-scan-parameters.jl"))
end
rm(prefix_file)

persec(r) = Float64(r * NU.s)
summ = open(joinpath(outdir, "summary_$(arm).csv"), "w")
println(summ, "# rate_dump_079 arm=$(arm) julia=$(VERSION) BITS=$(BITS)")
println(summ, "run_id,arm,j,log10beta,Y,T_last_alive_MeV,seconds")
for l in readlines(cfg)
    s = strip(l); (isempty(s) || startswith(s, "#")) && continue
    f = split(s); rid = String(f[1]); j = parse(Int, f[2]); lb = parse(Float64, f[3])
    t0 = time()
    m = m_PBH_f_list[j + 1]
    β = ArbFloat(10.0^lb; bits=BITS)
    res = magic(m, β; hadrons_output_flag=true)
    a_l, t_l, ρ_l, mP_l, nP_l, X_l, Y = res[1], res[2], res[3], res[4], res[5], res[6], res[7]
    nπm, nπp, nKm, nK0, npb, nnb = res[8], res[9], res[10], res[11], res[12], res[13]
    io = open(joinpath(outdir, "rates_$(rid).csv"), "w")
    println(io, "i,T_MeV,t_s,X,n_PBH_alive,r_p2n,r_n2p,r_p2n_pi,r_n2p_pi,r_p2n_K,r_n2p_K,r_p2n_K0L,r_n2p_K0L,r_p2n_nbar,r_n2p_pbar")
    Tlast = NaN
    for i in eachindex(a_l)
        T = from_ρ_to_T(ρ_l[i])
        pπ = persec(nπm[i] * σv_π⁻_pTOn(T)); nπ = persec(nπp[i] * σv_π⁺_nTOp(T))
        pK = persec(nKm[i] * σv_K⁻_pTOn(T)); nK = persec(nKm[i] * σv_K⁻_nTOp(T))
        pL = persec(nK0[i] * σv_K⁰ᴸ_pTOn(T)); nL = persec(nK0[i] * σv_K⁰ᴸ_nTOp(T))
        pN = persec(nnb[i] * σv_nn̄_pTOn(T)); nP = persec(npb[i] * σv_pp⁻_nTOp(T))
        alive = !iszero(nP_l[i])
        alive && (Tlast = Float64(EUval(MeV, T)))
        @printf(io, "%d,%.17g,%.17g,%.17g,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n", i,
                Float64(EUval(MeV, T)), Float64(t_l[i] / NU.s), Float64(X_l[i]), alive,
                pπ + pK + pL + pN, nπ + nK + nL + nP, pπ, nπ, pK, nK, pL, nL, pN, nP)
    end
    close(io)
    @printf(summ, "%s,%s,%d,%.6f,%.17g,%.17g,%.1f\n", rid, arm, j, lb, Float64(Y), Tlast, time() - t0)
    flush(summ)
end
close(summ)
println("DONE ", arm)
