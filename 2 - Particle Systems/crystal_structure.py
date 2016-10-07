'''
Craig Langford

This function creates a xyz text file containing a single frame of a crystal
structure. Utilizing VMD/PyMol the structure can easily be seen.
'''

import numpy as np

#Create x, y, z, d and L values
print 'Please input the number of atoms in each direction.'
x = int(raw_input('x-direction:'))
y = int(raw_input('y-direction:'))
z = int(raw_input('z-direction:'))
L = float(raw_input('distance between atoms:'))
d = float(raw_input('diameter of atoms:'))
filename = raw_input('Please input the desired filename:')
filename = filename + '.txt'


#Create file to save in

f = open( filename, 'w' )

if L >= d:
    #Put data into file
    with open( filename, 'a' ) as data:
        data.write( '%d \nDistance between atoms = %d' % (x*y*z, L) )
        for i in range(0, x) :
            for j in range(0,y):
                for k in range(0,z):
                    data.write('\nO %d %d %d' % (i*L , j*L, k*L))
    print "XYZ file '%s' has been created in the same folder as this program." % filename
    print "Please use VMD or PyMol to visualize the file."
else:
    print 'Atoms are overlapping. Please make sure that the linear length is larger than d.'
