#Prints the first ten items from timeline to terminal

from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':	
	client = get_twitter_client()

	"""status variable is instance of tweepy.Status (model used by
			Tweepy to wrap statuses aka tweets)"""
	for status in Cursor(client.home_timeline).items(10):
		print(status.text)
		print("-----------------")