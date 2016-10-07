'''
Craig Langford

This script performs a Monte-Carlo simulation. In this a particle system is
randomly created after which particles are moved one-by-one and the energy
of the system is checked to see if it decreases or increases (PECalculator).
If the energy goes down the change is allowed, however, if it is not allowed,
a probability is applied which may mean it may be allowed anyway. This randomness
allows the system to overcome local minima, and likely find the global minimum.
'''

import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import time

def PECalculator(rr, n, L):
    PE = 0.0
    for i in range(0,n-1):
        dr = rr[i] - rr[i+1:n]
        dr = dr - L * np.around(dr/L)
        xyz2 = dr*dr
        r2 = np.sum( xyz2, axis = 1 )
        effective = r2 <= cutoff2
        r6 = r2[effective]*r2[effective]*r2[effective]
        PE += 4 * np.sum(1/(r6*r6) - 1/r6)
    return PE

def MonteCarlo(n,rr,r_rand,L,beta,cutoff2):
    accepted = False
    particle = rnd.randint(0,n-1)
    PEi = PECalculator(rr, n, L)
    # Change particle position
    theta = 2* np.pi * rnd.random()
    phi = 2* np.pi * rnd.random()
    x = r * np.cos(theta)
    y = r * np.sin(phi)
    z = r * np.sin(theta)
    rnew = np.zeros((n,3))
    rnew[:,:] = rr[:,:]
    rnew[particle] = rnew[particle] + np.array([x,y,z])
    # Calculate PEj
    PEj = PECalculator(rnew, n, L)
    # Calculate dPE
    dPE = PEj - PEi
    # If dPE >= 0 particle position is replaced and go to next particle
    if dPE <= 0:
        rr = rnew
        accepted = True
        PE = PEj
    # If dPE > 0 computer w = exp(-beta*dPE)
    else:
        w = np.exp( - beta * dPE )
        # Generate uniform random number in range 0 to 1 called r
        randnum = rnd.random()
        # If r <= w particle position is replaced and next particle
        if randnum <= w:
            rr = rnew
            accepted = True
            PE = PEj
        else:
            PE = PEi
    return rr, PE, accepted

def WriteFunction(rr,L,n):
    exportxyz = rr - L*np.floor(rr/L)
    exportarray = np.append(particles, np.asarray(exportxyz, dtype=np.dtype((str,13))) , axis = 1)
    with open( filename, 'a' ) as data:
        data.write( '%d\n\n' % n )
        np.savetxt(data,exportarray, fmt ='%s %s %s %s')

# Default values
filename = 'Monte-Carlo.xyz'
particle = 'O'
n = 300
p = 0.4
m = 1
dt = 0.01
T = 1
d = 1.
beta = 1
acceptance_num = 10
r_rand = 1
upval = 1.1
timesteps = 10000
looptime = 0.0
writetime = 0.0
cutoff = 2.5
# Calculated values
r = d/2
V_tot = n/p # We know p = 0.4/unit^3 therefore total volume = n_particles/p
L = V_tot**(1./3)
particles =  np.empty((n,1),dtype=str)
for i in range(0,n):
    particles[i] = 'O'
cutoff2 = cutoff**2
rr = np.zeros((n,3))
PE_array =  np.zeros((timesteps))
accepted_array =  np.zeros((timesteps),dtype=bool)

f = open( filename, 'w' )
with open( filename, 'a' ) as data:
    data.write( '%s \nMonte Carlo Simulation\n' % n )
    for i in range(0,n):

        overlap = True
        olcounter = 0
        while overlap == True:
            x = rnd.random()*(L)
            y = rnd.random()*(L)
            z = rnd.random()*(L)
            if i == 0:
                overlap = False
            dxyz = np.zeros((n,3))
            dxyz = [x,y,z] - rr[0:i]
            dxyz = dxyz - L * np.around(dxyz/L)
            overlappers = np.sum(dxyz*dxyz, axis = 1) < d*d
            if np.sum(overlappers) == 0:
                overlap = False

        rr[i] = [x,y,z]
        data.write('%s %s %s %s\n' % (particle, x, y, z))

        # Create random particle direction
        x_dir = rnd.random() - 0.5
        y_dir = rnd.random() - 0.5
        z_dir = rnd.random() - 0.5
print 'Particles set up.'
t = time.time()
for step in range (0,timesteps):
    ratio = 0.0
    rr, PE, accepted = MonteCarlo(n,rr,r_rand,L,beta,cutoff2)
    PE_array[step] = PE
    accepted_array[step] = accepted
    if step < acceptance_num:
        ratio = np.sum(accepted_array[0:step])/(step+1)
    else:
        ratio = np.sum(accepted_array[step-acceptance_num:step])/acceptance_num

    if ratio > 0.5:
        r_rand = r_rand * upval
    else:
        r_rand = r_rand / upval
    WriteFunction(rr,L,n)
    if step%10 == 0:
        print "Timestep",step
print "Total calculation time:", time.time() - t
p1, = plt.plot(PE_array, 'go')
plt.xlabel("Iterations")
plt.ylabel("Potential Energy")
plt.title("Potential Energy vs Iterations")
plt.show()
