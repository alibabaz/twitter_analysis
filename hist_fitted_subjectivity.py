import sys
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import text_extract
from extract_tweets_full import pull_sentiment_polar_subjective
import numpy as np

def hist_fitted_subject(one, two, three):
	plt.figure(figsize=(12,7))

	users = [one, two, three]
	colors = ['red', 'green', 'blue']

	for x in range(0, 3):
		user_name = users[x]
		file_name = handle_dict[user_name]
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)
		
		array = np.array(subjectivity)
		removed_zero = array[array != 0]
		sns.distplot(removed_zero, label=candidates[user_name], 
								color=colors[x])

	plt.xlabel("Subjectivity")
	plt.title("Subjectivity Curve Comparison\n {} vs {} vs {}".format(candidates[sys.argv[1]],
						candidates[sys.argv[2]], candidates[sys.argv[3]]))
	plt.legend()
	plt.show()

if __name__ == "__main__":
	users = []
	for x in range(1, len(sys.argv)):
		users.append(sys.argv[x])
	hist_fitted_subject(users[0], users[1], users[2])