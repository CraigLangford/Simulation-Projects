'''
Craig Langford

This script creates a grid of points with random temperature. It then proceeds
to utilize the Laplace equation to simulate the temperature changing in each
point through each iterations. Negative and positive values are created as two
different phases. At lower temperatures the two phases stay separate, where they
mix at higher temperatures. Finally an output video is created utilizing
ffmpeg.

NOTE: FFMPEG is needed to be installed and in Window's environmental variables
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def FivePoint(Phi, h, kappa, a, b, height, width, dt):
    phiXminusH = np.roll(Phi, 1, axis = 1)
    phiXplusH  = np.roll(Phi, -1, axis = 1)
    phiYminusH = np.roll(Phi, 1, axis = 0)
    phiYplusH  = np.roll(Phi, -1, axis = 0)
    del2 = (phiXminusH + phiXplusH + phiYminusH + phiYplusH - 4*Phi ) / (h * h)
    Phi3 = Phi * Phi * Phi
    dPhidt = kappa * del2 - a * Phi - b * Phi3
    PhiNew = Phi + dPhidt * dt
    return PhiNew

# VARIABLES
# Number of iterations
nIterations = 120
# Size of array
height = 128
width  = 128
# Distance between points
h = 1
# Values for equation
kappa = 1
a = -1
b = 1
dt = 0.05
# Create matrix
Phi = np.random.rand(height,width) * 2 - 1
fig = plt.figure()
# Where to save the matrices
allPhis = []
allPhis.append((plt.pcolor(Phi, norm=plt.Normalize(-1, 1)),))
X = np.arange(0,width*h+h,h)
Y = np.arange(0,height*h+h,h)
for i in range(1,nIterations+1):
    Phi = FivePoint(Phi, h, kappa, a, b, height, width, dt)
    allPhis.append((plt.pcolor(X, Y, Phi, norm=plt.Normalize(-1, 1)),))
    #allPhis.append((plt.pcolor(X, Y, Phi, norm=plt.Normalize(np.min(Phi), np.max(Phi))),))
    if i%10 == 0:
        print "Frame:",i

# Output video using ffmpeg
plt.axis([0,width*h,0,height*h])
plt.colorbar()
animatedPhi = animation.ArtistAnimation(fig, allPhis, interval = 50, repeat_delay=1000,
    blit=True)
animatedPhi.save('High T.mp4', fps = 6)
plt.show()
