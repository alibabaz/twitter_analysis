import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import config

#Check the authentication works and then search for mueller items

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)


#overrite tweepy.StreamListener to add logic to on_status

class MyStreamListener(tweepy.StreamListener):
	def on_data(self, data):
		print(data)
		print("------")
		return True


myStreamListener = MyStreamListener()
myStream = Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['mueller'], is_async=True)