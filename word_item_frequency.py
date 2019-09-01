import sys
import string
import json
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
	text = text.lower()
	tokens = tokenizer.tokenize(text)
	return [token for token in tokens if token not in stopwords
							and not token.isdigit()]

def word_freq(file_name):
	tweet_tokenizer = TweetTokenizer()
	punct = list(string.punctuation)
	letters = list(string.ascii_letters)
	stopword_list = stopwords.words('english') + punct + ['rt', 'via', "'"]									
	word_tracker = []
	tf = Counter()
	with open(file_name, 'r') as f:
		for line in f:
			tweet = json.loads(line)
			tokens = process(text=tweet['text'],
							tokenizer=tweet_tokenizer,
							stopwords=stopword_list)
			tf.update(tokens)
		for tag, count in tf.most_common(30):
			#will take care of the weird punctuations not found before
			if (list(tag)[0]) in letters:
				word_tracker.append([tag, count])
	return word_tracker

if __name__ == '__main__':
	file_name = sys.argv[1]
	word_freq(file_name)