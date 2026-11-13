# Mech-S9 ROT012: exactly ONE author-native Wu-Xu magic() call, no full scan.
# Frozen prereg: IW_MECH_S9_ROT012_ONE_POINT_NATIVE_HADRON_FLOOR_PREREG_001_20261113
# Source first Wu/Xu original d395183; floor dual RAW/EFFECTIVE first LT8 ROT014-015.
# This driver only observes existing native author 10D solution, no ODE modification.
using Printf
using SHA

length(ARGS) == 2 || error("Expected exactly [frozen_author_source_dir] [artifact_output_dir]")
source_dir, out_dir = abspath.(ARGS)
mkpath(out_dir)
source_path = joinpath(source_dir, "main-scan.jl")
main_bytes = read(source_path, String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, main_bytes) || error("AUTHOR_MAIN_SOURCE_SCAN_SPLIT_MARKER_MISSING")
occursin("hadrons_output_flag &&", main_bytes) || error("AUTHOR_NATIVE_RAW_HADRONS_CONTRACT_MISSING")
occursin("2 * Xₙ_nuc / (1 - Xₙ_nuc)", main_bytes) || error("AUTHOR_NATIVE_YCODE_CONTRACT_MISSING")
prefix = split(main_bytes, marker; limit=2)[1]
temp_path = joinpath(source_dir, "_mech_s9_rot012_author_prefix_$(getpid()).jl")
write(temp_path, prefix)
try
    cd(source_dir) do
        include(temp_path)
        include(joinpath(source_dir, "main-scan-parameters.jl"))
    end
finally
    isfile(temp_path) && rm(temp_path)
end

# Source original 0-based mass-grid point j22, GPT-native L2 V2 point on SAME source.
const J = 22
const LOG10_BETA = -16.9974609375
const T1_SOURCE_MEVCAL = 0.0996888512474581
const HADRON_NAMES = ("pi_minus", "pi_plus", "K_minus", "K0_L", "pbar", "nbar")
const SOURCE_CLAIM = "MODEL_INTERNAL_NUMERIC_TRACE_ONLY_NOT_PHYSICAL_PBH_BOUND"

mass = m_PBH_f_list[J+1]
beta = ArbFloat(10.0^LOG10_BETA; bits=BITS)
seconds_julia = @elapsed solution = magic(mass, beta; hadrons_output_flag=true)
length(solution) == 13 || error("EXPECTED_NATIVE_AUTHOR_13_OUTPUTS_GOT_$(length(solution))")

a_list, t_list, rho_sm, mass_list, n_pbh_list, X_n, Ycode,
    pi_minus, pi_plus, K_minus, K0_L, pbar, nbar = solution

hads = (pi_minus, pi_plus, K_minus, K0_L, pbar, nbar)
n = length(a_list)
n == 10000 || error("EXPECTED_DEFAULT_AUTHOR_10000_OUTPUT_POINTS_GOT_$(n)")
all(length(arr)==n for arr in (t_list,rho_sm,mass_list,n_pbh_list,X_n,hads...)) ||
    error("ORIGINAL_OUTPUT_ARRAY_LENGTH_INCONSISTENCY")

temperatures = from_ρ_to_T.(rho_sm)
ts = Float64.(t_list ./ NU.s)
tm = [Float64(EUval(MeV,T)) for T in temperatures]
lograw = Matrix{Float64}(undef,n,6)
for k in 1:6, i in 1:n
    # The source RHS is n_eff = EU(exp(max(log_n_in_EU,-100)),3).
    # Returned hadrons are n_raw = EU(exp(log_n_in_EU),3), without clamp.
    # Log BEFORE conversion to Float64: preserve raw below exp(-100).
    lograw[i,k] = Float64(log(EUval(EU,hads[k][i])))
    isfinite(lograw[i,k]) || error("NONFINITE_LOGRAW index=$i species=$k")
end
all(isfinite, tm) && all(isfinite, ts) || error("NONFINITE_T_OR_TIME")
all(diff(ts) .> 0) || error("SOURCE_TIME_NOT_MONOTONIC")
all(tm .> 0) || error("SOURCE_T_NOT_POSITIVE")
evap_idx = findfirst(iszero,n_pbh_list)
post_idx = isnothing(evap_idx) ? n+1 : evap_idx
T0 = Float64(EUval(MeV,T_nuc))
targ_idx(target) = argmin(abs.(tm .- target))

tags = ["initial" => 1,
        "near_T1_source_calibration" => targ_idx(T1_SOURCE_MEVCAL),
        "near_T0_author_nucleosynthesis" => targ_idx(T0)]
