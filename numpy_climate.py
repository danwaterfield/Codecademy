# this script was written for codecademy's numpy course. It took an array from csv of temperatures, then manipulated them

import numpy as np

#opens temperature_data with , delimiter
temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

#adds 3 to each value in temperatures, then ensures we've saved it as an array so as not to return a tuple later. It prints mon-fri rows, with 5 columns of reported data

temperatures_fixed = [i + 3 for i in temperatures]
temperatures_fixed = np.array(temperatures_fixed)

#returns temps from first row
monday_temperatures = temperatures_fixed[0,:]

thursday_friday_morning = temperatures_fixed[3:5,1]

# creates a new array of all temperatures lower than 50 or greater than 60.
t = temperatures_fixed
temperature_extremes = temperatures_fixed[(t < 50) | (t > 60)]