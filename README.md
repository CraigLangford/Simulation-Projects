# Simulation Projects
These projects focus on utilizing different methods to simulate nanoenvironments. The READMEs in each folder further details the methods used. This includes some initial projects exploring various methods to generate random numbers, which is a powerful tool for the Monte-Carlo method as well as methods to create well dispersed particle systems. 

## Reading xyz files
From many of the simulations xyz files are produced. These can be visualized utilizing VMD or PyMOL, however, GIFs are included in the READMEs showing the resulting simulations.

# Random Number Generators
These projects focus on creating random numbers. This includes the linear congruential generator and the Fabonacci generator. 

## Linear Congruential Generator
A LCG is a random number generator that multiplies a previous value, adds to it and divides by a modulus (creating the range). This can be shown by the following equation:

![Linear Congruential Generator](https://wikimedia.org/api/rest_v1/media/math/render/svg/70a1708a4432a26fa32571271104f9caabdefc1c)

The randomness is highly dependent upon the choice of values for the generator. As seen in the image below which is the random value vs the previous value there can be seen to be a noticeable pattern with the red points representing a poor seed choice. Choosing a good seed choice as demonstrated by the green points will show little relationship between a point and the previous random number.

![Poor Seed Choice vs Good Seed Choice](https://github.com/CraigLangford/Simulation-Projects/blob/master/1%20-%20Random%20Number%20Generators/LCG%20Seed%20Comparison.png)

## Fibonacci Generator
A FB is similar to the Fibonacci Sequence in which the value is based of the two previous sums. By dividing this by a modulus a pseudo random sequence can be created. The image below shows the resulting values vs previous values with a FB.

![Fibonacci Generator - Value vs previous value](https://github.com/CraigLangford/Simulation-Projects/blob/master/1%20-%20Random%20Number%20Generators/Fibonacci%20Generator.png)


# Particle Systems
These projects focused on generating various systems in the .xyz format which can be read utiling VMD or PyMOL. Below are the resulting images images of the structures in VMD.

## Crystal Structure
![Ordered Structure](https://github.com/CraigLangford/Simulation-Projects/blob/master/2%20-%20Particle%20Systems/crystal_structure.bmp)

## Random Particles
![Random Particles](https://github.com/CraigLangford/Simulation-Projects/blob/master/2%20-%20Particle%20Systems/ramdom_particles.bmp)

## Two Phase Random Particles
![Two Phase Random Particles](https://github.com/CraigLangford/Simulation-Projects/blob/master/2%20-%20Particle%20Systems/dual_ramdom_particles.bmp)


# Dissipative Particle Dynamics (DPD)
In a DPD system the forces between each particle are calculated and the resulting velocity is then calculated. With each frame the position of the particles are updated. For simplification, if the particle is within the radius distance (<2R) of the other repulsion is created with a linear dependance and the particles are attracted if they
