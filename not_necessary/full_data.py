import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from word_item_frequency import word_freq
from mention_frequency import mention_freq
from get_user_timeline import pull_timeline

"""
(1) will pull the max number of tweets twitter will allow
(2) will pull the most mentions and most used words
(3) will plot both most used words/mentions
"""

if __name__ == '__main__':
	user = sys.argv[1]
	file_name = pull_timeline(user)
	most_mentions = pd.DataFrame(mention_freq(file_name))
	top_words = pd.DataFrame(word_freq(file_name))

	fig = plt.figure(figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
	fig = fig.suptitle(("Tweets by {}".format(user)), fontsize=30,
					color='r')
	plt.subplot(2, 1, 1)
	plt.barh(most_mentions[0], most_mentions[1])
	plt.title("Who {} mentioned the most".format(user), fontsize=15)

	plt.subplot(2, 1, 2)
	plt.barh(top_words[0], top_words[1])
	plt.title("What {} says the most".format(user), fontsize=15)
	
	plt.show()