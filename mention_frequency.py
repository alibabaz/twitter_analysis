import sys
import os
from collections import Counter
import json
from handle_file_dict import handle_dict

""" Shows who/what a user is mentioning most often"""
root = "timelines/"

def get_mentions(tweet):
	entities = tweet.get('entities', {})
	hashtags = entities.get('user_mentions', [])
	return [tag['screen_name'] for tag in hashtags]

def mention_freq(file_name):
	path = os.path.join(root + file_name)
	with open(path, 'r') as f:
		users = Counter()
		top_mentions = []
		for line in f:
			tweet = json.loads(line)
			mentions_in_tweet = get_mentions(tweet)
			users.update(mentions_in_tweet)
		for user, count in users.most_common(20):
			top_mentions.append([user, count])
		return top_mentions

if __name__ == "__main__":
	user_name = sys.argv[1]
	file_name = handle_dict[user_name]
	most_mentions = mention_freq(file_name)
	print(most_mentions)