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

iRadius = 150 # Particle radius m
density = 2000 # particle density kg/m^3
imass = density*4*pi*(iRadius*1e-9)**3/3 # mass kg

# Geometric parameters
ialpha_xAC = 0.5556
ialpha_yAC = 0.5000
ialpha_zAC = 0.2205
ialpha_zDC = 0.4682

iZ = 85 # No of elementry charges
iOmega = 5 # RF Voltage frequencey kHz
ix0 = 3.75 # distacne to pole from trap centre in mm
iy0 = 3.75 # distacne to pole from trap centre in mm
iz0 = 7.0 # distance to end caps from trap centre mm
iVac = 5000 # RF voltage V
iVdc = 300 # DC volatage V

# Now start on the params q and a

# We keep ar and qr as the forms are the same (when considering |q|) just some different numbers
def ar(Z,alpha,V,x,Omega,Radius):
    # value of the a parameter
    mass = density*4*pi*(Radius*1e-9)**3/3
    return ((-4*Z*e)/(mass*(2*pi*Omega*1e3)**2)) *alpha *(V/(x*1e-3)**2)


def qr(Z,alpha,V,x,Omega,Radius):
    # Magnitude of q parameter
    mass = density*4*pi*(Radius*1e-9)**3/3
    return ((4*Z*e)/(mass*(2*pi*Omega*1e3)**2)) *alpha *(V/(x*1e-3)**2)

def az(Z,alpha,V,x,Omega,Radius):
    # value of the a parameter
    mass = density*4*pi*(Radius*1e-9)**3/3
    return ((8*Z*e)/(mass*(2*pi*Omega*1e3)**2)) *alpha *(V/(x*1e-3)**2)


def qz(Z,alpha,V,x,Omega,Radius):
    # Magnitude of q parameter
    mass = density*4*pi*(Radius*1e-9)**3/3
    return ((4*Z*e)/(mass*(2*pi*Omega*1e3)**2)) *alpha *(V/(x*1e-3)**2)



from matplotlib.widgets import Button, Slider

# Create the figure 
fig, ax= plt.subplots()

ax.set_xlim(0,1.5)
ax.set_ylim(-0.5,0.5)
ax.set_xlabel('$|q|$')
ax.set_ylabel('$a$')
# Set up initial excludion regions
# This time we only have one because I am seperating each axis from the dot
ax.fill_between(q_axis,+mathieu_a(0,q_axis),  y2=-10,color='tab:red',alpha=0.5,label='Motion Unstable')
ax.fill_between(q_axis,+mathieu_b(1,q_axis),  y2=+10,color='tab:red',alpha=0.5)

# The points defining the trap in the parameter space
x_point = ax.scatter(qr(iZ,ialpha_xAC,iVac,ix0,iOmega,iRadius),ar(iZ,ialpha_zDC,iVdc,iz0,iOmega,iRadius),color='b',label='x Motion')
y_point = ax.scatter(qr(iZ,ialpha_yAC,iVac,iy0,iOmega,iRadius),ar(iZ,ialpha_zDC,iVdc,iz0,iOmega,iRadius),color='g',label='y Motion')
z_point = ax.scatter(qz(iZ,ialpha_zAC,iVac,iz0,iOmega,iRadius),az(iZ,ialpha_zDC,iVdc,iz0,iOmega,iRadius),color='k',label='z Motion')


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
# Slider for alpha_xac
axax_AC= fig.add_axes([0.65, 0.75, 0.3, 0.03])
axAC_slider = Slider(
    ax=axax_AC,
    label='$\\alpha_x^{AC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_xAC
)
# Slider for alpha_yac
axay_AC= fig.add_axes([0.65, 0.7, 0.3, 0.03])
ayAC_slider = Slider(
    ax=axay_AC,
    label='$\\alpha_y^{AC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_yAC
)
# Slider for alpha_zac
axaz_AC= fig.add_axes([0.65, 0.65, 0.3, 0.03])
azAC_slider = Slider(
    ax=axaz_AC,
    label='$\\alpha_z^{AC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_zAC
)
# Slider for alpha_zdc
axaz_DC= fig.add_axes([0.65, 0.6, 0.3, 0.03])
azDC_slider = Slider(
    ax=axaz_DC,
    label='$\\alpha_z^{DC}$',
    valmin=0,
    valmax=1,
    valinit=ialpha_zDC
)
# Slider for charge number
axZ= fig.add_axes([0.65, 0.55, 0.3, 0.03])
Z_slider = Slider(
    ax=axZ,
    label='$Z$',
    valmin=3,
    valmax=300,
    valstep=1,
    valinit=iZ
)
# Slider for Omega
axOmega= fig.add_axes([0.65, 0.5, 0.3, 0.03])
Omega_slider = Slider(
    ax=axOmega,
    label='$\\Omega$ [kHz]',
    #valstep=np.logspace(0,6,101),
    valmin=5,
    valmax=20,
    valinit=iOmega
)

