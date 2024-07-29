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
iRadius = 150e-9 # Particle radius m
density = 2000 # particle density kg/m^3
mass = lambda R: density*4*pi*(R)**3/3
imass = mass(iRadius) # mass kg

# Geometric parameters, recall alpha_r = (alpha_x+alpha_y)/2
ialpha_rAC = 0.4064
ialpha_zAC = 0.0457
ialpha_zDC = 0.1094

iZ = 85#9.85e-6 # charge number
iRF_Freq = 0.8e3 # # RF Voltage frequencey Hz
iOmega = 2*pi *iRF_Freq
ir0 = 04.00e-3 # distacne to pole from trap centre in m
iz0 = 16.65e-3 # distance to end caps from trap centre m
iVac = 450 # RF voltage V
iVdc = 300 # DC volatage V

# Now start on the params q and a

def a_r(Z,alpha,V,z0,Omega,Radius):
    """
    Finds the a_r parameter

    Parameters
    ----------
    Z : INTEGER
        The number of elementry charges on the particle.
    alpha : FLOAT
        The geometric factor alpha_zDC.
    V : FLOAT
        The voltage amplitude on the end caps in V.
    z0 : FLOAT
        The distance from the centre of the trap to the end cap in m.
    Omega : FLOAT
        The angluar RF frequency in Rad/s.
    Radius : FLOAT
        The radius of the particle in m.

    Returns
    -------
    FLAOT
        The value of a_r.

    """
    Q = (alpha*V)/(z0**2)
    return -((4*Z*e*Q)/(mass(Radius)*Omega**2))



