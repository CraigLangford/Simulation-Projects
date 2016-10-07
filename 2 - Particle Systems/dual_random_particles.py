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
iterations = 100
n_O = n_O_left = 256
n_N = n_N_left = 256
particles = ('O','N')
n = n_O + n_N
r_O = 6.6e-11
r_N = 7.1e-11
size = float(raw_input('Size of system:'))
filename = raw_input('Please input the desired filename:')
filename = filename + '.txt'

# Set up array and particle list
array = np.zeros((n,3))
particles_list = []
elapsedtimes = np.zeros(iterations)

for current in range(0,iterations):
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
                particle = 'N' #Nitrogen
            else:
                particle = 'O' #Oxygen
            particles_list.append(particle)
            if particles_list[i] == 'O':
                r_1= r_O
            else:
                r_1 = r_N
            x = rnd.random()*(size-r_1) + r_1/2
            y = rnd.random()*(size-r_1) + r_1/2
            z = rnd.random()*(size-r_1) + r_1/2
            for j in range(0,i):
                if particles_list[j] == 'O':
                    r_2 = r_O
                else:
                    r_2 = r_N
                while ((x-array[j][0])**2 + (y-array[j][1])**2 + (x-array[j][2])**2) < r_1 + r_2:
                    #This ensures the particles aren't overlapping by radius of the particles
                    x = rnd.random()*(size-r_1) + r_1/2
                    y = rnd.random()*(size-r_1) + r_1/2
                    z = rnd.random()*(size-r_1) + r_1/2
            data.write('\n%s %s %s %s' % (particle, x, y, z))
    elapsedtimes[current] = time.time() - t

mean = np.mean(elapsedtimes)
min = np.min(elapsedtimes)
max = np.max(elapsedtimes)

print 'Mean = %s \n Min = %s \n Max = %s' % (mean, min, max)
