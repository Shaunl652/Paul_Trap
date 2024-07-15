#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:18:13 2024

@author: shaun
"""

from numpy import sqrt,pi
from scipy.constants import elementary_charge





q = 95*elementary_charge
iRadius = 150 # Particle radius nm
density = 2000 # particle density kg/m^3
mass = lambda R: density*4*pi*(R*1e-9)**3/3
m = mass(iRadius) # mass kg

Omega = 2*pi*7.7e3
kDC = 0.38
kRF = 0.93

VAC = 830
VDC = 130

z0 = (2.8e-3)/2
r0 = (1.8e-3)/2

EDC = ((8*q)/(m*Omega**2))*kDC*((VDC/2)/(2*z0**2))
dRF = ((4*q)/(m*Omega**2))*kRF*((VAC/2)/(r0**2))

omega0 = (Omega/2) * sqrt(-EDC + (dRF**2/2))

print(omega0/(2*pi))