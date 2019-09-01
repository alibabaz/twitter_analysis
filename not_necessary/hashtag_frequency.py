import sys
from collections import Counter
import json

#will print out the 20 most common hashtags of whatever json file fed
""""Use tweet.get instead of tweet['entities'] - bc entities is
			optional, so if trying to access directly, could get KeyError"""

def get_hashtags(tweet):
	#will pull entities key - if not there will return empty dict
	entities = tweet.get('entities', {}) 
	#will pull value for hashtag key - return empty list if not available
	hashtags = entities.get('hashtags', []) 
	return [tag['text'].lower() for tag in hashtags]

if __name__ == '__main__':
	fname = sys.argv[1]
	with open(fname, 'r') as f:
		hashtags = Counter()
		for line in f:
			tweet = json.loads(line)
			hashtags_in_tweet = get_hashtags(tweet)
			hashtags.update(hashtags_in_tweet)
		for tag, count in hashtags.most_common(20):
			print("{}: {}".format(tag, count))