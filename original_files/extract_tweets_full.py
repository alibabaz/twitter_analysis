import sys
import json
import os
from textblob import TextBlob
from candidate_dictionary import candidates
from handle_file_dict import handle_dict

"""Just pull the full text do sentiment analysis - return
	polarity & subjectivity values - this is NOT selecting
	for tweets that have "trump" in them
"""
root = 'timelines/'

def get_text(tweet):
	text = tweet.get('full_text', [])
	return text

def text_extract(file_name):
	path = os.path.join(root + file_name)
	with open(path, 'r') as f:
		tweet_text = []
		for line in f:
			tweet = json.loads(line)
			text = get_text(tweet)
			tweet_text.append(text)
	return tweet_text


def pull_sentiment_polar_subjective(full_tweet_texts):
	polarity, subjectivity = [], []
	for x in range(len(full_tweet_texts)):
		testing = TextBlob(full_tweet_texts[x])
		sentiment = testing.sentiment
		polarity.append(sentiment.polarity)
		subjectivity.append(sentiment.subjectivity)
	return polarity, subjectivity

def full_tweet_sentiment(user_name):
	file_name = handle_dict[user_name]
	full_tweet_texts = text_extract(file_name)
	polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)
	#print_avg_polar_subjective(user_name, polarity, subjectivity)
	return polarity, subjectivity

def extract_about_topic(user_name, topic):
	file_name = handle_dict[user_name]
	full_tweet_texts = text_extract(file_name)
	found = []
	for x in range(len(full_tweet_texts)):
		if topic in full_tweet_texts[x]:
			found.append(full_tweet_texts[x])
	polarity, subjectivity = pull_sentiment_polar_subjective(found)
	#print_avg_polar_subjective(user_name, polarity, subjectivity)
	return polarity, subjectivity


if __name__ == "__main__":
	for x in range(1, len(sys.argv)):
		polarity, subjectivity = full_tweet_sentiment(sys.argv[x])
		print(len(polarity))