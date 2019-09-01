import sys
from tweet_stats import item_extract
from extract_tweets_full import full_tweet_sentiment
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from candidate_dictionary import candidates
"""
	The API has trouble extracting Favorites for some reason - 
		according to the documentation --> remove those items
		that have a zero favorite value
"""

def determine_coeff(favorites, retweets, polarity, subjectivity, user_name, coeff_dict):
	stats = pd.DataFrame(
		{'favorites': favorites,
		'retweets' : retweets,
		'polarity' : polarity,
		'subjectivity' : subjectivity
		})
	meow = stats.loc[stats.favorites > 0]	
	meow = meow.loc[stats.retweets > 0]	
	#print_coeff(meow, user_name)
	one_dict = store_coeff(meow)
	coeff_dict[user_name] = one_dict

def store_coeff(df):
	hmm = {}
	hmm["fav-subj"] = np.corrcoef(df['favorites'], df['subjectivity'])[0, 1]	
	hmm["rts-subj"] = np.corrcoef(df['retweets'], df['subjectivity'])[0, 1]
	hmm["fav-pol"] = np.corrcoef(df['favorites'], df['polarity'])[0, 1]
	hmm["rts-pol"] = np.corrcoef(df['retweets'], df['polarity'])[0, 1]
	return hmm

def print_coeff(df, user_name):
	print("\nWhen considering {}:\n".format(candidates[user_name]))
	print("The correl coef of SUBJECTIVITY with:")
	print("-----Favorites:")
	print(np.corrcoef(df['favorites'], df['subjectivity'])[0, 1])
	print("-----retweets:")
	print(np.corrcoef(df['retweets'], df['subjectivity'])[0, 1])
	print('\n')
	print("The correl coef of POLARITY with:")
	print("-----Favorites:")
	print(np.corrcoef(df['favorites'], df['polarity'])[0, 1])
	print("-----retweets:")
	print(np.corrcoef(df['retweets'], df['polarity'])[0, 1])
	print("--"*30)

if __name__ == "__main__":
	faves, rts, pol, subj = [], [], [], []
	coeff_dict = {}
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		favorites, retweets = item_extract(user_name)
		polarity, subjectivity = full_tweet_sentiment(user_name)
		determine_coeff(favorites, retweets, polarity, subjectivity, user_name, coeff_dict)
		#faves.extend(favorites)
		#rts.extend(retweets)
		#pol.extend(polarity)
		#subj.extend(subjectivity)
	print(coeff_dict.index)
	#determine_coeff(favorites, retweets, polarity, subjectivity, user_name)

	#corr = stats.corr()
	#corr.style.background_gradient(cmap='coolwarm')
	#plt.figure(figsize=(12,7))
	#sns.pairplot(meow, kind='reg', height=1.5, aspect=1,
	#			vars= ["favorites", 'retweets', 'polarity', 'subjectivity'])
	#plt.yticks(rotation=0)
	#plt.xticks(rotation=90)
	#plt.scatter(meow['favorites'], meow['subjectivity'])
	#plt.show()
