#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Plots the potential as a function of wehnelt bias
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# These first two functions are mostly about reading in the data
def valid(line):
    # Returns False if the first character in the line is '#'
    if line.startswith("#"): return False
    return True

def extract(line):
    # Pulls the values out of the file
    values = line.strip().split()
    return [v for v in values]

f = lambda x,a,b,c: a*x**2 + b*x + c

EC_Top = np.linspace(-100,-300,100)


with open('z_axis.dat','r') as file:
    lines = (line.strip() for line in file if valid(line))
    z_coords = np.array([extract(line) for line in lines])
    
z_points = np.array([float(z) for z in z_coords[:,2]])
z_axis = np.linspace(min(z_points),max(z_points),1001)

with open('TrapAC.z_axis.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])
    
    
potentials = []
min_pos = []
for i,V in enumerate(EC_Top):
    
    z_pot = [float(val[4]) for val in data if val[0]==f'ECV_{i}']
    z_vals, errs = curve_fit(f, z_points, z_pot)
    
    potentials.append(f(z_axis,z_vals[0],z_vals[1],z_vals[2]))
    min_pos.append(-z_vals[1]/(2*z_vals[0]))
    
potential_surface = np.array(potentials)*-1

plt.pcolormesh(z_axis,EC_Top,potential_surface)
plt.plot(min_pos,EC_Top,color='r',label='Trap centre')
plt.vlines(0,-300,-100,label='Geometric centre')
plt.xlabel('z [mm]')
plt.ylabel('Wehnelt Bias [V]')
plt.legend()
plt.colorbar()