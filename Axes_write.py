#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# This code will write the EP files containt the axis locations to measure the potential at
# =============================================================================

import numpy as np

# Set up trap dimensions
def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True
with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
r0 = float(vals[0])*1e3
z0 = float(vals[1])*1e3


# Measurment locations
xaxis = np.linspace(-r0,+r0,11)/20
yaxis = np.linspace(-r0,+r0,11)/20
zaxis = np.linspace(-z0,+z0,11)/20

with open('x_axis.dat','w') as f:
    for x in xaxis:
        f.write(f'{x} 0 0 \n')

with open('y_axis.dat','w') as f:
    for y in yaxis:
        f.write(f'0 {y} 0 \n')

with open('z_axis.dat','w') as f:
    for z in zaxis:
        f.write(f'0 0 {z} \n')