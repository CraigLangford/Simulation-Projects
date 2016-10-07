'''
Craig Langford

This is a basic file reader to withdraw xyz particle information from a xyz.txt
file.
'''

import numpy as np

filename = raw_input('Please input the filename:')
filename = filename + '.txt'

f = open( filename )
lines = f.readlines()
n = len(lines)

molecules = []
xyz_vals = np.zeros((n-2,3))

for line in range(2,n):
    seperate = lines[line].split()
    molecules.append(seperate[0])
    xyz_vals[line-2][0]=float(seperate[1])
    xyz_vals[line-2][1]=float(seperate[2])
    xyz_vals[line-2][2]=float(seperate[3])

for i in range(0, len(molecules)):
    print "Type:", molecules[i], " X:", xyz_vals[i][0], "Y:", xyz_vals[i][1], "Z:", xyz_vals[i][2] 
