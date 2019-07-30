import sys
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweet_content import text_extract
from extract_tweet_content import pull_sentiment_polar_subjective

"""
	Scatter plots of 4 candidates showing
		 sentiment of all retrievable tweets
"""

def plot_with_axes(row, column, subjectivity, polarity, color):
	ax[row, column].scatter(subjectivity, polarity, s=15, alpha=0.3,
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
	color = ['red', 'green', 'blue', 'purple']
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		cand.append(candidates[user_name])
		file_name = handle_dict[user_name]
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)

		coordinates = axis_coord[x - 1]
		plot_with_axes(coordinates[0], coordinates[1], subjectivity, polarity, color[x-1])
	

	fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97,
					bottom=0.06)
	fig.suptitle('Sentiment Analysis of:\n{} vs {} vs {} vs {}'.format(cand[0],
		cand[1], cand[2], cand[3], fontsize=16, fontweight="heavy"))
	plt.show()