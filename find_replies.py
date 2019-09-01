import sys
import os
import json
from candidate_dictionary import candidates
from handle_file_dict import handle_dict
from twitter_client import get_twitter_client

"""
Trying to pull out the number of replies a tweet has
Need to use the twitter search API feature
Provide the "@user" to be queried
Provide the tweet id for each tweet
	for tweets that match these two criteria - add to counter
"""

#First create a new get_text - pulls all the tweet ID #s

root = 'timelines/'

def get_id(tweet):
	identifier = tweet.get('id', [])
	return identifier

#returns a list with all id's for tweets
def id_extract(user_name):
	file_name = handle_dict[user_name]
	path = os.path.join(root + file_name)
	with open(path, 'r') as f:
		tweet_ids = []
		for line in f:
			tweet = json.loads(line)
			identifier = get_id(tweet)
			tweet_ids.append(identifier)
	return tweet_ids

def find_reply_count(user_name, tweet_ids):
	client = get_twitter_client()
	searched_tweets = [status for status in ]

if __name__ == "__main__":
	user_name = sys.argv[1]
	tweet_identifiers = id_extract(user_name)
	meow = find_reply_count(user_name, tweet_identifiers[0:10])
