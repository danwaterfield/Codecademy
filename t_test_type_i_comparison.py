#this lesson demonstrated the dangers of multiple t-tests. Comparing sales data from 3 stores (a, b, c)  for significance, it calculated the means and std then 
#compared this to a 2-sample t-test between each pair of location data. While two t-tests created the probability of a false positive (type I) error of 10%
#3 t tests meant the chance of a false positive rose to 0.1426



from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")


a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)

a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)

tstatistic, a_b_pval = ttest_ind(a, b)
tstatistic, a_c_pval = ttest_ind(a, c)
tstatistic, b_c_pval = ttest_ind(b, c)

error_prob = 1-0.95**3

print error_prob