# Laplace Equation
In this simulation the Laplace Equation is used to simulate two different phases. -1 represents phase A and +1 represents phase B. To calculate the amount of change in value at each point the five point stencil method is used, which incorporates the surrounding 4 points around a point. This is generalized by the Laplacian Equation below:

![Laplacian](https://wikimedia.org/api/rest_v1/media/math/render/svg/def5402aecaf6e3e613d9a879945cc851f3db3c2)

With this equation, the entire system will come to equilibrium. To simulate the phases staying separate the change is multiplied by a dampening variable kappa, as well as subtracted by other variables (based on literature). Therefore, by controlling these variables a "High T" system can be created where the different phases come together, or a "Low T" system can be created where phase separation occurs.

## High T - No Phase Separation
![High T](https://github.com/CraigLangford/Simulation-Projects/blob/master/4%20-%20Laplace/HighT.gif)

## Low T - Phase Separation
![Low T](https://github.com/CraigLangford/Simulation-Projects/blob/master/4%20-%20Laplace/LowT.gif)
