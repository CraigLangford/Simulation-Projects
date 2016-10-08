# Monte-Carlo Simulation
In a Monte-Carlo simulation the lowest energy of the system is found. By moving around particles individually one at a time and checking the resulting energy a local minimum can be found. Unfortunately, this local minimum may not be the global minimum. Therefore, in the Monte-Carlo simulation, there is a probability that a moved particle that creates a higher energy system stays in its new position. In this simulation the probability is calculated according to the equation:

![Probability a Particle Stays in Higher Energy Position](https://github.com/CraigLangford/Simulation-Projects/blob/master/5%20-%20Monte%20Carlo%20Simulation/Probability.png)

Where it can be seen that the higher the energy change, the lower the probability the particle will stay in the new higher energy position. The resulting simulation is as follows.

## Monte-Carlo Simulation
![Monte-Carlo Simulation](https://github.com/CraigLangford/Simulation-Projects/blob/master/5%20-%20Monte%20Carlo%20Simulation/Monte-Carlo%20Simulation.gif)

And finally the energy of the system can be seen to increase as found below. Take note on how the local minima are overcome and a global minimum is found.

![Energy of System](https://github.com/CraigLangford/Simulation-Projects/blob/master/5%20-%20Monte%20Carlo%20Simulation/Energ%20vs%20Time.png)
