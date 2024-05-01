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
    
r0 = float(vals[0])*1e3
z0 = float(vals[1])*1e3


Blade_Length = 22e3/2 # Blade is 22mm long
ECP_thick = 0.1e3

with open('TrapAC.scuffgeo','w') as f:
    f.write(f'OBJECT Rod1\n   MESHFILE Rod.o.msh\n   DISPLACED {+(r0+Blade_Length)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE Rod.o.msh\n   ROTATED 90 ABOUT 0 0 1\n   DISPLACED 0 {+(r0+Blade_Length)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE Rod.o.msh\n   ROTATED 90 ABOUT 0 0 1\n   DISPLACED 0 {-(r0+Blade_Length)}  0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE Rod.o.msh\n   DISPLACED {-(r0+Blade_Length)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Top\n   MESHFILE Endcap.o.msh\n   DISPLACED 0 0 {+(z0+ECP_thick/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Endcap.o.msh\n   DISPLACED 0 0 {-(z0+ECP_thick/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    
with open('TrapAC.scuffgeo','w') as f:
    f.write(f'OBJECT Rod1\n   MESHFILE Rod.o.msh\n   DISPLACED {+(r0+Blade_Length)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE Rod.o.msh\n   ROTATED 90 ABOUT 0 0 1\n   DISPLACED 0 {+(r0+Blade_Length)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE Rod.o.msh\n   ROTATED 90 ABOUT 0 0 1\n   DISPLACED 0 {-(r0+Blade_Length)}  0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE Rod.o.msh\n   DISPLACED {-(r0+Blade_Length)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Top\n   MESHFILE Endcap.o.msh\n   DISPLACED 0 0 {+(z0+ECP_thick/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Endcap.o.msh\n   DISPLACED 0 0 {-(z0+ECP_thick/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    
