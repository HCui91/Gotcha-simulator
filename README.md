# Simulator for gotcha game

淦，为什么还是不出闪光！

## Introduction

A simulator for gotcha. 

Probability to meet a shiny pokemon in egg hatching is taken as 1/682. 

## How to use

Make sure you get `numba` installed. 

Adjust `prob,num_of_trails_max,sample_size` depending on what you are simulating.

## Observation
Larger `sample_size` eventually ends up with narrower distribution of the mean of success counts. Therefore, don't trust too much comments under the video/article that they got a shiny pokemon in ~ 100 eggs.  

## File structure

main.py - Function and simulation variables inputs

## Acknowledgement

Thanks to numba for automatic parallel computing.
