
#uses numpy to analyse results of a Mayoral voting survey (survey_responses) against real world results, creates different sample sizes to show that the greater the sample size, the more accurate the relationship to irl data

import codecademylib
import numpy as np
import matplotlib.pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']


# iterates over survey_responses and finds number of votes for ceballos (33)
total_ceballos = sum(1 for response in survey_responses if response == 'Ceballos')

#calculates survey length as a variable - 70 - designating it as a float.
survey_length = float(len(survey_responses)) # defining float here avoids having to do awkward / 70. later on.


#gives a percentage of ceballos votes. 47.14% , however, compares poorly to the 54% of actual votes
percentage_ceballos = total_ceballos / survey_length

#print(percentage_ceballos) 


#creates a random data set of 70 replies, a 54% target, and 10k iterations, then plots a graph with 20 bins in order to best show participants
possible_surveys = np.random.binomial(survey_length, .54, size=10000) / survey_length

#plt.hist(possible_surveys, range=(0,1), bins=20)
#plt.show()


possible_surveys_length = float(len(possible_surveys))

incorrect_predictions = len(possible_surveys[possible_surveys < .5])

ceballos_loss_surveys = incorrect_predictions / possible_surveys_length

#print(ceballos_loss_surveys) which gives a 20 percent chance of receiving a result which is outside the actual results. The code after this demonstrates that, surprise surprise
#a bigger sample size gives a more accurate result. Indeed, with 7000 replies the chance that ceballos' is predicted to receive < 50% = 0.0!

large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size=10000) / large_survey_length

plt.hist(large_survey, range=(0,1), alpha=0.5, bins=20)
plt.show()
incorrect_predictions_new = len(large_survey[large_survey < .5])
ceballos_loss_new = incorrect_predictions_new / large_survey_length

print(ceballos_loss_new)



