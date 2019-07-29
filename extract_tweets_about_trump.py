import sys
import json
from candidate_dictionary import candidates
from handle_file_dict import handle_dict
from extract_tweet_content import pull_sentiment_polar_subjective
from extract_tweet_content import print_avg_polar_subjective

def get_text(tweet):
	text = tweet.get('full_text', [])
	return text

def text_extract(file_name):
	with open(file_name, 'r') as f:
		tweet_text = []
		for line in f:
			tweet = json.loads(line)
			text = get_text(tweet)
			tweet_text.append(text)
	return tweet_text

def extract_about_trump(user_name):
	file_name = handle_dict[user_name]
	full_tweet_texts = text_extract(file_name)
	found = []
	for x in range(len(full_tweet_texts)):
		if "Trump" in full_tweet_texts[x]:
			found.append(full_tweet_texts[x])
	polarity, subjectivity = pull_sentiment_polar_subjective(found)
	#print_avg_polar_subjective(user_name, polarity, subjectivity)
	return polarity, subjectivity

if __name__ == "__main__":
	for x in range(1, len(sys.argv)):
		extract_about_trump(sys.argv[x])
