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


    
with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
    
r0 = float(vals[0])+2
z0 = float(vals[1])+5

xs = np.linspace(-r0,+r0,101)#/10
ys = np.linspace(-r0,+r0,101)#/10
zs = np.linspace(-z0,+z0,101)

lw=2
rad = 1.27/2
Vmax = +300
Vmin = -200
levels = np.linspace(Vmin,Vmax,50)
import matplotlib.pyplot as plt

# Plot the xy plane
# =============================================================================
with open('TrapAC.xy_plane.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    xydata = np.array([extract(line) for line in lines])

xyvals = np.array([float(line[4]) for line in xydata])

xvals = np.array([float(line[1]) for line in xydata])
yvals = np.array([float(line[2]) for line in xydata])

coords = np.array([xvals,yvals]).T
XS,YS = np.meshgrid(xs,ys)
xyplot = griddata(coords, xyvals, (XS,YS))

figxy,ax = plt.subplots()

m=ax.contourf(xs,ys,xyplot,levels=levels,vmax=Vmax,vmin=Vmin)
CS=ax.contour(xs,ys,xyplot,2,colors='k',levels=levels)
Rod1 = plt.Circle((+4+rad,0),rad,fc='none',ec='r',lw=lw)
Rod2 = plt.Circle((-4-rad,0),rad,fc='none',ec='r',lw=lw)
Rod3 = plt.Circle((0,+4+rad),rad,fc='none',ec='r',lw=lw)
Rod4 = plt.Circle((0,-4-rad),rad,fc='none',ec='r',lw=lw)
plt.gca().add_patch(Rod1)
plt.gca().add_patch(Rod2)
plt.gca().add_patch(Rod3)
plt.gca().add_patch(Rod4)
#ax.clabel(CS, inline=True, fontsize=10)
figxy.colorbar(m)
ax.set(xlabel='x [mm]',ylabel='y [mm]',title='$x-y$ plane potential')


# Plot the xz plane
# =============================================================================
with open('TrapAC.xz_plane.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    xzdata = np.array([extract(line) for line in lines])

xzvals = np.array([float(line[4]) for line in xzdata])

xvals = np.array([float(line[1]) for line in xzdata])
zvals = np.array([float(line[3]) for line in xzdata])

coords = np.array([xvals,zvals]).T
XS,ZS = np.meshgrid(xs,zs)
xzplot = griddata(coords, xzvals, (XS,ZS))

figxz,ax = plt.subplots()

m=ax.contourf(xs,zs,xzplot,levels=levels)
CS = ax.contour(xs,zs,xzplot,2,colors='k',levels=levels,vmax=Vmax,vmin=Vmin)
lw=2
Rod1 = plt.Rectangle((-5,-16),1.27, 30,fc='none',ec='r',lw=lw)
Rod2 = plt.Rectangle((+5-1.27,-16),1.27, 30,fc='none',ec='r',lw=lw)
plt.gca().add_patch(Rod1)
plt.gca().add_patch(Rod2)

Wehnelt_Left  = plt.Rectangle((-1,16.6),-6, 2,fc='none',ec='r',lw=lw)
Wehnelt_Right = plt.Rectangle((+1,16.6),+6, 2,fc='none',ec='r',lw=lw)
plt.gca().add_patch(Wehnelt_Left)
plt.gca().add_patch(Wehnelt_Right)
#ax.clabel(CS, inline=True, fontsize=10)
figxz.colorbar(m)
ax.set(xlabel='x [mm]',ylabel='z [mm]',title='$x-z$ plane potential')
ax.set_xlim(-6,6)

# Plot the yz plane
# =============================================================================
with open('TrapAC.yz_plane.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    yzdata = np.array([extract(line) for line in lines])

yzvals = np.array([float(line[4]) for line in yzdata])

yvals = np.array([float(line[2]) for line in yzdata])
zvals = np.array([float(line[3]) for line in yzdata])

coords = np.array([yvals,zvals]).T
YS,ZS = np.meshgrid(ys,zs)
yzplot = griddata(coords, yzvals, (YS,ZS))


figyz,ax = plt.subplots()

m=ax.contourf(ys,zs,yzplot,levels=levels)
CS=ax.contour(ys,zs,yzplot,2,colors='k',levels=levels,vmax=Vmax,vmin=Vmin)
lw=2
Rod1 = plt.Rectangle((-5,-16),1.27, 30,fc='none',ec='r',lw=lw)
Rod2 = plt.Rectangle((+5-1.27,-16),1.27, 30,fc='none',ec='r',lw=lw)
plt.gca().add_patch(Rod1)
plt.gca().add_patch(Rod2)

Wehnelt_Left  = plt.Rectangle((-1,16.6),-6, 2,fc='none',ec='r',lw=lw)
Wehnelt_Right = plt.Rectangle((+1,16.6),+6, 2,fc='none',ec='r',lw=lw)
plt.gca().add_patch(Wehnelt_Left)
plt.gca().add_patch(Wehnelt_Right)
#ax.clabel(CS, inline=True, fontsize=10)
figyz.colorbar(m)
ax.set(xlabel='y [mm]',ylabel='z [mm]',title='$y-z$ plane potential')
ax.set_xlim(-6,6)
plt.show()