#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import griddata
import matplotlib as mpl

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

XS,YS = np.meshgrid(xs,zs)

#for i,z in enumerate(zs):

vals = np.array([float(line[4]) for line in data])

xvals = np.array([float(line[1]) for line in data])
yvals = np.array([float(line[3]) for line in data])

coords = np.array([xvals,yvals]).T

plot = griddata(coords, vals, (XS,YS))

Ex = griddata(coords, np.array([float(line[5]) for line in data]), (XS,YS))
Ey = griddata(coords, np.array([float(line[7]) for line in data]), (XS,YS))

vmin = -100
vmax = 0
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

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

norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
m = ax.streamplot(XS,YS,Ex,Ey,density=2,color=plot,cmap='jet',norm=norm)
lw=2
Rod1 = plt.Rectangle((-5,-16),1.27, 30,fc='none',ec='k',lw=lw)
Rod2 = plt.Rectangle((+5-1.27,-16),1.27, 30,fc='none',ec='k',lw=lw)
plt.gca().add_patch(Rod1)
plt.gca().add_patch(Rod2)

Wehnelt_Left  = plt.Rectangle((-1,16.6),-6, 2,fc='none',ec='k',lw=lw)
Wehnelt_Right = plt.Rectangle((+1,16.6),+6, 2,fc='none',ec='k',lw=lw)
plt.gca().add_patch(Wehnelt_Left)
plt.gca().add_patch(Wehnelt_Right)
ax.set(xlabel='$x$ [mm]',ylabel='$z$ [mm]')
fig.colorbar(m.lines,label='Potential [V]')

#fig.savefig(f'Figs/{i}_{z}.png')

with open('TrapAC.xy_plane.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])


vals = np.array([float(line[4]) for line in data])

xvals = np.array([float(line[1]) for line in data])
yvals = np.array([float(line[2]) for line in data])

coords = np.array([xvals,yvals]).T

plot = griddata(coords, vals, (XS,YS))
rad = 1.27/2
Ex = griddata(coords, np.array([float(line[5]) for line in data]), (XS,YS))
Ey = griddata(coords, np.array([float(line[6]) for line in data]), (XS,YS))

figxy,ax = plt.subplots()

m = ax.streamplot(XS,YS,Ex,Ey,density=2,color=plot,cmap='jet',norm=norm)

Rod1 = plt.Circle((+4+rad,0),rad,fc='none',ec='r',lw=lw)
Rod2 = plt.Circle((-4-rad,0),rad,fc='none',ec='r',lw=lw)
Rod3 = plt.Circle((0,+4+rad),rad,fc='none',ec='r',lw=lw)
Rod4 = plt.Circle((0,-4-rad),rad,fc='none',ec='r',lw=lw)
plt.gca().add_patch(Rod1)
plt.gca().add_patch(Rod2)
plt.gca().add_patch(Rod3)
plt.gca().add_patch(Rod4)
#ax.clabel(CS, inline=True, fontsize=10)
figxy.colorbar(m.lines,label='Potential [V]')
ax.set(xlabel='x [mm]',ylabel='y [mm]',title='$x-y$ Field Lines')