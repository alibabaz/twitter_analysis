import sys
import json
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from candidate_dictionary import candidates
from handle_file_dict import handle_dict
import numpy as np

def get_stats(tweet):
	favorite_count = tweet['favorite_count']
	retweet_count = tweet['retweet_count']
	follower_count = tweet['user']['followers_count']
	return favorite_count, retweet_count, follower_count

def tweet_stat_extract(file_name):
	with open(file_name, 'r') as f:
		favorites, retweets, followers = [], [], []
		for line in f:
			tweet = json.loads(line)
			favorite_count, retweet_count, followers_count = get_stats(tweet)
			favorites.append(favorite_count)
			retweets.append(retweet_count)
			followers.append(followers_count)
	return np.array(favorites), np.array(retweets), np.array(followers)

def plot_with_axes(row, column, subjectivity, polarity, color):
	ax[row, column].scatter(subjectivity, polarity, s=15, alpha=0.3,
						color=color)
	ax[row,column].set_title("{}".format(candidates[user_name]), fontsize= 10, 
							fontweight='heavy', color=color, pad=2)
	ax[row,column].set_xlabel("Favorites", fontsize=6, fontweight='heavy',
										labelpad=-2)
	ax[row,column].set_ylabel("Retweets", fontsize=6, fontweight='heavy',
										labelpad=0)
	ax[row,column].tick_params(labelsize=6, pad=-4)

if __name__ == '__main__':
	#fig, ax = plt.subplots(2, 2, figsize=(12,7))
	plt.figure(figsize=(12,7))
	cand = []
	axis_coord = [[0,0], [0,1], [1,0], [1,1]]
	color = ['red', 'green', 'blue', 'purple']
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		cand.append(candidates[user_name])
		file_name = handle_dict[user_name]
		tweet_stat_extract(file_name)
		favorites, retweets, followers = tweet_stat_extract(file_name)
		#plt.scatter(favorites,retweets, color=color[x-1], alpha=0.3, s=5,
		#	label=candidates[user_name], edgecolor=None)
		#coordinates = axis_coord[x - 1]
		#plot_with_axes(coordinates[0], coordinates[1], favorites, retweets, color[x-1])
	favorites = favorites[favorites == 0]
	print(len(favorites))
	#plt.legend()
	#plt.show()
	
	#fig.subplots_adjust(hspace=0.3, left=0.06, right=0.97,
	#				bottom=0.06)
	#fig.suptitle('Engagement Analysis of:\n{} vs {} vs {} vs {}'.format(cand[0],
	#	cand[1], cand[2], cand[3], fontsize=16, fontweight="heavy"))
	#plt.show()