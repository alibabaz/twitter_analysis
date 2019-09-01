import sys
import json
from textblob import TextBlob
import pandas as pd
from candidate_dictionary import candidates
from handle_file_dict import handle_dict

""" extract tweet - go through and do a sentiment analysis on each tweet """

def get_text(tweet):
	text = tweet.get('full_text', [])
	return text

def text_extract(file_name):
	path = "/older_timelines/" + file_name
	with open(path, 'r') as f:
		tweet_text = []
		for line in f:
			tweet = json.loads(line)
			text = get_text(tweet)
			tweet_text.append(text)
	return tweet_text

def print_avg_polar_subjective(user_name, polarity, subjectivity):
	average_polarity = sum(polarity)/len(polarity)
	average_subjectivity = sum(subjectivity) / len(subjectivity)
	print("\nLooking at {}'s tweets:\n".format(candidates[user_name]))
	print("----average polarity is: {}".format(average_polarity))
	#print("----most polarizing tweet was: {}".format(min(polarity)))
	print("----average subjectivity is: {}".format(average_subjectivity))
	#print("----most subjective tweet was: {}".format(max(subjectivity)))
	print("____________________________________________________")

def describe_polar_subjective(polarity, subjectivity):
	polarity_frame = pd.Series(polarity)
	subjectivity_frame = pd.Series(subjectivity)
	print("The polarity figures are:")
	print(polarity_frame.describe())
	print("The subjectivity figures are:")
	print(subjectivity_frame.describe())

def print_indiv_tweet_polarity_subjective(full_tweet_texts, polarity, subjectivity):
	for x in range(len(full_tweet_texts)):
		print("The tweets reads\n: {}".format(full_tweet_texts[x]))
		print("The polarity of the tweet is: {}".format(sentiment.polarity[x]))
		print("The subjectivity of the tweet is: {}".format(sentiment.subjectivity[x]))
		print("----------")

def pull_sentiment_polar_subjective(full_tweet_texts):
	polarity, subjectivity = [], []
	for x in range(len(full_tweet_texts)):
		testing = TextBlob(full_tweet_texts[x])
		sentiment = testing.sentiment
		polarity.append(sentiment.polarity)
		subjectivity.append(sentiment.subjectivity)
	return polarity, subjectivity


if __name__ == "__main__":
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		file_name = handle_dict[user_name]
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)
		print_avg_polar_subjective(user_name, polarity, subjectivity)
	#If you want individual tweet output and their polar/subjective value
		#print_indiv_tweet_polarity_subjective(full_tweet_texts, polarity, subjectivity)
	#to see how many tweets you have
		#print("The number of tweets is: {}".format(len(polarity)))
	
	"""if want to print out a stat breakdown of polarity & subjectivity"""
		#describe_polar_subjective(polarity, subjectivity)
		#print_avg_polar_subjective(polarity, subjectivity)

