#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:51:12 2024

@author: shaun
"""

import numpy as np
from scipy.interpolate import griddata
from scipy.constants import electron_mass,elementary_charge
e_c = elementary_charge
e_m = electron_mass



def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True
    
def extract(line):
    # Pulls the values out of the file
    values = line.strip().split()
    return [v for v in values]

with open('TrapAC.xz_plane.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])
    
with open('dims.txt','r') as file:
	rvals = [line for line in file if valid(line)]
    
r0 = float(rvals[0])+2
z0 = float(rvals[1])+5

xs = np.linspace(-r0,+r0,101)#/10
ys = np.linspace(-r0,+r0,101)
zs = np.linspace(-z0,+z0,101)

XS,ZS = np.meshgrid(xs,zs)

#for i,z in enumerate(zs):

vals = np.array([float(line[4]) for line in data])

xvals = np.array([float(line[1]) for line in data])
yvals = np.array([float(line[3]) for line in data])

coords = np.array([xvals,yvals]).T

#plot = griddata(coords, vals, (XS,ZS))

Ex = griddata(coords, np.array([float(line[5]) for line in data]), (XS,ZS))
Ez = griddata(coords, np.array([float(line[7]) for line in data]), (XS,ZS))

a_x = -(e_c/e_m)*Ex
a_z = -(e_c/e_m)*Ez

colours = np.sqrt(a_x**2 + a_z**2)
import matplotlib.pyplot as plt


# And field lines
fig,ax = plt.subplots(figsize=(10,8))
import matplotlib as mpl

m = ax.streamplot(XS,ZS,a_x,a_z,density=2,color=colours,cmap='jet')
lw=2
Rod1 = plt.Rectangle((-5,-16),1.27, 30,fc='none',ec='k',lw=lw)
Rod2 = plt.Rectangle((+5-1.27,-16),1.27, 30,fc='none',ec='k',lw=lw)
plt.gca().add_patch(Rod1)
plt.gca().add_patch(Rod2)

# Wehnelt_Left  = plt.Rectangle((-1,16.6),-6, 2,fc='none',ec='k',lw=lw)
# Wehnelt_Right = plt.Rectangle((+1,16.6),+6, 2,fc='none',ec='k',lw=lw)
# plt.gca().add_patch(Wehnelt_Left)
# plt.gca().add_patch(Wehnelt_Right)
ax.set(xlabel='$x$ [mm]',ylabel='$z$ [mm]',title='Electron Acceleration')
fig.colorbar(m.lines,label='Accel mag')
