using DelimitedFiles

source_file = abspath(ARGS[1])
mass_g = parse(Float64, ARGS[2])
beta_f = parse(Float64, ARGS[3])
label = ARGS[4]
outdir = abspath(ARGS[5])
mkpath(outdir)

cd(dirname(source_file)) do
    include(source_file)
end

m = ArbFloat(mass_g; bits=BITS) * NU.g
beta = ArbFloat(beta_f; bits=BITS)

res = magic(m, beta; num_points=1600, hadrons_output_flag=true)

a_list, t_list, rho_sm_list, m_list, npbh_list, xn_list, yp,
n_pim_list, n_pip_list, n_km_list, n_k0_list, n_pb_list, n_nb_list = res

T_list = from_ρ_to_T.(rho_sm_list)

tofloat(x) = Float64(x)
tosec(x) = Float64(x / NU.s)
togev(x) = Float64(EUval(GeV, x))
togram(x) = Float64(x / NU.g)
tocm3(x) = Float64(x * (1e-2 * NU.m)^3)

function rate_A(i)
    T = T_list[i]
    n_pim_list[i] * σv_π⁻_pTOn(T) +
    n_km_list[i] * σv_K⁻_pTOn(T) +
    n_k0_list[i] * σv_K⁰ᴸ_pTOn(T) +
    n_nb_list[i] * σv_nn̄_pTOn(T)
end

function rate_B(i)
    T = T_list[i]
    n_pip_list[i] * σv_π⁺_nTOp(T) +
    n_km_list[i] * σv_K⁻_nTOp(T) +
    n_k0_list[i] * σv_K⁰ᴸ_nTOp(T) +
    n_pb_list[i] * σv_pp⁻_nTOp(T)
end

A_list = [rate_A(i) for i in eachindex(a_list)]
B_list = [rate_B(i) for i in eachindex(a_list)]
F_list = [(1 - xn_list[i]) * A_list[i] - xn_list[i] * B_list[i] for i in eachindex(a_list)]

function floor_active(n, npbh)
    iszero(npbh) && return false
    return log(EUval(EU, n)) < -100
end

species = (
    ("pi_minus", n_pim_list),
    ("pi_plus", n_pip_list),
    ("K_minus", n_km_list),
    ("K0L", n_k0_list),
    ("pbar", n_pb_list),
    ("nbar", n_nb_list),
)

floor_flags = Dict(name => [floor_active(arr[i], npbh_list[i]) for i in eachindex(a_list)]
                   for (name, arr) in species)

traj = joinpath(outdir, "trajectory_$(label).csv")
open(traj, "w") do io
    println(io,
        "i,a,t_sec,T_GeV,m_PBH_g,n_PBH_cm3,Xn," *
        "n_pi_minus_cm3,n_pi_plus_cm3,n_K_minus_cm3,n_K0L_cm3,n_pbar_cm3,n_nbar_cm3," *
        "A_GeV,B_GeV,F_had_GeV,source_active,below_1e9g," *
        "floor_pi_minus,floor_pi_plus,floor_K_minus,floor_K0L,floor_pbar,floor_nbar"
    )
    for i in eachindex(a_list)
        source_active = !iszero(npbh_list[i])
        below_edge = source_active && togram(m_list[i]) < 1e9
        vals = [
            i, tofloat(a_list[i]), tosec(t_list[i]), togev(T_list[i]), togram(m_list[i]),
            tocm3(npbh_list[i]), Float64(xn_list[i]),
            tocm3(n_pim_list[i]), tocm3(n_pip_list[i]), tocm3(n_km_list[i]),
            tocm3(n_k0_list[i]), tocm3(n_pb_list[i]), tocm3(n_nb_list[i]),
            togev(A_list[i]), togev(B_list[i]), togev(F_list[i]),
            Int(source_active), Int(below_edge),
            Int(floor_flags["pi_minus"][i]), Int(floor_flags["pi_plus"][i]),
            Int(floor_flags["K_minus"][i]), Int(floor_flags["K0L"][i]),
            Int(floor_flags["pbar"][i]), Int(floor_flags["nbar"][i]),
        ]
        println(io, join(vals, ","))
    end
end

summary = joinpath(outdir, "summary_$(label).txt")
open(summary, "w") do io
    println(io, "label=$(label)")
    println(io, "mass_g=$(mass_g)")
    println(io, "beta=$(beta_f)")
    println(io, "Yp=$(Float64(yp))")
    println(io, "n_points=$(length(a_list))")
    println(io, "source_active_points=$(count(!iszero, npbh_list))")
    println(io, "source_active_below_1e9g_points=$(count(i -> !iszero(npbh_list[i]) && togram(m_list[i]) < 1e9, eachindex(a_list)))")
    for (name, _) in species
        println(io, "floor_$(name)_points=$(count(identity, floor_flags[name]))")
    end
end

println("WROTE ", traj)
println("WROTE ", summary)
println("Yp=", Float64(yp))