def q_r(Z,alpha,V,r0,Omega,Radius):
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
        The distance from the centre of the trap to the RF electrodes in m.
    Omega : FLOAT
        The angular RF frequency in Rad/s.
    Radius : FLOAT
        The radius of the particle in m.

    Returns
    -------
    FLAOT
        The value of a_r.

    """
    Q = (alpha*V)/(r0**2)
    return ((4*Z*e*Q)/(mass(Radius)*Omega**2))



def omega_i(Omega,q,a):
    """
    Finds the trap frequancy in the i direction

    Parameters
    ----------
    Omega: FLOAT
        The angular RF frequancy in Rad/s.
    q : FLOAT
        The value of the q parameter for the relevant axis.
    a : FLAOT
        The value of the a parameter for the relevant axis.

    Returns
    -------
    Float
        The trap frequancy.

    """
    
    return (Omega/2)*sqrt((q**2/2) + a)

def trap_depth(mass,omega,d0):
    """
    

    Parameters
    ----------
    mass : FLAOT
        The mass of the trapped object in kg.
    omega : FLOAT
        The trap frequency in the given axis.
    d0 : FLOAT
        The distance from the trap centre the the relevant electrode.

    Returns
    -------
    FLOAT
        The trap depth in the given axis in K.

    """

    return mass*omega**2*d0**2/Boltzmann


from matplotlib.widgets import Button, Slider

# Create the figure 
fig, ax= plt.subplots()

ax.set_xlim(0,1.5)
ax.set_ylim(-0.5,0.5)
ax.set_xlabel('$|q|$')
ax.set_ylabel('$a$')

q_conversion = (ialpha_zAC/ialpha_rAC)*(ir0/iz0)**2

# Set up initial excludion regions
ExcludeR1 = ax.fill_between(q_axis,+mathieu_a(0,q_axis),  y2=-10,color='tab:orange',alpha=0.5,label='Radial Unstable')
ExcludeR2 = ax.fill_between(q_axis,+mathieu_b(1,q_axis),  y2=+10,color='tab:orange',alpha=0.5)
ExcludeZ1 = ax.fill_between(q_axis,[0 for i in q_axis],   y2=+10,color='tab:red',   alpha=0.5,label='Axialy Unstable')
#ExcludeZ1 = ax.fill_between(q_axis,-mathieu_a(0,q_axis*q_conversion)/2,y2=+10,color='tab:red',alpha=0.5,label='Axialy Unstable')
#ExcludeZ2 = ax.fill_between(q_axis,-mathieu_b(1,q_axis*q_conversion)/2,y2=-10,color='tab:red',alpha=0.5)
#ExcludeR3 = ax.fill_between(q_axis,-(q_axis*q_conversion)**2/4,y2=-10,color='tab:orange',alpha=0.5)

# The q and a values of the point in the r axis
qr_val = q_r(iZ,ialpha_rAC,iVac,ir0,iOmega,iRadius)
ar_val = a_r(iZ,ialpha_zDC,iVdc,iz0,iOmega,iRadius)

# The q and a vals of the point in the z axis
qz_val = qr_val*q_conversion
az_val = ar_val*(-2)

# The point plotted in the stability diagram
point = ax.scatter(qr_val,ar_val,color='b')

omega_r_val = omega_i(iOmega,qr_val,ar_val)
omega_z_val = omega_i(iOmega,qz_val,az_val)#(iOmega/2)*sqrt(az_val)#sqrt(2*iZ*e*Qz/imass)#omega_i(iOmega,qz_val,az_val)##

CtM = plt.gcf().text(0.65,0.35,f'Charge to mass ratio: {e*iZ/imass:.2e}',fontsize=14)

omega_r = plt.gcf().text(0.65,0.30,f'$\\omega_r = 2\\pi \\times$ {omega_r_val/(2*pi):.0f} Hz',fontsize=14)
omega_z = plt.gcf().text(0.65,0.25,f'$\\omega_z = 2\\pi \\times$ {omega_z_val/(2*pi):.0f} Hz',fontsize=14)

depth_r = plt.gcf().text(0.65,0.20,f'depth r: {trap_depth(imass,omega_r_val,ir0):.2e} K',fontsize=14)
depth_z = plt.gcf().text(0.65,0.15,f'depth z: {trap_depth(imass,omega_z_val,iz0):.2e} K',fontsize=14)

# if qr_val > ir0:
#     amptd_r = plt.gcf().text(0.65,0.10,f'Radial Amplitude: {qr_val*1e3:.2f} mm EXCEEDS TRAP BOUNDS',fontsize=14,color='r')
# else:
#     amptd_r = plt.gcf().text(0.65,0.10,f'Radial Amplitude: {qr_val*1e3:.2f} mm',fontsize=14,color='k')

# if qz_val > iz0:
#     amptd_z = plt.gcf().text(0.65,0.05,f'Axial Amplitude: {qz_val*1e3:.2f} mm EXCEEDS TRAP BOUNDS',fontsize=14,color='r')
# else:
#     amptd_z = plt.gcf().text(0.65,0.05,f'Axial Amplitude: {qz_val*1e3:.2f} mm',fontsize=14,color='k')

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
    valstep=1,
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
    valinit=iRF_Freq/1e3
)

# Slider for r0
axr0= fig.add_axes([0.65, 0.5, 0.3, 0.03])
r0_slider = Slider(
    ax=axr0,
    label='$R_0$ [mm]',
    valmin=0.5,
    valmax=20,
    valinit=ir0/1e-3
)
# Slider for z0
axz0= fig.add_axes([0.65, 0.45, 0.3, 0.03])
z0_slider = Slider(
    ax=axz0,
    label='$z_0$ [mm]',
    valmin=1.,
    valmax=50,
    valinit=iz0/1e-3
)

# Slider for particle radius
axRad = fig.add_axes([0.65, 0.40, 0.3, 0.03])
Rad_slider = Slider(
    ax=axRad,
    label='$R$ [nm]',
    valmin=100,
    valmax=1000,
    valinit=iRadius/1e-9
)



# The function to be called anytime a slider's value changes
def update(val):
    # Sort out variables
    Vac       = Vac_slider.val
    Vdc       = Vdc_slider.val
    alpha_rAC = arAC_slider.val
    alpha_zAC = azAC_slider.val
    alpha_zDC = azDC_slider.val
    Z         = Z_slider.val
    RF_Freq   = RF_Freq_slider.val*1e3
    Omega     = 2*pi*RF_Freq
    Radius    = Rad_slider.val*1e-9
    r0        = r0_slider.val*1e-3
    z0        = z0_slider.val*1e-3
    
    mass_val = mass(Radius)
    q_conversion = (alpha_zAC/alpha_rAC)*(r0/z0)**2
    # The q and a values of the point in the r axis
    qr_val = q_r(Z,alpha_rAC,Vac,r0,Omega,Radius)
    ar_val = a_r(Z,alpha_zDC,Vdc,z0,Omega,Radius)

    # The q and a vals of the point in the z axis
    qz_val = qr_val*q_conversion
    az_val = ar_val*(-2)
    # Updates the point
    point.set_offsets([qr_val,ar_val])


# =============================================================================
#     # Updatest the exclusion regions
#     global ExcludeR1,ExcludeR2,ExcludeZ1,ExcludeZ2,ExcludeR3
#     ExcludeR1.remove()
#     ExcludeR2.remove()
#     ExcludeZ1.remove()
#     ExcludeZ2.remove()
#     ExcludeR3.remove()
#     
#     ExcludeR1 = ax.fill_between(q_axis,+mathieu_a(0,q_axis),  y2=-10,color='tab:orange',alpha=0.5)
#     ExcludeR2 = ax.fill_between(q_axis,+mathieu_b(1,q_axis),  y2=+10,color='tab:orange',alpha=0.5)
#     ExcludeZ1 = ax.fill_between(q_axis,-mathieu_a(0,q_axis*q_conversion)/2,y2=+10,color='tab:red',alpha=0.5)
#     ExcludeZ2 = ax.fill_between(q_axis,-mathieu_b(1,q_axis*q_conversion)/2,y2=-10,color='tab:red',alpha=0.5)
#     ExcludeR3 = ax.fill_between(q_axis,-(q_axis*q_conversion)**2/4,y2=-10,color='tab:orange',alpha=0.5)
# =============================================================================

    CtM.set_text(f'Charge to mass ratio: {e*Z/mass_val:.2e}')
    
    omega_r_val = omega_i(Omega,qr_val,ar_val)
    omega_z_val = omega_i(Omega,qz_val,az_val)#omega_i(Omega,qz_val,az_val)#(Omega/2)*sqrt(abs(az_val))#
    omega_r.set_text(f'$\\omega_r = 2\\pi \\times$ {omega_r_val/(2*pi):.0f} Hz')
    omega_z.set_text(f'$\\omega_z = 2\\pi \\times$ {omega_z_val/(2*pi):.0f} Hz')

    depth_r.set_text(f' depth r: {trap_depth(mass_val,omega_r_val,r0):.2e} K')
    depth_z.set_text(f' depth z: {trap_depth(mass_val,omega_z_val,z0):.2e} K')
    
    # if qr_val > r0:
    #     amptd_r.set_text(0.65,0.10,f'Radial Amplitude: {qr_val*1e3:.2f} mm EXCEEDS TRAP BOUNDS',fontsize=14,color='r')
    # else:
    #     amptd_r.set_text(0.65,0.10,f'Radial Amplitude: {qr_val*1e3:.2f} mm',fontsize=14,color='k')

    # if qz_val > z0:
    #     amptd_z.set_text(0.65,0.05,f'Axial Amplitude: {qz_val*1e3:.2f} mm EXCEEDS TRAP BOUNDS',fontsize=14,color='r')
    # else:
    #     amptd_z.set_text(0.65,0.05,f'Axial Amplitude: {qz_val*1e3:.2f} mm',fontsize=14,color='k')

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