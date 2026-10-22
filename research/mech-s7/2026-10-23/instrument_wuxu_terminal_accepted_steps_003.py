#!/usr/bin/env python3
"""Fail-closed source patch to trace accepted 10D solver steps in audited Wu-Xu main-scan.jl.
No changes to the physical ODE right-hand side. Adds explicit solver tolerances
and one CSV of accepted states per branch. Julia source MUST match audited solver marker.
The patch and emitted Julia code are NOT a substitute for runtime execution.
"""
from __future__ import annotations
import argparse
from pathlib import Path

SOLVE='    evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))'
TAIL='@info "Loading `main-scan-parameters.jl`"'
INJECT=r'''
    # Mech-S7 terminal-source probe: accepted adaptive steps, not RHS eval/rejected steps.
    _mech_rtol = parse(Float64, get(ENV, "MECH_RTOL", "1e-6"))
    _mech_atol = parse(Float64, get(ENV, "MECH_ATOL", "1e-8"))
    evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23());
        reltol=_mech_rtol, abstol=_mech_atol,
        save_everystep=true, dense=true)
    if haskey(ENV, "MECH_TRACE_DIR")
        mkpath(ENV["MECH_TRACE_DIR"])
        label = get(ENV, "MECH_LABEL", "unnamed")
        tracepath = joinpath(ENV["MECH_TRACE_DIR"], "accepted_" * label * ".csv")
        cutoff = log_m_PBH_evaporated_in_EU
        open(tracepath, "w") do io
            println(io, "step,eta,t_sec,T_MeV,M_PBH_g,source_active,below_1e9g,Xn," *
                "log_n_pi_minus,log_n_pi_plus,log_n_K_minus,log_n_K0L,log_n_pbar,log_n_nbar," *
                "A_GeV,B_GeV,F_GeV,floor_count,pi_emission_GeV,K_emission_GeV,K0L_emission_GeV,p_emission_GeV,n_emission_GeV")
            for (idx,(eta,v)) in enumerate(zip(evolution_solution.t,evolution_solution.u))
                mass = EU(exp(v[3]), 1)
                T = from_ρ_to_T(EU(exp(v[2]), 4))
                X = exp(v[4])
                active = v[3] > cutoff
                n = [EU(exp(max(v[j], -100)), 3) for j in 5:10]
                ff = count(j -> v[j] < -100, 5:10)
                A = n[1]*σv_π⁻_pTOn(T) + n[3]*σv_K⁻_pTOn(T) +
                    n[4]*σv_K⁰ᴸ_pTOn(T) + n[6]*σv_nn̄_pTOn(T)
                B = n[2]*σv_π⁺_nTOp(T) + n[3]*σv_K⁻_nTOp(T) +
                    n[4]*σv_K⁰ᴸ_nTOp(T) + n[5]*σv_pp⁻_nTOp(T)
                F = (1-X)*A-X*B
                rate = if active
                    [dN_over_dt_π(mass),dN_over_dt_K(mass),dN_over_dt_K⁰ᴸ(mass),
                     dN_over_dt_proton(mass),dN_over_dt_neutron(mass)]
                else
                    [zero(GeV(1)) for _ in 1:5]
                end
                vals = Any[idx,Float64(eta),Float64(EU(exp(v[1]),-1)/NU.s),
                    Float64(T/MeV(1)),Float64(mass/NU.g),Int(active),
                    Int(active && mass < 1e9*NU.g), Float64(X)]
                append!(vals, [Float64(v[j]) for j in 5:10])
                append!(vals, [Float64(EUval(GeV,A)),Float64(EUval(GeV,B)),
                    Float64(EUval(GeV,F)),ff])
                append!(vals,[Float64(EUval(GeV,r)) for r in rate])
                println(io,join(vals,","))
            end
        end
        open(joinpath(ENV["MECH_TRACE_DIR"],"meta_"*label*".txt"),"w") do io
            println(io,"branch=",label)
            println(io,"reltol=",_mech_rtol," abstol=",_mech_atol)
            println(io,"accepted_state_count=",length(evolution_solution.t))
            println(io,"solver_stats=",repr(evolution_solution.stats))
        end
    end
'''.lstrip('\n').rstrip()

def patch(text):
    if text.count(SOLVE)!=1 or text.count(TAIL)!=1:
        raise RuntimeError('FAIL-CLOSED: source solve or scan marker differs from audited revision')
    if 'MECH_TRACE_DIR' in text:
        raise RuntimeError('already instrumented')
    return text.replace(SOLVE,INJECT,1)

def main():
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path)
    a=p.parse_args(); src=a.input.read_text(encoding='utf-8');s=patch(src)
    a.output.write_text(s,encoding='utf-8')
    print('PASS: exact audited solver site; explicit tolerances + accepted-step trace inserted')
if __name__=='__main__':main()