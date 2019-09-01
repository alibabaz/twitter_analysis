import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

"""Pull the max number of tweets API will allow from a given user
	store in json format
"""

def pull_timeline(user):
	client = get_twitter_client()

	file_name = "tweets_{}.json".format(user)

	with open(file_name, 'w') as f:
		for page in Cursor(client.user_timeline, screen_name=user,
					count=200).pages():
			for status in page:
				f.write(json.dumps(status._json)+'\n')
	return file_name


if __name__ == '__main__':
	#twiter handle should be provided as argument
	user = sys.argv[1]
	pull_timeline(user)
