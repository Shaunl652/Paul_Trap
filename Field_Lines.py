#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
	rvals = [line for line in file if valid(line)]
    
r0 = float(rvals[0])
z0 = float(rvals[1])

xs = np.linspace(-r0,+r0,101)
ys = np.linspace(-r0,+r0,101)
zs = np.linspace(-z0,+z0,101)

XS,YS = np.meshgrid(xs,ys)

vals = np.array([float(line[4]) for line in data])

xvals = np.array([float(line[1]) for line in data])
yvals = np.array([float(line[2]) for line in data])

coords = np.array([xvals,yvals]).T

plot = griddata(coords, vals, (XS,YS))

Ex = griddata(coords, np.array([float(line[5]) for line in data]), (XS,YS))
Ey = griddata(coords, np.array([float(line[6]) for line in data]), (XS,YS))



import matplotlib.pyplot as plt

fig,ax = plt.subplots(subplot_kw={'projection':'3d'})
#levels = np.linspace(plot.min(),plot.max(),50)
#m=ax.contourf(xs/1e3,ys/1e3,plot,levels=levels)
#ax.contour(xs/1e3,ys/1e3,plot,2,colors='k',levels=levels)
#fig.colorbar(m)
ax.plot_surface(XS,YS,plot,cmap='jet',alpha=0.8)

ax.set(xlabel='x [mm]',ylabel='y [mm]',zlabel='$\\phi(x,y)$')
#ax.set_xlim(-6,6)
plt.show()

# And field lines
fig,ax = plt.subplots()

m = ax.streamplot(XS,YS,Ex,Ey,density=2,color=plot,cmap='jet')
ax.set(xlabel='$x$ [mm]',ylabel='$y$ [mm]')
fig.colorbar(m.lines,label='Potential [V]')