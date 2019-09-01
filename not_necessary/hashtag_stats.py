import sys
from collections import defaultdict
import json

""" Shows stats of how the hashtag frequency of a user breaksdown"""
def get_hashtags(tweet):
	entities = tweet.get('entities', {})
	hashtags = entities.get('hashtags', [])
	return [tag['text'].lower() for tag in hashtags]

def extract_counts(file):
	hashtag_count = defaultdict(int)
	with open(file, 'r') as file_name:
		for line in file_name:
			tweet = json.loads(line)
			hashtags_in_tweet = get_hashtags(tweet)
			n_of_hashtags = len(hashtags_in_tweet)
			hashtag_count[n_of_hashtags] += 1
	return hashtag_count

def usage():
	print("Usage:")
	print("python {} <filename.json>".format(sys.argv[0]))

def calc_tweets_with_hashtags(hashtag_count):
	return sum([count for n_of_tags, count in hashtag_count.items() if n_of_tags > 0])

def calc_tweets_without_hashtags(hashtag_count):
	return hashtag_count[0]

def total_tweets(t_wo_h, t_w_h):
	return t_wo_h + t_w_h


def print_initial_info(tweets_total, tweets_no_hashtags, tweets_no_hashtags_percent,
							tweets_with_hashtags, tweets_with_hashtags_percent):
	print("Total tweets: {}".format(tweets_total))
	print("{} tweets without hashtags ({}%)".format(tweets_no_hashtags,
							tweets_no_hashtags_percent))
	print("{} tweets w/ @ least 1 hashtag ({}%)".format(tweets_with_hashtags,
								tweets_with_hashtags_percent))

def print_hashtag_breakdown(hashtag_count):
	for tag_count, tweet_count in sorted(hashtag_count.items()):
		if tag_count > 0:
			percent_of_total_tweets = "%.1f" % (tweet_count / 
									tweets_total * 100)
			percent_of_hashtagged_tweets = "%.1f" % (tweet_count /
								tweets_with_hashtags * 100)
			print("{} tweets with {} hashtags ({}% of total tweets, {}% of hashtagged tweets)".format(tweet_count, 
						tag_count, percent_of_total_tweets, percent_of_hashtagged_tweets)) 

if __name__ == '__main__':
	file_name = sys.argv[1]
	hashtag_count = extract_counts(file_name)

	tweets_with_hashtags = calc_tweets_with_hashtags(hashtag_count)
	tweets_no_hashtags = calc_tweets_without_hashtags(hashtag_count)
	
	tweets_total = total_tweets(tweets_no_hashtags, tweets_with_hashtags)

	tweets_with_hashtags_percent = "%.1f" % (tweets_with_hashtags/ tweets_total * 100)
	tweets_no_hashtags_percent = "%.1f" % (tweets_no_hashtags / tweets_total * 100)

	print("\n---------------")
	print_initial_info(tweets_total, tweets_no_hashtags, tweets_no_hashtags_percent,
						tweets_with_hashtags, tweets_with_hashtags_percent)
	print("--------------")
	print_hashtag_breakdown(hashtag_count)
	print("\n")