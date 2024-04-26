#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:53:49 2024

@author: shaun
"""

import numpy as np
from scipy.interpolate import griddata

def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True
    
def extract(line):
    # Pulls the values out of the file
    values = line.strip().split()
    return [v for v in values]

with open('TrapAC.plane.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])
    
with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
    
x0 = float(vals[0])*1e3
y0 = float(vals[1])*1e3
z0 = float(vals[2])*1e3


xs = np.linspace(-x0,+x0,101)#/2
ys = np.linspace(-y0,+y0,101)#/2
zs = np.linspace(-z0,+z0,101)#/2

XS,YS = np.meshgrid(xs,ys)

vals = np.array([float(line[4]) for line in data])

xvals = np.array([float(line[1]) for line in data])
yvals = np.array([float(line[2]) for line in data])

coords = np.array([xvals,yvals]).T

plot = griddata(coords, vals, (XS,YS))

with open('u_axis.dat','r')as file:
    udata = np.array([line.strip().split() for line in file])
    
us = np.array([[float(x[0]),float(x[1])] for x in udata])/1e3
    
with open('v_axis.dat','r')as file:
    vdata = np.array([line.strip().split() for line in file])
    
vs = np.array([[float(x[0]),float(x[1])] for x in vdata])/1e3

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
levels = np.linspace(plot.min(),plot.max(),50)
m=ax.contourf(xs/1e3,ys/1e3,plot,levels=levels)
ax.contour(xs/1e3,ys/1e3,plot,2,colors='k',levels=levels)
fig.colorbar(m)

ax.scatter(us[:,0],us[:,1],color='r',marker='x',label='u axis')
ax.scatter(vs[:,0],vs[:,1],color='w',marker='x',label='v axis')
ax.legend()
ax.set(xlabel='x [mm]',ylabel='y [mm]')
#ax.set_xlim(-6,6)
plt.show()