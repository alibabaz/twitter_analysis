from handle_file_dict import handle_dict
from candidate_dictionary import candidates
import numpy as np
from extract_tweets_full import full_tweet_sentiment, text_extract
import sys

"""
Define a new topic extract function - so it doesn't need to double count

Seeing what proportion of tweets a topic is for user
May help identify where to look

ISSUE of RECOUNTING - for example, if using Guns and Gun - will get two counts
for the word "Guns" --> could resolve by ensuring to include the space after each
"""

def topics_list():
	topics = []
	print("What topic would you like to analyze? example: 'guns'")
	print("You may want to include different casings: 'Guns'")
	topics = input().split()
	while(True):
		print("\nAnything else?")
		print("input a single period if that's all you are interested in")
		topic = input()
		if(topic == '.'):
			break
		else:
			for item in topic.split(): 
				topics.append(item)
	return topics

def get_topics_totals(user_name, topics):
	file_name = handle_dict[user_name]
	full_tweet_texts = text_extract(file_name)
	found = []
	print(topics)
	for x in range(len(full_tweet_texts)):
		for topic in topics:
			if topic in full_tweet_texts[x]:
				found.append(full_tweet_texts[x])
				break
	return len(found)

def total_tweet_count(user_name):
	polarity, subjectivity = full_tweet_sentiment(user_name)
	return len(polarity)

def print_topic_stats(user_name, topics, total_tweets, total_topic_tweets):
		print("When considering {}:".format(user_name))
		print("Total # available tweets: {}".format(total_tweets))
		print("{} talks about {}:".format(user_name, topics))
		print("# tweets about is: {}".format(total_topic_tweets))
		fraction = total_topic_tweets / total_tweets
		print("representing {} % of what {} says".format((round(fraction*100, 2)), 
											user_name ))
		print("----------" * 5)

if __name__ == "__main__":
	topics = topic_list()
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		total_tweets = total_tweet_count(user_name)
		total_topic_tweets = get_topics_totals(user_name, topics)
		print_topic_stats(user_name, topics, total_tweets, total_topic_tweets)
