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
In a DPD system the forces between each particle are calculated and the resulting velocity is then calculated. With each frame the position of the particles are updated. For simplification, if the particle is within the radius distance (<2R) of the other repulsion is created with a linear dependance and the particles are attracted if theyre further than 2R. Finally, a continuous boundary is used in which a particle exiting one side of the system will appear in the opposing face.

## DPD Simulation
![DPD Simulation](https://github.com/CraigLangford/Simulation-Projects/blob/master/3-%20DPD%20Simulation/Simulation.gif)

# Laplace Equation
In this simulation the Laplace Equation is used to simulate two different phases. -1 represents phase A and +1 represents phase B. To calculate the amount of change in value at each point the five point stencil method is used, which incorporates the surrounding 4 points around a point. This is generalized by the Laplacian Equation below:

![Laplacian](https://wikimedia.org/api/rest_v1/media/math/render/svg/def5402aecaf6e3e613d9a879945cc851f3db3c2)

With this equation, the entire system will come to equilibrium. To simulate the phases staying separate the change is multiplied by a dampening variable kappa, as well as subtracted by other variables (based on literature). Therefore, by controlling these variables a "High T" system can be created where the different phases come together, or a "Low T" system can be created where phase separation occurs.

## High T - Phases Join
![High T](https://github.com/CraigLangford/Simulation-Projects/blob/master/4%20-%20Laplace/Phases%20Joining.gif)

## Low T - Phases Separate
![Low T](https://github.com/CraigLangford/Simulation-Projects/blob/master/4%20-%20Laplace/Phases%20Separating.gif)


# Monte-Carlo Simulation
In a Monte-Carlo simulation the lowest energy of the system is found. By moving around particles individually one at a time and checking the resulting energy a local minimum can be found. Unfortunately, this local minimum may not be the global minimum. Therefore, in the Monte-Carlo simulation, there is a probability that a moved particle that creates a higher energy system stays in its new position. In this simulation the probability is calculated according to the equation:

![Probability a Particle Stays in Higher Energy Position](https://github.com/CraigLangford/Simulation-Projects/blob/master/5%20-%20Monte%20Carlo%20Simulation/Probability.png)

Where it can be seen that the higher the energy change, the lower the probability the particle will stay in the new higher energy position. The resulting simulation is as follows.

## Monte-Carlo Simulation
![Monte-Carlo Simulation](https://github.com/CraigLangford/Simulation-Projects/blob/master/5%20-%20Monte%20Carlo%20Simulation/Monte-Carlo%20Simulation.gif)

And finally the energy of the system can be seen to increase as found below. Take note on how the local minima are overcome and a global minimum is found.

![Energy of System](https://github.com/CraigLangford/Simulation-Projects/blob/master/5%20-%20Monte%20Carlo%20Simulation/Energ%20vs%20Time.png)


# Two Phase DPD Project
In this project a much more complex DPD system was created utilizing two types of particles. In this method particles were attracted to themselves more than their opposing type. As a result the like particles should clump. As seen below it is difficult to tell whether the particles are clumping.

![All](https://github.com/CraigLangford/Simulation-Projects/blob/master/6%20-%20Final%20Complex%20DPD%20Project/All.gif)

However, by only visualizing one type of particle, it is very easy to see the grouping of the particles to create small pockets in the system.

![Just Particles A](https://github.com/CraigLangford/Simulation-Projects/blob/master/6%20-%20Final%20Complex%20DPD%20Project/JustA.gif)