if !isnothing(evap_idx)
    evap_idx > 1 && push!(tags,"last_observed_active_PBH" => evap_idx-1)
    push!(tags,"first_observed_zero_PBH" => evap_idx)
end
push!(tags,"final_solver_output" => n)

# Source's exact six channel conversion coefficients multiplying n_eff.
# This gives an on-trajectory instantaneous RHS difference from replacing
# effective values by raw values; DOES NOT solve an alternate unclamped ODE.
function signed_on_path_floor_correction(i)
    X = X_n[i]
    T = temperatures[i]
    coeff = ((1-X)*σv_π⁻_pTOn(T),
             -X*σv_π⁺_nTOp(T),
             (1-X)*σv_K⁻_pTOn(T)-X*σv_K⁻_nTOp(T),
             (1-X)*σv_K⁰ᴸ_pTOn(T)-X*σv_K⁰ᴸ_nTOp(T),
             -X*σv_pp⁻_nTOp(T),
             (1-X)*σv_nn̄_pTOn(T))
    # Recompute exact effective−raw using ORIGINAL source EU energy units.
    extra = ntuple(k -> begin
        eff = EU(exp(max(log(EUval(EU,hads[k][i])), -100)),3)
        coeff[k]*(eff-hads[k][i])
    end,6)
    signed = sum(extra)
    return Float64(signed*NU.s), [Float64(v*NU.s) for v in extra]
end

# Complete original returned RAW histories expressed in log original energy units.
open(joinpath(out_dir,"author_native_raw_hadron_history_10000.csv"),"w") do io
    println(io, join(vcat(
        ["index","a","t_seconds","T_MeV","Xn","nPBH_zero","PBH_mass_g"],
        ["lograw_"*x for x in HADRON_NAMES],
        ["floor_active_"*x for x in HADRON_NAMES]),","))
    for i in 1:n
        parts = String[
            string(i),
            @sprintf("%.15g",Float64(a_list[i])),
            @sprintf("%.15g",ts[i]),
            @sprintf("%.15g",tm[i]),
            @sprintf("%.15g",Float64(X_n[i])),
            string(Int(iszero(n_pbh_list[i]))),
            @sprintf("%.15g",Float64(mass_list[i]/NU.g))
        ]
        append!(parts,[@sprintf("%.15g",lograw[i,k]) for k in 1:6])
        append!(parts,[string(Int(lograw[i,k]<-100)) for k in 1:6])
        println(io,join(parts,","))
    end
end

# A one-row-per-hadron summary and floor crossing first-event brackets.
open(joinpath(out_dir,"six_species_floor_summary.csv"),"w") do io
    println(io,"species,first_floor_global_idx,first_floor_postev_idx,postev_floor_samples,postev_total_samples,postev_floor_fraction,terminal_lograw,min_postev_lograw,max_postev_lograw,global_below_floor_samples,first_floor_crossing_prior_log,first_floor_crossing_new_log")
    for k in 1:6
        flags = [lograw[i,k]<-100 for i in 1:n]
        first_floor = findfirst(identity,flags)
        post_fl = post_idx<=n ? findfirst(i -> flags[i],post_idx:n) : nothing
        npost = post_idx<=n ? n-post_idx+1 : 0
        nbad = npost>0 ? count(identity,flags[post_idx:n]) : 0
        mn = npost>0 ? minimum(lograw[post_idx:n,k]) : NaN
        mx = npost>0 ? maximum(lograw[post_idx:n,k]) : NaN
        pre = isnothing(first_floor) || first_floor==1 ? NaN : lograw[first_floor-1,k]
        new = isnothing(first_floor) ? NaN : lograw[first_floor,k]
        vals = (HADRON_NAMES[k],
                isnothing(first_floor) ? "NA" : string(first_floor),
                isnothing(post_fl) ? "NA" : string(post_fl),
                string(nbad),string(npost),
                npost>0 ? @sprintf("%.10g",nbad/npost) : "NA",
                @sprintf("%.14g",lograw[n,k]),
                @sprintf("%.14g",mn),@sprintf("%.14g",mx),
                string(count(identity,flags)),
                @sprintf("%.14g",pre),
                @sprintf("%.14g",new))
        println(io,join(vals,","))
    end
end

