#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Takes the radii of the inner and outer electrodes, and the magnitude of the 
# voltages applied then gives the potential as a function of z
# We also mark the locations of z0 and zmax and give the trap depth 
# =============================================================================

import numpy as np
from numpy import sqrt,trapz 
from scipy.constants import elementary_charge,pi

# Set up properties
Q = 86*elementary_charge
R = 150e-9
density = 2329
Mass = (4/3)*pi*density*R**3
Omega = 2*pi*4e3
Vin = 0 
Vout = 340
e = Vin/Vout
a = 1.07e-3
b = 3.63e-3

z_vals = np.linspace(0.01,3,101)*1e-3

def psi(z):

    
    epsilon =Vin/Vout
    A = Q**2*Vout**2/(4*Mass*Omega**2)
    # This is the differentiation from Alda EQ2 givein by mathematica
    term1 = b**2/((1+(b/z)**2)**(3/2)*z**3)
    term2 = ((1-epsilon)*a**2)/((1+(a/z)**2)**(3/2)*z**3)
    
    Dkappa = term1 + term2
    
    return A*np.abs(Dkappa)**2

  
z0numer = b**2 * a**(4/3) * (1-e)**(2/3) - a**2 * b**(4/3)
z0denom = b**(4/3) - a**(4/3) * (1-e)**(2/3)
    
z0 =  sqrt(z0numer/z0denom)


zmaxnumer = b**2 * a**(4/5) * (1-e)**(2/5) - a**2 * b**(4/5)
zmaxdenom = b**(4/5) - a**(4/5) * (1-e)**(2/5)
    
zmax = sqrt(zmaxnumer/zmaxdenom)

Trap_Depth = psi(zmax) - psi(z0)



psi_vals = psi(z_vals)
# Begin plotting
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(z_vals/1e-3,psi_vals)
ax.set(xlabel='x [mm]',ylabel='$\\psi$')

print(f'Trap Depth = {Trap_Depth:.2e}')





