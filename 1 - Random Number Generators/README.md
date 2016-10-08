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
