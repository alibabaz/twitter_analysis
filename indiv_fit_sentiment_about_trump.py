import sys
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import full_tweet_sentiment
from extract_tweets_about_trump import extract_about_trump
from extract_tweets_full import extract_about_topic
import numpy as np
import os

"""Look at an individual persons shift of total tweets vs
	those about trump
***Hard coded axes - only two plots so it's fine-
		-->if more need to make it variable

"""

def plot_control(user_name, topic=None):
	#Second one only looks @ tweets featuring 'Trump'
	polarity, subjectivity = full_tweet_sentiment(user_name)
	extract_convert_plot(polarity, subjectivity, "All tweets", 'red')
	if topic:
		polarity, subjectivity = extract_about_topic(user_name, topic)
		extract_convert_plot(polarity, subjectivity, "Only '{}'".format(topic), 'blue')
	else:
		polarity, subjectivity = extract_about_trump(user_name)
		extract_convert_plot(polarity, subjectivity, "Only 'Trump'", 'blue')
	
	plot_axes(0, "Polarity")
	plot_axes(1, "Subjectivity")
	fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97, bottom=0.06)
	title = "Sentiment analysis\n Distribution with & without mentioning Trump"
	fig.suptitle(("{} ".format(candidates[user_name]) + title), 
		fontsize=20, fontweight="heavy")
	plt.show()

#if want to see w/o conversion - comment out conv & change params plot_fitted_dist
def extract_convert_plot(polarity, subjectivity, label, color):
	removed_zero_subj = convert_array(subjectivity)
	removed_zero_polar = convert_array(polarity)
	plot_fitted_dist(0, removed_zero_polar, label, color)
	plot_fitted_dist(1, removed_zero_subj, label, color)

def plot_fitted_dist(index, sentiment, label, color):
	sns.distplot(sentiment, label=label, 
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
	fig, ax = plt.subplots(2, 1, figsize=(12,7))
	user_name = sys.argv[1]
	print("We can provide a comparison of the users full tweets vs about a topic")
	print("You can see how they talk about Trump or another topic")
	print("Input 'Trump' if you want to see that - or provide another subject")
	query = input()
	if query == 'Trump':
		plot_control(user_name)
	else:
		plot_control(user_name, topic=query)
		

