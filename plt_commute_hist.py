#imports MTA subway data, then produces a matplotlib bar chart restricted to between 20 and 50 minutes, with 6 bins in total.
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

commutes = np.genfromtxt('commutes.csv', delimiter=',')


plt.hist(commutes, bins=6, range=(20,50))
plt.show()