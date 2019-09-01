import sys
import json
from datetime import datetime


"""Pull the date for each tweet & format into python 
date-time format so can plot"""

def get_text(tweet):
	text = tweet.get('created_at', [])
	return text

def text_extract(file_name):
	with open(file_name, 'r') as f:
		tweet_text = []
		for line in f:
			tweet = json.loads(line)
			text = get_text(tweet)
			tweet_text.append(text)
		return tweet_text

def extract_and_format_date(full_date):
	year = full_date[-4:]
	month_day = full_date[4:10]
	date = month_day + " " + year
	return datetime.strptime(date, '%b %d %Y')


if __name__ == "__main__":
	file_name = sys.argv[1]
	full_tweet_texts = text_extract(file_name)
	for x in range(5):
		full_date = full_tweet_texts[x]
		date_formatted = extract_and_format_date(full_date)
		full_tweet_texts[x] = date_formatted
	print(len(full_tweet_texts))
	print(full_tweet_texts[-1])