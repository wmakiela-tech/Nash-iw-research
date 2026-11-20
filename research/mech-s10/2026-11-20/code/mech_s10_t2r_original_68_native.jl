# IW_MECH_S10_T2R_NATIVE68_001 — independent native source-replica driver
# Authorized directly by the Human Moderator, 2026-11-20.
# EXACT 34 author magic() calls per process, TWO arms, one workflow job.
# NOT Badacz b1_t2_contour_069.jl, not a source-data replay.
using Printf
using SHA

length(ARGS)==3 || error("USAGE: [ORIGINAL_AUTHOR_DIR] [orig|e5] [OUTPUT_CSV]")
author_dir=abspath(ARGS[1])
arm=ARGS[2]
dest=abspath(ARGS[3])
arm in ("orig","e5") || error("INVALID_ARM")
isfile(joinpath(author_dir,"main-scan.jl")) || error("ORIGINAL_SOURCE_MISSING")

main_source=read(joinpath(author_dir,"main-scan.jl"),String)
if arm=="e5"
    patch=abspath(joinpath(@__DIR__,"..","..","..","mech-s6","2026-10-17","apply_wuxu_charge_pair_source_map.py"))
    isfile(patch) || error("FROZEN_E5_PATCH_MISSING")
    patched=tempname()*".jl"
    try
        run(Cmd(["python3","-I",patch,joinpath(author_dir,"main-scan.jl"),patched]))
        main_source=read(patched,String)
    finally
        isfile(patched) && rm(patched)
    end
end

# Fail closed on the exact author source loading boundary, without running
# any embedded scan loops located after this boundary.
marker="@info \"Loading "*string(Char(0x60))*"main-scan-parameters.jl"*string(Char(0x60))*"\""
count(marker,main_source)==1 || error("NONUNIQUE_AUTHOR_SOURCE_BOUNDARY")
prefix=split(main_source,marker;limit=2)[1]
base_solve="evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))"
count(base_solve,prefix)==1 || error("UNEXPECTED_AUTHOR_DEFAULT_SOLVER")
if arm=="orig"
    count("d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH",prefix)==1 || error("ORIG_SOURCE_UNEXPECTED")
else
    count("d_n_π_dt_from_PBH = 0.5 * dN_over_dt_π(m_PBH) * n_PBH",prefix)==1 || error("E5_SOURCE_UNEXPECTED")
end
temp_prefix=joinpath(author_dir,"_mech_s10_t2r_prefix_"*string(getpid())*".jl")
try
    write(temp_prefix,prefix)
    cd(author_dir) do
        include(temp_prefix)
        include(joinpath(author_dir,"main-scan-parameters.jl"))
    end
finally
    isfile(temp_prefix) && rm(temp_prefix)
end

# Frozen source config matched by Git blob in workflow preflight.
cfgfile=abspath(joinpath(@__DIR__,"..","..","..","badacz","2026-11-16","code",
           arm=="orig" ? "cfg069_orig_default.dat" : "cfg069_e5_default.dat"))
cfg=Dict{Int,Tuple{Float64,Float64,Float64}}()
for line in eachline(cfgfile)
    t=strip(line)
    (isempty(t) || startswith(t,"#")) && continue
    ss=split(t)
    length(ss)==4 || error("BAD_CFG_RECORD")
    jj=parse(Int,ss[1])
    cfg[jj]=(parse(Float64,ss[2]),parse(Float64,ss[3]),parse(Float64,ss[4]))
end
wanted=arm=="orig" ? Dict(22=>(-17.38,-17.06,0.02),62=>(-19.54,-19.22,0.02)) :
                      Dict(22=>(-17.10,-16.78,0.02),62=>(-19.26,-18.94,0.02))
for j in (22,62)
    cfg[j]==wanted[j] || error("FROZEN_17_NODE_CONFIG_MISMATCH")
end

mkpath(dirname(dest))
open(dest,"w") do io
    println(io,"# Mech-S10 direct Moderator 2026-11-20; original Wu-Xu d395183; native Julia=$(VERSION), arm=$(arm), 34 calls, default author tolerance, bits=$(BITS)")
    println(io,"arm,tol,j,m_g,log10beta,Y,seconds")
    flush(io)
    n=0
    for j in (22,62)
        lo,hi,step=wanted[j]
        m=m_PBH_f_list[j+1]
        for k in 0:16
            lb=round(lo+k*step;digits=6)
            k==16 && abs(lb-hi)>1e-8 && error("BAD_END_NODE")
            start=time()
            native_Y=(last ∘ magic)(m,ArbFloat(10.0^lb;bits=BITS))
            val=Float64(native_Y)
            isfinite(val) || error("NONFINITE_AUTHOR_NATIVE_Y")
            @printf(io,"%s,default,%d,%.10e,%.6f,%.17g,%.5f\n",arm,j,Float64(m/NU.g),lb,val,time()-start)
            flush(io)
            n+=1
            @printf(stdout,"NATIVE_T2R_DONE arm=%s j=%d node=%d log10beta=%.6f Y=%.17g\n",arm,j,k+1,lb,val)
            flush(stdout)
        end
    end
    n==34 || error("NATIVE_NUMBER_NOT_34")
end
println("NATIVE_MECH_S10_T2R_$(arm)_34_CALLS_PASS")
