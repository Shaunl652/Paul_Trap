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
    
x0 = float(vals[0])*1e3
y0 = float(vals[1])*1e3
z0 = float(vals[2])*1e3


xs = np.linspace(-x0,+x0,101)#/2
ys = np.linspace(-y0,+y0,101)#/2
zs = np.linspace(-z0,+z0,101)#/2

XS,YS = np.meshgrid(xs,ys)

with open('plane.dat','w') as file:
    for x in xs:
        for y in ys:
            file.write(f'{x} {y} 0\n')
