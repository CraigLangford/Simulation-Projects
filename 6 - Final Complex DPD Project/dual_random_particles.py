'''
Craig Langford

This function creates a xyz text file containing a single frame of two types of
particles randomly distributed. Utilizing VMD/PyMol the particles can be seen.
'''

import random as rnd
import numpy as np
import time
import matplotlib.pyplot as plt

#Create values
n_O = n_O_left = 500
n_N = n_N_left = 4500
particles = ('A','B')
n = n_O + n_N
d_O = 1
d_N = 1
size = 11.856311015
filename = raw_input('Please input the desired filename:')
filename = filename + '.xyz'

# Set up array and particle list
array = np.zeros((n,3))
particles_list = []
elapsedtimes = 0

t = time.time()
f = open( filename, 'w' )
with open( filename, 'a' ) as data:
    # Input information of system
    data.write( '%d \nSize of system = %d x %d x %d' % (n, size, size, size) )
    for i in range(0,n):
        #Create random particle color choice
        if n_O_left > 0 and n_N_left > 0:
            particle = rnd.choice(particles)
        elif n_O_left == 0:
            particle = 'A' #Particle A
        else:
            particle = 'B' #Particle B
        particles_list.append(particle)
        if particles_list[i] == 'O':
            d_1= d_O
        else:
            d_1 = d_N
        x = rnd.random()*(size-d_1) + d_1/2
        y = rnd.random()*(size-d_1) + d_1/2
        z = rnd.random()*(size-d_1) + d_1/2
        '''
        This simulation is fine with particles overlapping, this part isn't needed
        for j in range(0,i):
            if particles_list[j] == 'O':
                r_2 = r_O
            else:
                r_2 = r_N
            while ((x-array[j][0])**2 + (y-array[j][1])**2 + (x-array[j][2])**2) < r_1 + r_2:
                #This ensures the particles aren't overlapping by radius of the particles
                x = rnd.random()*(size-d_1) + d_1/2
                y = rnd.random()*(size-d_1) + d_1/2
                z = rnd.random()*(size-d_1) + d_1/2
        '''
        data.write('\n%s %s %s %s' % (particle, x, y, z))
        if i % 100 == 0:
            print "Particle: " , i
elapsedtimes = time.time() - t

mean = np.mean(elapsedtimes)
min = np.min(elapsedtimes)
max = np.max(elapsedtimes)

print 'Mean = %s \n Min = %s \n Max = %s' % (mean, min, max)
