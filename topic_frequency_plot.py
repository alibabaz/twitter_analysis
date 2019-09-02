from handle_file_dict import handle_dict
from candidate_dictionary import candidates
import numpy as np
import sys
import matplotlib.pyplot as plt

from topic_frequency import (get_topics_totals,
							total_tweet_count,
							print_topic_stats,
							topics_list)

"""
import topic count fxns from topic_frequency

*created NEW plotting fxns for these

"""

def extract_stats(user_name, topics):
	total_tweets = total_tweet_count(user_name)
	total_topic_tweets = get_topics_totals(user_name, topics)
	#percentage_topic = total_topic_tweets / total_tweets

	print_topic_stats(user_name, topics, total_tweets, total_topic_tweets)

	return total_topic_tweets / total_tweets

def plot_stats(user_list, percentages, topics):
	plt.figure(figsize=(12, 7))
	plt.plot(user_list, percentages)
	plt.xlabel("Users")
	plt.ylabel("Percent of Tweets")
	plt.title("While talking about: \n{}".format(topics))
	plt.show()


if __name__ == "__main__":
	topics = topics_list() #extract what topics to condsider
	user_list, percentages = [], []
	
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		user_list.append(candidates[user_name])

		percentage_topic = extract_stats(user_name, topics)

		percentages.append(round( (percentage_topic * 100), 2))
		
		##SAME SO FAR

	plot_stats(user_list, percentages, topics)