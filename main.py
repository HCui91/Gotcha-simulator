########################
# Simulator for gotcha #
#    Author: HCui91    #
########################

import random

import matplotlib.pyplot as plt
import numpy as np
from numba import njit, prange


@njit(parallel=True)
def simulation(num_of_trails, sample_size, prob):
    """
    This program simulate n trails with a given sample size.
    Compare the random number (0-1) with probability.
    -----------
    Inputs:
    num_of_trails: number of trails in this gotcha
    sample_size: how many samples are taken
    prob: the probability to success
    ----------
    Outputs:
    result: the array of success counts in each sample (stats need to be done outside the function)"""
    # Housekeeping
    sample_size = int(sample_size)
    num_of_trails = int(num_of_trails)
    # Initialise output array
    result = np.zeros(sample_size)
    # Loop with prange -> parallel
    for sample_index in prange(sample_size):
        success = 0  # reset the counter
        for _ in prange(num_of_trails):
            if random.random() <= prob:
                success += 1
        result[sample_index] = success
    return result


# function inputs
prob = 1 / 682
num_of_trails_max = 3000
sample_size = 10

# Result array initialise
trail_index = np.arange(0, num_of_trails_max, 1)
expt = np.zeros(num_of_trails_max)
expt_min = np.zeros(num_of_trails_max)

# Simulation
for num_of_trails in trail_index:
    temp = simulation(num_of_trails, sample_size, prob)
    expt[num_of_trails] = np.mean(temp)
    expt_min[num_of_trails] = np.min(temp)
    temp = []

# Plotting
plt.figure(0, figsize=(8, 6))
plt.plot(trail_index, expt, label="Mean")
plt.scatter(trail_index, expt_min, label="Min")
plt.legend()
plt.xlabel("Number of trails")
plt.ylabel("Number of success")
plt.show()
