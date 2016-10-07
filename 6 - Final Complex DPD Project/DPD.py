'''
Craig Langford

This script has two main steps:
    1. Load system of particles with initial positions.
    2. Simulates the particles interactions and measures the kinetic
       energy during this process.
'''

import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import time

def DPDForce(particles, fr, rr, vr, L, alphaSame, alphaDifferent, gamma, sigma, sqrtdt, cutoff2, n):
    '''
    This function calculates the forces between the particles. It takes into
    account that particles A and B have different forces between eachother and
    themselves.
    '''

    for i in range(0,n-1):
        remainingParticles = particles[i+1:n]
        dr = rr[i] - rr[i+1:n]
        dv = vr[i] - vr[i+1:n]
        dr = dr - L * np.around(dr/L)
        xyz2 = dr*dr
        r2 = np.sum( xyz2, axis = 1 )
        effective = r2 <= cutoff2
        if np.sum(effective) > 0:
            effective_real = np.append(np.zeros((i+1),dtype = bool), effective)
            same = remainingParticles[effective] == particles[i] #Determine same particles
            same = np.reshape(same, np.sum(effective))
            different = remainingParticles[effective] != particles[i] #Determine different particles
            different = np.reshape(different, np.sum(effective))
            drradial = np.sqrt(r2[effective])
            dreffective = dr[effective]
            #Calculate forces
            fC = np.zeros((np.sum(effective),3))
            fC[0:np.sum(same)] = alphaSame * (( 1 - drradial[same]) * dreffective[same].T).T
            fC[np.sum(same):np.sum(effective)] = alphaDifferent * (( 1 - drradial[different]) * dreffective[different].T).T
            weightR = 1 - drradial
            weightD = weightR * weightR
            fD = - gamma * ( (weightD * drradial * np.sum( (dv[effective]*dr[effective]) ,axis = 1)) * dr[effective].T ).T
            randvals = np.random.randn(np.sum(effective),3)
            fR = sigma * (weightR * randvals.T * dr[effective].T).T / sqrtdt
            f_tot = fC + fD + fR
            fr[i] = fr[i] + np.sum( f_tot, axis = 0 )
            fr[effective_real] = fr[effective_real] - f_tot
    return fr


def WriteFunction(rr,L,n):
    '''
    This function writes the new positions to the file.
    '''
    exportxyz = rr - L*np.floor(rr/L)
    exportarray = np.append(particles, np.asarray(exportxyz, dtype=np.dtype((str,13))) , axis = 1)
    with open( filename, 'a' ) as data:
        data.write( '%d\n\n' % n )
        np.savetxt(data,exportarray, fmt ='%s %s %s %s')


# Default values
filename = 'dual_random_particles.xyz'
nmonomers = 1
n_A = 500
n_B = 4500
n = n_A + n_B
p = 3.0
m = 1
dt = 0.01
kbT = 1
d = 1.
cutoff = 1
lmbda = 0.5
timesteps = 1000
alphaSame = 25
alphaDifferent = 100
sigma = 3


# Other values and arrays

gamma = sigma * sigma / ( 2 * kbT )
sqrtdt = np.sqrt(dt)
looptime = 0.0
vvtime = 0.0
vvtimes = np.zeros((12))
writetime = 0.0
r = d/2
V_tot = n/p # We know p = 0.4/unit^3 therefore total volume = n_particles/p
L = V_tot**(1./3)
particles =  np.empty((n,1),dtype=str)
for i in range(0,n_A):
    particles[i] = 'A'
for i in range(n_A, n_A+n_B):
    particles[i] = 'B'
cutoff2 = cutoff*cutoff
rr = np.zeros((n,3))
vr = np.zeros((n,3))
fr = np.zeros((n,3))
v_avg = np.sqrt(3 * kbT / m)
kbT_array =  np.zeros((timesteps + 1))
C_array = np.zeros((timesteps + 1))

f = open( filename, 'w' )
with open( filename, 'a' ) as data:
    data.write( '%s \nParticles using DPD simulations\n' % n )
    for i in range(0,n):

        x = rnd.random() * L
        y = rnd.random() * L
        z = rnd.random() * L

        rr[i] = [x,y,z]
        data.write('%s %s %s %s\n' % (' '.join(map(str, particles[i])), x, y, z))

        # Create random particle direction
        theta = 2* np.pi * rnd.random()
        phi = 2* np.pi * rnd.random()
        vr[i][0] = v_avg * np.sin(theta) * np.cos(phi)
        vr[i][1] = v_avg * np.sin(theta) * np.sin(phi)
        vr[i][2] = v_avg * np.sin(phi)

print 'Particles set up.'
print 'Direction of mass: x =', np.sum(vr[:,0], axis = 0), 'y =', np.sum(vr[:,1], axis = 0), 'z =', np.sum(vr[:,2], axis = 0)
print 'Standard Deviation of Mass: x =', np.std(vr[:,0], axis = 0), 'y =', np.std(vr[:,1], axis = 0), 'z =', np.std(vr[:,2], axis = 0)

PE = 0.0

fr = DPDForce(particles, fr, rr, vr, L, alphaSame, alphaDifferent, gamma, sigma, sqrtdt, cutoff2, n)

vr2 = np.sum(np.sum(vr*vr,axis=1))
kbT_array[0] = vr2 / ( 3 * n )

t = time.time()
hitZero = False
numberAtZero = 0

for step in range (0,timesteps):

    rr = rr + dt * vr + 0.5 * dt * dt * fr #Step 1
    vr = vr + lmbda * dt * fr #Step 2

    frold = fr

    fr = np.zeros((n,3))

    fr = DPDForce(particles, fr, rr, vr, L, alphaSame, alphaDifferent, gamma,  sigma, sqrtdt, cutoff2, n) #Step 3

    vr = vr + 0.5 * dt * ( frold + fr) #Step 4

    vr2 = np.sum(np.sum(vr*vr,axis=1))
    kbT_array[step+1] = vr2 / ( 3 * n )

    WriteFunction(rr,L,n)

    if step%25 == 0:
        print "Timestep",step

print "Total force calculation time:", time.time() - t

p1, = plt.plot(kbT_array, 'ro')
# p2, = plt.plot(C_array, 'go')
plt.xlabel("Iterations")
plt.ylabel("k_B T")
plt.title("k_B T vs Iterations")
#plt.legend([p1,p2], ["KE", "PE"])

plt.savefig('500A 4500B alpha100')
#np.save('C:/Users/Craig Langford/Desktop/Saved Files/500A0B', C_array)
plt.show()
