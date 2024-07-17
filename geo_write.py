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
rod_rad = 0.635
ECP_thick = 0.1
Rod_Len = 20
gap = 0.5
Move = Rod_Len -z0 + gap

with open('TrapAC.scuffgeo','w') as f:
    f.write(f'OBJECT Rod1\n   MESHFILE RF_Upper.o.msh\n   DISPLACED 0 0 40\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE RF_Lower.o.msh\n   DISPLACED 0 0 40\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE RF_Upper.o.msh\n   DISPLACED 0 0 40\n   ROTATED 180 ABOUT 0 1 0\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE RF_Lower.o.msh\n   DISPLACED 0 0 40\n   ROTATED 180 ABOUT 0 1 0\n   ROTATED 45 ABOUT 0 0 1\n   ENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Wehnelt\n MESHFILE Rod.o.msh\n   DISPLACED 0 0 {32/2 + Rod_Len/2 -2} \nENDOBJECT\n')
    f.write('\n')
    #f.write(f'OBJECT Filament\n   MESHFILE Filament.o.msh\n   DISPLACED 0 0 {+z0+8}\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Endcap_bottom.o.msh\n   DISPLACED 0 0 {-(Rod_Len/2+1)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')

    
with open('TrapDC.scuffgeo','w') as f:
    f.write(f'OBJECT Rod1\n   MESHFILE RF_Upper.o.msh\n   DISPLACED 0 0 40\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE RF_Lower.o.msh\n   DISPLACED 0 0 40\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE RF_Upper.o.msh\n   DISPLACED 0 0 40\n   ROTATED 180 ABOUT 0 1 0\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE RF_Lower.o.msh\n   DISPLACED 0 0 40\n   ROTATED 180 ABOUT 0 1 0\n   ROTATED 45 ABOUT 0 0 1\n   ENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Wehnelt\n MESHFILE Rod.o.msh\n   DISPLACED 0 0 {Rod_Len-3}\nENDOBJECT\n')
    f.write('\n')
    #f.write(f'OBJECT Filament\n   MESHFILE Filament.o.msh\n   DISPLACED 0 0 {+z0+8}\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Endcap_bottom.o.msh\n   DISPLACED 0 0 {-(Rod_Len+1)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
