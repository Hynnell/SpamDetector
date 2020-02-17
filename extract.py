from collections import Counter
import os
import numpy as np

def count_words(directory):
	emails = [os.path.join(directory,file) for file in os.listdir(directory)] 
	track_words = []
	for email in emails:
		with open(email, encoding="latin-1") as email:
			for line in email:
				words = line.split() # Create list of words on a line
				track_words += words # Add each word to total count

	count_words = Counter(track_words) # Count frequency of each word

	# This portion removes unwanted features:
	# meaningless words, non-alphabetic characters...
	words = list(count_words.keys())

	for elem in words:
		if len(elem) == 1 or len(elem) == 2: # Remove stop words.
			del count_words[elem]
		if elem.isalpha() == False: # Remove non-alphabetical words.
			del count_words[elem]

	count_words = count_words.most_common(3000) # Take the most common 3000 words
	# print(count_words)
	return count_words

def extract_features(directory, dictionary):
	files = [os.path.join(directory,file) for file in os.listdir(directory)]
	features_matrix = np.zeros((len(files), 3000)) # Generate size of matrix containing vectors.
	docID = 0
	test = []
	for emails in files:
		with open(emails, encoding="latin-1") as email:
			for line in email:
				words = line.split() # Create list of words on a line
				for word in words: # Ok 
					wordID = 0
					for i,d in enumerate(dictionary):
						if d[0] == word:
							l = [d[0], i]
							test.append(l)
							wordID = i
							features_matrix[docID, wordID] = words.count(word)
			docID += 1

	# print("Length of features matrix:", len(features_matrix))
	return features_matrix



