#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Plots the Paschen curve in units of V vs m*mbar
# =============================================================================

import numpy as np

# taken from Wikipedia
def paschen(pd):
    # Reads in the pressure*distance in mbar meters
    # using gamma = 0.01
    # Values for air from wikipedia reworked to be in more useful units
    a =  1125 #(mBar m)^-1
    b = 27375 #V/(mBar m)
    V = b * pd / (np.log((a * pd) / np.log(1+1/.01)))
    
    # Only returns pd and V when V > 10 as this forces into the region where this is valid
    # We also allow an answer should we only pass a single value to the function or a range of values
    if hasattr(V, '__iter__'):
        return pd[V > 10], V[V > 10]
    else:
        return pd,V


P_LV = 1e3 # Pressure in mbar
P_HV = 1e-4 # pressure of the vacum


# When running the code in full we run over a good range of values for comparison with previous plots
xaxis = np.logspace(-3,1,1001)



import matplotlib.pyplot as plt
# Plot the graph
fig,ax1 = plt.subplots()
P,V = paschen(xaxis)
ax1.plot(P,V)
ax1.set(xscale='log',xlabel='$pd$ [mBar m]',yscale='log',ylabel='Breakdown Voltage [V]')
ax1.legend()

