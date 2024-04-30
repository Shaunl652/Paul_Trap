#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Hope is to have code that will decide if the trap is stable or not based on the
# given experimental parameters
# The stable region comes from stable solutions to the Mathieu equations
# =============================================================================


import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import elementary_charge as e
from scipy.constants import pi
from scipy.special import mathieu_a, mathieu_b, mathieu_cem, mathieu_sem
from numpy import cos, sin, sqrt, exp

# The x axis of the plots
q_axis = np.linspace(0,1.5 ,1001)


# Initial Parameters

iRadius = 20 # Particle radius um
density = 1000 # particle density kg/m^3
#imass = density*4*pi*(iRadius*1e-6)**3/3 # mass kg

# Geometric parameters, recall alpha_r = (alpha_x+alpha_y)/2
ialpha_rAC = 0.5232
ialpha_zAC = 0.5716
ialpha_zDC = 0.5232

iZ = 1997 # No of elementry charges
iOmega = 5 # RF Voltage frequencey kHz
ir0 = 8.0 # distacne to pole from trap centre in mm
iz0 = 20.0 # distance to end caps from trap centre mm
iVac = 1000 # RF voltage V
iVdc = 100 # DC volatage V

# Now start on the params q and a

def ar(Z,alpha,V,x,Omega,Radius):
    # value of the a parameter
    mass = density*4*pi*(Radius*1e-6)**3/3
    return ((-4*Z*e)/(mass*(2*pi*Omega*1e3)**2)) *alpha *(V/(x*1e-3)**2)


def qr(Z,alpha,V,x,Omega,Radius):
    # Magnitude of q parameter
    mass = density*4*pi*(Radius*1e-6)**3/3
    return abs(((4*Z*e)/(mass*(2*pi*Omega*1e3)**2)) *alpha *(V/(x*1e-3)**2))

charges = np.linspace(0,500,1001)

def charges_func(alpha_r,alpha_z,Vac,Vdc,r0,z0,q):
    return -q*r0**2*alpha_z*Vdc/(alpha_r*Vac*z0**2)

from matplotlib.widgets import Button, Slider

# Create the figure 
fig, ax= plt.subplots()

ax.set_xlim(0,1.5)
ax.set_ylim(-0.5,0.5)
ax.set_xlabel('$|q|$')
ax.set_ylabel('$a$')
# Set up initial excludion regions
ExcludeR1 = ax.fill_between(q_axis,+mathieu_a(0,q_axis),  y2=-10,color='tab:orange',alpha=0.5,label='Radial Unstable')
ExcludeR2 = ax.fill_between(q_axis,+mathieu_b(1,q_axis),  y2=+10,color='tab:orange',alpha=0.5)
ExcludeZ1 = ax.fill_between(q_axis,-mathieu_a(0,q_axis*(ialpha_zAC/ialpha_rAC)*(ir0**2/iz0**2))/2,y2=+10,color='tab:red',alpha=0.5,label='Axialy Unstable')
ExcludeZ2 = ax.fill_between(q_axis,-mathieu_b(1,q_axis*(ialpha_zAC/ialpha_rAC)*(ir0**2/iz0**2))/2,y2=-10,color='tab:red',alpha=0.5)
# The point defining the trap in the parameter space
point = ax.scatter(qr(iZ,ialpha_rAC,iVac,ir0,iOmega,iRadius),ar(iZ,ialpha_zDC,iVdc,iz0,iOmega,iRadius),color='b')
charge_line, = ax.plot(q_axis,charges_func(ialpha_rAC, ialpha_zDC, iVac, iVdc, ir0, iz0, q_axis),color='g',label='Charges')
    #qr(charges,ialpha_rAC,iVac,ir0,iOmega,iRadius),ar(charges,ialpha_zDC,iVdc,iz0,iOmega,iRadius),color='g',label='Charges')

ax.legend()

# adjust the main plot to make room for the sliders
fig.subplots_adjust(right=0.6)

# Now add all the sliders
# Slider for AC voltage
axVac = fig.add_axes([0.65, 0.85, 0.3, 0.03])
Vac_slider = Slider(
    ax=axVac,
    label='$V_{AC}$ [V]',
    valmin=100,
    valmax=10000,
    valinit=iVac
)
# Slider for DC voltage
axVdc= fig.add_axes([0.65, 0.8, 0.3, 0.03])
Vdc_slider = Slider(
    ax=axVdc,
    label='$V_{DC}$ [V]',
    valmin=100,
    valmax=5000,
    valinit=iVdc
    )
