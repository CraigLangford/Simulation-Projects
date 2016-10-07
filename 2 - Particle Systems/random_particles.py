'''
Craig Langford

This function creates a xyz text file containing a single frame of particles
randomly distributed. Utilizing VMD/PyMol the structure can be seen.
'''

import random as rnd
import numpy as np
import time
import matplotlib.pyplot as plt

#Create values
iterations = 100;
n = 512 #Defined in question
d = 1.2*10**(-10)
size = float(raw_input('Size of system:'))
filename = raw_input('Please input the desired filename:')
filename = filename + '.txt'

array = np.zeros((n,3))
elapsedtimes = np.zeros(iterations)

for current in range(0,iterations):
    t = time.time()
    f = open( filename, 'w' )
    with open( filename, 'a' ) as data:
        data.write( '%d \nSize of system = %d x %d x %d' % (n, size, size, size) )
        for i in range(0,n):
            x = rnd.random()*(size-d) + d/2
            y = rnd.random()*(size-d) + d/2
            z = rnd.random()*(size-d) + d/2
            for j in range(0,i):
                while ((x-array[j][0])**2 + (y-array[j][1])**2 + (x-array[j][2])**2) < d:
                    x = rnd.random()*(size-d) + d/2
                    y = rnd.random()*(size-d) + d/2
                    z = rnd.random()*(size-d) + d/2
            data.write('\nO %d %d %d' % (x , y, z))
    elapsedtimes[current] = time.time() - t

mean = np.mean(elapsedtimes)
min = np.min(elapsedtimes)
max = np.max(elapsedtimes)

print 'Mean = %s seconds\n Min = %s seconds\n Max = %s seconds' % (mean, min, max)
