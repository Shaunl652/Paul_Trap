#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:45:26 2024

@author: shaun
"""

import numpy as np
from numpy import arctan,sin,pi,sqrt

# Work in mm the whole way through
x0 = np.linspace(0.1,10,1001)
y0 = np.linspace(0.1,10,1001)

Rad = 0.635

X,Y = np.meshgrid(x0,y0)

def theta(R,x,y):
    phi = arctan((x+R)/(y+R))
    alpha = arctan(R/sqrt((x+R)**2 + (y+R)**2))#arctan(R*sin(phi)/(x+R))
    return np.rad2deg(((pi/2)-alpha-phi))

theta_vals = theta(Rad,X,Y)

import matplotlib.pyplot as plt
level = [10,20,37,50,60,70,80,90]
fig,ax = plt.subplots()
m = ax.pcolormesh(x0,y0,theta_vals)
CS = ax.contour(x0,y0,theta_vals,2,colors='k',levels=level)
ax.clabel(CS, inline=True, fontsize=10)
fig.colorbar(m)
ax.set(xlabel='$x_0$ [mm]',ylabel='$y_0$ [mm]')