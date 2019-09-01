import sys
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweet_content import text_extract
from extract_tweet_content import pull_sentiment_polar_subjective

if __name__ == "__main__":
	plt.figure(figsize=(12,7))

	colors = ['red', 'blue']
	markers = ['x', '+']
	label = ['first', 'second']
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		file_name = handle_dict[user_name]
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)

		label[x-1] = plt.scatter(subjectivity, polarity, edgecolors='none',
				norm=0.2, alpha=0.25, c=colors[x-1], marker=markers[x-1])

	plt.xlabel("Subjectivity", fontsize=12, labelpad=-2, fontweight='heavy')
	plt.ylabel("Polarity", fontsize=12, labelpad=-2, fontweight='heavy')
	plt.title("Sentiment Comparison of {} vs. {}".format(candidates[sys.argv[1]],
						candidates[sys.argv[2]]), fontweight="heavy")
	plt.legend((label[0], label[1]),
		(sys.argv[1], sys.argv[2]), 
		loc='lower left', fontsize=10)

	plt.show()