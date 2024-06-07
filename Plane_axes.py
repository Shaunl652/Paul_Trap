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
    
r0 = float(vals[0])
z0 = float(vals[1])



xs = np.linspace(-r0,+r0,101)
ys = np.linspace(-r0,+r0,101)
zs = np.linspace(-9,+9,11)

XS,YS = np.meshgrid(xs,ys)

with open('plane.dat','w') as file:
    for z in zs:
        for x in xs:
            for y in ys:
                file.write(f'{x} {y} {z}\n')
