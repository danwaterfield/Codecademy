#codecademy course that calculates number of sunflowers that bloomed, and the probability of success. 


import codecademylib
import numpy as np
from matplotlib import pyplot as plt


#imports csv of data, assigns to sunflower
sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')


#calculates mean and standard deviation for use in the following...
sunflowers_mean = np.mean(sunflowers) 
sunflowers_std = np.std(sunflowers)

#...creates a random set of numbers from the two variables above, with a size of 5000, below we create a histogram which compares this with the observed data imported from the csv above

sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, 5000)


plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()

#creates a rival sample set with 200 plants, a 10 percent rate of failure, and a size of 5,000
experiments = np.random.binomial(200, 0.1, size=5000)


#finds chance that less than 20 sunflowers will bloom, then prints it.
prob = np.mean(experiments < 20)
print(prob)