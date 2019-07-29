import os
import sys
from tweepy import API
from tweepy import OAuthHandler
import config


#responsible for authentication - just use get_twitter_client in calls

def get_twitter_auth():

	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	return auth

#create instance of tweepy.API -> used for interactions w/twitter
def get_twitter_client():
	"""Set up twitter API client --> return a tweepy.API object"""

	auth = get_twitter_auth()
	client = API(auth)
	return client
