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

def store_data(feature_matrix):
	# Stores the feature_matrix to the data.txt file
	with open('storage/data.txt', 'w') as file:
		for row in feature_matrix:
			length = len(row)
			for i in range(length):
				if i == 0:
					file.write(str(row[i]))
				else:
					file.write(' ')
					file.write(str(row[i]))
			file.write("\n")

def read_data():
	# Reads the feature_matrix from the data.txt file
	count = 0
	file = open('storage/data.txt', 'r')
	for line in file:
		count += 1

	print(count)
	features_matrix = np.zeros((count, 3000))

	with open('storage/data.txt', 'r') as file:
		count = 0
		for row in file:
			i = 0
			test = row.split(" ")
			# print(test)
			for item in test:
				features_matrix[count][i] = float(item)
				i += 1 
			count += 1

	return features_matrix

def extract_features(directory, dictionary):
	files = [os.path.join(directory,file) for file in os.listdir(directory)]

	# Create the matrix to store the features
	features_matrix = np.zeros((len(files), 3000))
	# print(features_matrix)

	docID = 0
	# traceback = [] #This is used to correlate words for the feedback

	for emails in files:
		with open(emails, encoding="latin-1") as email:
			for line in email:
				words = line.split() # Create list of words on a line
				for word in words:
					wordID = 0
					for i,d in enumerate(dictionary): # Here i is the index and d is the word
						if d[0] == word: # d[0] is the word, d[1] is the frequency.
							wordID = i
							# traceback[i] = d[0]
							features_matrix[docID, wordID] = 1 # Set the occurrence of that word.
							# features_matrix[docID, wordID] = word.count(word) # Original sets the frequency

			docID += 1 #Increment the index to indicate which email we are at.

	store_data(features_matrix)
	return features_matrix

def extract_features_single(file, dictionary):

	# Create the matrix to store the features
	features_vector = np.zeros(3000)
	# print(features_matrix)

	with open(file, encoding="latin-1") as email:
		for line in email:
			words = line.split() # Create list of words on a line
			for word in words:
				wordID = 0
				for i,d in enumerate(dictionary): # Here i is the index and d is the word
					if d[0] == word: # d[0] is the word, d[1] is the frequency.
						wordID = i
						features_vector[wordID] = 1 # Set the occurrence of that word.

	print(features_vector)
	return features_vector # Singular feature vector for email. 



