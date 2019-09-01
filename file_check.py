import sys
import os
import json
from textblob import TextBlob
import pandas as pd
from candidate_dictionary import candidates
from handle_file_dict import handle_dict

def get_text(tweet):
	text = tweet.get('text', [])
	return text

def text_extract(file_name):
	root = "timelines/older_timelines/"
	path = os.path.join(root + file_name)
	print(path)
	with open(path, 'r') as f:
		tweet_text = []
		for line in f:
			tweet = json.loads(line)
			text = get_text(tweet)
			tweet_text.append(text)
	return tweet_text

if __name__ == "__main__":
	file_name = "user_timeline_sensanders.json"
	meow = text_extract(file_name)
	print(meow[0])
	print('finished')