# Precisely indexed native diagnostics, with source target-temperature mismatch.
open(joinpath(out_dir,"selected_source_snapshots.csv"),"w") do io
    println(io,"tag,index,T_MeV,t_seconds,delta_T_from_target_MeV,Xn,nB_cm_minus3,evaporated_flag,floor_species_count,signed_delta_Xdot_floor_per_second,absolute_species_contribution_sum_per_second,delta_pi_minus,delta_pi_plus,delta_K_minus,delta_K0_L,delta_pbar,delta_nbar")
    for (tag,i) in tags
        nB = η_B*(2*ζ₃*temperatures[i]^3/π^2)
        b_cm3 = Float64(nB * (1e-2*NU.m)^3)
        d,details=signed_on_path_floor_correction(i)
        target = tag=="near_T1_source_calibration" ? T1_SOURCE_MEVCAL :
                 tag=="near_T0_author_nucleosynthesis" ? T0 : tm[i]
        line = String[
            tag,string(i),@sprintf("%.16g",tm[i]),
            @sprintf("%.16g",ts[i]),@sprintf("%.16g",tm[i]-target),
            @sprintf("%.16g",Float64(X_n[i])),
            @sprintf("%.16g",b_cm3),
            string(Int(iszero(n_pbh_list[i]))),
            string(count(k -> lograw[i,k]<-100, 1:6)),
            @sprintf("%.16e",d),
            @sprintf("%.16e",sum(abs,details))
        ]
        append!(line,[@sprintf("%.16e",v) for v in details])
        println(io,join(line,","))
    end
end

open(joinpath(out_dir,"native_source_summary.txt"),"w") do io
    println(io,"RESEARCH_ID=IW_MECH_S9_ROT012_SINGLE_PINNED_ORIGINAL_WUXU_RAW_HADRON_FLOOR_DIAGNOSTIC")
    println(io,"ORIGINAL_FIRST_AUTHORS=Wu-Xu")
    println(io,"ORIGINAL_FROZEN_COMMIT=d395183674cace6c9906a8911bdeb7234ba4040d")
    println(io,"ORIGINAL_MAIN_SCAN_SOURCE_SHA256=",bytes2hex(sha256(main_bytes)))
    println(io,"NO_AUTHOR_SOURCE_MODIFICATIONS=TRUE")
    println(io,"JULIA_VERSION=",VERSION)
    println(io,"BITS=",BITS)
    println(io,"AUTHOR_NATIVE_MAGIC_CALL_COUNT=1")
    println(io,"MAGIC_RETURN_SLOTS=",length(solution))
    println(io,"MAGIC_OUTPUT_ARRAY_LENGTH=",n)
    println(io,"J_ZERO_BASED=",J)
    println(io,"MASS_G=",Float64(mass/NU.g))
    println(io,"LOG10_BETA=",LOG10_BETA)
    println(io,"BETA=",Float64(beta))
    println(io,"NATIVE_YCODE_AUTHOR=",Float64(Ycode))
    println(io,"T0_ME_V=",T0)
    println(io,"T1_ME_V_FROZEN_BADACZ_SBBN=",T1_SOURCE_MEVCAL)
    println(io,"PBH_FIRST_ZERO_INDEX=",isnothing(evap_idx) ? "NOT_OBSERVED" : string(evap_idx))
    println(io,"PBH_POSTEV_FIRST_INDEX=",post_idx<=n ? string(post_idx) : "NO_POSTEV")
    println(io,"NATIVE_EXECUTION_SECONDS=",seconds_julia)
    println(io,"RAW_VS_EFFECTIVE_FLOOR_LOG_THRESHOLD=-100")
    println(io,"ACTIVE_IF_RAW_LOG_EU_LESS_THAN_MINUS_100=true")
    println(io,"HADRONS_RETURNED_ARE_RAW_NOT_CLAMPED=true")
    println(io,"NO_ALTERNATE_CLAMPED_VS_UNCLAMPED_ODE_RUN=true")
    println(io,"CLAIM_CEILING=",SOURCE_CLAIM)
    for (tag,i) in tags
        println(io,tag,"_index=",i," time_sec=",ts[i]," T_MeV=",tm[i],
            " n_floor=",count(k -> lograw[i,k]<-100,1:6))
    end
end

println("ROT012_NATIVE_SINGLE_ORIGINAL_MAGIC_PASS")
println("source=j22 log10beta=",LOG10_BETA," arrays=",length(solution),
        " points=",n," first_evaporated_index=",evap_idx," native_yp=",Float64(Ycode))
println("ROT012_FLOOR_AT_T0=",count(k -> lograw[targ_idx(T0),k]<-100,1:6),
    " T1=",count(k -> lograw[targ_idx(T1_SOURCE_MEVCAL),k]<-100,1:6),
    " FINAL=",count(k -> lograw[n,k]<-100,1:6))
