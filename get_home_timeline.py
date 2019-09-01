#Instead of printing onto terminal - way to store tweets retrieved
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
	client = get_twitter_client()

	with open('home_timeline.json', 'w') as f:
		for page in Cursor(client.home_timeline, count=200).pages(4):
			for status in page:
				f.write(json.dumps(status._json)+"\n")
