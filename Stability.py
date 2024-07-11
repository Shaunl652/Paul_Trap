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
from scipy.constants import pi, Boltzmann
from scipy.special import mathieu_a, mathieu_b, mathieu_cem, mathieu_sem
from numpy import cos, sin, sqrt, exp

# The x axis of the plots
q_axis = np.linspace(0,1.5 ,1001)


# Initial Parameters
iRadius = 150 # Particle radius nm
density = 2000 # particle density kg/m^3
mass = lambda R: density*4*pi*(R*1e-9)**3/3
imass = mass(iRadius) # mass kg

# Geometric parameters, recall alpha_r = (alpha_x+alpha_y)/2
ialpha_rAC = 0.3622
ialpha_zAC = 0.0307
ialpha_zDC = 0.0999

iZ = 85#9.85e-6 # charge number
iRF_Freq = 0.8 # RF Voltage frequencey kHz
ir0 = 04.00 # distacne to pole from trap centre in mm
iz0 = 16.65 # distance to end caps from trap centre mm
iVac = 450 # RF voltage V
iVdc = 300 # DC volatage V

# Now start on the params q and a

def a_r(Z,alpha,V,z0,RF_Freq,Radius):
    """
    Finds the a_r parameter

    Parameters
    ----------
    Z : INTEGER
        The number of elementry charges on the particle.
    alpha : FLOAT
        The geometric factor alpha_zDC.
    V : FLOAT
        The voltage amplitude on the end caps.
    z0 : FLOAT
        The distance from the centre of the trap to the end cap in mm.
    RF_Freq : FLOAT
        The RF frequency in kHz.
    Radius : FLOAT
        The radius of the particle in nm.

    Returns
    -------
    FLAOT
        The value of a_r.

    """
    
    return ((-4*Z*e/mass(Radius))/((2*pi*RF_Freq*1e3)**2)) *alpha *(V/(z0*1e-3)**2)


def q_r(Z,alpha,V,r0,RF_Freq,Radius):
    """
    Finds the a_r parameter

    Parameters
    ----------
    Z : INTEGER
        The number of elementry charges on the particle.
    alpha : FLOAT
        The geometric factor alpha_rAC.
    V : FLOAT
        The voltage amplitude on the RF electrodes.
    r0 : FLOAT
        The distance from the centre of the trap to the RF electrodes in mm.
    RF_Freq : FLOAT
        The RF frequency in kHz.
    Radius : FLOAT
        The radius of the particle in nm.

    Returns
    -------
    FLAOT
        The value of a_r.

    """
    return ((4*Z*e/mass(Radius))/((2*pi*RF_Freq*1e3)**2)) *alpha *(V/(r0*1e-3)**2)


def omega_i(RF_Freq,q,a):
    """
    Finds the trap frequancy in the i direction

    Parameters
    ----------
    RF_Freq: FLOAT
        The RF frequancy in kHz.
    q : FLOAT
        The value of the q parameter for the relevant axis.
    a : FLAOT
        The value of the a parameter for the relevant axis.

    Returns
    -------
    Float
        The trap frequancy.

    """
    
    return (2*pi*RF_Freq/2)*sqrt((q**2/2) + a)

def trap_depth(alpha,V,Z):
    """
    Finds the trap depth in the relevant axis

    Parameters
    ----------
    alpha : FLOAT
        The geometric factor for the relevant axis.
    V : FLOAT
        Volatage amplitude for the given axis.
    Z : INTEGER
        The number of elemetry charges on the particle.

    Returns
    -------
    FLOAT
        The trap dpeth in K.

    """

    return e*Z*(alpha*V)/Boltzmann

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

# The q and a values of the point in the r axis
qr_val = q_r(iZ,ialpha_rAC,iVac,ir0,iRF_Freq,iRadius)
ar_val = a_r(iZ,ialpha_zDC,iVdc,iz0,iRF_Freq,iRadius)

# The q and a vals of the point in the z axis
qz_val = q_r(iZ,ialpha_zAC,iVac,iz0,iRF_Freq,iRadius)/((ialpha_zAC/ialpha_rAC)*(ir0**2/iz0**2))
az_val = a_r(iZ,ialpha_zDC,iVdc,iz0,iRF_Freq,iRadius)*-2

# The point plotted in the stability diagram
point = ax.scatter(qr_val,ar_val,color='b')

CtM = plt.gcf().text(0.65,0.35,f'Charge to mass ratio: {e*iZ/imass:.2e}',fontsize=14)
omega_r = plt.gcf().text(0.65,0.30,f'$\\omega_r = 2\\pi \\times$ {omega_i(iRF_Freq,qr_val,ar_val)/(2*pi):.2e} Hz',fontsize=14)
omega_z = plt.gcf().text(0.65,0.25,f'$\\omega_z = 2\\pi \\times$ {omega_i(iRF_Freq,qz_val,az_val)/(2*pi):.2e} Hz',fontsize=14)
depth_r = plt.gcf().text(0.65,0.20,f'depth r: {trap_depth(ialpha_rAC, iVac,iZ):.2e} K',fontsize=14)
depth_z = plt.gcf().text(0.65,0.15,f'depth z: {trap_depth(ialpha_zDC, iVdc,iZ):.2e} K',fontsize=14)


