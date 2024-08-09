#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Writes the scuffgeo file based on the given parameters 
# All distances are given in mm to make simulations easier
# We wrtie a file for the AC and DC voltages
# This makes file names output form SCUFF-EM easier to read
# =============================================================================

def valid(line):
	if line.startswith('#'):
		return False
	else:
		return True
    
# Reads in the trap dimensions in mm
with open('dims.txt','r') as file:
	vals = [line for line in file if valid(line)]
    
r0 = float(vals[0])
z0 = float(vals[1])

# Rod dimesions
rod_rad = 1.27/2
Rod_Len = 32

# Writes the files
with open('TrapAC.scuffgeo','w') as f:
    # Start with the RF rods
    f.write(f'OBJECT Rod1\n   MESHFILE Rod.o.msh\n   DISPLACED {-(r0+rod_rad)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod2\n   MESHFILE Rod.o.msh\n   DISPLACED {+(r0+rod_rad)} 0 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod3\n   MESHFILE Rod.o.msh\n   DISPLACED 0 {-(r0+rod_rad)} 0\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT Rod4\n   MESHFILE Rod.o.msh\n   DISPLACED 0 {+(r0+rod_rad)} 0\nENDOBJECT\n')
    f.write('\n')
    # Next we do the end caps
    f.write(f'OBJECT End_Cap_Top\n   MESHFILE Rod.o.msh\n   DISPLACED 0 0 {+(z0+Rod_Len/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')
    f.write('\n')
    f.write(f'OBJECT End_Cap_Bot\n   MESHFILE Rod.o.msh\n   DISPLACED 0 0 {-(z0+Rod_Len/2)}\n   ROTATED 45 ABOUT 0 0 1\nENDOBJECT\n')

# And the same again
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

