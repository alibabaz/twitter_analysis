import sys
import os
import json
from candidate_dictionary import candidates
from handle_file_dict import handle_dict
from twitter_client import get_twitter_client


root = 'timelines/'

def get_retweets(tweet):
	retweets = tweet.get('retweet_count', [])
	#print("The number of retweets is: {}".format(retweets))
	return retweets

def get_favorites(tweet):
	favorites = tweet.get('favorite_count', [])
	#print("The number of favorites is: {}".format(favorites))
	return favorites

#returns a list with all id's for tweets
def item_extract(user_name):
	file_name = handle_dict[user_name]
	path = os.path.join(root + file_name)
	with open(path, 'r') as f:
		favorite_count, retweet_count = [], []
		for line in f:
			tweet = json.loads(line)
			retweets = get_retweets(tweet)
			favorites = get_favorites(tweet)
			retweet_count.append(retweets)
			favorite_count.append(favorites)
	return favorite_count, retweet_count


if __name__ == "__main__":
	user_name = sys.argv[1]
	fav, ret = item_extract(user_name)
	#meow, hmmm = item_extract(user_name, tweet_identifiers[0:10])