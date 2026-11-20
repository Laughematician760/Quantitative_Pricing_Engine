import numpy as np


rng = np.random.default_rng(1)

#Version 1

#(1+fwb) if there is a win, and -fw if there is a loss

def simulate_one_path(p, b, f, n_bets, rng):
    sample = rng.random(n_bets)
    truth_table_vec = (sample <= p)
    wealth_path = [1]*(n_bets + 1)
    for i in range(1, n_bets + 1):
        if truth_table_vec[i-1]:
            wealth_path[i] = wealth_path[i-1] + f*wealth_path[i-1]*b
        else:
            wealth_path[i] = wealth_path[i-1] - f*wealth_path[i-1]
    return wealth_path

print("Check 1: f=0", simulate_one_path(.5, 1, 0, 5, rng), [1]*(5 + 1))

print("Check p=1", simulate_one_path(1, 1, .5, 5, rng), (1+1*.5)**(5))

print("Check f =.2 and b=1", simulate_one_path(.5, 1, .2, 1, rng), "1.2 or .8")





