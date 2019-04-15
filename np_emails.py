#a/b testing chance of opening emails with numpy's random number generator.

import numpy as np

#creates a random data set with 500 emails, with 5% being opened, and a sample size of 10,000
emails = np.random.binomial(500, 0.05, size=10000)

#calculates the chance of 0 emails being opened.
no_emails = np.mean(emails == 0)

#calculates the chance of 8 emails being opened

b_test_emails = np.mean(emails == 8)

print(no_emails, b_test_emails)