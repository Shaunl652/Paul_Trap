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
zs = np.linspace(-9,+9,10)

XS,YS = np.meshgrid(xs,ys)

for i,z in enumerate(zs):
    
    vals = np.array([float(line[4]) for line in data if float(line[3])==z])
    
    xvals = np.array([float(line[1]) for line in data if float(line[3])==z])
    yvals = np.array([float(line[2]) for line in data if float(line[3])==z])
    
    coords = np.array([xvals,yvals]).T
    
    plot = griddata(coords, vals, (XS,YS))
    
    Ex = griddata(coords, np.array([float(line[5]) for line in data if float(line[3])==z]), (XS,YS))
    Ey = griddata(coords, np.array([float(line[6]) for line in data if float(line[3])==z]), (XS,YS))
    
    
    
    import matplotlib.pyplot as plt
    
    # fig,ax = plt.subplots(subplot_kw={'projection':'3d'})
    # #levels = np.linspace(plot.min(),plot.max(),50)
    # #m=ax.contourf(xs/1e3,ys/1e3,plot,levels=levels)
    # #ax.contour(xs/1e3,ys/1e3,plot,2,colors='k',levels=levels)
    # #fig.colorbar(m)
    # ax.plot_surface(XS,YS,plot,cmap='jet',alpha=0.8)
    
    # ax.set(xlabel='x [mm]',ylabel='y [mm]',zlabel='$\\phi(x,y)$')
    # #ax.set_xlim(-6,6)
    
    
    # And field lines
    fig,ax = plt.subplots(figsize=(10,8))
    import matplotlib as mpl
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    m = ax.streamplot(XS,YS,Ex,Ey,density=2,color=plot,cmap='jet',norm=norm)
    ax.set(xlabel='$x$ [mm]',ylabel='$y$ [mm]',title=f'z = {z:.2f} mm')
    fig.colorbar(m.lines,label='Potential [V]')
    
    fig.savefig(f'Figs/{i}_{z}.png')