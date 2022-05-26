from collections import Counter, defaultdict
import ase
import numpy as np

def get_N(specfile):
    spec = []
    time = []
    with open(specfile) as f:
        for line in f:
            s = line.split()
            time.append(int(s[1].strip(':')))
            s_step = defaultdict(int)
            for ss, nn in zip(s[2::2], [int(x) for x in s[3::2]]):
                s_step[ss] = nn
            spec.append(s_step)     
    step_tot = int(time[1]) - int(time[0])
    return spec, step_tot


def get_reactions(rfile):
    occs = []
    with open(rfile) as f:
        for line in f:
            s = line.split()
            occs.append((int(s[0]), Counter(s[1].split('->')[0].split('+')), s[1]))
    return occs

def get_rate(species,formula):
    a = 3.7601399999999998e+01
    timestep = 0.1 * 10**-15 # s
    N, step_tot =get_N(species)
    occs = get_reactions(formula)
    cell = np.array([a, a, a]) # A

    time_tot = step_tot * timestep
    cell *= 10**-8 # A to cm
    V = np.prod(cell)
    V *= ase.units.mol # V * NA
    
    with open("rate.txt","w") as ratefile:
        for occ, reacts, reactions in occs:
            # k = occ_tot / ( V * time_tot * c_tot )
            # c_tot = N_tot / (V * NA)
            N_react = np.array([[N_step[kk] for N_step in N] for kk in reacts.keys()])
            niu = np.array(list(reacts.values()))
            c_po = np.power(N_react / V, np.repeat(niu, N_react.shape[1]).reshape(N_react.shape))
            c_tot = np.sum(np.prod(c_po, axis=0))
            k = occ/( V * time_tot * c_tot)
            line=str(reactions)+" "+str("%e"%k)+"\n"
            ratefile.write(line)
        

#get_rate()
