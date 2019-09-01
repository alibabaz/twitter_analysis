from twitter_client import get_twitter_client
import tweepy

#will pull tweets as they are posted

class StreamListener(tweepy.StreamListener):
	def on_status(self, status):
		#only pull them if the poster has @ least 5 followers
		if status.user.followers_count is None or status.user.followers_countx < 5:
			return
		print(status.text)

	def on_error(self, status_code):
		#if 420 error - have an authentication issue, stop running!!!
		if status_code == 420:
			return False
		else:
			print(status_code)


if __name__ == '__main__':
	api = get_twitter_client()
	stream_listener = StreamListener()
	stream = tweepy.Stream(auth= api.auth, listener=stream_listener)
	stream.filter(track=['trump'])