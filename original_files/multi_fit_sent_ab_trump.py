import sys
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import full_tweet_sentiment
from extract_tweets_about_trump import extract_about_trump
import numpy as np

"""
Compare TWO candidates sentiment normally vs when talking about trump

Expansion of indiv_fit_sentiment_about_trump.py
**Really the big difference is with how the axis are called and invoked
	the current way of calling them uses an external variable(z) to pull
	the required indices
"""

def plot_control(user_name, coords_1, coords_2):
	#coords_1 --> polarity(top) &  coords_2 --> subjectivity (bottom)
	#sentiment of ALL tweets
	pol_all, subj_all = full_tweet_sentiment(user_name)
	extract_convert_plot(pol_all, coords_1, "All tweets", 'green')
	extract_convert_plot(subj_all, coords_2, "All tweets", 'green')

	#sentiment of only tweets mentioning trump
	pol_trump, subj_trump = extract_about_trump(user_name)
	extract_convert_plot(pol_trump, coords_1, "Only 'Trump'", 'blue')
	extract_convert_plot(subj_trump, coords_2, "Only 'Trump'", 'blue')

	plot_axes(coords_1, "Polarity", user_name)
	plot_axes(coords_2, "Subjectivity", user_name)
	fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97, bottom=0.06)

def extract_convert_plot(sentiment, coords, label, color):
	removed_zero_sentiment = convert_array(sentiment)
	plot_fitted_dist(coords, removed_zero_sentiment, label, color)

def plot_fitted_dist(coords, sentiment, label, color):
	one, two = coords[0], coords[1]
	sns.distplot(sentiment, label=label, color=color,
							ax=ax[one, two], hist=False)
	ax[one, two].tick_params(labelsize=6, pad=-4)

def plot_axes(coords, sentiment, user_name):
	one, two = coords[0], coords[1]
	ax[one, two].set_xlabel("{}".format(sentiment), fontsize=10, fontweight='heavy',
										labelpad=4)
	ax[one, two].set_ylabel("Distribution", fontsize=10, fontweight='heavy',
										labelpad=4)
	ax[one,two].set_title("{}".format(candidates[user_name]), fontsize=8,
							fontweight='heavy', pad=-1)
	ax[one, two].legend()

#removing the ones classified as Zero since they wash out the rest
def convert_array(sentiment):
	array = np.array(sentiment)
	return array[array != 0]

if __name__ == "__main__":
	fig, ax = plt.subplots(2, 2, figsize=(12,7))
	handle, z = [], 0
	axis_coord= [ [0,0], [1,0], [0,1], [1,1] ]
	
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		handle.append(user_name)
		plot_control(user_name, axis_coord[z], axis_coord[z + 1])
		z += 2

	title = "Sentiment Analysis\n Distribution with & without Mentioning Trump"
	fig.suptitle(("{} & {} ".format(candidates[handle[0]], 
							candidates[handle[1]]) + title), 
							fontsize=16, fontweight="heavy")
	plt.show()
