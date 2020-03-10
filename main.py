import numpy as np 
import random
import matplotlib.pyplot as plt

from numba import njit,prange

@njit(parallel=True)
def simulation(prob,num_of_trails_max,sample_size):
    expt = np.zeros(num_of_trails_max)
    for num_of_trails in prange(int(num_of_trails_max)):
        success = 0 # reset counter each new number of trails
        for sample_index in prange(int(sample_size)):
            for _ in prange(num_of_trails):
                if random.random() <= prob:
                    success += 1
        expt_of_success = success / sample_size
        expt[num_of_trails] = expt_of_success
    return expt

# function inputs
prob = 1 / 682
num_of_trails_max = 3000
sample_size = 25

# output array
trail_index = np.arange(0,num_of_trails_max,1)
expt = simulation(prob,num_of_trails_max,sample_size)

#print(len(expt),len(trail_index))

plt.figure(0,figsize=(8,6))
plt.scatter(trail_index,expt)
plt.show()
