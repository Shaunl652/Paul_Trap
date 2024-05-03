#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Want to see where the field is pointing
# =============================================================================

import numpy as np

# Set up trap dimensions
def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True
    
def extract(line):
    # Pulls the values out of the file
    values = line.strip().split()
    return [v for v in values]


with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
r0 = float(vals[0])*1e3
z0 = float(vals[1])*1e3


# Measurment locations
xaxis = np.linspace(-5,+5,10)*1e3#/20
yaxis = np.linspace(-5,+5,10)*1e3#/20
zaxis = np.linspace(-30,+30,10)*1e3#/20

with open('field_axis.dat','w') as f:
    for x in xaxis:
        for y in yaxis:
            for z in zaxis:
                f.write(f'{x} {y} {z} \n')

import matplotlib.pyplot as plt

with open('TrapDC.field_axis.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])


xs = np.array([float(x) for x in data[:,1]])
ys = np.array([float(y) for y in data[:,2]])
zs = np.array([float(z) for z in data[:,3]])    

pots = np.array([float(x) for x in data[:,4]])
Ex = np.array([float(x) for x in data[:,5]])
Ey = np.array([float(y) for y in data[:,6]])
Ez = np.array([float(z) for z in data[:,7]])
    
fig,ax = plt.subplots(subplot_kw={'projection':'3d'})

ax.quiver(xs/1e3,ys/1e3,zs/1e3,Ex,Ey,Ez,normalize=True)
#= ax.scatter(xs/1e3,ys/1e3,zs/1e3,c=pots,cmap='jet')
ax.set(xlabel='$x$ [mm]',ylabel='$y$ [mm]',zlabel='$z$ [mm]')
#fig.colorbar(m)