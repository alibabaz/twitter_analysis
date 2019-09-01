import sys
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import text_extract
from extract_tweets_full import pull_sentiment_polar_subjective
from extract_tweets_about_trump import extract_about_trump


"""
	Scatter plots of ONE user showing sentiment 
		of all retrievable tweets vs those a/b Trump
	Can call multiple users - kill plot each time and
		new one will generate
"""

def provide_sentiment(user_name, about_trump):
	if about_trump:
		polarity, subjectivity = extract_about_trump(user_name)
	else:
		file_name = handle_dict[user_name]
		full_tweets = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweets)

	return polarity, subjectivity

def plot_scatter(user_name):
	polarity, subjectivity = provide_sentiment(user_name, about_trump=False)
	plt.scatter(subjectivity, polarity, s=15, alpha= 0.3, color ='blue')

	specific_pol, specific_subj = provide_sentiment(user_name, about_trump=True)
	plt.scatter(specific_subj, specific_pol, s=20, alpha=0.5, color='red')

	title_scat = "Sentiment Analysis: With & Without Mentioning 'Trump"
	plt.title( ("{} ".format(candidates[user_name]) + title_scat) ,
					fontweight='heavy', color='green', fontsize=20)
	
	plt.xlabel("Subjectivity", fontsize=6, fontweight='heavy',labelpad=0)
	plt.ylabel("Polarity", fontsize=6, fontweight='heavy', labelpad=0)


if __name__ == "__main__":
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		plt.figure(figsize=(12,7))
		plot_scatter(user_name) 
		plt.show()