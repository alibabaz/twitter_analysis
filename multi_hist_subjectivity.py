import sys
import matplotlib.pyplot as plt
#import seaborn; seaborn.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweet_content import text_extract
from extract_tweet_content import pull_sentiment_polar_subjective

def plot_hist_axes(row, column, subjectivity, user_name, x):
	colors = ['green', 'red', 'blue', 'orange']
	ax[row, column].hist(subjectivity, alpha=0.3, bins=40, color=colors[x])
	ax[row,column].set_title("{}".format(candidates[user_name]), fontsize= 14, 
							fontweight='heavy', color=colors[x])
	ax[row,column].set_xlabel("How Subjective?", fontsize=6, 
							fontweight='heavy', labelpad=0)
	ax[row,column].set_ylabel("Number of Tweets", fontsize=6, fontweight='heavy',
										labelpad=0)
	ax[row,column].tick_params(labelsize=6, pad=0)

if __name__ == "__main__":
	fig, ax = plt.subplots(2, 2, figsize=(12,7))

	axis_coord = [[0,0], [0,1], [1,0], [1,1]]

	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		file_name = handle_dict[user_name]
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)
		
		coordinates = axis_coord[x - 1]
		plot_hist_axes(coordinates[0], coordinates[1], subjectivity, 
				user_name, x-1)

	fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97,
					bottom=0.06)
	fig.suptitle('Subjectivity Analysis!', fontsize=20, fontweight="heavy")
	plt.show()