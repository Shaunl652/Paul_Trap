#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Takes the radii of the inner and outer electrodes, and the magnitude of the 
# voltages applied then gives the potential as a function of z
# We also mark the locations of z0 and zmax and give the trap depth 
# =============================================================================

import numpy as np
from numpy import sqrt,trapz 

def psi(z,epsilon,a,b):
    """
    Finds the potential at the point z

    Parameters
    ----------
    z : Array or float
        z position.
    epsilon : FLAOT
        Ratio of the inner volatge over the outer voltage.
    a : Float
        radius of inner ring in m.
    b : FLAOT
        Radius of outer ring in m.

    Returns
    -------
    Array or float
        The potential at the z location(s).

    """
    


    # This is the differentiation from Alda EQ2 givein by mathematica
    term1 = b**2/((1+(b/z)**2)**(3/2)*z**3)
    term2 = ((1-epsilon)*a**2)/((1+(a/z)**2)**(3/2)*z**3)
    
    Dkappa = term1 + term2
    
    return np.abs(Dkappa)**2

def z0(a,b,e):
    
    numer = b**2 * a**(4/3) * (1-e)**(2/3) - a**2 * b**(4/3)
    denom = b**(4/3) - a**(4/3) * (1-e)**(2/3)
    
    return sqrt(numer/denom)


def zmax(a,b,e):
    
    numer = b**2 * a**(4/5) * (1-e)**(2/5) - a**2 * b**(4/5)
    denom = b**(4/5) - a**(4/5) * (1-e)**(2/5)
    
    return sqrt(numer/denom)

def Trap_Depth(a,b,e):
    
    return psi(zmax(a,b,e),e,a,b) - psi(z0(a,b,e),e,a,b)
