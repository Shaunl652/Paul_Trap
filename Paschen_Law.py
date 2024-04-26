#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:02:01 2024

@author: shaun
"""

import numpy as np

# taken from Wikipedia
def paschen(pd):
    # using gamma = 0.01
    # Values for air from wikipedia reworked to be in more useful units
    a =  1125 #(mBar m)^-1
    b = 27375 #V/(mBar m)
    V = b * pd / (np.log((a * pd) / np.log(1+1/.01)))
    # Only returns pd and V when V > 10
    
    if hasattr(V, '__iter__'):
        return pd[V > 10], V[V > 10]
    else:
        return pd,V


P_LV = 1e3 # Pressure in mbar
P_HV = 1e-4 # pressure of the vacum


xaxis = np.logspace(-3,1,1001)



import matplotlib.pyplot as plt

fig,ax1 = plt.subplots()
#ax2 = ax1.twiny()

P,V = paschen(xaxis)
#P = P*1e3
ax1.plot(P,V)
ax1.set(xscale='log',xlabel='$pd$ [mBar m]',yscale='log',ylabel='Breakdown Voltage [V]')
ax1.plot(P,[5e3 for i in P],label='RF Voltage')
ax1.plot(P,[600 for i in P],label='DC Voltage')
ax1.plot(P,[5e3-600 for i in P],label='Difference')
ax1.legend()
#ax2.plot(P/(P_HV),V)
#ax2.set(xscale='log',xlabel='Distance at $10^{-4}$ mBar [m]',yscale='log',ylabel='Breakdown Voltage [V]')
#ax.set_ylim(1e2,1e6)
