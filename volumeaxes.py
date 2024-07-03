#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:40:41 2024

@author: shaun
"""

import numpy as np


# Set up trap dimensions
def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True

with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
    
r0 = float(vals[0])+2
z0 = float(vals[1])+5



xs = np.linspace(-r0,+r0,11)
ys = np.linspace(-r0,+r0,11)
zs = np.linspace(-z0,+z0,11)

XS,YS = np.meshgrid(xs,ys)

with open('volume_axes.dat','w') as file:
    for z in zs:
        for x in xs:
            for y in ys:
                file.write(f'{x} {y} {z}\n')
            

