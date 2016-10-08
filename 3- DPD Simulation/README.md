# Dissipative Particle Dynamics (DPD)
In a DPD system the forces between each particle are calculated and the resulting velocity is then calculated. With each frame the position of the particles are updated. For simplification, if the particle is within the radius distance (<2R) of the other repulsion is created with a linear dependance and the particles are attracted if they're further than 2R. Finally, a continuous boundary is used in which a particle exiting one side of the system will appear in the opposing face.

## DPD Simulation
![DPD Simulation](https://github.com/CraigLangford/Simulation-Projects/blob/master/3-%20DPD%20Simulation/Simulation.gif)

