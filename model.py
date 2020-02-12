from collections import Counter
import os
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


'''
TODO: 

- Verify feature extraction works
- Test on sample data (currently takes a very long time to run)
- Refine text
- Connect to GUI
- Train the app so it doesnt need to be trained each time. 
- Support single email submission
'''

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


def main():
	# Test Email
	'''
	Lingspam_public data set
		- 4 categories
		- 10 parts each
		- Each part has 48 spam and 242 ham
	'''

	# File paths
	training2 = "./data/lingspam_public/bare/part1"
	testing1 = './data/lingspam_public/bare/part1'
	
	# =========================== TRAINING ===========================

	dictionary = count_words(training2) #Creates a dictionary containing frequencies of words.
	
	# Creating our labels, 1 indicates spam, 0 indicates ham
	train_labels = np.zeros(289)
	train_labels[241:288] = 1
	train_matrix = extract_features(training2, dictionary)
	
	# Initialize models
	model1 = LinearSVC()
	model2 = MultinomialNB()

	# Fitting the models for later use
	model1.fit(train_matrix, train_labels)
	model2.fit(train_matrix, train_labels)

	# ================================================================


	# ============================ TESTING ===========================
	# Testing unseen data
	test_matrix = extract_features(testing1, dictionary)
	
	# Creating our labels, 1 indicates spam, 0 indicates ham
	test_labels = np.zeros(289)
	test_labels[241:288] = 1

	result1 = model1.predict(test_matrix)
	result2 = model2.predict(test_matrix)

	# ================================================================


	# ============================ RESULTS ===========================
	'''
	Notes about the confusion matrix: 

	In binary classification, the count of:
	true negatives is C[0,0] <- want this high
	false negatives is C[1,0]
	true positives is C[1,1] <- want this high
	false positives is C[0,1].
	'''

	# Results for LinearSVC() model
	c1 = confusion_matrix(test_labels,result1)
	c1_acc = (c1[0,0] + c1[1,1])/len(test_labels)
	print("Support Vector Classification Accuracy:", c1_acc)

	# Results for MultinomialNB() model
	c2 = confusion_matrix(test_labels,result2)
	c2_acc = (c2[0,0] + c2[1,1])/len(test_labels)
	print("Naive Bayes Accuracy:", c2_acc)

	# ================================================================


if __name__ == '__main__':
	main()



