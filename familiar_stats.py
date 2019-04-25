#codecademy project to compare the benefits of 2 products from a health company using ttests and chi squared.


import familiar as fam
from scipy import stats
from scipy.stats import ttest_ind 
from scipy.stats import chi2_contingency

#pre-formed datasets from codecademy.

vein_pack_lifespans = fam.lifespans(package='vein')
artery_pack_lifespans = fam.lifespans(package='artery')
iron_contingency_table = fam.iron_counts_for_package()

tsamp, pval = stats.ttest_1samp(vein_pack_lifespans, 71.0)

#this found the pval meant, in fact, 'proven to make you live longer'
if pval < 0.05:
  print('The Vein Pack Is Proven To Make You Live Longer!')
elif pval > 0.05:
    print('The Vein Pack Is Probably Good For You Somehow!')
    



package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

if package_comparison_results.pvalue < 0.05:
  print('the Artery Package guarantees even stronger results!')
elif package_comparison_results.pvalue > 0.05:
  print('the Artery Package is also a great product!')

#lazy, yes, but since we're not using the other variables created by chi_2...

a, iron_pvalue, b, c = chi2_contingency(iron_contingency_table)

if iron_pvalue < 0.05:
  print('The Artery Package Is Proven To Make You Healthier!')
else:
    print('While We Cant Say The Artery Package Will Help You, I Bet Its Nice!')