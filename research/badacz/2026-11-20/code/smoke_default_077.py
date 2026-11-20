import sys, time, json
sys.path.insert(0, "/home/claude/bbn077/src/PRyMordial")
import PRyM.PRyM_init as PRyMini
PRyMini.verbose_flag = False
PRyMini.smallnet_flag = True
PRyMini.julia_flag = False
t0 = time.time()
import PRyM.PRyM_main as PRyMmain
res = PRyMmain.PRyMclass().PRyMresults()
print(json.dumps({"Neff": float(res[0]), "YP_CMB": float(res[3]), "YP_BBN": float(res[4]), "DH_e5": float(res[5]),
                  "tau_n": PRyMini.tau_n, "Omegabh2": PRyMini.Omegabh2, "eta0b": PRyMini.eta0b, "seconds": time.time()-t0}))
