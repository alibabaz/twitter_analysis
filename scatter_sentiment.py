import sys
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import text_extract
from extract_tweets_full import pull_sentiment_polar_subjective
from extract_tweets_about_trump import extract_about_trump

"""
	Scatter plots of 4 candidates showing
		 sentiment of all retrievable tweets
	Trying to overlay tweets ab a topic over full tweets
	requires image to be blown up - use scatter_trump.py
	for individual analysis
"""

def plot_with_axes(row, column, subjectivity, polarity, color, label, alpha):
	ax[row, column].scatter(subjectivity, polarity, s=15, alpha=alpha,
						color=color)
	ax[row,column].set_title("{}".format(candidates[user_name]), fontsize= 10, 
							fontweight='heavy', color=color, pad=2)
	ax[row,column].set_xlabel("Subjectivity", fontsize=6, fontweight='heavy',
										labelpad=-2)
	ax[row,column].set_ylabel("Polarity", fontsize=6, fontweight='heavy',
										labelpad=0)
	ax[row,column].tick_params(labelsize=6, pad=-4)


if __name__ == "__main__":
	fig, ax = plt.subplots(2, 2, figsize=(12,7))
	cand = []
	axis_coord = [[0,0], [0,1], [1,0], [1,1]]
	color = ['red', 'green', 'blue', 'cyan', 'purple']
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		file_name = handle_dict[user_name]
		cand.append(candidates[user_name])
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)

		coordinates = axis_coord[x - 1]
		plot_with_axes(coordinates[0], coordinates[1], subjectivity, 
				polarity, color[x-1], label="All Tweets", alpha=0.2)
		
		#polarity, subjectivity = extract_about_trump(user_name)
		#plot_with_axes(coordinates[0], coordinates[1], subjectivity, 
		#				 polarity, color[x], label="Talking about Trump", alpha=0.3)
		#ax[coordinates[0], coordinates[1]].legend("All Tweets", "Trump")


	fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97,
					bottom=0.06)
	fig.suptitle('Sentiment Analysis of:\n{} vs {} vs {} vs {}'.format(cand[0],
		cand[1], cand[2], cand[3], fontsize=16, fontweight="heavy"))
	plt.show()