	plt.figure(figsize=(12,7))

	for x in range(1, len(sys.argv)):
		file_name = sys.argv[x]
		user_name = extract_user_name(file_name)
		full_tweet_texts = text_extract(file_name)
		polarity, subjectivity = pull_sentiment_polar_subjective(full_tweet_texts)

	#If you want individual tweet output and their polar/subjective value
		#print_indiv_tweet_polarity_subjective(full_tweet_texts, polarity, subjectivity)

	#to see how many tweets you have
		#print("The number of tweets is: {}".format(len(polarity)))
		plt.subplot(2, 2, x)
		plt.scatter(subjectivity, polarity, s=15, alpha=0.5, cmap='viridis')
		plt.title("{}".format(candidates[user_name]), fontsize= 14, 
							fontweight='heavy', color='blue')
		plt.xlabel("Subjectivity", fontsize=6, labelpad=-2, fontweight='heavy')
		plt.ylabel("Polarity", fontsize=6, labelpad=-2, fontweight='heavy')
		plt.xticks(fontsize=6)
		plt.yticks(fontsize=6)

	plt.subplots_adjust(hspace=0.3, left=0.04, right=0.97,
					bottom=0.06)
	plt.show()
	