# Slider for x0
axx0= fig.add_axes([0.65, 0.45, 0.3, 0.03])
x0_slider = Slider(
    ax=axx0,
    label='$x_0$ [mm]',
    valmin=0.5,
    valmax=20,
    valinit=ix0
)
# Slider for r0
axy0= fig.add_axes([0.65, 0.4, 0.3, 0.03])
y0_slider = Slider(
    ax=axy0,
    label='$y_0$ [mm]',
    valmin=0.5,
    valmax=20,
    valinit=iy0
)
# Slider for z0
axz0= fig.add_axes([0.65, 0.35, 0.3, 0.03])
z0_slider = Slider(
    ax=axz0,
    label='$z_0$ [mm]',
    valmin=1.,
    valmax=20,
    valinit=iz0
)
# Slider for particle radius
axRad = fig.add_axes([0.65, 0.3, 0.3, 0.03])
Rad_slider = Slider(
    ax=axRad,
    label='$R$ [nm]',
    valmin=100,
    valmax=1000,
    valinit=iRadius
)


# The function to be called anytime a slider's value changes
def update(val):
    # Sort out variables
    Vac = Vac_slider.val
    Vdc = Vdc_slider.val
    alpha_xAC = axAC_slider.val
    alpha_yAC = ayAC_slider.val
    alpha_zAC = azAC_slider.val
    alpha_zDC = azDC_slider.val
    Z = Z_slider.val
    Omega = Omega_slider.val
    Radius = Rad_slider.val
    x0 = x0_slider.val
    y0 = y0_slider.val
    z0 = z0_slider.val
    
    # Updates the point
    x_point.set_offsets([qr(Z,alpha_xAC,Vac,x0,Omega,Radius),ar(Z,alpha_zDC,Vdc,z0,Omega,Radius)])
    y_point.set_offsets([qr(Z,alpha_yAC,Vac,y0,Omega,Radius),ar(Z,alpha_zDC,Vdc,z0,Omega,Radius)])
    z_point.set_offsets([qz(Z,alpha_zAC,Vac,z0,Omega,Radius),az(Z,alpha_zDC,Vdc,z0,Omega,Radius)])


    # Redraw the plot
    fig.canvas.draw_idle()


# register the update function with each slider
Vac_slider.on_changed(update)
Vdc_slider.on_changed(update)
axAC_slider.on_changed(update)
ayAC_slider.on_changed(update)
azAC_slider.on_changed(update)
azDC_slider.on_changed(update)
Z_slider.on_changed(update)
Omega_slider.on_changed(update)
x0_slider.on_changed(update)
y0_slider.on_changed(update)
z0_slider.on_changed(update)
Rad_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

# Restores the initial values
def reset(event):
    Vac_slider.reset()
    Vdc_slider.reset()
    axAC_slider.reset()
    ayAC_slider.reset()
    azAC_slider.reset()
    azDC_slider.reset()
    Z_slider.reset()
    Omega_slider.reset()
    x0_slider.reset()
    y0_slider.reset()
    z0_slider.reset()
    Rad_slider.reset()
button.on_clicked(reset)

plt.show()






