'''
Craig Langford

This function investigates the randomness utilizing different seed values for the
LCG. Patterns can easily be seen in the outgoing plot.

LCG is defined by X_(n+1) = (aX_n + c) (mod m)
'''

import numpy
import matplotlib.pyplot as plt

x_0 = 3;

def LCG(a,c,m,x_0,n):
    "This creates an array of xn and x_(n+1)"
    x_array = numpy.zeros([n,2])
    x_array[0][0] = x_0
    x_array[0][1] = (a*x_0 + c) % m
    for i in range (1,n):
        x_array[i][0] = x_array[i-1][1]
        x_array[i][1] = (a*x_array[i][0] + c) % m
    return x_array

x_array_1 = LCG(128,0,509,x_0,500);
x_array_2 = LCG(269,0,2048,x_0,500);

p1, = plt.plot(x_array_1[:,0],x_array_1[:,1], 'ro')
p2, = plt.plot(x_array_2[:,0],x_array_1[:,1], 'go')
plt.xlabel("x_n")
plt.ylabel("x_(n+1)")
plt.title("Plot of x_n and x_(n+1) for LCG(128,0,509) and LCG(269,0,2048) with x_0 values of %d" % x_0)
plt.legend([p1,p2], ["LCG(128,0,509)", "LCG(269,0,2048)"])

plt.show()
