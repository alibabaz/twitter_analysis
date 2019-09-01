import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from get_user_timeline import pull_timeline
from hashtag_stats import extract_counts, calc_tweets_with_hashtags
from hashtag_stats import get_hashtags, calc_tweets_without_hashtags
from hashtag_stats import total_tweets
import random
"""
(1) will pull the max number of tweets twitter will allow for 4 ppl
(2) pull the percentage of tweets with hashtags
(3) will plot both most used words/mentions
"""


def random_generator(number):
	numberz = []
	x = 0
	while(x == 0):
		numberz = random.sample(range(number), number)
		x = numberz[0]
	return numberz

if __name__ == '__main__':
	#user = sys.argv[1]
	#file_name = pull_timeline(user)
	file_name = sys.argv[1]
	hashtag_count = extract_counts(file_name)
	counter = []
	random_indexes = random_generator(len(hashtag_count))
	for i in random_indexes:
		counter.append([i, hashtag_count[i]])
	labels = pd.DataFrame(counter)[0]
	values = pd.DataFrame(counter)[1]

	fig1, ax1 = plt.subplots()
	ax1.pie(x=values, labels=None, autopct='%1.1f%%', labeldistance=1.01, 
						shadow=True, startangle=50)
	centre_circle = plt.Circle((0,0),0.70, fc='white')
	fig = plt.gcf()
	fig.gca().add_artist(centre_circle)
	ax1.axis('equal')
	plt.legend(labels)
	plt.title("How often does X use hashtags?")
	plt.tight_layout() 
	plt.show()