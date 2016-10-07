'''
Craig Langford

This script has two main steps:
    1. Creates a system of particles with random initial positions and velocities.
    2. Simulates the particles interactions and measures the kinetic
       energy during this process.
'''

import random as rnd
import numpy as np
import scipy.constants as constants
import time
import matplotlib.pyplot as plt

# Default values
filename = 'DPD Simulation.xyz'
particle = 'O'
n = 360
p = 0.4
m = 1
dt = 0.03
T = 1
d = 1.
timesteps = 10000

cutoff = 2.5

# Calculated values

r = d/2
V_sphere = 4/3 * np.pi * r**3
V_tot = n*V_sphere/p
L = V_tot**1./3

cutoff2 = cutoff**2

rr = np.zeros((n,3))
vr = np.zeros((n,3))
fr = np.zeros((n,3))
dt = 0.03
KE = 3/2 * n * T
v_avg = np.sqrt(2 * KE / n / m)
KE_array =  np.zeros((timesteps + 1))
PE_array =  np.zeros((timesteps + 1))
TE_array =  np.zeros((timesteps + 1))
T_array = np.zeros((timesteps + 1))
p_center_array = np.zeros((timesteps + 1,3))

f = open( filename, 'w' )
with open( filename, 'a' ) as data:
    data.write( '%s \nSystem of particles following DPD simulation.' % n )
for i in range(0,n):
    overlap = True
    while overlap == True:
        x = rnd.random()*(L)
        y = rnd.random()*(L)
        z = rnd.random()*(L)
        if i == 0:
            overlap = False
        for j in range(0,i):
            dx = x - rr[j][0]
            dy = y - rr[j][1]
            dz = z - rr[j][2]
            if dx > L - d:
                dx = dx - L
            elif dx < -L + d:
                dx = dx + L
            if dy > L - d:
                dy = dy - L
            elif dy < -L + d:
                dy = dy + L
            if dz > L - d:
                dz = dz - L
            elif dz < -L + d:
                dz = dz + L
            if dx**2 + dy**2 + dz**2 > 2*r**2:
                overlap = False
            else:
                overlap = True
                print 'Overlap'
    rr[i] = [x,y,z]
    with open( filename, 'a' ) as data:
        data.write('\n%s %s %s %s' % (particle, x, y, z))
    # Create random particle direction
    x_dir = rnd.random() - 0.5
    y_dir = rnd.random() - 0.5
    z_dir = rnd.random() - 0.5
    v_dir_rand = np.sqrt(x_dir**2 + y_dir**2 + z_dir**2)
    vr[i][0] = x_dir * v_avg / v_dir_rand
    vr[i][1] = y_dir * v_avg / v_dir_rand
    vr[i][2] = z_dir * v_avg / v_dir_rand

print 'Particles set up.'

PE = 0.0

for i in range(0,n-1):
    ## We must first calculate the forces currently between all the particles as well as
    ## current velocities
    dr = rr[i] - rr[i+1:n]
    dr = dr - L * np.around(dr/L)
    xyz2 = dr**2
    r2 = np.sum( xyz2, axis = 1 )
    effective = r2 <= cutoff2
    PE += 4 * np.sum(((1/r2[effective])**6 - (1/r2[effective])**3))
    f = 24*(2*(1/r2[effective])**6 - (1/r2[effective])**3)
    f_tot = ((f * dr[effective].T) / r2[effective]).T
    fr[i] = fr[i] + np.sum( f_tot, axis = 0 )
    effective_real = np.append(np.zeros((i+1),dtype = bool), effective)
    fr[effective_real] = fr[effective_real] - f_tot

print "Particles initial speed created."

KE_array[0] = 0.5 * m * np.sum(vr**2)
PE_array[0] = PE
TE_array[0] = KE_array[0] + PE_array[0]
p_center_array[0] = np.sum(vr,axis=0)

print "Simulation beginning"
for step in range (0,timesteps):
    # We now run the simulation
    vr = vr + 0.5 * fr * dt
    rr = rr + vr * dt

    PE = 0.0
    fr = np.zeros((n,3))
    for i in range(0,n-1):
        #Calculate the force on each particle
        dr = rr[i] - rr[i+1:n]
        dr = dr - L * np.around(dr/L)
        xyz2 = dr**2
        r2 = np.sum( xyz2, axis = 1 )
        effective = r2 <= cutoff2
        PE += 4 * np.sum(((1/r2[effective])**6 - (1/r2[effective])**3))
        f = 24*(2*(1/r2[effective])**6 - (1/r2[effective])**3)
        f_tot = ((f * dr[effective].T) / r2[effective]).T
        fr[i] = fr[i] + np.sum( f_tot, axis = 0 )
        effective_real = np.append(np.zeros((i+1),dtype = bool), effective)
        fr[effective_real] = fr[effective_real] - f_tot

    vr = vr + 0.5 * fr * dt

    vr2 = np.sum(np.sum(vr**2,axis=1))
    KE_array[step+1] = 0.5 * m * vr2
    PE_array[step+1] = PE
    TE_array[step+1] = KE_array[step+1] + PE_array[step+1]
    p_center_array[step+1] = np.sum(vr,axis=0)

    exportxyz = rr - L*np.floor(rr/L)
    with open( filename, 'a' ) as data:
        data.write( '\n%d\n' % n )
        for j in range(0,n):
          data.write('\n%s %s %s %s' % (particle, exportxyz[j][0], exportxyz[j][1], exportxyz[j][2]))

    if step%200 == 0:
        print "Frame: ", step

T_array = (KE_array * 2) / (3 * n)

np.savetxt('KE Array',KE_array)
np.savetxt('PE Array',PE_array)
np.savetxt('TE Array',TE_array)
np.savetxt('p Center Array' ,p_center_array)
np.savetxt('T Array',T_array)
