'''
Craig Langford

This function investigates the randomness utilizing the Fibonacci Generator.
The initial values can be seen to not be very random, however, the following values
appear to be random.
'''

import numpy
import matplotlib.pyplot as plt

n = 500
m = 2**31
x_0 = 15
x_1 = 12

def FG(m,x_0,x_1,n):
    '''
    This creates an array of xn and x_(n+1) utilizing the Fibonacci Generator
    function. x_n = x_(n-1) + x_(n-2) % m
    '''

    x_array = numpy.zeros([n,2])
    x_array[0][0] = x_0
    x_array[0][1] = x_array[1][0] = x_1
    x_array[1][1] = (x_0 + x_1) % m
    for i in range (2,n):
        x_array[i][0] = x_array[i-1][1]
        x_array[i][1] = (x_array[i-1][1] + x_array[i-1][0]) % m
    return x_array

rnd_vals = FG(m,x_0,x_1,n)

plt.plot(rnd_vals[:,0],rnd_vals[:,1], 'ro')
plt.xlabel("x_n")
plt.ylabel("x_(n+1)")
plt.title("Plot of x_n and x_(n+1) for %d iterations and x_0 and x_1 values of %d and %d" % (n, x_0, x_1))
plt.show()