# Slider for alpha_rac
axar_AC= fig.add_axes([0.65, 0.75, 0.3, 0.03])
arAC_slider = Slider(
    ax=axar_AC,
    label='$\\alpha_r^{AC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_rAC
)
# Slider for alpha_zac
axaz_AC= fig.add_axes([0.65, 0.7, 0.3, 0.03])
azAC_slider = Slider(
    ax=axaz_AC,
    label='$\\alpha_z^{AC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_zAC
)
# Slider for alpha_zdc
axaz_DC= fig.add_axes([0.65, 0.65, 0.3, 0.03])
azDC_slider = Slider(
    ax=axaz_DC,
    label='$\\alpha_z^{DC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_zDC
)
# Slider for charge number
axZ= fig.add_axes([0.65, 0.6, 0.3, 0.03])
Z_slider = Slider(
    ax=axZ,
    label='$Z$',
    valmin=100,
    valmax=+3000,
    valstep=1,
    valinit=iZ
)
# Slider for Omega
axOmega= fig.add_axes([0.65, 0.55, 0.3, 0.03])
Omega_slider = Slider(
    ax=axOmega,
    label='$\\Omega$ [kHz]',
    #valstep=np.logspace(0,6,101),
    valmin=5,
    valmax=20,
    valinit=iOmega
)

# Slider for r0
axr0= fig.add_axes([0.65, 0.5, 0.3, 0.03])
r0_slider = Slider(
    ax=axr0,
    label='$R_0$ [mm]',
    valmin=0.5,
    valmax=20,
    valinit=ir0
)
# Slider for z0
axz0= fig.add_axes([0.65, 0.45, 0.3, 0.03])
z0_slider = Slider(
    ax=axz0,
    label='$z_0$ [mm]',
    valmin=1.,
    valmax=20,
    valinit=iz0
)
# Slider for particle radius
axRad = fig.add_axes([0.65, 0.40, 0.3, 0.03])
Rad_slider = Slider(
    ax=axRad,
    label='$R$ [$\\mu$m]',
    valmin=10,
    valmax=30,
    valinit=iRadius
)


# The function to be called anytime a slider's value changes
def update(val):
    # Sort out variables
    Vac = Vac_slider.val
    Vdc = Vdc_slider.val
    alpha_rAC = arAC_slider.val
    alpha_zAC = azAC_slider.val
    alpha_zDC = azDC_slider.val
    Z = Z_slider.val
    Omega = Omega_slider.val
    Radius = Rad_slider.val
    r0 = r0_slider.val
    z0 = z0_slider.val
    
    # Updates the point
    point.set_offsets([qr(Z,alpha_rAC,Vac,r0,Omega,Radius),ar(Z,alpha_zDC,Vdc,z0,Omega,Radius)])
    charge_line.set_ydata(charges_func(alpha_rAC, alpha_zDC, Vac, Vdc, r0, z0, q_axis))

    # Updatest eh exclusion regions
    global ExcludeR1,ExcludeR2,ExcludeZ1,ExcludeZ2
    ExcludeR1.remove()
    ExcludeR2.remove()
    ExcludeZ1.remove()
    ExcludeZ2.remove()
    
    ExcludeR1 = ax.fill_between(q_axis,+mathieu_a(0,q_axis),  y2=-10,color='tab:orange',alpha=0.5)
    ExcludeR2 = ax.fill_between(q_axis,+mathieu_b(1,q_axis),  y2=+10,color='tab:orange',alpha=0.5)
    ExcludeZ1 = ax.fill_between(q_axis,-mathieu_a(0,q_axis*(alpha_zAC/alpha_rAC)*(r0**2/z0**2))/2,y2=+10,color='tab:red',alpha=0.5)
    ExcludeZ2 = ax.fill_between(q_axis,-mathieu_b(1,q_axis*(alpha_zAC/alpha_rAC)*(r0**2/z0**2))/2,y2=-10,color='tab:red',alpha=0.5)

    # Redraw the plot
    fig.canvas.draw_idle()


# register the update function with each slider
Vac_slider.on_changed(update)
Vdc_slider.on_changed(update)
arAC_slider.on_changed(update)
azAC_slider.on_changed(update)
azDC_slider.on_changed(update)
Z_slider.on_changed(update)
Omega_slider.on_changed(update)
r0_slider.on_changed(update)
z0_slider.on_changed(update)
Rad_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

# Restores the initial values
def reset(event):
    Vac_slider.reset()
    Vdc_slider.reset()
    arAC_slider.reset()
    azAC_slider.reset()
    azDC_slider.reset()
    Z_slider.reset()
    Omega_slider.reset()
    r0_slider.reset()
    z0_slider.reset()
    Rad_slider.reset()
button.on_clicked(reset)

plt.show()






