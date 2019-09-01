import sys
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from handle_file_dict import handle_dict
from candidate_dictionary import candidates
from extract_tweets_full import full_tweet_sentiment
from extract_tweets_full import pull_sentiment_polar_subjective
from extract_tweets_about_trump import extract_about_trump
import pandas as pd


def get_sentiment(user):
	polarity, subjectivity = full_tweet_sentiment(user)
	user_x = ["{}".format(user)] * len(polarity)
	pol = [polarity, user_x]
	subj = [subjectivity, user_x]
	#print(pol[0])

	return pol, subj

def violin_plot_control(users, coords):
	pol_final, subj_final = [], []
	for user in users:
		pol_mapped, subj_mapped = get_sentiment(user) 
		pol_final.append(pol_mapped)
		subj_final.append(subj_mapped)
		print("one polarity is:")
		print(len(pol_final[0][0]))
		print("---------")
	print(len(subj_final))
	#data_polarity = pd.DataFrame(zip(polarity, user_x),
								#columns=['polarity', 'user_x'])
	#data_subjectivity = pd.DataFrame(zip(subjectivity, user_x), 
								#columns=['subjectivity', 'user_x'])
	#sns.violinplot(x='user_x', y='polarity', data=data_polarity,
								#label="polarity", ax=ax[coords_1[0], coords_1[1]])
	#sns.violinplot(x='user_x', y='subjectivity', data=data_subjectivity,
								#label='subjectivity', ax=ax[coords_2[0], coords_2[1]])


if __name__ == "__main__":
	users, z = [], 0
	#fig, ax = plt.subplots(2, 2, figsize=(12,7))
	axis_coord= [ [0,0], [1,0], [0,1], [1,1] ]
	for x in range(1, len(sys.argv)):
		user_name = sys.argv[x]
		users.append(user_name)
	violin_plot_control(users, axis_coord)
	
	#plt.show()
