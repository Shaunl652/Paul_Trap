#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Just some code to caclulate the number of elemetry charges on a particle
# trapped in our Paul trap
# Follows the method given in Bykov (2020), see Eq. 2 and surrounding paragraph
# For testing ATM, I'm just using the values given by Byvok (2020)
# =============================================================================

import numpy as np
from scipy.constants import pi, elementary_charge
sqrt = np.sqrt

alpha_zDC = 0.38/2
alpha_rAC = 0.93/2
Omega_RF = 2*pi*7.7e3

VAC = 830 
VDC = 130
r0 = 0.9e-3
z0 = 1.4e-3

R = 154e-9
density = 2000 # particle density kg/m^3
mass = (4/3)*density*pi*R**3

Q_zDC = alpha_zDC*VDC/(z0**2)
Q_rAC = alpha_rAC*VAC/(r0**2)


# Using a value from Bykov for testing
# Potential to read in motion and calcualte this directly later
w0 = 2*pi *920
# The equatoin defining w0 can be rearanged to be quadratic wrt the charge to mass ratio
# Therefore, we use the quadratic formula for simplicity


sqrt_val = sqrt(Q_zDC**2 + (8*Q_rAC**2/Omega_RF**2)*w0**2)
# =============================================================================
# This value is always > Q_zDC as it's esentially (Q_zDC+ something)
# As a result we ignore the solution with Q_zDC - sqrt_val as this will 
# always be -ve, and a -ve charge to mass ratio is meaningless
# =============================================================================

  
Charge_to_mass = (Q_zDC + sqrt_val)*Omega_RF**2/(4*Q_rAC**2)  
Charge = Charge_to_mass*mass
Charge_Number = Charge/elementary_charge


# Charge_to_mass = w0**2/(Q_rAC - 2*Q_zDC)
# Charge = Charge_to_mass*mass
# Charge_Number = Charge/elementary_charge

print(f'Charge to mass ratio : {Charge_to_mass:.4e} C/kg')
print(f'Total Charge on part : {Charge:.4e} C')
print(f'Number of Charges    : {int(Charge_Number)} e')
