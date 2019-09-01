import sys
import json
import os
from tweepy import Cursor
from twitter_client import get_twitter_client
from handle_file_dict import handle_dict

root = 'timelines/'

def pull_timeline(user_name):
	client = get_twitter_client()

	file_name = "tweets_{}.json".format(user_name)

	path = os.path.join(root + file_name)

	if user_name not in handle_dict:
		print("You're going to want to add this to handle_file_dict:\n")
		print("'{}' : '{}'".format(user_name, file_name))

	with open(path, 'w') as f:
		for page in Cursor(client.user_timeline, screen_name=user_name,
					tweet_mode='extended', count=200).pages():
			for status in page:
				f.write(json.dumps(status._json)+'\n')
	return file_name


if __name__ == '__main__':
	#twiter handle should be provided as argument
	user_name = sys.argv[1]
	pull_timeline(user_name)
