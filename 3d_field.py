#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:55:20 2024

@author: shaun
"""

import numpy as np
from scipy.interpolate import griddata
from scipy.constants import electron_mass,elementary_charge
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
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

with open('TrapAC.volume_axes.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])
    
with open('dims.txt','r') as file:
	rvals = [line for line in file if valid(line)]
    
r0 = float(rvals[0])+2
z0 = float(rvals[1])+5

xs = np.linspace(-r0,+r0,101)
ys = np.linspace(-r0,+r0,101)
zs = np.linspace(-z0,+z0,101)

XS,YS,ZS = np.meshgrid(xs,ys,zs)

xvals = np.array([float(line[1]) for line in data])
yvals = np.array([float(line[2]) for line in data])
zvals = np.array([float(line[3]) for line in data])

coords = np.array([xvals,yvals,zvals]).T

Ex = griddata(coords, np.array([float(line[5]) for line in data]), (XS,YS,ZS))
Ey = griddata(coords, np.array([float(line[6]) for line in data]), (XS,YS,ZS))
Ez = griddata(coords, np.array([float(line[7]) for line in data]), (XS,YS,ZS))

fig,ax = plt.subplots(subplot_kw={'projection':'3d'})

ax.quiver(XS,YS,ZS, Ex,Ey,Ez)


