#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# This code will plot the potentials and estimate the geometric factors
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

# Now we want these in SI units as we aren't passing anything to SCUFF-EM anymore
with open('dims.txt','r') as file:
	#lines=(line.strip() for line in file if valid(line))
	dims = [line for line in file if valid(line)] 

r0 = float(dims[0])
z0 = float(dims[1])




# =============================================================================
# First start with alpha_x^AC
# =============================================================================


with open('x_axis.dat','r') as file:
    lines = (line.strip() for line in file if valid(line))
    x_coords = np.array([extract(line) for line in lines])
    
x_points = np.array([float(x) for x in x_coords[:,0]])
x_axis = np.linspace(min(x_points),max(x_points),1001)

with open('TrapAC.x_axis.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    xACdata = np.array([extract(line) for line in lines])
    
x_pot = [float(phi) for phi in xACdata[:,4]]


fig_xAC,ax = plt.subplots(figsize=(10,5))
ax.scatter(x_points,x_pot,marker='x',color='r',label='Simulation')

xAC_vals, errs = curve_fit(f, x_points, x_pot)

ax.plot(x_axis,f(x_axis,xAC_vals[0],xAC_vals[1],xAC_vals[2]),label=f'Fit: $ax^2 + bx + c$\n $a=$ {xAC_vals[0]:.1e}; $b=$ {xAC_vals[1]:.1e}; $c=$ {xAC_vals[2]:.1e}')
ax.set(xlabel='$x$ [mm]',ylabel='$\\phi$ [V]',title='Potential due to RF voltage')
ax.legend(loc='upper right')

alpha_xAC = xAC_vals[0]*r0**2
print(f'alpha_x^AC = {abs(alpha_xAC):.4f}')
 


# =============================================================================
# Now move onto alpha_y^AC
# =============================================================================

with open('y_axis.dat','r') as file:
    lines = (line.strip() for line in file if valid(line))
    y_coords = np.array([extract(line) for line in lines])
    
y_points = np.array([float(y) for y in y_coords[:,1]])
y_axis = np.linspace(min(y_points),max(y_points),1001)

with open('TrapAC.y_axis.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    yACdata = np.array([extract(line) for line in lines])
    
y_pot = [float(phi) for phi in yACdata[:,4]]


fig_yAC,ax = plt.subplots(figsize=(10,5))
ax.scatter(y_points,y_pot,marker='x',color='r',label='Simulation')

yAC_vals, errs = curve_fit(f, y_points, y_pot)

ax.plot(y_axis,f(y_axis,yAC_vals[0],yAC_vals[1],yAC_vals[2]),label=f'Fit: $ay^2 + by + c$\n $a=$ {yAC_vals[0]:.1e}; $b=$ {yAC_vals[1]:.1e}; $c=$ {yAC_vals[2]:.1e}')
ax.set(xlabel='$y$ [mm]',ylabel='$\\phi$ [V]',title='Potential due to RF voltage')
ax.legend(loc='upper right')

alpha_yAC = yAC_vals[0]*r0**2
print(f'alpha_y^AC = {abs(alpha_yAC):.4f}')
print('--------------------------------------------------')
alpha_rAC = (abs(alpha_xAC)+abs(alpha_yAC))/2
print(f'alpha_r^AC = {alpha_rAC:.4f}')

# =============================================================================
# Now we move onto alpha_z^AC
# =============================================================================

with open('z_axis.dat','r') as file:
    lines = (line.strip() for line in file if valid(line))
    z_coords = np.array([extract(line) for line in lines])
    
z_points = np.array([float(z) for z in z_coords[:,2]])
z_axis = np.linspace(min(z_points),max(z_points),1001)

with open('TrapAC.z_axis.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])
    
zAC_pot = [float(phi) for phi in data[:,4]]


fig_zAC,ax = plt.subplots(figsize=(10,5))
ax.scatter(z_points,zAC_pot,marker='x',color='r',label='Simulation')

zAC_vals, errs = curve_fit(f, z_points, zAC_pot)

ax.plot(z_axis,f(z_axis,zAC_vals[0],zAC_vals[1],zAC_vals[2]),label=f'Fit: $az^2 + bz + c$\n $a=$ {zAC_vals[0]:.1e}; $b=$ {zAC_vals[1]:.1e}; $c=$ {zAC_vals[2]:.1e}')
ax.set(xlabel='$z$ [mm]',ylabel='$\\phi$ [V]',title='Potential due to RF voltage')
ax.legend(loc='upper right')

alpha_zAC = zAC_vals[0]*z0**2
print(f'alpha_z^AC = {abs(alpha_zAC):.4f}')



# =============================================================================
# And finaly alpha_z^DC
# =============================================================================

# Car reuse the z coords ect

with open('TrapDC.z_axis.out','r') as file:
    lines = (line.strip() for line in file if valid(line))
    data = np.array([extract(line) for line in lines])
    
zDC_pot = [float(phi) for phi in data[:,4]]


fig_zDC,ax = plt.subplots(figsize=(10,5))
ax.scatter(z_points,zDC_pot,marker='x',color='r',label='Simulation')

zDC_vals, errs = curve_fit(f, z_points, zDC_pot)

ax.plot(z_axis,f(z_axis,zDC_vals[0],zDC_vals[1],zDC_vals[2]),label=f'Fit: $ax^2 + bx + c$\n $a=$ {zDC_vals[0]:.1e}; $b=$ {zDC_vals[1]:.1e}; $c=$ {zDC_vals[2]:.1e}')
ax.set(xlabel='$z$ [mm]',ylabel='$\\phi$ [V]',title='Potential due to end caps')
ax.legend(loc='upper right')

alpha_zDC = zDC_vals[0]*z0**2
print(f'alpha_z^DC = {abs(alpha_zDC):.4f}')


