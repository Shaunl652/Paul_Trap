#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Writes the scuffgeo file based on the given parameters 
# All distances are given in um
# =============================================================================


import numpy as np

# Trap sizes

def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True
with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
    
r0 = float(vals[0])
z0 = float(vals[1])

# Distance from surface of the rod to its centre
rod_rad = 1.27/2
ECP_thick = 0.44
Rod_Len = 32
gap = 0.5
Move = Rod_Len -z0 + gap

with open('TrapAC.scuffgeo','w') as f:
    f.write(f'OBJECT Rod1\n   MESHFILE Rod.o.msh\n   DISPLACED {-(r0+rod_rad)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE Rod.o.msh\n   DISPLACED {+(r0+rod_rad)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE Rod.o.msh\n   DISPLACED 0 {-(r0+rod_rad)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE Rod.o.msh\n   DISPLACED 0 {+(r0+rod_rad)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Top\n   MESHFILE Rod.o.msh\n   DISPLACED 0 0 {+(z0+Rod_Len/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Rod.o.msh\n   DISPLACED 0 0 {-(z0+Rod_Len/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')

    
with open('TrapDC.scuffgeo','w') as f:
    f.write(f'OBJECT Rod1\n   MESHFILE Rod.o.msh\n   DISPLACED {-(r0+rod_rad)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE Rod.o.msh\n   DISPLACED {+(r0+rod_rad)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE Rod.o.msh\n   DISPLACED 0 {-(r0+rod_rad)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE Rod.o.msh\n   DISPLACED 0 {+(r0+rod_rad)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Top\n   MESHFILE Rod.o.msh\n   DISPLACED 0 0 {+(z0+Rod_Len/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Rod.o.msh\n   DISPLACED 0 0 {-(z0+Rod_Len/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')