ax.legend()

# adjust the main plot to make room for the sliders
fig.subplots_adjust(right=0.6)

# Now add all the sliders
# Slider for AC voltage
axVac = fig.add_axes([0.65, 0.85, 0.3, 0.03])
Vac_slider = Slider(
    ax=axVac,
    label='$V_{AC}$ [V]',
    valmin=50,
    valmax=1000,
    valinit=iVac
)
# Slider for DC voltage
axVdc= fig.add_axes([0.65, 0.8, 0.3, 0.03])
Vdc_slider = Slider(
    ax=axVdc,
    label='$V_{DC}$ [V]',
    valmin=50,
    valmax=1000,
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
# Slider for charges
axZ= fig.add_axes([0.65, 0.6, 0.3, 0.03])
Z_slider = Slider(
    ax=axZ,
    label='$Z$',
    valmin=1,
    valmax=1000,
    valinit=iZ
)
# Slider for Omega
axRF_Freq= fig.add_axes([0.65, 0.55, 0.3, 0.03])
RF_Freq_slider = Slider(
    ax=axRF_Freq,
    label='$\\Omega/2\pi$ [kHz]',
    #valstep=np.logspace(0,6,101),
    valmin=0.01,
    valmax=20,
    valinit=iRF_Freq
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
    valmax=50,
    valinit=iz0
)

# Slider for particle radius
axRad = fig.add_axes([0.65, 0.40, 0.3, 0.03])
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
    alpha_rAC = arAC_slider.val
    alpha_zAC = azAC_slider.val
    alpha_zDC = azDC_slider.val
    Z = Z_slider.val
    RF_Freq = RF_Freq_slider.val
    Radius = Rad_slider.val
    r0 = r0_slider.val
    z0 = z0_slider.val
    
    # The q and a values of the point in the r axis
    qr_val = q_r(Z,alpha_rAC,Vac,r0,RF_Freq,Radius)
    ar_val = a_r(Z,alpha_zDC,Vdc,z0,RF_Freq,Radius)

    # The q and a vals of the point in the z axis
    qz_val = q_r(iZ,ialpha_zAC,iVac,iz0,iRF_Freq,iRadius)/((ialpha_zAC/ialpha_rAC)*(ir0**2/iz0**2))
    az_val = a_r(iZ,ialpha_zDC,iVdc,iz0,iRF_Freq,iRadius)*-2
    # Updates the point
    point.set_offsets([qr_val,ar_val])


    # Updatest the exclusion regions
    global ExcludeR1,ExcludeR2,ExcludeZ1,ExcludeZ2
    ExcludeR1.remove()
    ExcludeR2.remove()
    ExcludeZ1.remove()
    ExcludeZ2.remove()

    ExcludeR1 = ax.fill_between(q_axis,+mathieu_a(0,q_axis),  y2=-10,color='tab:orange',alpha=0.5)
    ExcludeR2 = ax.fill_between(q_axis,+mathieu_b(1,q_axis),  y2=+10,color='tab:orange',alpha=0.5)
    ExcludeZ1 = ax.fill_between(q_axis,-mathieu_a(0,q_axis*(alpha_zAC/alpha_rAC)*(r0**2/z0**2))/2,y2=+10,color='tab:red',alpha=0.5)
    ExcludeZ2 = ax.fill_between(q_axis,-mathieu_b(1,q_axis*(alpha_zAC/alpha_rAC)*(r0**2/z0**2))/2,y2=-10,color='tab:red',alpha=0.5)


    CtM.set_text(f'Charge to mass ratio: {e*Z/mass(Radius):.2e}')
    
    omega_r.set_text(f'$\\omega_r = 2\\pi \\times$ {omega_i(RF_Freq,qr_val,ar_val)/(2*pi):.2e} Hz')
    omega_z.set_text(f'$\\omega_z = 2\\pi \\times$ {omega_i(RF_Freq,qz_val,az_val)/(2*pi):.2e} Hz')

    
    depth_r.set_text(f' depth r: {trap_depth(alpha_rAC, Vac,Z):.2e} K')
    depth_z.set_text(f' depth r: {trap_depth(alpha_zAC, Vdc,Z):.2e} K')

    # Redraw the plot
    fig.canvas.draw_idle()


# register the update function with each slider
Vac_slider.on_changed(update)
Vdc_slider.on_changed(update)
arAC_slider.on_changed(update)
azAC_slider.on_changed(update)
azDC_slider.on_changed(update)
Z_slider.on_changed(update)
RF_Freq_slider.on_changed(update)
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
    RF_Freq_slider.reset()
    r0_slider.reset()
    z0_slider.reset()
    Rad_slider.reset()
button.on_clicked(reset)

plt.show()