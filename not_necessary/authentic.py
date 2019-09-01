import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import config

#Check the authentication works and then search for mueller items

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='mueller').items(10):
	print(tweet.text) 
	
	print("<------------->")