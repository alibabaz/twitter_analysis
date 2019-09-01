import sys
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import full_tweet_sentiment
from extract_tweets_about_trump import extract_about_trump
import numpy as np

"""
	- See how three candidates stack up in the polarity & subjectivity 
		of what they say (by %) - 
	- Conversion fxn ('convert_array'): will remove all the ZERO
		values in the subjectivity & polarity of their tweets -> since 
		most tweets get classified in those bins, it makes it hard to see
		the variation, can disable by commenting out and changing the call
		to plot_fitted_dist
"""

def plot_control(user_names):
	#for some reason can't declare figure outside of main fxn
	#fig, ax = plt.subplots(2, 1, figsize=(12,7))

	colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']

	names = []
	for user_name in user_names:
		names.append(candidates[user_name])
		
		#Second one only looks @ tweets featuring 'Trump'
		#polarity, subjectivity = full_tweet_sentiment(user_name)
		polarity, subjectivity = extract_about_trump(user_name)

		removed_zero_subj = convert_array(subjectivity)
		removed_zero_polar = convert_array(polarity)
		
		plot_fitted_dist(0, removed_zero_polar, user_name, colors[x-1])
		plot_fitted_dist(1, removed_zero_subj, user_name, colors[x-1])

	plot_axes(0, "Polarity")
	plot_axes(1, "Subjectivity")
	fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97, bottom=0.06)
	fig.suptitle('Sentiment Distribution', fontsize=22, fontweight="heavy")
	plt.show()


def plot_fitted_dist(index, sentiment, user_name, color):
	sns.distplot(sentiment, label=candidates[user_name], 
							ax=ax[index], hist=False)
	ax[index].tick_params(labelsize=6, pad=-4)

def plot_axes(index, sentiment):
	ax[index].set_xlabel("{}".format(sentiment), fontsize=10, fontweight='heavy',
										labelpad=4)
	ax[index].set_ylabel("Distribution", fontsize=10, fontweight='heavy',
										labelpad=4)
	ax[index].legend()

#removing the ones classified as Zero since they wash out the rest
def convert_array(sentiment):
	array = np.array(sentiment)
	return array[array != 0]

if __name__ == "__main__":
	user_names = []
	for x in range(1, len(sys.argv)):
		user_names.append(sys.argv[x])
	
	fig, ax = plt.subplots(2, 1, figsize=(12,7))

	plot_control(user_names)


		